import numpy as np

#### Dependencies ####
# Propensities / Reaction Rate
def ReactionRates(x, k):
    R = np.zeros((2, 1))
    R[0] = k[0] * x[0]
    R[1] = k[1] * x[1]
    return R

def RHS(t, X, k): #time and a state
  R = ReactionRates(X, k)
  dX = np.dot(S, R).flatten()  # Flatten the result to match dimensionality
  return dX

def ExplicitEuler (X, t, stepsize, param):
  X_next = X + stepsize * RHS(t, X, param)
  return X_next

def Integration(X0, t0, stepsize, param, t_end): # The last parameters can be timepoint also, then while loop will change to "for t in timepoint"
  t = t0
  X = X0
  t_store = [t]
  X_store = [X]
  while t < t_end:
    X = ExplicitEuler(X, t, stepsize, param)
    t += stepsize
    t_store.append(t)
    X_store.append(X)
  return np.array(X_store), np.array(t_store)

#### Main ####

# Reaction Parameters
k = np.array([0.5, 0.3]) # k[0] = ka, k[1] = ke

# Stoichiometric Matrix
S = np.array([[-1, 0], # Loss in dosing compartment
              [1, -1]]) # Gain in bloodstream and elimination

# Initial State
x0 = np.array([200, 0]) # x0[0] = dosage of drug, x0[1] = initial conc. in blood stream

states, times = Integration(x0, 0, 1, k, 24)

Output = np.concatenate((np.array(times,ndmin=2),np.array(states[:,1],ndmin=2)), axis=0)
np.savetxt('Task2aTraj.txt',Output,delimiter = ',',fmt='%1.2f')