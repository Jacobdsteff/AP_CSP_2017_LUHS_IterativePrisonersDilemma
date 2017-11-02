team_name = 'I did everthing just right'
strategy_name = 'They wil never know'
strategy_description = 'Betray 75% of the time and confess 25% of the time'
  
import random
           
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if 'b' in their_history:
        return 'b'
    
    else:
        if random.random()<0.25:
            return 'b'
        else:
            return 'c'