from binary_perceptron import BinaryPerceptron # Your implementation of binary perceptron
from plot_bp import PlotBinaryPerceptron
import csv  # For loading data.
from matplotlib import pyplot as plt  # For creating plots.
import remapper as rm


class PlotRingBP(PlotBinaryPerceptron):
    """
    Plots the Binary Perceptron after training it on the Ring dataset
    ---
    Extends the class PlotBinaryPerceptron
    """

    def __init__(self, bp, plot_all=True, n_epochs=25):
        super().__init__(bp, plot_all, n_epochs) # Calls the constructor of the super class
        self.IS_REMAPPED=True
        # self.IS_REMAPPED=False

    def read_data(self):
        data_as_rings = list(csv.reader(open('ring-data.csv'), delimiter=','))
        if self.IS_REMAPPED:
            self.TRAINING_DATA = [rm.remap(float(f1), float(f2))+[int(c)] for [f1, f2, c] in data_as_rings]
        else:
            self.TRAINING_DATA = [[float(f1), float(f2), int(c)] for [f1, f2, c] in data_as_rings]

    def plot(self):
        """
        Plots the dataset as well as the binary classifier
        ---
        Overrides the method in PlotBinaryPreceptron
        """
        plt.title("Ring datasset")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend(loc='best')
        plt.savefig("Ring plot")
        plt.show()

if __name__=='__main__':
    binary_perceptron = BinaryPerceptron(alpha=0.5)
    prp = PlotRingBP(binary_perceptron)
    prp.train()
    prp.plot()
