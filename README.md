# Weekly-Challenge-03-Sum-Two-Number-Optimized-vs-Brute-Force
This week is about evidence. I created a Python script to simulate and visualize the performance difference between a Brute Force approach ($O(n^2)$) and an **Optimized Hash Map** approach ($O(n)$) for the Two Sum problem.

# Complexity Analysis & Visualization

## Description
This week is about **evidence**. I created a Python script to simulate and visualize the performance difference between a **Brute Force** approach ($O(n^2)$) and an **Optimized Hash Map** approach ($O(n)$) for the Two Sum problem.

## The Simulation
Using `NumPy` for data generation and `Matplotlib` for visualization, the script:
1. Generates 50 random test cases with varying list sizes ($n$).
2. Runs both algorithms on the same datasets.
3. records the exact number of "attempts" (iterations) each algorithm needed.
4. Plots the results to visualize the Time Complexity.

## The Results
The generated graph clearly shows:
* Quadratic Growth ($O(n^2)$): The Brute Force method (Red) becomes exponentially slower as the input grows.
* Linear Growth ($O(n)$): The Optimized method (Green) maintains a low operation count regardless of input size.

## Code Snippet (Plotting)
python 3.14.2
Numpy
MatPlotLib

# Comparison logic
plt.scatter(lista_n, brute_attempts, color="red", label="Brute Force O(n^2)")
plt.scatter(lista_n, optimized_attempts, color="green", label="Optimized O(n)")
