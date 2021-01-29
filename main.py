from PyQt5.QtGui import * # FOR NOTE OF ANY CHANGE
from PyQt5.QtCore import * # FOR NOTE OF ANY CHANGE
from PyQt5.QtWidgets import *  # FOR NOTE OF ANY CHANGE
from PyQt5.uic import loadUiType # FOR LOAD UI APP LIVE
import sys # FOR ANY :)
import peewee
from dashbordadmin import MainApp2
import sqlite3 # FOR RUN DB WITH APP ANYTIME :)
import json # FOR SAVE IMAGES TRAK ITEMS
from PyQt5 import QtWidgets # FOR NOTE OF ANY CHANGE
ui,_ = loadUiType('bigg.ui') # FILE UI (STYLE) NAME IS : "bigg.ui"
#################################
#MAINAPP SET AND ADDID ANY METHOD
class MainApp(QMainWindow , ui):
        def __init__(self , parent=None):
            super(MainApp , self).__init__(parent)
            QMainWindow.__init__(self)
            self.setupUi(self)
            self.UICHANGES()
            self.db_connect()
            self.HANDELBUTTONS()
            self.tabs3()


#################################
#   CONNECT DB WITH APP   #
        def db_connect(self):
            self.db = sqlite3.connect('pos.db')
            self.cur = self.db.cursor()
            print('Sucssifly Connected!')
#################################
#    EDIT ON DESIGN APP HERE    #
        def UICHANGES(self):
           # self.tab_main.tabBar().setVisible(False)
        #    self.tabWidget_2.tabBar().setVisible(False)
             pass
#################################
#    ALL BUTTONS IN APP HEHE    #
        def HANDELBUTTONS(self):
            self.btn_cashier.clicked.connect(self.taps)
            self.btn_category_2.clicked.connect(self.taps2)
            self.btn_exit.clicked.connect(self.tabs3)
            self.pushButton_5.clicked.connect(self.tap_edit_user)
            self.pushButton_7.clicked.connect(self.tap_edit_category)
            self.pushButton_8.clicked.connect(self.tap_edit_items)
            self.btn_addusr.clicked.connect(self.save_add_user)
            self.btn_login_13.clicked.connect(self.save_add_category)
            self.saveBtn.clicked.connect(self.writeSettings)
            self.browseBtn.clicked.connect(self.setLogo)


###################################


        def save_add_user(self):
            new_user = self.lineEdit_usr.text()
            new_user_password = self.lineEdit_pwd.text()

            if new_user == new_user_password:
                QtWidgets.QMessageBox.warning(self,"Error name",
                                              "please dont use your username in password")
            elif  new_user_password == '':
                QtWidgets.QMessageBox.warning(self, "Error",
                                              "Please Enter username and password")
            elif  new_user == '':
                QtWidgets.QMessageBox.warning(self, "Error",
                                              "Please Enter username and password")

            else:
             self.cur.execute(f"""INSERT INTO Ussr(usr, pwd)  VALUES ('{new_user}', '{new_user_password}')""")





             self.db.commit()
             QtWidgets.QMessageBox.information(self, "Successfully",
                                              "successfully Add User to list")
             print('new user is : ', new_user)



        def save_add_category(self):

            new_category = self.lineEdit_username_13.text()
            if new_category == '':
                QtWidgets.QMessageBox.warning(self, "Error",
                                              "Couldn't write the new settings.")
            else:
               # layout = QVBoxLayout()
               # layout.addWidget(QPushButton(f'{new_category}'))
               # for append button (category (name))


                self.cur.execute(f'''CREATE TABLE  '{new_category}'
                (name text, price int, image blob) ''')

                self.db.commit()
                QtWidgets.QMessageBox.information(self, "Successfully",
                                              "successfully Add. to list")

                print('new category is : ', new_category)


        def taps(self):
            self.tab_main.setCurrentIndex(3)
            self.tab_main.tabBar().setVisible(False)
            self.btn_cashier.setVisible(False)
            self.btn_category.setVisible(False)
            self.btn_category_2.setVisible(False)
            #self.btn_exit.setVisible(False)



        def taps2(self):
            self.app = QApplication(sys.argv)
            self.window2 = MainApp2()
            self.app.exec_()
            self.window2.show()



        def tabs3(self):
            self.tab_main.setCurrentIndex(0)
        def tap_edit_user(self):
            self.tab_main.setCurrentIndex(2)
            self.tabWidget_2.setCurrentIndex(0)
        def tap_edit_category(self):
            self.tab_main.setCurrentIndex(2)
            self.tabWidget_2.setCurrentIndex(2)
        def tap_edit_items(self):
            self.tab_main.setCurrentIndex(2)
            self.tabWidget_2.setCurrentIndex(3)

        def setLogo(self):
            self.logoPath = QFileDialog.getOpenFileName(self, ("Open Image"), "",
                                                        ("Image Files (*.png *.jpg *.bmp *.svg *.jpeg)"))
            self.logoPath = self.logoPath[0]
            if self.logoPath != '':
                pixmap = QPixmap(self.logoPath)
                self.businessLogo.setPixmap(pixmap)

        def writeSettings(self):
            settings = {
                'logoPath': self.logoPath
            }
            try:
                with open('settings.json', 'w') as configsfile:
                    json.dump(settings, configsfile)
            except:
                QtWidgets.QMessageBox.warning(self, "Error",
                                              "Couldn't write the new settings.")
            else:
                QtWidgets.QMessageBox.information(self, "Successfully",
                                                  "successfully Upload Logo Item.")
            finally:
                self.taps()



def main1():
            app1 = QApplication(sys.argv)
            window = MainApp()
            window.show()
            app1.exec_()

if __name__ == '__main__':
            main1()