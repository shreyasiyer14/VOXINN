from voxinn import *

if __name__ == "__main__":
    window = Window((800,600))
    window.start(70)
    window.caption('Voxinn Voxel Engine Demo')
    blockList = []
    heightmapObj = HeightmapMatrix()
    terrain = TerrainGenerator(heightmapObj.generate())
    ID = terrain.generate()
    clock = pygame.time.Clock()
    play = Player(0,20,0)
    play.setOrigin(-10,-10,-50)
    moveList = [0,0,0]
    glNewList(12, GL_COMPILE)
    terrain.render(ID)
    glEndList()
    angle = 0.0
    mouse = False
    keymap = {'up':[0,0,1],'down':[0,0,-1],'left':[1,0,0],'right':[-1,0,0]}
    while True:
        mouse = KeyboardEvent(moveList, angle, keymap)
        if mouse:
            Control(0.2,0.2)
        window.clear()
        light0 = Light(30,50,20,[1,1,1,1],1)
        light0.bake(GL_LIGHT0)
        play.move(moveList[0],moveList[1],moveList[2])
        glCallList(12)
        clock.tick(60)
        window.update()
