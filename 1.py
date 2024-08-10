from PySide6.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QWidget
from PySide6.QtCore import Qt
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        line=QLineEdit(self)
        line.setPlaceholderText('输入账号:')
if __name__=='__main__':
    app=QApplication([])
    window=MyWindow()
    window.show()
    app.exec()
