# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets;


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(407, 595)
        MainWindow.setStyleSheet("background-color: rgb(62, 70, 89);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 302, 176))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tableWidget.setStyleSheet("color: rgb(58, 69, 103);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.tableWidget.setItem(2, 2, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(59)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(58)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 240, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
" border-radius: 10px;\n"
"background-color: rgb(109, 122, 167);")
        self.pushButton.clicked.connect(self.data)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 320, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(240, 0, 0);\n"
" border-radius: 10px;")
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 410, 281, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 460, 281, 41))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "ตรวจสอบผลลัพธ์"))
        self.pushButton_2.setText(_translate("MainWindow", "ล้างค่า"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">ผลลัพธ์</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">null</span></p></body></html>"))
    def clear(self):
                indexR1=False
                indexR2=False
                indexR3=False
                row1=0
                row2=0
                row3=0

                Row1=0
                Row2=0
                Row3=0

                Step1  = False
                Step2  = False
                self.label_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">null</span></p></body></html>")
                for x in range(3):
                        for i in range(3):
                                self.tableWidget.setItem(x,i,QtWidgets.QTableWidgetItem(""))
                                # self.tableWidget.setTextAlignment(QtCore.Qt.AlignCenter)
                                # font = QtGui.QFont()
                                # font.setPointSize(20)
                                # self.tableWidget.setFont(font)

    def data(self):
        try:

                indexR1=False
                indexR2=False
                indexR3=False
                row1=0
                row2=0
                row3=0

                Row1=0
                Row2=0
                Row3=0

                Step1  = False
                Step2  = False
                

             
                for i in range(3):
                        #self.tableWidget.item(0,i).text()
                        R1=self.tableWidget.item(0,i).text()
                        R2=self.tableWidget.item(1,i).text()
                        R3=self.tableWidget.item(2,i).text()

                        
                        # Row1 += int(R1)
                        # Row2 += int(R2)
                        # Row3 += int(R3)

                        if int(R1) >=1 and indexR1==False: 
                                if int(R1) == 1 and indexR1==False:
                                        row1=i+1
                                indexR1=True
                        if int(R2) >= 1 and indexR2==False:
                                if int(R2) == 1 and indexR2==False:
                                        row2=i+1
                                        for x in range(0,i):
                                                Row2+=int(self.tableWidget.item(0,1).text())
                                indexR2=True
                        if int(R3) >= 1 and indexR3==False:
                                if int(R3) == 1 and indexR3==False:
                                        row3=i+1
                                        for x in range(0,i):
                                                Row3+=int(self.tableWidget.item(1,2).text())
                                                #+int(self.tableWidget.item(0,1).text()))+int(self.tableWidget.item(0,2).text())
                                indexR3=True
                        

                if row1-row2==-1 or row1-row2==-2 and row1 > 0:
                        if row2-row3==-1 or row2-row3==3 or row3==0:
                                
                                if Row1==0 and Row2==0 and  Row3>=0:
                                        Step2=True
                                else:
                                        Step1=True

                        else :
                                print("ไม่มี")
                # else if  :
                #         print()
                else :
                        print("ไม่มี")


                print("R1 ="+str(row1))
                print("R2 ="+str(row2))
                print("R3 ="+str(row3))

                print("=========")     

                print("R1+r2 ="+str(row1-row2))  
                print("R2+r3 ="+str(row2-row3))  
                print("=========")    
                if Step1==True:
                        print("เป็นเมทริกซ์ขั้นบันไดทั่วไป")
                        self.label_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">เป็นเมทริกซ์ขั้นบันไดทั่วไป</span></p></body></html>")
                        #self.label_2.setText("เป็นเมทริกซ์ขั้นบันไดทั่วไป")
                        print("=========") 
                elif Step2==True:
                        print("เป็นเมทริกซ์ขั้นบันไดลดรูป")
                        #self.label_2.setText("เป็นเมทริกซ์ขั้นบันไดลดรูป")  
                        self.label_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">เป็นเมทริกซ์ขั้นบันไดลดรูป</span></p></body></html>")
                        print("=========") 
                else :
                        #self.label_2.setText("ไม่เป็นเป็นเมทริกซ์ขั้นบันไดลดรูป")  
                        self.label_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">ไม่เป็นเป็นเมทริกซ์ขั้นบันได</span></p></body></html>")
                print("=========") 
                print("Row1"+str(Row1)) 
                print("Row2"+str(Row2)) 
                print("Row3"+str(Row3)) 
        except :
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)

                msg.setText("กรุณาใส่ตข้อมุลตัวเลขลงในช่องให้ถูกต้อง !")
                msg.setWindowTitle("Matrix error !")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                retval = msg.exec_()
           
                     




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
