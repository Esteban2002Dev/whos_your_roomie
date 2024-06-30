import pandas as pd

class Roomies:
    global data

    def get_data():
        data = pd.read_csv('./uploads/roomies.csv')
        return data