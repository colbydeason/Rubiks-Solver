from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpperLayer(theCube: Cube) -> str:
    
    _solveCorners(theCube)
    _solveEdges(theCube)
    
    return theCube.popCurrentRotationStringResetOrientation()

def _solveCorners(cornerCube):
    for algo in range(2):
        numSolved = 0
        for face in range(4):
            if cornerCube.isSameColor([FTL, FTR]):
                numSolved += 1
                cornerCube.rotateCubeR()
        if numSolved == 4:
            return
        for face in range(3):
            if cornerCube.isSameColor([FTL, FTR]):
                cornerCube.rotateCubeR()
                cornerCube.rotateCubeR()
                break
            else:
                cornerCube.rotateCubeR()
        cornerCube.rotate('rFrBBRfrBBRR')
    return 

def _solveEdges(edgeCube):
    return 