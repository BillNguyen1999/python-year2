## @file testCalc.py
#  @author Bill Nguyen
#  @brief Testing CalcModule.py functions
#  @date January 18,2019

from ReadAllocationData import *
from CalcModule import *

#Referenced Assignment 1 2018 Solution For Format of testCalc.py

def assertionEqual(testcase, result, name):
    if testcase == result:
        print("%s passed" % (name))
    else:
        print("%s failed, correct result is: %s" % (name, result))



def testSort1():
    sort_list = sort(readStdnts("src/TextFiles/ReadStdntsTest1.txt"))
    #TestSort1: when ReadStdnts is empty
    #Results suppose to be []
    assertionEqual(sort_list, [], "TestSort1")

def testSort2():
    #TestSort2: normal input
    sort_list = sort(readStdnts("src/TextFiles/ReadStdntsTest2.txt"))
    correct = [{'macid': 'macid3',
               'fname': 'firt3',
               'lname': 'last3',
               'gender': 'female',
               'gpa': 12.0,
               'choices': ['software', 'mechanical', 'electrical']},
               {'macid': 'macid2',
               'fname': 'first2',
               'lname': 'last2',
               'gender': 'male',
               'gpa': 11.0,
               'choices': ['civil', 'chemical', 'engphys']},
               {'macid': 'macid4',
               'fname': 'firt4',
               'lname': 'last4',
               'gender': 'male',
               'gpa': 11.0,
               'choices': ['chemical', 'mechanical', 'electrical']},
               {'macid': 'macid1',
               'fname': 'first1',
               'lname': 'last1',
               'gender': 'male',
               'gpa': 10.8,
               'choices': ['software', 'mechanical', 'electrical']},
               {'macid': 'macid5',
               'fname': 'firt5',
               'lname': 'last5',
               'gender': 'male',
               'gpa': 9.0,
               'choices': ['mechanical', 'electrical', 'materials']},
               {'macid': 'macid6',
               'fname': 'firt6',
               'lname': 'last6',
               'gender': 'female',
               'gpa': 4.0,
               'choices': ['engphys', 'mechanical', 'materials']}]
    assertionEqual(sort_list, correct, "TestSort2")

def testAverage1():
    avg = average(readStdnts("src/TextFiles/ReadStdntsTest1.txt"), "male")
    #testing when text file is empty
    assertionEqual(avg, 0, "TestAverage1")

def testAverage2():
    avg = average(readStdnts("src/TextFiles/ReadStdntsTest2.txt"), "male")
    correct = 10.45
    #testing with normal inputs
    assertionEqual(avg, correct, "TestAverage2")

def testAverage3():
    avg = average(readStdnts("src/TextFiles/ReadStdntsTest3.txt"), "female")
    #testing with only male inputs but checking for female average
    assertionEqual(avg, 0, "TestAverage3")
def testAverage4():
    avg = average(readStdnts("src/TextFiles/ReadStdntsTest2.txt"), "hello")
    #testing when user does not input male or female in g
    assertionEqual(avg, "in g enter male or female", "TestAverage4")

def testAllocate1():
    allo = allocate(readStdnts("src/TextFiles/ReadStdntsTest1.txt"), readFreeChoice("src/TextFiles/ReadFreeChoiceTest1.txt"), readDeptCapacity("src/TextFiles/ReadDeptCapacityTest1.txt"))
    #testing when every textfiles are empty
    correct = {'civil': [],
        'chemical': [],
        'electrical': [],
        'software': [],
        'materials': [],
        'mechanical': [],
        'engphys': []}
    assertionEqual(allo, correct, "TestAllocate1")

def testAllocate2():
    allo = allocate(readStdnts("src/TextFiles/ReadStdntsTest2.txt"), readFreeChoice("src/TextFiles/ReadFreeChoiceTest2.txt"), readDeptCapacity("src/TextFiles/ReadDeptCapacityTest2.txt"))
    #testing with normal inputs
    correct = {'civil': [{'macid': 'macid2', 'fname': 'first2', 'lname': 'last2', 'gender': 'male', 'gpa': 11.0, 'choices': ['civil', 'chemical', 'engphys']}], 'chemical': [{'macid': 'macid4', 'fname': 'firt4', 'lname': 'last4', 'gender': 'male', 'gpa': 11.0, 'choices': ['chemical', 'mechanical', 'electrical']}], 'electrical': [], 'software': [{'macid': 'macid1', 'fname': 'first1', 'lname': 'last1', 'gender': 'male', 'gpa': 10.8, 'choices': ['software', 'mechanical', 'electrical']}], 'materials': [], 'mechanical': [{'macid': 'macid3', 'fname': 'firt3', 'lname': 'last3', 'gender': 'female', 'gpa': 12.0, 'choices': ['software', 'mechanical', 'electrical']}, {'macid': 'macid5', 'fname': 'firt5', 'lname': 'last5', 'gender': 'male', 'gpa': 9.0, 'choices': ['mechanical', 'electrical', 'materials']}], 'engphys': [{'macid': 'macid6', 'fname': 'firt6', 'lname': 'last6', 'gender': 'female', 'gpa': 4.0, 'choices': ['engphys', 'mechanical', 'materials']}]}
    assertionEqual(allo, correct, "TestAllocate2")

def testAllocate3():
    allo = allocate(readStdnts("src/TextFiles/ReadStdntsTest2.txt"), readFreeChoice("src/TextFiles/ReadFreeChoiceTest1.txt"), readDeptCapacity("src/TextFiles/ReadDeptCapacityTest2.txt"))
    #testing when ReadFreeChoice text file is empty
    correct = {'civil': [{'macid': 'macid2', 'fname': 'first2', 'lname': 'last2', 'gender': 'male', 'gpa': 11.0, 'choices': ['civil', 'chemical', 'engphys']}], 'chemical': [{'macid': 'macid4', 'fname': 'firt4', 'lname': 'last4', 'gender': 'male', 'gpa': 11.0, 'choices': ['chemical', 'mechanical', 'electrical']}], 'electrical': [], 'software': [{'macid': 'macid3', 'fname': 'firt3', 'lname': 'last3', 'gender': 'female', 'gpa': 12.0, 'choices': ['software', 'mechanical', 'electrical']}], 'materials': [], 'mechanical': [{'macid': 'macid1', 'fname': 'first1', 'lname': 'last1', 'gender': 'male', 'gpa': 10.8, 'choices': ['software', 'mechanical', 'electrical']}, {'macid': 'macid5', 'fname': 'firt5', 'lname': 'last5', 'gender': 'male', 'gpa': 9.0, 'choices': ['mechanical', 'electrical', 'materials']}], 'engphys': [{'macid': 'macid6', 'fname': 'firt6', 'lname': 'last6', 'gender': 'female', 'gpa': 4.0, 'choices': ['engphys', 'mechanical', 'materials']}]}
    assertionEqual(allo, correct, "TestAllocate3")

def testAllocate4():
    allo = allocate(readStdnts("src/TextFiles/ReadStdntsTest4.txt"), readFreeChoice("src/TextFiles/ReadFreeChoiceTest2.txt"), readDeptCapacity("src/TextFiles/ReadDeptCapacityTest2.txt"))
    #testing when some people go their third choice stream
    correct = {'civil': [], 'chemical': [{'macid': 'macid2', 'fname': 'first2', 'lname': 'last2', 'gender': 'male', 'gpa': 11.0, 'choices': ['software', 'chemical', 'engphys']}], 'electrical': [{'macid': 'macid5', 'fname': 'firt5', 'lname': 'last5', 'gender': 'male', 'gpa': 9.0, 'choices': ['mechanical', 'electrical', 'materials']}], 'software': [{'macid': 'macid1', 'fname': 'first1', 'lname': 'last1', 'gender': 'male', 'gpa': 10.8, 'choices': ['software', 'mechanical', 'electrical']}], 'materials': [{'macid': 'macid6', 'fname': 'firt6', 'lname': 'last6', 'gender': 'female', 'gpa': 4.0, 'choices': ['mechanical', 'software', 'materials']}], 'mechanical': [{'macid': 'macid4', 'fname': 'firt4', 'lname': 'last4', 'gender': 'male', 'gpa': 11.0, 'choices': ['mechanical', 'materials', 'electrical']}, {'macid': 'macid3', 'fname': 'firt3', 'lname': 'last3', 'gender': 'female', 'gpa': 12.0, 'choices': ['software', 'mechanical', 'electrical']}], 'engphys': []}
    assertionEqual(allo, correct, "TestAllocate4")

def testAllocate5():
    allo = allocate(readStdnts("src/TextFiles/ReadStdntsTest5.txt"), readFreeChoice("src/TextFiles/ReadFreeChoiceTest2.txt"), readDeptCapacity("src/TextFiles/ReadDeptCapacityTest2.txt"))
    #testing when every student has a gpa below 4.0 or gpa above 12.0
    correct = {'civil': [],
        'chemical': [],
        'electrical': [],
        'software': [],
        'materials': [],
        'mechanical': [],
        'engphys': []}
    assertionEqual(allo, correct, "TestAllocate5")

def test():
    testSort1()
    testSort2()
    testAverage1()
    testAverage2()
    testAverage3()
    testAverage4()
    testAllocate1()
    testAllocate2()
    testAllocate3()
    testAllocate4()
    testAllocate5()

test()
