#I really don't understand why here we have on the first repetition the same values of the reference and on the other repetitions not.

import numpy as np
k = [10**(-4),10**(-8),5*10**(-5),0.3]
X0 = [k[0]/k[1],20, 0, 0]

S = np.array([[1, -1, -1, 0, 0, 0],
              [0,  0,  1, -1, -1, 0],
              [0,  0,  0,  0,  1, -1],
              [0,  0,  0,  1,  0, 0]])



#Propensity rates are calculated having the konstants the educts and the degree order of the reaction for each reaction
def ReactionRates(k,X):
        R = np.zeros((6,1))
        R[0] = k[0]
        R[1] = k[1]* X[0]
        R[2] = X[0] * X[1] * k[2]
        R[3] = X[1] * 0.3
        R[4] = X[1] * k[3]
        R[5] = X[2] * k[1]
        return a


#Function that randomly select and index considering their relative probability, (input a propensity vector)
def reactionindex(a):
        r=np.random.rand()
        while r==0: #if r equal to 0 division is impossible
                r=np.random.rand()
        return np.sum(np.cumsum(arr)< (r*np.sum(arr))) # it creates an array of boolean and we count how many of those are True, and it is basically the index, strange way but it works.



#Function that calculates the time before any reaction happens, it takes as input "big lamda" that is the sum of our propensity vector
def time2nextreaction(lam):
        r=np.random.rand()
        while r==0: #if r equal to 0 division is impossible
                r=np.random.rand()
        return (1/lam) * (np.log(1/r))



def SSA (S,X0, t_final,k):
	X_store=[]
	T_store=[]
	t=0
	x=X0
	X_store.append(x[1,0])
	T_store.append(t)
        while t <t_final:
                a = ReactionRates(k,X0) 
                tau=time2nextreaction(np.sum(arr)
                if (t +tau > t_final) or (np.sum(a)==0):
                	return np.array(X_store), np.array(T_store)
                else:
                	t=t+tau
                	j=reactionindex(a)
                	x= x+S[:,[j]]
                	X_store.append(x[1,0])
                	T_store.append(t)
        return X_store, T_store




inputs = np.loadtxt('Input.txt')  # Load input parameters
seeds, NrSimulations = int(inputs[0]), int(inputs[1])
np.random.seed(seeds + i)  # Modify the seed for each trajectory



for i in range(NrSimulations):
    trajectory = gillespie(X0)
    np.savetxt(f'Taskk1Traj{i + 1}.txt', trajectory, delimiter=',', fmt='%1.3f')

