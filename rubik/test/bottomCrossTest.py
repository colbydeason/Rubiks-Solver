'''
Created on Feb 15, 2023

@author: Colby
'''
import unittest
import rubik.model.cube as cube
from rubik.controller.bottomCross import solveBottomCross

class Test(unittest.TestCase):

    # Analysis of solveBottomCross:
    #     Solves the bottom cross of the cube, including matching edges
    #
    #     input:
    #         theCube: Cube object
    #
    #     output: 
    #         nominal:
    #             bottomCrossString: string of the rotations that solved the bottom cross
    #         abnormal:
    #             none
    #         side-effects:
    #             Cube object is rotated and the bottom cross is solved
    #       
    #     happy path:
    #         DEVELOPER TESTS
    #         test 001: Flower stage
    #         test 002: bottom cross
    
    def test_bottomCrossTest_solveBottomCross_001_TopFlower(self):
        testCube = cube.Cube('114205020241014115213322235500133144004342453355054253')
        bottomColor = testCube.get()[49]
        edgeList = {37, 39, 41, 43}
        solveBottomCross(testCube)
        for edge in edgeList:
            if testCube.get(edge) == bottomColor:
                continue
            else
                self.fail()
        pass