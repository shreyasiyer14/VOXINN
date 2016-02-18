import random
import sys
import os

from ProceduralTerrain import *

class HeightmapMatrix:
    def __init__(self):
        pass
 
    def generate(self):
        heightmapList = []
        for i in range(40):
            subList = []
            for j in range(40):
                subList.append(0)
            heightmapList.append(subList)
        
        heightmapObj = ProceduralTerrain(heightmapList)
        for j in range(10):
            heightmaplist = heightmapObj.generateHill()
        
        return heightmaplist
        
