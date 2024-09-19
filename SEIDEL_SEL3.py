import numpy as np

def gauss_seidel(A, b, x0, max_iterations=1000, tolerance=1e-6):
    n = len(A)
    x = x0.copy()
    iterations = []
    
    for iteration in range(max_iterations):
        x_old = x.copy()
        iterations.append(x_old)
        
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]
        
        if np.linalg.norm(x - x_old, ord=np.inf) < tolerance:
            iterations.append(x)
            return x, iterations
    
    iterations.append(x)
    return x, iterations

def check_diagonal_dominance(A):
    n = len(A)
    for i in range(n):
        if abs(A[i][i]) <= sum(abs(A[i][j]) for j in range(n) if j != i):
            return False
    return True

def calculate_convergence_indicator(A):
    n = len(A)
    alphas = []
    for i in range(n):
        alpha = sum(abs(A[i][j]) for j in range(n) if j != i) / abs(A[i][i])
        alphas.append(alpha)
    return alphas, max(alphas)

# Definir la matriz A y el vector b
A = np.array([
    [0.52, 0.3, 0.18],
    [0.2, 0.5, 0.3],
    [0.25, 0.2, 0.55]
])
b = np.array([4800, 5810, 5690])

print("Matriz A:")
print(A)
print("\nVector b:")
print(b)

# Verificar diagonal dominante
is_diag_dominant = check_diagonal_dominance(A)
print(f"\n1. La matriz {'tiene' if is_diag_dominant else 'no tiene'} diagonal predominante")

# Calcular indicador de convergencia
alphas, max_alpha = calculate_convergence_indicator(A)
print("\nIndicador de convergencia (alfa):")
for i, alpha in enumerate(alphas, 1):
    print(f"alfa{i} = {alpha:.9f}")
print(f"máximo = {max_alpha:.9f}")

print(f"\nEl sistema {'converge' if max_alpha < 1 else 'converge lentamente o no converge'}")

# Resolver usando Gauss-Seidel
x0 = np.zeros(3)
solution, iterations = gauss_seidel(A, b, x0, max_iterations=5, tolerance=1e-6)

print("\n3. Iteraciones:")
print("   {:^15} {:^15} {:^15}".format("x1", "x2", "x3"))
for i, x in enumerate(iterations):
    print(f"{i}  {x[0]:15.6f} {x[1]:15.6f} {x[2]:15.6f}")

print("\nErrores:")
print("   {:^15} {:^15} {:^15}".format("e1", "e2", "e3"))
for i in range(1, len(iterations)):
    errors = np.abs(iterations[i] - iterations[i-1])
    print(f"{i}  {errors[0]:15.9f} {errors[1]:15.9f} {errors[2]:15.9f}")

print("\nSolución final:")
print(f"x1 = {solution[0]:.6f}")
print(f"x2 = {solution[1]:.6f}")
print(f"x3 = {solution[2]:.6f}")