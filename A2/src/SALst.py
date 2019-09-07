## @file SALst.py
#  @author Bill Nguyen
#  @brief makes list of students and have tools to manipulate list (sort, allocate etc.)
#  @date February 11, 2019

from StdntAllocTypes import *
from DCapALst import *
from AALst import *

## @brief an abstract data type that represents a set of students


class SALst:
    ## @brief initializes class by creating an empty list
    @staticmethod
    def init():
        SALst.s = []

    ## @brief adds macid and student info to list
    #  @param m represents a string that is the macid
    #  @param i represents student information in a named tuple
    @staticmethod
    def add(m, i):
        for j in SALst.s:
            if m in j:
                raise KeyError
        SALst.s.append([m, i])

    ## @brief removes student from list based on macid
    #  @param m is a string that represents the macid of student
    @staticmethod
    def remove(m):
        count = 0
        for i in SALst.s:
            if m in i:
                SALst.s.remove(i)
                count += 1
        if count == 0:
            raise KeyError

    ## @brief checks if student is in list or not
    #  @param m is a string that represents macid
    #  @return True when student is in list else returns False
    @staticmethod
    def elm(m):
        for i in SALst.s:
            if m in i:
                return True
        return False

    ## @brief returns the student info of given student
    #  @param m is a string that represents macid
    #  @return A namedtuple that represents the student info
    @staticmethod
    def info(m):
        for i in SALst.s:
            if m in i:
                return i[1]
        raise KeyError

    ## @brief gets gpa of given student in the list of students
    #  @param m is a string that represents macid
    #  @param s is the list of students with macid and student info
    #  @return gpa of selected student
    @staticmethod
    def get_gpa(m, s):
        for i in s:
            if m in i:
                return i[1].gpa

    ## @brief sorts the list of students based on given condition
    #  @param f is like a filter where it indicates what you want to sort
    #  in the given condition
    #  @return a sorted list in descending order based on given condition
    @staticmethod
    def sort(f):
        sort_list = list(filter(lambda stdnt: f(stdnt[1]), SALst.s))
        for j in range(len(sort_list)):
            index = 0
            while index < (len(sort_list) - 1):
                if (sort_list[index][1].gpa > sort_list[index + 1]
                        [1].gpa) or (sort_list[index][1].gpa == sort_list[index + 1][1].gpa):
                    index += 1
                else:
                    temp = sort_list[index]
                    sort_list[index] = sort_list[index + 1]
                    sort_list[index + 1] = temp
        macid_list = []
        for k in sort_list:
            macid_list.append(k[0])
        return macid_list

    ## @brief gives the average gpa of students based on given condition
    #  @param f is a filter (like the sort function)
    #  @return the average gpa of students
    @staticmethod
    def average(f):
        avg_list = list(filter(lambda stdnt: f(stdnt[1]), SALst.s))
        add = 0
        if len(avg_list) == 0:
            raise ValueError
        for stdnt in avg_list:
            add += stdnt[1].gpa
        return add / len(avg_list)

    ## @brief allocates students to department based on gpa and freechoice
    #  @details sorts and allocates people with free choice first
    #  and then allocates students who don't have free choice
    @staticmethod
    def allocate():
        AALst.init()
        f = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for m in f:
            ch = SALst.info(m).choices
            AALst.add_stdnt(ch.next(), m)
        s = SALst.sort(lambda t: not t.freechoice and t.gpa >= 4.0)
        for m in s:
            ch = SALst.info(m).choices
            alloc = False
            while not alloc and not ch.end():
                d = ch.next()
                if AALst.num_alloc(d) < DCapALst.capacity(d):
                    AALst.add_stdnt(d, m)
                    alloc = True
            if not alloc:
                raise RuntimeError
