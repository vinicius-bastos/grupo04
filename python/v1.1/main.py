
import time
import tracemalloc
import config as sql

def main():
    cnx,cursor = sql.conn()
    transactions(cursor,1,1_000_000,100)
    sql.desconect(cnx,cursor)
    
def transactions(cursor,init,final,step):
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
    while(orderedTranscation!= []):
        sql.insert(cursor, 
                   orderedTranscation.pop(),
                   lista_tempo.pop(),
                   lista_memoria.pop())
    
if __name__ == "__main__":
    main()
