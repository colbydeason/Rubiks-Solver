import rubik.model.constants
from rubik.model.cube import Cube

def solveUpSurface(theCube: Cube) -> str:
    
    return theCube.popCurrentRotationStringResetOrientation()

def _alignCorner(cornerCube):
    return True