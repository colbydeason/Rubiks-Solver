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
    #    
    #    Analysis of Cube.rotate
    #        inputs:
    #            directions: string, len >= 0, in[FfRrBbLlUu]; optional, defaults to F if missing; unvalidated
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
    
    rngCube = 'oworwygogwbbborwyywwwyygrrgoryorgywyggrbgobobryrbbgowb'
    
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
        self.assertFalse()
