from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import os
import backend
from time import sleep


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 511, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.inputText = QtWidgets.QTextEdit(self.centralwidget)
        self.inputText.setGeometry(QtCore.QRect(170, 120, 177, 25))
        self.inputText.setObjectName("inputText")

        self.input = QtWidgets.QLabel(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 120, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input.setFont(font)
        self.input.setObjectName("input")

        self.process = QtWidgets.QLabel(self.centralwidget)
        self.process.setGeometry(QtCore.QRect(10, 160, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.process.setFont(font)
        self.process.setObjectName("process")

        self.processText = QtWidgets.QTextEdit(self.centralwidget)
        self.processText.setGeometry(QtCore.QRect(170, 160, 177, 25))
        self.processText.setObjectName("processText")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.click())
        self.pushButton.setGeometry(QtCore.QRect(120, 260, 241, 51))
        self.pushButton.setObjectName("pushButton")

        self.outputText = QtWidgets.QLabel(self.centralwidget)
        self.outputText.setGeometry(QtCore.QRect(165, 210, 300, 30))
        self.outputText.setText("")
        self.outputText.setObjectName("outputText")

        self.boxes = []
        columns = 4*50
        for idx in range(columns):
            self.boxes.append(QtWidgets.QPushButton(self.centralwidget))
            self.boxes[idx].setGeometry(QtCore.QRect(-1,-1, 1, 1))

        self.outputBoxes = self.boxes.copy()


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def click(self):
        input = self.inputText.toPlainText()
        process = self.processText.toPlainText()
        cond = True
        for num in input:
            x = int(num) <= 4
            if x == False:
                cond = False
                break

        cond = input.isnumeric() and process.isnumeric() and process[-1] == '0' and len(input) <= 4*50

        if cond:
            self.writeCSV(input, process)
            backend.main()
            self.drawMap(input)
            self.readAndDisplay()
            
        else:
            out = "Error: Enter input and process configuration in numeric form"
            self.outputText.setText(out + "\nprocess configuration must end with 0")


    def drawMap(self, input):
        columns = len(input)
        self.line.setGeometry(QtCore.QRect(450, 170, 21, 351))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2.setGeometry(QtCore.QRect(460, 510, 60*columns, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        for column in range(columns):

            numBox =  int(input[column])
            for box in range(numBox):
                x = self.boxes.pop(box)
                x.setGeometry(QtCore.QRect(460+60*column, 460 - 60*box, 60, 60))


    def writeCSV(self, input, process):
        with open('inputAndProcess.csv', 'w', newline='') as f:
            write = csv.writer(f)
            write.writerow(input)
            write.writerow(process)


    def readAndDisplay(self):
        while(True):
            with open('output.csv', 'r', newline='') as f:
                reader = csv.reader(f, delimiter=' ')
                row = next(reader)
                if not row==[]:
                    out = ''.join([str(elem) for elem in row])
                    out = out.replace(',', '')
                    self.outputText.setText(out)
                    break
            f.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Crane Simulator 9000"))
        self.inputText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.input.setText(_translate("MainWindow", "Input configuration"))
        self.process.setText(_translate("MainWindow", "Process configuration"))
        self.processText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Output configuration:"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
