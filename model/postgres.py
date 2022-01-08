import psycopg2

conn = psycopg2.connect(host='localhost', dbname = 'postgres', user='khjoo', password='khjoo', port=5432)

cur = conn.cursor()


# cur.execute("SELECT * FROM pg_database;")
cur.execute("select * from tb_user;")
rows = cur.fetchall()
# print(rows)
for i in rows:
    print(i)

print("===================================")

    
# cur.execute("INSERT INTO numbers VALUES (%s)", (42,)) # correct

