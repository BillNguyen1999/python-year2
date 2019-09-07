## @file CalcModule.py
#  @author Kevin Zhou
#  @brief completes various calculations on the list of students created
#          using the functions in the previous module. 
#  @date 16/01/2019

import ReadAllocationData
lib1 = ReadAllocationData.readStdnts('library1.txt')
lib2 = ReadAllocationData.readFreeChoice('library3.txt')
lib3 = ReadAllocationData.readDeptCapacity('library2.txt')
## @brief A function that sorts the students in decending order of GPA.
#  @details It is just a general bubble sort algorithm and it takes
#            the GPA of all students and place them in decending order
#            into the list.


def sort(S):
    for num in range(len(S)-1,0,-1):
        for i in range(num):
            if S[i]['gpa']<S[i+1]['gpa']:
                temp = S[i]
                S[i] = S[i+1]
                S[i+1] = temp
    # print(S)
    return(S)
# sort(lib1)

## @brief A function that calculates the average of the students
#    based on input gender.
#  @details It takes a list and a string, which is the gender of the students,
#            and it loops through the student data to grab the matched gender.
#            Then, it just adds the gpa of those students and divides by
#            the number of the students who matches the gender.

def average(L, g):
    sum_up = 0
    gender = []
    for i in lib1:
        if i['gender'] == g:
            gender.append(i)
    for j in gender:
        sum_up = sum_up + j['gpa']
    avg = sum_up / len(gender)
    # print(avg)
    return(avg)

# average(lib1, 'Female')

## @brief A function that allocate the students in the library
#    into their choices based on various things.
#  @details It loops through the data and first put the students
#           with free choice into a list, and for the rest of those
#           students, they will be put into another list. For each list,
#           first it checks if the gpa is greater than 4, then it starts
#           placing students into their choice. For each operation, it will
#           decrease the department capacity. The 'passed' list will be sorted
#           to match the requirement.
def allocate(S,F,C):
    out = {'civil':[], 'chemical':[], 'electrical':[], 'mechanical':[], 'software':[], 'materials':[], 'engphys':[]}
    passed = []
    free = []

    for student in S:
        if student['macid'] in F:
            free.append(student)
        else:
            passed.append(student)
    
    for i in range(len(free)):
        if free[i]['gpa'] > 4.0:

            if C[(free[i]['choices'][0])] > 0:
                out[(free[i]['choices'][0])].append(free[i])
                C[(free[i]['choices'][0])] -= 1

            elif C[(free[i]['choices'][1])] > 0:
                out[(free[i]['choices'][1])].append(free[i])
                C[(free[i]['choices'][1])] -= 1

            elif C[(free[i]['choices'][2])] > 0:
                out[(free[i]['choices'][2])].append(free[i])
                C[(free[i]['choices'][2])] -= 1


    passed = sort(passed)
    for j in range(len(passed)):
        if passed[j]['gpa'] > 4.0:

            if C[(passed[j]['choices'][0])] > 0:
                out[(passed[j]['choices'][0])].append(passed[j])
                C[(passed[j]['choices'][0])] -= 1

            elif C[(passed[j]['choices'][1])] > 0:
                out[(passed[j]['choices'][1])].append(passed[j])
                C[(passed[j]['choices'][1])] -= 1

            elif C[(passed[j]['choices'][2])] > 0:
                out[(passed[j]['choices'][2])].append(passed[j])
                C[(passed[j]['choices'][2])] -= 1

    # print(out)
    return out

# allocate(lib1, lib2, lib3)