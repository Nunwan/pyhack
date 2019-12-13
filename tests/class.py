#!/usr/bin/env python3

class Essai:
    def __init__(self):
        self.x = 1
        self.y = 2

    def use(self):
        print(self.__dict__)
        self.__dict__['x'] += 1
        print(self.__dict__)
        print(self.x)

if __name__ == "__main__":
    essai = Essai()
    essai.use()
