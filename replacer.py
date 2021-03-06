from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from random import randint
import nltk.data


class Replacer(object):
    def __init__(self, text):

        self.text = text
        self.output = ""

    def tokenize(self):
        # Load the pretrained neural net
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


        # Get the list of words from the entire text
        words = word_tokenize(self.text)

        # Identify the parts of speech
        tagged = nltk.pos_tag(words)
        #print tagged

        for i in range(0,len(words)):
            replacements = []

            # Only replace nouns with nouns, vowels with vowels etc.
            for syn in wordnet.synsets(words[i]):

                # Do not attempt to replace proper nouns or determiners
                if tagged[i][1] == 'NNP' or tagged[i][1] == 'DT':
                    break

                # The tokenizer returns strings like NNP, VBP etc
                # but the wordnet synonyms has tags like .n.
                # So we extract the first character from NNP ie n
                # then we check if the dictionary word has a .n. or not
                word_type = tagged[i][1][0].lower()
                if syn.name().find("."+word_type+"."):
                    # extract the word only
                    r = syn.name()[0:syn.name().find(".")]
                    replacements.append(r)

            if len(replacements) > 0:
                # Choose a random replacement
                replacement = replacements[randint(0,len(replacements)-1)]
                self.output = self.output + " " + replacement
            else:
                # If no replacement could be found, then just use the
                # original word
                self.output = self.output + " " + words[i]

    def get_output(self):
        #print the result
        return (self.output)

'''
r = Replacer("Your desire is inside spiritual fulfillment")
r.tokenize()
print r.get_output()
'''