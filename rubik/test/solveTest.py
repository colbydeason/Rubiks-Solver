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
#         # Lots of random cubes to insure success
#         test 010
#         test 011
#         test 012
#         test 013
#         test 014
#         test 015
#         test 016
#         test 017
#         test 018
#         test 019
#         test 020
#
#     sad path:
#         test 901: invalid cube missing
#         # Unsolvable cubes
#         test 902: corner twist
#         test 903: edge flip
#         test 904: corner and edge flip
#         test 905: multiple of each
#         test 906: sticker swap
#         test 907: sticker swap
#         test 908: sticker swap
#         test 909: sticker swap
#         test 910: twist flip swap

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
                self.fail()
        for pair in pairEdgeList:
            if testCube[pair[0]] == testCube[pair[1]]:
                continue
            else:
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
        
    def test_solveTest_solve_010_NominalSolve(self):
        parmsSolve = {}
        parmsSolve['cube'] = '125205044342112135301420342255333524414041012330555100'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = '125205044342112135301420342255333524414041012330555100'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube)
    
    def test_solveTest_solve_011_NominalSolve(self):
        parmsSolve = {}
        parmsSolve['cube'] = '041304210230015322110322343545132251104140324554055435'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = '041304210230015322110322343545132251104140324554055435'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube)
    
    def test_solveTest_solve_012_NominalSolve(self):
        parmsSolve = {}
        parmsSolve['cube'] = '535203352151411105414024133223031412350440050524453022'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = '535203352151411105414024133223031412350440050524453022'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube)
     
    def test_solveTest_solve_013_NominalSolve(self):
        parmsSolve = {}
        parmsSolve['cube'] = '305200234012314150453121123254034231531142043520450455'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = '305200234012314150453121123254034231531142043520450455'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube)
     
    def test_solveTest_solve_014_NominalSolve(self):
        parmsSolve = {}
        parmsSolve['cube'] = '033003002515414321224122454041131344151045500355253232'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = '033003002515414321224122454041131344151045500355253232'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube)
     
    def test_solveTest_solve_015_NominalSolve(self):
        parmsSolve = {}
        parmsSolve['cube'] = '214404023231013021044521251353533411025040503435451225'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = '214404023231013021044521251353533411025040503435451225'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube)
     
    def test_solveTest_solve_016_NominalSolve(self):
        parmsSolve = {}
        parmsSolve['cube'] = '520104422545015512330225454433130220302543031111454103'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = '520104422545015512330225454433130220302543031111454103'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube)
     
    def test_solveTest_solve_017_NominalSolve(self):
        parmsSolve = {}
        parmsSolve['cube'] = '344201201351513402443423320400535121210440520512353515'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = '344201201351513402443423320400535121210440520512353515'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube)
     
    def test_solveTest_solve_018_NominalSolve(self):
        parmsSolve = {}
        parmsSolve['cube'] = '414104105140315130312225103500130234345342322042255455'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = '414104105140315130312225103500130234345342322042255455'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube)
     
    def test_solveTest_solve_019_NominalSolve(self):
        parmsSolve = {}
        parmsSolve['cube'] = '310002351440314451103124501450035232234342523512452510'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = '310002351440314451103124501450035232234342523512452510'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube)
     
    def test_solveTest_solve_020_NominalSolve(self):
        parmsSolve = {}
        parmsSolve['cube'] = '531405012434110435131521244550230003222245100543154323'
        solveDic = solve(parmsSolve)
        parmsRotate = {}
        parmsRotate['cube'] = '531405012434110435131521244550230003222245100543154323'
        parmsRotate['dir'] = solveDic['solution']
        rotateDic = rotate(parmsRotate)
        testCube = rotateDic['cube']
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube)
               
    def test_solveTest_solve_901_MissingCube(self):
        parmsTest = {}
        parmsTest['cube'] = None
        solveDic = solve(parmsTest)
        self.assertEqual('error: missing cube [string]', solveDic['status'])
        
    def test_solveTest_solve_902_CornerTwistUnsolvable(self):
        parmsSolve = {}
        parmsSolve['cube'] = '453504314432314050103121425252233005545142122003350141'
        solveDic = solve(parmsSolve)
        self.assertEqual('error: unsolvable cube', solveDic['status'])
        
    def test_solveTest_solve_903_EdgeFlipUnsolvable(self):
        parmsSolve = {}
        parmsSolve['cube'] = '544002310135411134035520124242135340103142332425055250'
        solveDic = solve(parmsSolve)
        self.assertEqual('error: unsolvable cube', solveDic['status'])
        
    def test_solveTest_solve_904_FlipAndTwistUnsolvable(self):
        parmsSolve = {}
        parmsSolve['cube'] = '531405012432110435431521224550230003221245100543154343'
        solveDic = solve(parmsSolve)
        self.assertEqual('error: unsolvable cube', solveDic['status'])
        
    def test_solveTest_solve_905_FlipTwistMultipleUnsolvable(self):
        parmsSolve = {}
        parmsSolve['cube'] = '131405012434110435131521244550230003222245500543154323'
        solveDic = solve(parmsSolve)
        self.assertEqual('error: unsolvable cube', solveDic['status'])
        
    def test_solveTest_solve_906_StickerSwapsUnsolvable(self):
        parmsSolve = {}
        parmsSolve['cube'] = '352504454142313112551024024010232242543040515330150133'
        solveDic = solve(parmsSolve)
        self.assertEqual('error: unsolvable cube', solveDic['status'])
        
    def test_solveTest_solve_907_StickerSwapsUnsolvable(self):
        parmsSolve = {}
        parmsSolve['cube'] = '030500235125412153122523435405530213113144004422451340'
        solveDic = solve(parmsSolve)      
        self.assertEqual('error: unsolvable cube', solveDic['status'])
        
    def test_solveTest_solve_908_StickerSwapsUnsolvable(self):
        parmsSolve = {}
        parmsSolve['cube'] = '324400120145013424310521302415030520343543252511354152'
        solveDic = solve(parmsSolve)  
        self.assertEqual('error: unsolvable cube', solveDic['status'])
        
    def test_solveTest_solve_909_StickerSwapsUnsolvable(self):
        parmsSolve = {}
        parmsSolve['cube'] = '000010000111101111222222222333333333444444444555555555'
        solveDic = solve(parmsSolve)
        self.assertEqual('error: unsolvable cube', solveDic['status'])
        
    def test_solveTest_solve_910_TwistFlipSwapUnsolvable(self):
        parmsSolve = {}
        parmsSolve['cube'] = '041000000011111112222222522333333333444444404551555555'
        solveDic = solve(parmsSolve)      
        self.assertEqual('error: unsolvable cube', solveDic['status'])
        
    def test_solveTest_solve_911_UnsolvableRandomGenerate(self):
        parmsSolve = {}
        parmsSolve['cube'] = '242405100533112421551422510534330312230044313451055420'
        solveDic = solve(parmsSolve)      
        self.assertEqual('error: unsolvable cube', solveDic['status'])
        
        
        
