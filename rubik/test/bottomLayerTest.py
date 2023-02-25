'''
Created on Feb 24, 2023

@author: Colby
'''
import unittest
import rubik.model.cube as cube
from rubik.controller.bottomLayer import solveBottomLayer

class Test(unittest.TestCase):

    # Analysis of solveBottomLayer:
    #     Solves the bottom Layer of the cube
    #
    #     input:
    #         theCube: Cube object
    #
    #     output: 
    #         nominal:
    #             bottomLayerString: string of the rotations that solved the bottom layer
    #         abnormal:
    #             none
    #         side-effects:
    #             Cube object is rotated and the bottom layer is solved
    #       
    #     happy path:
    #         DEVELOPER TEST
    #         test 001: moveCornerOut
    #         FULL TEST
    #         test 002: bottom layer nominal
    #         test 003: bottom layer nominal
    #         test 004: bottom layer nominal
    #         test 005: bottom layer nominal
    #         test 006: bottom layer solved
    
    def test_bottomLayerTest_solveBottomCross_001_CornerOut(self):
        testCube = cube.Cube('')
        cornersCheckList = [[0, 42, 29], [2, 44, 9], [11, 18, 38], [36, 20, 27]]
        bottomColor = testCube.get()[49]
        for group in cornersCheckList:
            colorArray = []
            for color in group:
                colorArray.append(testCube.get()[color])
            if colorArray.count(bottomColor) == 1:
                continue
            else:
                self.fail("Corners are not on the top layer")
                
            
    def test_bottomLayerTest_solveBottomCross_002_BottomLayer(self):
        testCube = cube.Cube('')
        quadMatchList = [[4, 6, 7, 8], [13, 15, 16, 17], [22, 24, 25, 26], [31, 33, 34, 35]]
        bottomRangeList = {45, 46, 47, 48, 49, 50, 51, 52, 53}
        for group in quadMatchList:
            colorArray = []
            for color in group:
                colorArray.append(testCube.get()[color])
            if colorArray.count(colorArray[0]) == len(colorArray):
                continue
            else:
                self.fail("Sides do not match color")
        colorArray = []
        for square in bottomRangeList:
            colorArray.append(testCube.get()[square])
        if colorArray.count(colorArray[0]) == len(colorArray):
            continue
        else:
            self.fail("Bottom face is not solid")
    
    def test_bottomLayerTest_solveBottomCross_003_BottomLayer(self):
        testCube = cube.Cube('')
        quadMatchList = [[4, 6, 7, 8], [13, 15, 16, 17], [22, 24, 25, 26], [31, 33, 34, 35]]
        bottomRangeList = {45, 46, 47, 48, 49, 50, 51, 52, 53}
        for group in quadMatchList:
            colorArray = []
            for color in group:
                colorArray.append(testCube.get()[color])
            if colorArray.count(colorArray[0]) == len(colorArray):
                continue
            else:
                self.fail("Sides do not match color")
        colorArray = []
        for square in bottomRangeList:
            colorArray.append(testCube.get()[square])
        if colorArray.count(colorArray[0]) == len(colorArray):
            continue
        else:
            self.fail("Bottom face is not solid")
    
    def test_bottomLayerTest_solveBottomCross_004_BottomLayer(self):
        testCube = cube.Cube('')
        quadMatchList = [[4, 6, 7, 8], [13, 15, 16, 17], [22, 24, 25, 26], [31, 33, 34, 35]]
        bottomRangeList = {45, 46, 47, 48, 49, 50, 51, 52, 53}
        for group in quadMatchList:
            colorArray = []
            for color in group:
                colorArray.append(testCube.get()[color])
            if colorArray.count(colorArray[0]) == len(colorArray):
                continue
            else:
                self.fail("Sides do not match color")
        colorArray = []
        for square in bottomRangeList:
            colorArray.append(testCube.get()[square])
        if colorArray.count(colorArray[0]) == len(colorArray):
            continue
        else:
            self.fail("Bottom face is not solid")
    
    def test_bottomLayerTest_solveBottomCross_005_BottomLayer(self):
        testCube = cube.Cube('')
        quadMatchList = [[4, 6, 7, 8], [13, 15, 16, 17], [22, 24, 25, 26], [31, 33, 34, 35]]
        bottomRangeList = {45, 46, 47, 48, 49, 50, 51, 52, 53}
        for group in quadMatchList:
            colorArray = []
            for color in group:
                colorArray.append(testCube.get()[color])
            if colorArray.count(colorArray[0]) == len(colorArray):
                continue
            else:
                self.fail("Sides do not match color")
        colorArray = []
        for square in bottomRangeList:
            colorArray.append(testCube.get()[square])
        if colorArray.count(colorArray[0]) == len(colorArray):
            continue
        else:
            self.fail("Bottom face is not solid")
    
    def test_bottomLayerTest_solveBottomCross_006_BottomLayer(self):
        testCube = cube.Cube('')
        quadMatchList = [[4, 6, 7, 8], [13, 15, 16, 17], [22, 24, 25, 26], [31, 33, 34, 35]]
        bottomRangeList = {45, 46, 47, 48, 49, 50, 51, 52, 53}
        for group in quadMatchList:
            colorArray = []
            for color in group:
                colorArray.append(testCube.get()[color])
            if colorArray.count(colorArray[0]) == len(colorArray):
                continue
            else:
                self.fail("Sides do not match color")
        colorArray = []
        for square in bottomRangeList:
            colorArray.append(testCube.get()[square])
        if colorArray.count(colorArray[0]) == len(colorArray):
            continue
        else:
            self.fail("Bottom face is not solid")
    
    