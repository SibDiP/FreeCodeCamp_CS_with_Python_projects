class Rectangle:
    EQUAL_SIDES_AMOUNT = 2
    SQUARE_ROOT = 0.5
    MAX_PICTURE_LEN = 50

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.picture = ''

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.EQUAL_SIDES_AMOUNT * self.width + self.EQUAL_SIDES_AMOUNT * self.height

    def get_diagonal(self):
        return (self.width ** self.EQUAL_SIDES_AMOUNT + self.height ** self.EQUAL_SIDES_AMOUNT) ** self.SQUARE_ROOT

    def get_picture(self):
        if self.width > self.MAX_PICTURE_LEN or self.height > self.MAX_PICTURE_LEN:
            return 'Too big for picture.'

        for row in range(self.height):
            self.picture += f'{"*" * self.width}\n'

        return self.picture

    def get_amount_inside(self, rectangle: object) -> int:
        """
        Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance,
        a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        """
        times_fit_height = self.height / rectangle.height
        times_fit_width = self.width / rectangle.width

        return (times_fit_width * times_fit_height) // 1


class Square(Rectangle):
    def __init__(self, side_len):
        super().__init__(side_len, side_len)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, new_side_len):
        self.width = self.height = new_side_len

    def set_width(self, new_width):
        self.set_side(new_width)

    def set_height(self, new_height):
        self.set_side(new_height)
