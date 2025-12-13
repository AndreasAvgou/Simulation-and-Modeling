import numpy as np
import matplotlib.pyplot as plt

def run_ofc_simulation():
    # Parameters based on the C file and PDF
    N = 10              # Grid size (10x10) [cite: 16]
    F_CRIT = 4.0        # Critical Threshold 
    F_OUT = 0.001       # External driving force added every step 
    ALPHA = 0.25        # Distribution factor (25% to each neighbor) [cite: 63]
    STEPS = 50000       # Simulation steps
    
    # Initialize grid with random values between 0 and F_CRIT 
    grid = np.random.uniform(0, F_CRIT, (N, N))
    
    avalanche_sizes = [] # To store size of earthquakes
    time_series = []     # To store activity over time

    print(f"Starting OFC Earthquake Simulation on {N}x{N} grid for {STEPS} steps...")

    for t in range(STEPS):
        # STEP 1: Increase all cells by F_OUT [cite: 19, 62]
        grid += F_OUT
        
        step_avalanche_size = 0
        toppling = True
        
        # STEP 2 & 3: Relaxation loop (Avalanche)
        # Repeat until no cell is above F_CRIT [cite: 69]
        while toppling:
            # Find unstable cells
            unstable_indices = np.argwhere(grid >= F_CRIT)
            
            if len(unstable_indices) == 0:
                toppling = False
                break
            
            # Count them for earthquake magnitude
            step_avalanche_size += len(unstable_indices)
            
            # Create a temporary grid for redistribution (helper matrix) [cite: 17]
            transfer_grid = np.zeros((N, N))
            
            for (r, c) in unstable_indices:
                # Calculate amount to transfer (25% of current value) [cite: 63]
                # Note: If alpha=0.25 and 4 neighbors, the system is conservative within the grid.
                transfer_amount = grid[r, c] * ALPHA 
                
                # Distribute to neighbors (Up, Down, Left, Right)
                neighbors = [
                    (r-1, c), (r+1, c), (r, c-1), (r, c+1)
                ]
                
                for nr, nc in neighbors:
                    # Check boundaries (Non-periodic/Open boundaries)
                    if 0 <= nr < N and 0 <= nc < N:
                        transfer_grid[nr, nc] += transfer_amount
                
                # Reset the unstable cell to 0 [cite: 65]
                grid[r, c] = 0

            # Add the distributed energy to the main grid [cite: 67]
            grid += transfer_grid
            
            # Any cell that received energy might now be unstable, so the loop continues.

        # Record data
        if step_avalanche_size > 0:
            avalanche_sizes.append(step_avalanche_size)
            time_series.append(step_avalanche_size)
        else:
            time_series.append(0)

    # Plotting results
    plt.figure(figsize=(12, 5))

    # Plot 1: Activity over time
    plt.subplot(1, 2, 1)
    plt.plot(time_series, color='red', linewidth=0.5)
    plt.title("Seismic Activity vs Time (OFC Model)")
    plt.xlabel("Time Steps")
    plt.ylabel("Magnitude (Cells Toppled)")

    # Plot 2: Frequency Distribution (Gutenberg-Richter Law)
    plt.subplot(1, 2, 2)
    # Filter out zeros for the histogram
    nonzero_avalanches = [x for x in avalanche_sizes if x > 0]
    if nonzero_avalanches:
        plt.hist(nonzero_avalanches, bins=30, color='orange', log=True)
        plt.title("Earthquake Frequency Distribution")
        plt.xlabel("Size")
        plt.ylabel("Frequency (Log Scale)")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_ofc_simulation()