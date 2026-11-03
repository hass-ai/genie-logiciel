from liste_commands import LISTE_COMMANDS

def parse_robot_command(command_flow):
    liste = command_flow.split(",")
    res = []
    for code in liste:
        if ":" in code:
            c,nombre = code.split(":")
            for i in range(int(nombre)):
                res.append(LISTE_COMMANDS[c])
        else:
            res.append(LISTE_COMMANDS[code])
    return res
