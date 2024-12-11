# SBVisualizer

Systems Biology Markup Language, or SBML, is a software model for biological reactions. SBVisualizer is a Python package for visualizing reaction fluxes in SBML models using SBMLDiagrams visualization. Flux of a reaction is illustrated with arrows of different thicknesses and colors, with thicker arrows representing a greater absolute value of flux and pure red representing positive flux, pure green representing 0 flux, and pure blue representing negative flux. The final output is a file with the diagram of each species and the flux arrows. 

# Installation
## Prerequisites - have these installed

1. tellurium
2. SBMLDiagrams
     
Install the package with:
`pip install SBVisualizer`

# How to Use 

Make sure you have these imports
```python
import tellurium as te
import SBMLDiagrams as sb
from SBVisualizer.Visualizer import Visualizer 

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


