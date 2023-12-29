from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Alert_BLL import *


# plot function is created for
# plotting the graph in
# tkinter child_frame
def Protocol_xy(month):
    # list of squares
    protocol_dict = Alert_BLL.count(2, month)
    x = list(protocol_dict.keys())
    y = list(protocol_dict.values())
    return x, y


def Month_xy():
    month_dict = Alert_BLL.count(0)
    x = list(month_dict.keys())
    y = list(month_dict.values())
    return x, y


def plot(child_frame, id, month):
    if id == 2:
        x, y = Protocol_xy(month)
    if id == 3:
        x, y = Month_xy()
    # the figure that will contain the plot
    fig = Figure(figsize=(3, 3), dpi=100)
    # adding the subplot
    plot1 = fig.add_subplot(111)
    # plotting the graph
    if id == 2:
        plot1.bar(x, y)
    elif id == 3:
        plot1.plot(x, y)
    plot1.tick_params(axis="x", which="major", labelsize=8)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=child_frame)
    canvas.draw()

    # placing the canvas on the Tkinter child_frame
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, child_frame)
    toolbar.update()

    # placing the toolbar on the Tkinter child_frame
    canvas.get_tk_widget().pack()
