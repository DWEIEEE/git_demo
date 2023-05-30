from PyQt5 import QtWidgets

from controller import MainWindow_controller

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)#實例化應用程式
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())