from PyQt5 import uic, QtWidgets
import banco as db
import gerarRandom as gr
import time
import threading

def showDB(obj):
    data=obj.getData()
    screem.tableWidget.setRowCount(len(data))
    screem.tableWidget.setColumnCount(3)
    
    for i in range(0,len(data)):
        for j in range (0,3):
            screem.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(data[i][j])))
            
def main():
    nome=""
    email=""
    telefone=0
    
    nome = screem.lineEdit.text()
    email = screem.lineEdit_2.text()
    telefone = screem.lineEdit_3.text()
    
    obj = db.cadastro(nome, email, telefone)
    obj.insert()
    showDB(obj) 
  
def random():
    obj = db.cadastro("","",0)
    data=obj.getData()   
    size=len(data)   
    numRaffle=gr.raffle(size)
    
    for i in range(0,101):
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
            
        #setText("")
        screem2.progressBar.setValue(i)
        
    
    screem2.label_2.setText(f"O vercedor deste sorteio é:{numRaffle}")

def raffle():
    screem2.show()
    screem2.pushButton.clicked.connect(random)
    

#INICIANDO O SISTEMA

app=QtWidgets.QApplication([])
screem=uic.loadUi("main.ui")
screem2=uic.loadUi("sc2.ui")
obj = db.cadastro("","",0)#....................NÃO SEI COMO RECUPERAR OS DADOS DO MÉTODO getData() SEM UM OBJETO
showDB(obj)#...................................INICIANDO O PROGRAMA COM A LISTA
screem.pushButton.clicked.connect(main)#.......RECUPERA OS DADOS INSERIDOS PELO USUARIO
screem.pushButton_2.clicked.connect(raffle)#...FUNÇÃO SORTEAR
screem.show()
app.exec()