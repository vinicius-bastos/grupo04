import mysql.connector
from mysql.connector import errorcode
import tracemalloc
from datetime import date, datetime


def conn():
    try:
        cnx = mysql.connector.connect(host='localhost',database='algas',user='grupo04',password='urubu100')
        print("Conectado ao servidor MySQL versão ")
        cursor = cnx.cursor()
        return cnx,cursor
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
def desconect(cnx,cursor):
    cnx.commit()
    cursor.close()
    cnx.close()

def insert(cursor,lista, tempo_final):
        cursor.execute("""
        INSERT INTO dados (entrada,tempo,memoria, data_insercao)
        VALUES (%d, %.20f,%d,'%s')
        """ % (lista.pop(), tempo_final, tracemalloc.get_traced_memory()[0], datetime.now()))
