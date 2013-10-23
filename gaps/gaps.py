#!/usr/bin/env python
import pylab as plt
import numpy as np

def ll(priorsidelength, ratio, sigmasquare):
	radius = priorsidelength * np.sqrt(ratio / np.pi)
	return -np.log(2.*np.pi)-2.*np.log(sigmasquare)-0.5*radius*radius/sigmasquare 


if __name__=="__main__":
	
	priorsidelength = 20.
	sigmasquare = 1.
	
	filename1 = "l00010000.txt"
	n1 = 10000.
	j1 = 3678.
	
	filename2 = "l00100000.txt"
	n2 = 100000.
	j2 = 36787.
	
	
	data1 = np.loadtxt( filename1 )
	data1 = data1 + 2*np.log(10)
	e1 = np.zeros( data1.shape[1] )
	var1 = np.zeros( data1.shape[1] )
	e1[0] = j1/(n1+1)
	var1[0] = j1*(n1-j1)/(n1+1)/(n1+1)/(n1+2)
	
	data2 = np.loadtxt( filename2 )
	data2 = data2 + 2*np.log(10)
	e2 = np.zeros( data2.shape[1] )
	var2 = np.zeros( data2.shape[1] )
	e2[0] = j2/(n2+1)
	var2[0] = j2*(n2-j2)/(n2+1)/(n2+1)/(n2+2)
	
	for i in range(1, data1.shape[1]):
		e1[i] = e1[0]*e1[i-1]
		e2[i] = e2[0]*e2[i-1]
		var1[i] = var1[0]*var1[i-1] + var1[i-1]*e1[0]*e1[0] + var1[0]*e1[i-1]*e1[i-1]
		var2[i] = var2[0]*var2[i-1] + var2[i-1]*e2[0]*e2[0] + var2[0]*e2[i-1]*e2[i-1]
	
	for i in range(6):
		print np.std(data1[:,i])
	for i in range(6):
		print np.std(data2[:,i])	
	for i in range(6):
		print str(200./np.pi*np.sqrt(var1[i]))
	for i in range(6):
		print str(200./np.pi*np.sqrt(var2[i]))
		#print str(-0.5*(ll(priorsidelength, e2[i]+np.sqrt(var2[i]), sigmasquare)-ll(priorsidelength, e2[i]-np.sqrt(var2[i]), sigmasquare)))
	
	i = 0
	
	plt.figure(0, figsize=(16,5))
	h2=plt.subplot(122)
	[N, Bins, Patches] = plt.hist(data2[:,i], bins=25, color='blue', histtype='step', linewidth = 3)
	plt.vlines(np.mean(data2[:,i]), 0, max(N)*1.1, color='green', linewidth = 3)
	plt.vlines(np.mean(data2[:,i])+np.std(data2[:,i]), 0, max(N)*1.1, color='green', linestyles='dashed', linewidth = 3)
	plt.vlines(np.mean(data2[:,i])-np.std(data2[:,i]), 0, max(N)*1.1, color='green', linestyles='dashed', linewidth = 3)
	plt.vlines(ll(priorsidelength, e2[i], sigmasquare), 0, max(N)*1.1, color='red', linewidth = 3)
	plt.vlines(ll(priorsidelength, e2[i]+np.sqrt(var2[i]), sigmasquare), 0, max(N)*1.1, color='red', linestyles='dashed', linewidth = 3)
	plt.vlines(ll(priorsidelength, e2[i]-np.sqrt(var2[i]), sigmasquare), 0, max(N)*1.1, color='red', linestyles='dashed', linewidth = 3)
	plt.xlabel('Level '+str(i+1)+' Threshold with '+str(int(n2))+' Likelihoods')
	locs, labels = plt.yticks()
	plt.yticks(locs,())
	plt.ylim(0, max(N)*1.1)
	
	h1=plt.subplot(121)
	[N, Bins, Patches] = plt.hist(data1[:,i], bins=25, color='blue', histtype='step', linewidth = 3)
	plt.vlines(np.mean(data1[:,i]), 0, max(N)*1.1, color='green', linewidth = 2)
	plt.vlines(np.mean(data1[:,i])+np.std(data1[:,i]), 0, max(N)*1.1, color='green', linestyles='dashed', linewidth = 3)
	plt.vlines(np.mean(data1[:,i])-np.std(data1[:,i]), 0, max(N)*1.1, color='green', linestyles='dashed', linewidth = 3)
	plt.vlines(ll(priorsidelength, e1[i], sigmasquare), 0, max(N)*1.1, color='red', linewidth = 3)
	plt.vlines(ll(priorsidelength, e1[i]+np.sqrt(var1[i]), sigmasquare), 0, max(N)*1.1, color='red', linestyles='dashed', linewidth = 3)
	plt.vlines(ll(priorsidelength, e1[i]-np.sqrt(var1[i]), sigmasquare), 0, max(N)*1.1, color='red', linestyles='dashed', linewidth = 3)
	plt.xlabel('Level '+str(i+1)+' Threshold with '+str(int(n1))+' Likelihoods')
	locs, labels = plt.yticks()
	plt.yticks(locs,())
	plt.ylim(0, max(N)*1.1)
	plt.savefig('level'+str(i+1)+'.eps')
	plt.show()
