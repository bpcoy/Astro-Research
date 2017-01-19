from astropy import *
from astropy.io import fits
from matplotlib import *
import math
import matplotlib.pyplot as plt
import numpy as np

metal=raw_input("What is the metallicity of the region?")
filename='modelm'+metal+'.cmd'
startlist=fits.open('hlsp_angst_hst_acs-wfc_10210-antlia_f606w-f814w_v1_gst.fits')
print startlist.info()
a=startlist[1]
filter1=a.data['MAG1_ACS']
filter2=a.data['MAG1_ACS']-a.data['MAG2_ACS']
plt.scatter(filter2,filter1,s=6)
print filter1
modelx=[]
modely=[]
#density=np.histogram2d(blah2,blah1,bins=100)
f=open(filename,'r')
x=15
while x:
    f.readline()
    x-=1

a=f.readline()
b=len(a.split())

dist=float(raw_input('What is the approximate distance in parsecs of this region?'))
distmod=5*math.log10(dist)-5
#distmod=25.546
distmod=0
extincta=float(raw_input('What is the extinction coefficient for filter 1?'))
#extincta=.194
extincta=0
extinctb=float(raw_input('And filter 2?'))
#extinctb=.120
extinctb=0
c=1
x=0
ages=[]
masses=[]
totalx=[]
totaly=[]
while c:
    if b==21:
        modelx+=[float(a.split()[12])-extinctb-float(a.split()[17])+extincta,]
        modely+=[float(a.split()[12])+distmod-extinctb,]
        ages+=[float(a.split()[1]),]
        masses+=[float(a.split()[2]),]
        
        a=f.readline()
        b=len(a.split())
    else:
        plt.plot(modelx,modely,'--')
        totalx+=modelx
        totaly+=modely
        modelx=[]
        modely=[]
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        a=f.readline()
        b=len(a.split())
        x+=1
        if b!=21:
            c=0


z=ages[0]
masslist=[]
gap1=1
gap2=1
x3=[]
x18=[]
y3=[]
y18=[]
for i in range(len(ages)):
    masslist+=[masses[i]]
    if abs(masses[i]-1.2552725051)<gap1:
        gap1=abs(masses[i]-1.2552725051)
        x1=totalx[i]
        y1=totaly[i]
    if abs(masses[i]-0.47712125472)<gap2:
        gap2=abs(masses[i]-0.47712125472)
        x2=totalx[i]
        y2=totaly[i]
    if ages[i]!=z:
        gap1=1
        gap2=1
        z=ages[i]
        x18+=[x1,]
        x3+=[x2,]
        y18+=[y1,]
        y3+=[y2,]


print y18

plt.scatter(x3,y3,s=100)
plt.scatter(x18,y18,s=100)  
plt.axis([-1,4,30,17])
plt.xlabel('F606W-F814W')
plt.ylabel('F814W')
plt.show()
