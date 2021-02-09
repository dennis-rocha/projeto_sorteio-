from PyQt5 import uic, QtWidgets
import banco as db

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
    print("olá mundo")

app=QtWidgets.QApplication([])
screem=uic.loadUi("main.ui")
screem.pushButton.clicked.connect(main)
screem.pushButton_2.clicked.connect(raffle)
screem.show()
app.exec()