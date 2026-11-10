class Command:
    def __init__(self, code):
        self.code = code


moveForwardCommand = Command("moveForward")
moveBackwardCommand = Command("moveBackward")
stopCommand = Command("stop")

LISTE_COMMANDS ={"0X123":moveForwardCommand,
                 "0X789":moveBackwardCommand,
                 "0XABC":stopCommand
}
