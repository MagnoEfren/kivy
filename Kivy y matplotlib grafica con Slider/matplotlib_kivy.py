# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
#
# instalar:  kivy_garden  -> pip install kivy_garden
# Instalar:  matplotlib version menor a 3.3.0  -> pip install "matplotlib<3.3.0"
# instalar: garden install matplotlib 
# Youtube: https://www.youtube.com/c/MagnoEfren

from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt
from kivy.garden.matplotlib import FigureCanvasKivyAgg
import numpy as np
from kivy.config import Config
  
Config.set('graphics', 'resizable', True)

class Grafica(App):
    def build(self):
        self.fig, self.ax = plt.subplots(dpi=80, figsize=(7,5), facecolor='#000000b7')
        plt.xlim(-11, 11)
        plt.ylim(-8, 8)
        plt.grid (alpha=0.2)
        plt.title("Kivy y Matplotlib",color='blue',size=28, family="Kaufmann BT")

        self.ax.set_facecolor('#6E6D7000')
        self.ax.axhline(linewidth=2, color='w')
        self.ax.axvline(linewidth=2, color='w')

        self.ax.spines['bottom'].set_color('blue')
        self.ax.spines['left'].set_color('blue')        
        #self.ax.spines['top'].set_color('blue')
        #self.ax.spines['right'].set_color('blue')
        
        self.ax.set_xlabel("Eje  Horizontal", color='white', family = 'Cambria', size=15)
        self.ax.set_ylabel("Eje  Vertical", color='white', family = 'Cambria', size = 15)
        self.ax.tick_params(color = 'blue', labelcolor = 'white', direction='out', length=6, width=2) 

        box = BoxLayout( orientation = 'vertical', spacing=10)
        self.canvas = FigureCanvasKivyAgg(self.fig, size_hint=(1, 0.9))
        box.add_widget(self.canvas)

        self.nivel = Slider(min=0, max = 7, orientation= 'horizontal',value_track = True,
          value_track_color =[0, 1, 0, 1], size_hint=(1, 0.1))
        box.add_widget(self.nivel)
        self.nivel.bind(value = self.valor_slider)

        return box

    def valor_slider(self, instance, value):
        x = np.arange(-4*np.pi, value*np.pi, 0.01)
        line, = self.ax.plot(x, value*np.sin(x), color ='lime', marker='o', linestyle='dotted', 
          markersize=1,linewidth=8)
        self.canvas.draw()        
        line.set_ydata(20)

Grafica().run() 
