import pytest

from solver.main import Solver

_solver = Solver()


@pytest.fixture
def solver():
    return _solver


def test_5cd_4s5hTsQh9h(solver):
    assert solver.process("five-card-draw 4s5hTsQh9h Qc8d7cTcJd 5s5d7s4dQd 3cKs4cKdJs 2hAhKh4hKc 7h6h7d2cJc As6d5cQsAc") == "4s5hTsQh9h Qc8d7cTcJd 5s5d7s4dQd 7h6h7d2cJc 3cKs4cKdJs 2hAhKh4hKc As6d5cQsAc"


def test_5cd_7h4s4h8c9h(solver):
    assert solver.process("five-card-draw 7h4s4h8c9h Tc5h6dAc5c Kd9sAs3cQs Ah9d6s2cKh 4c8h2h6c9c") == "4c8h2h6c9c Ah9d6s2cKh Kd9sAs3cQs 7h4s4h8c9h Tc5h6dAc5c"


def test_5cd_5s3s4c2h9d(solver):
    assert solver.process("five-card-draw 5s3s4c2h9d 8dKsTc6c2c 4h6s8hJd5d 5c3cQdTd9s AhQhKcQc2d KhJs9c5h9h 8c3d7h7dTs") == "5s3s4c2h9d 4h6s8hJd5d 5c3cQdTd9s 8dKsTc6c2c 8c3d7h7dTs KhJs9c5h9h AhQhKcQc2d"


def test_5cd_3d4s5dJsQd(solver):
    assert solver.process("five-card-draw 3d4s5dJsQd 5c4h7sJdKc As9h7h2dTc Qh8cTsJc3c") == "3d4s5dJsQd Qh8cTsJc3c 5c4h7sJdKc As9h7h2dTc"


def test_5cd_3s7sAhQhTd(solver):
    assert solver.process("five-card-draw 3s7sAhQhTd 8h4s9c4hKd 9s3hTs9h6c TcKh6sKs8c") == "3s7sAhQhTd 8h4s9c4hKd 9s3hTs9h6c TcKh6sKs8c"


def test_5cd_5d5h6d7dAh(solver):
    assert solver.process("five-card-draw 5d5h6d7dAh 3sKcKhTdKd 7cAc8s4d3c AdQc7sTs5s 2s7h9hQdTc 6c9s4hJhJc") == "2s7h9hQdTc 7cAc8s4d3c AdQc7sTs5s 5d5h6d7dAh 6c9s4hJhJc 3sKcKhTdKd"


def test_5cd_5s6sJsKsQs(solver):
    assert solver.process("five-card-draw 5s6sJsKsQs 4d8h6c9h5c JhQc9s7s7d 2sJdJc8s7c") == "4d8h6c9h5c JhQc9s7s7d 2sJdJc8s7c 5s6sJsKsQs"


def test_5cd_4c4s7c7s8c(solver):
    assert solver.process("five-card-draw 4c4s7c7s8c 3h2hJh9h6c QsJc2s3dAd 4h2c8dKd2d") == "3h2hJh9h6c QsJc2s3dAd 4h2c8dKd2d 4c4s7c7s8c"


def test_5cd_4c7c8cAcJc(solver):
    assert solver.process("five-card-draw 4c7c8cAcJc 3cJs6d4h4s 5hKdKc8h3d Jd9h5s9d8d") == "3cJs6d4h4s Jd9h5s9d8d 5hKdKc8h3d 4c7c8cAcJc"


def test_5cd_4d5c7hJcQh(solver):
    assert solver.process("five-card-draw 4d5c7hJcQh 4hQc8hQdTc 3d9c7sAs8d KhKc2s6cKd") == "4d5c7hJcQh 3d9c7sAs8d 4hQc8hQdTc KhKc2s6cKd"