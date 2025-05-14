class Pose:
    """A class for keeping track of the robot's position and orientation"""
    def __init__(self, x, y, angle):
        """
        Initializes the Pose class

        :param x: X coordinate in mm
        :param y: Y coordinate in mm
        :param angle: Angle in degrees
        """
        self._x = x
        self._y = y
        self._angle = angle

    def __str__(self):
        """
        Returns a string representation of the Pose object
        
        :return: String representation of the Pose object
        """
        return "Pose(x={}, y={}, angle={})".format(self.x, self.y, self.angle)

    @property
    def angle(self):
        """
        Returns the angle of the Pose object

        :return: Angle in degrees
        """
        return self._angle
    
    @angle.setter
    def angle(self, angle):
        """
        Sets the angle of the Pose object

        :param angle: Angle in degrees
        """
        self.angle = angle
    
    @property
    def coordinates(self):
        """
        Returns the coordinates of the Pose object

        :return: Tuple of (x, y) coordinates in mm
        """
        return (self._x, self._y)
    
    @coordinates.setter
    def coordinates(self, x, y):
        """
        Sets the coordinates of the Pose object

        :param x: X coordinate in mm
        :param y: Y coordinate in mm
        """
        self._x = x
        self._y = y
    
    def reset(self):
        """
        Resets the Pose object to the origin
        """
        self._x = 0
        self._y = 0
        self._angle = 0
    
    def reset_angle(self):
        """
        Resets the angle of the Pose object to 0
        """
        self._angle = 0