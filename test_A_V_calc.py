'''
TPRG 2131 Fall 2023 Assignment 1
Sept/oct, 2023
Nelson Hucklebridge
This file is too test the equations for areas and volumes of various shapes

'''

from A_V_calc import SQUARE_AREA

def test_SQUARE_AREA():#test for area of a square
    assert SQUARE_AREA(2, 3) == 6
    assert SQUARE_AREA(1, 2) == 2
    assert SQUARE_AREA(0, 9) == 0