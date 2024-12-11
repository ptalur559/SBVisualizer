import unittest
from unittest.mock import MagicMock
from Visualizer import Visualizer

class TestVisualizer(unittest.TestCase):
    def setUp(self):
        """Set up a mock model and Visualizer instance for testing."""
        self.mock_model = MagicMock()
        self.mock_model.getReactionIds.return_value = ["R1", "R2", "R3"]
        self.mock_model.getReactionRates.return_value = [50, 10, -5]
        self.mock_model.getSBML.return_value = "<sbml></sbml>"
        self.visualizer = Visualizer(r=self.mock_model)

    def test_get_fluxes(self):
        """Test that get_fluxes correctly retrieves reaction fluxes."""
        expected_fluxes = {"R1": 50, "R2": 10, "R3": -5}
        fluxes = self.visualizer.get_fluxes()
        self.assertEqual(fluxes, expected_fluxes)

    def test_set_line_thickness(self):
        """Test that set_line_thickness scales line thicknesses correctly."""
        self.visualizer.get_fluxes = MagicMock(return_value={"R1": 50, "R2": 10, "R3": -5})
        expected_thickness = {"R1": 5, "R2": 1, "R3": -0.5}
        thickness = self.visualizer.set_line_thickness("R1", 5)
        self.assertEqual(thickness, expected_thickness)

    def test_make_color_gradient(self):
        """Test that make_color_gradient creates the correct RGB gradients."""
        self.visualizer.get_fluxes = MagicMock(return_value={"R1": 50, "R2": 10, "R3": -5})
        colors = self.visualizer.make_color_gradient()

        self.assertIn("R1", colors)
        self.assertIn("R2", colors)
        self.assertIn("R3", colors)

        # Check that positive and negative fluxes are handled
        self.assertGreater(colors[50][0], colors[10][0])  # Higher flux is more red
        self.assertGreater(colors[-5][2], colors[10][2])  # Negative flux is more blue

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

    def test_rgb_to_hex(self):
        """Test that rgb_to_hex correctly converts RGB to HEX."""
        self.visualizer.extract_rgb_values = MagicMock(return_value=(255, 0, 0))
        hex_color = self.visualizer.rgb_to_hex()
        self.assertEqual(hex_color, "#FF0000")

        self.visualizer.extract_rgb_values = MagicMock(return_value=(0, 255, 0))
        hex_color = self.visualizer.rgb_to_hex()
        self.assertEqual(hex_color, "#00FF00")

        with self.assertRaises(ValueError):
            self.visualizer.extract_rgb_values = MagicMock(return_value=(300, 0, 0))
            self.visualizer.rgb_to_hex()

if __name__ == "__main__":
    unittest.main()
