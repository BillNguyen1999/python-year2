## @file StdntAllocTypes.py
#  @author Bill Nguyen
#  @brief initializes the enumerations of GenT and DeptT and a namedtuple SInfoT
#  @date February 11, 2019

from enum import Enum
from typing import NamedTuple
from SeqADT import *

## @brief an enumeration of GenT for male and female
#  @param Enum for enumeration


class GenT(Enum):
    male = 1
    female = 2

## @brief an enumeration of DeptT for all the departments
#  @param Enum for enumeration


class DeptT(Enum):
    civil = 1
    chemical = 2
    electrical = 3
    mechanical = 4
    software = 5
    materials = 6
    engphys = 7

## @brief a named tuple of SInfoT where we store all the information about a student
#  @param NamedTuple


class SInfoT(NamedTuple):
    fname: str
    lname: str
    gender: type(GenT)
    gpa: float
    choices: type(SeqADT(DeptT))
    freechoice: bool
