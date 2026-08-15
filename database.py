import mysql.connector
from config import DB_CONFIG
def connect(): return mysql.connector.connect(**DB_CONFIG)
def save(name,skill,ai,final):
 c=connect();cur=c.cursor()
 cur.execute("INSERT INTO candidates(name,skill_score,ai_score,final_score) VALUES(%s,%s,%s,%s)",(name,skill,ai,final));c.commit();c.close()
