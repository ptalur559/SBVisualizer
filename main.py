from Visualizer import Visualizer
import tellurium as te
import sbmlnetwork
import SBMLDiagrams

r = te.loada("""
    J1: S1 -> S2; k1*S1;
    J2: S2 -> S3; k2*S2;
    S1 = 10; S2 = 0; S3 = 0; k1 = 0.1; k2 = 0.05;
""") 
visualizer = Visualizer(r)
visualizer.loadIntoSBML()

print(visualizer.get_fluxes())
print(visualizer.set_line_thickness('J1', 50))
print(visualizer.make_color_gradient())
print(visualizer.extract_rgb_values())

