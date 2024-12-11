# SBVisualizer

Systems Biology Markup Language, or SBML, is a software model for biological reactions. SBVisualizer is a Python package for visualizing reaction fluxes in SBML models using SBMLDiagrams visualization. Flux of a reaction is illustrated with arrows of different thicknesses and colors, with thicker arrows representing a greater absolute value of flux and pure red representing positive flux, pure green representing 0 flux, and pure blue representing negative flux. The final output is a file with the diagram of each species and the flux arrows. 

# Installation
## Prerequisites - have these installed

1. tellurium
2. SBMLDiagrams
     
Install the package with:
`pip install SBVisualizer`

Most current version = 0.1.3

# How to Use 

Make sure you have these imports
```python
import tellurium as te
import SBMLDiagrams as sb
from SBVisualizer.Visualizer import Visualizer
```

Write the Antimony model and load it into tellurium

```python
r = te.loada('''
    // Reactions
    J1: A -> B; k1*A;
    J2: B -> C; k2*B;

    // Initial conditions
    A = 10;
    B = 2;
    C = 5;

    // Parameters
    k1 = 0.5;
    k2 = 0.3;
''')
```
Create the Visualizer object. From that, you can load into SBMLDiagrams, get reaction fluxes, line thicknesses, colors, and then set them, which will change them in SBML Diagrams. 

```python
visualizer = Visualizer(r)
# Load the SBML model
visualizer.loadIntoSBML()
# Get and print the fluxes
fluxes = visualizer.get_fluxes()
print("Fluxes:", fluxes)
# Set the line thickness based on fluxes
line_thicknesses = visualizer.get_line_thickness()
print("Line thicknesses:", line_thicknesses)
# Set the line thickness in the SBML model
visualizer.set_line_thickness(line_thicknesses)
# Set the colors based on fluxes
visualizer.set_colors()
```
Finally, you can draw the diagram (scaling it if needed) and see it in a file. 

```python
output_file_name = 'model_output.png'
visualizer.draw(output_fileName=output_file_name, scale=500, k=60)
```
<img width="294" alt="Screenshot 2024-12-10 at 6 34 58 PM" src="https://github.com/user-attachments/assets/4f27a8ef-c909-405e-86bf-c93c3a3fa3b4">

# Additional Notes

SBMLDiagrams is no longer supported, so there are some errors with changing the border color of the arrow. When the thickness is too big, the border hides the inside color of the arrow head, and therefore, the set color is not visible. Future work on this issue can include using `sbmlnetworks` with Spyder. 
