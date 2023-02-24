# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slider_plot.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Plotter(object):
    def setupUi(self, Plotter):
        Plotter.setObjectName("Plotter")
        Plotter.resize(717, 863)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Plotter)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 661, 211))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        self.formLayoutWidget = QtWidgets.QWidget(Plotter)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 610, 681, 240))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.polynomial_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.polynomial_edit.setObjectName("polynomial_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.polynomial_edit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lowerx_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lowerx_edit.setObjectName("lowerx_edit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lowerx_edit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.upperx_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.upperx_edit.setObjectName("upperx_edit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.upperx_edit)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.stepsize_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.stepsize_edit.setObjectName("stepsize_edit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.stepsize_edit)
        self.plot_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.plot_button.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.plot_button.setObjectName("plot_button")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.plot_button)
        self.clear_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.clear_button.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.clear_button.setObjectName("clear_button")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.clear_button)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.power_slider = QtWidgets.QSlider(self.formLayoutWidget)
        self.power_slider.setProperty("value", 2)
        self.power_slider.setOrientation(QtCore.Qt.Horizontal)
        self.power_slider.setObjectName("power_slider")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.power_slider)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.stepsize_slider = QtWidgets.QSlider(self.formLayoutWidget)
        self.stepsize_slider.setProperty("value", 1)
        self.stepsize_slider.setOrientation(QtCore.Qt.Horizontal)
        self.stepsize_slider.setObjectName("stepsize_slider")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.stepsize_slider)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label = QtWidgets.QLabel(Plotter)
        self.label.setGeometry(QtCore.QRect(200, 10, 325, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Plotter)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(29, 50, 661, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.formLayoutWidget_2 = QtWidgets.QWidget(Plotter)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(19, 340, 681, 262))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.minpower_edit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.minpower_edit.setObjectName("minpower_edit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.minpower_edit)
        self.maxpower_edit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.maxpower_edit.setObjectName("maxpower_edit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.maxpower_edit)
        self.powerintsize_edit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.powerintsize_edit.setObjectName("powerintsize_edit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.powerintsize_edit)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.minstepsize_edit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.minstepsize_edit.setObjectName("minstepsize_edit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.minstepsize_edit)
        self.maxstepsize_edit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.maxstepsize_edit.setObjectName("maxstepsize_edit")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.maxstepsize_edit)
        self.stepsizeintsize_edit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.stepsizeintsize_edit.setObjectName("stepsizeintsize_edit")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.stepsizeintsize_edit)
        self.setsliders_button = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.setsliders_button.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.setsliders_button.setObjectName("setsliders_button")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.setsliders_button)
        self.label_8 = QtWidgets.QLabel(Plotter)
        self.label_8.setGeometry(QtCore.QRect(20, 310, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Plotter)
        QtCore.QMetaObject.connectSlotsByName(Plotter)

    def retranslateUi(self, Plotter):
        _translate = QtCore.QCoreApplication.translate
        Plotter.setWindowTitle(_translate("Plotter", "Form"))
        self.label_2.setText(_translate("Plotter", "Power of x (obtained from slider) (eg. 2 plots x^2)"))
        self.polynomial_edit.setText(_translate("Plotter", "2"))
        self.label_3.setText(_translate("Plotter", "Lower limit of x axis"))
        self.lowerx_edit.setText(_translate("Plotter", "-5"))
        self.label_4.setText(_translate("Plotter", "Upper limit of x axis"))
        self.upperx_edit.setText(_translate("Plotter", "+5"))
        self.label_5.setText(_translate("Plotter", "Step-size (obtained from slider)"))
        self.stepsize_edit.setText(_translate("Plotter", "0.1"))
        self.plot_button.setText(_translate("Plotter", "Plot"))
        self.clear_button.setText(_translate("Plotter", "Clear Graph"))
        self.label_6.setText(_translate("Plotter", "Slider for power of x"))
        self.label_7.setText(_translate("Plotter", "Slider for step size"))
        self.label_9.setText(_translate("Plotter", "2) Plot:"))
        self.label.setText(_translate("Plotter", "Plotting Powers of x"))
        self.label_10.setText(_translate("Plotter", "Power Slider:"))
        self.label_11.setText(_translate("Plotter", "Minimum power"))
        self.label_12.setText(_translate("Plotter", "Maximum power"))
        self.label_13.setText(_translate("Plotter", "Interval size (eg, 0.1, for ticks at 2, 2.1, 2.2, etc.) (>0) "))
        self.minpower_edit.setText(_translate("Plotter", "0"))
        self.maxpower_edit.setText(_translate("Plotter", "10"))
        self.powerintsize_edit.setText(_translate("Plotter", "1"))
        self.label_14.setText(_translate("Plotter", "Step-size Slider:"))
        self.label_15.setText(_translate("Plotter", "Minimum step-size (>0)"))
        self.label_16.setText(_translate("Plotter", "Maximum step-size"))
        self.label_17.setText(_translate("Plotter", "Interval size (eg, 0.1, for ticks at 2, 2.1, 2.2, etc.) (>0)"))
        self.minstepsize_edit.setText(_translate("Plotter", "0.1"))
        self.maxstepsize_edit.setText(_translate("Plotter", "1"))
        self.stepsizeintsize_edit.setText(_translate("Plotter", "0.001"))
        self.setsliders_button.setText(_translate("Plotter", "Set Sliders"))
        self.label_8.setText(_translate("Plotter", "1) Set up the sliders:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Plotter = QtWidgets.QWidget()
    ui = Ui_Plotter()
    ui.setupUi(Plotter)
    Plotter.show()
    sys.exit(app.exec_())