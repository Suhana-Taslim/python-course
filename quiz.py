# quiz game with sqlite

# def f1():
#    print("hello world")
# f1()
import sqlite3

score = 0
playerName = ""

quiz = "quiz.db"
connection = sqlite3.connect(quiz)
# cursor
cur = connection.cursor()

def insertScore():
   cur.execute("CREATE TABLE IF NOT EXISTS quiz (name TEXT, score INTEGER)")

   cur.execute("INSERT INTO quiz (name, score) VALUES (?, ?)", (playerName, score))
  # commit
   connection.commit()


def displayMaxScore():
  
    cur.execute("SELECT name,MAX(score) FROM quiz")

    print("max score is ",cur.fetchall())

# function : delete a record
#  update record
#  display all records


def playQUiz():
   global score
   playerName = input("What is your name? ")
   print("Welcome to the quiz game!")
   print("Q1. What is the capital of France?")
   print("A. Paris")
   print("B. London")
   print("C. Madrid")

   choice = input("Enter your choice: ")
   if choice == "A":
       score += 10
       print("Correct!")
   else:
       score -= 5
       print("Incorrect!")

   print("Q2. What is the capital of Spain?")
   print("A. Paris")
   print("B. London")
   print("C. Madrid")
   choice = input("Enter your choice: ")
   if choice == "C":
       score += 10
       print("Correct!")
   else:
       score -= 5
       print("Incorrect!")
   print("Q3. What is the capital of England?")
   print("A. Paris")
   print("B. London")
   print("C. Madrid")
   choice = input("Enter your choice: ")
   if choice == "B":
       score += 10
       print("Correct!")
   else:
       score -= 5
       print("Incorrect!")

   print("Your score is: ", score)



print("Welcome to the quiz game!")

print("1. Play Quiz")
print("2. Display Max Score")

choice = int(input("Enter your choice: "))

if choice == 1:
   playQUiz()
   insertScore()
elif choice == 2:
   displayMaxScore()