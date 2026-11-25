#!/usr/bin/python3
"""Square model derived from the Rectangle class."""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """Represent a rectangle with equal dimensions."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the formatted square representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Return the square size."""
        return self.width

    @size.setter
    def size(self, value):
        """Validate and update both square dimensions."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes using positional or keyword arguments."""
        names = ("id", "size", "x", "y")
        values = zip(names, args) if args else kwargs.items()
        for key, value in values:
            if key in names:
                if key == "id" and value is None:
                    Base.__init__(self)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the square dictionary representation."""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
