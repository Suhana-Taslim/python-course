import sqlite3

db = "batBallGame.sqlite"

connection = sqlite3.connect(db)

print("Database opened successfully, " ,connection)

cursr = connection.cursor()

cursr.execute('''
create table if not exists bbg(
              playername text,
              playerage integer,
              score integer
              )
              ''')

name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your score: "))

cursr.execute('''insert into bbg(playername,playerage,score)values(?,?,?)''',(name,age,score))

connection.commit()
print("data has been inserted successfully")

cursr.execute('''select * from bbg''')

print(cursr.fetchall())