## @file AALst.py
#  @author Bill Nguyen
#  @brief creates allocation list that will indicating the students in each department
#  @date February 11, 2019

from StdntAllocTypes import *

## @brief an abstract data type that represents a set of departments and students


class AALst:
    # @brief initializes list by storing a list with each department and an empty list
    @staticmethod
    def init():
        AALst.s = [
            [
                DeptT.civil, []], [
                DeptT.chemical, []], [
                DeptT.electrical, []], [
                    DeptT.mechanical, []], [
                        DeptT.software, []], [
                            DeptT.materials, []], [
                                DeptT.engphys, []]]

    ## @brief adds student to selected department
    #  @param dep represents department
    #  @param m represents macid of student
    @staticmethod
    def add_stdnt(dep, m):
        for i in AALst.s:
            if dep in i:
                i[1].append(m)
    ## @brief shows the allocated students in selected department
    #  @param d represents selected department
    #  @return list of students in selected department
    @staticmethod
    def lst_alloc(d):
        for i in AALst.s:
            if d in i:
                return i[1]

    ## @brief shows the number allocated students in selected department
    #  @param d represents selected department
    #  @return number of students in selected department
    @staticmethod
    def num_alloc(d):
        for i in AALst.s:
            if d in i:
                return len(i[1])
