COMMANDS = {
    "0X123": "moveForward",
}

def parse_robot_command(command_flow):
    return [COMMANDS[command_flow]]
