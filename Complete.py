class Complete:
    def __init__(self, words):
        self.words = words
        self._1 = []
        self._2 = []
        self.flag = 0
    def out(self, input):
        count = 0
        if input:
            if self.flag == 0:
                self.flag = 1
                for a in self.words:
                    if a.startswith(input):
                        self._1.append(a)
                        count += 1
                if count < 10:
                    for n in range(10-count):
                        self._1.append('')
                return self._1[0:10]

            elif self.flag == 1:
                self.flag = 2
                self._2 = []
                for a in self._1:
                    if a.startswith(input):
                        self._2.append(a)
                        count += 1
                if count < 10:
                    for n in range (10-count):
                        self._2.append('')
                return self._2[0:10]

            elif self.flag == 2:
                self.flag = 1
                self._1 = []
                for a in self._2:
                    if a.startswith(input):
                        self._1.append(a)
                        count += 1
                if count < 10:
                    for n in range(10-count):
                        self._1.append('')
                return self._1[0:10]
def main ():
    with open('data1.txt') as file:
        words = file.readlines()
    com = Complete(words)
    return com
if __name__ == '__main__':
    com = main()
    print(com.out('t'))
    print(com.out('te'))
    print(com.out('tee'))
    print(com.out('teem'))
