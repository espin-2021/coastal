import matplotlib.pyplot as plt
from matplotlib import path
import numpy as np
import pandas as pd

def shorelinetogrid(x,y,dx,dy,plotdata=True):
    """ function to convert xy shoreline to gridded elevation for input to CEM
        takes arrays of x and y in UTM or lat lon values. Assumes a Dean Profile.
        Will plot output unless specified plotdata=False
            """
    # build grid
    # find the smallest and largest x's and y's to initialize grid boundaries 
    x0=int(np.ceil(min(x)/dx)*dx)
    y0=int(np.ceil(min(y)/dy)*dy)
    x1=x0 + int(np.ceil((max(x)-min(x))/dx)*dx-2*dx) # add total length of x to origin x
    y1=y0 + int(np.ceil((max(y)-min(y))/dy)*dy+5000)
    
    # create mesh grid of x and y
    [xg,yg] = np.meshgrid(list(range(x0,x1,dx)),list(range(y0,y1,dy)),sparse=False,indexing='ij')

    # generate bathy using dean profile
    surf_width=1000
    A=0.1 
    landmax=1
    rng=100000
    zg=np.zeros_like(xg)
    dist=np.zeros_like(xg)

    for i in range(0,xg.shape[1]):
        for j in range(0,xg.shape[0]):
            inrange=(abs(x-xg[j,i])<rng) & (abs(y-yg[j,i])<rng);
            r=np.zeros_like(x);
            r[inrange]=(x[inrange]-xg[j,i])**2 + (y[inrange]-yg[j,i])**2;
            r[~inrange]=1.e10;
            # Compute closest grid cell
            value=min(r);
            dist[j,i]=np.sqrt(value);
            zg[j,i]=-A*(dist[j,i])**(2/3);

    p = path.Path(np.transpose([x,y]))
    IN = p.contains_points(np.transpose([xg.flatten(),yg.flatten()]))
    IN = IN.reshape(xg.shape)
    zg[IN]=(min(A*(dist[IN])**(2/3)))+1
    zg=zg*-1
    if plotdata==True:
        Bathy = plt.contourf(xg,yg,zg, cmap=plt.cm.GnBu)
        cbar = plt.colorbar(Bathy)
        cbar.ax.set_ylabel('Depth (m)')
        plt.xlabel('Eastings')
        plt.ylabel('Northings')
        Shore = plt.plot(x,y,'k')
    return xg,yg,zg

def plotmeteo(X):
    fig,ax = plt.subplots(2,sharex=True);
    X.WVHT.plot(ax=ax[0]);
    ax[0].set_ylabel('Wave Height (m)',fontsize=12);
    X.DPD.plot(ax=ax[1]);
    ax[1].set_ylabel('Dominant Period (s)',fontsize=12);
    ax[1].set_xlabel('');