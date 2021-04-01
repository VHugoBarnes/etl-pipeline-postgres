#coding: utf-8
from classes.DBConn import DBConn

class Sales:

    file_config = ''

    def __init__(self, file) -> None:
        self.file_config = file

    def getCardCount(self):
        cursor = DBConn.connect(filename=self.file_config)
        sql = "SELECT COUNT(*) FROM card;"
        cursor.execute(sql)

        card_count = cursor.fetchone()
        card_count_int = card_count[0]

        return card_count_int
