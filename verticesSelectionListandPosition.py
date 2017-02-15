import maya.cmds as cmds

cmds.file(new=True, force=True)

cube = cmds.polyCube()
print 'cube'
vertexnumber = 0
print 'cube vertext number %d is at world pos pos=%s' % (vertexnumber, cmds.xform(
    str(cube[vertexnumber]) + ".pnts[" + str(vertexnumber) + "]", query=True, translation=True, worldSpace=True))

cmds.select(cube[0])
print cmds.polyEvaluate(v=True)
verticesNumber = cmds.getAttr(cube[0] + ".vrts", multiIndices=True)
print verticesNumber
# use either vtx or pnts to access an individual vertex (could also use the pointinfo commad check manual)
print cmds.xform(str(cube[0]) + ".vtx[" + str(vertexnumber) + "]", query=True, translation=True,
                 worldSpace=True)  # [1.1269192869360154, 4.5408735275268555, 1.3387055339628269]
print cmds.xform(str(cube[0]) + ".pnts[" + str(vertexnumber) + "]", query=True, translation=True,
                 worldSpace=True)  # [1.1269192869360154, 4.5408735275268555, 1.3387055339628269]

# OR use the shape node (not recommended)
cmds.select(cube[0])
nameStart = cube[0][:-1]
nameEnd = cube[0][-1]
verticesNumber = cmds.getAttr(str(nameStart) + "Shape" + str(nameEnd) + ".vrts", multiIndices=True)
print verticesNumber

# vtxIndexList = cmds.getAttr( strcube[1]+".vrts", multiIndices=True )

cmds.xform(str(cube[0]) + ".pnts[" + str(vertexnumber) + "]", query=True, translation=True,
           worldSpace=True)  # [1.1269192869360154, 4.5408735275268555, 1.3387055339628269]

print str(cube[0]) + ".pnts"
