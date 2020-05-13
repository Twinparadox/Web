import numpy as np
import sys

import requests
import json

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("KerasGUI.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 버튼 이벤트 연결
        self.btn_predict.clicked.connect(self.execPredict)
        self.btn_clear.clicked.connect(self.execClear)

    def execPredict(self):
        print("execute Predict Button")
        X1 = float(self.textEdit_X1.toPlainText())
        X2 = float(self.textEdit_X2.toPlainText())
        X3 = float(self.textEdit_X3.toPlainText())

        #model = load_model('model.h5')
        url = 'http://localhost:3000/users'
        params = { 'X1':X1, 'X2':X2, 'X3':X3 }
        print(params)
        print(json.dumps(params))
        pred = requests.post(url=url, data=params)
        print(pred.json())
        self.textEdit_Pred.setPlainText(pred.json()[1])

    def execClear(self):
        self.textEdit_X1.clear()
        self.textEdit_X2.clear()
        self.textEdit_X3.clear()
        self.textEdit_Pred.clear()

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    