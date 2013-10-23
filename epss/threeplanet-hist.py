#!/usr/bin/env python
import pylab as plt
import numpy as np

if __name__=="__main__":
	
	model_name = 'exop_282_mod_3'
	star_name = '282'
	data_name = star_name + '.txt'
	data = np.loadtxt( data_name )
	file_name = '282_mod_3_20130930.txt'
	sample = np.loadtxt( file_name )
	
	samindex = np.nonzero(sample[:,0] < 79)[0]
	
	fig = plt.figure(num=1, figsize=(24,24))
	
	ax = fig.add_subplot(221)
	ax.hist(sample[samindex,0], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$K_3\,(\mathrm{m\,s^{-1}})$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	ax = fig.add_subplot(222)
	ax.hist(sample[samindex,3], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$\mathrm{Eccentricity}_3$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	samindex54 = np.array([],dtype=long)
	for i in range(sample.shape[0]):
		if sample[i,1]>0.113:
			if sample[i,1]<0.117:
				if sample[i,0]<79:
					samindex54 = np.append(samindex54, i)
	
	period3 = np.zeros(sample.shape[0])
	for i in range(sample.shape[0]):
		period3[i] = 2.0 * np.pi / sample[i,1]
	
	ax = fig.add_subplot(223)
	ax.hist(period3[samindex], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$\mathrm{Period}_3\,(\mathrm{days})$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	ax = fig.add_subplot(224)
	ax.hist(period3[samindex54], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$\mathrm{Period}_3\,(\mathrm{days})$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	ax.set_title('zoom in', fontsize = 20, fontweight = 'bold')
	plt.savefig('282-3-hist.eps')
	plt.savefig('282-3-hist.png')
	
	
