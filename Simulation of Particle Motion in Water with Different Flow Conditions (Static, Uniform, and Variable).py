import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Gravitational acceleration (m/s^2)
rho_fluid = 1000  # Density of the fluid (water) (kg/m^3)
Cd = 0.47  # Drag coefficient for a sphere

# Types of water flow
def uniform_flow(t, v_flow):
    return v_flow  # Uniform flow with constant velocity

def variable_flow(t):
    return 0.2 * np.sin(2 * np.pi * t)  # Sinusoidal variable flow

def compute_forces(rho_particle, r, v, v_fluid):
    """Calculate buoyancy and drag forces for a particle"""
    volume = (4/3) * np.pi * r**3  # Particle volume
    mass = rho_particle * volume  # Particle mass
    
    # Buoyancy force
    Fb = (rho_fluid - rho_particle) * volume * g
    
    # Drag force
    A = np.pi * r**2  # Particle cross-sectional area
    relative_velocity = v - v_fluid  # Relative velocity of the particle with respect to the fluid
    Fd = 0.5 * Cd * rho_fluid * A * relative_velocity**2 * np.sign(relative_velocity)
    
    return Fb, Fd, mass

def simulate_particle(rho_particle, r, v0, flow_type, v_flow=0, dt=0.01, t_max=5):
    """Simulate the motion of a particle with a given density in a fluid flow"""
    t_values = np.arange(0, t_max, dt)
    v_values = []
    y_values = []
    
    y = 0  # Initial position
    v = v0  # Initial velocity
    
    for t in t_values:
        # Check if flow_type requires an extra argument
        if flow_type.__code__.co_argcount == 1:
            v_fluid = flow_type(t)  # Only pass t if the function takes one argument
        else:
            v_fluid = flow_type(t, v_flow)  # Otherwise, pass both t and v_flow
        
        Fb, Fd, mass = compute_forces(rho_particle, r, v, v_fluid)
        
        # Newton's Second Law: F = m * a
        F_net = Fb - Fd
        a = F_net / mass
        
        # Update velocity and position
        v += a * dt
        y += v * dt
        
        v_values.append(v)
        y_values.append(y)
    
    return t_values, v_values, y_values

    
    return t_values, v_values, y_values

# Simulations for two particles with different densities in various water flows
rho_particle_1 = 800  # Density lower than water (bubble)
rho_particle_2 = 1200 # Density higher than water (heavy particle)
radius = 0.01  # Particle radius (m)
initial_velocity = -1  # Initial velocity (m/s)

# Different water flow conditions
t, v1_static, y1_static = simulate_particle(rho_particle_1, radius, initial_velocity, uniform_flow, 0)
t, v2_static, y2_static = simulate_particle(rho_particle_2, radius, initial_velocity, uniform_flow, 0)

t, v1_uniform, y1_uniform = simulate_particle(rho_particle_1, radius, initial_velocity, uniform_flow, 0.5)
t, v2_uniform, y2_uniform = simulate_particle(rho_particle_2, radius, initial_velocity, uniform_flow, -0.5)

t, v1_variable, y1_variable = simulate_particle(rho_particle_1, radius, initial_velocity, variable_flow)
t, v2_variable, y2_variable = simulate_particle(rho_particle_2, radius, initial_velocity, variable_flow)

# Plot results
plt.figure(figsize=(12, 10))

# Velocity plots
plt.subplot(2, 2, 1)
plt.plot(t, v1_static, label="Bubble - Static Water")
plt.plot(t, v2_static, label="Heavy Particle - Static Water")
plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.title("Velocity in Static Water")

plt.subplot(2, 2, 2)
plt.plot(t, v1_uniform, label="Bubble - Uniform Flow")
plt.plot(t, v2_uniform, label="Heavy Particle - Uniform Flow")
plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.title("Velocity in Uniform Flow")

plt.subplot(2, 2, 3)
plt.plot(t, v1_variable, label="Bubble - Variable Flow")
plt.plot(t, v2_variable, label="Heavy Particle - Variable Flow")
plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.title("Velocity in Variable Flow")

# Position plots
plt.subplot(2, 2, 4)
plt.plot(t, y1_static, label="Bubble - Static Water")
plt.plot(t, y2_static, label="Heavy Particle - Static Water")
plt.plot(t, y1_uniform, label="Bubble - Uniform Flow")
plt.plot(t, y2_uniform, label="Heavy Particle - Uniform Flow")
plt.plot(t, y1_variable, label="Bubble - Variable Flow")
plt.plot(t, y2_variable, label="Heavy Particle - Variable Flow")
plt.xlabel("Time (seconds)")
plt.ylabel("Position (m)")
plt.legend()
plt.title("Comparison of Position in All Cases")

plt.tight_layout()
plt.show()
