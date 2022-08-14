from interface import Ui_Plotter
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QFileDialog, QTextEdit, QPlainTextEdit, QTabWidget, QWidget, QSlider
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
	def __init__(self, parent=None, width=5, height=4, dpi=100):
	 #def __init__(self, *args, **kwargs):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		super(MplCanvas, self).__init__(fig)
		fig.tight_layout()


class plotwindow(QtWidgets.QWidget):

	i = 0

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.ui = Ui_Plotter()
		self.ui.setupUi(self)

		#self.ui.scroll = scrollArea()

		# exsearch tab
		self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
		self.toolbar = Navi(self.canvas, self)
		# bounding phase tab
		self.canvas2 = MplCanvas(self, width=5, height=4, dpi=100)
		self.toolbar2 = Navi(self.canvas2, self)
		# interval halving tab
		self.canvas3 = MplCanvas(self, width=5, height=4, dpi=100)
		self.toolbar3 = Navi(self.canvas3, self)
		# fibonacci search tab
		self.canvas4 = MplCanvas(self, width=5, height=4, dpi=100)
		self.toolbar4 = Navi(self.canvas4, self)
		# golden section
		self.canvas5 = MplCanvas(self, width=5, height=4, dpi=100)
		self.toolbar5 = Navi(self.canvas5, self)
		# newton raphson
		self.canvas6 = MplCanvas(self, width=5, height=4, dpi=100)
		self.toolbar6 = Navi(self.canvas6, self)
		# bisection
		self.canvas7 = MplCanvas(self, width=5, height=4, dpi=100)
		self.toolbar7 = Navi(self.canvas7, self)
		# secant
		self.canvas8 = MplCanvas(self, width=5, height=4, dpi=100)
		self.toolbar8 = Navi(self.canvas8, self)
		# cubic search
		self.canvas9 = MplCanvas(self, width=5, height=4, dpi=100)
		self.toolbar9 = Navi(self.canvas9, self)

		# setting toolbars in position
		self.ui.horizontalLayout_7.addWidget(self.toolbar, 1)
		self.ui.horizontalLayout_8.addWidget(self.toolbar2, 1)
		self.ui.horizontalLayout_9.addWidget(self.toolbar3, 1)
		self.ui.horizontalLayout_10.addWidget(self.toolbar4, 1)
		self.ui.horizontalLayout_11.addWidget(self.toolbar5, 1)
		self.ui.horizontalLayout_12.addWidget(self.toolbar6, 1)
		self.ui.horizontalLayout_14.addWidget(self.toolbar7, 1)
		self.ui.horizontalLayout_16.addWidget(self.toolbar8, 1)
		self.ui.horizontalLayout_18.addWidget(self.toolbar9, 1)

		# setting canvases in position
		self.ui.horizontalLayout_2.addWidget(self.canvas, 1)
		self.ui.horizontalLayout_3.addWidget(self.canvas2, 1)
		self.ui.horizontalLayout_4.addWidget(self.canvas3, 1)
		self.ui.horizontalLayout_5.addWidget(self.canvas4, 1)
		self.ui.horizontalLayout_6.addWidget(self.canvas5, 1)
		self.ui.horizontalLayout_13.addWidget(self.canvas6, 1)
		self.ui.horizontalLayout_15.addWidget(self.canvas7, 1)
		self.ui.horizontalLayout_17.addWidget(self.canvas8, 1)
		self.ui.horizontalLayout_19.addWidget(self.canvas9, 1)

		# exsearchtab
		self.ui.plot_button.clicked.connect(self.SubmitInput_ExSearch)
		self.ui.clear_button.clicked.connect(self.ClearBut_ExSearch)
		self.ui.final_button.clicked.connect(self.FinalBut_ExSearch)
		self.ui.next_button.clicked.connect(self.StepBut_ExSearch)
		self.ui.disp_edit.setText('')
		self.ui.setslider_button.clicked.connect(self.SettingSlider_ExSearch)

		# bounding phase tab
		self.ui.plot_button_2.clicked.connect(self.SubmitInput_BPhase)
		self.ui.clear_button_2.clicked.connect(self.ClearBut_BPhase)
		self.ui.final_button_2.clicked.connect(self.FinalBut_BPhase)
		self.ui.next_button_2.clicked.connect(self.StepBut_BPhase)
		self.ui.disp_edit_2.setText('')
		self.ui.setslider_button_2.clicked.connect(self.SettingSlider_BPhase)

		# interval halving
		self.ui.plot_button_3.clicked.connect(self.SubmitInput_IntHalving)
		self.ui.clear_button_3.clicked.connect(self.ClearBut_IntHalving)
		self.ui.final_button_3.clicked.connect(self.FinalBut_IntHalving)
		self.ui.next_button_3.clicked.connect(self.StepBut_IntHalving)
		self.ui.disp_edit_3.setText('')
		self.ui.setslider_button_3.clicked.connect(self.SettingSlider_IntHalving)

		# fibonacci search
		self.ui.plot_button_4.clicked.connect(self.SubmitInput_FibSearch)
		self.ui.clear_button_4.clicked.connect(self.ClearBut_FibSearch)
		self.ui.final_button_4.clicked.connect(self.FinalBut_FibSearch)
		self.ui.next_button_4.clicked.connect(self.StepBut_FibSearch)
		self.ui.disp_edit_4.setText('')
		self.ui.setslider_button_4.clicked.connect(self.SettingSlider_FibSearch)

		# golden section
		self.ui.plot_button_5.clicked.connect(self.SubmitInput_GoldSec)
		self.ui.clear_button_5.clicked.connect(self.ClearBut_GoldSec)
		self.ui.final_button_5.clicked.connect(self.FinalBut_GoldSec)
		self.ui.next_button_5.clicked.connect(self.StepBut_GoldSec)
		self.ui.disp_edit_5.setText('')
		self.ui.setslider_button_5.clicked.connect(self.SettingSlider_GoldSec)

		# newton raphson
		self.ui.plot_button_6.clicked.connect(self.SubmitInput_NewtonRaphson)
		self.ui.clear_button_6.clicked.connect(self.ClearBut_NewtonRaphson)
		self.ui.final_button_6.clicked.connect(self.FinalBut_NewtonRaphson)
		self.ui.next_button_6.clicked.connect(self.StepBut_NewtonRaphson)
		self.ui.disp_edit_6.setText('')
		self.ui.setslider_button_6.clicked.connect(self.SettingSlider_NewtonRaphson)

		# bisection
		self.ui.plot_button_7.clicked.connect(self.SubmitInput_Bisection)
		self.ui.clear_button_7.clicked.connect(self.ClearBut_Bisection)
		self.ui.final_button_7.clicked.connect(self.FinalBut_Bisection)
		self.ui.next_button_7.clicked.connect(self.StepBut_Bisection)
		self.ui.disp_edit_7.setText('')
		self.ui.setslider_button_7.clicked.connect(self.SettingSlider_Bisection)

		# secant
		self.ui.plot_button_8.clicked.connect(self.SubmitInput_Secant)
		self.ui.clear_button_8.clicked.connect(self.ClearBut_Secant)
		self.ui.final_button_8.clicked.connect(self.FinalBut_Secant)
		self.ui.next_button_8.clicked.connect(self.StepBut_Secant)
		self.ui.disp_edit_8.setText('')
		self.ui.setslider_button_8.clicked.connect(self.SettingSlider_Secant)

		# cubic search
		self.ui.plot_button_9.clicked.connect(self.SubmitInput_CubicSearch)
		self.ui.clear_button_9.clicked.connect(self.ClearBut_CubicSearch)
		self.ui.final_button_9.clicked.connect(self.FinalBut_CubicSearch)
		self.ui.next_button_9.clicked.connect(self.StepBut_CubicSearch)
		self.ui.disp_edit_9.setText('')
		self.ui.setslider_button_9.clicked.connect(self.SettingSlider_CubicSearch)


		self.ui.returnhome_button.clicked.connect(self.rethome_button)
		# home tab connection to various tabs
		self.ui.exsearch_button.clicked.connect(self.exsearchbut)
		self.ui.bp_button.clicked.connect(self.bpbut)
		self.ui.interval_halving_button.clicked.connect(self.ihb_button)
		self.ui.fsearch_button.clicked.connect(self.fib_button)
		self.ui.gss_button.clicked.connect(self.golden_button)
		self.ui.nr_button.clicked.connect(self.newton_button)
		self.ui.bisection_button.clicked.connect(self.bis_button)
		self.ui.secant_button.clicked.connect(self.sec_button)
		self.ui.cubicsearch_button.clicked.connect(self.cubsearch_button)

	def rethome_button(self):
		self.ui.Tabs.setCurrentIndex(0)

	def exsearchbut(self):
		self.ui.Tabs.setCurrentIndex(1)

	def bpbut(self):
		self.ui.Tabs.setCurrentIndex(2)

	def ihb_button(self):
		self.ui.Tabs.setCurrentIndex(3)

	def fib_button(self):
		self.ui.Tabs.setCurrentIndex(4)

	def golden_button(self):
		self.ui.Tabs.setCurrentIndex(5)

	def newton_button(self):
		self.ui.Tabs.setCurrentIndex(6)

	def bis_button(self):
		self.ui.Tabs.setCurrentIndex(7)

	def sec_button(self):
		self.ui.Tabs.setCurrentIndex(8)

	def cubsearch_button(self):
		self.ui.Tabs.setCurrentIndex(9)

	def funnc(self, x):
		f = x**2 + 54/x
		return f

	# derivative of funcc
	def funncdash(self,x):
		f = 2*x - 54/(x**2)
		return f


	###############################################################################################################################################################
	#1  EXHAUATIVE SEARCH Tab
	###############################################################################################################################################################

	def StepBut_ExSearch(self):

		lowerx = float(self.ui.lowerx_edit.text())
		upperx = float(self.ui.upperx_edit.text())
		stepsize = float(self.ui.stepsize_edit.text())

		i = float(self.ui.iterationnumber_label.text())
		delta = stepsize
		if i == 0:
			
			global x1
			global x2
			global x3
			x1 = lowerx
			x2 = lowerx + delta
			x3 = x2 +delta
		
		cont = 1

		if x3<= upperx and cont==1 and i<=k-1:

			self.ClearBut_ExSearch()
			t = np.arange(lowerx, upperx, stepsize)
			s = self.funnc(t)
			#s = t**2 + 54/t
			self.canvas.axes.grid(True,linestyle='--')
			self.canvas.axes.plot(t, s)
			self.canvas.axes.axvline(x1, 0, 1, label='x1', color='r', linestyle='--')
			self.canvas.axes.axvline(x2, 0, 1, label='x2', color='g', linestyle='--')
			self.canvas.axes.axvline(x3, 0, 1, label='x3', color='r', linestyle='--')
			self.canvas.draw_idle()

			i = i+1

			self.ui.disp_edit.clear()
			self.ui.iterationnumber_label.setText(str(i))
			self.ui.stepslider.setValue(i)
			str1 = "Iteration " + str(i) +  " \n"
			#print(str1)

			self.ui.disp_edit.append(str1)

			f1 = self.funnc(x1)
			f2 = self.funnc(x2)
			f3 = self.funnc(x3)
			#f1 = x1**2 + 54/x1
			#f2 = x2**2 + 54/x2
			#f3 = x3**2 + 54/x3
			str2 = "x1 =" + str(x1) + " \n"
			self.ui.disp_edit.append(str2)
			self.ui.disp_edit.append("x2 =" + str(x2) + " \n")
			self.ui.disp_edit.append("x3 ="+ str(x3)+ " \n")
			self.ui.disp_edit.append("f(x1) ="+ str(f1)+ " \n")
			self.ui.disp_edit.append("f(x2) ="+ str(f2)+ " \n")
			self.ui.disp_edit.append("f(x3) ="+ str(f3)+ " \n")

			if f1>= f2 and f2<=f3:
				ans = [x1,x3]
				cont = 0
				QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')
				
			else:
				x1 = x2
				x2 = x3
				x3 = x2 + delta
				#print("here")


		#self.ui.disp_edit.append("Answer interval = "+ str(ans)+ " \n")

	def SubmitInput_ExSearch(self):


		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit.text())
		upperx = float(self.ui.upperx_edit.text())
		stepsize = float(self.ui.stepsize_edit.text())

		if lowerx!=0 and stepsize != 0 and stepsize>=0 and stepsize<(upperx-lowerx) and upperx>lowerx:

			#print("2")
			self.ShowPlot_ExSearch()

			QtWidgets.QMessageBox.information(self, 'Success', 'Function has been plotted. Next: Exhaustive Search Method. Click on Enable Slider button')
			
			#self.settingslider()
			

		else:
			QtWidgets.QMessageBox.critical(self, 'Fail', 'Invaliid input')

	def ShowPlot_ExSearch(self):

		self.ui.iterationnumber_label.setText(str(0))
		self.ui.stepslider.setValue(0)
		self.ui.disp_edit.clear()
		self.ui.finalresult_edit.clear()
		#self.ui.iterationnumber_label.clear()
		k = 0 

		self.FinalBut_ExSearch()

		self.canvas.axes.clear()
		self.canvas.draw_idle()
	
		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit.text())
		upperx = float(self.ui.upperx_edit.text())
		stepsize = float(self.ui.stepsize_edit.text())

		t = np.arange(lowerx, upperx, stepsize)
		#s = t**2 + 54/t
		s = self.funnc(t)
		#s = np.sin(t)
		# self.canvas.axes.clear()
		# self.canvas.draw()
		
		
		self.canvas.axes.grid(True,linestyle='--')
		# self.canvas.axes.set_xlabel('X axis')
		# self.canvas.axes.set_ylabel('Y axis')
		# self.canvas.axes.set_title('Plot')
		self.canvas.axes.plot(t, s)
		self.canvas.axes.axvline(lowerx, 0, 1, label='x1', color='r', linestyle='--')
		self.canvas.axes.axvline(upperx, 0, 1, label='x3', color='r', linestyle='--')
		self.canvas.draw_idle()
		
	def SettingSlider_ExSearch(self):

		iterationtot = float(self.ui.numberoiterations_edit.text())
		#print(iterationtot)
		lower = float(1)
		self.ui.stepslider.setMinimum(lower)
		#print("a")
		self.ui.stepslider.setMaximum(iterationtot)
		#print("b")
		self.ui.stepslider.setTickInterval(1)
		#print("c")
		self.ui.stepslider.setTickPosition(QSlider.TicksBelow)
		# print("d")
		self.ui.numberoiterations_edit.setText(str(iterationtot))
		#print("slider set")
		QtWidgets.QMessageBox.information(self, 'Success', 'Slider has been set (only for display purposes). Click on Next Steps button')

	def ClearBut_ExSearch(self):

		self.canvas.axes.clear()
		self.canvas.draw_idle()
		#self.ui.horizontalLayout_2.clear()
		#print("c")

	def FinalBut_ExSearch(self):

		lowerx = float(self.ui.lowerx_edit.text())
		upperx = float(self.ui.upperx_edit.text())
		stepsize = float(self.ui.stepsize_edit.text())

		delta = stepsize
		x1 = lowerx
		x2 = lowerx + delta
		x3 = x2 +delta
		cont = 1
		global k
		k = 0

		while x3<= upperx and cont==1:

			k = k+1
			#print("Iteration", i)
			
			f1 = self.funnc(x1)
			f2 = self.funnc(x2)
			f3 = self.funnc(x3)
			# f1 = x1**2 + 54/x1
			# f2 = x2**2 + 54/x2
			# f3 = x3**2 + 54/x3	
			if f1>= f2 and f2<=f3:
				ans = [x1,x3]
				cont = 0
				

			else:
				x1 = x2
				x2 = x3
				x3 = x2 + delta
				#print("here")

		self.ui.numberoiterations_edit.setText(str(k))
		self.ui.finalresult_edit.setText("Answer interval = "+ str(ans)+ " \n")

	###############################################################################################################################################################
	#2  BOUNDING PHASE Tab
	###############################################################################################################################################################

	def StepBut_BPhase(self):

		lowerx = float(self.ui.lowerx_edit_2.text())
		upperx = float(self.ui.upperx_edit_2.text())
		stepsize = float(self.ui.stepsize_edit_2.text())
		i = float(self.ui.iterationnumber_label_2.text())

		guessbp = float(self.ui.initialguess_edit.text())
		global cont
		global k3
		global x1
		global x2
		global deel
		k2 = float(self.ui.numberoiterations_edit_2.text())

		# f1 = funnc(guessbp - np.abs(delta))
		# f2 = funnc(guessbp)
		# f3 = funnc(guessbp + np.abs(delta))
		if i==0:

			delta = stepsize
			#print(delta)
			x1 = guessbp - np.abs(delta)
			x2 = guessbp
			x3 = guessbp + np.abs(delta)

			# f1 = x1**2 + 54/x1
			# f2 = x2**2 + 54/x2
			# f3 = x3**2 + 54/x3
			f1 = self.funnc(x1)
			f2 = self.funnc(x2)
			f3 = self.funnc(x3)

			if f1>=f2 and f2>=f3:
				delta = delta
			else:
				delta = -delta
				#print("heeer")
			deel = delta
		
			# global k2
			k3 = 0
			# x = []
			# x.append(guessbp)
			x1 = guessbp
			x2 = x1 + (2**k3)*delta

		cont = 1
		delta = deel
		# print('deel')
		# print(delta)

		if i==k2:
			
			QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')
			#cont = 0
		

		#if x3<= upperx and x3>=lowerx and cont==1 and i<=k2:
		if cont==1 and i<=k2-1:

			self.ClearBut_BPhase()
			t = np.arange(lowerx, upperx, stepsize)
			s = self.funnc(t)
			# s = t**2 + 54/t
			self.canvas2.axes.grid(True,linestyle='--')
			self.canvas2.axes.plot(t, s)
			

			self.canvas2.axes.axvline(x1, 0, 1, label='x1', color='r', linestyle='--')
			self.canvas2.axes.axvline(x2, 0, 1, label='x2', color='g', linestyle='--')
			#self.canvas2.axes.axvline(x3, 0, 1, label='x3', color='r', linestyle='--')
			self.canvas2.draw_idle()

			i = i+1
			# print(i)

			self.ui.disp_edit_2.clear()
			self.ui.iterationnumber_label_2.setText(str(i))
			self.ui.stepslider_2.setValue(i)
			str1 = "Iteration " + str(i) +  " \n"
			#print(str1)

			self.ui.disp_edit_2.append(str1)

			# f1 = x1**2 + 54/x1
			# f2 = x2**2 + 54/x2
			f1 = self.funnc(x1)
			f2 = self.funnc(x2)
			
			#f3 = x3**2 + 54/x3
			str2 = "x1 =" + str(x1) + " \n"
			self.ui.disp_edit_2.append(str2)
			self.ui.disp_edit_2.append("x2 =" + str(x2) + " \n")
			#self.ui.disp_edit_2.append("x3 ="+ str(x3)+ " \n")
			self.ui.disp_edit_2.append("f(x1) ="+ str(f1)+ " \n")
			self.ui.disp_edit_2.append("f(x2) ="+ str(f2)+ " \n")
			#self.ui.disp_edit_2.append("f(x3) ="+ str(f3)+ " \n")


			
			

			#x.append(x[k3] + (2**k3)*delta)

			#f4 = (x[k3+1])**2 + 54/(x[k3+1])
			#f5 = (x[k3])**2 + 54/(x[k3])
			# f4 = x2**2 + 54/x2
			# f5 = x1**2 + 54/x1
			f4 = self.funnc(x2)
			f5 = self.funnc(x1)
			

			# print(f4)
			# print(f5)

			if f4<f5:
				
				# x1 = x[k3-1]
				# x2 = x[k3]
				# x3 = x[k3+1]
				# k3 = k3+1
				# print(k3)
				x1 = x2
				#x3 = x2
				

				k3 = k3+1
				x2 = x1 + (2**k3)*delta
				#print(k3)



			else:
				# ans = [x[k3-1], x[k3+1]]
				
				QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')
				cont=0

		#self.ui.disp_edit.append("Answer interval = "+ str(ans)+ " \n")

	def SubmitInput_BPhase(self):


		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_2.text())
		upperx = float(self.ui.upperx_edit_2.text())
		stepsize = float(self.ui.stepsize_edit_2.text())

		if lowerx!=0 and stepsize != 0 and stepsize>=0 and stepsize<(upperx-lowerx) and upperx>lowerx:

			#print("2")
			self.ShowPlot_BPhase()

			QtWidgets.QMessageBox.information(self, 'Success', 'Function has been plotted. Next: Bounding Phase Method. Click on Enable Slider button')
			
			#self.settingslider()
			

		else:
			QtWidgets.QMessageBox.critical(self, 'Fail', 'Invaliid input')

	def ShowPlot_BPhase(self):

		self.ui.iterationnumber_label_2.setText(str(0))
		self.ui.stepslider_2.setValue(0)
		self.ui.disp_edit_2.clear()
		self.ui.finalresult_edit_2.clear()
		#self.ui.iterationnumber_label.clear()
		k2 = 0 
		k3 = 0

		self.FinalBut_BPhase()
		

		self.canvas2.axes.clear()
		self.canvas2.draw_idle()
	
		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_2.text())
		upperx = float(self.ui.upperx_edit_2.text())
		stepsize = float(self.ui.stepsize_edit_2.text())

		t = np.arange(lowerx, upperx, stepsize)
		s = self.funnc(t)
		# s = t**2 + 54/t
		#s = np.sin(t)
		# self.canvas.axes.clear()
		# self.canvas.draw()
		
		
		self.canvas2.axes.grid(True,linestyle='--')
		# self.canvas.axes.set_xlabel('X axis')
		# self.canvas.axes.set_ylabel('Y axis')
		# self.canvas.axes.set_title('Plot')
		self.canvas2.axes.plot(t, s)
		self.canvas2.axes.axvline(lowerx, 0, 1, label='x1', color='r', linestyle='--')
		self.canvas2.axes.axvline(upperx, 0, 1, label='x3', color='r', linestyle='--')
		self.canvas2.draw_idle()
		
	def SettingSlider_BPhase(self):

		iterationtot = float(self.ui.numberoiterations_edit_2.text())
		#print(iterationtot)
		lower = float(1)
		self.ui.stepslider_2.setMinimum(lower)
		#print("a")
		self.ui.stepslider_2.setMaximum(iterationtot)
		#print("b")
		self.ui.stepslider_2.setTickInterval(1)
		#print("c")
		self.ui.stepslider_2.setTickPosition(QSlider.TicksBelow)
		# print("d")
		self.ui.numberoiterations_edit_2.setText(str(iterationtot))
		#print("slider set")
		QtWidgets.QMessageBox.information(self, 'Success', 'Slider has been set (only for display purposes). Click on Next Steps button')

	def ClearBut_BPhase(self):

		self.canvas2.axes.clear()
		self.canvas2.draw_idle()
		#self.ui.horizontalLayout_2.clear()
		#print("c")

	def FinalBut_BPhase(self):

		lowerx = float(self.ui.lowerx_edit_2.text())
		upperx = float(self.ui.upperx_edit_2.text())
		stepsize = float(self.ui.stepsize_edit_2.text())
		guessbp = float(self.ui.initialguess_edit.text())
		delta = stepsize

		# f1 = funnc(guessbp - np.abs(delta))
		# f2 = funnc(guessbp)
		# f3 = funnc(guessbp + np.abs(delta))
		x1 = guessbp - np.abs(delta)
		x2 = guessbp
		x3 = guessbp + np.abs(delta)

		# f1 = x1**2 + 54/x1
		# f2 = x2**2 + 54/x2
		# f3 = x3**2 + 54/x3
		f1 = self.funnc(x1)
		f2 = self.funnc(x2)
		f3 = self.funnc(x3)

		if f1>=f2 and f2>=f3:
			delta = delta
		else:
			delta = -delta
			#print("heeer")

		cont = 1
		global k2
		k2 = 0
		x = []
		x.append(guessbp)

		while x[k2]<= upperx and x[k2]>=lowerx and cont==1:

			x.append(x[k2] + (2**k2)*delta)
			# f4 = (x[k2+1])**2 + 54/(x[k2+1])
			# f5 = (x[k2])**2 + 54/(x[k2])
			f4 = self.funnc(x[k2+1])
			f5 = self.funnc(x[k2])

			# print(f4)
			# print(f5)

			if f4<f5:
				k2 = k2+1
				#print(k)

			else:
				ans = [x[k2-1], x[k2+1]]
				cont=0
				#print(ans)


		self.ui.numberoiterations_edit_2.setText(str(k2))
		self.ui.finalresult_edit_2.setText("Answer interval = "+ str(ans)+ " \n")

	###############################################################################################################################################################
	#3  INTERVAL HALVING Tab
	###############################################################################################################################################################

	def StepBut_IntHalving(self):

		i = float(self.ui.iterationnumber_label_3.text())
		stepsize = float(self.ui.stepsize_edit_3.text())
		lowerx = float(self.ui.lowerx_edit_3.text())
		upperx = float(self.ui.upperx_edit_3.text())
		global cont

		if i==0:
			cont = 1
			global a
			global b
			global L
			a = lowerx
			b = upperx
			L = a-b

		if i == kinthalf:
			QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')


		if cont==1 and i<=kinthalf-1:

			global x1
			global x2
			global xm
			x1 = a + L/4
			x2 = b - L/4
			xm = (a + b)/2

			#print("Iteration", i)
			self.ClearBut_IntHalving()
			t = np.arange(lowerx, upperx, stepsize)
			s = self.funnc(t)
			# s = t**2 + 54/t
			self.canvas3.axes.grid(True,linestyle='--')
			self.canvas3.axes.plot(t, s)
			self.canvas3.axes.axvline(x1, 0, 1, label='x1', color='r', linestyle='--')
			self.canvas3.axes.axvline(xm, 0, 1, label='x2', color='g', linestyle='--')
			self.canvas3.axes.axvline(x2, 0, 1, label='x3', color='r', linestyle='--')
			self.canvas3.draw_idle()

			i = i+1

			self.ui.disp_edit_3.clear()
			self.ui.iterationnumber_label_3.setText(str(i))
			self.ui.stepslider_3.setValue(i)
			str1 = "Iteration " + str(i) +  " \n"
			#print(str1)

			self.ui.disp_edit_3.append(str1)

			# f1 = x1**2 + 54/x1
			# f2 = x2**2 + 54/x2
			# fxm = xm**2 + 54/xm	
			f1 = self.funnc(x1)
			f2 = self.funnc(x2)
			fxm = self.funnc(xm)


			str2 = "x1 =" + str(x1) + " \n"
			self.ui.disp_edit_3.append(str2)
			self.ui.disp_edit_3.append("x2 =" + str(x2) + " \n")
			self.ui.disp_edit_3.append("xm ="+ str(xm)+ " \n")
			self.ui.disp_edit_3.append("f(x1) ="+ str(f1)+ " \n")
			self.ui.disp_edit_3.append("f(x2) ="+ str(f2)+ " \n")
			self.ui.disp_edit_3.append("f(xm) ="+ str(fxm)+ " \n")
			

			if f1<=fxm:
				b = xm
				xm = x1
				if np.abs(b-a)<=stepsize:
					ans = [a, b]
					QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')
					#print('here1')
					cont = 0

			else:

				if f2<=fxm:
					a = xm
					xm = x2
					if np.abs(b-a)<=stepsize:
						ans = [a, b]
						QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')
						#print('here2')
						cont = 0
				else:
					a = x1
					b = x2

	def SubmitInput_IntHalving(self):


		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_3.text())
		upperx = float(self.ui.upperx_edit_3.text())
		stepsize = float(self.ui.stepsize_edit_3.text())

		if lowerx!=0 and stepsize != 0 and stepsize>=0 and stepsize<(upperx-lowerx) and upperx>lowerx:

			#print("2")
			self.ShowPlot_IntHalving()

			QtWidgets.QMessageBox.information(self, 'Success', 'Function has been plotted. Next: Interval Halving Method. Click on Enable Slider button')
			
			#self.settingslider()
			

		else:
			QtWidgets.QMessageBox.critical(self, 'Fail', 'Invaliid input')

	def ShowPlot_IntHalving(self):

		self.ui.iterationnumber_label_3.setText(str(0))
		self.ui.stepslider_3.setValue(0)
		self.ui.disp_edit_3.clear()
		self.ui.finalresult_edit_3.clear()
		#self.ui.iterationnumber_label.clear()
		k = 0 

		self.FinalBut_IntHalving()

		self.canvas3.axes.clear()
		self.canvas3.draw_idle()
	
		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_3.text())
		upperx = float(self.ui.upperx_edit_3.text())
		stepsize = float(self.ui.stepsize_edit_3.text())

		t = np.arange(lowerx, upperx, stepsize)
		s = self.funnc(t)
		# s = t**2 + 54/t
		#s = np.sin(t)
		# self.canvas.axes.clear()
		# self.canvas.draw()
		
		
		self.canvas3.axes.grid(True,linestyle='--')
		# self.canvas.axes.set_xlabel('X axis')
		# self.canvas.axes.set_ylabel('Y axis')
		# self.canvas.axes.set_title('Plot')
		self.canvas3.axes.plot(t, s)
		self.canvas3.axes.axvline(lowerx, 0, 1, label='x1', color='r', linestyle='--')
		self.canvas3.axes.axvline(upperx, 0, 1, label='x3', color='r', linestyle='--')
		self.canvas3.draw_idle()		

	def SettingSlider_IntHalving(self):

		iterationtot = float(self.ui.numberoiterations_edit_3.text())
		#print(iterationtot)
		lower = float(1)
		self.ui.stepslider_3.setMinimum(lower)
		#print("a")
		self.ui.stepslider_3.setMaximum(iterationtot)
		#print("b")
		self.ui.stepslider_3.setTickInterval(1)
		#print("c")
		self.ui.stepslider_3.setTickPosition(QSlider.TicksBelow)
		# print("d")
		self.ui.numberoiterations_edit_3.setText(str(iterationtot))
		#print("slider set")
		QtWidgets.QMessageBox.information(self, 'Success', 'Slider has been set (only for display purposes). Click on Next Steps button')

	def ClearBut_IntHalving(self):

		self.canvas3.axes.clear()
		self.canvas3.draw_idle()
		#self.ui.horizontalLayout_2.clear()
		#print("c")

	def FinalBut_IntHalving(self):

		lowerx = float(self.ui.lowerx_edit_3.text())
		upperx = float(self.ui.upperx_edit_3.text())
		stepsize = float(self.ui.stepsize_edit_3.text())

		L = upperx - lowerx

		cont = 1
		global kinthalf
		kinthalf = 0

		while cont==1:

			kinthalf = kinthalf+1
			x1 = lowerx + L/4
			x2 = upperx - L/4
			xm = (upperx + lowerx)/2
			#print("Iteration", i)
			
			# f1 = x1**2 + 54/x1
			# f2 = x2**2 + 54/x2
			# fxm = xm**2 + 54/xm	
			f1 = self.funnc(x1)
			f2 = self.funnc(x2)
			fxm = self.funnc(xm)
			# print(f1)
			# print(f2)

			if f1<=fxm:
				upperx = xm
				xm = x1
				if np.abs(upperx-lowerx)<=stepsize:
					ans = [lowerx, upperx]
					#print('here1')
					cont = 0

			else:

				if f2<=fxm:
					lowerx = xm
					xm = x2
					if np.abs(upperx-lowerx)<=stepsize:
						ans = [lowerx, upperx]
						#print('here2')
						cont = 0
				else:
					lowerx = x1
					upperx = x2

		self.ui.numberoiterations_edit_3.setText(str(kinthalf))
		self.ui.finalresult_edit_3.setText("Answer interval = "+ str(ans)+ " \n")

	###############################################################################################################################################################
	#4	FIBONACCI SEARCH Tab
	###############################################################################################################################################################

	def StepBut_FibSearch(self):

		i = float(self.ui.iterationnumber_label_4.text())
		stepsize = float(self.ui.stepsize_edit_4.text())
		lowerx = float(self.ui.lowerx_edit_4.text())
		upperx = float(self.ui.upperx_edit_4.text())
		kmax = float(self.ui.numberoiterations_edit_4.text())
		n = int(self.ui.initialguess_edit_3.text())

		global cont

		if i==0:
			cont = 1
			global a
			global b
			global L
			a = lowerx
			b = upperx

		if i == kmax:
			QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')

		global F
		F =[]
		F.append(1)
		F.append(1)
		terms = 2

		while terms<=n+1:
			F.append(F[terms-1]+F[terms-2]) 
			terms = terms + 1

		#print(F)

		L = upperx - lowerx

		global x1
		global x2
		global kfib
		kfib = 2

		if cont==1 and i<=kmax-1 and kfib<=n:

			#print("ITERATION "+ str(kfib-2))
			# print("a " + str(a))
			# print("b " + str(b))
			if (n-kfib+1)>=0:
				Lk= (F[n-kfib+1]/F[n+1])*L
				# print([n-kfib+1])
			else:
				print("Desired accuracy cannot be obtained, increase stepsize or n")
				QtWidgets.QMessageBox.critical(self, 'Fail', 'Desired accuracy cannot be obtained, increase stepsize or n')
				cont = 0

			#print("Lk  "+ str(Lk))

			kfib = kfib +1
			x1 = a + Lk
			x2 = b - Lk
			#xm = (a + b)/2
			
			# print("x1 " + str(x1))
			# print("x2 " + str(x2))
			#print("Iteration", i)
			
			# f1 = x1**2 + 54/x1
			# f2 = x2**2 + 54/x2
			f1 = self.funnc(x1)
			f2 = self.funnc(x2)
			
			#fxm = (xm*(upperx-lowerx) + lowerx)**2 + 54/(xm*(upperx-lowerx) + lowerx)
			# print("f1 " + str(f1))
			# print("f2 " + str(f2))

			self.ClearBut_FibSearch()
			t = np.arange(lowerx, upperx, stepsize)
			s = self.funnc(t)
			# s = t**2 + 54/t
			self.canvas4.axes.grid(True,linestyle='--')
			self.canvas4.axes.plot(t, s)
			self.canvas4.axes.axvline(x1, 0, 1, label='x1', color='r', linestyle='--')
			#self.canvas4.axes.axvline(xm, 0, 1, label='x2', color='g', linestyle='--')
			self.canvas4.axes.axvline(x2, 0, 1, label='x2', color='g', linestyle='--')
			self.canvas4.draw_idle()

			i = i+1

			self.ui.disp_edit_4.clear()
			self.ui.iterationnumber_label_4.setText(str(i))
			self.ui.stepslider_4.setValue(i)
			str1 = "Iteration " + str(i) +  " \n"
			#print(str1)

			self.ui.disp_edit_4.append(str1)


			str2 = "x1 =" + str(x1) + " \n"
			self.ui.disp_edit_4.append(str2)
			self.ui.disp_edit_4.append("x2 =" + str(x2) + " \n")
			
			self.ui.disp_edit_4.append("f(x1) ="+ str(f1)+ " \n")
			self.ui.disp_edit_4.append("f(x2) ="+ str(f2)+ " \n")

			
			if f1<=f2:
				#a = x1
				b = x2
				#xm = x1
				if np.abs(b-a)<=stepsize:
					ans = [a, b]
					# print('here1')
					QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')
					cont = 0

			else:

				if f1>f2:
					#b = x2
					a = x1
					#xm = x2
					if np.abs(b-a)<=stepsize:
						ans = [a, b]
						#print('here2')
						QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')
						cont = 0
				else:
					a = x1
					b = x2

	def SubmitInput_FibSearch(self):


		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_4.text())
		upperx = float(self.ui.upperx_edit_4.text())
		stepsize = float(self.ui.stepsize_edit_4.text())

		if lowerx!=0 and stepsize != 0 and stepsize>=0 and stepsize<(upperx-lowerx) and upperx>lowerx:

			#print("2")
			self.ShowPlot_FibSearch()

			QtWidgets.QMessageBox.information(self, 'Success', 'Function has been plotted. Next: Fibonacci Search Method. Click on Enable Slider button')
			
			#self.settingslider()
			

		else:
			QtWidgets.QMessageBox.critical(self, 'Fail', 'Invaliid input')

	def ShowPlot_FibSearch(self):

		self.ui.iterationnumber_label_4.setText(str(0))
		self.ui.stepslider_4.setValue(0)
		self.ui.disp_edit_4.clear()
		self.ui.finalresult_edit_4.clear()
		#self.ui.iterationnumber_label.clear()
		k = 0 

		self.FinalBut_FibSearch()

		self.canvas4.axes.clear()
		self.canvas4.draw_idle()
	
		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_4.text())
		upperx = float(self.ui.upperx_edit_4.text())
		stepsize = float(self.ui.stepsize_edit_4.text())

		t = np.arange(lowerx, upperx, stepsize)
		s = self.funnc(t)
		# s = t**2 + 54/t
		#s = np.sin(t)
		# self.canvas.axes.clear()
		# self.canvas.draw()
		
		
		self.canvas4.axes.grid(True,linestyle='--')
		# self.canvas.axes.set_xlabel('X axis')
		# self.canvas.axes.set_ylabel('Y axis')
		# self.canvas.axes.set_title('Plot')
		self.canvas4.axes.plot(t, s)
		self.canvas4.axes.axvline(lowerx, 0, 1, label='x1', color='r', linestyle='--')
		self.canvas4.axes.axvline(upperx, 0, 1, label='x3', color='r', linestyle='--')
		self.canvas4.draw_idle()		

	def SettingSlider_FibSearch(self):

		iterationtot = float(self.ui.numberoiterations_edit_4.text())
		#print(iterationtot)
		lower = float(1)
		self.ui.stepslider_4.setMinimum(lower)
		#print("a")
		self.ui.stepslider_4.setMaximum(iterationtot)
		#print("b")
		self.ui.stepslider_4.setTickInterval(1)
		#print("c")
		self.ui.stepslider_4.setTickPosition(QSlider.TicksBelow)
		# print("d")
		self.ui.numberoiterations_edit_4.setText(str(iterationtot))
		#print("slider set")
		QtWidgets.QMessageBox.information(self, 'Success', 'Slider has been set (only for display purposes). Click on Next Steps button')

	def ClearBut_FibSearch(self):

		self.canvas4.axes.clear()
		self.canvas4.draw_idle()
		#self.ui.horizontalLayout_2.clear()
		#print("c")

	def FinalBut_FibSearch(self):

		lowerx = float(self.ui.lowerx_edit_4.text())
		upperx = float(self.ui.upperx_edit_4.text())
		stepsize = float(self.ui.stepsize_edit_4.text())
		n = int(self.ui.initialguess_edit_3.text())

		F =[]
		F.append(1)
		F.append(1)
		terms = 2

		while terms<=n+1:
			F.append(F[terms-1]+F[terms-2]) 
			terms = terms + 1

		# print(F)

		L = upperx - lowerx
		#Lw = 1
		a = lowerx
		b = upperx
		#stepsize = stepsize/L

		cont = 1
		global kfib
		kfib = 2

		while cont==1 and kfib<=n:

			# print("ITERATION "+ str(kfib-1))
			# print("a " + str(a))
			# print("b " + str(b))
			if (n-kfib+1)>=0:
				Lk= (F[n-kfib+1]/F[n+1])*L
				# print([n-kfib+1])
			else:
				print("Desired accuracy cannot be obtained, increase stepsize or n")
				QtWidgets.QMessageBox.critical(self, 'Fail', 'Desired accuracy cannot be obtained, increase stepsize or n')
				cont = 0

			# print("Lk  "+ str(Lk))

			kfib = kfib+1
			x1 = a + Lk
			x2 = b - Lk
			#xm = (a + b)/2
			
			# print("x1 " + str(x1))
			# print("x2 " + str(x2))
			#print("Iteration", i)
			
			# f1 = x1**2 + 54/x1
			# f2 = x2**2 + 54/x2
			f1 = self.funnc(x1)
			f2 = self.funnc(x2)
			
			#fxm = (xm*(upperx-lowerx) + lowerx)**2 + 54/(xm*(upperx-lowerx) + lowerx)
			# print("f1 " + str(f1))
			# print("f2 " + str(f2))
			
			if f1<=f2:
				#a = x1
				b = x2
				#xm = x1
				if np.abs(b-a)<=stepsize:
					ans = [a, b]
					# print('here1')
					cont = 0

			else:

				if f1>f2:
					#b = x2
					a = x1
					#xm = x2
					if np.abs(b-a)<=stepsize:
						ans = [a, b]
						#print('here2')
						cont = 0
				else:
					a = x1
					b = x2

		ans = [a,b]
		#print(ans)

		self.ui.numberoiterations_edit_4.setText(str(kfib-2))
		self.ui.finalresult_edit_4.setText("Answer interval = "+ str(ans)+ " \n")

	###############################################################################################################################################################
	#5  GOLDEN SECTION Tab
	###############################################################################################################################################################

	def StepBut_GoldSec(self):

		i = float(self.ui.iterationnumber_label_5.text())
		stepsize = float(self.ui.stepsize_edit_5.text())
		lowerx = float(self.ui.lowerx_edit_5.text())
		upperx = float(self.ui.upperx_edit_5.text())
		global cont
		global x1
		global x2
		global a
		global b
		global Lw

		kgs = float(self.ui.numberoiterations_edit_5.text())

		if i==0:
			cont = 1
			a = 0
			b = 1
			#L = a-b
			#print('here')

		if i==kgs:
			QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')

		L = upperx - lowerx
		#print('here2')

		if cont==1 and i<=kgs-1:
			#stepsize = stepsize/L
			#print('hereaaa')
			kgs = kgs+1
			# print("ITERATION "+ str(kinthalf))
			# print("b " + str(b))
			# print("a " + str(a))
			Lw = b - a
			# print("Lw  "+ str(Lw))
			x1 = a + Lw*0.618
			x2 = b - Lw*0.618
			#xm = (a + b)/2
			
			# print("w1" + str(x1))
			# print("w2" + str(x2))
			#print("Iteration", i)
			f1 = self.funnc((x1*(upperx-lowerx) + lowerx))
			f2 = self.funnc((x2*(upperx-lowerx) + lowerx))
			
			
			# f1 = (x1*(upperx-lowerx) + lowerx)**2 + 54/(x1*(upperx-lowerx) + lowerx)
			# f2 = (x2*(upperx-lowerx) + lowerx)**2 + 54/(x2*(upperx-lowerx) + lowerx)

			#fxm = (xm*(upperx-lowerx) + lowerx)**2 + 54/(xm*(upperx-lowerx) + lowerx)
			# print("f1" + str(f1))
			# print("f2" + str(f2))
			
			#print("Iteration", i)
			self.ClearBut_GoldSec()
			t = np.arange(lowerx, upperx, stepsize)
			s = self.funnc(t)
			# s = t**2 + 54/t
			self.canvas5.axes.grid(True,linestyle='--')
			self.canvas5.axes.plot(t, s)
			self.canvas5.axes.axvline((x1*(upperx-lowerx) + lowerx), 0, 1, label='x1', color='r', linestyle='--')
			#self.canvas5.axes.axvline(xm, 0, 1, label='x2', color='g', linestyle='--')
			self.canvas5.axes.axvline((x2*(upperx-lowerx) + lowerx), 0, 1, label='x2', color='g', linestyle='--')
			self.canvas5.draw_idle()

			i = i+1

			self.ui.disp_edit_5.clear()
			self.ui.iterationnumber_label_5.setText(str(i))
			self.ui.stepslider_5.setValue(i)
			str1 = "Iteration " + str(i) +  " \n"
			#print(str1)

			self.ui.disp_edit_5.append(str1)

			
			str2 = "w1 =" + str(x1) + " \n"
			self.ui.disp_edit_5.append(str2)
			self.ui.disp_edit_5.append("w2 =" + str(x2) + " \n")
			#self.ui.disp_edit_5.append("xm ="+ str(xm)+ " \n")
			self.ui.disp_edit_5.append("f(w1) ="+ str(f1)+ " \n")
			self.ui.disp_edit_5.append("f(w2) ="+ str(f2)+ " \n")
			self.ui.disp_edit_5.append("x1 ="+ str((x1*(upperx-lowerx) + lowerx))+ " \n")
			self.ui.disp_edit_5.append("x2 ="+ str((x2*(upperx-lowerx) + lowerx))+ " \n")
			#self.ui.disp_edit_5.append("f(xm) ="+ str(fxm)+ " \n")

			if f1<=f2:
				a = x2
				#xm = x1
				if np.abs(b-a)<=stepsize:
					ans = [a, b]
					# print('here1')
					cont = 0

			else:

				if f1>f2:
					b = x1
					#xm = x2
					if np.abs(b-a)<=stepsize:
						ans = [a, b]
						#print('here2')
						cont = 0
				else:
					a = x1
					b = x2
			
	def SubmitInput_GoldSec(self):


		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_5.text())
		upperx = float(self.ui.upperx_edit_5.text())
		stepsize = float(self.ui.stepsize_edit_5.text())

		if lowerx!=0 and stepsize != 0 and stepsize>=0 and stepsize<(upperx-lowerx) and upperx>lowerx:

			#print("2")
			self.ShowPlot_GoldSec()

			QtWidgets.QMessageBox.information(self, 'Success', 'Function has been plotted. Next: Golden Section Method. Click on Enable Slider button')
			
			#self.settingslider()
			

		else:
			QtWidgets.QMessageBox.critical(self, 'Fail', 'Invaliid input')

	def ShowPlot_GoldSec(self):

		self.ui.iterationnumber_label_5.setText(str(0))
		self.ui.stepslider_5.setValue(0)
		self.ui.disp_edit_5.clear()
		self.ui.finalresult_edit_5.clear()
		#self.ui.iterationnumber_label.clear()
		#kgs = 0 

		self.FinalBut_GoldSec()

		self.canvas5.axes.clear()
		self.canvas5.draw_idle()
	
		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_5.text())
		upperx = float(self.ui.upperx_edit_5.text())
		stepsize = float(self.ui.stepsize_edit_5.text())

		t = np.arange(lowerx, upperx, stepsize)
		s = self.funnc(t)
		# s = t**2 + 54/t
		#s = np.sin(t)
		# self.canvas.axes.clear()
		# self.canvas.draw()
		
		
		self.canvas5.axes.grid(True,linestyle='--')
		# self.canvas.axes.set_xlabel('X axis')
		# self.canvas.axes.set_ylabel('Y axis')
		# self.canvas.axes.set_title('Plot')
		self.canvas5.axes.plot(t, s)
		self.canvas5.axes.axvline(lowerx, 0, 1, label='x1', color='r', linestyle='--')
		self.canvas5.axes.axvline(upperx, 0, 1, label='x3', color='r', linestyle='--')
		self.canvas5.draw_idle()		

	def SettingSlider_GoldSec(self):

		iterationtot = float(self.ui.numberoiterations_edit_5.text())
		#print(iterationtot)
		lower = float(1)
		self.ui.stepslider_5.setMinimum(lower)
		#print("a")
		self.ui.stepslider_5.setMaximum(iterationtot)
		#print("b")
		self.ui.stepslider_5.setTickInterval(1)
		#print("c")
		self.ui.stepslider_5.setTickPosition(QSlider.TicksBelow)
		# print("d")
		self.ui.numberoiterations_edit_5.setText(str(iterationtot))
		#print("slider set")
		QtWidgets.QMessageBox.information(self, 'Success', 'Slider has been set (only for display purposes). Click on Next Steps button')

	def ClearBut_GoldSec(self):

		self.canvas5.axes.clear()
		self.canvas5.draw_idle()
		#self.ui.horizontalLayout_2.clear()
		#print("c")

	def FinalBut_GoldSec(self):

		lowerx = float(self.ui.lowerx_edit_5.text())
		upperx = float(self.ui.upperx_edit_5.text())
		stepsize = float(self.ui.stepsize_edit_5.text())

		L = upperx - lowerx
		#Lw = 1
		a = 0
		b = 1
		#stepsize = stepsize/L

		cont = 1
		global kgs
		kgs = 0

		while cont==1:

			kgs = kgs+1
			# print("ITERATION "+ str(kinthalf))
			# print("b " + str(b))
			# print("a " + str(a))
			Lw = b - a
			# print("Lw  "+ str(Lw))
			x1 = a + Lw*0.618
			x2 = b - Lw*0.618
			#xm = (a + b)/2
			
			# print("w1" + str(x1))
			# print("w2" + str(x2))
			#print("Iteration", i)
			f1 = self.funnc((x1*(upperx-lowerx) + lowerx))
			f2 = self.funnc((x2*(upperx-lowerx) + lowerx))
			
			# f1 = (x1*(upperx-lowerx) + lowerx)**2 + 54/(x1*(upperx-lowerx) + lowerx)
			# f2 = (x2*(upperx-lowerx) + lowerx)**2 + 54/(x2*(upperx-lowerx) + lowerx)
			#fxm = (xm*(upperx-lowerx) + lowerx)**2 + 54/(xm*(upperx-lowerx) + lowerx)
			# print("f1" + str(f1))
			# print("f2" + str(f2))
			

			if f1<=f2:
				a = x2
				#xm = x1
				if np.abs(b-a)<=stepsize:
					ans = [a, b]
					# print('here1')
					cont = 0

			else:

				if f1>f2:
					b = x1
					#xm = x2
					if np.abs(b-a)<=stepsize:
						ans = [a, b]
						#print('here2')
						cont = 0
				else:
					a = x1
					b = x2

		# print(ans)
		ansfinal = [(ans[0]*(upperx-lowerx) + lowerx), (ans[1]*(upperx-lowerx) + lowerx)]
		# print(ansfinal)

		self.ui.numberoiterations_edit_5.setText(str(kgs))
		self.ui.finalresult_edit_5.setText("Answer interval = "+ str(ansfinal)+ " \n")

	###############################################################################################################################################################
	#6  NEWTON RAPHSON Tab
	###############################################################################################################################################################

	def StepBut_NewtonRaphson(self):

		i = float(self.ui.iterationnumber_label_6.text())
		stepsize = float(self.ui.stepsize_edit_6.text())
		lowerx = float(self.ui.lowerx_edit_6.text())
		upperx = float(self.ui.upperx_edit_6.text())
		initialguess = float(self.ui.initialguess_edit_5.text())
		global cont
		
		k_nr = float(self.ui.numberoiterations_edit_6.text())
		
		# global k_nr
		# k_nr = 0
		global x1
		global x2
		

		if i==0:
			cont = 1
			a = lowerx
			b = upperx
			x1 = initialguess
			# i = 1
			#L = a-b
			# print('here')

		if i==k_nr:
			QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')

		# L = upperx - lowerx
		#print('here2')

		if cont==1 and i<=k_nr-1:

			# print(x[i])
			# x.append((x[i] - (self.nr_funncdash1(x[i])/self.nr_funncdash2(x[i]))))
			x2 = ((x1 - (self.nr_funncdash1(x1)/self.nr_funncdash2(x1))))

			# print("ok")
			
			# print("w1" + str(x1))
			# print("w2" + str(x2))
			#print("Iteration", i)
			f1 = self.funnc(x1)
			f2 = self.funnc(x2)
			
			
			# f1 = (x1*(upperx-lowerx) + lowerx)**2 + 54/(x1*(upperx-lowerx) + lowerx)
			# f2 = (x2*(upperx-lowerx) + lowerx)**2 + 54/(x2*(upperx-lowerx) + lowerx)

			#fxm = (xm*(upperx-lowerx) + lowerx)**2 + 54/(xm*(upperx-lowerx) + lowerx)
			# print("f1" + str(f1))
			# print("f2" + str(f2))
			
			#print("Iteration", i)
			self.ClearBut_NewtonRaphson()
			t = np.arange(lowerx, upperx, stepsize)
			s = self.funnc(t)
			# s = t**2 + 54/t
			self.canvas6.axes.grid(True,linestyle='--')
			self.canvas6.axes.plot(t, s)
			self.canvas6.axes.axvline(x1, 0, 1, label='x1', color='r', linestyle='--')
			#self.canvas5.axes.axvline(xm, 0, 1, label='x2', color='g', linestyle='--')
			self.canvas6.axes.axvline(x2, 0, 1, label='x2', color='g', linestyle='--')
			self.canvas6.draw_idle()
			
			i = i+1
						
			self.ui.disp_edit_6.clear()
			self.ui.iterationnumber_label_6.setText(str(i))
			self.ui.stepslider_6.setValue(i)
			str1 = "Iteration " + str(i) +  " \n"
			#print(str1)

			self.ui.disp_edit_6.append(str1)

			
			str2 = "x1 =" + str(x1) + " \n"
			self.ui.disp_edit_6.append(str2)
			self.ui.disp_edit_6.append("x2 =" + str(x2) + " \n")
			#self.ui.disp_edit_5.append("xm ="+ str(xm)+ " \n")
			self.ui.disp_edit_6.append("f(x1) ="+ str(f1)+ " \n")
			self.ui.disp_edit_6.append("f(x2) ="+ str(f2)+ " \n")
			# self.ui.disp_edit_6.append("x1 ="+ str((x1*(upperx-lowerx) + lowerx))+ " \n")
			# self.ui.disp_edit_6.append("x2 ="+ str((x2*(upperx-lowerx) + lowerx))+ " \n")
			#self.ui.disp_edit_5.append("f(xm) ="+ str(fxm)+ " \n")

			if abs(self.nr_funncdash1(x2))<stepsize:
				ans = x2
				cont = 0

			else:
				x1 = x2		

	def SubmitInput_NewtonRaphson(self):


		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_6.text())
		upperx = float(self.ui.upperx_edit_6.text())
		stepsize = float(self.ui.stepsize_edit_6.text())

		if lowerx!=0 and stepsize != 0 and stepsize>=0 and stepsize<(upperx-lowerx) and upperx>lowerx:

			#print("2")
			self.ShowPlot_NewtonRaphson()

			QtWidgets.QMessageBox.information(self, 'Success', 'Function has been plotted. Next: Newton Raphson Method. Click on Enable Slider button')
			
			#self.settingslider()
			

		else:
			QtWidgets.QMessageBox.critical(self, 'Fail', 'Invaliid input')

	def ShowPlot_NewtonRaphson(self):

		self.ui.iterationnumber_label_6.setText(str(0))
		self.ui.stepslider_6.setValue(0)
		self.ui.disp_edit_6.clear()
		self.ui.finalresult_edit_6.clear()
		#self.ui.iterationnumber_label.clear()
		#kgs = 0 

		self.FinalBut_NewtonRaphson()

		self.canvas6.axes.clear()
		self.canvas6.draw_idle()
	
		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_6.text())
		upperx = float(self.ui.upperx_edit_6.text())
		stepsize = float(self.ui.stepsize_edit_6.text())

		t = np.arange(lowerx, upperx, stepsize)
		s = self.funnc(t)
		# s = t**2 + 54/t
		#s = np.sin(t)
		# self.canvas.axes.clear()
		# self.canvas.draw()
		
		
		self.canvas6.axes.grid(True,linestyle='--')
		# self.canvas.axes.set_xlabel('X axis')
		# self.canvas.axes.set_ylabel('Y axis')
		# self.canvas.axes.set_title('Plot')
		self.canvas6.axes.plot(t, s)
		self.canvas6.axes.axvline(lowerx, 0, 1, label='x1', color='r', linestyle='--')
		self.canvas6.axes.axvline(upperx, 0, 1, label='x3', color='r', linestyle='--')
		self.canvas6.draw_idle()
		
	def SettingSlider_NewtonRaphson(self):

		iterationtot = float(self.ui.numberoiterations_edit_6.text())
		#print(iterationtot)
		lower = float(1)
		self.ui.stepslider_6.setMinimum(lower)
		#print("a")
		self.ui.stepslider_6.setMaximum(iterationtot)
		#print("b")
		self.ui.stepslider_6.setTickInterval(1)
		#print("c")
		self.ui.stepslider_6.setTickPosition(QSlider.TicksBelow)
		# print("d")
		self.ui.numberoiterations_edit_6.setText(str(iterationtot))
		#print("slider set")
		QtWidgets.QMessageBox.information(self, 'Success', 'Slider has been set (only for display purposes). Click on Next Steps button')

	def ClearBut_NewtonRaphson(self):

		self.canvas6.axes.clear()
		self.canvas6.draw_idle()
		#self.ui.horizontalLayout_2.clear()
		#print("c")

	def FinalBut_NewtonRaphson(self):

		lowerx = float(self.ui.lowerx_edit_6.text())
		upperx = float(self.ui.upperx_edit_6.text())
		stepsize = float(self.ui.stepsize_edit_6.text())
		initialguess = float(self.ui.initialguess_edit_5.text())
		a = lowerx
		b = upperx

		# fdash1 = nr_funncdash1(intialguess)
		cont = 1
		global k_nr
		k_nr = 0
		x = [initialguess]
		
		while cont==1:
			# print("2")
			# print("Iteration " + str(k_nr))
			# print(x[k_nr])
			# print(self.nr_funncdash1(x[k_nr]))
			x.append((x[k_nr] - (self.nr_funncdash1(x[k_nr])/self.nr_funncdash2(x[k_nr]))))

			if abs(self.nr_funncdash1(x[k_nr+1]))<stepsize:
				ans = x[k_nr+1]
				cont = 0

			else:
				k_nr = k_nr+1

		self.ui.numberoiterations_edit_6.setText(str(k_nr))
		self.ui.finalresult_edit_6.setText("Answer = "+ str(ans)+ " \n")


	def nr_funncdash1(self, x):
		return (self.funnc(x+self.nr_deltax(x)) - self.funnc(x - self.nr_deltax(x)))/(2*self.nr_deltax(x))

	def nr_funncdash2(self, x):
		return (self.funnc(x+self.nr_deltax(x)) - 2*self.funnc(x) + self.funnc(x - self.nr_deltax(x)))/((self.nr_deltax(x))**2)

	def nr_deltax(self, x):
		if abs(x)>0.01:
			return 0.01*abs(x)
		else:
			return 0.0001


	###############################################################################################################################################################
	#7  BISECTION Tab
	###############################################################################################################################################################

	def StepBut_Bisection(self):

		i = float(self.ui.iterationnumber_label_7.text())
		stepsize = float(self.ui.stepsize_edit_7.text())
		lowerx = float(self.ui.lowerx_edit_7.text())
		upperx = float(self.ui.upperx_edit_7.text())
		a = float(self.ui.initialguess_edit_6.text())
		b = float(self.ui.b_lineedit.text())
		global cont
		global x1
		global x2
		global z
		
		k_bm = float(self.ui.numberoiterations_edit_7.text())

		if i==0:
			cont = 1
			x1 = a
			x2 = b

		if i==k_bm:
			QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')

		#print('here2')

		if cont==1 and i<=k_bm-1:

			z = (x1+x2)/2
			
			f1 = self.funnc(x1)
			f2 = self.funnc(x2)
			f3 = self.funnc(z)
			
			
			# f1 = (x1*(upperx-lowerx) + lowerx)**2 + 54/(x1*(upperx-lowerx) + lowerx)
			# f2 = (x2*(upperx-lowerx) + lowerx)**2 + 54/(x2*(upperx-lowerx) + lowerx)

			#fxm = (xm*(upperx-lowerx) + lowerx)**2 + 54/(xm*(upperx-lowerx) + lowerx)
			# print("f1" + str(f1))
			# print("f2" + str(f2))
			
			#print("Iteration", i)
			self.ClearBut_Bisection()
			t = np.arange(lowerx, upperx, stepsize)
			s = self.funnc(t)
			# s = t**2 + 54/t
			self.canvas7.axes.grid(True,linestyle='--')
			self.canvas7.axes.plot(t, s)
			self.canvas7.axes.axvline(x1, 0, 1, label='x1', color='r', linestyle='--')
			self.canvas7.axes.axvline(z, 0, 1, label='z', color='g', linestyle='--')
			self.canvas7.axes.axvline(x2, 0, 1, label='x2', color='r', linestyle='--')
			self.canvas7.draw_idle()

			i = i+1

			self.ui.disp_edit_7.clear()
			self.ui.iterationnumber_label_7.setText(str(i))
			self.ui.stepslider_7.setValue(i)
			str1 = "Iteration " + str(i) +  " \n"
			#print(str1)

			self.ui.disp_edit_7.append(str1)

			
			str2 = "x1 =" + str(x1) + " \n"
			self.ui.disp_edit_7.append(str2)
			self.ui.disp_edit_7.append("x2 =" + str(x2) + " \n")
			self.ui.disp_edit_7.append("z ="+ str(z)+ " \n")
			self.ui.disp_edit_7.append("f(x1) ="+ str(f1)+ " \n")
			self.ui.disp_edit_7.append("f(z) ="+ str(f3)+ " \n")
			self.ui.disp_edit_7.append("f(x2) ="+ str(f2)+ " \n")
			
			#self.ui.disp_edit_5.append("f(xm) ="+ str(fxm)+ " \n")

			if abs(self.bm_funncdash1(z))<stepsize:
				ans = [x1,x2]
				cont = 0

			else:
				if self.bm_funncdash1(z)<0:
					x1  = z
				else:
					x2 = z	

	def SubmitInput_Bisection(self):

		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_7.text())
		upperx = float(self.ui.upperx_edit_7.text())
		stepsize = float(self.ui.stepsize_edit_7.text())
		a = float(self.ui.initialguess_edit_6.text())
		b = float(self.ui.b_lineedit.text())


		if lowerx!=0 and stepsize != 0 and stepsize>=0 and stepsize<(upperx-lowerx) and upperx>lowerx:

			#print("2")
			if (self.bm_funncdash1(a)*self.bm_funncdash1(b)) >0:
				QtWidgets.QMessageBox.critical(self, 'Fail', 'Invaliid input. Ensure that fdash(a)*fdash(b)<0')
			else:
				self.ShowPlot_Bisection()
				QtWidgets.QMessageBox.information(self, 'Success', 'Function has been plotted. Next: Bisection Method. Click on Enable Slider button')
			
			#self.settingslider()
			

		else:
			QtWidgets.QMessageBox.critical(self, 'Fail', 'Invaliid input')

	def ShowPlot_Bisection(self):

		self.ui.iterationnumber_label_7.setText(str(0))
		self.ui.stepslider_7.setValue(0)
		self.ui.disp_edit_7.clear()
		self.ui.finalresult_edit_7.clear()
		#self.ui.iterationnumber_label.clear()
		#kgs = 0 

		self.FinalBut_Bisection()

		self.canvas7.axes.clear()
		self.canvas7.draw_idle()
	
		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_7.text())
		upperx = float(self.ui.upperx_edit_7.text())
		stepsize = float(self.ui.stepsize_edit_7.text())

		t = np.arange(lowerx, upperx, stepsize)
		s = self.funnc(t)
		# s = t**2 + 54/t
		#s = np.sin(t)
		# self.canvas.axes.clear()
		# self.canvas.draw()
		
		
		self.canvas7.axes.grid(True,linestyle='--')
		# self.canvas.axes.set_xlabel('X axis')
		# self.canvas.axes.set_ylabel('Y axis')
		# self.canvas.axes.set_title('Plot')
		self.canvas7.axes.plot(t, s)
		self.canvas7.axes.axvline(lowerx, 0, 1, label='x1', color='r', linestyle='--')
		self.canvas7.axes.axvline(upperx, 0, 1, label='x3', color='r', linestyle='--')
		self.canvas7.draw_idle()
		
	def SettingSlider_Bisection(self):

		iterationtot = float(self.ui.numberoiterations_edit_7.text())
		#print(iterationtot)
		lower = float(1)
		self.ui.stepslider_7.setMinimum(lower)
		#print("a")
		self.ui.stepslider_7.setMaximum(iterationtot)
		#print("b")
		self.ui.stepslider_7.setTickInterval(1)
		#print("c")
		self.ui.stepslider_7.setTickPosition(QSlider.TicksBelow)
		# print("d")
		self.ui.numberoiterations_edit_7.setText(str(iterationtot))
		#print("slider set")
		QtWidgets.QMessageBox.information(self, 'Success', 'Slider has been set (only for display purposes). Click on Next Steps button')

	def ClearBut_Bisection(self):

		self.canvas7.axes.clear()
		self.canvas7.draw_idle()
		#self.ui.horizontalLayout_2.clear()
		#print("c")

	def FinalBut_Bisection(self):

		lowerx = float(self.ui.lowerx_edit_7.text())
		upperx = float(self.ui.upperx_edit_7.text())
		stepsize = float(self.ui.stepsize_edit_7.text())
		a = float(self.ui.initialguess_edit_6.text())
		b = float(self.ui.b_lineedit.text())

		cont = 1
		global k_bm
		k_bm = 0
		x1 = a
		x2 = b

		while cont==1:

			# print("Iteration " + str(k_bm))
			
			z = (x1+x2)/2
			# print(z)

			if abs(self.bm_funncdash1(z))<stepsize:
				ans = [x1,x2]
				cont = 0

			else:
				if self.bm_funncdash1(z)<0:
					x1  = z
				else:
					x2 = z

				k_bm = k_bm+1
			

		self.ui.numberoiterations_edit_7.setText(str(k_bm))
		self.ui.finalresult_edit_7.setText("Answer interval = "+ str(ans)+ " \n")

	def bm_funncdash1(self, x):
		return (self.funnc(x+self.bm_deltax(x)) - self.funnc(x - self.bm_deltax(x)))/(2*self.bm_deltax(x))

	def bm_funncdash2(self, x):
		return (self.funnc(x+self.bm_deltax(x)) - 2*self.funnc(x) + self.funnc(x - self.bm_deltax(x)))/((self.bm_deltax(x))**2)

	def bm_deltax(self, x):
		if abs(x)>0.01:
			return 0.01*abs(x)
		else:
			return 0.0001

	###############################################################################################################################################################
	#8  SECANT Tab
	###############################################################################################################################################################

	def StepBut_Secant(self):

		i = float(self.ui.iterationnumber_label_8.text())
		lowerx = float(self.ui.lowerx_edit_8.text())
		upperx = float(self.ui.upperx_edit_8.text())
		stepsize = float(self.ui.stepsize_edit_8.text())
		a = float(self.ui.initialguess_edit_7.text())
		b = float(self.ui.secant_b_lineEdit.text())

		global cont
		global x1
		global x2
		global z
		
		k_sec = float(self.ui.numberoiterations_edit_8.text())


		if i==0:
			cont = 1
			x1 = a
			x2 = b

		if i==k_sec:
			QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')

		#print('here2')

		if cont==1 and i<=k_sec-1:

			z = x2 - ((self.sec_funncdash1(x2))/((self.sec_funncdash1(x2)-self.sec_funncdash1(x1))/(x2-x1)))
			
			f1 = self.funnc(x1)
			f2 = self.funnc(x2)
			f3 = self.funnc(z)
			
			#print("Iteration", i)
			self.ClearBut_Secant()
			t = np.arange(lowerx, upperx, stepsize)
			s = self.funnc(t)
			# s = t**2 + 54/t
			self.canvas8.axes.grid(True,linestyle='--')
			self.canvas8.axes.plot(t, s)
			self.canvas8.axes.axvline(x1, 0, 1, label='x1', color='r', linestyle='--')
			self.canvas8.axes.axvline(z, 0, 1, label='z', color='g', linestyle='--')
			self.canvas8.axes.axvline(x2, 0, 1, label='x2', color='r', linestyle='--')
			self.canvas8.draw_idle()

			i = i+1

			self.ui.disp_edit_8.clear()
			self.ui.iterationnumber_label_8.setText(str(i))
			self.ui.stepslider_8.setValue(i)
			str1 = "Iteration " + str(i) +  " \n"
			#print(str1)

			self.ui.disp_edit_8.append(str1)

			
			str2 = "x1 =" + str(x1) + " \n"
			self.ui.disp_edit_8.append(str2)
			self.ui.disp_edit_8.append("x2 =" + str(x2) + " \n")
			self.ui.disp_edit_8.append("z ="+ str(z)+ " \n")
			self.ui.disp_edit_8.append("f(x1) ="+ str(f1)+ " \n")
			self.ui.disp_edit_8.append("f(z) ="+ str(f3)+ " \n")
			self.ui.disp_edit_8.append("f(x2) ="+ str(f2)+ " \n")
			
			#self.ui.disp_edit_5.append("f(xm) ="+ str(fxm)+ " \n")

			if abs(self.sec_funncdash1(z))<stepsize:
				ans = [x1,x2]
				cont = 0

			else:
				if self.sec_funncdash1(z)<0:
					x1  = z
				else:
					x2 = z	

	def SubmitInput_Secant(self):

		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_8.text())
		upperx = float(self.ui.upperx_edit_8.text())
		stepsize = float(self.ui.stepsize_edit_8.text())
		a = float(self.ui.initialguess_edit_7.text())
		b = float(self.ui.secant_b_lineEdit.text())

		if lowerx!=0 and stepsize != 0 and stepsize>=0 and stepsize<(upperx-lowerx) and upperx>lowerx:

			# print("2")
			if (self.bm_funncdash1(a)*self.bm_funncdash1(b)) >0:
				QtWidgets.QMessageBox.critical(self, 'Fail', 'Invaliid input. Ensure that fdash(a)*fdash(b)<0')
			else:
				self.ShowPlot_Secant()
				QtWidgets.QMessageBox.information(self, 'Success', 'Function has been plotted. Next: Secant Method. Click on Enable Slider button')
			
			#self.settingslider()
			

		else:
			QtWidgets.QMessageBox.critical(self, 'Fail', 'Invaliid input')

	def ShowPlot_Secant(self):

		self.ui.iterationnumber_label_8.setText(str(0))
		self.ui.stepslider_8.setValue(0)
		self.ui.disp_edit_8.clear()
		self.ui.finalresult_edit_8.clear()
		#self.ui.iterationnumber_label.clear()
		#kgs = 0 

		self.FinalBut_Secant()

		self.canvas8.axes.clear()
		self.canvas8.draw_idle()
	
		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_8.text())
		upperx = float(self.ui.upperx_edit_8.text())
		stepsize = float(self.ui.stepsize_edit_8.text())

		t = np.arange(lowerx, upperx, stepsize)
		s = self.funnc(t)
		# s = t**2 + 54/t
		#s = np.sin(t)
		# self.canvas.axes.clear()
		# self.canvas.draw()
		
		
		self.canvas8.axes.grid(True,linestyle='--')
		# self.canvas.axes.set_xlabel('X axis')
		# self.canvas.axes.set_ylabel('Y axis')
		# self.canvas.axes.set_title('Plot')
		self.canvas8.axes.plot(t, s)
		self.canvas8.axes.axvline(lowerx, 0, 1, label='x1', color='r', linestyle='--')
		self.canvas8.axes.axvline(upperx, 0, 1, label='x3', color='r', linestyle='--')
		self.canvas8.draw_idle()
		
	def SettingSlider_Secant(self):

		iterationtot = float(self.ui.numberoiterations_edit_8.text())
		#print(iterationtot)
		lower = float(1)
		self.ui.stepslider_8.setMinimum(lower)
		#print("a")
		self.ui.stepslider_8.setMaximum(iterationtot)
		#print("b")
		self.ui.stepslider_8.setTickInterval(1)
		#print("c")
		self.ui.stepslider_8.setTickPosition(QSlider.TicksBelow)
		# print("d")
		self.ui.numberoiterations_edit_8.setText(str(iterationtot))
		#print("slider set")
		QtWidgets.QMessageBox.information(self, 'Success', 'Slider has been set (only for display purposes). Click on Next Steps button')

	def ClearBut_Secant(self):

		self.canvas8.axes.clear()
		self.canvas8.draw_idle()
		#self.ui.horizontalLayout_2.clear()
		#print("c")

	def FinalBut_Secant(self):

		lowerx = float(self.ui.lowerx_edit_8.text())
		upperx = float(self.ui.upperx_edit_8.text())
		stepsize = float(self.ui.stepsize_edit_8.text())
		a = float(self.ui.initialguess_edit_7.text())
		b = float(self.ui.secant_b_lineEdit.text())

		cont = 1
		global k_sec
		k_sec = 0
		x1 = a
		x2 = b

		while cont==1:

			# print("Iteration " + str(k_bm))
			
			z = x2 - ((self.sec_funncdash1(x2))/((self.sec_funncdash1(x2)-self.sec_funncdash1(x1))/(x2-x1)))
			# print(z)

			if abs(self.sec_funncdash1(z))<stepsize:
				ans = [x1,x2]
				cont = 0

			else:
				if self.sec_funncdash1(z)<0:
					x1  = z
				else:
					x2 = z

				k_sec = k_sec+1
			

		self.ui.numberoiterations_edit_8.setText(str(k_sec))
		self.ui.finalresult_edit_8.setText("Answer interval = "+ str(ans)+ " \n")

	def sec_funncdash1(self, x):
		return (self.funnc(x+self.sec_deltax(x)) - self.funnc(x - self.sec_deltax(x)))/(2*self.sec_deltax(x))

	def sec_funncdash2(self, x):
		return (self.funnc(x+self.sec_deltax(x)) - 2*self.funnc(x) + self.funnc(x - self.sec_deltax(x)))/((self.sec_deltax(x))**2)

	def sec_deltax(self, x):
		if abs(x)>0.01:
			return 0.01*abs(x)
		else:
			return 0.0001


	###############################################################################################################################################################
	#9  CUBIC SEARCH Tab
	###############################################################################################################################################################

	def StepBut_CubicSearch(self):

		i = float(self.ui.iterationnumber_label_9.text())
		lowerx = float(self.ui.lowerx_edit_9.text())
		upperx = float(self.ui.upperx_edit_9.text())
		stepsize = float(self.ui.stepsize_edit_9.text())
		initialguess = float(self.ui.initialguess_edit_8.text())
		param1 = float(self.ui.cs_epsilon1_edit.text())
		param2 = float(self.ui.cs_epsilon2_edit.text())
		global cont
		global cont2
		global x1
		global x2
		global xbar
		
		k_cs = float(self.ui.numberoiterations_edit_9.text())
		# self.ui.numberoiterations_edit_9.setText(str(k_cs+1))
		delta = stepsize

		if (self.cs_funncdash1(initialguess))>0:
			# print('a')
			delta = -1*delta

		x = [initialguess]

		if i==0:
			cont = 1
			cont2 = 1
			x1= initialguess

		if i==k_cs:
			QtWidgets.QMessageBox.information(self, 'Success', 'All iterations complete')


		if cont==1 and cont2==1 and i<=k_cs-1:
			
			x2 = (x1) + (2**i)*delta
			f1 = self.funnc(x1)
			f2 = self.funnc(x2)
			
			
			self.ClearBut_CubicSearch()
			t = np.arange(lowerx, upperx, stepsize)
			s = self.funnc(t)
			# s = t**2 + 54/t
			self.canvas9.axes.grid(True,linestyle='--')
			self.canvas9.axes.plot(t, s)
			self.canvas9.axes.axvline(x1, 0, 1, label='x1', color='r', linestyle='--')
			#self.canvas5.axes.axvline(xm, 0, 1, label='x2', color='g', linestyle='--')
			self.canvas9.axes.axvline(x2, 0, 1, label='x2', color='g', linestyle='--')
			self.canvas9.draw_idle()

			i = i+1

			self.ui.disp_edit_9.clear()
			self.ui.iterationnumber_label_9.setText(str(i))
			self.ui.stepslider_9.setValue(i)
			str1 = "Iteration " + str(i) +  " \n"
			self.ui.disp_edit_9.append(str1)
			str2 = "x1 =" + str(x1) + " \n"
			self.ui.disp_edit_9.append(str2)
			self.ui.disp_edit_9.append("x2 =" + str(x2) + " \n")
			# self.ui.disp_edit_9.append("xbar ="+ str(xbar)+ " \n")
			self.ui.disp_edit_9.append("f(x1) ="+ str(f1)+ " \n")
			self.ui.disp_edit_9.append("f(x2) ="+ str(f2)+ " \n")
			
			if (self.cs_funncdash1(x2))*(self.cs_funncdash1(x1))<=0:
				# print('yes')
				# x1 = x[k_cs]
				# x2 = x[k_cs+1]
				# print(x2)

				if cont2 == 1:

				#step 4
					xbar = self.cs_xbar(x1,x2)           
					# print(xbar)

				# step 5
					if self.funnc(xbar)<=self.funnc(x1):

				  # step 6
						if (abs(self.cs_funncdash1(xbar))<=param1) and (abs((xbar-x1)/xbar)<=param2):
							ans = [x1, x2]
							cont = 0
							cont2 = 0
						else:
							if self.cs_funncdash1(xbar)*self.cs_funncdash1(x1)<0:
								x2 = xbar
							else:
								x1 = xbar
					else:

						#while funnc(xbar)>funnc(x1):
						xbar = xbar - 0.5*(xbar - x1)
			 
				# step 6
						if (abs(self.cs_funncdash1(xbar))<=param1) and (abs((xbar-x1)/xbar)<=param2):
							ans = [x1, x2]
							cont = 0
							cont2 = 0
						else:
							if self.cs_funncdash1(xbar)*self.cs_funncdash1(x1)<0:
								x2 = xbar
							else:
								x1 = xbar

				#print(x1)
				#print(x2)

			else:
				i = i + 1

	def SubmitInput_CubicSearch(self):

		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_9.text())
		upperx = float(self.ui.upperx_edit_9.text())
		stepsize = float(self.ui.stepsize_edit_9.text())

		if lowerx!=0 and stepsize != 0 and stepsize>=0 and stepsize<(upperx-lowerx) and upperx>lowerx:

			#print("2")
			self.ShowPlot_CubicSearch()

			QtWidgets.QMessageBox.information(self, 'Success', 'Function has been plotted. Next: Cubic Search Method. Click on Enable Slider button')
			
			#self.settingslider()
			

		else:
			QtWidgets.QMessageBox.critical(self, 'Fail', 'Invaliid input')

	def ShowPlot_CubicSearch(self):

		self.ui.iterationnumber_label_9.setText(str(0))
		self.ui.stepslider_9.setValue(0)
		self.ui.disp_edit_9.clear()
		self.ui.finalresult_edit_9.clear()
		#self.ui.iterationnumber_label.clear()
		#kgs = 0 

		self.FinalBut_CubicSearch()

		self.canvas9.axes.clear()
		self.canvas9.draw_idle()
	
		#power = float(self.ui.polynomial_edit.text())
		lowerx = float(self.ui.lowerx_edit_9.text())
		upperx = float(self.ui.upperx_edit_9.text())
		stepsize = float(self.ui.stepsize_edit_9.text())

		t = np.arange(lowerx, upperx, stepsize)
		s = self.funnc(t)
		# s = t**2 + 54/t
		#s = np.sin(t)
		# self.canvas.axes.clear()
		# self.canvas.draw()
		
		
		self.canvas9.axes.grid(True,linestyle='--')
		# self.canvas.axes.set_xlabel('X axis')
		# self.canvas.axes.set_ylabel('Y axis')
		# self.canvas.axes.set_title('Plot')
		self.canvas9.axes.plot(t, s)
		self.canvas9.axes.axvline(lowerx, 0, 1, label='x1', color='r', linestyle='--')
		self.canvas9.axes.axvline(upperx, 0, 1, label='x3', color='r', linestyle='--')
		self.canvas9.draw_idle()
		
	def SettingSlider_CubicSearch(self):

		iterationtot = float(self.ui.numberoiterations_edit_9.text())
		#print(iterationtot)
		lower = float(1)
		self.ui.stepslider_9.setMinimum(lower)
		#print("a")
		self.ui.stepslider_9.setMaximum(iterationtot)
		#print("b")
		self.ui.stepslider_9.setTickInterval(1)
		#print("c")
		self.ui.stepslider_9.setTickPosition(QSlider.TicksBelow)
		# print("d")
		self.ui.numberoiterations_edit_9.setText(str(iterationtot))
		#print("slider set")
		QtWidgets.QMessageBox.information(self, 'Success', 'Slider has been set (only for display purposes). Click on Next Steps button')

	def ClearBut_CubicSearch(self):

		self.canvas9.axes.clear()
		self.canvas9.draw_idle()
		#self.ui.horizontalLayout_2.clear()
		#print("c")

	def FinalBut_CubicSearch(self):

		# print('here')

		lowerx = float(self.ui.lowerx_edit_9.text())
		upperx = float(self.ui.upperx_edit_9.text())
		stepsize = float(self.ui.stepsize_edit_9.text())
		initialguess = float(self.ui.initialguess_edit_8.text())
		param1 = float(self.ui.cs_epsilon1_edit.text())
		param2 = float(self.ui.cs_epsilon2_edit.text())

		cont = 1
		cont2 = 1
		global k_cs
		k_cs = 0

		delta = stepsize

		if (self.cs_funncdash1(initialguess))>0:
			# print('a')
			delta = -1*delta

		x = [initialguess]
		# print('a')

		while cont==1 and cont2==1:

			# print(k_cs)
			# print(x)

		  #step2
			x.append((x[k_cs]) + (2**k_cs)*delta)

			if (self.cs_funncdash1(x[k_cs + 1]))*(self.cs_funncdash1(x[k_cs]))<=0:
				# print('yes')
				x1 = x[k_cs]
				x2 = x[k_cs+1]
				# print(x2)

				while cont2 == 1:

				#step 4
					xbar = self.cs_xbar(x1,x2)           
					# print(xbar)

				# step 5
					if self.funnc(xbar)<=self.funnc(x1):

				  # step 6
						if (abs(self.cs_funncdash1(xbar))<=param1) and (abs((xbar-x1)/xbar)<=param2):
							ans = [x1, x2]
							cont = 0
							cont2 = 0
						else:
							if self.cs_funncdash1(xbar)*self.cs_funncdash1(x1)<0:
								x2 = xbar
							else:
								x1 = xbar
					else:

						#while funnc(xbar)>funnc(x1):
						xbar = xbar - 0.5*(xbar - x1)
			 
				# step 6
						if (abs(self.cs_funncdash1(xbar))<=param1) and (abs((xbar-x1)/xbar)<=param2):
							ans = [x1, x2]
							cont = 0
							cont2 = 0
						else:
							if self.cs_funncdash1(xbar)*self.cs_funncdash1(x1)<0:
								x2 = xbar
							else:
								x1 = xbar

				#print(x1)
				#print(x2)

			else:
				k_cs = k_cs + 1


		self.ui.numberoiterations_edit_9.setText(str(k_cs+1))
		self.ui.finalresult_edit_9.setText("Answer interval = "+ str(ans)+ " \n")

	def cs_funncdash1(self, x):
		return (self.funnc(x+self.cs_deltax(x)) - self.funnc(x - self.cs_deltax(x)))/(2*self.cs_deltax(x))

	def cs_funncdash2(self, x):
		return (self.funnc(x+self.cs_deltax(x)) - 2*self.funnc(x) + self.funnc(x - self.cs_deltax(x)))/((self.cs_deltax(x))**2)

	def cs_deltax(self, x):
		if abs(x)>0.01:
			return 0.01*abs(x)
		else:
			return 0.0001

	def cs_xbar(self, x1, x2):
		z = ((3*(self.funnc(x1)-self.funnc(x2)))/(x2-x1)) + self.cs_funncdash1(x1) + self.cs_funncdash1(x2)
		w = ((x2-x1)/(abs(x2-x1)))*np.sqrt(z**2 - (self.cs_funncdash1(x1)*self.cs_funncdash1(x2)))
		mu = (self.cs_funncdash1(x2) + w -z)/(self.cs_funncdash1(x2)-self.cs_funncdash1(x1) + 2*w)

		if mu == 0:
			xbar = x2
		else:
			if mu>1:
				xbar = x1
			else:
				xbar =  x2 - mu*(x2-x1)

		return xbar


if __name__ == '__main__':
	app = QtWidgets.QApplication([])

	widget = plotwindow()
	widget.show()

	app.exec_()