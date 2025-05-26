# Vector Calculus - Python Visualization Project

This project contains a comprehensive collection of Python scripts for anyone going through the Vectorial Calculus course _(or any course that includes the extra topics outside of pure vectorial calc)_, helpful for visualizing and understanding vector calculus concepts (Plus a Fourier Series analysis example). The scripts are organized into four main topics (T1-T4) that progressively build upon each other to cover the fundamental concepts of vector calculus.

## Project Structure

```
Calculo vectorial/
├── T1/                 # Vectors in Space
├── T2/                 # Plane Curves, Parametric Equations and Polar Coordinates
├── T3/                 # Vector Functions of a Real Variable
├── T4/                 # Multivariable Real Functions
├── Fourier_Series.py   # Fourier Series Analysis
└── Least_Squares.py    # Least Squares Method Implementation
```

## Requirements

To run these scripts, you'll need the following Python packages:

- `matplotlib` - For plotting and visualization
- `numpy` - For numerical computations
- `tabulate` - For formatting data tables
- `sympy` - For symbolic mathematics (T4)
- `mpl_toolkits` - For 3D plotting

Install the requirements using:

```bash
pip install matplotlib numpy tabulate sympy
```

## Topic 1 (T1): Vectors in Space

This section covers fundamental vector operations and visualization in 2D and 3D space.

### Scripts Description:

- **`simple_line_2D.py`**: Basic 2D line plotting with parametric equations. Demonstrates how to create and visualize lines in 2D coordinate systems with grid configuration.

- **`simple_line_3D.py`**: Extension to 3D space with parametric line equations. Includes coordinate axis visualization with arrows and comprehensive point plotting along parametric curves.

- **`practica_T1.py`**: Practice exercises demonstrating multiple vector operations. Shows two different vectors from the same starting point with parametric and symmetric equations.

- **`programa_en_clase.py`**: In-class programming examples for 2D coordinate systems. Features custom axis configuration with arrow-style coordinate axes.

- **`programa_en_clase_2.py`**: Extended in-class examples with table generation for parametric equations and enhanced axis styling.

- **`simple_surface.py`**: Introduction to 3D surface plotting. Demonstrates coordinate axis visualization with colored arrows (red for x, green for y, blue for z axes).

- **`simple_surface_ramses.py`**: Advanced surface plotting with vectors and planes. Includes point and vector visualization on 3D surfaces.

- **`line3D_tabla_corregida.py`**: Corrected 3D line implementation with data tables. Features comprehensive tabulation of parametric coordinates.

- **`plot_2D_point.py`**: Basic point plotting in 2D coordinates. Fundamental script for understanding coordinate system setup.

- **`nuevo2D.py`**: New 2D plotting techniques and Taylor series examples. Demonstrates multiple point plotting with scatter plots.

- **`T3_ejercicio1.py`**: Advanced 3D parametric curve visualization. Creates helical curves using `<sin(t), cos(t), t>` with vector field representation.

## Topic 2 (T2): Plane Curves, Parametric Equations and Polar Coordinates

This section focuses on parametric curves, polar coordinates, and animated visualizations.

### Scripts Description:

- **`parametric_parabola.py`**: Static parametric parabola visualization. Demonstrates basic curve plotting with data tabulation and coordinate point analysis.

- **`animated_parametric_parabola.py`**: Animated version of parametric parabola. Features frame-by-frame animation with coordinate tracking and annotation overlays.

- **`animated_parametric_tangent.py`**: Advanced animation showing parametric curves with tangent lines. Displays moving tangent lines and slope calculations at each point.

- **`grafica_en_clase.py`**: Class exercise for parametric curves. Implements specific mathematical functions like `x(t) = 8t^(3/2)` and `y(t) = 3 + (8-t)^(3/2)`.

- **`polar_rectangular.py`**: Polar to rectangular coordinate conversion. Demonstrates the relationship between polar and Cartesian coordinate systems.

- **`polar_rectangular_subplot_animated.py`**: Dual-view animation showing both polar and rectangular representations simultaneously. Features synchronized plotting in both coordinate systems.

- **`simple_parametric_with_tangent.py`**: Parametric curves with tangent line analysis. Shows tangent vectors and their geometric interpretation.

- **`animated_practice_parabola.py`**: Practice animation for understanding parametric motion along parabolic paths.

### Exercise Bank (Banco_de_ejercicios/):

- **`P1.1_banco_de_ejercicios.py`** and **`P1.2_banco_de_ejercicios.py`**: Problem set 1 focusing on basic parametric equations.

- **`P2.1_banco_ejercicios.py`** and **`P2.2_banco_ejercicios.py`**: Problem set 2 covering intermediate parametric curve analysis.

- **`P3.1_banco_ejercicios.py`** and **`P3.2_banco_ejercicios.py`**: Problem set 3 dealing with polar coordinate transformations.

- **`P4_banco_ejercicios.py`**: Advanced problems combining parametric and polar coordinate concepts.

## Topic 3 (T3): Vector Functions of a Real Variable

This section explores vector-valued functions and their properties including tangent vectors and derivatives.

### Scripts Description:

- **`vector_function_tangent_1.py`**: Main script for vector function analysis. Demonstrates 3D parametric curves with tangent line calculations and comprehensive coordinate tabulation.

- **`Ejercicio1_1.py`**: Exercise demonstrating linear parametric functions `x(t) = t-2, y(t) = t²+1`. Includes tangent line visualization at specific parameter values.

- **`Ejercicio1_2.py`**: Polynomial parametric functions `x(t) = t², y(t) = t³`. Shows tangent line calculation using derivative methods.

- **`Ejercicio1_3.py`**: Trigonometric parametric functions `x(t) = sin(t), y(t) = 2cos(t)`. Demonstrates elliptical curves with tangent analysis.

- **`Ejercicio1_4.py`**: Exponential parametric functions `x(t) = e^(2t), y(t) = e^t`. Features exponential curve behavior with tangent vectors.

- **`Ejercicio3_1.py`**: 3D vector function `r(t) = <t²+3t, t²+1, 3t+4>`. Shows 3D parametric curves with tangent line calculations.

- **`Ejercicio3_2.py`**: 3D trigonometric vector function `r(t) = <cos(t), 3t, 2sin(2t)>`. Demonstrates periodic behavior in 3D space.

- **`Ejercicio3_3.py`**: Advanced 3D function `r(t) = <sin²(t), cos²(t), tan²(t)>`. Shows complex trigonometric relationships.

- **`Ejercicio4_1.py`**: Mixed function types `r(t) = <1+2√t, t³-t, t³+t>`. Combines polynomial and root functions.

- **`Ejercicio4_2.py`**: Exponential vector functions `r(t) = <e^t, te^t, te^(t²)>`. Shows exponential growth in multiple dimensions.

- **`Ejercicio_de_clase.py`**: Class exercise combining multiple function types `r(t) = <1+t³, te^(-t), sin(2t)>`. Demonstrates mixed analytical approaches.

## Topic 4 (T4): Multivariable Real Functions

This section covers multivariable calculus including directional derivatives, gradient vectors, and tangent planes.

### Scripts Description:

- **`programa_potente.py`**: Comprehensive multivariable function analyzer. This powerful script includes:
  - **Directional Derivative Calculation**: Computes directional derivatives using gradient vectors and unit direction vectors
  - **Gradient Vector Visualization**: Shows gradient vectors at specific points on surfaces
  - **Tangent Plane Generation**: Creates tangent planes to surfaces at given points
  - **3D Surface Plotting**: Visualizes multivariable functions as 3D surfaces
  - **Vector Field Representation**: Displays normal vectors and directional vectors
  - **Coordinate Analysis**: Provides detailed tabulation of parametric line coordinates
  - **Symbolic Mathematics**: Uses SymPy for exact derivative calculations

## Fourier Series Module

- **`Fourier_Series.py`**: Standalone module for Fourier series analysis and visualization. Demonstrates periodic function decomposition and harmonic analysis.

## Least Squares Method

- **`Least_Squares.py`**: Traditional least squares implementation for linear regression analysis. Calculates coefficients for the equation y = ax + b using the classical formulas. Features both predefined datasets and custom data input options, with step-by-step calculation display and prediction capabilities.

## Key Features

### Visualization Capabilities:

- **3D Surface Plotting**: Advanced surface visualization with color mapping
- **Parametric Curve Animation**: Frame-by-frame animation of curve generation
- **Vector Field Visualization**: Arrow-based representation of vector fields
- **Coordinate System Display**: Custom axis styling with arrows and grids
- **Tangent Line Analysis**: Real-time tangent vector calculation and display

### Mathematical Analysis:

- **Parametric Equations**: Comprehensive support for parametric representations
- **Derivative Calculations**: Automatic computation of tangent vectors and derivatives
- **Coordinate Transformations**: Polar to rectangular coordinate conversion
- **Symbolic Mathematics**: Integration with SymPy for exact calculations
- **Data Tabulation**: Formatted output of coordinate values and parameters

### Interactive Elements:

- **Animation Controls**: Frame-by-frame progression with coordinate tracking
- **Multi-view Displays**: Simultaneous polar and rectangular coordinate visualization
- **Real-time Annotations**: Dynamic coordinate and parameter display
- **Customizable Parameters**: Easy modification of mathematical functions and ranges

## Usage Instructions

1. **Run Individual Scripts**: Each script can be executed independently to explore specific concepts.

   ```bash
   python T1/simple_line_3D.py
   ```

2. **Modify Parameters**: Most scripts include easily configurable parameters at the top of the file for customization.

3. **Study Progression**: Follow the topics in order (T1 → T2 → T3 → T4) for a complete understanding of vector calculus concepts.

4. **Animation Controls**: For animated scripts, use standard matplotlib controls to pause, play, and navigate through frames.

## Educational Objectives

This project serves as a comprehensive learning tool for:

- Understanding vector operations in 2D and 3D space
- Visualizing parametric equations and their geometric interpretations
- Exploring the relationship between polar and rectangular coordinates
- Analyzing vector-valued functions and their derivatives
- Investigating multivariable functions and their properties
- Developing intuition for calculus concepts through visual representation

## Contributing

To extend this project:

1. Follow the existing naming conventions (`Ejercicio#_#.py` for exercises)
2. Include comprehensive comments explaining mathematical concepts
3. Provide data tabulation for numerical analysis
4. Use consistent visualization styling across scripts
5. Include both static and animated versions where appropriate

## License

This educational project is designed for learning vector calculus concepts through computational visualization and interactive analysis.
