import sqlite3

conector = sqlite3.connect("dbCadastro.db")

cursor = conector.cursor()

#cursor.execute("CREATE TABLE pessoas (nome varchar, email varchar, telefone int)")

class cadastro:
    def __init__ (self, nome, email, telefone):
        self.nome=nome
        self.email=email
        self.telefone=telefone
        
    def insert (self):
        cursor.execute("INSERT INTO pessoas VALUES ('"+str(self.nome)+"','"+str(self.email)+"','"+str(self.telefone)+"')")
        conector.commit()
        #cursor.close() !!!!!!!!!!!!!!!!! NÃO FUNCIONA SE FECHAR O BANCO DE DADOS
        #conector.close()
        
    def getData (self):
        cursor.execute("SELECT * FROM pessoas")
        dataRead = cursor.fetchall()
        return dataRead