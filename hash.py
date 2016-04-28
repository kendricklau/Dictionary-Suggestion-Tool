#!/usr/bin/python3

from string import ascii_letters

# Linked list for hashtable
# Should switch to balanced binary tree for future cause it's not good
class Node:
    def __init__(self, word, defnlist):
        self.next = None
        self.word = word
        self.defn = defnlist
    def add(self, word, defnlist):
        if self.next == None:
            self.next = Node(word, defnlist)
        else:
            self.next.add(word, defnlist)

# Called with x = Hashtable(hashsize)
# Uses x.lookup("Salmon") to find list of defs
# Installs with x.lookup("Salmon", "Def")
class Hashtable:
    def __init__(self, hashsize):
        self.hashsize = hashsize
        self.storage = [Node("", [])] * hashsize
    def lookup(self, word):
        deflist = []
        node = self.storage[hash(word) % self.hashsize]
        while node != None and node.word != word:
            node = node.next
        if node == None:
            return []
        else:
            return node.defn
        #return self.storage[hash(word) % self.hashsize].defn
    def install(self, word, defn):
        if self.storage[hash(word) % self.hashsize].word == "":
            self.storage[hash(word) % self.hashsize] = Node(word, [defn])
        elif self.storage[hash(word) % self.hashsize].word != word:
            self.storage[hash(word) % self.hashsize].add(word, [defn])
        else:
            self.storage[hash(word) % self.hashsize].defn.append(defn)

# Adds all the words in file to a hash and returns it
# Currently ignores words that aren't 100% letters
def add_words(file):
    defnext = False # If true it needs to check for def next
    hashtable = Hashtable(500000)
    txtfile = open(file, 'r')
    for i in range(348):
        _ = txtfile.readline()

    for line in txtfile:
        if '<h1>' in line:
            defnext = True
            word = line.split("<h1>")[1].split("</h1>")[0].lower()
            for c in word:
                if not c in ascii_letters:
                    defnext = False
                    break
        #elif defnext and '<def>' in line and not '<er>' in line:
        elif defnext and '<def>' in line:
            defn = remove_tags(line.split("<def>")[1].split("</def>")[0])
            hashtable.install(word, defn)
            defnext = False

    txtfile.close()

    return hashtable

#def add_words(file):
#    hashtable = Hashtable(500000)
#    with open(file, 'r') as txtfile:
#        word = txtfile.readline()
#        word = word[1:]
#        defn = txtfile.readline()
#        for line in txtfile:
#            if line[0] == '*':
#                hashtable.install(word, defn)
#                word = line[1:]
#            else:
#                defn = line
#
#    return hashtable

# Removes any html tags but not the best yet
def remove_tags(defined):
    final = ""
    intag = False
    for c in defined:
        if c == '<':
            intag = True
        elif c == '>':
            intag = False
        elif not intag:
            final += c
	#change
    return final

if __name__ == '__main__':
    hashtable = add_words('text.txt')
    print(hashtable.lookup("yea"))
