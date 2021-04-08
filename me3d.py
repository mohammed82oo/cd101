import Rhino.Geometry as rg

points=[]
K=0
for i in range(N):
    for j in range(N):
        point=rg.Point3d(i*STEP,j*STEP,NOISES[K])
        K+=1
        points.append(point)