import pymysql
from pymysql import cursors

db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
cursors = db.cursor()

cursors.execute('USE bbs;')
# cursors.execute('INSERT INTO bbs.user(userID,userPassword,userName,userGender,userEmail') VALUES ("999","999","999","999","999")

cursors.execute('SELECT * FROM bbs.user')

# value = cursors.fetchall()
# value = cursors.fetchmany()
# value = cursors.fetchone()
# print(value)

for i in cursors.fetchone():
    print(cursors.fetchone())

    # i+=1
    # cur.execute("INSERT INTO tb_user VALUES (%s,%s,%s,%s,%s);",
    #         (i,'test2','USA',36+i,'m'))


# db.commit()
db.close()
