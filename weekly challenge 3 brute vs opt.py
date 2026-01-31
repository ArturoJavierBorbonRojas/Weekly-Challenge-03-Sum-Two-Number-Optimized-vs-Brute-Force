import numpy as np
import matplotlib.pyplot as plt

# Weekly challenge 3: Sum two number optimized vs brute force.
# Author: Ing. Arturo Javier Borbon Rojas.

# 1 Define function two sum optimal
def two_sum_optimal(nums, target):
    seen = {}
    counter = 0
    for i, num in enumerate(nums):
        counter += 1
        complement = target - num
        if complement in seen:
            return counter #  Just return the number of attemps!
        seen[num] = i
    return counter #  If return 0, return just the number of attempts

# 2 Def function brute force sum two numbers
def brute_two_value(nums, target):
    counter = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            counter += 1
            if nums[i] + nums[j] == target:
                return counter # Just return the number of attempts 
    return counter

# 3 Generate conditions of simulation
# 50 simulation data. Empty lists to save data to plot.
list_n= []
brute_attempts= []
opt_attempts= []
print("Simulating 50 events...")

# 4 Start for simulation
for _ in range(50):
 
 # 5 Generate pseudo random values:
 # 5.1 number of elements
 n=np.random.randint(0,100)
 # 5.2 Set a random objective value 
 objective_value= np.random.randint(0,100)
 # 5.3 Set a random list with n elements
 value1= np.random.randint(0,100,n)

 # 6 Print our pseudo random values
 print("Simulaion: ", _)
 print("------------------")
 print(" Our pseudo random values")
 print("Our objective value is: ", objective_value)
 print(f"The pseudo random list is:{value1} with n={n} objects")
 print("------------------")

 # 7 save n's
 list_n.append(n)

 # 8 Execute function
 print("Optimized method: ",opt_attempts.append((two_sum_optimal(value1, objective_value))))
 print("Bruce force method: ", brute_attempts.append(brute_two_value(value1, objective_value)))


# 9 Graph

# 9.1 Brute force: Graph type
plt.scatter(list_n, brute_attempts, color="red", label="Brute Force O(n^2)" )

# 9.2 Optimized: Graph type
plt.scatter(list_n, opt_attempts, color="green", label="Optimized O(n)")

# 9.3 Label
plt.title("Brute Force vs Optimized")
plt.xlabel("Values of n")
plt.ylabel("Values of attempts")
plt.grid(True)
plt.legend()

# 9.4 Axes limits
plt.xlim(0,100)
plt.ylim(0, max(brute_attempts)+10)

# 9.5 Show graph
plt.show()


