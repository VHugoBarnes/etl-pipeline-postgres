#coding: utf-8
import classes.DBConn
from classes.Sales import Sales

if __name__ == '__main__':
    # classes.DBConn.DBConn.connect(filename='salesdb.ini')
    sales = Sales('salesdb.ini')
    print("La cantidad de registros en la tabla card es:", sales.getCardCount())
