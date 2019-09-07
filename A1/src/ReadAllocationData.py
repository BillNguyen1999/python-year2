## @file ReadAllocationData.py
#  @author Bill Nguyen
#  @brief Reads Data to generate student information entering second year
#  @date January 18, 2019



## @brief Gets all the students in textfile and makes a list filled with dictionaries representing students
#  @param s is textfile representing students entering second year
#  @return List with dictionaries inside, representing students entering second year
def readStdnts(s):
    file = open(s, "r")
    values = ["macid", "fname", "lname", "gender", "gpa", "choices"]
    student_list = []
    file_list = file.readlines()
    for line in file_list:
        split_list = line.split(",")
        student_dict = {}
        for i in range(0, 6):
            if i == 4:
                gpa = float(split_list[i])
                student_dict[values[i]] = gpa
            elif i == 5:
                choices = split_list[i].split()
                student_dict[values[i]] = choices
            else:
                student_dict[values[i]] = split_list[i]
        student_list.append(student_dict)
    file.close()
    return student_list

## @brief Puts all students with free choice into a list
#  @param s is textfile containing students who have free choice
#  @return List with all students who have free choice
def readFreeChoice(s):
    file = open(s, "r")
    free_list = []
    for line in file:
        free_list.append(line.strip("\n"))
    file.close()
    return free_list
## @brief Creates a dictionary that contains the capacity of each department
#  @param s is a textfile that contains all department capacities
#  @return Dictionary of all department capacities
def readDeptCapacity(s):
    file = open(s, "r")
    dept_dict = {}
    file_list = file.readlines()
    for dept in file_list:
        split_list = dept.split(",")
        dept_dict[split_list[0]] = int(split_list[1].strip("\n"))
    file.close()
    return dept_dict

