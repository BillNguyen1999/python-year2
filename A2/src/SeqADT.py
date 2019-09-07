## @file SeqADT.py
#  @author Bill Nguyen
#  @brief mainly for DeptT since it helps go through student choices
#  @date February 11, 2019

## @brief an abstract data type that represents a sequence


class SeqADT:
    ## @brief initializes SeqADT
    #  @param x is represents the list of choices of a student
    def __init__(self, x):
        self.s = x
        self.i = 0

    ## @brief start function that initializes i to zero
    def start(self):
        self.i = 0

    ## @brief next function that goes to the student next choice
    #  @details returns the current position of next but iterates to the next choice
    #  When there are no more choices and user inputs this function it will raise an error
    #  @return returns the current choice of student which is self.s[self.i]
    def next(self):
        if self.i >= len(self.s):
            raise StopIteration
        temp = self.i
        self.i = self.i + 1
        return self.s[temp]

    ## @brief inidcates whether there are any choices left
    #  @return a boolean value indicating if the there is nothing left in the list or not
    def end(self):
        return self.i >= len(self.s)
