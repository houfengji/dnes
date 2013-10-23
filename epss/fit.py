#!/usr/bin/env python
import pylab as plt
import numpy as np
import keplers as kp
import covariance as cov

if __name__=="__main__":
	
	star_name = "282"
	#star_name = "fake1"
	
	data_name = star_name + ".txt"
	data = np.loadtxt( data_name )
	
	para_name = "best_fit_exop_282_mod_3_1376919313.txt"
	#para_name = "best_fit_exop_282_mod_2_1363885813.txt"
	#para_name = "best_fit_exop_fake1_mod_2_1364916949.txt"
	#para_name = "best_fit_exop_fake1_mod_3_1364916905.txt"
	para = np.loadtxt( para_name )
	
	num_comp = int(np.floor((para.shape[0] - 1)/5))
	
	plt.figure(num=1, figsize=(16,12))
	
	start_time = data[0,0]
	end_time = data[data.shape[0]-1,0]
	time_span = end_time - start_time
	t=np.arange(start_time-0.2*time_span, end_time+0.2*time_span,0.1)
	v=np.zeros(t.shape[0])
	
	for i in range(v.shape[0]):
		for j in range(num_comp):
			v[i] = v[i] + kp.rad_v_pred(t[i]-data[0,0],para[j*5+0],para[j*5+1],para[j*5+2],para[j*5+3],para[j*5+4])
		v[i] = v[i] + para[num_comp*5]
	
	if num_comp == 2:
		title = 'fit of star ' + star_name + ' with ' + str(num_comp) + ' comp(s)\n' + 'Period 1: ' + str(np.round(2*np.pi/para[1])) + ' d; ' + 'Period 2: ' + str(np.round(2*np.pi/para[6])) + ' d '
	
	if num_comp == 3:
		title = 'fit of star ' + star_name + ' with ' + str(num_comp) + ' comp(s)\n' + 'Period 1: ' + str(np.round(2*np.pi/para[1])) + ' d; ' + 'Period 2: ' + str(np.round(2*np.pi/para[6])) + ' d; ' + 'Period 3: ' + str(np.round(2*np.pi/para[11])) + ' d '
	
	plt.plot(t,v,alpha=0.8,color=[0,0,1])
	plt.plot(data[:,0], data[:,1], marker='+', markersize=12, linewidth=0)
	plt.grid(b=True)
	plt.xlabel('time '+r'$(d)$', fontsize='x-large')
	plt.ylabel('radial velocity '+'$(m\,s^{-1})$', fontsize='x-large')
	plt.title(title, fontsize='x-large')
	plt.savefig('fit_'+star_name+'_'+str(num_comp)+'_comp'+'.png')
