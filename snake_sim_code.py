import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Gait Parameters (from your code)
amplitude_deg = 25
frequency =  np.pi / 2  # rad/s
phase_offset = 0.05
n_links = 5
link_length = 1.0

# Motion Parameters
forward_speed = 0.03  # units/frame
fps = 30
t_total = 5
frames = int(t_total * fps)

# Initialize figure
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1, 10)
ax.set_ylim(-n_links / 2, n_links / 2)
line, = ax.plot([], [], 'o-', lw=3)

# Store base position
base_x = 0.0

def update(frame):
    global base_x
    t = frame / fps
    base_x += forward_speed

    # Compute angles for each link
    angles = np.array([
        amplitude_deg * np.sin(frequency * (t - (i + 1) * phase_offset)) * np.pi / 180
        for i in range(n_links)
    ])
    
    # Kinematic chain
    x, y = [base_x], [0]
    angle_sum = 0
    for theta in angles:
        angle_sum += theta
        x.append(x[-1] + link_length * np.cos(angle_sum))
        y.append(y[-1] + link_length * np.sin(angle_sum))

    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.title("LandSnake Forward Gait Simulation")
plt.xlabel("Forward Position")
plt.ylabel("Lateral Deviation")
plt.show()
