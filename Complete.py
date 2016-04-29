import readexcel
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
                        self._1.append(a[:-1])
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
                        self._2.append(a[:-1])
                        count += 1
                if count < 10:
                    new = readexcel.correct(input)
                    for pre in new:
                        for a in self.words:
                            if a.startswith(pre):
                                self._2.append(a[:-1])
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
                        self._1.append(a[:-1])
                        count += 1
                if count < 10:
                    new = readexcel.correct(input)
                    for pre in new:
                        for a in self.words:
                            if a.startswith(pre):
                                self._1.append(a[:-1])
                                count += 1
                if count < 10:
                    for n in range(10-count):
                        self._1.append('')
                return self._1[0:10]
def main ():
    with open('data.txt') as file:
        words = file.readlines()
    com = Complete(words)
    return com
if __name__ == '__main__':
    com = main()

    (com.out('t'))
    print(com._1)
    #print(com._2)
    (com.out('te'))
    #print(com._1)
    print(com._2)
    (com.out('ter'))
    print(com._1)
    #print(com._2)
    (com.out('tera'))
    #print(com._1)
    print(com._2)
    (com.out('teras'))
    print(com._1)
    #print(com._2)
