from astropy import *
from astropy.io import fits
from matplotlib import *
import matplotlib.pyplot as plt


startlist=fits.open('hlsp_angst_hst_acs-wfc_10210-antlia_f606w-f814w_v1_gst.fits')
print startlist.info()
a=startlist[1]
blah1=a.data['MAG1_ACS']
blah2=a.data['MAG1_ACS']-a.data['MAG2_ACS']
def density(x,y):
    p=0
    for item in blah1:
        for thing in blah2:
            if abs(thing-x)<.1 and abs(item-y)<.2:
                p+=1
    return p

dense=[]
for i in range(0,len(blah1)):
    dense+=[density(blah2[i],blah1[i]),]

plt.plot(blah2,blah1,'ro')
plt.axis([-1,4,28,19])
plt.set_xlabel('F606W-F814W')
plt.set_ylabel('F814W')
plt.contour(blah2,blah1,dense)
plt.show()
