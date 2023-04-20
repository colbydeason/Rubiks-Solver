'''
Created on Apr 19, 2023

@author: Colby
'''
import unittest
import rubik.model.cube as cube
from rubik.model.constants import *
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer

class Test(unittest.TestCase):
    # Analysis of solveUpperLayer:
    #     Solves the upper layer of the cube, finishing cube
    #
    #     input:
    #         theCube: Cube object with bottom, middle, and upper cross solved
    #
    #     output:
    #         nominal:
    #             theCube.popCurrentRotationStringResetOrientation(): string of rotations
    #             to get to a solved upper layer / solved cube
    #         abnormal:
    #             none
    #         side-effects:
    #             Cube object is rotated and the top layer / cube is solved
    #
    #     happy path:
    #         test 101: top layer corners only
    #         test 102: top layer corners only
    #         test 103: top layer corners only
    #         test 001: top layer nominal
    #         test 002: top layer nominal
    #         test 003: top layer nominal
    #         test 004: top layer nominal
    #         test 005: top layer solved        
    #     sad path:
    #         none
    #     evil path: 
    #         none
    
    def setUp(self):
        self.faceArray = [FACED, FACEF, FACER, FACEL, FACEB, FACEU]
        self.faceArrayCorner = [FACED, FACEU, [FTL, FTR, FML, FMM, FMR, FBL, FBM, FBR], 
                                [RTL, RTL, RML, RMM, RMR, RBL, RBM, RBR], [LTL, LTR, LML, LMM, LMR, LBL, LBM, LBR], 
                                [BTL, BTR, BML, BMM, BMR, BBL, BBM, BBR]]
        
    # def test_upperLayer_101_solveCorners(self):
    #     testCube = cube.Cube('302102343140113413101223014022535252554440435530250145')
    #     solveBottomCross(testCube)
    #     solveBottomLayer(testCube)
    #     solveMiddleLayer(testCube)
    #     solveUpCross(testCube)
    #     solveUpSurface(testCube)
    #     solveUpperLayer(testCube)
    #     for face in self.faceArrayCorner:
    #         if testCube.isSameColor(face):
    #             continue
    #         else:
    #             self.fail("Top layer corners are not solved")
        pass
    
    def test_upperLayer_102_solveCorners(self):
        testCube = cube.Cube('120504224505110033223524531544331023051041241413350452')
        solveBottomCross(testCube)
        solveBottomLayer(testCube)
        solveMiddleLayer(testCube)
        solveUpCross(testCube)
        solveUpSurface(testCube)
        solveUpperLayer(testCube)
        for face in self.faceArrayCorner:
            if testCube.isSameColor(face):
                continue
            else:
                self.fail("Top layer corners are not solved")
        pass
    
    # def test_upperLayer_103_solveCorners(self):
    #     testCube = cube.Cube('000000000111111111222222222333333333444444444555555555')
    #     solveBottomCross(testCube)
    #     solveBottomLayer(testCube)
    #     solveMiddleLayer(testCube)
    #     solveUpCross(testCube)
    #     solveUpSurface(testCube)
    #     solveUpperLayer(testCube)
    #     for face in self.faceArrayCorner:
    #         if testCube.isSameColor(face):
    #             continue
    #         else:
    #             self.fail("Top layer corners are not solved")
    #     pass
        
    # def test_upperLayer_001_solveUpperLayerNom(self):
    #     testCube = cube.Cube('302102343140113413101223014022535252554440435530250145')
    #     solveBottomCross(testCube)
    #     solveBottomLayer(testCube)
    #     solveMiddleLayer(testCube)
    #     solveUpCross(testCube)
    #     solveUpSurface(testCube)
    #     solveUpperLayer(testCube)
    #     for face in self.faceArray:
    #         if testCube.isSameColor(face):
    #             continue
    #         else:
    #             self.fail("Top layer is not solved")
    #     pass
    #
    # def test_upperLayer_002_solveUpperLayerNom(self):
    #     testCube = cube.Cube('120504224505110033223524531544331023051041241413350452')
    #     solveBottomCross(testCube)
    #     solveBottomLayer(testCube)
    #     solveMiddleLayer(testCube)
    #     solveUpCross(testCube)
    #     solveUpSurface(testCube)
    #     solveUpperLayer(testCube)
    #     for face in self.faceArray:
    #         if testCube.isSameColor(face):
    #             continue
    #         else:
    #             self.fail("Top layer is not solved")
    #     pass  
    #
    # def test_upperLayer_003_solveUpperLayerNom(self):
    #     testCube = cube.Cube('402001044321211241030520252351433314555043014331452525')
    #     solveBottomCross(testCube)
    #     solveBottomLayer(testCube)
    #     solveMiddleLayer(testCube)
    #     solveUpCross(testCube)
    #     solveUpSurface(testCube)
    #     solveUpperLayer(testCube)
    #     for face in self.faceArray:
    #         if testCube.isSameColor(face):
    #             continue
    #         else:
    #             self.fail("Top layer is not solved")
    #     pass
    #
    # def test_upperLayer_004_solveUpperLayerNom(self):
    #     testCube = cube.Cube('135004211034115530241120340212435455433240553300252124')
    #     solveBottomCross(testCube)
    #     solveBottomLayer(testCube)
    #     solveMiddleLayer(testCube)
    #     solveUpCross(testCube)
    #     solveUpSurface(testCube)
    #     solveUpperLayer(testCube)
    #     for face in self.faceArray:
    #         if testCube.isSameColor(face):
    #             continue
    #         else:
    #             self.fail("Top layer is not solved")
    #     pass  
    #
    # def test_upperLayer_005_solveUpperLayerSolv(self):
    #     testCube = cube.Cube('000000000111111111222222222333333333444444444555555555')
    #     solveBottomCross(testCube)
    #     solveBottomLayer(testCube)
    #     solveMiddleLayer(testCube)
    #     solveUpCross(testCube)
    #     solveUpSurface(testCube)
    #     solveUpperLayer(testCube)
    #     for face in self.faceArray:
    #         if testCube.isSameColor(face):
    #             continue
    #         else:
    #             self.fail("Top layer is not solved")
    #     pass
    
    