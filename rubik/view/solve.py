from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
import hashlib
import random

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
     
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    if theCube.get().startswith('error: '):
        result['status'] = theCube.get()
        return result
    if theCube.isSolved():
        rotations = ""
    else:
        rotations = ""
        rotations += solveBottomCross(theCube)      #iteration 2
        rotations += solveBottomLayer(theCube)      #iteration 3
        rotations += solveMiddleLayer(theCube)      #iteration 4
        rotations += solveUpCross(theCube)          #iteration 5
        rotations += solveUpSurface(theCube)        #iteration 5
        rotations += solveUpperLayer(theCube)       #iteration 6

        
        # rotations = ""
        # rotSolveBottomCross = solveBottomCross(theCube)
        # rotSolveBottomLayer = solveBottomLayer(theCube)
        # rotSolveMiddleLayer = solveMiddleLayer(theCube) 
        # rotSolveUpCross = solveUpCross(theCube)
        # rotSolveUpSurface = solveUpSurface(theCube)
        # rotSolveUpperLayer = solveUpperLayer(theCube)
        # rotArray = {rotSolveBottomCross, rotSolveBottomLayer, rotSolveMiddleLayer, rotSolveUpCross, rotSolveUpSurface, rotSolveUpperLayer}
        # for rotationString in rotArray:
        #     if rotationString == 'error: unsolvable cube':
        #         result['status'] = rotationString
        #         return result
        #     else:
        #         rotations += rotationString
        
        
    itemToTokenize = encodedCube + rotations + 'cjd0057'
    sha256Hash = hashlib.sha256()
    sha256Hash.update(itemToTokenize.encode())
    fullToken = sha256Hash.hexdigest()
    tokenIndex = random.randint(0, len(fullToken) - 8)
    integrityToken = fullToken[tokenIndex:tokenIndex + 8]
    
    result['status'] = 'ok' 
    result['solution'] = rotations   
    result['integrity'] = integrityToken                    #iteration 3
                     
    return result

