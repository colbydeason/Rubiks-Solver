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
    #     test 001: edgeOut
    #     FULL TEST
    #     test 002: bottom layer nominal
    #     test 003: bottom layer nominal
    #     test 004: bottom layer nominal
    #     test 005: bottom layer nominal
    #     test 006: bottom layer solved
    
    def test_middleLayerTest_solveMiddleLayer_001_EdgeOut(self):
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
            if topColor in edgeColors:
                continue
            else:
                self.fail('Edges not correct for edgeOut')
        pass