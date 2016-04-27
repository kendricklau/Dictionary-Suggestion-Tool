import csv
class Complete:
    def __init__(self, words):
        self.words = words
        self.out = []
    def fin(self, input):
        self.out = []
        count = 0
        if input:
            for a in self.words:
                if a.startswith(input):
                    self.out.append(a)
                    count += 1
                if count == 5:
                    break
        if count < 5:
            for n in range (5 - count):
                self.out.append('')
        return self.out
def main(text):
	words = []
	with open('database.csv') as cvsfile:
	    reader = csv.reader(cvsfile)
	    for line in reader:
	        words.append(line[1])
	com = Complete(words)
	return com.fin(text)
