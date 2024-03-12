import random

def is_wall_or_out_of_bounds(x, y):
    # Define the wall locations and check boundaries
    walls = [
        (0, 5),
        (2, 5),
        (3, 5),
        (4, 5),
        (5, 0),
        (5, 2),
        (5, 3),
        (5, 4),
        (5, 5),
        (5, 6),
        (5, 7),
        (5, 9),
        (5, 10),
        (6, 4),
        (7, 4),
        (9, 4),
        (10, 4),]
    return (x < 0 or x > 10 or y < 0 or y > 10 or (x, y) in walls)

def simulate(state, action):
    x, y = state
    if state == (10, 10):  # Goal state, reset to start
        return (0, 0), 0

    # Define action effects
    action_effects = {
        'left': (-1, 0),
        'down': (0, 1),
        'right': (1, 0),
        'up': (0, -1)
    }

    # Determine actual action considering noise
    if random.random() < 0.9:
        actual_action = action
    else:
        # Choose one of the perpendicular actions
        if action in ['left', 'right']:
            actual_action = random.choice(['up', 'down'])
        else:
            actual_action = random.choice(['left', 'right'])

    # Calculate the new state
    dx, dy = action_effects[actual_action]
    new_x, new_y = x + dx, y + dy

    # Check for wall or boundary collisions
    if is_wall_or_out_of_bounds(new_x, new_y):
        new_x, new_y = x, y  # State does not change

    # Check for reaching the goal
    reward = 1 if (new_x, new_y) == (10, 10) else 0

    return (new_x, new_y), reward

# Example usage
print(simulate((0,10), 'up'))  # Test case as per the description






# import random

# def is_wall_or_out_of_bounds(x, y):
#     # Define the wall locations and check boundaries
#     walls = [(1,2), (2,2), (3,2), (4,2), (6,2), (7,2), (8,2), (9,2), (1,7), (2,7), (3,7), (4,7), (6,7), (7,7), (8,7), (9,7)]
#     return (x < 0 or x > 10 or y < 0 or y > 10 or (x, y) in walls)

# def simulate(state, action):
#     x, y = state
#     if state == (10, 10):  # Goal state, reset to start
#         return (0, 0), 0

#     # Define action effects
#     action_effects = {
#         'left': (-1, 0),
#         'down': (0, 1),
#         'right': (1, 0),
#         'up': (0, -1)
#     }

#     # Determine actual action considering noise
#     if random.random() < 0.8:
#         actual_action = action
#     else:
#         # Choose one of the perpendicular actions
#         if action in ['left', 'right']:
#             actual_action = random.choice(['up', 'down'])
#         else:
#             actual_action = random.choice(['left', 'right'])

#     # Calculate the new state
#     dx, dy = action_effects[actual_action]
#     new_x, new_y = x + dx, y + dy

#     # Check for wall or boundary collisions
#     if is_wall_or_out_of_bounds(new_x, new_y):
#         new_x, new_y = x, y  # State does not change

#     # Check for reaching the goal
#     reward = 1 if (new_x, new_y) == (10, 10) else 0

#     return (new_x, new_y), reward

# # Example usage
# simulate((0,10), 'up')  # Test case as per the description
