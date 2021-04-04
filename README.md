# Pipeline ETL para la base de datos Sales

Este es un proyecto para la materia de Inteligencia de Negocios en el Instituto tecnológico de Matamoros.   

Creado por:
- Brandon Alejandro Esquivel Rivas
- Cassandra Ayde González Vega
- Nicole Rodríguez González
- Víctor Hugo Vázquez Gómez

El proyecto lleva a cabo una extracción, transformación y carga de datos de una base de datos de ventas a un data warehouse usando en ambas bases de datos la tecnología de PostgreSQL.

# Descarga

Puedes hacer un fork o un `git clone` con las opciones que proporciona GitHub o también descargarlo directamente [aquí](https://github.com/VHugoBarnes/proyecto-etl/releases/tag/v1.0).

# Requerimientos

Esta proyecto utiliza la version de Python 3.8 y los paquetes de pip que ocupa de momento son:   

```
    psycopg2
    pygrametl
```

# Ejecución

Puedes ejecutar el proyecto siempre y cuando tengas las dos bases de datos hechas. Si no tienes la base de datos para el datawarehouse abre el archivo `database.sql`, copia y ejecuta la sección para la creación de la base de datos.   

Teniendo las dos bases de datos hechas ya puedes ejecutar el script de la siguiente manera:   

## Si estás con un ambiente virtual (virtualenv o env)

```bash
python src/app.py
```

## Si estás sin ambiente virtual

```bash
python3 src/app.py
```
