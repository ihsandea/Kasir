from kivy.app import App
from kivy.uix.label import Label

class KasirApp(App):
    def build(self):
        return Label(text='Kasir Ihsan Berhasil Jalan!')

KasirApp().run()
