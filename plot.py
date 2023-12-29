from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Alert_BLL import *


# plot function is created for
# plotting the graph in
# tkinter child_frame
def Protocol_plot(child_frame):
    # the figure that will contain the plot
    fig = Figure(figsize=(3, 3), dpi=100)

    # list of squares
    protocol_dict = Alert_BLL.protocol_count()
    x = list(protocol_dict.keys())
    y = list(protocol_dict.values())

    # adding the subplot
    plot1 = fig.add_subplot(111)
    print(y)
    # plotting the graph
    plot1.bar(x, y)
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
