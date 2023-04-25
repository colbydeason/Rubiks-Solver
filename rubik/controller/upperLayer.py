from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpperLayer(theCube: Cube) -> str:
    if theCube.isSolved():
        return ''
    
    _solveCorners(theCube)
    # while not theCube.isSameColor([FTL, FML]):
    #     theCube.rotate('U')
    for face in range(4):
        if theCube.isSameColor([FTL, FML]):
            break
        else:
            theCube.rotate('u')
        
   
    _solveEdges(theCube)
    
    if not theCube.isSolved():
        return 'error: unsolvable cube' 
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
    for algo in range(3):
        for face in range (4):
            if edgeCube.isSameColor(FACEF):
                edgeCube.rotateCubeR()
                edgeCube.rotateCubeR()
                isSolidFace = True
                break
            else:
                edgeCube.rotateCubeR()
        if isSolidFace:
            
            
            # while not edgeCube.isSolved():
            #     edgeCube.rotate('FFUrLFFlRUFF')
            #     break
            if edgeCube.isSolved():
                return
            else:
                edgeCube.rotate('FFUrLFFlRUFF')
            
            
        else:
            edgeCube.rotate('FFUrLFFlRUFF')
            continue
    return 