import sqlite3

connection = sqlite3.connect('database.db')


with open('schemas/users.sql', 'r') as sql_file:
    connection.executescript(sql_file.read())