import string

def erase(message: string):

  
    if message == "": # Am I even real ? No...
        return message # So I just return myself : the void
    
        #   So I know that I'm not the void, am I space ?
    if message[0] != ' ': # Surely not, you are discussing to the wrong person
        return message[0] + erase(message[1:]) # I enter the Valallah and the purge continues !

        #   Yeah it's me ! The famous and beautiful space char ;)
    else:
        if len(message) > 1: # *you look behind* Am I the last one standing ?

                    # Hehe somebody is behind, that's nice
                if message[1] == ' ': # IT'S IT ! MY SPACE LOVER
                    return '  ' + erase(message[2:]) # WE ENTER THE VALHALLA TOGETHER ! And the purge continues (next episode)...
                else: # Oh no, I've lost my space love ...
                    return erase(message[1:]) # I cannot enter, i'll find it before ! Do not wait me ! And let the purge continue without me !

        else: # Oh no, I've lost my space love ... Nobody is behind me ...
            return '' # I cannot enter, i'll find it before ! Do not wait me !