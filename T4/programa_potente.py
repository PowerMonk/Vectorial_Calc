import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def calculate_directional_derivative(f, x0, y0, theta):
    """
    Calcula la derivada direccional de una función en un punto
    
    Parámetros:
    f: función simbolica
    x0, y0: coordenadas del punto
    theta: ángulo de la dirección
    
    Retorna:
    Derivada direccional, vector unitario, vector gradiente
    """
    # Calcular derivadas parciales en el punto
    x, y = sp.symbols('x y')
    
    # Convertir valores simbólicos a números
    fx = float(sp.diff(f, x).subs([(x, x0), (y, y0)]))
    fy = float(sp.diff(f, y).subs([(x, x0), (y, y0)]))
    
    # Vector unitario
    unit_vector = np.array([np.cos(theta), np.sin(theta), 
                             (fx * np.cos(theta) + fy * np.sin(theta))], dtype=float)
    unit_vector /= np.linalg.norm(unit_vector)
    
    # Calcular valor de la función en el punto
    z0 = float(f.subs([(x, x0), (y, y0)]))
    
    # Vector normal para el plano tangente
    normal_vector = np.array([fx, fy, -1], dtype=float)
    
    return unit_vector, normal_vector, z0, fx, fy

def generate_tangent_plane(x0, y0, z0, normal_vector):
    """
    Genera la ecuación del plano tangente
    
    Parámetros:
    x0, y0, z0: punto de tangencia
    normal_vector: vector normal al plano
    
    Retorna:
    Ecuación del plano
    """
    A, B, C = normal_vector
    D = -(A*x0 + B*y0 + C*z0)
    return A, B, C, D

# Función original simbólica
x, y = sp.symbols('x y')
f_sym = x**3 - 3*x*y + 4*y**2

# Convertir a función numérica para graficar
f = sp.lambdify([x, y], f_sym, 'numpy')

# Parámetros del problema
x0, y0 = 1, 2
theta = np.pi / 6

# Calcular derivada direccional y vectores
unit_vector, normal_vector, z0, fx, fy = calculate_directional_derivative(f_sym, x0, y0, theta)

# Punto original
p0 = np.array([x0, y0, z0])

# Generar plano tangente
plane_coeffs = generate_tangent_plane(x0, y0, z0, normal_vector)

# Valores para graficar
t_values = np.linspace(-10, 10, 50)
x_line = p0[0] + unit_vector[0] * t_values
y_line = p0[1] + unit_vector[1] * t_values
z_line = p0[2] + unit_vector[2] * t_values

# Crear malla para el plano tangente
xx, yy = np.meshgrid(np.linspace(-10, 10, 30), np.linspace(-10, 10, 30))
zz = (-plane_coeffs[0]*xx - plane_coeffs[1]*yy - plane_coeffs[3]) / plane_coeffs[2]

# Crear figura 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar superficie de la función
x_surf = np.linspace(-3, 3, 50)
y_surf = np.linspace(-3, 3, 50)
x_surf, y_surf = np.meshgrid(x_surf, y_surf)
z_surf = f(x_surf, y_surf)
ax.plot_surface(x_surf, y_surf, z_surf, color='cyan', alpha=0.5, rstride=100, cstride=100)

# Graficar punto original, línea direccional y plano tangente
ax.scatter(p0[0], p0[1], p0[2], color='blue', s=50, label="Punto original P0")
ax.plot(x_line, y_line, z_line, color='green', label="Línea direccional")
ax.plot_surface(xx, yy, zz, color='yellow', alpha=0.3)

# Graficar vectores
ax.quiver(p0[0], p0[1], p0[2], unit_vector[0], unit_vector[1], unit_vector[2], 
          color='red', length=5, label="Vector unitario")
ax.quiver(p0[0], p0[1], p0[2], normal_vector[0], normal_vector[1], normal_vector[2], 
          color='purple', length=5, label="Vector normal")

# Configuración de la gráfica
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-5, 20])
ax.legend()

# Tabulación de resultados
headers = ["t", "x", "y", "z"]
table = list(zip(t_values, x_line, y_line, z_line))
print("Tabla de valores paramétricos de la línea direccional:")
for row in table[:5]:  # Mostrar solo los primeros 5 para no saturar
    print(f"{row[0]:.3f}, {row[1]:.3f}, {row[2]:.3f}, {row[3]:.3f}")
print("...")

# Imprimir información adicional
print(f"\nPunto original: {p0}")
print(f"Vector unitario: {unit_vector}")
print(f"Vector normal: {normal_vector}")
print(f"Ecuación del plano tangente: {plane_coeffs[0]}x + {plane_coeffs[1]}y + {plane_coeffs[2]}z + {plane_coeffs[3]} = 0")

plt.show()