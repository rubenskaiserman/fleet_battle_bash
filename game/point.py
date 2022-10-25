class Point:
    x: int
    y: int
    def __init__(self, x:int, y:int):
       self.x = x
       self.y = y
    
    def get_point(self):
        return (self.x, self.y)
