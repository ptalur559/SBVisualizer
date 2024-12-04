import tellurium as te
import sbmlnetwork
import SBMLDiagrams
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

# Build a simple model
r = te.loada("""
    J1: S1 -> S2; k1*S1;
    J2: S2 -> S3; k2*S2;
    S1 = 10; S2 = 0; S3 = 0; k1 = 0.1; k2 = 0.05;
""")

# Load SBML into sbmlnetwork
sb = sbmlnetwork.load(r.getSBML())

# Set basic styles
sb.setReactionsLineWidth(4)
sb.setSpeciesFillColor('yellow')

# Customize specific styles
sb.setLineWidth('J1', 3)
sb.setLineWidth('J2', 3)
sb.setLineColor('J1', 'blue')
sb.setLineColor('J2', 'darkblue')

# Save the styled SBML model
styled_sbml_path = "styled_model.sbml"
sb.save(styled_sbml_path)  # Save the styled SBML

# Load and visualize the styled SBML using SBMLDiagrams
diagram = SBMLDiagrams.load(styled_sbml_path)

# Save the diagram as a PNG image
output_png_path = "styled_network.png"
diagram.draw(output_fileName=output_png_path)

# Embed the PNG image into a PDF
output_pdf_path = "styled_network.pdf"
with PdfPages(output_pdf_path) as pdf:
    img = plt.imread(output_png_path)
    plt.figure(figsize=(8, 6))
    plt.imshow(img)
    plt.axis('off')  # Turn off axes for clean display
    pdf.savefig()  # Save the current figure to the PDF
    plt.close()


