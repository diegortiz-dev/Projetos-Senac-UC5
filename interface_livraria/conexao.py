import mysql.connector

def conectar_banco():
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="q1w2e3",
            database="TElivraria",
            ssl_disabled=True  
        )
        return conexao
    