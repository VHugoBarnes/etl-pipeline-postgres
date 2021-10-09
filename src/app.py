#coding: utf-8
import psycopg2
import pygrametl
from pygrametl.datasources import SQLSource
from pygrametl.tables import Dimension, FactTable

# Abrir la conexión para la base de datos fuente
sales_string = "host='localhost' dbname='sales' user='vhugobarnes' password='maliakaka55'"
sales_pgconn = psycopg2.connect(sales_string)

# Abrir la conexión para la base de datos destino, crea una conexión de tipo ConnectionWrapper
dwh_string = "host='localhost' dbname='sales_dwh' user='vhugobarnes' password='maliakaka55'"
dwh_pgconn = psycopg2.connect(dwh_string)
dw_conn_wrapper = pygrametl.ConnectionWrapper(connection=dwh_pgconn)

# Extraction
# Creación de las fuentes de datos de la base de datos sales
# query para obtener todos los datos necesarios.
sql = "select ca.card , cl.country, sa.date_sale, cl.gender, cl.job_title, min(sa.sale_paid) as min_sale_paid, max(sa.sale_paid) as max_sale_paid, count(sa.sale_paid) as count_sale_paid, sum(sa.sale_paid) as sum_sale_paid, avg(sa.sale_paid) as avg_sale_paid from sale sa, card ca, client cl where ca.id_card = sa.id_card and cl.id_client = ca.id_client group by ca.card, cl.country, sa.date_sale, cl.gender, cl.job_title, sa.sale_paid order by ca.card, cl.country, sa.date_sale, cl.gender, cl.job_title, sa.sale_paid;"
# el nombre de los campos que genera la query.
name_mapping = 'card', 'country', 'date_sale', 'gender', 'job_title', 'min_sale_paid', 'max_sale_paid', 'count_sale_paid', 'sum_sale_paid', 'avg_sale_paid'
sales_source = SQLSource(connection=sales_pgconn, query=sql, names=name_mapping)

# Data warehouse
# Creamos los objetos para agregar posteriormente los datos al datawarehouse
# Cada objeto tiene sus métodos para asegurarse de que los datos no hayan sido ingresados previamente o para guardarlos
card_dimension = Dimension(
    name='dim_card', # Nombre de la tabla
    key='id_card', # Clave primaria de la tabla
    attributes=['card'] # Atributos de la tabla
)

country_dimension = Dimension(
    name='dim_country',
    key='id_country',
    attributes=['country']
)

date_sale_dimension = Dimension(
    name='dim_date_sale',
    key='id_date_sale',
    attributes=['date_sale']
)

gender_dimension = Dimension(
    name='dim_gender',
    key='id_gender',
    attributes=['gender']
)

job_title_dimension = Dimension(
    name='dim_job_title',
    key='id_job_title',
    attributes=['job_title']
)

fact_table = FactTable(
    name='fact_table',
    keyrefs=['id_date_sale', 'id_card', 'id_gender', 'id_job_title', 'id_country'], # Llaves foraneas
    measures=['min_sale_paid', 'max_sale_paid', 'count_sale_paid', 'sum_sale_paid', 'avg_sale_paid'] # Campos usados para medir
)

# Transformation
# Recorremos cada uno de los datos que genera la query pasada.
for row in sales_source:
    # Nos aseguramos que el dato no haya sido agredado anteriormente.
    row['id_date_sale'] = date_sale_dimension.ensure(row)
    row['id_card'] = card_dimension.ensure(row)
    row['id_gender'] = gender_dimension.ensure(row)
    row['id_job_title'] = job_title_dimension.ensure(row)
    row['id_country'] = country_dimension.ensure(row)

    # Insertar datos en la tabla de hechos.
    fact_table.insert(row)

# Loading
# Con commit nos aseguramos que se hayan guardado los datos y después cerramos la conexión
dw_conn_wrapper.commit()
dw_conn_wrapper.close()

# Cerramos la conexión con la base de datos 'sales'
sales_pgconn.close()

