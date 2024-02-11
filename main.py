import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = np.load("data_gearing_damage.npy", mmap_mode='r')

# Get the number of campaigns and situations
num_campaigns = data.shape[0]
num_situations = data.shape[1]

# Plot speed and torque for each campaign and situation
for campaign in range(num_campaigns):
    for situation in range(num_situations):
        speed_data = data[campaign, situation, 2]  # Actual speed (index 4)
        torque_data = data[campaign, situation, 3]  # Actual torque (index 5)

        # Plot speed over time
        plt.figure(figsize=(10, 6))
        plt.plot(speed_data, label='Speed')
        plt.title(f'Speed over Time for Campaign {campaign} Situation {situation}')
        plt.xlabel('Time')
        plt.ylabel('Speed (rpm)')
        plt.legend()
        plt.grid(True)
        plt.show()

        # Plot torque over time
        plt.figure(figsize=(10, 6))
        plt.plot(torque_data, label='Torque')
        plt.title(f'Torque over Time for Campaign {campaign} Situation {situation}')
        plt.xlabel('Time')
        plt.ylabel('Torque (Nm)')
        plt.legend()
        plt.grid(True)
        plt.show()
