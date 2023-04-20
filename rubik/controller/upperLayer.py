from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpperLayer(theCube: Cube) -> str:
    if theCube.isSolved():
        return ''
    _solveCorners(theCube)
    while not theCube.isSameColor([FTL, FML]):
        theCube.rotate('U')
        
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
        else:
            for face in range(4):
                if cornerCube.isSameColor([FTL, FTR]):
                    cornerCube.rotateCubeR()
                    cornerCube.rotateCubeR()
                    break
                else:
                    cornerCube.rotateCubeR()
            cornerCube.rotate('rFrBBRfrBBRR')
    cornerCube.resetCubeOrientation()
    return 

def _solveEdges(edgeCube):
    isSolidFace = False
    for algo in range(2):
        for face in range (4):
            if edgeCube.isSameColor([FACEF]):
                edgeCube.rotateCubeR()
                edgeCube.rotateCubeR()
                isSolidFace = True
                break
            else:
                edgeCube.rotateCubeR()
        if isSolidFace:
            while not edgeCube.isSolved():
                edgeCube.rotate('FFUrLFFlRUFF')
                break
        else:
            edgeCube.rotate('FFUrLFFlRUFF')
            continue
    return 