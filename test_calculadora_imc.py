import pytest
from calcIMC import *

class Test_CalcIMC:

    def test_imc(self):
        user = CalcIMC("Zoe", 21, 1.63, 52, "F")
        assert user.imc() == 19.57

    def test_BSex_F(self):
        user = CalcIMC("Zoe", 21, 1.63, 52, "F")
        assert user.BSex() == "Zoe your BMI is 19.57, in other words, you are of normal weight.\n\tZoe o seu IMC é 19.57, ou seja, você está com peso normal."

    def test_BSex_M(self):
        user = CalcIMC("Bernardo", 25, 1.89, 115, "M")
        assert user.BSex() == "Bernardo your BMI is 32.19, in other words, you are obese I.\n\tBernardo o seu IMC é 32.19, ou seja, você está com obsidade I."

