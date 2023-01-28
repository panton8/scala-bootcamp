import pytest

from solver.main import Solver

_solver = Solver()


@pytest.fixture
def solver():
    return _solver


def test_oh_5c6dAcAsQs(solver):
    assert solver.process("omaha-holdem 5c6dAcAsQs TsQh9hQc 8d7cTcJd 5s5d7s4d Qd3cKs4c KdJs2hAh Kh4hKc7h 6h7d2cJc") == "8d7cTcJd 6h7d2cJc Qd3cKs4c Kh4hKc7h KdJs2hAh 5s5d7s4d TsQh9hQc"


def test_oh_3d4s5dJsQd(solver):
    assert solver.process("omaha-holdem 3d4s5dJsQd 8s2h6s8h 7cThKs5s 5hJh2s7d 8d9s5c4h 7sJdKcAs 9h7h2dTc Qh8cTsJc") == "9h7h2dTc 7cThKs5s 7sJdKcAs 8d9s5c4h 5hJh2s7d Qh8cTsJc 8s2h6s8h"


def test_oh_3d3s4d6hJc(solver):
    assert solver.process("omaha-holdem 3d3s4d6hJc Js2dKd8c KsAsTcTs Jh2h3c9c Qc8dAd6c 7dQsAc5d") == "Qc8dAd6c KsAsTcTs Js2dKd8c 7dQsAc5d Jh2h3c9c"


def test_oh_2h4s8d8hKh(solver):
    assert solver.process("omaha-holdem 2h4s8d8hKh 3hTsJcJh QhKs9h9d ThAc6c4c Ad7h6dQc 5h8c6s5s 2d5d3s2c 4h3c8s9c") == "Ad7h6dQc ThAc6c4c 5h8c6s5s 3hTsJcJh QhKs9h9d 2d5d3s2c 4h3c8s9c"


def test_oh_3d4h4s5c5s(solver):
    assert solver.process("omaha-holdem 3d4h4s5c5s 6h9c8h6d Jh3sKc9h Tc6sAs5d 8cQc7s7h Ts5h4c3c") == "Jh3sKc9h 6h9c8h6d 8cQc7s7h Tc6sAs5d Ts5h4c3c"


def test_oh_4c4s8c9cQd(solver):
    assert solver.process("omaha-holdem 4c4s8c9cQd Jd8dJsQh 2s6d9hTh AdKsTs8s Kd3d6c7h 5sQsQcTc 2c5c3h4h 7c7sAs8h 3s2dAcKc") == "Kd3d6c7h 7c7sAs8h=AdKsTs8s 2s6d9hTh Jd8dJsQh 2c5c3h4h 3s2dAcKc 5sQsQcTc"


def test_oh_2h3s4sAsQh(solver):
    assert solver.process("omaha-holdem 2h3s4sAsQh 5d9d3d9s Ac5hJhJc Kd6hJs7d 7cKs7h7s 5c6d4cKh Ts8d4d2s 2dJd4h5s") == "Kd6hJs7d 2dJd4h5s=5d9d3d9s=Ac5hJhJc 5c6d4cKh Ts8d4d2s 7cKs7h7s"


def test_oh_3sJsKdQhTc(solver):
    assert solver.process("omaha-holdem 3sJsKdQhTc 4s3c7d8d Jc4c6cTh Jh9h7c3h Qd7hAsKs") == "4s3c7d8d Jc4c6cTh Jh9h7c3h Qd7hAsKs"


def test_oh_4s6h8sKsQc(solver):
    assert solver.process("omaha-holdem 4s6h8sKsQc 5s7h8d5c 7s3h9dTc 7d2d2hAc QsTd8c8h 2cAd2s3s 4cQd4hKdc") == "7s3h9dTc 7d2d2hAc 4cQd4hKd QsTd8c8h 5s7h8d5c 2cAd2s3s"


def test_oh_2s6h8c8sTs(solver):
    assert solver.process("omaha-holdem 2s6h8c8sTs 9d5cJc3d KdAs9s5h 4c3c8hJs 6cQcQd6s 4h2c6dKs Td7dAdJd 7s4d9hKc") == "9d5cJc3d 4h2c6dKs Td7dAdJd 4c3c8hJs 7s4d9hKc KdAs9s5h 6cQcQd6s"