from StdntAllocTypes import *
from SeqADT import *
from DCapALst import *
from AALst import *
from SALst import *

DCapALst.init()
DCapALst.add(DeptT.civil, 2)
DCapALst.add(DeptT.software, 1)
print(DCapALst.s)
sinfo1 = SInfoT("first", "last", GenT.male, 12.0, SeqADT([DeptT.civil, DeptT.software]), True)

SALst.init()
SALst.add("stdnt1", sinfo1)


print(SALst.elm("stdnt1"))

print(SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0))

print(SALst.average(lambda x: x.gender == GenT.male))


SALst.allocate()
print(AALst.lst_alloc(DeptT.civil))

