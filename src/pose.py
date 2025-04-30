class Pose:
    def __init__(self, x, y, angle):
        """
        Initializes the Pose class

        :param x: X coordinate in mm
        :param y: Y coordinate in mm
        :param angle: Angle in degrees
        """
        self.x = x
        self.y = y
        self.angle = angle

    def __str__(self):
        """
        Returns a string representation of the Pose object

        :return: String representation of the Pose object
        """
        return "Pose(x={}, y={}, angle={})".format(self.x, self.y, self.angle)
    
    def set_angle(self, angle):
        """
        Sets the angle of the Pose object
        :param angle: Angle in degrees
        """
        self.angle = angle
    
    def set_coordinates(self, x, y):
        """
        Sets the coordinates of the Pose object
        
        :param x: X coordinate in mm
        :param y: Y coordinate in mm
        """
        self.x = x
        self.y = y
    
    def reset(self):
        """
        Resets the Pose object to the origin
        """
        self.x = 0
        self.y = 0
        self.angle = 0
    
    def reset_angle(self):
        """
        Resets the angle of the Pose object to 0
        """
        self.angle = 0