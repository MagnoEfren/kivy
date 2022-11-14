
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ListProperty

from kivy.core.window import Window
Window.size = (350, 580)

class Ui(BoxLayout):

    gray = ListProperty([212/255, 212/255, 210/255,1])
    gray_black = ListProperty([80/255, 80/255, 80/255,1])
    orange = ListProperty([255/255, 149/255, 0,1])
    black = ListProperty([0, 0, 0,1])
    white = ListProperty([1, 1, 1,1])

class MainApp(App):
    def build(self):
        Builder.load_file('style.kv')
        return Ui()

    def operacion(self, data):
        try:
            self.root.ids.entry.text = str(eval(data))
        except SyntaxError:
            self.root.ids.entry.text = '' #ERROR
        except ZeroDivisionError:
            self.root.ids.entry.text = '' #
        except  TypeError:
            self.root.ids.entry.text = '' # x

    def borrar_uno(self,i):
        n = str(self.root.ids.entry.text)[:-1]
        self.root.ids.entry.text = n

    def mas_menos(self, i ):
        n = str(self.root.ids.entry.text)[:]
        try:
            if n[0]=='-':
                n = n[1:]
                self.root.ids.entry.text = n
            else:
                n = '-' + n
                self.root.ids.entry.text = n
        except IndexError:
             self.root.ids.entry.text = ''

    def porcentaje(self, i):
        try:
            n = int(eval(self.root.ids.entry.text))/(100)
            self.root.ids.entry.text = str(n)
        except ValueError:
            self.root.ids.entry.text = ''
        except  SyntaxError:
            self.root.ids.entry.text = ''


if __name__ == '__main__':
    MainApp().run()
