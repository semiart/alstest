import sys, time, socket
from PyQt5 import QtWidgets, QtCore
from als_ui import Ui_Form
from telnetlib import Telnet
import re

class AlsGui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
    
        # Init slider
        self.ui.sldIrLevel.setMaximum(10)
        self.ui.sldIrLevel.setMinimum(0)
        self.ui.sldIrLevel.setValue(0)
        self.ui.sldIrLevel.setTickPosition(QtWidgets.QSlider.TicksBelow)

        # Init spinbox
        self.ui.sbxIrRampInterval.setRange(0, 5000)
        self.ui.sbxIrRampInterval.setSingleStep(200)
        self.ui.sbxIrRampInterval.setValue(0)
        self.ui.sbxIrRampInterval.setToolTip('Set interval to 0 to output constant IR')

        self.ui.sbxSamplingInterval.setRange(100, 1000)
        self.ui.sbxSamplingInterval.setSingleStep(100)
        self.ui.sbxSamplingInterval.setValue(200)

        # Init progressbar
        self.ui.prgAlsLevel.setMaximum(0xfff)
        self.ui.prgAlsLevel.setValue(0)

        # Init Telnet
        self.tn = AlsTelnet()

        # Init timer
        self.timerUpdatePrgbar = QtCore.QTimer()
        self.timerUpdatePrgbar.setInterval(1000)

        self.timerReadAls = QtCore.QTimer()
        self.timerReadAls.setInterval(200)

        self.timerUpdateIrLevel = QtCore.QTimer()
        self.timerUpdateIrLevel.setInterval(1000)

        # Init variables
        self.currentIrLevel = 0

        # Connect signals and slots
        self.ui.btnConnect.clicked.connect(self.btnConnectClicked)
        self.ui.sldIrLevel.valueChanged.connect(self.sldIrLevelValueChanged)
        self.timerUpdatePrgbar.timeout.connect(self.updatePrgbar)
        self.timerReadAls.timeout.connect(self.readAls)
        self.timerUpdateIrLevel.timeout.connect(self.updateIrLevel)
        self.ui.sbxIrRampInterval.valueChanged.connect(self.sbxIrRampIntervalValueChanged)
        self.ui.sbxSamplingInterval.valueChanged.connect(self.sbxSamplingIntervalValueChanged)

        self.show()
        
    def btnConnectClicked(self):
        if(self.tn.connected):
            self.timerUpdatePrgbar.stop()
            self.timerReadAls.stop()
            self.timerUpdateIrLevel.stop()
            self.tn.disconnect()
            self.ui.btnConnect.setText('Connect')
            if(self.logfile is not None):
                self.logfile.close()
        else:
            self.tn.connect()
            if(self.tn.connected):
                self.timerUpdatePrgbar.start()
                self.timerReadAls.start()
                if(self.ui.sbxIrRampInterval.value()):
                    self.timerUpdateIrLevel.start()
                self.ui.btnConnect.setText('Disconnect')
                self.logfile = open(time.strftime('%d-%b-%y-%H-%M-%S', time.localtime() + '.log', 'w'))
                self.logfile = open(time.strftime('%d-%b-%y-%H-%M-%S', time.localtime()) + '.log', 'w')
            else:
                msg = QtWidgets.QMessageBox()
                msg.setText('Open Telnet Failed')
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()

    def sldIrLevelValueChanged(self):
        self.ui.lblIrLevel.setText('Max IR Level ' + str(self.ui.sldIrLevel.value() * 10))
        if(self.tn.connected and self.ui.sbxIrRampInterval.value() == 0):
            self.tn.setIrLevel(self.ui.sldIrLevel.value())

    def updatePrgbar(self):
        self.ui.prgAlsLevel.setValue(self.tn.alsLastReading)
        self.ui.lblAlsLevel.setText('ALS Level: ' + str(hex(self.tn.alsLastReading)))

    def readAls(self):
        self.tn.readAlsLevel()
        self.logfile.write(str(time.time()) + ' ' + str(self.tn.alsLastReading) + ' ' + str(self.currentIrLevel * 10) + '\n')

    def updateIrLevel(self):
        self.tn.setIrLevel(self.currentIrLevel)
        self.currentIrLevel += 1
        if(self.currentIrLevel > self.ui.sldIrLevel.value()):
            self.currentIrLevel = 0

    def sbxIrRampIntervalValueChanged(self):
        if(self.tn.connected):
            if(self.ui.sbxIrRampInterval.value()):
                self.timerUpdateIrLevel.stop()
                self.timerUpdateIrLevel.setInterval(self.ui.sbxIrRampInterval.value())
                self.timerUpdateIrLevel.start()
            else:
                self.timerUpdateIrLevel.stop()
                self.tn.setIrLevel(self.ui.sldIrLevel.value())

    def sbxSamplingIntervalValueChanged(self):
        if(self.tn.connected):
            self.timerReadAls.stop()
            self.timerReadAls.setInterval(self.ui.sbxSamplingInterval.value())
            self.timerReadAls.start()
            

class AlsTelnet(Telnet):
    def __init__(self):
        super().__init__()
        self.connected = False
        self.alsLastReading = 0

    def connect(self):
        try:
            self.open('10.1.0.2', timeout=5)
        except socket.error:
            self.close()
        else:
            self.connected = True
            self.read_until(b'login: ')
            self.write(b'root\n')
    
    def readAlsLevel(self):
        # read als level, parse and return the integer value
        self.write(b'nanit_hwtest lgt\n')
        while(1):
            time.sleep(10/1000)
            data = self.read_very_eager().decode('ascii')
            if(data != ''):
                if(re.search('0x[0-9a-f]+', data)):
                    self.alsLastReading = int(re.search('0x[0-9a-f]+', data).group(0), 16)
                    break
        
    
    def setIrLevel(self, level=0):
        # write irl level, argument is in range 0-10, need multiply 10
        self.write(b'nanit_hwtest irl ' + str(level * 10).encode('ascii') + b'\n')

    def disconnect(self):
        self.connected = False
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = AlsGui()
    sys.exit(app.exec_())


