import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE carford")

mycursor.execute("CREATE DATABASE carford")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="carford"
)

mycursor = mydb.cursor()

mycursor.execute(
    """CREATE TABLE owners (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        qtycars INT(2) NOT NULL DEFAULT 0,
        PRIMARY KEY (id))"""
        )

mycursor.execute(
    """CREATE TABLE cars (
        id INT NOT NULL AUTO_INCREMENT,
        owner INT(255) NOT NULL,
        color VARCHAR(50) NOT NULL,
        type VARCHAR(50) NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY (owner)
            REFERENCES owners(id)
            ON DELETE CASCADE)"""
        )