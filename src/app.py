#coding: utf-8
import psycopg2
import pygrametl
from pygrametl.datasources import SQLSource
from pygrametl.tables import Dimension, FactTable

sales_string = "host='localhost' dbname='sales' user='vhugobarnes' password='maliakaka55'"
sales_pgconn = psycopg2.connect(sales_string)

dwh_string = "host='localhost' dbname='sales_dwh' user='vhugobarnes' password='maliakaka55'"
dwh_pgconn = psycopg2.connect(dwh_string)

dw_conn_wrapper = pygrametl.ConnectionWrapper(connection=dwh_pgconn)
