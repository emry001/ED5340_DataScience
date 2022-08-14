from uislider4 import Ui_Plotter
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QFileDialog, QTextEdit, QSlider
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
import warnings

# # runtimewarning error comes due to nans in the s array (y axis) (due to raising of negative number to fractional powers)
warnings.simplefilter(action = "ignore", category = RuntimeWarning)

class MplCanvas(FigureCanvas):
	def __init__(self, parent=None, width=1.5, height=3, dpi=100):
	 #def __init__(self, *args, **kwargs):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		super(MplCanvas, self).__init__(fig)
		fig.tight_layout()


class plotwindow(QtWidgets.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.ui = Ui_Plotter()
		self.ui.setupUi(self)

		self.canvas = MplCanvas(self, width=1.5, height=3, dpi=100)
		self.toolbar = Navi(self.canvas, self)
		#print("1")
		self.ui.horizontalLayout_7.addWidget(self.toolbar, 1)
		self.ui.horizontalLayout_2.addWidget(self.canvas, 1)

		self.ui.plot_button.clicked.connect(self.plotbut)
		self.ui.clear_button.clicked.connect(self.clearbut)
		self.ui.setsliders_button.clicked.connect(self.setsliders)
		self.ui.power_slider.valueChanged.connect(self.plotbut)
		self.ui.stepsize_slider.valueChanged.connect(self.plotbut)

	def setsliders(self):

		minpower = float(self.ui.minpower_edit.text())
		maxpower = float(self.ui.maxpower_edit.text())
		powerintsize = float(self.ui.powerintsize_edit.text())
		minstepsize = float(self.ui.minstepsize_edit.text())
		maxstepsize = float(self.ui.maxstepsize_edit.text())
		stepsizeintsize = float(self.ui.stepsizeintsize_edit.text())

		if maxpower>minpower and powerintsize<(maxpower-minpower) and powerintsize>0  and maxstepsize>minstepsize and stepsizeintsize>0 and stepsizeintsize<(maxstepsize-minstepsize):
			self.ui.power_slider.setMinimum(minpower/powerintsize)
			self.ui.power_slider.setMaximum(maxpower/powerintsize)
			self.ui.power_slider.setTickInterval(1)
			self.ui.power_slider.setTickPosition(QSlider.TicksBelow)

			self.ui.stepsize_slider.setMinimum(minstepsize/stepsizeintsize)
			self.ui.stepsize_slider.setMaximum(maxstepsize/stepsizeintsize)
			self.ui.stepsize_slider.setTickInterval(1)
			self.ui.stepsize_slider.setTickPosition(QSlider.TicksBelow)

			

			if powerintsize<1:
				QtWidgets.QMessageBox.information(self, 'Note', 'You have set fractional powers via power step size. Plot will only contain the positive x values(/axis). This is due to limitations on raising a negative number to fractional powers. ')


			QtWidgets.QMessageBox.information(self, 'Success', 'Sliders have been set. You can move the pins of the sliders to obtain desired plots.')


		else:
			QtWidgets.QMessageBox.critical(self, 'Fail', 'Invaliid input')


	def plotbut(self):

		self.ui.polynomial_edit.setText(str((self.ui.power_slider.value())*float(self.ui.powerintsize_edit.text())))
		self.ui.stepsize_edit.setText(str((self.ui.stepsize_slider.value())*float(self.ui.stepsizeintsize_edit.text())))

		power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit.text())
		upperx = float(self.ui.upperx_edit.text())
		stepsize = float(self.ui.stepsize_edit.text())

		if stepsize != 0 and stepsize>=0 and stepsize<(upperx-lowerx) and upperx>lowerx:

			#print("2")
			self.showplot()
			#QtWidgets.QMessageBox.information(self, 'Success', 'Function has been plotted')


		else:
			QtWidgets.QMessageBox.critical(self, 'Fail', 'Invaliid input')

	def showplot(self):

		self.canvas.axes.clear()
		self.canvas.draw()
	
		power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit.text())
		upperx = float(self.ui.upperx_edit.text())
		stepsize = float(self.ui.stepsize_edit.text())

		t = np.arange(lowerx, upperx, stepsize)
		#print(power)
		#s = (np.float_power(t, power)).real
		#print(s)

		#runtime warning error comes here due to nans in the s array
		#s = s[np.logical_not(np.isnan(s))]
		#print(s)

		s = (t**power).real
		#print(s)
		#s = np.sin(t)
		# self.canvas.axes.clear()
		# self.canvas.draw()
		
		
		self.canvas.axes.grid(True,linestyle='--')
		# self.canvas.axes.set_xlabel('X axis')
		# self.canvas.axes.set_ylabel('Y axis')
		# self.canvas.axes.set_title('Plot')
		self.canvas.axes.plot(t, s)
		self.canvas.draw()

	def clearbut(self):

		self.canvas.axes.clear()
		self.canvas.draw()
		#self.ui.horizontalLayout_2.clear()
		#print("c")


if __name__ == '__main__':
	app = QtWidgets.QApplication([])

	widget = plotwindow()
	widget.show()

	app.exec_()