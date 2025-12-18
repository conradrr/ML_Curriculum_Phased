class CustomVector:
    def __init__(self, coordinates, name=""):
        if (len(coordinates) > 4 or len(coordinates) < 2):
            raise Exception("Only 2d, 3d, or 4d vectors are accepted.")
        self.coordinates = coordinates
        self.name = name

    def printCoordinates(self):
        print(self.name, ": ", self.coordinates)

    def addVector(self, vector):
        print("Adding vectors: ", self.coordinates, " + ", vector.coordinates)
        c1Length = len(self.coordinates)
        c2Length = len(vector.coordinates)
        if (c1Length < c2Length):
            for i in range(0, c2Length):
                if i >= c1Length:
                    self.coordinates.append(0)
                self.coordinates[i]=self.coordinates[i]+vector.coordinates[i]
        else:
            for i in range(0, c2Length):
                self.coordinates[i]=self.coordinates[i]+vector.coordinates[i]
        
    def scaleVector(self, scalar):
        print("Scaling vector by ", scalar)
        for i in range(0, len(self.coordinates)):
            self.coordinates[i] = self.coordinates[i] * scalar


class Vector2d:
    def __init__(self, x, y, name=""):
        self.x = x
        self.y = y
        self.name = name

    # Function for visual convenience
    def printCoordinates(self):
        print(self.name, ": ", self.x, ", ", self.y)
    
    # Vectors added together are the sum of their parts x1+x2, y1+y2, etc.
    def addVector(self, vector):
        print("Adding vectors: ", self.coordinates, " + ", vector.coordinates)
        self.x = self.x + vector.x
        self.y = self.y + vector.y

    # Vector scaling is to multiply each coordinate by the scalar
    # - Scalar of >1 increases the size of the vector
    # - Scalar of 1 maintains the vector's size
    # - Scalar of >= 0 AND < 1 reduces the size of the vector
    # - Scalar of < 0 flips the vector while maintaining the origin
    def scaleVector(self, scalar):
        print("Scaling vector by ", scalar)
        self.x = self.x * scalar
        self.y = self.y * scalar

def Vector2d_Test():
    v1 = Vector2d(1, 2, "v1")
    v2 = Vector2d(3, 3, "v2")
    v1.printCoordinates()
    v2.printCoordinates()
    v1.addVector(v2)
    v1.printCoordinates()
    v2.printCoordinates()
    v2.scaleVector(2)
    v1.printCoordinates()
    v2.printCoordinates()
    v1.scaleVector(-1)
    v1.printCoordinates()
    v2.printCoordinates()

def CustomVector_Test():
    v1 = CustomVector([1, 2], "v1")
    v1.printCoordinates()
    v2 = CustomVector([4, 5], "v2")
    v2.printCoordinates()
    v3 = CustomVector([1, 2, 4, 5], "v3")
    v3.printCoordinates()
    v2.addVector(v1)
    v2.printCoordinates()
    v3.addVector(v1)
    v3.printCoordinates()
    v2.addVector(v3)
    v2.printCoordinates()
    v1.scaleVector(2)
    v1.printCoordinates()
    v3.scaleVector(3)
    v3.printCoordinates()

CustomVector_Test()