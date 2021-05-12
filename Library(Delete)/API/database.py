import psycopg2
import json

hostname = ""
username = ""
password = ""
port = ""
db_name = ""
    
def delete(no):
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "DELETE FROM table_name WHERE no = '"+no+"';"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return "Success"
    except:
        return "Error (Delete)"