#Generates random sentences based on template sentence structure
from time import *

#The 'Random' class definition
class Random:
    def __init__(self,seed):
        self.s = seed
        self.n = self.s
    def next(self, range):
        self.n = ((7**5)*((self.n)-1))%((2**31)-1)
        return self.n%range
    def choose(self, objects):
        temp = self.next(len(objects))
        return objects[temp]
    
#The 'Wonce' class definition
class Wonce:
    def __init__(self, seed):
        self.first = []
        self.follow = {}
        self.random = Random(seed)
        self.count = 0
    def add(self, word):
        self.first.append(word[0])
        self.count += 1
        i = 1
        while i<len(word) and " " in word:
            if word[i] == " ":
                break
            self.first[self.count-1] += word[i]
            i += 1
        i = 0
        prev = ""
        while not(i >= len(word) or word[i]==" "):
                prev += word[i]
                i += 1
        i += 1
        while i<(len(word)-1):
            nex = ""
            while not(i >= len(word) or word[i]==" "):
                nex += word[i]
                i += 1
            if prev in self.follow:
                self.follow[prev].append(nex)
            else:
                self.follow[prev] = [nex]
            prev = nex
            i += 1
    def make(self, size):
        word = ""
        another = self.random.choose(self.first)
        word += another
        word += " "
        i = 0
        while i<size-1:
            if another in self.follow:
                another = self.random.choose(self.follow[another])
                word += another
            else:
                another = self.random.choose(self.first)
                word += another
            if i<size-2:
                word += " "
            else:
                word += "."
            i += 1
        return word

#Implementation

go = Wonce(int(time())) 
go.add("This is an example sentence")
go.make(4) # make a sentence of length 4
