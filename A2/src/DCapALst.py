## @file DCapALst.py
#  @author Bill Nguyen
#  @brief creates department set
#  @date February 11, 2019

from StdntAllocTypes import *

## @brief An abstract data type that represent a set of departments


class DCapALst:
    ## @brief initializes class by creating an empty list
    @staticmethod
    def init():
        DCapALst.s = []

    ## @brief add department and capacity to list
    #  @param d represents the department
    #  @param n represents capacity of d
    @staticmethod
    def add(d, n):
        for i in DCapALst.s:
            if d in i:
                raise KeyError
        DCapALst.s.append([d, n])

    ## @brief removes selected department
    #  @param d represents the department you want to remove from list
    @staticmethod
    def remove(d):
        count = 0
        for i in DCapALst.s:
            if d in i:
                DCapALst.s.remove(i)
                count += 1
        if count == 0:
            raise KeyError

    ## @brief checks if department is in the list or not
    #  @param d represents the department you want to check
    #  @return True when d is in list if not then returns False
    @staticmethod
    def elm(d):
        for i in DCapALst.s:
            if d in i:
                return True
        return False

    ## @brief checks capacity of department
    #  @param d represents department
    #  @returns a natural number indicating capacity of given department
    @staticmethod
    def capacity(d):
        for i in DCapALst.s:
            if d in i:
                return i[1]
        raise KeyError
