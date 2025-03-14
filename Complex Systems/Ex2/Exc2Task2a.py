import numpy as np
import matplotlib.pyplot as plt

def SSA(S_ini, k_in, k_dr):
    # Initialize
    I = 0
    t = 0
    S = S_ini

    # For Storage
    infected_times = []
    infected_counts = []

    while S > 0:
        # Calculate reaction rates
        r1 = k_dr * S
        r2 = k_in * S
        rates = [r1, r2]

        tau, reaction = find_reaction_time(rates)

        t += tau

        if reaction == 0:
            S -= 1  # Dropout
        elif reaction == 1:
            S -= 1  # Infection
            I += 1
            infected_times.append(t)  # Store time in infected_times list
            infected_counts.append(I)  # Store infected individual in infected_counts list

    return infected_times, infected_counts

def find_reaction_time(rates):
    # Get the total of rates
    r_total = sum(rates)

    # Get random uniform random numbers
    u1 = np.random.rand()
    u2 = np.random.rand()

    tau = (1.0 / r_total) * np.log(1.0 / u1)

    # Find out which reaction will happen
    reaction = np.searchsorted(np.cumsum(rates), u2 * r_total)

    return tau, reaction

# Load input data
with open('Input.txt', 'r') as f:
    seed = int(f.readline().strip())
np.random.seed(seed)

with open('kinf.txt', 'r') as f:
    k_in = [float(line.strip()) for line in f]

# Parameters
S_init = 100  # Number of trial participants
avg_follow_up_time = 1.0  # Average follow-up time per person
nsim = 100  # Number of simulations

# Run simulations
all_infected_counts = []
final_infected_counts = []  # To store final infected counts for histogram
data = []  # To store data for plotting

for k in k_in:
    k_dr = 1 / avg_follow_up_time - k
    infected_counts_final = []
    infected_times_final = []
    for count in range(nsim):
        infected_times, infected_counts = SSA(S_init, k, k_dr)
        data.append((infected_times, infected_counts))
        if infected_counts:
            infected_counts_final.append(infected_counts[-1])  # Store final count
            infected_times_final.append(infected_times[-1])  # Store final infection time
        else:# No infections occurred
            infected_counts_final.append(0)
            infected_times_final.append(0)
    all_infected_counts.append((infected_counts_final, infected_times_final))
    final_infected_counts.extend(infected_counts_final)

# Save results
with open('Task2Infected.txt', 'w') as f:
    for counts, times in all_infected_counts:
        for count, time in zip(counts, times):
            f.write(f'{count},{time}\n')

#Uncomment to show the plots

# # Plot ti vs. I(ti) for one simulation as a step function
# times, counts = data[0]
# plt.figure(figsize=(10, 6))
# plt.step(times, counts, where='post', label='Infections over time')
# plt.xlabel('Time (t)')
# plt.ylabel('Number of Infections (I(t))')
# plt.title('Function: Time vs. Infections')
# plt.legend()
# plt.grid()
# plt.show()

# # Histogram of I in t_end
# plt.figure(figsize=(10, 6))
# plt.hist(final_infected_counts, bins=20, alpha=0.7, color='blue', label='I(t_end) distribution')
# sample_mean = np.mean(final_infected_counts)
# plt.axvline(sample_mean, color='red', linestyle='dashed', linewidth=1.5, label=f'Sample Mean: {sample_mean:.2f}')

# #Number of cases reported in the clinical trial paper
# reported_cases = 8
# plt.axvline(reported_cases, color='green', linestyle='dashed', linewidth=1.5, label=f'Reported Cases: {reported_cases}')

# plt.xlabel('Number of Infected Individuals (I(t_end))')
# plt.ylabel('Frequency')
# plt.title('Histogram of Final Infected Individuals')
# plt.legend()
# plt.grid()
# plt.show()
