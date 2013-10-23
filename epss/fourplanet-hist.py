#!/usr/bin/env python
import pylab as plt
import numpy as np

if __name__=="__main__":
	
	model_name = 'exop_282_mod_4'
	star_name = '282'
	data_name = star_name + '.txt'
	data = np.loadtxt( data_name )
	file_name = '282_mod_4_20130930.txt'
	sample = np.loadtxt( file_name )
	
	period3 = np.zeros(sample.shape[0])
	for i in range(sample.shape[0]):
		period3[i] = 2.0 * np.pi / sample[i,1]
		
	period4 = np.zeros(sample.shape[0])
	for i in range(sample.shape[0]):
		period4[i] = 2.0 * np.pi / sample[i,6]
	
	bad = 66
	ens = 100
	ens_chain_length = sample.shape[0]/ens
	samindex = np.zeros(long(ens_chain_length*(ens-1)),dtype=long)
	j = 0
	for i in range(sample.shape[0]):
		if i%1000 == 0:
			print str(i)
		if i%ens != bad:
			samindex[j] = i
			j = j+1
			
	fig = plt.figure(num=1, figsize=(24,36))
	
	ax = fig.add_subplot(321)
	print str(1)
	ax.hist(sample[samindex,0], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$K_3\,(\mathrm{m\,s^{-1}})$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	ax = fig.add_subplot(323)
	print str(2)
	ax.hist(period3[samindex], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$\mathrm{Period}_3\,(\mathrm{days})$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	ax = fig.add_subplot(325)
	print str(3)
	ax.hist(sample[samindex,3], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$\mathrm{Eccentricity}_3$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	ax = fig.add_subplot(322)
	print str(4)
	ax.hist(sample[samindex,5], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$K_4\,(\mathrm{m\,s^{-1}})$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	ax = fig.add_subplot(324)
	print str(5)
	ax.hist(period4[samindex], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$\mathrm{Period}_4\,(\mathrm{days})$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	ax = fig.add_subplot(326)
	print str(6)
	ax.hist(sample[samindex,8], bins=50, histtype='step',linewidth=5)
	ax.set_xlabel(r'$\mathrm{Eccentricity}_4$', fontsize = 40, fontweight = 'bold')
	ax.set_yticklabels([])
	ax.tick_params(axis = 'x', which = 'major', labelsize = 25)
	
	plt.savefig('282-4-hist.eps')
	plt.savefig('282-4-hist.png')
	
	
