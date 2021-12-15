import pytest
from src.Ex3 import par_impar

def test_par_impar():
    vetor_par,vetor_impar=par_impar([1,2,3,4,5,6])
    assert vetor_par==[2,4,6]
    assert vetor_impar==[1,3,5]