import pytest
from src.Ex2 import count_consonants

def test_count_consonants():
    assert count_consonants('cachorro') == 5