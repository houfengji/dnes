#!/usr/bin/env python
import pylab as plt
import numpy as np
import keplers as kp

if __name__=="__main__":
	
	star_name = "282"
	
	data_name = star_name + '.txt'
	data = np.loadtxt( data_name )
	res = np.zeros(data.shape[0])

	model_name = 'mod_4'
	dim = 4
	time_label = '20130930'
	para_name = '282_mod_4_select_20130930.txt'
	para = np.loadtxt( para_name )
	
	k = para.shape[0]-1
	for i in range(data.shape[0]):
		res[i] = data[i,1]
		for j in range(0,dim):
			res[i] = res[i] - kp.rad_v_pred(data[i,0]-data[0,0],para[k,j*5+0],para[k,j*5+1],para[k,j*5+2],para[k,j*5+3],para[k,j*5+4])
		res[i] = res[i] - para[k, 5*dim]
	
	
	start_time = data[0,0]
	end_time = data[data.shape[0]-1,0]
	time_span = end_time - start_time
	t = np.arange(start_time-0.1*time_span, end_time+0.1*time_span, 0.5)
	v = np.zeros(t.shape[0])
	
	fig = plt.figure(num=1, figsize=(36,36))
	
	ax = plt.subplot2grid((3,3), (2,0), colspan=3, rowspan=1)
	ax.errorbar(data[:,0], res[:], data[:,2], marker='o', markersize=15, markeredgewidth=3 ,linewidth=0, color=[0,0.5,0.02], markeredgecolor=[0,0.5,0.02], fmt='-', capsize=0, elinewidth=3)
	ax.set_xlim(t[0], t[t.shape[0]-1])
	ax.tick_params(axis = 'both', which = 'major', labelsize = 60)
	#plt.title('residual of star ' + star_name + ' data (2 major planets removed) \n' +'period-folded according to the 3rd planet\'s period', fontsize='x-large')
	ax.set_xlabel('Modified Julian Date '+r'$(\mathrm{day})$', fontsize = 60, fontweight = 'bold' )
	ax.set_ylabel('Residual '+'$(\mathrm{m\,s^{-1}})$', fontsize = 60, fontweight = 'bold')
	ax.hlines(0, t[0], t[t.shape[0]-1], color='r')
	ax.grid(b=True)
	
	ax = plt.subplot2grid((3,3), (0,0), colspan=3, rowspan=2)
	k = para.shape[0]-1
	for i in range(v.shape[0]):
		v[i] = 0
		for j in range(0,dim):
			v[i] = v[i] + kp.rad_v_pred(t[i]-data[0,0],para[k,j*5+0],para[k,j*5+1],para[k,j*5+2],para[k,j*5+3],para[k,j*5+4])
		v[i] = v[i] + para[k, 5*dim]
	ax.plot(t,v,'-',alpha=0.05, color=[0,0,1])
	
	for k in range(0,para.shape[0]):
		print str(k)
		for i in range(v.shape[0]):
			v[i] = 0
			for j in range(0,dim):
				v[i] = v[i] + kp.rad_v_pred(t[i]-data[0,0],para[k,j*5+0],para[k,j*5+1],para[k,j*5+2],para[k,j*5+3],para[k,j*5+4])
			v[i] = v[i] + para[k, 5*dim]
		ax.plot(t,v,'-',alpha=0.05, color=[0,0,1])
	
	ax.errorbar(data[:,0], data[:,1], data[:,2], marker='o', markersize=15, markeredgewidth=3 ,linewidth=0, color=[0,0.5,0.02], markeredgecolor=[0,0.5,0.02], fmt='-', capsize=0, elinewidth=3)
	#ax.plot(data[:,0], data[:,1], marker='+', markersize=12, markeredgewidth=3, linewidth=0, color=[0,0.5,0.02])
	ax.set_xlim(t[0], t[t.shape[0]-1])
	ax.tick_params(axis = 'both', which = 'major', labelsize = 60)
	ax.grid(b=True)
	ax.set_xticklabels([])
	ax.set_ylabel('Radial Velocity '+'$(\mathrm{m\,s^{-1}})$', fontsize = 60, fontweight = 'bold')
	#plt.title(str(dim)+'-Companion Fit for HIP88048', fontsize = 60, fontweight='bold')
	plt.savefig('fit_res_'+star_name+'_'+model_name+'_'+time_label+'.png')
	plt.savefig('fit_res_'+star_name+'_'+model_name+'_'+time_label+'.eps')
