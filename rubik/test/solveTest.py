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
#         test 001: solve bottom cross
#         test 002: solve bottom layer
#         # Same cube different stages
#         test 003: unsolved
#         test 004: bottom cross done
#         test 005: bottom layer done
#         test 006: middle layer done
#         test 007: upFaceCross done
#         test 008: upFaceSurface done
#         test 009: Solved cube
#
#     sad path:
#         test 901: invalid cube missing
#         test 902: invalid dir
#         test 903: invalid dir multiple
#         # Unsolvable cubes
#         test 904: 
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
    
    def test_solveTest_solve_003_Unsolved(self):
        parmsSolve = {}
        parmsSolve['cube'] = 'ywgrorwowrbowboogyyoogrwbbgggrbgyrwrwbgyyybgwbybowryro'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = 'ywgrorwowrbowboogyyoogrwbbgggrbgyrwrwbgyyybgwbybowryro'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww', testCube)
        
    def test_solveTest_solve_004_BottomCrossSolved(self):
        parmsSolve = {}
        parmsSolve['cube'] = 'wgbrooworyggybggbrworyrbyryybbrgyogbbboyyrrooowwwwwgwg'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = 'wgbrooworyggybggbrworyrbyryybbrgyogbbboyyrrooowwwwwgwg'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww', testCube)
        
    def test_solveTest_solve_005_BottomLayerSolved(self):
        parmsSolve = {}
        parmsSolve['cube'] = 'gbygoyooobbbrbobbbyggyryrrrorrggogggyrobyoyyrwwwwwwwww'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = 'gbygoyooobbbrbobbbyggyryrrrorrggogggyrobyoyyrwwwwwwwww'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww', testCube)
        
    def test_solveTest_solve_006_MiddleLayerSolved(self):
        parmsSolve = {}
        parmsSolve['cube'] = 'oyrooooooyrybbbbbbryorrrrrrbogggggggybgyyyygbwwwwwwwww'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = 'oyrooooooyrybbbbbbryorrrrrrbogggggggybgyyyygbwwwwwwwww'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww', testCube)
        
    def test_solveTest_solve_007_UpFaceCrossSolved(self):
        parmsSolve = {}
        parmsSolve['cube'] = 'broooooooyggbbbbbbybyrrrrrrooyggggggbyryyyrygwwwwwwwww'
        solveDic = solve(parmsSolve)
        print(solveDic)
        parmsRotate = {}
        parmsRotate['cube'] = 'broooooooyggbbbbbbybyrrrrrrooyggggggbyryyyrygwwwwwwwww'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww', testCube)
        
    def test_solveTest_solve_008_UpFaceSurfaceSolved(self):
        parmsSolve = {}
        parmsSolve['cube'] = 'ooooooooobbrbbbbbbggbrrrrrrrrgggggggyyyyyyyyywwwwwwwww'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = 'ooooooooobbrbbbbbbggbrrrrrrrrgggggggyyyyyyyyywwwwwwwww'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww', testCube)
        
    def test_solveTest_solve_009_Solved(self):
        parmsSolve = {}
        parmsSolve['cube'] = 'ooooooooobbbbbbbbbrrrrrrrrrgggggggggyyyyyyyyywwwwwwwww'
        solveDic = solve(parmsSolve)
        self.assertEqual('', solveDic['solution'])
                
    def test_solveTest_solve_901_MissingCube(self):
        parmsTest = {}
        parmsTest['cube'] = None
        solveDic = solve(parmsTest)
        self.assertEqual('error: missing cube [string]', solveDic['status'])
        
        
        
