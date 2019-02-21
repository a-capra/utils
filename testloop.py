import numpy as np

if __name__=='__main__':
	
	z=np.array([0.0,40.0])
	z=np.append(z, np.arange(80.,116.,0.5) )
    #print z
	phi=np.arange(0.,360.,5.)
	#print phi
	i=0
	for InitialZed in z:
		for InitialPhi in phi:
			i+=1
			
	print(i)
