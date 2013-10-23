#!/usr/bin/env python
import pylab as plt
import numpy as np
import keplers as kp

if __name__=="__main__":
	
	star_name = "282"
	#star_name = "fake1"
	
	data_name = star_name + '.txt'
	data = np.loadtxt( data_name )
	
	model_name = 'mod_3'
	time_label = '1363885779'
	para_name = 'best_fit_'+'exop_'+star_name+'_'+model_name+'_'+time_label+'.txt'
	
	#para_name = "best_fit_exop_122_mod_3_1363030508.txt"
	#para_name = "best_fit_exop_282_mod_3_1363885779.txt"
	#para_name = "best_fit_exop_282_mod_3_1376919313.txt"
	#para_name = "best_fit_exop_282_mod_2_1363885813.txt"
	#para_name = "best_fit_exop_fake1_mod_2_1364916949.txt"
	#para_name = "best_fit_exop_fake1_mod_3_1364916905.txt"
	para = np.loadtxt( para_name )
	
	num_comp = int(np.floor((para.shape[0] - 1)/5))
	
	fold_per = 2*np.pi/para[2*5+1]
	
	
	
	start_time = data[0,0]
	end_time = data[data.shape[0]-1,0]
	t=np.arange(0, 2.0*fold_per, 0.001)
	v=np.zeros(t.shape[0])
	data_fold = np.zeros( (data.shape[0]*2, 2) )
	
	for i in range(data.shape[0]):
		v2 = 0
		for j in range(2):
			v2 = v2 + kp.rad_v_pred(data[i,0]-data[0,0],para[j*5+0],para[j*5+1],para[j*5+2],para[j*5+3],para[j*5+4])
		v2 = v2 + para[num_comp*5]
		data_fold[i,1] = data[i,1] - v2
		data_fold[i + data.shape[0], 1] = data_fold[i,1]

	f = open('residual_'+star_name+'_'+model_name+'_'+time_label+'.txt', 'w')
	for i in range(data.shape[0]):
		f.write(str(data[i,0]) + '     ' + str(data[i,1]) + '      ' + str(data[i,2]) + '\n')
	
	for i in range(data.shape[0]):
		data_fold[i,0] = data[i,0] - np.floor( data[i,0] / fold_per ) * fold_per;
		data_fold[i + data.shape[0], 0] = data_fold[i,0] + fold_per
	
	v=np.zeros(t.shape[0])
	for i in range(v.shape[0]):
		for j in range(2,3):
			v[i] = v[i] + kp.rad_v_pred(t[i]-data[0,0],para[j*5+0],para[j*5+1],para[j*5+2],para[j*5+3],para[j*5+4])
	
	fig = plt.figure(num=1, figsize=(24,24))
	
	title = 'res of star ' + star_name + ' with 2 large companions removed'
	
	ax = fig.add_subplot(211)
	ax.plot(data_fold[:,0], data_fold[:,1], marker='+', markersize=12, markeredgewidth=3 ,linewidth=0, color=[0,0.5,0.02])
	ax.set_xlim(0, 2.0*fold_per)
	ax.tick_params(axis = 'both', which = 'major', labelsize = 30)
	#plt.title('residual of star ' + star_name + ' data (2 major planets removed) \n' +'period-folded according to the 3rd planet\'s period', fontsize='x-large')
	ax.set_ylabel('radial velocity '+'$(\mathrm{m\,s^{-1}})$', fontsize = 30, fontweight = 'bold')
	ax.grid(b=True)
	
	ax = fig.add_subplot(212)
	ax.plot(t,v,'.',alpha=0.8, color=[0,0,1], linewidth=0)
	ax.plot(data_fold[:,0], data_fold[:,1], marker='+', markersize=12, markeredgewidth=3, linewidth=0, color=[0,0.5,0.02])
	ax.set_xlim(0, 2.0*fold_per)
	ax.tick_params(axis = 'both', which = 'major', labelsize = 30)
	ax.grid(b=True)
	ax.set_xlabel('time '+r'$(\mathrm{day})$', fontsize = 30, fontweight = 'bold' )
	ax.set_ylabel('radial velocity '+'$(\mathrm{m\,s^{-1}})$', fontsize = 30, fontweight = 'bold')
	#plt.title('fit of residual of star ' + star_name + ' data \n' +'period-folded according to the 3rd planet\'s period', fontsize='x-large')
	plt.savefig('res_'+star_name+'_'+model_name+'_'+time_label+'.png')
	plt.savefig('res_'+star_name+'_'+model_name+'_'+time_label+'.eps')
