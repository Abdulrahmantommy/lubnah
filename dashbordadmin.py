from PyQt5.QtGui import * # FOR NOTE OF ANY CHANGE
from PyQt5.QtCore import * # FOR NOTE OF ANY CHANGE
from PyQt5.QtWidgets import *  # FOR NOTE OF ANY CHANGE
from PyQt5.uic import loadUiType # FOR LOAD UI APP LIVE
import sys # FOR ANY :)
import peewee
import sqlite3 # FOR RUN DB WITH APP ANYTIME :)
import json # FOR SAVE IMAGES TRAK ITEMS
from PyQt5 import QtWidgets # FOR NOTE OF ANY CHANGE
ui,_ = loadUiType('dashbordadmin.ui') # FILE UI (STYLE) NAME IS : "bigg.ui"
#################################
#MAINAPP SET AND ADDID ANY METHOD
class MainApp2(QMainWindow , ui):  # عمليات التنفيذ لما تفتحي المشروع تلقائي تتنفذ
        def __init__(self , parent=None):
            super(MainApp2, self).__init__(parent)
            QMainWindow.__init__(self) # يستدعي الواجهه
            self.setupUi(self) # يقوم بفحص الواجهه
            self.db_connect() # يتصل بقاعدة البيانات
            self.UICHANGES() # فانكشن خاصة بتغيير الواجهه ( اخفاء التابات )
            self.HANDELBUTTONS() # داله خاصة بهندلة الازرار ( جميع الازرار
            self.btnshome() # داله خاصة بكل المتغيرات في الواجهة الرئيسيه
            self.tap0() # لازم يفتح علي الواجهة الاولي
            self.show_category() # بيظهر الفئات في الداتا بيز
            self.show_all_categorry() # بيجهز الفئات للتعديل عليها
            self.show_all_supp() # بيجهز العملاء


            #MainWindow_Settings

        def UICHANGES(self):
            pass



        def HANDELBUTTONS(self):   #جميع الازرار واتصالها بالدوال هنا



            self.btn_show_list_user.clicked.connect(self.showw_user)
            self.btn_show_list_sup.clicked.connect(self.showw_sup)
            self.btn_show_list_category.clicked.connect(self.showw_category)
            self.btn_show_list_items.clicked.connect(self.showw_items)
            self.btn_show_list_all.clicked.connect(self.showw_list_all)

            # user = 1,2,3

            self.btn_add_user.clicked.connect(self.tap1)
            self.btn_edit_user.clicked.connect(self.tap2)
            self.btn_delete_user.clicked.connect(self.tap3)

            # category = 4,5,6

            self.btn_add_category.clicked.connect(self.tap4)
            self.btn_edit_category.clicked.connect(self.tap5)
            self.btn_delete_category.clicked.connect(self.tap6)

            # items = 7,8,9

            self.btn_add_items.clicked.connect(self.tap7)
            self.btn_edit_items.clicked.connect(self.tap8)
            self.btn_delete_items.clicked.connect(self.tap9)

            # sup = 10,11,12

            self.btn_add_sup.clicked.connect(self.tap10)
            self.btn_edit_sup.clicked.connect(self.tap11)
            self.btn_delete_sup.clicked.connect(self.tap12)


            # show = 13,14,15

            self.btn_show_all_users.clicked.connect(self.tap13)
            self.btn_show_all_sup.clicked.connect(self.tap14)
            self.btn_show_all_items_category.clicked.connect(self.tap15)



            self.btn_exit_to_app_18.clicked.connect(self.tap0)
            self.btn_exit_to_app_17.clicked.connect(self.tap0)
            self.btn_exit_to_app_16.clicked.connect(self.tap0)
            self.btn_exit_to_app_15.clicked.connect(self.tap0)
            self.btn_exit_to_app_14.clicked.connect(self.tap0)
            self.btn_exit_to_app_13.clicked.connect(self.tap0)
            self.btn_exit_to_app_12.clicked.connect(self.tap0)
            self.btn_exit_to_app_11.clicked.connect(self.tap0)
            self.btn_exit_to_app_10.clicked.connect(self.tap0)
            self.btn_exit_to_app_9.clicked.connect(self.tap0)
            self.btn_exit_to_app_8.clicked.connect(self.tap0)
            self.btn_exit_to_app_7.clicked.connect(self.tap0)
            self.btn_exit_to_app_4.clicked.connect(self.tap0)
            self.btn_exit_to_app_3.clicked.connect(self.tap0)
            self.btn_exit_to_app_2.clicked.connect(self.tap0)
            self.btn_show_all.clicked.connect(self.show_all)
            self.btn_hide_all.clicked.connect(self.btnshome)
            self.saveBtn_4.clicked.connect(self.save_add_category)
            self.saveBtn_7.clicked.connect(self.add_items)
            self.saveBtn_10.clicked.connect(self.add_sup)
            self.saveBtn_13.clicked.connect(self.edit_supp)
            self.saveBtn_12.clicked.connect(self.edit_supplier)
            self.saveBtn_5.clicked.connect(self.edit_categor)
            self.browseBtn_4.clicked.connect(self.set_logo)









        #################################
#   CONNECT DB WITH APP   #
        def db_connect(self):
            self.db = sqlite3.connect('pos.db')
            self.cur = self.db.cursor()
            print('تم التوصيل بقاعدة البيانات ')
            self.db1 = sqlite3.connect('usrs.db')
            self.cur1 = self.db1.cursor()
            print('تم التوصيل بقاعدة بيانات الموظفين ')

 # اظن واضح من جملة البرينت انه يتصل بقاعدتين بيانات
        # pos =  القاعدة الخاصة بالفئات والمنتجات
        # usrs = خاصة بالعملاء والموردين وكده





        def UICHANGES(self):
            self.TAPP.tabBar().setVisible(False)


 ########## خاصه اذا ضغط علي الموظفين يظهر الازارار الخاصه بالموظفين فقط وهكذا
        def btnshome(self):
            #    user
            self.btn_add_user.setVisible(False)
            self.btn_edit_user.setVisible(False)
            self.btn_delete_user.setVisible(False)

            #     sup

            self.btn_add_sup.setVisible(False)
            self.btn_edit_sup.setVisible(False)
            self.btn_delete_sup.setVisible(False)

            #    category

            self.btn_add_category.setVisible(False)
            self.btn_edit_category.setVisible(False)
            self.btn_delete_category.setVisible(False)

            self.btn_add_items.setVisible(False)
            self.btn_edit_items.setVisible(False)
            self.btn_delete_items.setVisible(False)

            self.btn_show_all_users.setVisible(False)
            self.btn_show_all_sup.setVisible(False)
            self.btn_show_all_items_category.setVisible(False)


        def showw_user(self):
                self.btn_edit_user.show()
                self.btn_delete_user.show()
                self.btn_add_user.show()
                self.btn_add_sup.setVisible(False)
                self.btn_edit_sup.setVisible(False)
                self.btn_delete_sup.setVisible(False)

                self.btn_add_category.setVisible(False)
                self.btn_edit_category.setVisible(False)
                self.btn_delete_category.setVisible(False)

                self.btn_add_items.setVisible(False)
                self.btn_edit_items.setVisible(False)
                self.btn_delete_items.setVisible(False)

                self.btn_show_all_users.setVisible(False)
                self.btn_show_all_sup.setVisible(False)
                self.btn_show_all_items_category.setVisible(False)

        def showw_sup(self):
                self.btn_add_sup.show()
                self.btn_edit_sup.show()
                self.btn_delete_sup.show()
                self.btn_add_user.setVisible(False)
                self.btn_edit_user.setVisible(False)
                self.btn_delete_user.setVisible(False)

                self.btn_add_category.setVisible(False)
                self.btn_edit_category.setVisible(False)
                self.btn_delete_category.setVisible(False)

                self.btn_add_items.setVisible(False)
                self.btn_edit_items.setVisible(False)
                self.btn_delete_items.setVisible(False)

                self.btn_show_all_users.setVisible(False)
                self.btn_show_all_sup.setVisible(False)
                self.btn_show_all_items_category.setVisible(False)

        def showw_category(self):
                self.btn_add_category.show()
                self.btn_edit_category.show()
                self.btn_delete_category.show()
                self.btn_add_user.setVisible(False)
                self.btn_edit_user.setVisible(False)
                self.btn_delete_user.setVisible(False)
                self.btn_add_sup.setVisible(False)
                self.btn_edit_sup.setVisible(False)
                self.btn_delete_sup.setVisible(False)
                self.btn_add_items.setVisible(False)
                self.btn_edit_items.setVisible(False)
                self.btn_delete_items.setVisible(False)
                self.btn_show_all_users.setVisible(False)
                self.btn_show_all_sup.setVisible(False)
                self.btn_show_all_items_category.setVisible(False)

        def showw_items(self):
                self.btn_add_items.show()
                self.btn_edit_items.show()
                self.btn_delete_items.show()
                self.btn_add_user.setVisible(False)
                self.btn_edit_user.setVisible(False)
                self.btn_delete_user.setVisible(False)
                self.btn_add_sup.setVisible(False)
                self.btn_edit_sup.setVisible(False)
                self.btn_delete_sup.setVisible(False)
                self.btn_add_category.setVisible(False)
                self.btn_edit_category.setVisible(False)
                self.btn_delete_category.setVisible(False)
                self.btn_show_all_users.setVisible(False)
                self.btn_show_all_sup.setVisible(False)
                self.btn_show_all_items_category.setVisible(False)


        def showw_list_all(self):
                self.btn_show_all_users.show()
                self.btn_show_all_sup.show()
                self.btn_show_all_items_category.show()
                self.btn_add_user.setVisible(False)
                self.btn_edit_user.setVisible(False)
                self.btn_delete_user.setVisible(False)
                self.btn_add_sup.setVisible(False)
                self.btn_edit_sup.setVisible(False)
                self.btn_delete_sup.setVisible(False)
                self.btn_add_category.setVisible(False)
                self.btn_edit_category.setVisible(False)
                self.btn_delete_category.setVisible(False)
                self.btn_add_items.setVisible(False)
                self.btn_edit_items.setVisible(False)
                self.btn_delete_items.setVisible(False)


        def tap0(self):
            self.TAPP.setCurrentIndex(0)
        def tap1(self):
            self.TAPP.setCurrentIndex(1)
        def tap2(self):
            self.TAPP.setCurrentIndex(2)
        def tap3(self):
            self.TAPP.setCurrentIndex(3)
        def tap4(self):
            self.TAPP.setCurrentIndex(4)
        def tap5(self):
            self.TAPP.setCurrentIndex(5)
        def tap6(self):
            self.TAPP.setCurrentIndex(6)
        def tap7(self):
            self.TAPP.setCurrentIndex(7)
        def tap8(self):
            self.TAPP.setCurrentIndex(8)
        def tap9(self):
            self.TAPP.setCurrentIndex(9)
        def tap10(self):
            self.TAPP.setCurrentIndex(10)
        def tap11(self):
            self.TAPP.setCurrentIndex(11)
        def tap12(self):
            self.TAPP.setCurrentIndex(12)
        def tap13(self):
            self.TAPP.setCurrentIndex(13)
        def tap14(self):
            self.TAPP.setCurrentIndex(14)
        def tap15(self):
            self.TAPP.setCurrentIndex(15)


 # زرار اظهار الكل

        def show_all(self):
            self.btn_edit_user.show()
            self.btn_delete_user.show()
            self.btn_add_user.show()
            self.btn_add_sup.show()
            self.btn_edit_sup.show()
            self.btn_delete_sup.show()
            self.btn_add_category.show()
            self.btn_edit_category.show()
            self.btn_delete_category.show()
            self.btn_add_items.show()
            self.btn_edit_items.show()
            self.btn_delete_items.show()
            self.btn_show_all_users.show()
            self.btn_show_all_sup.show()
            self.btn_show_all_items_category.show()

# لتصفح الصور واختيار صورة للمنتج
        def set_logo(self):
            self.logoPath = QFileDialog.getOpenFileName(self, ("Open Image"), "",
                                                        ("Image Files (*.png *.jpg *.bmp *.svg *.jpeg)"))
            self.logoPath = self.logoPath[0]
            if self.logoPath != '':
                pixmap = QPixmap(self.logoPath)
                self.businessLogo_3.setPixmap(pixmap)
# اضافة وحفظ المنتج
        def add_items(self):
            try:

             #   pixmap = QPixmap(self.logoPath)


             #   image =self.businessLogo_3.pixmap(pixmap)
                name = self.lineEdit_21.text()
                price = self.lineEdit_17.text()
                category = self.comboBox.currentText()

                if price is str:

                    QtWidgets.QMessageBox.warning(self, "Error",
                                              "Couldn't write the new settings.")
                else:

                    self.logoPath = QFileDialog.getOpenFileName(self, ("Open Image"), "",
                                                                ("Image Files (*.png *.jpg *.bmp *.svg *.jpeg)"))
                    self.logoPath = self.logoPath[0]
                    if self.logoPath != '':
                        pixmap = QPixmap(self.logoPath)
                        self.businessLogo.setPixmap(pixmap)
                    self.cur1.execute(
                        f"INSERT INTO {category} (name, price, category , image) VALUES (?, ?, ?, ?) ", (name, price, category))
                    self.db1.commit()
                    self.lineEdit_21.clear()
                    self.lineEdit_17.clear()
                    QtWidgets.QMessageBox.information(self, "Successfully",
                                                  "successfully Add. to list")
            except:
                QtWidgets.QMessageBox.warning(self, "Error",
                                              "Couldn't write the new settings.")



# لانشاء الفئه
        def save_add_category(self):

            new_category = self.lineEdit_13.text()

            try:
                # layout = QVBoxLayout()
               # layout.addWidget(QPushButton(f'{new_category}'))
               # for append button (category (name))
                self.cur1.execute(f'''CREATE TABLE IF NOT EXISTS '{new_category}'
                (name text, price real,category text,  image blob) ''')
                #self.show_category()

                self.db1.commit()
                QtWidgets.QMessageBox.information(self, "Successfully",
                                              "successfully Add. to list")
                self.lineEdit_13.clear()
                print('new category is : ', new_category)
                self.comboBox.clear()
                self.comboBox_2.clear()
                self.show_category()
                self.edit_categor()

                self.show_all_categorry()
            except:

                     QtWidgets.QMessageBox.warning(self, "Error",
                                                   "الاسم موجود من قبل")




# عشان يظهر كل الفئات في الداتا بيز

        def show_category(self):

            self.cur1.execute('''
                SELECT name FROM sqlite_master WHERE type='table';''')
            shh = self.cur1.fetchall()
            for categorye in shh:

                self.comboBox.addItem((categorye[0]))
                self.comboBox_2.addItem((categorye[0]))

        def add_sup(self):

         try:
            self.show_all_supp()
            name = self.lineEdit_26.text()
            number = self.lineEdit_27.text()
            location = self.lineEdit_28.text()
            category = self.lineEdit_37.text()
            if name  == '':
                QtWidgets.QMessageBox.warning(self, "Error",
                                              "Couldn't write the new settings.")
            elif location == '':
                QtWidgets.QMessageBox.warning(self, "Error",
                                              "Couldn't write the new settings.")
            elif number == '':
                QtWidgets.QMessageBox.warning(self, "Error",
                                              "Couldn't write the new settings.")



            else:
             self.cur.execute('''
                INSERT INTO supplier(name, location, number, category)
                VALUES (?,?,?,?);
            
            
            
                      ''',(name,location,number,category))
             self.db.commit()
             QtWidgets.QMessageBox.information(self, "Successfully",
                                              "successfully Add. to list")
             self.show_all_supp()




         except:
               QtWidgets.QMessageBox.warning(self, "Error",
                                           "Couldn't write the new settings.")
# وهكذا

        def show_all_categorry(self):
            self.tableWidget.insertRow(0)
            self.tableWidget_4.insertRow(0)
            self.cur1.execute('''
                SELECT name FROM sqlite_master WHERE type='table';''')
            shh = self.cur1.fetchall()
            for row, form in enumerate(shh):
                for col, item in enumerate(form):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                    self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))


                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                self.tableWidget_4.insertRow(row_position)


# عشان يظهر الموردين في الداتا بيز للانترفيس
        def show_all_supp(self):
            self.tableWidget.insertRow(0)
            self.cur.execute('''
                SELECT name , number, category, location FROM supplier;''')
            shh = self.cur.fetchall()
            for row, form in enumerate(shh):
                for col, item in enumerate(form):
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)





  # للتعديل علي معلومات مورد

        def edit_supp(self):
         try:
            self.tableWidget_3.insertRow(0)
            self.tableWidget_2.insertRow(0)
            self.cur.execute('''
                SELECT name , number, category, location FROM supplier;''')
            shh = self.cur.fetchall()
            for row, form in enumerate(shh):
                for col, item in enumerate(form):
                    self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))


                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_3.insertRow(row_position)
                self.tableWidget_2.insertRow(row_position)

                search = self.lineEdit_22.text()
            sql = ('''
                            SELECT * FROM supplier WHERE name  OR id = (?)            
            ''')
            self.cur.execute(sql,[(search)] )

            data = self.cur.fetchone()
            self.lineEdit_29.setText(data[1])
            self.lineEdit_30.setText(data[3])
            self.lineEdit_31.setText(data[2])
            self.lineEdit_36.setText(data[4])
         except:
             QtWidgets.QMessageBox.warning(self, "Error",
                                           "Couldn't write the new settings.")


        def edit_supplier(self):


           try:
            name = self.lineEdit_29.text()
            number = self.lineEdit_30.text()
            location = self.lineEdit_31.text()
            category = self.lineEdit_36.text()
            id = self.lineEdit_22.text()
            self.cur.execute('UPDATE supplier SET name = (?), location = (?), number = (?), category= (?)  WHERE id = (?)',(str(name) , str(location),str(number),str(category),str(id)))
            self.db.commit()
            QtWidgets.QMessageBox.information(self, "Successfully",
                                              "successfully Add. to list")
            self.show_all_supp()
           except:
               QtWidgets.QMessageBox.warning(self, "Error",
                                             "Couldn't write the new settings.")





    # تعديل علي اسم كاتيجوري

        def edit_categor(self):
         try:
            oldname = self.lineEdit_14.text()
            newname = self.lineEdit_15.text()
            if oldname == '':
                QtWidgets.QMessageBox.warning(self, "Error",
                                              "Couldn't write the new settings.")
            elif newname == '':
                QtWidgets.QMessageBox.warning(self, "Error",
                                              "Couldn't write the new settings.")
            else:

                self.cur1.execute(f'ALTER TABLE {oldname} RENAME TO {newname};')
                self.db1.commit()
                QtWidgets.QMessageBox.information(self, "Successfully",
                                                  "successfully Add. to list")
         except:
             QtWidgets.QMessageBox.warning(self, "Error",
                                           "Couldn't write the new settings.")

# كده ايه تاني
# ولا اي حاجة كل شي هيك رح يوصل صح













# لا يوجد بها اي تعديل لانها خاصة بظهور الواجهه دايما للعميل
def main():
            app = QApplication(sys.argv)
            window2 = MainApp2()
            window2.show()
            app.exec_()

# خاصة بتشغيل الواجهه من ال main
if __name__ == '__main__':
    main()