class Rectangle:

    def __init__(self, width: int, height: int):
        self.__update_attrs__()
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __update_attrs__(self):
        self._perimeter_ = None
        self._area_ = None
        self._diagonal_ = None
        self._amount_ = None

    def get_width(self):
        return self._width_

    def set_width(self, value: int):
        if isinstance(value, int):
            self._width_ = value
            self.__update_attrs__()
        else:
            raise ValueError("value should be int")

    def get_height(self):
        return self._height_

    def set_height(self, value: int):
        if isinstance(value, int):
            self._height_ = value
            self.__update_attrs__()
        else:
            raise ValueError("value should be int")

    def get_area(self):
        if self._area_ is None:
            self._area_ = (self.width * self.height)
        return self._area_

    def get_perimeter(self):
        if self._perimeter_ is None:
            self._perimeter_ = 2 * (self.width + self.height)
        return self._perimeter_

    def get_diagonal(self):
        if self._diagonal_ is None:
            self._diagonal_ = ((self.width ** 2 + self.height ** 2) ** .5)
        return self._diagonal_

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, other: 'Rectangle'):
        return (self.width // other.width) * (self.height // other.height)

    def __floordiv__(self, other):
        return self.get_amount_inside(other)

    width = property(get_width, set_width)
    height = property(get_height, set_height)
    area = property(get_area)
    perimeter = property(get_perimeter)
    diagonal = property(get_diagonal)
    picture = property(get_picture)


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(width=side, height=side)
        self.side = side

    def __str__(self):
        return f"Square(side={self.side})"

    def get_side(self):
        return self._side_

    def set_side(self, value: int):
        if isinstance(value, int):
            self._side_ = value
            self.__update_attrs__()
        else:
            raise ValueError("value should be int")

    side = property(get_side, set_side)
    _width_ = side
    _height_ = side

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))