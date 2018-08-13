from PyDictionary import PyDictionary
from utilities.GeneralUtilities import print_say
from six.moves import input
import warnings
import sys
import six
import os
warnings.filterwarnings("ignore")


def blockPrint():
    sys.stdout = open(os.devnull, 'w')


def enablePrint():
    sys.stdout = sys.__stdout__


def dictionary(self):
	# Returns meaning, synonym and antonym of any word
	Dict = PyDictionary()
	print_say('\nEnter word', self)
	word = input()

	#Gets and displays each meaning of the word
	if Dict.googlemeaning(word) == None:
		#executes if googlemeaning() is not working
		#part_of_speech refers to verbs, nouns, adverbs etc
		#definition is the meaning explanantion
		meaning = Dict.meaning(word)
		print('\nMeanings: ') 
		for part_of_speech in meaning:
			print(part_of_speech + ':')
			for definition in meaning[part_of_speech]:
				if '(' in definition:
					print(' ~' + definition + ')')
				else:
					print(' ~' + definition)
	else:
		print('\nMeaning : ' + str(Dict.googlemeaning(word)))

	if Dict.synonym(word) != None and Dict.antonym(word) != None:
		blockPrint()
		syn = Dict.synonym(word)
		ant = Dict.antonym(word)
		syn = [x.encode('UTF8') for x in syn]
		ant = [x.encode('UTF8') for x in ant]
		enablePrint()
		print('\nSynonyms : ' + str(syn))
		print('\nAntonyms : ' + str(ant))
	else:
		print('\nSynonyms and antonyms are not available due to external module error')
