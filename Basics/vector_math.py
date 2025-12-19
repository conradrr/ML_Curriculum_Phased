class Matrix2d:
    def __init__(self, rows):
        self.rows = rows

class Vector:
    def __init__(self, coordinates, name=""):
        # Only accept 2d, 3d, or 4d vectors
        if (len(coordinates) > 4 or len(coordinates) < 2):
            raise Exception("Only 2d, 3d, or 4d vectors are accepted.")
        self.coordinates = coordinates
        self.name = name

    def renameVector(self, name):
        self.name = name

    # Function for visual convenience
    def printCoordinates(self):
        print(self.name, ": ", self.coordinates)

    # Add vectors based on length:
    # - IF this vector is smaller THEN append (if needed) and sum the coordinates in sequence
    # - OTHERWISE we can add based off of the incoming vector's length since it is tossed anyway
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
    
    # Scale vectors
    # Simply multiply each element of this vector by the scalar
    def scaleVector(self, scalar):
        print("Scaling vector by ", scalar)
        for i in range(0, len(self.coordinates)):
            self.coordinates[i] = self.coordinates[i] * scalar


class Vector2d(Vector):
    def __init__(self, x, y, name=""):
        super().__init__([x, y], name)

    def transformVector(self, matrix):
        a = self.coordinates[0] * matrix.rows[0]
        b = self.coordinates[1] * matrix.rows[1]
        c = self.coordinates[0] * matrix.rows[2]
        d = self.coordinates[1] * matrix.rows[3]
        self.coordinates[0] = a+b
        self.coordinates[1] = c+d

class Vector3d(Vector):
    def __init__(self, x, y, z, name=""):
        super().__init__([x, y, z], name)

class Vector4d(Vector):
    def __init__(self, w, x, y, z, name=""):
        super().__init__([w, x, y, z], name)

def CustomVector_Test():
    v1 = Vector([1, 2], name="v1")
    v1.printCoordinates()
    v2 = Vector([4, 5], name="v2")
    v2.printCoordinates()
    v3 = Vector([1, 2, 4, 5], name="v3")
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

def Vector2d_Test():
    v1 = Vector2d(1, 2, name="v1")
    v2 = Vector2d(3, 3, name="v2")
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

def Vector_ChildClasses_Test():
    v2d = Vector2d(1, 2, name="v2d")
    v4d = Vector4d(3, 4, 5, 6, name="v4d")
    v2d.printCoordinates()
    v2d.addVector(v4d)
    v2d.printCoordinates()

def Vector2d_Rotate_90def():
    v2d = Vector2d(2, 1, name="vector")
    v2d.printCoordinates()
    matrix = Matrix2d([0, -1, 1, 0])
    v2d.transformVector(matrix)
    v2d.renameVector("rotated-vector")
    v2d.printCoordinates()

Vector2d_Rotate_90def()