#!/usr/bin/env python
import pylab as plt
import numpy as np

if __name__=="__main__":
	
	model_name = 'exop_282_mod_2'
	star_name = '282'
	data_name = star_name + '.txt'
	data = np.loadtxt( data_name )
	file_name = '282_mod_2_20130930.txt'
	sample = np.loadtxt( file_name )
	
	period1 = np.zeros(sample.shape[0])
	for i in range(sample.shape[0]):
		period1[i] = 2.0 * np.pi / sample[i,1]
		
	period2 = np.zeros(sample.shape[0])
	for i in range(sample.shape[0]):
		period2[i] = 2.0 * np.pi / sample[i,6]
			
	fig = plt.figure(num=1, figsize=(24,36))
	
	ax = fig.add_subplot(321)
	print str(1)
	ax.hist(sample[:,0], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$K_1\,(\mathrm{m\,s^{-1}})$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	ax = fig.add_subplot(323)
	print str(2)
	ax.hist(period1[:], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$\mathrm{Period}_1\,(\mathrm{days})$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	ax = fig.add_subplot(325)
	print str(3)
	ax.hist(sample[:,3], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$\mathrm{Eccentricity}_1$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	ax = fig.add_subplot(322)
	print str(4)
	ax.hist(sample[:,5], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$K_2\,(\mathrm{m\,s^{-1}})$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	ax = fig.add_subplot(324)
	print str(5)
	ax.hist(period2[:], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$\mathrm{Period}_2\,(\mathrm{days})$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	ax = fig.add_subplot(326)
	print str(6)
	ax.hist(sample[:,8], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$\mathrm{Eccentricity}_2$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	plt.savefig('282-2-hist.eps')
	plt.savefig('282-2-hist.png')
	
	
