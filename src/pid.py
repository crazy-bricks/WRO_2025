from utils import clamp

class PID_Controller:
    """A PID controller class implementation"""

    def __init__(self, config, setpoint):
        """
        Initializes the PID controller with the given configuration and setpoint.
        
        :param config: Configuration dictionary containing PID parameters
        :param setpoint: Desired setpoint value
        """
        self.kp = config["kp"]
        self.ki = config["ki"]
        self.kd = config["kd"]
        self.i_max = config["i_max"]
        self.output_max = config["output_max"]

        self.setpoint = setpoint

        self.proportional = 0
        self.integral = 0
        self.derivative = 0

        self.last_error = 0
    
    def update(self, input):
        """
        Updates the PID controller with the new input value.
        
        :param input: The current input value
        :return: The correction value
        """
        error = self.setpoint - input

        self.proportional = error * self.kp
        self.integral += error * self.ki
        self.derivative = (error - self.last_error) * self.kd

        if self.i_max is not None:
            self.integral = clamp(self.integral, -self.i_max, self.i_max)

        correction = self.proportional + self.integral + self.derivative
        if self.output_max is not None:
            correction = clamp(correction, -self.output_max, self.output_max)

        self.last_error = error
        return correction