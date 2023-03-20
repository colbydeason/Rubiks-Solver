'''
Created on Mar 19, 2023

@author: Colby
'''
import unittest
import rubik.model.cube as cube
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.middleLayer import solveMiddleLayer

class Test(unittest.TestCase):
    # Analysis of solveMiddleLayer:
    #     Solves the middle layer of the cube
    #
    #     input:
    #         theCube: Cube object with bottom layer solved
    # 
    #     output:
    #         nominal:
    #             theCube.popCurrentRotationStringResetOrientation(): string of rotations
    #             to get to a solved middle layer
    #     abnormal:
    #         none
    #     side-effects: 
    #         Cube object is rotated and middle layer is solved
    #
    #     happy path:
    #     DEVELOPER TEST
    #     test 001: edgeOut Nominal
    #     test 002: edgeOut Nominal
    #     test 003: edgeOut Solved
    #     FULL TEST
    #     test 004: bottom layer nominal
    #     test 005: bottom layer nominal
    #     test 006: bottom layer nominal
    #     test 007: bottom layer nominal
    #     test 008: bottom layer solved
    
    def test_middleLayerTest_solveMiddleLayer_001_EdgeOutNominal(self):
        testCube = cube.Cube('542305011404012521220121233453532541343344011400355205')
        edgeList = [[1, 43], [10, 41], [19, 37], [28, 39]]
        topColor = testCube.get()[40]
        solveBottomCross(testCube)
        solveBottomLayer(testCube)
        solveMiddleLayer(testCube)
        for edge in edgeList:
            edgeColors = []
            for color in edge:
                edgeColors.append(testCube.get()[color])
            if topColor not in edgeColors:
                continue
            else:
                self.fail('Edges not correct for edgeOut')
        pass
    
    def test_middleLayerTest_solveMiddleLayer_002_EdgeOutNominal(self):
        testCube = cube.Cube('552002044332412251125522055303331014215440034331450114')
        edgeList = [[1, 43], [10, 41], [19, 37], [28, 39]]
        topColor = testCube.get()[40]
        solveBottomCross(testCube)
        solveBottomLayer(testCube)
        solveMiddleLayer(testCube)
        for edge in edgeList:
            edgeColors = []
            for color in edge:
                edgeColors.append(testCube.get()[color])
            if topColor not in edgeColors:
                continue
            else:
                self.fail('Edges not correct for edgeOut')
        pass
    
    
    def test_middleLayerTest_solveMiddleLayer_003_EdgeOutNominal(self):
        testCube = cube.Cube('000000000111111111222222222333333333444444444555555555')
        edgeList = [[1, 43], [10, 41], [19, 37], [28, 39]]
        topColor = testCube.get()[40]
        solveBottomCross(testCube)
        solveBottomLayer(testCube)
        solveMiddleLayer(testCube)
        for edge in edgeList:
            edgeColors = []
            for color in edge:
                edgeColors.append(testCube.get()[color])
            if topColor not in edgeColors:
                continue
            else:
                self.fail('Edges not correct for edgeOut')
        pass