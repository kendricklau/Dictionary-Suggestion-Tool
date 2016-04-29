import re
import collections

#checks input text for regular expression
#returns altered text with all lowercase letters
#def words(text):
 #   return re.findall('[a-z]+', text.lower())
    #stuff = re.findall('[a-z]+', text.lower())
    #return [(stuff[l], l) for l in range(len(stuff))]
    #return re.findall('[a-z]+', text.lower())

#trains algorithm using input file to determine frequency of words
#def train(features):
#    model = collections.defaultdict(lambda: 1)
#    for f in features:
#        model[f] += 1
#    return model

#NWORDS = train(words(file('data.txt').read()))
with open('data.txt') as txtfile:
    NWORDS1 = txtfile.readlines()
NWORDS = NWORDS1[0:19339]
#
# i = 19340
# while i < 85488:
#     NWORDS.append(NWORDS1[i])
#     i += 4
#NWORDS = words(file('data.txt').read())

#alphabet = 'abcdefghijklmnopqrstuvwxyz'
from string import ascii_lowercase as alphabet
keyboard = ["qwertyuiop","asdfghjkl","zxcvbnm"]
#performs various operations on input in order to try to correct word
def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   #deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces = []
   for a, b in splits:
       for key in keyboard:
           if b and b[0] in key:
               val = key.index(b[0])
               if val > 0:
                   replaces.append(a + key[val - 1] + b[1:])
               if val < len(key)-1:
                   replaces.append(a + key[val + 1] + b[1:])
   #replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   #inserts    = [a + c + b     for a, b in splits for c in alphabet]
   #return set(transposes + replaces)
   return set(replaces + transposes)
   #return set(deletes + transposes + replaces + inserts)

#two edits
def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

#one edit
def known(words):
    emily = set()
    for n in words:
        for i in NWORDS:
            if i.startswith(n):
                emily.add(n)
                break
    return emily
    #return set(w for w in words if w in NWORDS)

#final function that returns correction or original word
def correct(word):
    #candidates = known([word]) or known(edits1(word)) or [word]
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    #candidates = known([word]) | known(edits1(word)) | known_edits2(word) | set(word)
    #return max(candidates, key=NWORDS.get)
    #return max(candidates)
    popularity = []
    for i in candidates:
        for j in range(len(NWORDS)):
            if NWORDS[j].startswith(i):
                popularity.append((j, i))
                break
    #return candidates
    popularity.sort()
    return [b for a, b in popularity]
    #return popularity

if __name__ == '__main__':
    text = input('Enter word here: ')
    #text = raw_input('Enter word here: ')
    best = correct(text)
    print(best)
