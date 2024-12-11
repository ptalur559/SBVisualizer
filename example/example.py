import tellurium as te
import SBMLDiagrams as sb
from SBVisualizer.Visualizer import Visualizer  # Import your Visualizer class

# Create a simple Tellurium model (for demonstration purposes)
model_code = '''
model example_model
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
end
'''

# Load the model into Tellurium
r = te.loada(model_code)

# Create a Visualizer object
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

# Draw the model with the updated settings and save the image
output_file_name = 'model_output.png'
visualizer.draw(output_fileName=output_file_name, scale=500, k=60)

print(f"SBML model diagram saved as {output_file_name}")

