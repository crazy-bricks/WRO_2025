from helper import clamp

class PID_Controller:
    """A PID controller class implementation"""

    def __init__(self, config, setpoint):
        """
        Initializes the PID controller with the given configuration and setpoint.
        
        :param config: Configuration dictionary containing PID parameters
        :param setpoint: Desired setpoint value
        """
        self.kp = config.get("kp", 0)
        self.ki = config.get("ki", 0)
        self.kd = config.get("kd", 0)
        self.i_max = config.get("i_max", None)
        self.output_max = config.get("output_max", None)

        self.setpoint = setpoint

        self._proportional = 0
        self._integral = 0
        self._derivative = 0

        self._last_error = 0
        self._error = 100000
    
    def update(self, input, dt=1):
        """
        Updates the PID controller with the new input value.
        
        :param input: The current input value
        :return: The correction value
        """
        error = input - self.setpoint

        self._proportional = error * self.kp * dt
        self._integral += error * self.ki * dt
        self._derivative = ((error - self._last_error) / dt) * self.kd if dt > 0 else 0

        if self.i_max is not None:
            self._integral = clamp(self._integral, -self.i_max, self.i_max)

        correction = self._proportional + self._integral + self._derivative
        if self.output_max is not None:
            correction = clamp(correction, -self.output_max, self.output_max)

        self._last_error = error
        self._error = error
        return correction
    
    def reset(self):
        """
        Resets the PID controller.
        
        :return: None
        """
        self._proportional = 0
        self._integral = 0
        self._derivative = 0
        self._last_error = 0
    
    @property
    def tunings(self):
        """
        Returns the current PID tunings.
        
        :return: A dictionary containing the current PID tunings
        """
        return {
            "kp": self.kp,
            "ki": self.ki,
            "kd": self.kd,
            "i_max": self.i_max,
            "output_max": self.output_max
        }
    
    @tunings.setter
    def tunings(self, tunings):
        """
        Sets new tunings for the PID controller.
        
        :param tunings: A dictionary containing the new PID tunings
        :return: None
        """
        self.kp = tunings.get("kp", self.kp)
        self.ki = tunings.get("ki", self.ki)
        self.kd = tunings.get("kd", self.kd)
        self.i_max = tunings.get("i_max", self.i_max)
        self.output_max = tunings.get("output_max", self.output_max)
        self.reset()
    
    @property
    def setpoint(self):
        """
        Returns the current setpoint of the PID controller.
        
        :return: The current setpoint value
        """
        return self._setpoint
    
    @setpoint.setter
    def setpoint(self, setpoint):
        """
        Sets a new setpoint for the PID controller.
        
        :param setpoint: The new setpoint value
        :return: None
        """
        self._setpoint = setpoint
    
    @property
    def components(self):
        """
        Returns the current PID components.
        
        :return: A dictionary containing the current PID components
        """
        return {
            "proportional": self._proportional,
            "integral": self._integral,
            "derivative": self._derivative
        }
    
    @property
    def error(self):
        """
        Returns the error value.
        
        :return: The last error value
        """
        return self._error
    
    @error.setter
    def error(self, value):
        """
        Sets the error value.
        
        :param value: The new error value
        :return: None
        """
        self._error = value