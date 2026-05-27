import mysql.connector as mysql
from mysql.connector import  Error
def conectar_banco():
    try:
        print("conectou")
    except Error as erro:
        print(f"Erro ao conectar: {erro}")
    