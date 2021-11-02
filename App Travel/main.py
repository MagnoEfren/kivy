#@autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren/videos
#API https://travelbriefing.org/api

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest


class TravelApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        
        self.window.size_hint = (0.9,0.9)
        self.window.pos_hint = {'center_x':0.5, 'center_y':0.5}


        self.imagen = Image(source = 'logo.png')

        self.buscar = TextInput(
            size_hint = (1,0.2),
            multiline= False, 
            font_size = '18sp', 
            halign ='center')

        self.boton_buscar = Button(
            size_hint = (0.3,0.2),
            text= 'Buscar', 
            background_color = '#F500FD',
            color = [1,1,1,1],
            pos_hint = {'center_x':0.5, 'center_y':0.5})

        self.informacion = Label(
            text = 'Busca un Pais', 
            color = '#F500FD',
            font_size = '16sp')

        self.window.add_widget(self.imagen)
        self.window.add_widget(self.buscar)
        self.window.add_widget(self.boton_buscar)
        self.window.add_widget(self.informacion)
        self.boton_buscar.bind(on_press = self.informacion_pais)


        return self.window
    

    def informacion_pais(self, instance):
        def edit_label (request, result):
            data = result['names']['full']
            self.informacion.text = f'Dados: { data}'
        link = f'https://travelbriefing.org/{ self.buscar.text }?format=json'
        req = UrlRequest(url = link, on_success= edit_label)
   

    #@staticmethod 


if __name__ == "__main__":
    TravelApp().run()



'''            data = result     
            self.informacion.text = ('Nombre:  ' + data["names"]["full"] + '\n'
                                    + 'Idioma: '+ data["language"][0]["language"] + '\n'
                                    + 'Volate: ' + data["electricity"]["voltage"] + ' V' + '\n' 
                                    + 'Frecuencia: '+ data["electricity"]["frequency"] +' Hz' + '\n'
                                    + 'Numero Policia: ' + data["telephone"]["police"] + '\n' 
                                    + 'Numero Ambulacia: '+ data["telephone"]["ambulance"] + '\n'
                                    + 'Tipo de Moneda : ' + data["currency"]['name'] )'''
