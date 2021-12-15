from src.Ex4 import get_media_alunos,get_aprovados

def test_get_media_alunos():
    assert get_media_alunos(7.0,7.0)==7.0

def test_get_aprovados():
    assert get_aprovados([7.0,5.5,8.3])==2