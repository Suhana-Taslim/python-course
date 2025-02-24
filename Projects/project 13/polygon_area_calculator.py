import math

class RegularPolygon:
    def __init__(self, num_sides, side_length):
        
        self.num_sides = num_sides
        self.side_length = side_length

    def area(self):
        
        n = self.num_sides
        s = self.side_length
        return (n * s**2) / (4 * math.tan(math.pi / n))

# Example usage:
square = RegularPolygon(4, 10)
print("Area of the square:", square.area())
