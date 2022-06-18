import pytest
from calcIMC import *

class Test_CalcIMC:
    #@pytest.fixture
    #def user():
    #    user = CalcIMC("Zoe", 21, 1.63, 52, "F")
    #    return user

    def test_imc(self):
        user = CalcIMC("Zoe", 21, 1.63, 52, "F")
        assert user.imc() == 19.57
