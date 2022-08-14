
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QFileDialog, QTextEdit, QPlainTextEdit, QTabWidget, QWidget, QSlider
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure



lowerx = 0
upperx = 8
stepsize = 0.5
guessbp = 2
delta = stepsize

# f1 = funnc(guessbp - np.abs(delta))
# f2 = funnc(guessbp)
# f3 = funnc(guessbp + np.abs(delta))
x1 = guessbp - np.abs(delta)
x2 = guessbp
x3 = guessbp + np.abs(delta)

f1 = x1**2 + 54/x1
f2 = x2**2 + 54/x2
f3 = x3**2 + 54/x3

if f1>=f2 and f2>=f3:
	delta = delta
else:
	delta = -delta
	print("heeer")

cont = 1
global k
k = 0
x = []
x.append(guessbp)

while x[k]<= upperx and x[k]>=lowerx and cont==1:

	x.append(x[k] + (2**k)*delta)
	f4 = (x[k+1])**2 + 54/(x[k+1])
	f5 = (x[k])**2 + 54/(x[k])
	# print(f4)
	# print(f5)

	if f4<f5:
		k = k+1
		#print(k)

	else:
		ans = [x[k-1], x[k+1]]
		cont=0
		print(ans)