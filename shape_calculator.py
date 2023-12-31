class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height


  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


  def set_width(self, width):
    self.width = width


  def set_height(self, height):
    self.height = height

  
  def get_area(self):
    return self.width * self.height


  def get_perimeter(self):
    return 2 * self.width + 2 * self.height


  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5


  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    return(("*" * self.width + "\n") * self.height)
    
    
  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()


class Square(Rectangle):
  def __init__(self, side_length):
    self.width = side_length
    self.height = side_length


  def __str__(self):
    return f"Square(side={self.width})"


  def set_side(self, side_length):
    self.width = side_length
    self.height = side_length


  def set_width(self, width):
    self.set_side(width)

  
  def set_height(self, height):
    self.set_side(height)