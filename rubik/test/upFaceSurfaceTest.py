'''
Created on Apr 7, 2023

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

class Test(unittest.TestCase):
    # Analysis of solveUpCrosss:
    #     Solves the upper face on the cube
    #
    #     input:
    #         theCube: Cube object with bottom, middle, and upper cross solved
    #
    #     output:
    #         nominal:
    #             theCube.popCurrentRotationStringResetOrientation(): string of rotations
    #             to get to a solved upper face
    #         abnormal:
    #             none
    #         side-effects:
    #             Cube object is rotated and top face is solved
    #
    #     happy path:
    #         test 001: top face nominal
    #         test 002: top face nominal
    #         test 003: top face nominal
    #         test 004: top face nominal
    #         test 005: top face solved
    
    def setUp(self):
        faceD = [DTL, DTM, DTR, DML, DMM, DMR, DBL, DBM, DBR]
        faceF = [FML, FMM, FMR, FBL, FBM, FBR]
        faceR = [RML, RMM, RMR, RBL, RBM, RBR]
        faceL = [LML, LMM, LMR, LBL, LBM, LBR]
        faceB = [BML, BMM, BMR, BBL, BBM, BBR]
        faceU = [UTL, UTM, UTR, UML, UMM, UMR, UBL, UBM, UBR]
        self.faceArray = [faceD, faceF, faceR, faceL, faceB, faceU]
    
    def test_upFaceSurface_001_solveUpSurfaceNom(self):
        testCube = cube.Cube('302102343140113413101223014022535252554440435530250145')
        for face in self.faceArray:
            if testCube.isSameColor(face):
                continue
            else:
                self.fail("Bottom, middle, and / or top face are not solved")
        pass
                
    def test_upFaceSurface_002_solveUpSurfaceNom(self):
        testCube = cube.Cube('120504224505110033223524531544331023051041241413350452')
        for face in self.faceArray:
            if testCube.isSameColor(face):
                continue
            else:
                self.fail("Bottom, middle, and / or top face are not solved")
        pass  
          
    def test_upFaceSurface_003_solveUpSurfaceNom(self):
        testCube = cube.Cube('402001044321211241030520252351433314555043014331452525')
        for face in self.faceArray:
            if testCube.isSameColor(face):
                continue
            else:
                self.fail("Bottom, middle, and / or top face are not solved")
        pass
    
    def test_upFaceSurface_004_solveUpSurfaceNom(self):
        testCube = cube.Cube('135004211034115530241120340212435455433240553300252124')
        for face in self.faceArray:
            if testCube.isSameColor(face):
                continue
            else:
                self.fail("Bottom, middle, and / or top face are not solved")
        pass  
    
    def test_upFaceSurface_005_solveUpSurfaceSolv(self):
        testCube = cube.Cube('000000000111111111222222222333333333444444444555555555')
        for face in self.faceArray:
            if testCube.isSameColor(face):
                continue
            else:
                self.fail("Bottom, middle, and / or top face are not solved")
        pass     