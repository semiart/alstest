from PyQt5 import QtWidgets, QtCore
import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MatplotlibWidget(QtWidgets.QWidget):
    """
    Implements a Matplotlib figure inside a QWidget.
    Use getFigure() and redraw() to interact with matplotlib.

    Example::

        mw = MatplotlibWidget()
        ax = mw.figure.add_subplot(111)
        ax.plot(x,y)
        mw.draw()
    """

    def __init__(self, width=4.0, height=3.0, dpi=100):
        QtWidgets.QWidget.__init__(self)
        self.figure = Figure(figsize=(4.0, 3.0), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self)

    def draw(self):
        self.canvas.draw()


