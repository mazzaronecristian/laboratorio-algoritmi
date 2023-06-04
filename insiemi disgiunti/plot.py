import matplotlib.pyplot as plt

class Plot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def add_data(self, x_data, y_data, label=None):
        self.ax.plot(x_data, y_data, label=label)

    def set_title(self, title):
        self.ax.set_title(title)

    def set_xlabel(self, xlabel):
        self.ax.set_xlabel(xlabel)

    def set_ylabel(self, ylabel):
        self.ax.set_ylabel(ylabel)

    def show(self):
        self.ax.legend()
        plt.show()

    def save_and_show(self, destination='images/plot.png'):
        self.ax.legend()
        self.fig.savefig(destination, format="png", dpi=300)
        plt.show()

def plot_results(x, y, labels, title, destination='images/plot.png',
                xlabel = 'Number of nodes',  ylabel = 'Time (s)'):
    plot = Plot()
    plot.set_title(title)
    plot.set_xlabel(xlabel)
    plot.set_ylabel(ylabel)

    #* per ogni riga di y, ho una curva diversa da disegnare sul grafico (se i = 0, ho una sola curva)
    for i in range( len(y) ):
        plot.add_data(x, y[i], labels[i])
    plot.save_and_show(destination)