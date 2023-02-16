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
        
    def test_cubeTest_cube_904_UniqueCenterError(self):
        testCube = cube.Cube('lllllllll333333333KKKKKKKKKKrrrrrrrr999999999AAAAAAAAA')
        self.assertEqual('error: incorrect number of unique colors [6, 9 of each]', testCube.get())
        
        
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
    
    
    def test_cubeTest_rotateCube_001_RightTurn(self):
        testCube = cube.Cube('aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeefffffffff')
        testCube.rotateCubeR()
        self.assertEqual('R', testCube.getCurrentFrontFace())
        
    def test_cubeTest_rotateCube_002_LeftTurn(self):
        testCube = cube.Cube('aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeefffffffff')
        testCube.rotateCubeL()
        self.assertEqual('L', testCube.getCurrentFrontFace())
        
    def test_cubeTest_rotateCube_003_MultipleTurns(self):
        testCube = cube.Cube('aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeefffffffff')
        testCube.rotateCubeR()
        testCube.rotateCubeL()
        testCube.rotateCubeR()
        testCube.rotateCubeR()
        self.assertEqual('B', testCube.getCurrentFrontFace())
        
    def test_cubeTest_rotateCube_004_MultipleTurns2(self):
        testCube = cube.Cube('aaaaaaaaabbbbbbbbbcccccccccdddddddddeeeeeeeeefffffffff')
        testCube.rotateCubeL()
        testCube.rotateCubeR()
        testCube.rotateCubeL()
        testCube.rotateCubeL()
        self.assertEqual('B', testCube.getCurrentFrontFace())
        