import pymysql

conn = pymysql.connect(host="localhost", user="root", password="Shim5186!!", db="new_schema")
curs = conn.cursor()
sql = "select * from new_table"
curs.execute(sql)
rows = curs.fetchall()
print(rows)