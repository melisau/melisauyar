import sys
sys.path.append(".")
import pytest
from src.melisauyar import statistics

def test_mean():
    assert statistics.mean([1,2,3,4,5]) == 3