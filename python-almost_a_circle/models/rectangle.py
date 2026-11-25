#!/usr/bin/python3
"""Rectangle model with validated dimensions and coordinates."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle with dimensions and position."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Validate and assign the width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Validate and assign the height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return the horizontal position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Validate and assign the horizontal position."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return the vertical position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Validate and assign the vertical position."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the rectangle area."""
        return self.width * self.height

    def display(self):
        """Print the rectangle using hash characters."""
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the formatted rectangle representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes using positional or keyword arguments."""
        names = ("id", "width", "height", "x", "y")
        values = zip(names, args) if args else kwargs.items()
        for key, value in values:
            if key in names:
                if key == "id" and value is None:
                    Base.__init__(self)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the rectangle dictionary representation."""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
