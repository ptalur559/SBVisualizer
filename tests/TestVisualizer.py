import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import unittest
from unittest.mock import MagicMock
from SBVisualizer.Visualizer import Visualizer
import tellurium as te
import SBMLDiagrams as sb

class TestVisualizer(unittest.TestCase):
    def setUp(self):
        """Set up a mock model and Visualizer instance for testing."""
        self.r = te.loada('''
            J1: S1 -> S2; k1*S1
            J2: S2 -> S3; k2*S2
            J3: S3 -> S4; k3*S3
            J4: S4 -> S1; k4*S4
            S1 = 10
            S2 = 5
            S3 = 2
            S4 = 1
            k1 = 0.5
            k2 = 0.2
            k3 = -0.1
            k4 = 0.4
        ''')
        self.visualizer = Visualizer(r=self.r)
        self.visualizer.loadIntoSBML()

    def test_get_fluxes(self):
        """Test that get_fluxes correctly retrieves reaction fluxes."""
        reaction_ids = self.r.getReactionIds()
        reaction_fluxes = self.r.getReactionRates()
        # Create a dictionary for fluxes
        expected_fluxes = {reaction: flux for reaction, flux in zip(reaction_ids, reaction_fluxes)}
        fluxes = self.visualizer.get_fluxes()
        self.assertEqual(fluxes, expected_fluxes)

    def test_get_line_thickness(self):
        """Test that get_line_thickness scales line thicknesses correctly."""
        # Mock the fluxes
        self.r.reset()
        self.visualizer.get_fluxes = MagicMock(return_value={"R1": 50, "R2": 10, "R3": -5})
        max_flux = 50
        min_flux = 5
        min_thickness = 0.1
        max_thickness = 30.0
        expected_thickness = {
            rxn: min_thickness + ((abs(flux) - min_flux) / (max_flux - min_flux)) * (max_thickness - min_thickness)
            if flux != 0 else min_thickness
            for rxn, flux in {"R1": 50, "R2": 10, "R3": -5}.items()
        }
        thickness = self.visualizer.get_line_thickness()
        self.assertEqual(thickness, expected_thickness)

    def test_get_color_gradient(self):
        """Test that get_color_gradient creates the correct RGB gradients."""
        self.visualizer.get_fluxes = MagicMock(return_value={"R1": 50, "R2": 10, "R3": -5})       
        colors = self.visualizer.get_color_gradient()
        self.assertIn("R1", colors)
        self.assertIn("R2", colors)
        self.assertIn("R3", colors)
        self.assertGreater(colors["R1"][0], colors["R2"][0])  # Higher flux should be more red
        self.assertGreater(colors["R3"][2], colors["R2"][2])  # Negative flux should be more blue

    def test_extract_rgb_values(self):
        """Test that extract_rgb_values retrieves the correct RGB values."""
        self.visualizer.make_color_gradient = MagicMock(return_value={
            "R1": (255, 0, 0),
            "R2": (128, 128, 0),
            "R3": (0, 128, 255),
        })
        rgb = self.visualizer.extract_rgb_values("R1")
        self.assertEqual(rgb, (255, 0, 0))
        with self.assertRaises(ValueError):
            self.visualizer.extract_rgb_values("R4")

if __name__ == "__main__":
    unittest.main()

