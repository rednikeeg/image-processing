import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.stacklayout import StackLayout

import image
import select_file

class Popups(StackLayout):
    pass


def show_popup():
    show = Popups()

    popupWindow = Popup(title="Popup Window", content=show,
                        size_hint=(None, None), size=(500, 500))


    popupWindow.open()

class MainWindow(Screen):
    pass

class SecondWindow(Screen):

    imgDiff = ObjectProperty(None)
    filebtnname = "'click to open'"

    def pressWhite(self):
        self.bgColor = "White"

    def show_pop(self):
        show_popup()

    def pressBlack(self):
        self.bgColor = "Black"

    def pressRed(self):
        self.bgColor = "Red"

    def pressBlue(self):
        self.bgColor = "Blue"

    def fileBtn(self):
        self.file = select_file.openFile()

    def showOriginalPic(self):
        image.showOriginal(self.file)


    def btn(self):
        newImage = image.DelBackground(self.file, self.bgColor, self.imgDiff.text)
        newImage.run()
        self.imgDiff.text = ""

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv
