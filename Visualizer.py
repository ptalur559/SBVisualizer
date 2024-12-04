# How to test plots
# have the plot function return data
# ex. histogram function in numpy that returns arrays
# smoke test - does it throw an exception?
# if there is no data to return
# if is_plot is True - shows the plot
# if false - doesn't show the plot


# Write program to change thickness of lines
# Set the flux of one species and the rest of the species follow
# Get the fluxes of all the species
# Set the line thickness of one of the fluxes
  # the other ones scale to that one
import SBMLDiagrams
class Visualizer:
  # Initializer
  # Attributes: r
  def __init__(self, r=None, colors=None):
    # assume that r = teloada already happened
    self.r = r
    self.colors = colors if colors is not None else {}
    self.line_thickness = {}

  # Loads into SBML
  def loadIntoSBML(self):
    # loads in to SBML
    sbml = self.r.getSBML()
    self.df = SBMLDiagrams.load(sbml)
    self.df.autolayout()

  # Get fluxes
  # returns a dict: key-species, value-flux
  def get_fluxes(self)->dict:
    # Get the fluxes of all the species
    fluxes = {} # Rxn name:flux
    reaction_ids = self.r.getReactionIds()
    rxn_rates = self.r.getReactionRates()
    fluxes = {rxn: rate for rxn, rate in zip(reaction_ids, rxn_rates)}
    return fluxes

  def set_line_thickness(self, rxn_name:str, thickness):
    # User picks a species flux to change the line width of
    # scales all the other fluxes
    # proportionality constant
    # returns a dict of all line thicknesses for each species
    fluxes = self.get_fluxes()
    # example: if flux = 50, thickness is 5
    prop_constant = thickness / fluxes[rxn_name]
    for rxn in fluxes:
      self.line_thickness[rxn] = fluxes[rxn] * prop_constant
    return self.line_thickness

#   def set_colors(self, species, color) -> dict:
#     # User sets colors for each species
#     # Need to figure out how to do the color gradient
#     self.colors[species] = color

  def autolayout(self):
    self.df.autolayout()
    self.update_lines()

#   def draw(self):
#     self.figure, self.ax = plt.subplots()


#     # Drawing the species as circles
#     for species in self.df.getSpecies():
#       species_id = species.getIdentifier()
#       x, y = positions[species_id]
#       self.ax.plot(x, y, 'o', label=species_id)
#       self.ax.text(x, y, species_id, ha='center', color='black')

#     # Drawing the rxn arrows
#     for rxn in self.df.getReactions():
#       rxn_id = rxn.getIdentifier()
#       reactants = rxn.getReactants()
#       products = rxn.getProducts()

#       for reactant in reactants:
#         reaction_id = reactant.getSpecies()
#         rx, ry = positions[reaction_id]

#         for product in products:
#           product_id = product.getSpecies()
#           px, py = positions[product_id]

#           line_width = self.line_thickness.get(rxn_id, 1)  # Default to 1 if not set
#           color = self.colors.get(rxn_id, "blue")

#           self.ax.annotate("",
#                     xy=(px, py), xycoords='data',
#                     xytext=(rx, ry), textcoords='data',
#                     arrowprops=dict(arrowstyle="->", color="blue", lw=line_width))

#     plt.show()


  def update_lines(self):
    for line in self.df.lines:
      if line.species in self.line_thickness:
        line.thickness = self.line_thickness[line.species]

        
  # Decide on the color scheme for fluxes
  # Positive flux color gradient - Green (low) to red (high)
  # Negative flux color gradient - Green (low) to blue (high)
  # Take the system and find the max flux

  def make_color_gradient(self):
    fluxes = self.get_fluxes() # dict
    abs_fluxes = [abs(value) for value in fluxes.values()]
    max_flux = max(abs_fluxes)

    pos_fluxes =[]
    neg_fluxes = []

    colors_dict = {}

    for flux in fluxes.values():
      # Positive and 0 flux
      if flux >= 0:
        factor = flux / max_flux
        rgb_vector = (255 * factor, 255 * (1 - factor), 0)   

      # Negative flux
      else:
        factor = abs(flux) / max_flux
        rgb_vector = (0, 255 * (1-factor), 255 * factor)
      colors_dict[flux] = rgb_vector
    return colors_dict

  def extract_rgb_values(self, rxn_name: str):
    """
    Extracts the RGB values for a single reaction from a color gradient.
    Args:
        rxn_name (str): The name of the reaction to extract RGB values for.
    Returns:
        tuple: A tuple containing the (red, green, blue) values for the specified reaction.
    """
    colors_dict = self.make_color_gradient()  
    if rxn_name not in colors_dict:
        raise ValueError(f"Reaction '{rxn_name}' not found in the color gradient.")   
    red_character, green_character, blue_character = colors_dict[rxn_name]
    return red_character, green_character, blue_character
  
  def rgb_to_hex(self):
    r, g, b = self.extract_rgb_values()
    if any(not (0 <= val <= 255) for val in (r, g, b)):
        raise ValueError("RGB values must be in the range 0-255")

    return f'#{r:02X}{g:02X}{b:02X}'