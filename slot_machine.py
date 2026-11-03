def slot_machine(bet, result):

    if (result[0]==result[1]) or (result[1]==result[2]):
        return bet *2
    
    return 0
