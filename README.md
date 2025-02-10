![image](https://github.com/user-attachments/assets/ee815c62-1ce0-44a5-a5bf-4848bf84150a)<img width="1199" alt="Screen Shot 2025-02-10 at 3 58 17 PM" src="https://github.com/user-attachments/assets/5841a142-bedd-4a29-84ca-564d50a6e9fa" /># navier-stokes-equation
These codes simulate particle motion in water flow, considering buoyancy, drag forces, and Newton’s Second Law, based on the Navier-Stokes equations.

This code simulates the motion of particles with varying densities in different types of water flows, specifically uniform and sinusoidal (variable) flows. It takes into account the forces acting on the particles, including buoyancy (which is the upward force exerted by the fluid on the particle) and drag force (the resistance experienced by the particle due to its motion in the fluid). These forces are modeled based on Newton's Second Law of Motion.

Functions:

uniform_flow(t, v_flow): Returns the constant velocity of the fluid in a uniform flow, based on the given v_flow.
variable_flow(t): Returns a sinusoidal velocity profile for a variable flow, simulating a fluid that changes speed over time.
compute_forces(rho_particle, r, v, v_fluid): Calculates the buoyancy and drag forces acting on a particle based on its density (rho_particle), radius (r), velocity (v), and the fluid velocity (v_fluid).
simulate_particle(rho_particle, r, v0, flow_type, v_flow, dt, t_max): Simulates the motion of a particle by updating its velocity and position over time using the forces calculated by compute_forces.
Outputs: The results of the simulation include the velocity and position of particles with different densities over time, under various fluid flow conditions (static water, uniform flow, and variable flow). These results are visualized using matplotlib for easy comparison of the particle's behavior in different scenarios.

Code 2: Simulation of Particle Motion in Constant Flow
This code simulates the motion of particles with different densities in a simple constant flow scenario. It calculates the forces acting on the particles, including buoyancy and drag force, and uses Newton's Second Law to update the particles' velocity and position over time.

Functions:

compute_forces(rho_particle, r, v): Calculates the buoyancy and drag forces acting on a particle, given the particle's density (rho_particle), radius (r), and velocity (v).
simulate_particle(rho_particle, r, dt, t_max): Simulates the motion of a particle in a constant flow by updating its velocity and position over time. The function returns the time (t), velocity (v), and position (y) of the particle.
Outputs: This code generates velocity and position plots over time for two particles with different densities, allowing for a comparison of their movement under constant flow conditions.

<img width="1241" alt="Screen Shot 2025-02-10 at 3 57 51 PM" src="https://github.com/user-attachments/assets/7d5c20ec-deae-4537-b82b-d07e0ebabcc4" />
<img width="1199" alt="Screen Shot 2025-02-10 at 3 58 17 PM" src="https://github.com/user-attachments/assets/5c799637-0c39-43d0-ab0a-9f480c3e8667" />
