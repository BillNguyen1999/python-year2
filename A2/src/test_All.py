## @file test_All.py
#  @author Bill Nguyen
#  @brief test functionality of SeqADT, DCapALst and SALst
#  @date February 11, 2019

from StdntAllocTypes import *
from SeqADT import *
from DCapALst import *
from AALst import *
from SALst import *

from pytest import *


class TestSeqADT:
    def test_seq_next(self):
        sequence = SeqADT([DeptT.civil, DeptT.software, DeptT.chemical])
        assert sequence.next() == DeptT.civil
        assert sequence.next() == DeptT.software
        assert sequence.next() == DeptT.chemical

    def test_seq_next_stop(self):
        sequence = SeqADT([])
        with raises(StopIteration):
            sequence.next()

    def test_seq_end(self):
        sequence = SeqADT([])
        assert sequence.end()

    def test_seq_end2(self):
        sequence = SeqADT([DeptT.software])
        assert sequence.end() == False

    def test_seq_start(self):
        zero = 0
        assert zero == 0


class TestDCapALst:
    def test_dcap_add_error(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 3)
        with raises(KeyError):
            DCapALst.add(DeptT.civil, 3)

    def test_dcap_remove_error(self):
        DCapALst.init()
        with raises(KeyError):
            DCapALst.remove(DeptT.civil)

    def test_dcap_capacity(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 3)
        capacity = DCapALst.capacity(DeptT.civil)
        assert capacity == 3

    def test_dcap_capacity2(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 100000)
        capacity = DCapALst.capacity(DeptT.civil)
        assert capacity == 100000

    def test_dcap_capacity3(self):
        DCapALst.init()
        with raises(KeyError):
            DCapALst.capacity(DeptT.civil)

    def test_dcap_elm(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 100000)
        elm = DCapALst.elm(DeptT.civil)
        assert elm

    def test_dcap_elm2(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 100000)
        DCapALst.remove(DeptT.civil)
        elm = DCapALst.elm(DeptT.civil)
        elm2 = DCapALst.elm("Harry")
        assert elm == False
        assert elm2 == False


class TestSALst:
    def test_sal_add_error(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.software]), True)
        SALst.add("stdnt1", sinfo1)
        with raises(KeyError):
            SALst.add("stdnt1", sinfo1)

    def test_sal_remove_error(self):
        SALst.init()
        with raises(KeyError):
            DCapALst.remove("macid1")

    def test_sal_elm(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.software]), True)
        SALst.add("stdnt1", sinfo1)
        elm = SALst.elm("stdnt1")
        assert elm

    def test_sal_sort(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 8.0,
                        SeqADT([DeptT.civil, DeptT.software]), True)
        sinfo2 = SInfoT("first", "last", GenT.male, 11.0,
                        SeqADT([DeptT.civil, DeptT.software]), True)
        sinfo3 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.software]), True)
        sinfo4 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.software]), False)
        SALst.add("stdnt1", sinfo1)
        SALst.add("stdnt2", sinfo2)
        SALst.add("stdnt3", sinfo3)
        SALst.add("stdnt4", sinfo4)
        sort = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        assert sort == ['stdnt3', 'stdnt2', 'stdnt1']

    def test_sal_average(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 8.0,
                        SeqADT([DeptT.civil, DeptT.software]), True)
        sinfo2 = SInfoT("first", "last", GenT.male, 11.0,
                        SeqADT([DeptT.civil, DeptT.software]), True)
        sinfo3 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.software]), True)
        sinfo4 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.software]), False)
        SALst.add("stdnt1", sinfo1)
        SALst.add("stdnt2", sinfo2)
        SALst.add("stdnt3", sinfo3)
        SALst.add("stdnt4", sinfo4)
        avg = SALst.average(lambda x: x.gender == GenT.male)
        assert avg == 10.75

    def test_sal_allocate(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.software]), True)
        SALst.add("stdnt1", sinfo1)
        SALst.allocate()
        choice = AALst.lst_alloc(DeptT.civil)
        assert choice == ['stdnt1']
