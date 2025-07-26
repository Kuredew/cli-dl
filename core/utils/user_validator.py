def validate(msg):
    user_input = input(msg + ' [Y/n] ')

    if user_input.lower() == 'y':
        return True
    else:
        return False
    


        


