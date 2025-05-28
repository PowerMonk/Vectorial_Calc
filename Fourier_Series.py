import numpy as np
import matplotlib.pyplot as plt

def fourier_series(x, a0, an, bn, n_terms=None):
    """
    Calcula la serie de Fourier en los puntos x.
    
    Parámetros:
    - x: Valores de x donde calcular la serie
    - a0: Coeficiente constante
    - an: Lista de coeficientes para los términos coseno
    - bn: Lista de coeficientes para los términos seno
    - n_terms: Número de términos a usar
    """
    if n_terms is None:
        n_terms = min(len(an), len(bn))
    else:
        n_terms = min(n_terms, len(an), len(bn))
    
    # El término constante del inicio de la ecuación a0/2
    y = a0 / 2.0
    
    # Sumamos los términos de la serie
    for n in range(n_terms):
        # n va de 0 a n_terms-1. Para las funciones, usamos (n+1)
        y += an[n] * np.cos((n + 1) * x) + bn[n] * np.sin((n + 1) * x)
    
    return y

# Ejemplos predefinidos de coeficientes para funciones comunes
def get_predefined_coefficients(option, num_terms=10):
    """
    Devuelve coeficientes predefinidos para funciones comunes.
    """
    if option == 1:  # Onda cuadrada
        a0 = 0
        an = [0] * num_terms
        bn = [] 
        for k in range(1, num_terms + 1): # k representa n en la fórmula de Fourier (1, 2, 3... etc)
            if k % 2 != 0: 
                bn.append(4 / (np.pi * k))
            else: 
                bn.append(0)
        name = "Onda cuadrada"
    elif option == 2:  # Onda diente de sierra
        a0 = 0
        an = [0] * num_terms
        bn = [2/((k)*np.pi) * ((-1)**(k+1)) for k in range(1, num_terms+1)]
        name = "Onda diente de sierra"
    elif option == 3:  # Onda triangular (impar, seno)
        a0 = 0
        an = [0] * num_terms  # Todos los coeficientes de coseno son 0
        bn = []
        for k in range(1, num_terms + 1):
            if k % 2 != 0:  # Solo impares
                # Fórmula: (8 / (π² * k²)) * (-1)^((k - 1)/2)
                bn.append((8 / (np.pi**2 * k**2)) * ((-1)**((k - 1)/2)))
            else:
                bn.append(0)
        name = "Onda triangular"

    elif option == 4:  # Serie de Fourier de la clase 
        a0 = np.pi /4.0  # Para que a0/2 -> pi/4
        an = [((1 - (-1)**k) / ((k**2) * np.pi)) for k in range(1, num_terms + 1)]
        bn = [(1 / k) for k in range(1, num_terms + 1)]
        name = "Diente de sierra 'con valle' (vista en clase)"
    elif option == 5:  # Serie de Fourier de la clase v2 
        a0 = np.pi / 4.0  
        an = [((1 / (np.pi * k**2)) * ((-1)**k - 1)) for k in range(1, num_terms + 1)]
        bn = [(-(1 / k) * (-1)**k) for k in range(1, num_terms + 1)]
        name = "Diente de sierra con valle v2"
    else:
        a0 = 1
        an = [0] * num_terms
        bn = [0] * num_terms
        name = "Constante"
    
    return a0, an, bn, name

def main():
    print("=== CALCULADORA DE SERIES DE FOURIER ===")
    print("Serie de Fourier: f(x) = a₀/2 + Σ[aₙcos(nx) + bₙsin(nx)]")
    
    # Opciones para definir los coeficientes
    print("\nOpciones:")
    print("1. Ingresar coeficientes manualmente")
    print("2. Usar funciones predefinidas")
    option = input("Seleccione una opción (1/2): ")
    
    if option == "1":
        a0 = float(input("Ingrese el coeficiente a₀: "))
        
        n_terms = int(input("¿Cuántos términos de la serie desea usar? (No tantos, no queremos que explote la computadora): "))
        
        an = []
        bn = []
        
        print("\nIngrese los coeficientes aₙ (coseno):")
        for i in range(n_terms):
            an.append(float(input(f"a{i+1} (para cos({i+1}x)): ")))
        
        print("\nIngrese los coeficientes bₙ (seno):")
        for i in range(n_terms):
            bn.append(float(input(f"b{i+1} (para sin({i+1}x)): ")))
        
        function_name = "Función personalizada"
    
    else:
        # coeficientes predefinidos
        print("\nFunciones predefinidas:")
        print("1. Onda cuadrada")
        print("2. Onda diente de sierra")
        print("3. Onda triangular")
        print("4. Diente de sierra 'con valle' (vista en clase)")
        print("5. Diente de sierra con valle v2")
        
        func_option = int(input("Seleccione una función (1-5): "))
        n_terms = int(input("¿Cuántos términos desea usar? (Recomendado: 100-1000, pero no infinitos, no queremos que explote la computadora): "))
        
        a0, an, bn, function_name = get_predefined_coefficients(func_option, n_terms)

    # Crear puntos x para graficar (dos periodos)
    x = np.linspace(0, 4*np.pi, 1000)
    
    # Configuramps la figura para múltiples gráficos
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    fig.suptitle(f'Serie de Fourier: {function_name}', fontsize=16)
    
    # Gráfico 1 -> Serie de Fourier comoleta
    y_full = fourier_series(x, a0, an, bn)
    ax1.plot(x, y_full, 'b-')
    ax1.set_title(f'Serie de Fourier completa ({n_terms} términos)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.grid(True)
    ax1.set_xlim(0, 4*np.pi)
    
    # Gráfico 2 -> Aproximaciones con diferentes términos
    ax2.set_title('Aproximación con diferente número de términos')
    ax2.set_xlabel('x')
    ax2.set_ylabel('f(x)')
    ax2.grid(True)
    ax2.set_xlim(0, 4*np.pi)
    
    # Determinar los términos a mostrar
    if n_terms <= 4:
        terms_list = list(range(1, n_terms + 1))
    else:
        terms_list = [1, 3, 5, n_terms]
        if n_terms > 10:
            terms_list.insert(3, n_terms // 2)
    
    colors = ['g', 'r', 'c', 'm', 'y']
    for i, terms in enumerate(terms_list):
        if terms <= n_terms:
            y = fourier_series(x, a0, an, bn, terms)
            ax2.plot(x, y, color=colors[i % len(colors)], label=f'{terms} términos')
    
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()