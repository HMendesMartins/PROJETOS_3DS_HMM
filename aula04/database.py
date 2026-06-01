import mysql.connector as mysql
from mysql.connector import  Error

def conectar_banco():
    try:
        print("conectou")
        conexao = mysql.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "parque_diversoes"
        )
        if conexao.is_connected():
            print("conectou")
            return conexao
            
    except Error as erro:
        print(f"Erro ao conectar: {erro}")
        return None
def cadastrar_atracao():    
    conexao_aberta = conectar_banco()
    if conexao_aberta:
        cursor = conexao_aberta.cursor()
        nome = input("Nome da atracao: ")
        estado = input("Estado da atração: ")
        sql = "INSERT INTO atracoes (nome, estado) VALUES (%s,%s);"
        dados = (nome, estado)
        try:
            cursor.execute(sql, dados)
            conexao_aberta.commit()
            print(f"{nome} deu certo")
        except Error as erro:
            print(f"Fodeu kk. Erro ao cadastrar:{erro}")
        finally:
            cursor.close()
            conexao_aberta.close()
def listar():
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        listar = "SELECT * FROM atracoes"
        try:
            cursor.execute(listar)
            resultados = cursor.fetchall()
            print("Deu certo!")
            if not resultados:
                print("Nenhum resultado encontrado!")
            else:
                for atracao in resultados:
                    print(f"ID: {atracao[0]}, Atracao: {atracao[1]}, Estado: {atracao[2]}") 
        except Error as error:
            print(f"Erro ao listar itens: {error}")
        
cadastrar_atracao()
listar()