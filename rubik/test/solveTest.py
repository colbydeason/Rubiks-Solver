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
#         test 002: solve bottom layer
#         test 003: solve middle layer
#         test 004: solve up face cross
#         test 005: solve up face surface
#         test 006: solve upper layer / full cube
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
                
    def test_solveTest_solve_901_MissingCube(self):
        parmsTest = {}
        parmsTest['cube'] = None
        solveDic = solve(parmsTest)
        self.assertEqual('error: missing cube [string]', solveDic['status'])
        
        
        
