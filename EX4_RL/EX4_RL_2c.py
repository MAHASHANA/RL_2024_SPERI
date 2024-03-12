import numpy as np
import matplotlib.pyplot as plt

print("Hello")
# Parameters of the MDP and policies
prob_left = 0.9  # Probability of transitioning back to s when taking the left action
gamma = 1.0  # Discount factor

# Behavior policy: equal probability for right and left
def behavior_policy():
    return np.random.choice(['left', 'right'])

# Target policy always takes left
def target_policy():
    return 'left'

# Generate an episode
def generate_episode():
    episode = []
    while True:
        action = behavior_policy()
        if action == 'right':
            episode.append((action, 0))
            break
        else:
            episode.append((action, 0))
            if np.random.rand() > prob_left:
                episode.append(('termination', 1))
                break
    return episode

# Every-visit MC with importance sampling
def every_visit_mc_importance_sampling(num_episodes):
    value_estimates = []
    value = 0.0
    for _ in range(num_episodes):
        episode = generate_episode()
        G = 0
        W = 1
        for action, reward in reversed(episode):
            G = gamma * G + reward
            if action == 'left':
                W *= 2  # Importance sampling ratio (2 because behavior policy is 0.5 and target policy is 1)
            if W == 0:
                break
        if W != 0:
            value += W * G
            value_estimates.append(value / (_ + 1))
        else:
            value_estimates.append(value / (_ + 1))
    return value_estimates

#  Settings
num_runs = 7
num_episodes = 100000
every_visit_estimates = []

# Run the every-visit MC with importance sampling for a number of runs
for _ in range(num_runs):
    estimates = every_visit_mc_importance_sampling(num_episodes)
    every_visit_estimates.append(estimates)

# Plotting
plt.figure(figsize=(10, 6))
for run in every_visit_estimates:
    plt.plot(run, alpha=0.5)
plt.xscale('log')
plt.xlabel('Episodes (log scale)')
plt.ylabel('Monte-Carlo estimate of $v_π(s)$ with ordinary importance sampling')
plt.title('Every-Visit MC with Ordinary Importance Sampling (ten runs)')
plt.axhline(y=1, color='gray', linestyle='--')  # The correct value
plt.show()
