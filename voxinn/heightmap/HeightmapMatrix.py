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
        sublist = []
        objects = 1600
        heightmapObj = ProceduralTerrain(heightmapList)
        for j in range(10):
            heightmaplist = heightmapObj.generateStar()
        for i in range(130):
            sublist.append(0)
        
        for j in range(65):
                heightmaplist.append(sublist)
        objects += 65 * 130 + 105
        for i in range(105):
        		heightmaplist[i].append(0)
        print objects
        return heightmaplist
        
        
