from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton,QMainWindow,QWidget,QLineEdit,QApplication
from calculate import Ui_Form

class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__=='__main__':
    app=QApplication([])
    window=MyWindow()
    window.show()
    app.exec()