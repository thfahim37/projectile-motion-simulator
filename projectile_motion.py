import numpy as np
import matplotlib.pyplot as plt

print("Projectile Motion Simulator v1.0")

# Initial Conditions
x0 = 0 # Starting position
y0 = 0 # Starting height
ax = 0 # Horizontal acceleration
ay = -9.8 # Vertical acceleration
dt = 0.0001 # Step size

# User Input
v0 = float(input("Initial velocity:\n"))
angle = np.radians(float(input("Initial angle:\n" )))

# Components of Velocity
v0x = v0 * np.cos(angle)
v0y = v0 * np.sin(angle)

# Data Arrays
x_vals = [x0]
y_vals = [y0]
vx_vals = [v0x]
vy_vals = [v0y]

# Update Loop
while True:
	vx = vx_vals[-1] + ax * dt
	vy = vy_vals[-1] + ay * dt
	
	x = x_vals[-1] + vx * dt
	y = y_vals[-1] + vy * dt
	
	if y < 0:
		break # Stop as soon as projectile hits the ground
	
	x_vals.append(x)
	y_vals.append(y)
	vx_vals.append(vx)
	vy_vals.append(vy)


# Plot Customization
plt.title("Projectile Motion")
plt.xlabel("Distance")
plt.ylabel("Height")
plt.grid(True)

# Results
plt.plot(x_vals, y_vals)
plt.show()