import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QDialog, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtCore import QCoreApplication, Qt
import random
import numpy as np

#签到的url
url = "https://api.live.bilibili.com/sign/doSign"

#获得headers
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
    ,"Accept-Encoding": "gzip, deflate, br"
    ,"Accept-Language": "zh-CN,zh;q=0.9"
    ,"Cache-Control": "no-cache"
    ,"Connection": "keep-alive"
    ,"Cookie": "不给你们"
    ,"Host": "live.bilibili.com"
    ,"Pragma": "no-cache"
    ,"Referer": "https://www.bilibili.com/"
    ,"Upgrade-Insecure-Requests": "1"
    ,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

#定义全局随机变量，用来设置随机背景
i = random.choices(np.arange(6) + 1)

#写一个签到界面
class DoSign(QWidget):

    def __init__(self):
        super().__init__()

        #初始化界面
        self.initUI()

    def paintEvent(self, event):
        """
        用paintEvent画背景
        :param event:
        :return:
        """
        #随机读取本地图片
        url = './images/{}.png'.format(i[0])

        #用QPainter画在界面上
        pixmap = QPixmap(url)
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), pixmap)

    def initUI(self):
        #初始化窗体大小，设置title，设置图标，设置不能放大缩小
        self.setGeometry(300, 300, 350, 220)
        self.setWindowTitle("Bilibili Sign")
        self.setWindowIcon(QIcon("sign.jpg"))
        self.setFixedSize(self.width(), self.height())

        #连个按钮，签到和退出
        closeBtn = QPushButton("exit", self)
        signBtn = QPushButton("sign", self)

        closeBtn.clicked.connect(QCoreApplication.instance().quit)
        #绑定消息函数
        signBtn.clicked.connect(self.sign_message)

        #设置按钮样式
        closeBtn.setStyleSheet("border:4px groove gray;border-radius:10px;padding:2px 4px;font-family:Times New Roman;font-size:15Pt;font-weight:bold;color:#9900FF")
        signBtn.setStyleSheet("border:4px groove gray;border-radius:10px;padding:2px 4px;font-family:Times New Roman;font-size:15Pt;font-weight:bold;color:#FF6633")

        #按钮之见水平布局
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(signBtn)
        hbox.addWidget(closeBtn)

        #总体垂直布局
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.show()

    def sign_message(self):
        """
        签到
        :return:
        """
        js = requests.get(url, headers=header)
        code = js.json()['code']
        msg = js.json()['msg']
        if code == 0:
            reply = QMessageBox.about(self, "message", msg)
        else:
            reply = QMessageBox.about(self, "message", "签到失败")


app = QApplication(sys.argv)
dosing = DoSign()
sys.exit(app.exec_())



