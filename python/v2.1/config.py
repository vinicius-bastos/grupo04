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

def insert(cursor,transaction, tempo, memoria):
        cursor.execute("""
        INSERT INTO dados (entrada,tempo,memoria, data_insercao)
        VALUES (%d, %.20f,%d,'%s')
        """ % (transaction, tempo, memoria, datetime.now()))

def insert_info(cursor,cidade_atual, leitos_ocupados, data_inicio_insercao, tempo_total_insercao):
        cursor.execute("""
        INSERT INTO infos (cidade, leitos_ocupados, data_inicio_insercao, tempo_execucao)
        VALUES ('%s', %d,'%s','%s')
        """ % (cidade_atual, leitos_ocupados, data_inicio_insercao, tempo_total_insercao))

def select_dados(cursor):   
    cursor.execute("""
    SELECT * FROM dados
    """)
    myResult = cursor.fetchall()
    for x in myResult:
        print(x)

def select_dados_info(cursor):
    cursor.execute("""
    SELECT * FROM infos
    """)
    for (idInfo, cidade, leitos_ocupados, data_inicio_insercao, tempo_execucao) in cursor:
        print("idInfo: %d, Cidade: %s, Leitos ocupados: %d, Data inicio inserção: %s, Tempo total de execução: %s" % (idInfo, cidade, leitos_ocupados, data_inicio_insercao, tempo_execucao))