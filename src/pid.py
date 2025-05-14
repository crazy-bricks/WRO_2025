class PID_Controller:
    def __init__(self, config, setpoint):
        self.kp = config["kp"]
        self.ki = config["ki"]
        self.kd = config["kd"]
        self.i_max = config["i_max"]
        self.p = 0
        self.i = 0
        self.d = 0
        self.last_error = 0
        self.error = 0
        self.correction = 0