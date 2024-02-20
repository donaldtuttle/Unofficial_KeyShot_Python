# Keyshot Python3.11 Luxmath

```python

Help on built-in module luxmath:
NAME
    luxmath - The module contains a vector and matrix class for mathematical operations.
CLASSES
    builtins.object
        Matrix
        Vector
    
    class Matrix(builtins.object)
       Matrix enables mathematical operations of matrices and vectors.
       
       Its constructor takes either a number or a tuple/list of size 16.
       Examples:
         luxmath.Matrix(3) # -> (3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3)
         luxmath.Matrix((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)) # -> (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
       
       Methods defined here:
       
       __eq__(self, value, /)
           Return self==value.
       
       __ge__(self, value, /)
           Return self>=value.
       
       __gt__(self, value, /)
           Return self>value.
       
       __hash__(self, /)
           Return hash(self).
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __le__(self, value, /)
           Return self<=value.
       
       __lt__(self, value, /)
           Return self<value.
       
       __ne__(self, value, /)
           Return self!=value.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       add(...)
           Add Matrix to a copy of this Matrix and return the result.
           mat = Matrix to add. *
       
       det(...)
           Computes the determinant of the Matrix.
       
       dump(...)
           Returns a string representation of the Matrix.
       
       getTransformation(...)
           Get scale, rotate and translate vectors from Matrix.
       
       invert(...)
           Inverts the Matrix.
       
       isDeforming(...)
           Checks if the Matrix is deforming.
       
       isEqual(...)
           Checks if the Matrix is equal to the other Matrix.
           mat = Matrix to check equality against. *
       
       isIdentity(...)
           Checks if the Matrix is the identity Matrix.
       
       isTranslation(...)
           Checks if the Matrix is a translation.
       
       mul(...)
           Multipy Matrix by a copy of this Matrix and return the result.
           mat = Matrix to multiply by. *
       
       normalize(...)
           Normalizes a copy of the Matrix and return the result.
       
       rotate(...)
           Rotate a copy of the Matrix by a Vector and return the result.
           vec = Vector to rotate by. *
           left = Boolean for rotating left (default = False).
       
       rotateAroundAxis(...)
           Rotate a copy of the Matrix around an axis by an angle in degrees and return the result.
           axis = The axis as a Vector. *
           angle = The angle in degrees to rotate by. *
       
       scale(...)
           Scale a copy of the Matrix by a Vector or number and return the result.
           val = Vector or number to scale with. *
       
       scale4(...)
           Scale a copy of the Matrix by a number (all entries) and return the result.
           num = Number to scale with. *
       
       scalePos(...)
           Scale a copy of the Matrix "position" part by a number and return the result.
           num = Number to scale with. *
       
       setTransformation(...)
           Set scale, rotate and translate parts of the Matrix.
           scale = Scale Vector. *
           rotate = Rotate Vector. *
           trans = Translate Vector. *
       
       sub(...)
           Subtract Matrix from a copy of this Matrix and return the result.
           mat = Matrix to subtract. *
       
       translate(...)
           Translate a copy of the Matrix by a Vector and return the result.
           vec = Vector to translate by. *
       
       transpose(...)
           Transposes a copy of the Matrix and return the result.
       
       val(...)
           Returns the data of the Matrix.
       
       ----------------------------------------------------------------------
       Class methods defined here:
       
       makeIdentity(...) from builtins.type
           Creates an identity matrix (class method).
       
       makeRotate(...) from builtins.type
           Creates an rotation matrix from given input (class method).
       
       makeScale(...) from builtins.type
           Creates an scaling matrix from given input (class method).
       
       makeTranslate(...) from builtins.type
           Creates an translation matrix from given input (class method).
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
       
       ----------------------------------------------------------------------
       Data descriptors defined here:
       
       data
           The Matrix data (4x4).
    
    class Vector(builtins.object)
       Vector enables mathematical operations of vectors.
       
       Its constructor takes either a tuple/list of three values (x, y, z), a single number as (x, x, x) or three numbers as (x, y, z).
       Examples:
         luxmath.Vector((1, 2, 3)) # -> (1, 2, 3)
         luxmath.Vector(1)         # -> (1, 1, 1)
         luxmath.Vector(1, 2, 3)   # -> (1, 2, 3)
       
       Additionally, whenever a luxmath.Vector is accepted it is also allowed to give a tuple/list of size 3 or a number.
       Examples:
         luxmath.Vector(1).add(1)         # -> (2, 2, 2)
         luxmath.Vector(1).add((1, 2, 3)) # -> (2, 3, 4)
       
       Methods defined here:
       
       __eq__(self, value, /)
           Return self==value.
       
       __ge__(self, value, /)
           Return self>=value.
       
       __gt__(self, value, /)
           Return self>value.
       
       __hash__(self, /)
           Return hash(self).
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __le__(self, value, /)
           Return self<=value.
       
       __lt__(self, value, /)
           Return self<value.
       
       __ne__(self, value, /)
           Return self!=value.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       add(...)
           Adds the Vector to a copy of this Vector and returns the result.
           vec = Vector to add. *
       
       cross(...)
           Calculates the cross product and returns the result.
           vec1 = Vector one. *
           vec2 = Vector two. *
       
       div(...)
           Divides a copy of this Vector with a number and returns the result.
           num = Number to divide with. *
       
       getOrthogonalBasis(...)
           Gets the orthogonal basis as two Vectors.
       
       len(...)
           Returns the length of the Vector.
       
       mul(...)
           Multiplies the Vector or number to a copy of this Vector and returns the result.
           val = Vector or number to multiply with.
       
       normalize(...)
           Normalizes a copy of the Vector and returns the result.
       
       set(...)
           Set (x, y, z) values.
           tup = Tuple of size 3 to assign. *
       
       setOrthogonal(...)
           Sets orthogonal to input Vector.
           vec = Vector make orthogonal to. *
       
       sub(...)
           Subtracts the Vector from a copy of this Vector and returns the result.
           vec = Vector to subtract. *
       
       val(...)
           Returns the values in a tuple (x, y, z).
       
       ----------------------------------------------------------------------
       Class methods defined here:
       
       dot(...) from builtins.type
           Calculates the dot product and returns the result (class method).
           vec1 = Vector one. *
           vec2 = Vector two. *
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
       
       ----------------------------------------------------------------------
       Data descriptors defined here:
       
       x
           The X part.
       
       y
           The Y part.
       
       z
           The Z part.
FILE
    (built-in)
```
