# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren/videos
# Calculadora Basica
from kivy.app import App
from kivy.lang import Builder

class Calculadora(App):
    def build(self):
        return Builder.load_string(KV)
    def operacion(self, data):
        try:
            self.root.pantalla.text = str(eval(data))
        except SyntaxError:
            self.root.pantalla.text = '' #ERROR
        except ZeroDivisionError:
            self.root.pantalla.text = '' #NO SE PUEDE DIVIDIR ENTRE CERO
        except  TypeError:
            self.root.pantalla.text = '' # (2)(2)  x 

    def borrar_uno(self,i):
        n = str(self.root.pantalla.text)[:-1]
        self.root.pantalla.text = n

KV = '''
<FormaButton@Button>:
    font_size: self.width/3
    color: '#FFFFFF'
GridLayout
    pantalla: entry
    rows: 6
    padding: 5
    spacing: 5
    BoxLayout:
        TextInput:
            id: entry
            halign: 'right'
            font_size: 35
           # multiline: False
    BoxLayout:
        spacing: 5
        FormaButton:
            text: "7"
            on_press: entry.text += self.text
        FormaButton:
            text: "8"
            on_press: entry.text += self.text
        FormaButton:
            text: "9"
            on_press: entry.text += self.text
        FormaButton:
            text: "AC"
            on_press: app.borrar_uno(entry.text)
            background_color: '#DD0044'
    BoxLayout:
        spacing: 5
        FormaButton:
            text: "4"
            on_press: entry.text += self.text
        FormaButton:
            text: "5"
            on_press: entry.text += self.text
        FormaButton:
            text: "6"
            on_press: entry.text += self.text
        FormaButton:
            text: "+"
            on_press: entry.text += self.text
            background_color: '#00D4FF'
    BoxLayout:
        spacing: 5
        FormaButton:
            text: "1"
            on_press: entry.text += self.text
        FormaButton:
            text: "2"
            on_press: entry.text += self.text
        FormaButton:
            text: "3"
            on_press: entry.text += self.text
        FormaButton:
            text: "-"
            on_press: entry.text += self.text
            background_color: '#00D4FF'
    BoxLayout:
        spacing: 5
        FormaButton:
            text: "."
            on_press: entry.text += self.text         
        FormaButton:
            text: "0"
            on_press: entry.text += self.text
        FormaButton:
            text: "C"
            on_press: entry.text = ""
            background_color: (1,0,0,1) 
        FormaButton:
            text: "*"
            on_press: entry.text += self.text
            background_color: '#00D4FF'
    BoxLayout:
        spacing: 5
        FormaButton:
            text: "("
            on_press: entry.text += self.text
        FormaButton:
            text: ")"
            on_press: entry.text += self.text
        FormaButton:
            text: "="
            on_press: app.operacion(entry.text)
            background_color: '#F503F9'
        FormaButton:
            text: "/"
            on_press: entry.text += self.text
            background_color: '#00D4FF'
'''
if __name__ == "__main__":
    Calculadora().run()
