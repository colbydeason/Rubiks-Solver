import rubik.model.constants
from rubik.model.cube import Cube

def solveUpCross(theCube: Cube) -> str:
    return theCube.popCurrentRotationStringResetOrientation()

def _alignShape(shapeCube):
    return True