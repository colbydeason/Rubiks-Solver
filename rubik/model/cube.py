from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        self._cube = encodedCube
        self._cubeList = list(self._cube)
        
    def rotate(self, directions = 'F'):
        self._rotateF()
        pass
    
    def get(self):
        return self._cube

    # Individual rotation private methods
    def _rotateF(self):
        rotatedCubeList = self._cubeList[:]
        # Rotate front panels
        rotatedCubeList[2] = self._cubeList[0]
        rotatedCubeList[5] = self._cubeList[1]
        rotatedCubeList[8] = self._cubeList[2]
        rotatedCubeList[1] = self._cubeList[3]
        rotatedCubeList[4] = self._cubeList[4]
        rotatedCubeList[7] = self._cubeList[5]
        rotatedCubeList[0] = self._cubeList[6]
        rotatedCubeList[3] = self._cubeList[7]
        rotatedCubeList[6] = self._cubeList[8]
        # Rotate top panels CW
        rotatedCubeList[9] = self._cubeList[42]
        rotatedCubeList[12] = self._cubeList[43]
        rotatedCubeList[13] = self._cubeList[44]
        # Rotate right panels CW
        rotatedCubeList[45] = self._cubeList[9]
        rotatedCubeList[46] = self._cubeList[12]
        rotatedCubeList[47] = self._cubeList[15]
        # Rotate bottom panels CW
        rotatedCubeList[29] = self._cubeList[45]
        rotatedCubeList[32] = self._cubeList[46]
        rotatedCubeList[35] = self._cubeList[47]
        # Rotate left panels CW
        rotatedCubeList[42] = self._cubeList[29]
        rotatedCubeList[43] = self._cubeList[32]
        rotatedCubeList[44] = self._cubeList[35]
        # Modifies the cube
        self._cubeList = rotatedCubeList
        return self._cubelist
        
    def _rotatef(self):
        pass
    
    def _rotateB(self):
        pass
    
    def _rotateb(self):
        pass

    def _rotateL(self):
        pass

    def _rotatel(self):
        pass

    def _rotateR(self):
        pass

    def _rotater(self):
        pass

    def _rotateU(self):
        pass

    def _rotateu(self):
        pass