from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import custom_button
from kivy.uix.label import Label
from kivy.app import App
from kivy.core.window import Window
import logic


class BoxLayoutWords(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxLayoutWords, self).__init__(**kwargs)
        self.xml = logic.gatherXML()
        self.orientation = "vertical"

        self.label_adjective = Label(text="Adjective: ")
        self.label_noun = Label(text="Noun: ")
        self.label_verb = Label(text="Verb: ")
        self.button_get_stacks = custom_button.EloButton(text="Get words")
        self.button_get_stacks.bind(on_release=lambda x: self.xml.new_words(self.button_get_stacks,
                                                                  self.label_adjective,
                                                                  self.label_noun,
                                                                  self.label_verb))
        self.add_widget(self.label_adjective)
        self.add_widget(self.label_noun)
        self.add_widget(self.label_verb)
        self.add_widget(self.button_get_stacks)





