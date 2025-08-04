import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
amplitude_deg = 25
frequency = 5 * np.pi / 2
phase_offset = 0.05
n_links = 5
link_length = 1.0
broken_link_index = 3  # Link 4 (zero-indexed)

# Simulation parameters
fps = 30
t_total = 10
frames = int(t_total * fps)

# Set up plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-5, 5)

# Plot handles
line, = ax.plot([], [], 'o-', lw=3, label="Snake Body")
first_dot, = ax.plot([], [], 'go', markersize=10, label="Link 1 (End)")
ax.legend()

# Initial position
head_pos = np.array([0.0, 0.0])
head_angle = 0.0

def update(frame):
    global head_pos, head_angle
    t = frame / fps

    # Joint angles (in radians)
    joint_angles = []
    for i in range(n_links):
        if i == broken_link_index:
            angle = 0.0  # simulate failed link
        else:
            angle = amplitude_deg * np.sin(frequency * (t - i * phase_offset))
        angle *= (-1)**i  # alternate servo direction
        joint_angles.append(np.deg2rad(angle))
    joint_angles = np.array(joint_angles)

    # Move snake forward
    head_angle = np.sum(joint_angles[::-1])
    speed = 0.05
    head_pos += speed * np.array([np.cos(head_angle), np.sin(head_angle)])

    # Build link positions
    x, y = [head_pos[0]], [head_pos[1]]
    angle = head_angle
    for theta in joint_angles:
        angle -= theta
        x.append(x[-1] + link_length * np.cos(angle))
        y.append(y[-1] + link_length * np.sin(angle))

    # Plot full body
    line.set_data(x, y)
    first_dot.set_data([x[-1]], [y[-1]])  # <- Fixed: wrap values in list

    return line, first_dot


ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.title("LandSnake Simulation — Link 1 Highlighted (End Module)")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.show()
