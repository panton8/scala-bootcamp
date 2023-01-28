import pytest

from solver.main import Solver

_solver = Solver()


@pytest.fixture
def solver():
    return _solver


def test_th_5c6dAcAsQs(solver):
    assert solver.process("texas-holdem 5c6dAcAsQs Ks4c KdJs 2hAh Kh4h Kc7h 6h7d 2cJc") == "2cJc Kh4h=Ks4c Kc7h KdJs 6h7d 2hAh"


def test_th_2h5c8sAsKc(solver):
    assert solver.process("texas-holdem 2h5c8sAsKc Qs9h KdQh 3cKh Jc6s") == "Jc6s Qs9h 3cKh KdQh"


def test_th_3d4s5dJsQd(solver):
    assert solver.process("texas-holdem 3d4s5dJsQd 5c4h 7sJd KcAs 9h7h 2dTc Qh8c TsJc") == "9h7h 2dTc KcAs 7sJd TsJc Qh8c 5c4h"


def test_th_5c5h5s8sAc(solver):
    assert solver.process("texas-holdem 5c5h5s8sAc 3h6d 6c9s 7cJd As6s 9cAd 4sTd Ts3d 8c8h") == "3h6d 6c9s 4sTd=Ts3d 7cJd 9cAd=As6s 8c8h"


def test_th_4c4s7c7d7s(solver):
    assert solver.process("texas-holdem 4c4s7c7d7s 8c3h 2hJh 9h6c QsJc 2s3d Ad4h 2c8d Kd2d Th6d") == "2c8d=2hJh=2s3d=8c3h=9h6c=Ad4h=Kd2d=QsJc=Th6d"


def test_th_4c4h4s6c6h(solver):
    assert solver.process("texas-holdem 4c4h4s6c6h 3dJc 2c5c 7h6s TsQc") == "2c5c=3dJc=TsQc 7h6s"


def test_th_4h5d8h9sQd(solver):
    assert solver.process("texas-holdem 4h5d8h9sQd Jc3c 5c8d Kd2s 6h3s 8sAc 6d6s Kc9c 5h2h Ah3d") == "6h3s Jc3c Kd2s Ah3d 5h2h 6d6s 8sAc Kc9c 5c8d"


def test_th_3c5c7d7sKh(solver):
    assert solver.process("texas-holdem 3c5c7d7sKh AcJs Tc6d Jc5d Td9c Ts8c 4c8d KcTh 7cQh") == "4c8d Tc6d Ts8c Td9c AcJs Jc5d KcTh 7cQh"


def test_th_2c5h6h9cAs(solver):
    assert solver.process("texas-holdem 2c5h6h9cAs Jc8c Td7c 3s2s TcKc 9sTs 8s4h Th6d 7s8h QsAh") == "8s4h Td7c Jc8c TcKc 3s2s Th6d 9sTs QsAh 7s8h"


def test_th_3c6h9h9sQh(solver):
    assert solver.process("texas-holdem 3c6h9h9sQh TcKh 4h4s") == "TcKh 4h4s"