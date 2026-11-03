class Command:
    def __init__(self, code):
        self.code = code


moveForwardCommand = Command("moveForward")
moveBackwardCommand = Command("moveBackward")
stopCommand = Command("stop")

