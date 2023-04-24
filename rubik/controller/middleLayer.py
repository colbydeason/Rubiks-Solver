from rubik.model.constants import *
from rubik.model.cube import Cube

def solveMiddleLayer(theCube: Cube) -> str:
    
    # Solving Breakdown
    #
    # Step 1: Move edges out of middle layer
    #     find top edge that is yellow, move into place where edge is not yellow on middle layer
    # Step 2: Move edges into middle layer and solve
    #     go through each edge and come down
    
    if theCube.middleLayerDone():
        return ''
    _edgeOut(theCube)
    _bringDown(theCube)
    
    return theCube.popCurrentRotationStringResetOrientation()
    
def _edgeOut(edgeCube):
    topColor = UMM
    for edge in range(4):
        if edgeCube.checkForColor([FMR, RML], topColor):
            edgeCube.rotateCubeR()
            continue
        else:
            for j in range(4):
                if edgeCube.checkForColor([LTM, UML], topColor):
                    edgeCube.rotate('RUrufuF')
                    edgeCube.rotateCubeR()
                    break
                else:
                    edgeCube.rotate('U')
    edgeCube.resetCubeOrientation()
            
def _bringDown(solveCube):
    topColor = UMM
    for edge in range(4):
        # while solveCube.checkForColor([FTM, UBM], topColor):
        #         solveCube.rotate('u')
        for matchEdge in range(4):
            if solveCube.checkForColor([FTM, UBM], topColor):
                solveCube.rotate('u')
            else:
                break
        matchSide = _alignTopEdge(solveCube)
        match matchSide:
            case 'L':
                solveCube.rotate('ulULUFuf')
            case 'R':
                solveCube.rotate('URurufUF')
            
        
    
def _alignTopEdge(alignCube):
    # while alignCube.getRelativeSquare(FTM) != alignCube.getRelativeSquare(FMM):
    #     alignCube.rotate('u')
    #     alignCube.rotateCubeR()
    for face in range(4):
        if alignCube.getRelativeSquare(FTM) != alignCube.getRelativeSquare(FMM):
            alignCube.rotate('u')
            alignCube.rotateCubeR()
        else:
            break 
    if alignCube.getRelativeSquare(UBM) == alignCube.getRelativeSquare(LMM):
        matchSide = 'L'
    else:
        matchSide = 'R'
    return matchSide
            