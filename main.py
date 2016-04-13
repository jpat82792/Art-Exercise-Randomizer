import gui
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

class TestApp(App):
    def build(self):
        self.title = "Art Exercise Word Randomizer"
        #Window.clearcolor = (0.04705, 0.1019, .10588, 1)
        return gui.BoxLayoutWords()

if __name__ == "__main__":
    TestApp().run()
