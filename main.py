import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize

# Profits
def f1(xy):          # Profit of wheat
    x, y = xy
    return 2*x**2 + 3*x*y - y**2
def f2(xy):          # Profit of barley
    x, y = xy
    return x**2 - 4*x*y + 5*y**2
def f(xy):           # Total profit
    return f1(xy) + f2(xy)
def f_maximize(xy):  # Maximised total profit
    return -(f1(xy) + f2(xy))

# Constrainst
def contrainst1(xy):   # x + y <= 50
    x, y = xy
    return 50 - (x+y)
def contrainst2(xy):   # xy <= 600
    x, y = xy
    return 600 - (x*y)
def contrainst3(xy):   # y > x^2/50 +2
    x, y = xy
    return y-(x**2)/50-2

# Input bounds
def get_bounds():
    x_min = int(input("x_min = "))
    x_max = int(input("x_max = "))
    y_min = int(input("x_min = "))
    y_max = int(input("y_max = "))
    return ((x_min, x_max), (y_min, y_max))

# Displaying the profit function in 3D
def display_function_3d(x_bounds, y_bounds):
    x = np.linspace(x_bounds[0], x_bounds[1], 100)
    y = np.linspace(y_bounds[0], y_bounds[1], 100)
    
    X, Y = np.meshgrid(x, y)
    
    Z = f((X, Y))
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot_surface(X, Y, Z, cmap='viridis')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('f(X, Y)')
    ax.set_title('Graphique de la fonction f')
    
    plt.show()

# Displaying the profit function in 2D with the constrainsts
def display_function_2d_constrainsts(x_bounds, y_bounds, solution):
    x = np.linspace(x_bounds[0], x_bounds[1], 400)
    y = np.linspace(y_bounds[0], y_bounds[1], 400)
        
    X, Y = np.meshgrid(x, y)
    
    Z = f((X, Y))

    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar(label="Objective function")

    plt.plot(x, 600 / x, label='xy <= 600', color='red')  # Area constraint
    plt.plot(x, 50 - x, label='x + y <= 50', color='blue')  # Perimeter constraint
    plt.plot(x, x**2 / 50 + 2, label='y > x^2/50 + 2', color='green')  # Nonlinear constraint
    
    plt.plot(solution[0], solution[1], 'ro')

    plt.xlim(x_bounds)
    plt.ylim(y_bounds)
    plt.xlabel('x (width)')
    plt.ylabel('y (height)')
    plt.legend()
    plt.title('Feasible Region and Objective Function')
    plt.show()
    
# Calculating the solution
def calculate_solution(x_bounds, y_bounds):
    constraints = [
        {'type': 'ineq', 'fun': contrainst1},
        {'type': 'ineq', 'fun': contrainst2},
        {'type': 'ineq', 'fun': contrainst3}
    ]

    # Minimez function from SLSQP module
    result = minimize(f_maximize, [10,10], method='SLSQP', bounds=[x_bounds, y_bounds], constraints=constraints)

    if result.success:
        print("Optimal solution found:")
        print(f"x = {result.x[0]:.2f}, y = {result.x[1]:.2f}")
        print(f"Maximized profit = {-result.fun:.2f}")
        return result.x
    else:
        print("Optimization failed:", result.message)
        return False



if __name__ == "__main__":
    x_bounds, y_bounds = get_bounds()
    display_function_3d(x_bounds, y_bounds)
    display_function_2d_constrainsts(x_bounds, y_bounds, calculate_solution(x_bounds, y_bounds))