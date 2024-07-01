import pandas as pd
import matplotlib.pyplot as plt
import os

class Roomies:
    def __init__(self, data_file='./uploads/roomies.csv'):
        self.data_file = data_file
        self.df = pd.read_csv(self.data_file)
        self.translate_values()

    def translate_values(self):
        bool_columns = ['¿Fumas?\r\n(1=si/0=No)', '¿Tienes mascotas? (1=Sí/0=No)', '¿Te gusta cocinar? (1=Sí/2=No)']
        choice_columns = ['¿Eres una persona madrugador/a o noctámbulo/o?\r\n(1=Madrugadora/2=Noctámbula)']

        for column in bool_columns:
            self.df[column] = self.df[column].map({1: 'Sí', 0: 'No', 2: 'No'})

        for column in choice_columns:
            self.df[column] = self.df[column].apply(lambda x: str(x).strip() if pd.notnull(x) else x)
            self.df[column] = self.df[column].map({'1': 'Madrugadora', '2': 'Noctámbula', '1,5': 'Un poco de ambos'})

        self.df['genero'] = self.df['genero'].map({'F': 'Femenino', 'M': 'Masculino'})
        return self.df
    
    def get_data(self):
        return self.df.to_dict(orient='records')
    
    def get_roomie_by_id(self, id):
        roomie = self.df[self.df['id_usuario'] == int(id)].to_dict(orient='records')
        return roomie[0] if roomie else None
    
    def generate_charts(self, roomie):
        user_id = roomie['id_usuario']
        user_chart_dir = f'./static/charts/{user_id}'

        if not os.path.exists(user_chart_dir):
            os.makedirs(user_chart_dir)

        chart_paths = {}
        i = 0
        for key, value in roomie.items():
            if key not in ['id_usuario', 'nombre', 'edad', 'genero', 
                '¿Eres una persona madrugador/a o noctámbulo/o?\n(1=Madrugadora/2=Noctámbula)', 
                'hobbies (Especificar)', '¿Qué tipo de música escuchas?  (Especificar)', 
                '¿Tienes mascotas? (1=Sí/0=No)', '¿Te gusta cocinar? (1=Sí/2=No)', '¿Fumas?\n(1=si/0=No)']:
                i += 1
                chart_path = f'{user_chart_dir}/{i}.png'

                if not os.path.exists(chart_path):
                    plt.figure()
                    plt.bar([key], [value], color='blue')
                    plt.ylim(0, 10)
                    plt.title(key)
                    plt.ylabel('Valor')

                    plt.savefig(chart_path)
                    plt.close()
                
                chart_paths[key] = chart_path
        return chart_paths

plt.switch_backend('Agg')
