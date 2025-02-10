import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Gravitational acceleration (m/s^2)
rho_fluid = 1000  # Fluid density (water) (kg/m^3)
Cd = 0.47  # Drag coefficient for a sphere

def compute_forces(rho_particle, r, v):
    """Calculate buoyancy and drag forces for a particle"""
    volume = (4/3) * np.pi * r**3  # Particle volume
    mass = rho_particle * volume  # Particle mass
    
    # Buoyancy force
    Fb = (rho_fluid - rho_particle) * volume * g
    
    # Drag force
    A = np.pi * r**2  # Cross-sectional area of the particle
    Fd = 0.5 * Cd * rho_fluid * A * v**2 * np.sign(v)
    
    return Fb, Fd, mass

def simulate_particle(rho_particle, r, dt=0.01, t_max=5):
    """Simulate the motion of a particle with a given density"""
    t_values = np.arange(0, t_max, dt)
    v_values = []
    y_values = []
    
    y = 0  # Initial position
    v = 0  # Initial velocity
    
    for t in t_values:
        Fb, Fd, mass = compute_forces(rho_particle, r, v)
        
        # Newton's Second Law: F = m * a
        F_net = Fb - Fd
        a = F_net / mass
        
        # Update velocity and position
        v += a * dt
        y += v * dt
        
        v_values.append(v)
        y_values.append(y)
    
    return t_values, v_values, y_values

# Simulation for two particles with different densities
rho_particle_1 = 800  # Density lower than water (bubble)
rho_particle_2 = 1200 # Density higher than water (heavy particle)
radius = 0.01  # Particle radius (m)

t, v1, y1 = simulate_particle(rho_particle_1, radius)
t, v2, y2 = simulate_particle(rho_particle_2, radius)

# Display results
plt.figure(figsize=(12, 5))

# Velocity plot
plt.subplot(1, 2, 1)
plt.plot(t, v1, label="Bubble (Density 800)")
plt.plot(t, v2, label="Heavy particle (Density 1200)")
plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.title("Velocity Change Over Time")

# Position plot
plt.subplot(1, 2, 2)
plt.plot(t, y1, label="Bubble (Density 800)")
plt.plot(t, y2, label="Heavy particle (Density 1200)")
plt.xlabel("Time (seconds)")
plt.ylabel("Position (m)")
plt.legend()
plt.title("Position Change Over Time")

plt.tight_layout()
plt.show()
