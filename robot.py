COMMANDS = {
    "0X123": "moveForward",
    "0X789": "moveBackward",
    "0XABC": "stop",
}

def parse_robot_command(command_flow):
    liste = command_flow.split(",")
    res = []
    for code in liste:
        res.append(COMMANDS[code])
    return res
