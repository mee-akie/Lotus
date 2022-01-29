import time
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.label import Label
from kivymd.uix.behaviors import FocusBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.popup import Popup
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem
from datetime import date


# define um tamanho de tela padrao (obs: nao eh fixo)
Window.size = (400, 650)



KV = '''
#:include HomeScreen.kv
#:include Login.kv
#:include CadastroScreen.kv

#:import get_color_from_hex kivy.utils.get_color_from_hex
#:set toolbarColor get_color_from_hex("#F6C7B7")


ScreenManager:
    LoginPage:
    HomePage:
    CadastroPage:

'''

class LoginPage(Screen):
    
    def validaLogin(self, *args):
        self.parent.current = 'home'

    def switchCadastro(self):
        self.parent.current = 'cadastro'


class CadastroPage(Screen):

    def switchLogin(self):
        self.parent.current = 'login'


class HomePage(Screen):

    def switchHome(self):
        self.parent.current = 'home'



# Gerenciador de paginas
sm = ScreenManager()
sm.add_widget(HomePage(name='home'))
sm.add_widget(LoginPage(name='login'))
sm.add_widget(CadastroPage(name='cadastro'))



class Main(MDApp):
    def build(self):

        #Cor base da aplicacao
        self.theme_cls.primary_palette = "Pink"
        
        return Builder.load_string(KV)


Main().run()
