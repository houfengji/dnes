__all__ = ["triplot"]

import itertools

import matplotlib.pyplot as pl
from matplotlib.ticker import MaxNLocator

import numpy as np

def triplot(samples, titles=None, sfactor=0.1, maxindex=-1):
    """
    ## Arguments

    * `samples` (numpy.ndarray): The samples (nsamples, nvars).
    * `titles` (list): A list of length nvars.

    """
    nvars = samples.shape[-1]
    if titles is None:
        titles = [str(d) for d in range(nvars)]
    ranges = [[np.min(samples[:,i])*(1-sfactor),
               np.max(samples[:,i])*(1+sfactor)] for i in range(nvars)]
    assert nvars == len(titles)

    fig = pl.figure(figsize=(60, 60))

    for i, (yi,xi) in enumerate(itertools.product(np.arange(nvars),
                                                        np.arange(nvars))):
        if xi <= yi:
            x, y = samples[:,xi], samples[:,yi]
            ax = fig.add_subplot(nvars, nvars, i+1)

            if xi == yi:
                ax.hist(x, 50, histtype="step", color="k")
                ax.set_yticklabels([])
                ax.set_xlim(ranges[xi])
                ymin, ymax = ax.get_ylim()
                if maxindex >= 0:
	                ax.vlines(samples[maxindex,xi], ymin, ymax, color='r')
	                ax.set_ylim(ymin, ymax)
            else:
                ax.plot(x, y, ".k")
                ax.set_xlim(ranges[xi])
                ax.set_ylim(ranges[yi])
                xmin, xmax = ax.get_xlim()
                ymin, ymax = ax.get_ylim()
                if maxindex >= 0:
	                #ax.vlines(samples[maxindex,xi], ymin, ymax, color='r')
	                #ax.hlines(samples[maxindex,yi], xmin, xmax, color='r')
	                pl.axvline(samples[maxindex,xi], 0, 1, color='r')
	                pl.axhline(samples[maxindex,yi], 0, 1, color='r')

            ax.xaxis.set_major_locator(MaxNLocator(5))
            ax.yaxis.set_major_locator(MaxNLocator(5))

            if xi > 0:
                ax.set_yticklabels([])
            else:
                if yi > 0:
                    ax.set_ylabel(titles[yi])

            if yi < nvars-1:
                ax.set_xticklabels([])
            else:
                ax.set_xlabel(titles[xi])
                for t in ax.get_xticklabels():
                    t.set_rotation(60)

if __name__ == "__main__":
    #nvars, nsamples = 10, 1000
    #samples = np.random.randn(nvars*nsamples).reshape(nsamples, nvars)
    #titles = ["Variable %d"%i for i in range(nvars)]
    samples = np.loadtxt('295_chain_1_planet_1_oscillation.txt')
    dim = samples.shape[1]-1
    maxindex=-1
    
    if dim == 8:
    	samples[:,2] = samples[:,2] + samples[:,4]
    	flr = np.floor((samples[:,2] + 3.)/(2.*np.pi))
    	samples[:,2] = samples[:,2] - flr*(2.*np.pi)
    	samples[:,6] = np.sqrt(samples[:,6])
    	samples[:,7] = samples[:,7] * 365.25
    	titles = [r'$Orbital\,Amp\,(m\,s^{-1})$', r'$Orbital\,\omega\,(rad\,d^{-1})$', r'$\phi+\varpi\,(rad)$', r'$e$', r'$\varpi\,(rad)$', r'$v_0\,(m\,s^{-1})$', r'$Jitter\,(m\,s^{-1})$', r'$linear\,trend\,(m\,s^{-1}\,y^{-1})$']
    
    if dim == 11:
    	samples[:,2] = samples[:,2] + samples[:,4]
    	flr = np.floor((samples[:,2] + 3.)/(2.*np.pi))
    	samples[:,2] = samples[:,2] - flr*(2.*np.pi)
    	samples[:,6] = np.sqrt(samples[:,6])
    	samples[:,7] = samples[:,7] * 365.25
    	samples[:,8] = np.sqrt(samples[:,8])
    	maxindex = np.argmax(samples[:,11])
    	titles = [r'$Orbital\,Amp\,(m\,s^{-1})$', r'$Orbital\,\omega\,(rad\,d^{-1})$', r'$\phi+\varpi\,(rad)$', r'$e$', r'$\varpi\,(rad)$', r'$v_0\,(m\,s^{-1})$', r'$Jitter\,(m\,s^{-1})$', r'$linear\,trend\,(m\,s^{-1}\,y^{-1})$', r'$Oscillation\,V_{RMS}\,(m\,s^{-1})$', r'$Oscillation\,\omega_0\,(rad\,d^{-1})$', r'$Oscillation\,\gamma\,(d^{-1})$']
    
    if dim == 13:
    	samples[:,2] = samples[:,2] + samples[:,4]
    	flr = np.floor((samples[:,2] - 2.)/(2.*np.pi))
    	samples[:,2] = samples[:,2] - flr*(2.*np.pi)
    	samples[:,7] = samples[:,7] + samples[:,9]
    	flr = np.floor((samples[:,7] - 2.)/(2.*np.pi))
    	samples[:,7] = samples[:,7] - flr*(2.*np.pi)
    	samples[:,11] = np.sqrt(samples[:,11])
    	samples[:,12] = samples[:,12] * 365.25
    	titles = [r'$Orbital\,Amp\,1\,(m\,s^{-1})$', r'$Orbital\,\omega\,1\,(rad\,d^{-1})$', r'$\phi+\varpi\,1\,(rad)$', r'$e\,1$', r'$\varpi\,1\,(rad)$', r'$Orbital\,Amp\,2\,(m\,s^{-1})$', r'$Orbital\,\omega\,2\,(rad\,d^{-1})$', r'$\phi+\varpi\,2\,(rad)$', r'$e\,2$', r'$\varpi\,2\,(rad)$', r'$v_0\,(m\,s^{-1})$', r'$Jitter\,(m\,s^{-1})$', r'$linear\,trend\,(m\,s^{-1}\,y^{-1})$']
    	
    if dim == 16:
    	samples[:,2] = samples[:,2] + samples[:,4]
    	flr = np.floor((samples[:,2] - 3.)/(2.*np.pi))
    	samples[:,2] = samples[:,2] - flr*(2.*np.pi)
    	samples[:,7] = samples[:,7] + samples[:,9]
    	flr = np.floor((samples[:,7] - 3.)/(2.*np.pi))
    	samples[:,7] = samples[:,7] - flr*(2.*np.pi)
    	samples[:,11] = np.sqrt(samples[:,11])
    	samples[:,12] = samples[:,12] * 365.25
    	samples[:,13] = np.sqrt(samples[:,13])
    	titles = [r'$Orbital\,Amp\,1\,(m\,s^{-1})$', r'$Orbital\,\omega\,1\,(rad\,d^{-1})$', r'$\phi+\varpi\,1\,(rad)$', r'$e\,1$', r'$\varpi\,1\,(rad)$', r'$Orbital\,Amp\,2\,(m\,s^{-1})$', r'$Orbital\,\omega\,2\,(rad\,d^{-1})$', r'$\phi+\varpi\,2\,(rad)$', r'$e\,2$', r'$\varpi\,2\,(rad)$', r'$v_0\,(m\,s^{-1})$', r'$Jitter\,(m\,s^{-1})$', r'$linear\,trend\,(m\,s^{-1}\,y^{-1})$', r'$Oscillation\,V_{RMS}\,(m\,s^{-1})$', r'$Oscillation\,\omega_0\,(rad\,d^{-1})$', r'$Oscillation\,\gamma\,(d^{-1})$']
    
    triplot(samples[:,0:dim], titles, 0.01, maxindex)
    pl.savefig("triplot.png")
