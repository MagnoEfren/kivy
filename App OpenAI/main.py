
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.snackbar import Snackbar
import urllib.request
import openai # pip install openai
import os
Window.size = (350,500)

class Ui(ScreenManager):
    pass

class MainApp(MDApp):
    size_image = '512x512'
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        Builder.load_file('style.kv')
        return Ui()

    def generate_image(self):
        prompt = self.root.ids.text_prompt.text
        if len(prompt)>=8:
            try:
                openai.api_key ='API_KEY'
                res = openai.Image.create(
                    prompt = prompt,
                    n = 3,
                    size = self.size_image
                )
                self.image_url1 = res['data'][0]['url']
                self.image_url2 = res['data'][1]['url']
                self.image_url3 = res['data'][2]['url']

                self.root.ids.image_one.source = self.image_url1
                self.root.ids.image_two.source = self.image_url2
                self.root.ids.image_three.source = self.image_url3
            except Exception as e:
                Snackbar(text = 'Error al conectar a internet').open()
        else:
            Snackbar(text = 'Ingrese un texto mas amplio').open()


    def download_image_one(self):
        folder_name = 'imagenes'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        new_filename = 'imagen1.png'
        i = 1
        while os.path.exists(os.path.join(folder_name, new_filename)):
            new_filename = f'imagen({i}).png'
            i+=1
        try:
            urllib.request.urlretrieve(self.image_url1, os.path.join(folder_name, new_filename))
            Snackbar(text = 'Imagen guardada con exito')
        except:
            Snackbar(text = 'No se pudo guardar la imagen')


    def download_image_two(self):
        folder_name = 'imagenes'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        new_filename = 'imagen2.png'
        i = 1
        while os.path.exists(os.path.join(folder_name, new_filename)):
            new_filename = f'imagen2({i}).png'
            i+=1
        try:
            urllib.request.urlretrieve(self.image_url2, os.path.join(folder_name, new_filename))
            Snackbar(text = 'Imagen guardada con exito')
        except:
            Snackbar(text = 'No se pudo guardar la imagen')

    def download_image_three(self):
        folder_name = 'imagenes'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        new_filename = 'imagen3.png'
        i = 1
        while os.path.exists(os.path.join(folder_name, new_filename)):
            new_filename = f'imagen3({i}).png'
            i+=1
        try:
            urllib.request.urlretrieve(self.image_url3, os.path.join(folder_name, new_filename))
            Snackbar(text = 'Imagen guardada con exito')
        except:
            Snackbar(text = 'No se pudo guardar la imagen')

    def checkbox_size(self, x):
        self.size_image = x
if __name__ =="__main__":
    MainApp().run()
