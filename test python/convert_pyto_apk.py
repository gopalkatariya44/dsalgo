from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class App(MDApp):
    def build(self):
        return MDLabel(text="Welcome to Wscube Tech", halign="center")


App().run()
