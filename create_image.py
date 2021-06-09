#create image using pyton code
import cv2
import numpy

cn=numpy.zeros([500,600,3])
cn.shape

#background
cn[:,:]=[12,10,255]

#house
cn[200:400,200:400]=[120,32,0]  #house lower rectangle
#triangle
for i,z,k in zip(range(100,200),range(300,200,-1),range(300,400)):
    m=z
    while(m<=k):
        cn[i,m]=[0,191,254]
        m+=1
#door rectangle        
cn[300:400,280:320]=[255,0,0]
# rectangle beside
cn[1:100,450:550]=[120,0,0]
cn[1:100,50:150]=[125,20,0]
cn[1:100,180:280]=[255,0,80]
cn[1:100,310:410]=[245,0,60]
cn[150:250,450:550]=[120,20,0]
cn[150:250,50:150]=[125,0,150]
cn[300:400,450:550]=[0,120,45]
cn[300:400,50:150]=[120,0,45]
cn[450:500,450:550]=[0,120,120]
cn[450:500,50:150]=[120,0,0]
cn[450:500,180:280]=[255,0,120]
cn[450:500,310:410]=[0,255,120]

#show image    
cv2.imshow("hi",cn)
cv2.waitKey()
cv2.destroyAllWindows()
