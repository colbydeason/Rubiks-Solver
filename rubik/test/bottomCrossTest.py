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
    #         DEVELOPER TEST
    #         test 001: Flower stage
    #         FULL TEST
    #         test 002: bottom cross
    #         test 003: bottom cross
    #         test 004: bottom cross
    #         test 005: bottom cross
    
    # def test_bottomCrossTest_solveBottomCross_001_TopFlower(self):
    #     testCube = cube.Cube('114205020241014115213322235500133144004342453355054253')
    #     bottomColor = testCube.get()[49]
    #     edgeList = {37, 39, 41, 43}
    #     solveBottomCross(testCube)
    #     for edge in edgeList:
    #         if testCube.get()[edge] == bottomColor:
    #             continue
    #         else:
    #             print(testCube.get())
    #             self.fail()
    #     print(testCube.get())
    #     pass
    
    def test_bottomCrossTest_solveBottomCross_002_BottomLayer(self):
        testCube = cube.Cube('114205020241014115213322235500133144004342453355054253')
        bottomColor = testCube.get()[49]
        edgeList = {46, 48, 50, 52}
        pairEdgeList = [[4, 7], [13, 16], [22, 25], [31, 34]]
        solveBottomCross(testCube)
        for edge in edgeList:
            if testCube.get()[edge] == bottomColor:
                continue
            else:
                print(testCube.get())
                self.fail()
        for pair in pairEdgeList:
            if testCube.get()[pair[0]] == testCube.get()[pair[1]]:
                continue
            else:
                print(testCube.get())
                self.fail()
        print(testCube.get())
        pass
    def test_bottomCrossTest_solveBottomCross_003_BottomLayer(self):
        testCube = cube.Cube('h00xxxNhDXXxDXXhN0DhDx0XhD0xNxDhhX0XX0h0DNNDNxN0XNxDhN')
        bottomColor = testCube.get()[49]
        edgeList = {46, 48, 50, 52}
        pairEdgeList = [[4, 7], [13, 16], [22, 25], [31, 34]]
        solveBottomCross(testCube)
        for edge in edgeList:
            if testCube.get()[edge] == bottomColor:
                continue
            else:
                print(testCube.get())
                self.fail()
        for pair in pairEdgeList:
            if testCube.get()[pair[0]] == testCube.get()[pair[1]]:
                continue
            else:
                print(testCube.get())
                self.fail()
        print(testCube.get())
        pass
    def test_bottomCrossTest_solveBottomCross_004_BottomLayer(self):
        testCube = cube.Cube('CgZC11COZOO1ZOvOOOZgZOCvvZvCgv1gvggvgvgCZ1OZCgZ11vC1C1')
        bottomColor = testCube.get()[49]
        edgeList = {46, 48, 50, 52}
        pairEdgeList = [[4, 7], [13, 16], [22, 25], [31, 34]]
        solveBottomCross(testCube)
        for edge in edgeList:
            if testCube.get()[edge] == bottomColor:
                continue
            else:
                print(testCube.get())
                self.fail()
        for pair in pairEdgeList:
            if testCube.get()[pair[0]] == testCube.get()[pair[1]]:
                continue
            else:
                print(testCube.get())
                self.fail()
        print(testCube.get())
        pass
    def test_bottomCrossTest_solveBottomCross_005_BottomLayer(self):
        testCube = cube.Cube('5Vddx5xVd4d405405VVx0V0x54dV4VV404054dxxd5x0xd554Vx0d0')
        bottomColor = testCube.get()[49]
        edgeList = {46, 48, 50, 52}
        pairEdgeList = [[4, 7], [13, 16], [22, 25], [31, 34]]
        solveBottomCross(testCube)
        for edge in edgeList:
            if testCube.get()[edge] == bottomColor:
                continue
            else:
                print(testCube.get())
                self.fail()
        for pair in pairEdgeList:
            if testCube.get()[pair[0]] == testCube.get()[pair[1]]:
                continue
            else:
                print(testCube.get())
                self.fail()
        print(testCube.get())
        pass
    def test_bottomCrossTest_solveBottomCross_006_BottomLayer(self):
        testCube = cube.Cube('YnFnnY45F5YB4YnnB455545FB45FBnBBY4nYYY44FFFFBnFBB45Y5n')
        bottomColor = testCube.get()[49]
        edgeList = {46, 48, 50, 52}
        pairEdgeList = [[4, 7], [13, 16], [22, 25], [31, 34]]
        solveBottomCross(testCube)
        for edge in edgeList:
            if testCube.get()[edge] == bottomColor:
                continue
            else:
                print(testCube.get())
                self.fail()
        for pair in pairEdgeList:
            if testCube.get()[pair[0]] == testCube.get()[pair[1]]:
                continue
            else:
                print(testCube.get())
                self.fail()
        print(testCube.get())
        pass
    def test_bottomCrossTest_solveBottomCross_007_BottomLayer(self):
        testCube = cube.Cube('JjJ0jJMLhML0MJj00JMLhMLhMhh0Jh00MJJ0L0LjMMjhjjhjLhjLJL')
        bottomColor = testCube.get()[49]
        edgeList = {46, 48, 50, 52}
        pairEdgeList = [[4, 7], [13, 16], [22, 25], [31, 34]]
        solveBottomCross(testCube)
        for edge in edgeList:
            if testCube.get()[edge] == bottomColor:
                continue
            else:
                print(testCube.get())
                self.fail()
        for pair in pairEdgeList:
            if testCube.get()[pair[0]] == testCube.get()[pair[1]]:
                continue
            else:
                print(testCube.get())
                self.fail()
        print(testCube.get())
        pass
    def test_bottomCrossTest_solveBottomCross_008_BottomLayer(self):
        testCube = cube.Cube('TbZTuubATT6bA666bA6T6AbbbuAuZu6ZuZZTAZAbTTZAb6ZuuATu6Z')
        bottomColor = testCube.get()[49]
        edgeList = {46, 48, 50, 52}
        pairEdgeList = [[4, 7], [13, 16], [22, 25], [31, 34]]
        solveBottomCross(testCube)
        for edge in edgeList:
            if testCube.get()[edge] == bottomColor:
                continue
            else:
                print(testCube.get())
                self.fail()
        for pair in pairEdgeList:
            if testCube.get()[pair[0]] == testCube.get()[pair[1]]:
                continue
            else:
                print(testCube.get())
                self.fail()
        print(testCube.get())
        pass