# 导入库文件
import sys,os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import time
import webbrowser
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtWidgets import QApplication, QMainWindow
from UpperComputer import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    # 初始化
    def __init__(self,parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置实例
        self.CreateItems()
        # 设置信号和槽
        self.CreateSignalSlot()
        self.count = 0

    # 设置实例
    def CreateItems(self):
        # QT串口类
        self.com = QSerialPort()
        # QT定时器类
        self.timer = QTimer(self) #初始化一个定时器
        self.timer.timeout.connect(self.ShowTime) #计时结束调用operate()方法
        self.timer.start(100) #设置计时间隔 100ms 并启动


    # 设置信号与槽
    def CreateSignalSlot(self):
        self.pushButton.clicked.connect(self.pushButton_clicked)        # 串口刷新
        self.actionAbout.triggered.connect(self.Goto_MyBlog)            # 关于我们
        self.actions.triggered.connect(self.Goto_friend)                # 友情链接
        self.pushButton_2.clicked.connect(self.Com_Open)                # 打开串口
        self.pushButton_18.clicked.connect(self.Com_Close)              # 关闭串口
        self.pushButton_20.clicked.connect(self.ComSendData)            # 发送数据
        self.com.readyRead.connect(self.Com_Receive_Data)               # 接收数据
        self.horizontalSlider.valueChanged.connect(self.Base_Servo)     # 拖动控件-控制底座舵机
        self.horizontalSlider_2.valueChanged.connect(self.Left_Servo)   # 拖动控件-控制左舵机
        self.horizontalSlider_3.valueChanged.connect(self.Right_Servo)  # 拖动控件-控制右舵机
        self.horizontalSlider_4.valueChanged.connect(self.Claw_Servo)   # 拖动控件-控制爪子舵机
        self.horizontalSlider_5.valueChanged.connect(self.Not)          # 拖动控件-未定义
        self.horizontalSlider_6.valueChanged.connect(self.Not_2)        # 拖动控件-未定义
        self.pushButton_10.clicked.connect(self.Add_action)             # 添加动作按钮
        self.pushButton_11.clicked.connect(self.Del_action)           # 删除动作按钮
        self.pushButton_14.clicked.connect(self.Save_action)          # 保存动作按钮
        self.pushButton_13.clicked.connect(self.Download_action)      # 下载动作组按钮
        self.pushButton_16.clicked.connect(self.Run_action)           # 运行动作组按钮
        self.pushButton_15.clicked.connect(self.Open_action)          # 打开动作组按钮

    # 显示时间
    def ShowTime(self):
        self.label_11.setText(time.strftime("%B %d, %H:%M:%S", time.localtime()))

    # 跳转到我的博客
    def Goto_MyBlog(self):
        webbrowser.open("http://www.cnblogs.com/YanQing1998/")

    # 跳转到友情链接
    def Goto_friend(self):
        webbrowser.open("https://sevenold.github.io/")

    # 串口发送数据
    def ComSendData(self):
        SendData = self.textEdit_9.toPlainText()
        if len(SendData) == 0 :
            return
        else:
            for i in range(0, len(SendData) - 17, 18):
                m = i + 18
                sendData = SendData[i:m]
                self.com.write(sendData.encode('UTF-8'))

    # 串口接收数据
    def Com_Receive_Data(self):
        try:
            rxData = bytes(self.com.readAll())
        except:
            QMessageBox.critical(self,'ERROR','串口接收数据错误')
        try:
            self.textEdit_8.insertPlainText(rxData.decode('UTF-8'))
            self.count += 1
            if self.count > 15:
                self.count = 0
                self.textEdit_8.clear()
        except:
            return



    # 串口刷新
    def pushButton_clicked(self):
        self.comboBox_2.clear()
        com = QSerialPort()
        com_list = QSerialPortInfo.availablePorts()
        for info in com_list:
            com.setPort(info)
            if com.open(QSerialPort.ReadWrite):
                self.comboBox_2.addItem(info.portName())
                com.close()

    # 串口打开按钮按下
    def Com_Open(self):
        comName = self.comboBox_2.currentText()
        comBaud = int(self.comboBox.currentText())
        self.com.setPortName(comName)
        self.com.setBaudRate(comBaud)
        try:
            if self.com.open(QSerialPort.ReadWrite) == False:
                QMessageBox.critical(self,'ERROR','串口打开失败')
                return
        except:
            QMessageBox.critical(self,'ERROR','串口打开识别')
            return
        self.pushButton_18.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.comboBox_2.setEnabled(False)
        self.comboBox.setEnabled(False)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider_2.setEnabled(True)
        self.horizontalSlider_3.setEnabled(True)
        self.horizontalSlider_4.setEnabled(True)
        self.horizontalSlider_5.setEnabled(True)
        self.horizontalSlider_6.setEnabled(True)
        self.pushButton_19.setEnabled(True)
        self.pushButton_20.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_14.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_16.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        self.pushButton_15.setEnabled(True)
        self.pushButton_13.setEnabled(True)
        self.pushButton_17.setEnabled(True)
        self.pushButton_10.setEnabled(True)

    # 串口关闭按钮按下
    def Com_Close(self):
        self.com.close()
        # 让控件处于不可选状态
        self.pushButton_18.setEnabled(False)
        self.horizontalSlider.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.comboBox_2.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.horizontalSlider_2.setEnabled(False)
        self.horizontalSlider_3.setEnabled(False)
        self.horizontalSlider_4.setEnabled(False)
        self.horizontalSlider_5.setEnabled(False)
        self.horizontalSlider_6.setEnabled(False)
        self.pushButton_19.setEnabled(False)
        self.pushButton_20.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        self.pushButton_13.setEnabled(False)
        self.pushButton_17.setEnabled(False)
        self.pushButton_10.setEnabled(False)

    # 拖动控件-控制底座舵机
    def Base_Servo(self):
        Data = self.horizontalSlider.value()
        self.textEdit_10.setText(str(Data))
        try:
            temp = str(self.horizontalSlider.value())
            for i in range((3-len(temp))):
                temp = '0'+ temp
            SendData = 'aa0' + temp + 'ff'
            if len(SendData) == 0:
                return
            else:
                self.com.write(SendData.encode('UTF-8'))
        except:
            return

    # 拖动控件-控制左舵机
    def Left_Servo(self):
        Data = self.horizontalSlider_2.value()
        self.textEdit_2.setText(str(Data))
        try:
            temp = str(self.horizontalSlider_2.value())
            for i in range(3-len(temp)):
                temp = '0' + temp
            SendData = 'aa1' + temp + 'ff'
            if len(SendData) == 0:
                return
            else:
                self.com.write(SendData.encode('UTF-8'))
        except:
            return

    # 拖动控件-控制右舵机
    def Right_Servo(self):
        Data = self.horizontalSlider_3.value()
        self.textEdit_3.setText(str(Data))
        try:
            temp = str(self.horizontalSlider_3.value())
            for i in range(3-len(temp)):
                temp = '0' + temp
            SendData = 'aa2' + temp + 'ff'
            if len(SendData) == 0:
                return
            else:
                self.com.write(SendData.encode('UTF-8'))
        except:
            return

    # 拖动控件-控制爪子舵机
    def Claw_Servo(self):
        Data = self.horizontalSlider_4.value()
        self.textEdit_4.setText(str(Data))
        try:
            temp = str(self.horizontalSlider_4.value())
            for i in range(3-len(temp)):
                temp = '0' + temp
            SendData =  'aa3' + temp + 'ff'
            if len(SendData) == 0:
                return
            else:
                self.com.write(SendData.encode('UTF-8'))
        except:
            return

    # 拖动控件-控制下部
    def Not(self):
        Data = self.horizontalSlider_5.value()
        self.textEdit_5.setText(str(Data))

    # 拖到控件-控制转盘
    def Not_2(self):
        Data = self.horizontalSlider_6.value()
        self.textEdit_6.setText(str(Data))

    # 添加动作按钮
    def Add_action(self):
        temp_1 = str(self.horizontalSlider.value())
        temp_2 = str(self.horizontalSlider_2.value())
        temp_3 = str(self.horizontalSlider_3.value())
        temp_4 = str(self.horizontalSlider_4.value())
        for i in range(3-len(temp_1)):
            temp_1 = '0'+ temp_1
        for i in range(3-len(temp_2)):
            temp_2 = '0'+ temp_2
        for i in range(3-len(temp_3)):
            temp_3 = '0'+ temp_3
        for i in range(3-len(temp_4)):
            temp_4 = '0'+ temp_4
        Data =    'aa4' + temp_1 + temp_2 + temp_3 + temp_4 + 'ff' + "\n"
        self.textEdit_7.insertPlainText(Data)

    # 保存动作组
    def Save_action(self):
        try:
            f = open('text','a')
            SendData = self.textEdit_7.toPlainText()
            if len(SendData) > 0 :
                f.write(SendData)
                f.close()
                QMessageBox.about(self,"提示","保存成功")
            else:
                QMessageBox.critical(self, "ERROR", "未添加动作")
        except:
            QMessageBox.critical(self,"ERROR","操作失败")

    # 删除动作组
    def Del_action(self):
        try:
            open('text','w').close()
            QMessageBox.about(self,"提示","删除成功")
        except:
            QMessageBox.critical(self,"ERROR","操作失败")

    # 打开动作组
    def Open_action(self):
        try:
            f = open('text','r')
            Text_action = f.read()
            self.textEdit_7.insertPlainText(Text_action)
            f.close()
        except:
            pass

    # 下载动作组
    def Download_action(self):
        pass

    # 运行动作组
    def Run_action(self):
        SendData = self.textEdit_7.toPlainText()
        if len(SendData) == 0 :
            QMessageBox.critical(self,"ERROR","动作组为空")
        else:
            for i in range(0, len(SendData) - 17, 18):
                m = i + 18
                sendData = SendData[i:m]
                self.com.write(sendData.encode('UTF-8'))


def main():
    window = QApplication(sys.argv)
    TheWin = MainWindow()
    TheWin.show()
    sys.exit(window.exec_())

if __name__ == '__main__':
    main()
