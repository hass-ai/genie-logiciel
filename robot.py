COMMANDS = {
    "0X123": "moveForward",
    "0X789": "moveBackward",
    "0XABC": "stop",
}

def parse_robot_command(command_flow):
    return [COMMANDS[command_flow]]
