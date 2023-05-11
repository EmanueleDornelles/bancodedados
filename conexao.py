import mysql.connector

def conectar():
  mydb = mysql.connector.connect(
    host="db-brasil.cnrvq9aynriy.us-east-1.rds.amazonaws.com",
    user="admin",
    password="aulanoite",
    database="brasil"
  )
  return mydb