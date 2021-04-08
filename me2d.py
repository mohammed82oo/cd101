import Rhino.Geometry as rg

P=[]
for i,val in enumerate(NOISES):
    point = rg.Point3d(i,val,0)
    P.append(point)