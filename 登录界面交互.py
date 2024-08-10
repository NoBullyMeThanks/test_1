from PySide6.QtWidgets import QMainWindow,QLabel,QLineEdit,QPushButton,QApplication,QWidget
from PySide6.QtCore import Qt
from login import Ui_Form

class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #调用Ui_Form的setupUi方法
        self.pushButton.clicked.connect(self.loginFuc)

    def loginFuc(self):
        account=self.lineEdit.text()
        password=self.lineEdit_2.text()
        if account=='123' and password=='123':
            print('Yes')
        else:
            print('No')


if __name__=='__main__':
    app=QApplication([])
    window=MyWindow()
    window.show()
    app.exec()