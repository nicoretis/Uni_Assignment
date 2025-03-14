import numpy as np

# A: -----Fixed Quantities-----
#0. initial state
#It loads the file with the initial quantitites
X0 = np.loadtxt('Input.txt')

# ===> fill here, everywhere where a "..." is <===

#1. Stoichiometric matrix calculated from the pdf reaction image
S = np.array([[1, -1, -1, 0, 1],
              [0, 0, 1, -1, -1],
              [0, 0, 0, 0, 1],
              [0, 0, -1, 0, 0]])

#2. reaction parameters given in the pdf
k = [5,3,12,7,3];


# B: functions that depend on the state of the system X
#Propensity rates are calculated having the konstants the educts and the degree order of the reaction for each reaction
def ReactionRates(k,X):
        R = np.zeros((5,1))
        R[0] = k[0]
        R[1] = k[1]*X[0]
        R[2] = k[2]*X[0]*X[3]
        R[3] = k[3]*X[1]
        R[4] = k[4]*X[1]
        return R


# compute reaction propensities/rates
R = ReactionRates(k,X0)

#compute the value of the ode with time step delta_t = 1
#np.dot combines the propensity function R with the stoichiometry matrix S to obtain the ODE
dX = np.dot(S,R)

##a) save stoichiometric Matrix
np.savetxt('SMatrix.txt',S,delimiter = ',',fmt='%1.0f');
##b) save ODE value as float with 2 digits after the comma (determined with the c-style precision argument e.g. '%3.2f')
np.savetxt('ODEValue.txt',dX,delimiter=',',fmt='%1.2f');

