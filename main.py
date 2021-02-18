from PyQt5 import uic, QtWidgets
import banco as db
import gerarRandom as gr

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
    
    
def raffle():
    screem2.show()
    obj = db.cadastro("","",0)
    data=obj.getData()
    size=len(data)
    
    
    print(size)
    
    numRaffle=gr.raffle(size)
    print(f"numero sorteado é: {numRaffle}")
    screem2.label_2.setText(f"O vercedor deste sorteio é:{numRaffle}")

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