from PyQt5 import uic, QtWidgets
import banco as db
import gerarRandom as gr
import time
import threading

def showDB(obj): #FUNÇÃO QUE MOSTRA NA TELA OS DADOS DOS PARTICIPANTES
    data=obj.getData() #OBTER O OBJ..
    screem.tableWidget.setRowCount(len(data)) #CRIAR O TAMANHO DA TABELA COM O MESMO TAMANHO DA LISTA
    screem.tableWidget.setColumnCount(3) #SÓ POSSUI 3 COLUNAS FIXAS
    
    for i in range(0,len(data)): #FUNÇÃO PARA PERCORRER A MATRIZ
        for j in range (0,3):
            screem.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(data[i][j]))) 
            
def main(): #FUNÇÃO RPINCIPAL PARA RECUPERAR OS DADOS PREENCHIDOS PELO TECLADO
    nome=""
    email=""
    telefone=0
    
    nome = screem.lineEdit.text()
    email = screem.lineEdit_2.text()
    telefone = screem.lineEdit_3.text()
    
    obj = db.cadastro(nome, email, telefone) #CRIANDO UM OBJ COM OS DADOS LIDOS NO MÓDULO DO BANCO DE DADOS
    obj.insert() #SALVANDO O OBJ NO BANCO DE DADOS
    showDB(obj) #CHAMANDO A FUNÇÃO QUE PRINTA NA TELA OS DADOS DO BANCO DE DADOS
  
def random(): #FUNÇÃO PARA SORTEAR UM NOME
    obj = db.cadastro("","",0) #CARREGANDO OBJ
    data=obj.getData()   
    size=len(data)   
    numRaffle=gr.raffle(size)
    
    for i in range(0,101): #FUNÇÃO SÓ PARA 'ESTILIZAR' UM POUCO O SORTEIO. PARA NÃO FICAR MUITO 'SECO', EX: CLICA NO BOTÃO E JÁ SORTEIA O NOME
        time.sleep(0.1)
        if i < 19:
            screem2.label_3.setText("Carregando base de dados")
        elif i < 46:
            screem2.label_3.setText("Escolhendo valor aleatorio")
        elif i < 75:
            screem2.label_3.setText("Recuperando dados")
        elif i < 88:
            screem2.label_3.setText("carregando nome")
        elif i < 96:
            screem2.label_3.setText("Só mais alguns instantes...")
        elif i < 100:
            screem2.label_3.setText("Finalizado")
            
        screem2.progressBar.setValue(i) #INCREMENTA 'I' A BARRA DE PROGRESSO 
        
    screem2.label_2.setText(f"O vencedor deste sorteio é:{numRaffle}")


def raffle(): #FUNÇÃO SORTEAR 
    screem2.show() #INICIA A SEGUNDA TELA
    screem2.pushButton.clicked.connect(random) #REALIZA O SORTEIO ATRAVÉS DO CLIQUE DO BOTÃO
    

#INICIANDO O SISTEMA

app=QtWidgets.QApplication([])
screem=uic.loadUi("main.ui")#..................TELA PRINCIPAL
screem2=uic.loadUi("sc2.ui")#..................TELA SEGUNDARIA, EXECUTADA QUANDO ACIONA O BOTÃO SORTEAR
obj = db.cadastro("","",0)#....................NÃO SEI COMO RECUPERAR OS DADOS DO MÉTODO getData() SEM UM OBJETO
showDB(obj)#...................................INICIANDO O PROGRAMA COM A LISTA
screem.pushButton.clicked.connect(main)#.......RECUPERA OS DADOS INSERIDOS PELO USUARIO
screem.pushButton_2.clicked.connect(raffle)#...FUNÇÃO SORTEAR
screem.show()
app.exec()