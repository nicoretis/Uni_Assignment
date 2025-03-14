import numpy as np

# Propensities
def propensities(x, k):
    R = np.zeros((4, 1))
    R[0] = k[0] * x[0] * (x[0] - 1)
    R[1] = k[1] * x[0] * (x[0] - 1) * (x[0] - 2)
    R[2] = k[2]
    R[3] = k[3] * x[0]
    return R


# Time to Reaction
def Time_To_Next_Reaction(lam):
    r = np.random.rand()
    while r == 0:
        r = np.random.rand()
    return (1.0 / lam) * np.log(1.0 / r)


# Find Reaction Index
def Find_Reaction_Index(a):
    r = np.random.rand()
    while r == 0:
        r = np.random.rand()
    return np.sum(np.cumsum(a) < r * np.sum(a))


# Stochastic Simulation Algorithm (SSA)
def SSA(Stochiometry, X_0, t_final, k):
    X_store = []
    T_store = []

    # Initialize
    t = 0.0
    x = X_0
    X_store.append(x[0])
    T_store.append(t)

    while t < t_final:
        a = propensities(x, k)
        tau = Time_To_Next_Reaction(np.sum(a))
        if (t + tau > t_final) or (np.sum(a) == 0):
            return np.array(X_store), np.array(T_store)
        else:
            t += tau
            j = Find_Reaction_Index(a)
            x += Stochiometry[:, j]
            X_store.append(x[0])
            T_store.append(t)

inputs = np.loadtxt('Input.txt')
rdseed, NrSimulations= int(inputs[0]),int(inputs[1])

np.random.seed(rdseed)

for i in range(NrSimulations):
    # Reaction Parameters
    k = np.array([0.15, 0.0015, 20.0, 3.5])
    # Stoichiometric Matrix
    S = np.array([[1, -1, 1, -1]])
    # Initial State
    x0 = np.array([40])
    
    states, times = SSA(S, x0, 5, k)
    times_formatted = ",".join(f"{time:.3f}" for time in times)
    states_formatted = ",".join(f"{int(state):.3f}" for state in states)
    Output = np.concatenate((np.array(times,ndmin=2),np.array(states,ndmin=2)), axis=0)
    np.savetxt('Task1Traj'+str(i+1)+'.txt',Output,delimiter = ',',fmt='%1.3f')

#################
#####PART B######
#import matplotlib.pyplot as plt
# x1_t5=[]
# for i in range(200):
#     k = np.array([0.15, 0.0015, 20.0, 3.5])
#     S = np.array([[1, -1, 1, -1]])
#     x0 = np.array([40])
    
#     states, times = SSA(S, x0, 5, k)
#     x1_t5.append(states[-1])

# below_equal_40 = [x for x in x1_t5 if x <= 40]
# above_40 = [x for x in x1_t5 if x > 40]
# bin_edges = np.arange(0,200, 5)
# expected_value= np.mean(x1_t5)
# # Plot the histograms
# plt.figure(figsize=(10, 6))
# plt.hist(below_equal_40, bins=bin_edges, color='skyblue', edgecolor='black')
# plt.hist(above_40, bins=bin_edges, color='salmon', edgecolor='black')
# plt.axvline(expected_value, color='darkred', linestyle=':', linewidth=2)
# plt.xlim(left=0, right=max(above_40)+5)
# plt.xlabel('X1', fontsize=20)
# plt.ylabel('Counts', fontsize=20)
# plt.title('Counts of X1 at T5', fontsize=20)
# plt.show()


#################
#####PART C######
# Lists to store simulation results
# all_states = []
# all_times = []
# np.random.seed(222)
# # Run 20 simulations
# for i in range(10):
#     k = np.array([0.15, 0.0015, 20.0, 3.5])
#     S = np.array([[1, -1, 1, -1]])
#     x0 = np.array([40])
#     states, times = SSA(S, x0, 5, k)
#     all_states.append(states)
#     all_times.append(times)

# # Plot the simulations
# plt.figure(figsize=(10, 6))
# for i in range(10):
#     plt.step(all_times[i], all_states[i], where='post', label=f'Simulation {i+1}', 
#              linewidth=10, alpha=0.5)  # Adjust thickness and transparency
# plt.xlabel('Time', fontsize=20)
# plt.ylabel('State', fontsize=20)
# plt.title('10 Stochastic Simulations', fontsize=20)
# plt.grid(True, alpha=0.5) 
# plt.show()
