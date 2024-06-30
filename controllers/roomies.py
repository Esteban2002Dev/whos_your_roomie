import pandas as pd
import matplotlib.pyplot as plt

class Roomies:
    def __init__(self, data_file='./uploads/roomies.csv'):
        self.data_file = data_file
        self.df = pd.read_csv(self.data_file)

    def get_data(self):
        return self.df.to_dict(orient='records')
    
    def generate_data_frame(self, x_column, y_column, kind='line', title='Title', xlabel='X-axis', ylabel='Y-axis'):
        self.df.plot(x=x_column, y=y_column, kind=kind)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
