def slot_machine(bet, result):

    if result==['$','$','$']:
        return bet *20
    
    if (result[0]==result[1]) and (result[1]==result[2]):
        return bet *5
    
    if (result[0]==result[1]) or (result[1]==result[2]):
        return bet *2
    
    return 0