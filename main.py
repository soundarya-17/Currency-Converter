import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

kivy.require('2.0.0')
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('design.ky')


class ConvertScreen(Screen):
    def convert(self):
        self.manager.current = "convert_screen"

    def franc(self, val):
        if (val.isalpha()):
            self.ids.answer.text = "Enter a valid amount"
        elif (int(val) <= 0):
            self.ids.answer.text = "Enter A greater value"
        else:
            francvalue = int(val) * 0.012
            passing = "The franc value is"
            self.ids.answer.text = passing + " " + str(francvalue)

    def peso(self, val):

        if (val.isalpha()):
            self.ids.answer.text = "Enter a valid amount"
        elif (int(val) <= 0):
            self.ids.answer.text = "Enter A greater value"
        else:
            pesovalue = int(val) * 0.68
            passing = "The peso value is"
            self.ids.answer.text = passing + " " + str(pesovalue)

    def dollar(self, val):
        if (val.isalpha()):
            self.ids.answer.text = "Enter a valid amount"
        elif (int(val) <= 0):
            self.ids.answer.text = "Enter A greater value"
        else:
            dollarvalue = int(val) * 0.014
            passing = "The dollar value is"
            self.ids.answer.text = passing + " " + str(dollarvalue)

    def dinar(self, val):
        if (val.isalpha()):
            self.ids.answer.text = "Enter a valid amount"
        elif (int(val) <= 0):
            self.ids.answer.text = "Enter A greater value"
        else:
            dinarvalue = int(val) * 0.0041
            passing = "The dinar value is"
            self.ids.answer.text = passing + " " + str(dinarvalue)


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
# to import file we use builder file
