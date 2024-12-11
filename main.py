from SBVisualizer.Visualizer import Visualizer
import tellurium as te 
import SBMLDiagrams
# Build a simple model
r = te.loada("""
    J1: S1 -> S2; k1*S1;
    J2: S2 -> S3; k2*S2;
    S1 = 10; S2 = 0; S3 = 0; k1 = 0.1; k2 = 0.05;
""")
sb = SBMLDiagrams.load(r.getSBML())
# sb.setReactionFillColor ('J1', 'red')
# sb.setReactionArrowHeadFillColor('J1', 'red')
# sb.setReactionLineThickness('J1', 15)
# sb.draw(output_fileName = 'fileName.pdf')

# Debugging code to check SBMLDiagrams initialization
# visualizer = Visualizer(r)
# visualizer.loadIntoSBML()
# print("SBMLDiagrams instance:", visualizer.sb)  # Verify if SBMLDiagrams is loaded
# line_thicknesses = visualizer.get_line_thickness('J1', 50)
# visualizer.set_line_thickness(line_thicknesses)
# visualizer.set_colors()
# sb.draw(output_fileName = 'fileName1.pdf')

visualizer = Visualizer(r)
visualizer.loadIntoSBML()
# print("SBMLDiagrams instance:", visualizer.sb)  # Verify if SBMLDiagrams is loaded
line_thicknesses = visualizer.get_line_thickness()
visualizer.set_line_thickness(line_thicknesses)

# Generate the color dictionary using get_color_gradient
colors_dict = visualizer.get_color_gradient()

# Apply colors
visualizer.set_colors()

# Debug: Check reaction colors
# for rxn_name in colors_dict.keys():  # Now colors_dict is explicitly defined
#     try:
#         color = visualizer.sb.getReactionFillColor(rxn_name)
#         print(f"Reaction {rxn_name} color: {color}")
#     except AttributeError:
#         print(f"Could not fetch color for reaction: {rxn_name}")

visualizer.draw(output_fileName='fileName2.pdf')
# #visualizer.sb.draw(output_fileName='test_manual_color.pdf')

# # visualizer.sb.setReactionFillColor('J1', '#FF0000')  # Set red
# # visualizer.sb.draw(output_fileName='test_manual_color.pdf')








