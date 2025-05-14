from utils import clamp

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

        self.proportional = 0
        self.integral = 0
        self.derivative = 0

        self.last_error = 0
    
    def update(self, input, dt=1):
        """
        Updates the PID controller with the new input value.
        
        :param input: The current input value
        :return: The correction value
        """
        error = self.setpoint - input

        self.proportional = error * self.kp * dt
        self.integral += error * self.ki * dt
        self.derivative = ((error - self.last_error) / dt) * self.kd if dt > 0 else 0

        if self.i_max is not None:
            self.integral = clamp(self.integral, -self.i_max, self.i_max)

        correction = self.proportional + self.integral + self.derivative
        if self.output_max is not None:
            correction = clamp(correction, -self.output_max, self.output_max)

        self.last_error = error
        return correction
    
    def reset(self):
        """
        Resets the PID controller.
        
        :return: None
        """
        self.proportional = 0
        self.integral = 0
        self.derivative = 0
        self.last_error = 0

    def set_setpoint(self, setpoint):
        """
        Sets a new setpoint for the PID controller.
        
        :param setpoint: The new setpoint value
        :return: None
        """
        self.setpoint = setpoint
    
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
    
    def set_tunings(self, tunings):
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