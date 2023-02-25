'''
Created on Feb 24, 2023

@author: Colby
'''
import unittest
import rubik.model.cube as cube
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.bottomCross import solveBottomCross

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
    
    # def test_bottomLayerTest_solveBottomCross_001_CornerOut(self):
    #     testCube = cube.Cube('542305011404012521220121233453532541343344011400355205')
    #     solveBottomCross(testCube)
    #     solveBottomLayer(testCube)
    #     cornersCheckList = [[0, 42, 29], [2, 44, 9], [11, 18, 38], [36, 20, 27]]
    #     bottomColor = testCube.get()[49]
    #     for group in cornersCheckList:
    #         colorArray = []
    #         for color in group:
    #             colorArray.append(testCube.get()[color])
    #         if colorArray.count(bottomColor) == 1:
    #             continue
    #         else:
    #             print(testCube.get())
    #             self.fail("Corners are not on the top layer")
                
            
    def test_bottomLayerTest_solveBottomCross_002_BottomLayer(self):
        testCube = cube.Cube('302102343140113413101223014022535252554440435530250145')
        quadMatchList = [[4, 6, 7, 8], [13, 15, 16, 17], [22, 24, 25, 26], [31, 33, 34, 35]]
        bottomRangeList = {45, 46, 47, 48, 49, 50, 51, 52, 53}
        solveBottomCross(testCube)
        solveBottomLayer(testCube)
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
            pass
        else:
            self.fail("Bottom face is not solid")
    
    # def test_bottomLayerTest_solveBottomCross_003_BottomLayer(self):
    #     testCube = cube.Cube('120504224505110033223524531544331023051041241413350452')
    #     quadMatchList = [[4, 6, 7, 8], [13, 15, 16, 17], [22, 24, 25, 26], [31, 33, 34, 35]]
    #     bottomRangeList = {45, 46, 47, 48, 49, 50, 51, 52, 53}
    #     solveBottomCross(testCube)
    #     solveBottomLayer(testCube)
    #     for group in quadMatchList:
    #         colorArray = []
    #         for color in group:
    #             colorArray.append(testCube.get()[color])
    #         if colorArray.count(colorArray[0]) == len(colorArray):
    #             continue
    #         else:
    #             self.fail("Sides do not match color")
    #     colorArray = []
    #     for square in bottomRangeList:
    #         colorArray.append(testCube.get()[square])
    #     if colorArray.count(colorArray[0]) == len(colorArray):
    #         pass
    #     else:
    #         self.fail("Bottom face is not solid")
    #
    # def test_bottomLayerTest_solveBottomCross_004_BottomLayer(self):
    #     testCube = cube.Cube('402001044321211241030520252351433314555043014331452525')
    #     quadMatchList = [[4, 6, 7, 8], [13, 15, 16, 17], [22, 24, 25, 26], [31, 33, 34, 35]]
    #     bottomRangeList = {45, 46, 47, 48, 49, 50, 51, 52, 53}
    #     solveBottomCross(testCube)
    #     solveBottomLayer(testCube)
    #     for group in quadMatchList:
    #         colorArray = []
    #         for color in group:
    #             colorArray.append(testCube.get()[color])
    #         if colorArray.count(colorArray[0]) == len(colorArray):
    #             continue
    #         else:
    #             self.fail("Sides do not match color")
    #     colorArray = []
    #     for square in bottomRangeList:
    #         colorArray.append(testCube.get()[square])
    #     if colorArray.count(colorArray[0]) == len(colorArray):
    #         pass
    #     else:
    #         self.fail("Bottom face is not solid")
    #
    # def test_bottomLayerTest_solveBottomCross_005_BottomLayer(self):
    #     testCube = cube.Cube('135004211034115530241120340212435455433240553300252124')
    #     quadMatchList = [[4, 6, 7, 8], [13, 15, 16, 17], [22, 24, 25, 26], [31, 33, 34, 35]]
    #     bottomRangeList = {45, 46, 47, 48, 49, 50, 51, 52, 53}
    #     solveBottomCross(testCube)
    #     solveBottomLayer(testCube)
    #     for group in quadMatchList:
    #         colorArray = []
    #         for color in group:
    #             colorArray.append(testCube.get()[color])
    #         if colorArray.count(colorArray[0]) == len(colorArray):
    #             continue
    #         else:
    #             self.fail("Sides do not match color")
    #     colorArray = []
    #     for square in bottomRangeList:
    #         colorArray.append(testCube.get()[square])
    #     if colorArray.count(colorArray[0]) == len(colorArray):
    #         pass
    #     else:
    #         self.fail("Bottom face is not solid")
    #
    # def test_bottomLayerTest_solveBottomCross_006_BottomLayer(self):
    #     testCube = cube.Cube('000000000111111111222222222333333333444444444555555555')
    #     quadMatchList = [[4, 6, 7, 8], [13, 15, 16, 17], [22, 24, 25, 26], [31, 33, 34, 35]]
    #     bottomRangeList = {45, 46, 47, 48, 49, 50, 51, 52, 53}
    #     solveBottomCross(testCube)
    #     solveBottomLayer(testCube)
    #     for group in quadMatchList:
    #         colorArray = []
    #         for color in group:
    #             colorArray.append(testCube.get()[color])
    #         if colorArray.count(colorArray[0]) == len(colorArray):
    #             continue
    #         else:
    #             self.fail("Sides do not match color")
    #     colorArray = []
    #     for square in bottomRangeList:
    #         colorArray.append(testCube.get()[square])
    #     if colorArray.count(colorArray[0]) == len(colorArray):
    #         pass
    #     else:
    #         self.fail("Bottom face is not solid")
    
    