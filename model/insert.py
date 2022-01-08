import psycopg2

conn = psycopg2.connect(host='localhost', dbname = 'postgres', user='khjoo', password='khjoo', port=5432)

cur = conn.cursor()

# 데이터추가
# for i in range(8,15):
#     i+=1
#     cur.execute("INSERT INTO tb_user VALUES (%s,%s,%s,%s,%s);",
#             (i,'test2','USA',36+i,'m'))
#     print(i)



print("===================================")
cur.execute("select * from tb_user;")
rows = cur.fetchall()
# print(rows)

#튜플 인덱싱하여 출력
# for i in rows: #i는 받아온 테이블정보의 raw 수
#     if i[0]<5:   #튜플 첫번째컬럼이 0부터 4까지(5)라면
#         print(i)  #출력


lst = list(rows)
print(lst[3])
# conn.commit()


    


