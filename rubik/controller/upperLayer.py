import rubik.model.constants
from rubik.model.cube import Cube

def solveUpperLayer(theCube: Cube) -> str:
    
    _solveCorners(theCube)
    _solveEdges(theCube)
    
    return theCube.popCurrentRotationStringResetOrientation()

def _solveCorners(cornerCube):
    return 

def _solveEdges(edgeCube):
    return 