'''
Created on Apr 6, 2023

@author: Colby
'''
import unittest
import rubik.model.cube as cube
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross

class Test(unittest.TestCase):
    # Analysis of solveUpCrosss:
    #     Solves the upper cross on the cube
    #
    #     input:
    #         theCube: Cube object with bottom and middle layer solved
    #
    #     output:
    #         nominal:
    #             theCube.popCurrentRotationStringResetOrientation(): string of rotations
    #             to get to a solved upper cross
    #         abnormal:
    #             none
    #         side-effects:
    #             Cube object is rotated and top cross is solved
    #
    #     happy path:
    #         test 001: top cross nominal
    #         test 002: top cross nominal
    #         test 003: top cross nominal
    #         test 004: top cross nominal
    #         test 005: top cross solved

    def test_upFaceCross_solveUpCross_001_solveUpCrossNom(self):
        testCube = cube.Cube('302102343140113413101223014022535252554440435530250145')
        matchArray = [[45, 46, 47, 48, 49, 50, 51, 52, 53], [3, 4, 5, 6, 7, 8], [12, 13, 14, 15, 16, 17], [21, 22, 23, 24, 25, 26], [30, 31, 32, 33, 34, 35], [37, 39, 40, 41, 43]]
        solveBottomCross(testCube)
        solveBottomLayer(testCube)
        solveMiddleLayer(testCube)
        solveUpCross(testCube)
        for side in matchArray:
            sideColorArray = []
            for square in side:
                sideColorArray.append(testCube.get()[square])
            if sideColorArray.count(sideColorArray[0]) == len(sideColorArray):
                continue
            else:
                self.fail("Bottom, middle, and / or top layer cross not solved")
        pass
    
    def test_upFaceCross_solveUpCross_002_solveUpCrossNom(self):
        testCube = cube.Cube('120504224505110033223524531544331023051041241413350452')
        matchArray = [[45, 46, 47, 48, 49, 50, 51, 52, 53], [3, 4, 5, 6, 7, 8], [12, 13, 14, 15, 16, 17], [21, 22, 23, 24, 25, 26], [30, 31, 32, 33, 34, 35], [37, 39, 40, 41, 43]]
        solveBottomCross(testCube)
        solveBottomLayer(testCube)
        solveMiddleLayer(testCube)
        solveUpCross(testCube)
        for side in matchArray:
            sideColorArray = []
            for square in side:
                sideColorArray.append(testCube.get()[square])
            if sideColorArray.count(sideColorArray[0]) == len(sideColorArray):
                continue
            else:
                self.fail("Bottom, middle, and / or top layer cross not solved")
        pass
    
    def test_upFaceCross_solveUpCross_003_solveUpCrossNom(self):
        testCube = cube.Cube('402001044321211241030520252351433314555043014331452525')
        matchArray = [[45, 46, 47, 48, 49, 50, 51, 52, 53], [3, 4, 5, 6, 7, 8], [12, 13, 14, 15, 16, 17], [21, 22, 23, 24, 25, 26], [30, 31, 32, 33, 34, 35], [37, 39, 40, 41, 43]]
        solveBottomCross(testCube)
        solveBottomLayer(testCube)
        solveMiddleLayer(testCube)
        solveUpCross(testCube)
        for side in matchArray:
            sideColorArray = []
            for square in side:
                sideColorArray.append(testCube.get()[square])
            if sideColorArray.count(sideColorArray[0]) == len(sideColorArray):
                continue
            else:
                self.fail("Bottom, middle, and / or top layer cross not solved")
        pass
    
    def test_upFaceCross_solveUpCross_004_solveUpCrossNom(self):
        testCube = cube.Cube('135004211034115530241120340212435455433240553300252124')
        matchArray = [[45, 46, 47, 48, 49, 50, 51, 52, 53], [3, 4, 5, 6, 7, 8], [12, 13, 14, 15, 16, 17], [21, 22, 23, 24, 25, 26], [30, 31, 32, 33, 34, 35], [37, 39, 40, 41, 43]]
        solveBottomCross(testCube)
        solveBottomLayer(testCube)
        solveMiddleLayer(testCube)
        solveUpCross(testCube)
        for side in matchArray:
            sideColorArray = []
            for square in side:
                sideColorArray.append(testCube.get()[square])
            if sideColorArray.count(sideColorArray[0]) == len(sideColorArray):
                continue
            else:
                self.fail("Bottom, middle, and / or top layer cross not solved")
        pass
    
    def test_upFaceCross_solveUpCross_005_solveUpCrossSolv(self):
        testCube = cube.Cube('000000000111111111222222222333333333444444444555555555')
        matchArray = [[45, 46, 47, 48, 49, 50, 51, 52, 53], [3, 4, 5, 6, 7, 8], [12, 13, 14, 15, 16, 17], [21, 22, 23, 24, 25, 26], [30, 31, 32, 33, 34, 35], [37, 39, 40, 41, 43]]
        solveBottomCross(testCube)
        solveBottomLayer(testCube)
        solveMiddleLayer(testCube)
        solveUpCross(testCube)
        for side in matchArray:
            sideColorArray = []
            for square in side:
                sideColorArray.append(testCube.get()[square])
            if sideColorArray.count(sideColorArray[0]) == len(sideColorArray):
                continue
            else:
                self.fail("Bottom, middle, and / or top layer cross not solved")
        pass
    