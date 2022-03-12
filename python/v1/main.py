
import time
import tracemalloc
import config as sql

def main():
    cnx,cursor = sql.conn()
    transactions(cursor,100,600,10)
    sql.desconect(cnx,cursor)
    
    
def transactions(cursor,init,final,step):
    transaction = []
    tempo_inical = (time.time())
    for n in range(init,final,step):
        transaction.append(n)

    while(transaction != []):
        tracemalloc.start()
        tempo_final = (time.time()) - tempo_inical
        sql.insert(cursor,transaction,tempo_final)
        tracemalloc.stop()
  
if __name__ == "__main__":
    main()
