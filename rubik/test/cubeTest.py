'''
Created on Jan 31, 2023

@author: Colby Deason
'''
import unittest
import rubik.model.cube as cube


class Test(unittest.TestCase):

    # Analysis of cube:
    #     
    #    Cube: class, instance of a state machine, maintain internal state (don't allow changes of state from the outside)
    #    Methods: __init__ => instantiates a cube from a string denoting the colors on the cube
    #             get      => returns string of internal representation of the cube
    #             rotate   => rotates the cube based on the 'dir' key
    
     
    #    Analysis of Cube() -> __init__
    #        input:
    #            cube: string, 54 characters, 6 unique characters [a-zA-Z0-9], 0-53; 4, 13, 22, 31, 40, and 49 must be unique
    #                mandatory, arrived unvalidated
    #        outputs: 
    #            nominal:
    #                Instance of a cube with self._cube equal to the input
    #            abnormal:
    #                Instance of a cube with self._cube equal to the error
    #                    error 1: invalid length
    #                    error 2: incorrect amount of unique characters (6 unique, and 9 of each)
    #                    error 3: centers not unique
    #                future errors not implemented:
    #                    error 4-...: unsolvable cube
    #            side-effects:
    #                none
    #
    #        happy path:
    #            test 001: lower-case cube
    #            test 002: upper-case cube
    #            test 003: number cube
    #            test 004: mixed cube
    #
    #        sad path:
    #            test 901: invalid length for cube [54]
    #            test 902: invalid character for cube [a-zA-Z0-9]
    #            test 903: incorrect number of unique colors [6, 9 of each] (more unique colors)
    #            test 904: centers are not unique           
    #            test 905: incorrect number of unique colors [6, 9 of each] (6 unique but unbalanced)
    #
    #            Future error tests
    #                test 904-...: cube is unsolvable
    #            
    #        evil path:
    #            none

    def test_cubeTest_cube_001_LowerCaseCube(self):
        testCube = cube.Cube('wwwwwwwwwbbbbbbbbbyyyyyyyyygggggggggooooooooorrrrrrrrr')
        self.assertEqual('wwwwwwwwwbbbbbbbbbyyyyyyyyygggggggggooooooooorrrrrrrrr', testCube.get())
    
    def test_cubeTest_cube_002_UpperCaseCube(self):
        testCube = cube.Cube('WWWWWWWWWBBBBBBBBBYYYYYYYYYGGGGGGGGGOOOOOOOOORRRRRRRRR')
        self.assertEqual('WWWWWWWWWBBBBBBBBBYYYYYYYYYGGGGGGGGGOOOOOOOOORRRRRRRRR', testCube.get())
    
    def test_cubeTest_cube_003_NumberCube(self):
        testCube = cube.Cube('000000000111111111222222222333333333444444444555555555')
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube.get())
    
    def test_cubeTest_cube_004_UpperLowerAndNumberCube(self):
        testCube = cube.Cube('lllllllll333333333KKKKKKKKKrrrrrrrrr999999999AAAAAAAAA')
        self.assertEqual('lllllllll333333333KKKKKKKKKrrrrrrrrr999999999AAAAAAAAA', testCube.get())
        
    def test_cubeTest_cube_901_InvalidLength(self):
        testCube = cube.Cube('lllllllll333333333KKKKKKKKKrrrrrrrrr999999999AAAAAAAA')
        self.assertEqual('error: invalid length for cube [54]', testCube.get())
        
    def test_cubeTest_cube_902_InvalidCharacter(self):
        testCube = cube.Cube('lllllllll333333-33KKKKKKKKKrrrrrrrrr999999999AAAAAAAAA')
        self.assertEqual('error: invalid character for cube [a-zA-Z0-9]', testCube.get())
    
    def test_cubeTest_cube_903_UniqueColorError(self):
        testCube = cube.Cube('jjjjjjjjjjjjjjjjjjffffffffffffffffffbbbbbbbbbbbbbbbbbb')
        self.assertEqual('error: incorrect number of unique colors [6, 9 of each]', testCube.get())
        
    def test_cubeTest_cube_904_UniqueCenterError(self):
        testCube = cube.Cube('llllrllll333333333KKKKKKKKKlrrrrrrrr999999999AAAAAAAAA')
        self.assertEqual('error: centers are not unique', testCube.get())
        
    def test_cubeTest_cube_905_IncorrectUniqueColor(self):
        testCube = cube.Cube('lllllllll333333333KKKKKKKKKKrrrrrrrr999999999AAAAAAAAA')
        self.assertEqual('error: incorrect number of unique colors [6, 9 of each]', testCube.get())
        
    def test_cubeTest_cube_906_MissingCube(self):
        testCube = cube.Cube(None)
        self.assertEqual('error: missing cube [string]', testCube.get())
        
    #    Analysis of Cube.rotate
    #        inputs:
    #            directions: string, len >= 0, in[FfRrBbLlUu]; optional, defaults to F if missing; un-validated
    #        outputs:
    #            nominal:
    #                return serialized rotated cube
    #            abnormal:
    #                raise DirException
    #            side-effects: internal state change of cube
    #
    #        happy path:
    #            test 001: F rotation
    #            test 002: f rotation
    #            test 003: B rotation
    #            test 004: b rotation
    #            test 005: L rotation
    #            test 006: l rotation 
    #            test 007: R rotation
    #            test 008: r rotation
    #            test 009: U rotation
    #            test 010: u rotation
    #            test 011: missing direction
    #            test 012: empty direction - ""
    #            test 013: multiple rotations
    #            
    #        sad path:
    #            test 901: invalid direction
    #
    #        evil path:
    #            none
    #        
    #        full solve:
    #            test 555: one algorithm left, should solve, uses most rotations
    
    
    def test_cubeTest_rotate_001_FRotation(self):
        testCube = cube.Cube('gobgwywrwwbgobwowgybygybyrybowygybrororgorrwrgybgrbowo')
        rotatedCube = testCube.rotate('F')
        self.assertEqual(rotatedCube, 'wggrwowybrbgwbwrwgybygybyrybogygybrbrorgoroywoowgrbowo')
    
    def test_cubeTest_rotate_002_fRotation(self):
        testCube = cube.Cube('oworwygogwbbborwyywwwyygrrgoryorgywyggrbgobobryrbbgowb')
        rotatedCube = testCube.rotate('f')
        self.assertEqual(rotatedCube, 'oygwwoorgrbbyorryywwwyygrrgorboroywbggrbgowbwygybbgowb')
    
    def test_cubeTest_rotate_003_BRotation(self):
        testCube = cube.Cube('oworwygogwbbborwyywwwyygrrgoryorgywyggrbgobobryrbbgowb')
        rotatedCube = testCube.rotate('B')
        self.assertEqual(rotatedCube, 'oworwygogwbbbowwyorywrywggwrrygrggwybrybgobobryrbbgooy')
    
    def test_cubeTest_rotate_004_bRotation(self):
        testCube = cube.Cube('oworwygogwbbborwyywwwyygrrgoryorgywyggrbgobobryrbbgowb')
        rotatedCube = testCube.rotate('b')
        self.assertEqual(rotatedCube, 'oworwygogwbgbogwyrwggwyrwyrorywrgbwyyoobgobobryrbbgyrb')
    
    def test_cubeTest_rotate_005_LRotation(self):
        testCube = cube.Cube('oworwygogwbbborwyywwwyygrrgoryorgywyggrbgobobryrbbgowb')
        rotatedCube = testCube.rotate('L')
        self.assertEqual(rotatedCube, 'gwobwybogwbbborwyywwoyybrrryoowrrygyggrggowoboyrrbggwb')
    
    def test_cubeTest_rotate_006_lRotation(self):
        testCube = cube.Cube('oworwygogwbbborwyywwwyygrrgoryorgywyggrbgobobryrbbgowb')
        rotatedCube = testCube.rotate('l')
        self.assertEqual(rotatedCube, 'rwobwyoogwbbborwyywwbyybrrgygyrrwooyogrrgogobgyrgbgwwb')
    
    def test_cubeTest_rotate_007_RRotation(self):
        testCube = cube.Cube('oworwygogwbbborwyywwwyygrrgoryorgywyggrbgobobryrbbgowb')
        rotatedCube = testCube.rotate('R')
        self.assertEqual(rotatedCube, 'owrrwggobwbwyobyrbbwwoygrrgoryorgywyggobgybogryrbbyoww')
    
    def test_cubeTest_rotate_008_rRotation(self):
        testCube = cube.Cube('oworwygogwbbborwyywwwyygrrgoryorgywyggrbgobobryrbbgowb')
        rotatedCube = testCube.rotate('r')
        self.assertEqual(rotatedCube, 'owrrwogobbryboywbwbwwgygrrgoryorgywyggrbgybowryobbyowg')
    
    def test_cubeTest_rotate_009_URotation(self):
        testCube = cube.Cube('oworwygogwbbborwyywwwyygrrgoryorgywyggrbgobobryrbbgowb')
        rotatedCube = testCube.rotate('U')
        self.assertEqual(rotatedCube, 'wbbrwygogwwwborwyyoryyygrrgowoorgywybbgoggborryrbbgowb')
    
    def test_cubeTest_rotate_010_uRotation(self):
        testCube = cube.Cube('oworwygogwbbborwyywwwyygrrgoryorgywyggrbgobobryrbbgowb')
        rotatedCube = testCube.rotate('u')
        self.assertEqual(rotatedCube, 'oryrwygogowoborwyywbbyygrrgwwworgywyrobggogbbryrbbgowb')
    
    def test_cubeTest_rotate_011_MissingDirection(self):
        testCube = cube.Cube('gobgwywrwwbgobwowgybygybyrybowygybrororgorrwrgybgrbowo')
        rotatedCube = testCube.rotate()
        self.assertEqual(rotatedCube, 'wggrwowybrbgwbwrwgybygybyrybogygybrbrorgoroywoowgrbowo')
    
    def test_cubeTest_rotate_012_EmptyDirection(self):
        testCube = cube.Cube('gobgwywrwwbgobwowgybygybyrybowygybrororgorrwrgybgrbowo')
        rotatedCube = testCube.rotate('')
        self.assertEqual(rotatedCube, 'wggrwowybrbgwbwrwgybygybyrybogygybrbrorgoroywoowgrbowo')
    
    def test_cubeTest_rotate_013_MultipleRotations(self):
        testCube = cube.Cube('oworwygogwbbborwyywwwyygrrgoryorgywyggrbgobobryrbbgowb')
        rotatedCube = testCube.rotate('Full')
        self.assertEqual(rotatedCube, 'grrgwwbyogrooorbyybbgyyorrorwyyrowwwwoybggobyrbwgbggwb')
    
    def test_cubeTest_rotate_901_InvalidDirection(self):
        testCube = cube.Cube('oworwygogwbbborwyywwwyygrrgoryorgywyggrbgobobryrbbgowb')
        rotatedCube = testCube.rotate('D')
        self.assertEqual(rotatedCube, 'error: invalid direction')
    
    def test_cubeTest_rotate_555_FullSolveFinalAlgorithm(self):
        testCube = cube.Cube('bgwwwwgwwobybbybbgbyygyywgbgwwrggooyobroooorgrrryrryor')
        rotatedCube = testCube.rotate('rLuRUbblrRuB')
        self.assertEqual(rotatedCube, 'wwwwwwwwwbbbbbbbbbyyyyyyyyygggggggggooooooooorrrrrrrrr')
        
    # Rotate State:
    #     Rotates a list of faces, showing which is the "front face" to map relative face algorithms to absolute face directions
    #
    #     input: 
    #         N/A
    #
    #     output:
    #         Nominal: N/A
    #         Side-effects: Changed "state" of cube, determining what rotate actually rotates
    #     
    #     happy path:
    #         DEVELOPER TESTS: getCurrentFace is a developer test only available outside of Cube for this test and these tests will be commented out
    #         test 001: Right turn
    #         test 002: Left turn
    #         test 003: Multiple turns
    #         test 004: Multiple turns 2
    #         REGULAR TESTS: determine if rotate now works with changed states, supplying correct rotations and string output for use in controller classes
    #                        These tests also use rotate, which has already been implemented and tested, but will be retested using new conditions
    #         test 001: Rotate all directions CW using F as basis
    #         test 002: Rotate all directions CW using R as basis
    #         test 003: Rotate all directions CW using B as basis
    #         test 004: Rotate all directions CW using L as basis
    #         test 005: Rotate all directions CCW using F as basis
    #         test 006: Rotate all directions CCW using R as basis
    #         test 007: Rotate all directions CCW using B as basis
    #         test 008: Rotate all directions CCW using L as basis
    #         test 009: Combination of all, resulting in string showing true rotations on cube
    #
    #     sad path:
    #         N/A
    #
    #     evil path:
    #         N/A
    
    
    def test_cubeTest_rotateCube_001_RightTurn(self):
        testCube = cube.Cube('aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeefffffffff')
        testCube.rotateCubeR()
        self.assertEqual('R', testCube.getCurrentOrientation())
        
    def test_cubeTest_rotateCube_002_LeftTurn(self):
        testCube = cube.Cube('aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeefffffffff')
        testCube.rotateCubeL()
        self.assertEqual('L', testCube.getCurrentOrientation())
        
    def test_cubeTest_rotateCube_003_MultipleTurns(self):
        testCube = cube.Cube('aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeefffffffff')
        testCube.rotateCubeR()
        testCube.rotateCubeL()
        testCube.rotateCubeR()
        testCube.rotateCubeR()
        self.assertEqual('B', testCube.getCurrentOrientation())
        
    def test_cubeTest_rotateCube_004_MultipleTurns2(self):
        testCube = cube.Cube('aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeefffffffff')
        testCube.rotateCubeL()
        testCube.rotateCubeR()
        testCube.rotateCubeL()
        testCube.rotateCubeL()
        self.assertEqual('B', testCube.getCurrentOrientation())
        
    def test_cubeTest_rotateUpdated_001_FBasisCW(self):
        testCube = cube.Cube('244300555344511211044522522134534530221041300333250110')
        testCube.rotate('FRBLU')
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube.get())
        
    def test_cubeTest_rotateUpdated_002_RBasiCW(self):
        testCube = cube.Cube('244300555344511211044522522134534530221041300333250110')
        testCube.rotateCubeR()
        testCube.rotate('LFRBU')
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube.get())
    
    def test_cubeTest_rotateUpdated_003_BBasiCW(self):
        testCube = cube.Cube('244300555344511211044522522134534530221041300333250110')
        testCube.rotateCubeR()
        testCube.rotateCubeR()
        testCube.rotate('BLFRU')
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube.get())
        
    def test_cubeTest_rotateUpdated_004_LBasiCW(self):
        testCube = cube.Cube('244300555344511211044522522134534530221041300333250110')
        testCube.rotateCubeL()
        testCube.rotate('RBLFU')
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube.get())
        
    def test_cubeTest_rotateUpdated_005_FBasisCCW(self):
        testCube = cube.Cube('444001355312412055423423155431435235211240000011052332')
        testCube.rotate('frblu')
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube.get())
        
    def test_cubeTest_rotateUpdated_006_RBasiCCW(self):
        testCube = cube.Cube('444001355312412055423423155431435235211240000011052332')
        testCube.rotateCubeR()
        testCube.rotate('lfrbu')
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube.get())
    
    def test_cubeTest_rotateUpdated_007_BBasiCCW(self):
        testCube = cube.Cube('444001355312412055423423155431435235211240000011052332')
        testCube.rotateCubeR()
        testCube.rotateCubeR()
        testCube.rotate('blfru')
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube.get())
        
    def test_cubeTest_rotateUpdated_008_LBasiCCW(self):
        testCube = cube.Cube('444001355312412055423423155431435235211240000011052332')
        testCube.rotateCubeL()
        testCube.rotate('rblfu')
        self.assertEqual('000000000111111111222222222333333333444444444555555555', testCube.get())
        
    def test_cubeTest_rotateUpdated_008_CombinationString(self):
        testCube = cube.Cube('000000000111111111222222222333333333444444444555555555')
        testCube.rotate('FRBLU')
        testCube.rotateCubeR()
        testCube.rotate('LFRBU')
        testCube.rotateCubeR()
        testCube.rotate('BLFRU')
        testCube.rotateCubeR()
        testCube.rotate('RBLFU')
        testCube.rotateCubeR()
        testCube.rotate('frblu')
        testCube.rotateCubeL()
        testCube.rotate('rblfu')
        testCube.rotateCubeL()
        testCube.rotate('blfru')
        testCube.rotateCubeL()
        testCube.rotate('lfrbu')
        correctStringList = ('FRBLUFRBLUFRBLUFRBLUfrblufrblufrblufrblu')
        self.assertEqual(correctStringList, testCube.getCurrentRotationString())
        
    # Analysis getRelativeSquare:
    #     Returns square value relative to the orientation state
    #     
    #     input:
    #         int [0-53] representing a square, unvalidated, developer use only
    #     
    #     output:
    #         char representing color of the requested cube
    #
    #     happy path:
    #         test 001: recreated cube F facing
    #         test 002: recreated cube R facing
    #         test 003: recreated cube B facing
    #         test 004: recreated cube L Facing
    #
    #     sad path:
    #         none
    #    
    #     evil path:
    #         none
    
    def test_cubeTest_getRelativeSquare_001_FFacing(self):
        testCube = cube.Cube('520403304503011230434225544011231052142044231551155323')
        recreatedCube = ''
        recreatedCube += testCube.getRelativeSquare(0)
        recreatedCube += testCube.getRelativeSquare(1)
        recreatedCube += testCube.getRelativeSquare(2)
        recreatedCube += testCube.getRelativeSquare(3)
        recreatedCube += testCube.getRelativeSquare(4)
        recreatedCube += testCube.getRelativeSquare(5)
        recreatedCube += testCube.getRelativeSquare(6)
        recreatedCube += testCube.getRelativeSquare(7)
        recreatedCube += testCube.getRelativeSquare(8)
        recreatedCube += testCube.getRelativeSquare(9)
        recreatedCube += testCube.getRelativeSquare(10)
        recreatedCube += testCube.getRelativeSquare(11)
        recreatedCube += testCube.getRelativeSquare(12)
        recreatedCube += testCube.getRelativeSquare(13)
        recreatedCube += testCube.getRelativeSquare(14)
        recreatedCube += testCube.getRelativeSquare(15)
        recreatedCube += testCube.getRelativeSquare(16)
        recreatedCube += testCube.getRelativeSquare(17)
        recreatedCube += testCube.getRelativeSquare(18)
        recreatedCube += testCube.getRelativeSquare(19)
        recreatedCube += testCube.getRelativeSquare(20)
        recreatedCube += testCube.getRelativeSquare(21)
        recreatedCube += testCube.getRelativeSquare(22)
        recreatedCube += testCube.getRelativeSquare(23)
        recreatedCube += testCube.getRelativeSquare(24)
        recreatedCube += testCube.getRelativeSquare(25)
        recreatedCube += testCube.getRelativeSquare(26)
        recreatedCube += testCube.getRelativeSquare(27)
        recreatedCube += testCube.getRelativeSquare(28)
        recreatedCube += testCube.getRelativeSquare(29)
        recreatedCube += testCube.getRelativeSquare(30)
        recreatedCube += testCube.getRelativeSquare(31)
        recreatedCube += testCube.getRelativeSquare(32)
        recreatedCube += testCube.getRelativeSquare(33)
        recreatedCube += testCube.getRelativeSquare(34)
        recreatedCube += testCube.getRelativeSquare(35)
        recreatedCube += testCube.getRelativeSquare(36)
        recreatedCube += testCube.getRelativeSquare(37)
        recreatedCube += testCube.getRelativeSquare(38)
        recreatedCube += testCube.getRelativeSquare(39)
        recreatedCube += testCube.getRelativeSquare(40)
        recreatedCube += testCube.getRelativeSquare(41)
        recreatedCube += testCube.getRelativeSquare(42)
        recreatedCube += testCube.getRelativeSquare(43)
        recreatedCube += testCube.getRelativeSquare(44)
        recreatedCube += testCube.getRelativeSquare(45)
        recreatedCube += testCube.getRelativeSquare(46)
        recreatedCube += testCube.getRelativeSquare(47)
        recreatedCube += testCube.getRelativeSquare(48)
        recreatedCube += testCube.getRelativeSquare(49)
        recreatedCube += testCube.getRelativeSquare(50)
        recreatedCube += testCube.getRelativeSquare(51)
        recreatedCube += testCube.getRelativeSquare(52)
        recreatedCube += testCube.getRelativeSquare(53)
        self.assertEqual(recreatedCube, testCube.get())
        
    def test_cubeTest_getRelativeSquare_002_RFacing(self):
        testCube = cube.Cube('520403304503011230434225544011231052142044231551155323')
        recreatedCube = ''
        testCube.rotateCubeR()
        recreatedCube += testCube.getRelativeSquare(0)
        recreatedCube += testCube.getRelativeSquare(1)
        recreatedCube += testCube.getRelativeSquare(2)
        recreatedCube += testCube.getRelativeSquare(3)
        recreatedCube += testCube.getRelativeSquare(4)
        recreatedCube += testCube.getRelativeSquare(5)
        recreatedCube += testCube.getRelativeSquare(6)
        recreatedCube += testCube.getRelativeSquare(7)
        recreatedCube += testCube.getRelativeSquare(8)
        recreatedCube += testCube.getRelativeSquare(9)
        recreatedCube += testCube.getRelativeSquare(10)
        recreatedCube += testCube.getRelativeSquare(11)
        recreatedCube += testCube.getRelativeSquare(12)
        recreatedCube += testCube.getRelativeSquare(13)
        recreatedCube += testCube.getRelativeSquare(14)
        recreatedCube += testCube.getRelativeSquare(15)
        recreatedCube += testCube.getRelativeSquare(16)
        recreatedCube += testCube.getRelativeSquare(17)
        recreatedCube += testCube.getRelativeSquare(18)
        recreatedCube += testCube.getRelativeSquare(19)
        recreatedCube += testCube.getRelativeSquare(20)
        recreatedCube += testCube.getRelativeSquare(21)
        recreatedCube += testCube.getRelativeSquare(22)
        recreatedCube += testCube.getRelativeSquare(23)
        recreatedCube += testCube.getRelativeSquare(24)
        recreatedCube += testCube.getRelativeSquare(25)
        recreatedCube += testCube.getRelativeSquare(26)
        recreatedCube += testCube.getRelativeSquare(27)
        recreatedCube += testCube.getRelativeSquare(28)
        recreatedCube += testCube.getRelativeSquare(29)
        recreatedCube += testCube.getRelativeSquare(30)
        recreatedCube += testCube.getRelativeSquare(31)
        recreatedCube += testCube.getRelativeSquare(32)
        recreatedCube += testCube.getRelativeSquare(33)
        recreatedCube += testCube.getRelativeSquare(34)
        recreatedCube += testCube.getRelativeSquare(35)
        recreatedCube += testCube.getRelativeSquare(36)
        recreatedCube += testCube.getRelativeSquare(37)
        recreatedCube += testCube.getRelativeSquare(38)
        recreatedCube += testCube.getRelativeSquare(39)
        recreatedCube += testCube.getRelativeSquare(40)
        recreatedCube += testCube.getRelativeSquare(41)
        recreatedCube += testCube.getRelativeSquare(42)
        recreatedCube += testCube.getRelativeSquare(43)
        recreatedCube += testCube.getRelativeSquare(44)
        recreatedCube += testCube.getRelativeSquare(45)
        recreatedCube += testCube.getRelativeSquare(46)
        recreatedCube += testCube.getRelativeSquare(47)
        recreatedCube += testCube.getRelativeSquare(48)
        recreatedCube += testCube.getRelativeSquare(49)
        recreatedCube += testCube.getRelativeSquare(50)
        recreatedCube += testCube.getRelativeSquare(51)
        recreatedCube += testCube.getRelativeSquare(52)
        recreatedCube += testCube.getRelativeSquare(53)
        recreatedCubeString = '503011230434225544011231052520403304201344142153552513'
        self.assertEqual(recreatedCube, recreatedCubeString)
        
    def test_cubeTest_getRelativeSquare_003_BFacing(self):
        testCube = cube.Cube('520403304503011230434225544011231052142044231551155323')
        recreatedCube = ''
        testCube.rotateCubeR()
        testCube.rotateCubeR()
        recreatedCube += testCube.getRelativeSquare(0)
        recreatedCube += testCube.getRelativeSquare(1)
        recreatedCube += testCube.getRelativeSquare(2)
        recreatedCube += testCube.getRelativeSquare(3)
        recreatedCube += testCube.getRelativeSquare(4)
        recreatedCube += testCube.getRelativeSquare(5)
        recreatedCube += testCube.getRelativeSquare(6)
        recreatedCube += testCube.getRelativeSquare(7)
        recreatedCube += testCube.getRelativeSquare(8)
        recreatedCube += testCube.getRelativeSquare(9)
        recreatedCube += testCube.getRelativeSquare(10)
        recreatedCube += testCube.getRelativeSquare(11)
        recreatedCube += testCube.getRelativeSquare(12)
        recreatedCube += testCube.getRelativeSquare(13)
        recreatedCube += testCube.getRelativeSquare(14)
        recreatedCube += testCube.getRelativeSquare(15)
        recreatedCube += testCube.getRelativeSquare(16)
        recreatedCube += testCube.getRelativeSquare(17)
        recreatedCube += testCube.getRelativeSquare(18)
        recreatedCube += testCube.getRelativeSquare(19)
        recreatedCube += testCube.getRelativeSquare(20)
        recreatedCube += testCube.getRelativeSquare(21)
        recreatedCube += testCube.getRelativeSquare(22)
        recreatedCube += testCube.getRelativeSquare(23)
        recreatedCube += testCube.getRelativeSquare(24)
        recreatedCube += testCube.getRelativeSquare(25)
        recreatedCube += testCube.getRelativeSquare(26)
        recreatedCube += testCube.getRelativeSquare(27)
        recreatedCube += testCube.getRelativeSquare(28)
        recreatedCube += testCube.getRelativeSquare(29)
        recreatedCube += testCube.getRelativeSquare(30)
        recreatedCube += testCube.getRelativeSquare(31)
        recreatedCube += testCube.getRelativeSquare(32)
        recreatedCube += testCube.getRelativeSquare(33)
        recreatedCube += testCube.getRelativeSquare(34)
        recreatedCube += testCube.getRelativeSquare(35)
        recreatedCube += testCube.getRelativeSquare(36)
        recreatedCube += testCube.getRelativeSquare(37)
        recreatedCube += testCube.getRelativeSquare(38)
        recreatedCube += testCube.getRelativeSquare(39)
        recreatedCube += testCube.getRelativeSquare(40)
        recreatedCube += testCube.getRelativeSquare(41)
        recreatedCube += testCube.getRelativeSquare(42)
        recreatedCube += testCube.getRelativeSquare(43)
        recreatedCube += testCube.getRelativeSquare(44)
        recreatedCube += testCube.getRelativeSquare(45)
        recreatedCube += testCube.getRelativeSquare(46)
        recreatedCube += testCube.getRelativeSquare(47)
        recreatedCube += testCube.getRelativeSquare(48)
        recreatedCube += testCube.getRelativeSquare(49)
        recreatedCube += testCube.getRelativeSquare(50)
        recreatedCube += testCube.getRelativeSquare(51)
        recreatedCube += testCube.getRelativeSquare(52)
        recreatedCube += testCube.getRelativeSquare(53)
        recreatedCubeString = '434225544011231052520403304503011230132440241323551155'
        self.assertEqual(recreatedCube, recreatedCubeString)
        
    def test_cubeTest_getRelativeSquare_004_LFacing(self):
        testCube = cube.Cube('520403304503011230434225544011231052142044231551155323')
        recreatedCube = ''
        testCube.rotateCubeL()
        recreatedCube += testCube.getRelativeSquare(0)
        recreatedCube += testCube.getRelativeSquare(1)
        recreatedCube += testCube.getRelativeSquare(2)
        recreatedCube += testCube.getRelativeSquare(3)
        recreatedCube += testCube.getRelativeSquare(4)
        recreatedCube += testCube.getRelativeSquare(5)
        recreatedCube += testCube.getRelativeSquare(6)
        recreatedCube += testCube.getRelativeSquare(7)
        recreatedCube += testCube.getRelativeSquare(8)
        recreatedCube += testCube.getRelativeSquare(9)
        recreatedCube += testCube.getRelativeSquare(10)
        recreatedCube += testCube.getRelativeSquare(11)
        recreatedCube += testCube.getRelativeSquare(12)
        recreatedCube += testCube.getRelativeSquare(13)
        recreatedCube += testCube.getRelativeSquare(14)
        recreatedCube += testCube.getRelativeSquare(15)
        recreatedCube += testCube.getRelativeSquare(16)
        recreatedCube += testCube.getRelativeSquare(17)
        recreatedCube += testCube.getRelativeSquare(18)
        recreatedCube += testCube.getRelativeSquare(19)
        recreatedCube += testCube.getRelativeSquare(20)
        recreatedCube += testCube.getRelativeSquare(21)
        recreatedCube += testCube.getRelativeSquare(22)
        recreatedCube += testCube.getRelativeSquare(23)
        recreatedCube += testCube.getRelativeSquare(24)
        recreatedCube += testCube.getRelativeSquare(25)
        recreatedCube += testCube.getRelativeSquare(26)
        recreatedCube += testCube.getRelativeSquare(27)
        recreatedCube += testCube.getRelativeSquare(28)
        recreatedCube += testCube.getRelativeSquare(29)
        recreatedCube += testCube.getRelativeSquare(30)
        recreatedCube += testCube.getRelativeSquare(31)
        recreatedCube += testCube.getRelativeSquare(32)
        recreatedCube += testCube.getRelativeSquare(33)
        recreatedCube += testCube.getRelativeSquare(34)
        recreatedCube += testCube.getRelativeSquare(35)
        recreatedCube += testCube.getRelativeSquare(36)
        recreatedCube += testCube.getRelativeSquare(37)
        recreatedCube += testCube.getRelativeSquare(38)
        recreatedCube += testCube.getRelativeSquare(39)
        recreatedCube += testCube.getRelativeSquare(40)
        recreatedCube += testCube.getRelativeSquare(41)
        recreatedCube += testCube.getRelativeSquare(42)
        recreatedCube += testCube.getRelativeSquare(43)
        recreatedCube += testCube.getRelativeSquare(44)
        recreatedCube += testCube.getRelativeSquare(45)
        recreatedCube += testCube.getRelativeSquare(46)
        recreatedCube += testCube.getRelativeSquare(47)
        recreatedCube += testCube.getRelativeSquare(48)
        recreatedCube += testCube.getRelativeSquare(49)
        recreatedCube += testCube.getRelativeSquare(50)
        recreatedCube += testCube.getRelativeSquare(51)
        recreatedCube += testCube.getRelativeSquare(52)
        recreatedCube += testCube.getRelativeSquare(53)
        recreatedCubeString = '011231052520403304503011230434225544241443102315255351'
        self.assertEqual(recreatedCube, recreatedCubeString)
        
    def test_cubeTest_isSolved_001_unsolved(self):
        testCube = cube.Cube('245403511024510222050423410551033353101143423245251403')
        isSolved = testCube.isSolved()
        self.assertFalse(isSolved)
        
    def test_cubeTest_isSolved_002_solved(self):
        testCube = cube.Cube('000000000111111111222222222333333333444444444555555555')
        isSolved = testCube.isSolved()
        self.assertFalse(isSolved)