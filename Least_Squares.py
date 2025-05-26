
import numpy as np
from tabulate import tabulate

# Códigos de color ANSI para la consola
class Colors:
    GREEN = '\033[92m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def calculate_least_squares(x_values, y_values):
    """
    Calcula los coeficientes a y b para la ecuación y = ax + b
    usando el método de mínimos cuadrados tradicional.
    
    Fórmulas:
    a = (n*Σxy - Σx*Σy) / (n*Σx² - (Σx)²)
    b = (Σy - a*Σx) / n
    """
    n = len(x_values)
    
    # Calcular las columnas auxiliares
    xy_values = [x * y for x, y in zip(x_values, y_values)]
    x2_values = [x**2 for x in x_values]
    
    # Calcular las sumatorias
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_xy = sum(xy_values)
    sum_x2 = sum(x2_values)
    
    # Mostrar tabla de cálculos
    print("\nTabla de cálculos:")
    headers = ["x", "y", "xy", "x²"]
    table_data = list(zip(x_values, y_values, xy_values, x2_values))
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
    
    # Mostrar sumatorias
    print(f"\nSumatorias:")
    print(f"n = {n}")
    print(f"Σx = {sum_x}")
    print(f"Σy = {sum_y}")
    print(f"Σxy = {sum_xy}")
    print(f"Σx² = {sum_x2}")
    
    # Calcular coeficientes
    # a = (n*Σxy - Σx*Σy) / (n*Σx² - (Σx)²)
    numerator_a = n * sum_xy - sum_x * sum_y
    denominator_a = n * sum_x2 - (sum_x)**2
    a = numerator_a / denominator_a
    
    # b = (Σy - a*Σx) / n
    b = (sum_y - a * sum_x) / n
    print(f"\nCálculo de coeficientes:")
    print(f"a = (n*Σxy - Σx*Σy) / (n*Σx² - (Σx)²)")
    print(f"a = ({n}*{sum_xy} - {sum_x}*{sum_y}) / ({n}*{sum_x2} - ({sum_x})²)")
    print(f"a = ({numerator_a}) / ({denominator_a})")
    print(f"{Colors.GREEN}{Colors.BOLD}a = {a:.6f}{Colors.RESET}")
    
    print(f"\nb = (Σy - a*Σx) / n")
    print(f"b = ({sum_y} - {a:.6f}*{sum_x}) / {n}")
    print(f"{Colors.GREEN}{Colors.BOLD}b = {b:.6f}{Colors.RESET}")
    
    return a, b

def use_predefined_dataset():
    """Usa el dataset hardcodeado con datos de matrícula"""
    print("=== DATASET PRECARGADO ===")
    print("Datos de matrícula por año:")
    
    # Dataset hardcodeado
    x_values = [15, 16, 17, 18, 19, 20, 21, 22, 23]  # Años (2015-2023)
    y_values = [305, 340, 338, 385, 410, 300, 319, 365, 382]  # Matrícula
    
    print("Años: 2015-2023")
    print("x (codificado):", x_values)
    print("y (matrícula):", y_values)
    
    a, b = calculate_least_squares(x_values, y_values)
    print(f"\n=== ECUACIÓN DE LA RECTA ===")
    print(f"{Colors.GREEN}{Colors.BOLD}y = {a:.6f}x + {b:.6f}{Colors.RESET}")
    
    # Predicción para 2025 (x = 25)
    x_2025 = 25
    y_2025 = a * x_2025 + b
    print(f"\n=== PREDICCIÓN PARA 2025 ===")
    print(f"Para el año 2025 (x = {x_2025}):")
    print(f"Matrícula esperada = {a:.6f} * {x_2025} + {b:.6f}")
    print(f"Matrícula esperada = {y_2025:.2f} estudiantes")

def load_custom_dataset():
    """Permite al usuario cargar su propio dataset"""
    print("=== CARGAR DATASET PERSONALIZADO ===")
    
    try:
        n = int(input("Ingrese el número de puntos de datos (n): "))
        
        if n <= 0:
            print("Error: n debe ser mayor que 0")
            return
        
        x_values = []
        y_values = []
        
        print(f"\nIngrese {n} pares de valores (x, y):")
        for i in range(n):
            print(f"Punto {i+1}:")
            x = float(input(f"  x[{i+1}]: "))
            y = float(input(f"  y[{i+1}]: "))
            x_values.append(x)
            y_values.append(y)
        
        print(f"\nDatos ingresados:")
        print(f"x: {x_values}")
        print(f"y: {y_values}")
        
        a, b = calculate_least_squares(x_values, y_values)
        print(f"\n=== ECUACIÓN DE LA RECTA ===")
        print(f"{Colors.GREEN}{Colors.BOLD}y = {a:.6f}x + {b:.6f}{Colors.RESET}")
        
        # Opción para hacer predicción
        predict = input("\n¿Desea hacer una predicción? (s/n): ").lower()
        if predict == 's' or predict == 'si':
            x_pred = float(input("Ingrese el valor de x para la predicción: "))
            y_pred = a * x_pred + b
            print(f"Para x = {x_pred}, y predicho = {y_pred:.6f}")
            
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos")
    except Exception as e:
        print(f"Error inesperado: {e}")

def main():
    """Función principal del programa"""
    print("=" * 60)
    print("         MÉTODO DE MÍNIMOS CUADRADOS")
    print("         Cálculo de y = ax + b")
    print("=" * 60)
    
    while True:
        print("\nSeleccione una opción:")
        print("1. Usar dataset precargado (matrícula 2015-2023)")
        print("2. Cargar dataset personalizado")
        print("3. Salir")
        
        try:
            option = input("\nIngrese su opción (1, 2 o 3): ").strip()
            
            if option == "1":
                use_predefined_dataset()
            elif option == "2":
                load_custom_dataset()
            elif option == "3":
                print("\n¡Gracias por usar el programa!")
                break
            else:
                print("Opción no válida. Por favor seleccione 1, 2 o 3.")
                
            # Preguntar si desea continuar
            if option in ["1", "2"]:
                continue_program = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
                if continue_program not in ['s', 'si']:
                    print("\n¡Gracias por usar el programa!")
                    break
                    
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()