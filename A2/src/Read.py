## @file Read.py
#  @author Bill Nguyen
#  @brief gets data from textfiles and adds data to necssary list
#  @date February 11, 2019

from StdntAllocTypes import *
from DCapALst import *
from SALst import *

## @brief an abstract data type that reads data


class Read:
    ## @brief gets data of student from textfile and adds it to SALst
    #  @param s is the text file that you extract the data from
    @staticmethod
    def load_stdnt_data(s):
        SALst.init()
        file = open(s, "r")
        f_list = file.readlines()
        for line in f_list:
            sinfo = line.replace(
                ' ', '').replace(
                '[', '').replace(
                ']', '').strip('\n').split(',')
            macid = sinfo[0]
            fname = sinfo[1]
            lname = sinfo[2]
            if sinfo[3] == "male":
                gender = GenT.male
            elif sinfo[3] == "female":
                gender = GenT.female
            gpa = float(sinfo[4])
            choices = []
            for i in range(5, len(sinfo)):
                if (not sinfo[i] == "True") and (not sinfo[i] == "False"):
                    if sinfo[i] == "civil":
                        choices.append(DeptT.civil)
                    elif sinfo[i] == "chemical":
                        choices.append(DeptT.chemical)
                    elif sinfo[i] == "electrical":
                        choices.append(DeptT.electrical)
                    elif sinfo[i] == "mechanical":
                        choices.append(DeptT.mechanical)
                    elif sinfo[i] == "software":
                        choices.append(DeptT.software)
                    elif sinfo[i] == "materials":
                        choices.append(DeptT.materials)
                    elif sinfo[i] == "engphys":
                        choices.append(DeptT.engphys)
                else:
                    freechoice = sinfo[i].strip("\n") == "True"
            sinfo1 = SInfoT(fname, lname, gender, gpa, SeqADT(choices), freechoice)
            SALst.add(macid, sinfo1)
        file.close()

    ## @brief gets data of departments from textfile and adds it to DCapALst
    #  @param s is the text file that you extract the data from
    @staticmethod
    def load_dcap_data(s):
        DCapALst.init()
        file = open(s, "r")
        file_list = file.readlines()
        for dept in file_list:
            split_list = dept.split(",")
            DCapALst.add(split_list[0], int(split_list[1].strip("\n")))
        file.close()
