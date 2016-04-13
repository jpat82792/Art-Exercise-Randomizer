import xml.etree.ElementTree as ET
import random as ran


class gatherXML:
    def __init__(self):
        self.int_rand_adjectives = ran.randrange(0,48)
        self.int_rand_nouns = ran.randrange(0, 48)
        self.int_rand_verbs = ran.randrange(0, 48)
        self.array_adjectives = []
        self.array_nouns = []
        self.array_verbs = []
        self.adjectives = ET.parse("dictionaries/adjectives.xml")
        self.nouns = ET.parse("dictionaries/nouns.xml")
        self.verbs = ET.parse("dictionaries/verbs.xml")
        self.adjectives_root = self.adjectives.getroot()
        self.nouns_root = self.nouns.getroot()
        self.verbs_root = self.verbs.getroot()
        print(self.adjectives_root.tag)
        print(self.nouns_root.tag)
        print(self.verbs_root.tag)
        for child in self.adjectives_root:
            print(child.text)
            self.array_adjectives.append(child.text)
        for child in self.nouns_root:
            print(child.text)
            self.array_nouns.append(child.text)
        for child in self.verbs_root:
            print(child.text)
            self.array_verbs.append(child.text)

    def reset_randoms(self):
        self.int_rand_adjectives = ran.randrange(0, 48)
        self.int_rand_nouns = ran.randrange(0, 48)
        self.int_rand_verbs = ran.randrange(0, 48)

    def get_current_adjective(self):
        return "Adjective: " + self.array_adjectives[self.int_rand_adjectives]

    def get_current_noun(self):
        return "Noun: " + self.array_nouns[self.int_rand_nouns]

    def get_current_verb(self):
        return "Verb: " + self.array_verbs[self.int_rand_verbs]

    def new_words(self, btn, label_adj, label_noun, label_verb):
        self.reset_randoms()
        label_adj.text = self.get_current_adjective()
        label_noun.text = self.get_current_noun()
        label_verb.text = self.get_current_verb()






