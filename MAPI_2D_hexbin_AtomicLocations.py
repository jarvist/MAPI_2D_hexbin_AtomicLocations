# MAPI_2D_hexbin_AtomicLocations.py
# Jarvist Moore Frost - originally written March 2014 ish
# Updated April 2016 with Hexbins and other slight niceities

# Reads in some cut-up .dat XYZ files; and generates 2D histograms of projections through them
# Nothing clever happens; the assumption is that your Z direction is orthogonal

import matplotlib.pyplot as plt

import numpy
import math
from IPython import embed #iPython magic for interactive session...

# These be my files
filelist=["C.dat", "I.dat", "Pb.dat", "C_symm.dat", "I_symm.dat", "Pb_symm.dat"]
nbins=42

# Suffix of _r reverses the colourmap
# See: http://matplotlib.org/examples/color/colormaps_reference.html
#colourmap=plt.cm.RdPu 
#colourmap=plt.cm.cubehelix_r
colourmap=plt.cm.Spectral_r

for datafile in filelist:
    data = numpy.genfromtxt(datafile)

    print(datafile)

    H,xedges,yedges = numpy.histogram2d(data[:,1],data[:,2],bins=nbins)
    H.shape, xedges.shape, yedges.shape
    # Detect where edges of data are (i.e. dynamic range)
    extent = [yedges[0], yedges[-1], xedges[0], xedges[-1]]
    
    if (yedges[-1]<1.0): # Bit of a hack - if the data appears to be bounded on [0,1], assume fractional
        extent = [0,1,0,1] # Fractional coordinates .'. plot 0 to 1
    if (yedges[-1]>5.0): # Worse hack - fixed unit cell, real space units
        extent = [0,12.57398,0,12.57398]

    # General setup of figure...
    fig=plt.figure()
    ax=fig.add_subplot(111)

#Contours - via http://micropore.wordpress.com/2011/10/01/2d-density-plot-or-2d-histogram/
# - Data are too noisy for this to be useful. Also, they're upside down?! Weird!
#fig.subplots_adjust(bottom=0.15,left=0.15)
#levels = (5.0e1, 4.0e1, 3.0e1, 2.0e1)
#cset = plt.contour(H, levels, origin='lower',colors=['black','green','blue','red'],linewidths=(1.9, 1.6, 1.5, 1.4),extent=extent)
#plt.clabel(cset, inline=1, fontsize=10, fmt='%1.0i')
#for c in cset.collections:
#    c.set_linestyle('solid')

# NOW WITH HEXBINS
# extent = limits over which bins are calculate (consumate with axes)
# mincnt = minimal count; below this histogram count hex-cell will be left blank (white)
    plt.hexbin(data[:,1],data[:,2],gridsize=nbins,marginals=False,cmap=colourmap,extent=extent,mincnt=1)
    plt.axis(extent)
    plt.grid(True)

# Or standard 2D histogram with numpy histogrammed data (see above)
#    plt.imshow(H,extent=extent,interpolation='nearest')
    plt.colorbar()
    plt.show()

    # Pb_I_2dhistogram.py
    fig.savefig(datafile.split(".")[0]+'_2dhistogram.png')
    plt.close()