from PyQt5 import QtWidgets
from PyQt5 import QtGui

class ZcsTray(QtWidgets.QSystemTrayIcon):
    def __init__(self, parent=None):
        super(ZcsTray, self).__init__(parent)
        self.create_menu()
        self.activated.connect(self.on_icon_clicked)

    def create_menu(self):
        self.menu = QtWidgets.QMenu()
        self.menu.addAction(QtWidgets.QAction('退出', self, triggered=self.quit))
        self.setContextMenu(self.menu)
 
        self.setIcon(QtGui.QIcon('./assets/eye.png'))
        
    def quit(self):
        QtWidgets.qApp.quit()

    def on_icon_clicked(self, reason):
        '''
        鼠标点击icon传递的信号会带有一个整形的值，
        1是单击右键，2是双击，3是单击左键，4是用鼠标中键点击
        '''
        print(reason)
        if reason != 1:
            self.hide() #无论reason是几，都出现contex menu，所以这里hide再show，就行了
            self.show()
            self.parent().show()
            self.parent().raise_()
        
        # if reason == 2 or reason == 3:
        #     # self.showMessage("Message", "skr at here", self.icon)
        #     if self.ui.isMinimized() or not self.ui.isVisible():
        #         #若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
        #         self.ui.showNormal()
        #         self.ui.activateWindow()
        #         self.ui.setWindowFlags(QtCore.Qt.Window)
        #         self.ui.show()
        #     else:
        #         #若不是最小化，则最小化
        #         self.ui.showMinimized()
        #         self.ui.setWindowFlags(QtCore.Qt.SplashScreen)
        #         self.ui.show()
        #         # self.ui.show()