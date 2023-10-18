'''
TPRG 2131 Fall 2023 Assignment 1
Sept/oct, 2023
Nelson Hucklebridge
This file is too test the equations for areas and volumes of various shapes

'''

from A_V_calc import square_area, cyl_vol, triangle_area, pyramid_volume, rectangle_tank_volume 

def test_square_area():#test for area of a square
    assert square_area(2, 3) == 6
    assert square_area(1, 2) == 2
    assert square_area(0, 9) == 0
    
def test_cyl_vol():#test for Cylinder volume
    assert cyl_vol(2, 6) == 12
    assert cyl_vol(4, 4) == 16
    assert cyl_vol(0, 10) == 0
    
def test_triangle_area():#test for Triangle area
    assert triangle_area(2, 6) == 6
    assert triangle_area(4, 4) == 8
    assert triangle_area(2, 10) == 10

def test_pyramid_volume():#test for pyramid volume
    assert pyramid_volume(3, 6) == 6
    assert pyramid_volume(6, 9) == 18
    assert pyramid_volume(12, 15) == 60

def test_rectangle_tank_volume():#rectangle tank volume
    assert rectangle_tank_volume(8, 6) == 48
    assert rectangle_tank_volume(4, 6) == 24
    assert rectangle_tank_volume(2, 30) == 60


