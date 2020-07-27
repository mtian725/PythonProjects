import main
import unittest

class TestProject4(unittest.TestCase):
    def test_shape(self):
        triangle = main.Triangle(3)
        square = main.Square(5)
        circle = main.Circle(4)
        self.assertEqual("This shape is a triangle with side length of 3 and area of 4.", str(triangle))
        self.assertEqual("This shape is a square with side length of 5 and area of 25.", str(square))
        self.assertEqual("This shape is a circle with radius of 4 and area of 50.", str(circle))

    def test_satellite(self):
        natural = main.NaturalSatellite("Nix", 48694, 51419, "Pluto")
        artificial = main.ArtificialSatellite("GLONASS", 19130, "Russia", "Earth")
        self.assertEqual("Nix has a diameter of about 51419 km^3 and orbits Pluto with an orbit radius of 48694 km.", str(natural))
        self.assertEqual("GLONASS is owned by Russia and orbits Earth with an orbit distance of 19130 km.", str(artificial))

if __name__ == '__main__':
    unittest.main()
