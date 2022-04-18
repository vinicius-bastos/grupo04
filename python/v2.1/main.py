
from ast import Nonlocal
from datetime import datetime
import re
import time
import tracemalloc
import config as sql

cidade_atual = "SP"
def transactions(cursor,init,final,step):
    global cidade_atual
    transaction = []
    lista = []
    lista_tempo = []
    lista_memoria = []
    # Criação dos valores do Range
    for n in range(init,final,step):
        lista.append(n)
    tracemalloc.start()
    tempo_inicial = (time.time())
    # Inserção dos valores, pegando o tempo e o espaço ocupado na memória.
    while(lista != []):
        transaction.append(lista.pop())
        lista_memoria.append(tracemalloc.get_traced_memory()[0])
        tempo_final = (time.time()) - tempo_inicial
        lista_tempo.append(tempo_final)
    tracemalloc.stop()
    orderedTranscation = [num for num in reversed(transaction)]
    # Inserção no Banco
    tempo_inical_insercao = (datetime.now())
    while(orderedTranscation!= []):
        transac = orderedTranscation.pop()
        tempo = lista_tempo.pop()
        memoria = lista_memoria.pop()
        print("Inserido o valor no banco de dados: transaction = {}, tempo = {}, memoria = {}".format(transac,tempo,memoria))
        sql.insert(cursor, 
                   transac,
                   tempo,
                   memoria)
    tempo_total_insercao =  (datetime.now()) - tempo_inical_insercao
    print("tempo inicial de inserção:" + str(tempo_inical_insercao))
    print("tempo final de inserção:" + str(datetime.now()))
    print("Tempo de total inserção: {}".format(tempo_total_insercao))
    sql.insert_info(cursor, cidade_atual, len(transaction),tempo_inical_insercao, tempo_total_insercao)
    
    
def cenario(cursor):
    global cidade_atual
    valor = int(input("Escolha um cenário \n 1. [100_000,600_000,100_000] \n 2. [1_000,6_000,100] \n 3. [100,600,10] \n 4. [10,60,10] \n 5. [1_000_000,6_000_000,1_000_000] \n 6. Personalizado \n 7. Alterar cidade de inserção \n 8. Select \n 9. Sair \n"))
    if valor == 1:
        return  transactions(cursor,100_000,600_000,100_000)
    if valor == 2:
        return transactions(cursor,1_000,6_000,100)
    if valor == 3:
        return  transactions(cursor,100,600,100)
    if valor == 4:
        return  transactions(cursor,10,60,10)
    if valor == 5:
        return transactions(cursor,1_000_000,6_000_000,1_000_000)
    if valor == 6:
        dado_inicial = int(input("Digite o valor inicial: "))
        dado_final = int(input("Digite o valor final: "))
        dado_passo = int(input("Digite o valor do passo: "))
        return transactions(cursor,dado_inicial,dado_final,dado_passo)
    if valor == 7:
        cidade_atual = input("Digite o nome da cidade: ")
        return
    if valor == 8:
        select(cursor)
        return
    if valor == 9:
        return False
    print("Opção inválida")

def select(cursor):
    valor = int(input("Escolha um cenário \n 1. Seleciona todos os valores da tabela dados \n 2. Seleciona todos os valores da tabela dados_info \n 3. Sair \n"))
    if valor == 1:
        sql.select_dados(cursor)
    if valor == 2:
        sql.select_dados_info(cursor)
    if valor == 3:
        return

def main():
    cnx,cursor = sql.conn()
    while(cenario(cursor) != False):
        cnx.commit()
        pass
    sql.desconect(cnx,cursor)
    
if __name__ == "__main__":
    main()
