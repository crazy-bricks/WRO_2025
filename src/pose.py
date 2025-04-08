class Pose:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def __str__(self):
        return f"Pose(x={self.x}, y={self.y}, angle={self.angle})"
    
    def set_angle(self, angle):
        self.angle = angle
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.x = 0
        self.y = 0
        self.angle = 0
    
    def reset_angle(self):
        self.angle = 0