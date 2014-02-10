from string import split
from string import ascii_uppercase
from string import ascii_lowercase

names = open('names.txt')
names = names.read()
names = names.split(',')


total_score = 0
for nameIndex in len(names):
	total_score += (nameIndex+1) * score_of_word(names[nameIndex])


def make_letter_scores_dict():
	scores = {}
	for char in (ascii_lowercase + ascii_uppercase):
		order = ord(char)
		if order <= 122  and order >= 97:
			#lowercase
			scores[char] = order - 96
		elif order <= 90  and order >= 65:
			#uppercase
			scores[char] = order - 64      
		else:
			#invalid char
			pass
	return scores

print make_letter_scores_dict()

#print names

#for name in names:
	#Strip quotes.

def score_of_word(word):
	letter_scores = {}
	score = 0
	for letter in word:
		#Needs a check for letter existace in dict.
		score += letter_scores[letter]
	return score



