from binary_perceptron import BinaryPerceptron # Your implementation of binary perceptron
from plot_bp import PlotBinaryPerceptron
import csv  # For loading data.
from matplotlib import pyplot as plt  # For creating plots.


class PlotMultiBPOneVsAll(PlotBinaryPerceptron):
    """
    Plots the Binary Perceptron after training it on the Iris dataset
    ---
    Extends the class PlotBinaryPerceptron
    """

    def __init__(self, bp, plot_all=True, n_epochs=50):
        super().__init__(bp, plot_all, n_epochs) # Calls the constructor of the super class
        self.CLASSES = (1,2)
        self.PLOT_ALL = False # only plot the final separator

    def read_data(self):
        """
        Read data from the Iris dataset with 2 features and 2 classes
        for both training and testing.
        ---
        Overrides the method in PlotBinaryPerceptron
        """
        data_as_strings = list(csv.reader(open('synthetic_data.csv'), delimiter=','))
        self.TRAINING_DATA = [[float(f1), float(f2), int(c)]
                              for [f1, f2, c] in data_as_strings]
        i = 0
        while i < len(self.TRAINING_DATA):
            if self.TRAINING_DATA[i][-1] == self.CLASSES[0]:
              self.TRAINING_DATA[i][-1] = 1
              i += 1
            elif self.TRAINING_DATA[i][-1] == self.CLASSES[1]:
              self.TRAINING_DATA[i][-1] = -1
              i += 1
            else:
                del(self.TRAINING_DATA[i])

    def plot(self):
        """
        Plots the dataset as well as the binary classifier
        ---
        Overrides the method in PlotBinaryPreceptron
        """
        plt.title("Plot between classes 1 and 2")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend(loc='best')
        plt.savefig("1_2_plot")
        plt.show()



if __name__=='__main__':
    binary_perceptron = BinaryPerceptron(alpha=0.5)
    pbp = PlotMultiBPOneVsAll(binary_perceptron)
    pbp.train()
    pbp.test()
    pbp.plot()