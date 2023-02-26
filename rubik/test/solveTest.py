from unittest import TestCase
from rubik.view.solve import solve
from rubik.view.rotate import rotate
 

class SolveTest(TestCase):
        
# Analysis of solve:
#     Solves the cube and returns the directions to solve
#
#     input:
#         parms: 
#             'cube': String [0-53] validated through cube, unchecked 
#             
#     output: 
#         nominal:
#             result: string showing the combination of directions to solve the rubik cube
#         abnormal: 
#             'error: ' that is the same as the ones in rotate, brought up by cube instantiation
#         
#     happy path:
#         test 000: continuous check test -> does string output equal consequence of cube state
#         test 001: solve bottom cross
#         test 002-003: solve bottom layer
#         test 004-005: solve middle layer
#         test 006-007: solve up face cross
#         test 009-009: solve up face surface
#         test 010-011: solve upper layer / full cube
#
#     sad path:
#         test 901: invalid cube (implementation only, boundary tests done by cubeTest for invalid cube)
#
    def test_solveTest_solve_001_BottomCross(self):
        parmsSolve = {}
        parmsRotate= {}
        parmsSolve['cube'] = '453302001421512031240422212500134313114343302544055555'
        parmsRotate['cube'] = '453302001421512031240422212500134313114343302544055555'
        solveDic = solve(parmsSolve)
        solveString = solveDic['solution']
        parmsRotate['dir'] = solveString
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        print(testCube + ',')
        
        bottomColor = testCube[49]
        edgeList = {46, 48, 50, 52}
        pairEdgeList = [[4, 7], [13, 16], [22, 25], [31, 34]]
        for edge in edgeList:
            if testCube[edge] == bottomColor:
                continue
            else:
                print(testCube)
                self.fail()
        for pair in pairEdgeList:
            if testCube[pair[0]] == testCube[pair[1]]:
                continue
            else:
                print(testCube)
                self.fail()
            
    def test_solveTest_solve_002_BottomLayer(self):
        parmsSolve = {}
        parmsRotate= {}
        parmsSolve['cube'] = '453302001421512031240422212500134313114343302544055555'
        parmsRotate['cube'] = '453302001421512031240422212500134313114343302544055555'
        solveDic = solve(parmsSolve)
        solveString = solveDic['solution']
        parmsRotate['dir'] = solveString
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        print(testCube + ',')
        
        quadMatchList = [[4, 6, 7, 8], [13, 15, 16, 17], [22, 24, 25, 26], [31, 33, 34, 35]]
        bottomRangeList = {45, 46, 47, 48, 49, 50, 51, 52, 53}
        for group in quadMatchList:
            colorArray = []
            for color in group:
                colorArray.append(testCube[color])
            if colorArray.count(colorArray[0]) == len(colorArray):
                continue
            else:
                self.fail("Sides do not match color")
        colorArray = []
        for square in bottomRangeList:
            colorArray.append(testCube[square])
        if colorArray.count(colorArray[0]) == len(colorArray):
            pass
        else:
            self.fail("Bottom face is not solid")
            
    def test_solveTest_solve_003_BottomLayer(self):
        parmsSolve = {}
        parmsRotate= {}
        parmsSolve['cube'] = '113504143452313041513523442035030504423242052025151102'
        parmsRotate['cube'] = '113504143452313041513523442035030504423242052025151102'
        solveDic = solve(parmsSolve)
        solveString = solveDic['solution']
        parmsRotate['dir'] = solveString
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        print(testCube + ',')
        
        quadMatchList = [[4, 6, 7, 8], [13, 15, 16, 17], [22, 24, 25, 26], [31, 33, 34, 35]]
        bottomRangeList = {45, 46, 47, 48, 49, 50, 51, 52, 53}
        for group in quadMatchList:
            colorArray = []
            for color in group:
                colorArray.append(testCube[color])
            if colorArray.count(colorArray[0]) == len(colorArray):
                continue
            else:
                self.fail("Sides do not match color")
        colorArray = []
        for square in bottomRangeList:
            colorArray.append(testCube[square])
        if colorArray.count(colorArray[0]) == len(colorArray):
            pass
        else:
            self.fail("Bottom face is not solid")
                
    def test_solveTest_solve_901_MissingCube(self):
        parmsTest = {}
        parmsTest['cube'] = None
        solveDic = solve(parmsTest)
        self.assertEqual('error: missing cube [string]', solveDic['status'])
        
        
        
