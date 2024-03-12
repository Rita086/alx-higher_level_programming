#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
<<<<<<< HEAD
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
=======
        """Starts a current Square.

        Arguments:
            size (int): The size of the current  Square.
            x (int): The x coordinate of the current Square.
>>>>>>> 71f43bfc6369b08317e718e1ba22adee01dfea5f
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
<<<<<<< HEAD
        """Get/set the size of the Square."""
=======
        """Find/set the size of the Square."""
>>>>>>> 71f43bfc6369b08317e718e1ba22adee01dfea5f
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

<<<<<<< HEAD
        Args:
=======
        Arguments:
>>>>>>> 71f43bfc6369b08317e718e1ba22adee01dfea5f
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
<<<<<<< HEAD
            a = 0
            for arg in args:
                if a == 0:
=======
            b = 0
            for arg in args:
                if b == 0:
>>>>>>> 71f43bfc6369b08317e718e1ba22adee01dfea5f
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
<<<<<<< HEAD
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
=======
                elif b == 1:
                    self.size = arg
                elif b == 2:
                    self.x = arg
                elif b == 3:
                    self.y = arg
                b += 1

        elif kwargs and len(kwargs) != 0:
            for m, v in kwargs.items():
                if m == "id":
>>>>>>> 71f43bfc6369b08317e718e1ba22adee01dfea5f
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
<<<<<<< HEAD
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
=======
                elif m == "size":
                    self.size = v
                elif m == "x":
                    self.x = v
                elif m == "y":
>>>>>>> 71f43bfc6369b08317e718e1ba22adee01dfea5f
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
<<<<<<< HEAD
        """Return the print() and str() representation of a Square."""
=======
        """Takes back the print() and str() representation of a Square."""
>>>>>>> 71f43bfc6369b08317e718e1ba22adee01dfea5f
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
