####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

'''team_name = 'E1'
strategy_name = 'Betray'
strategy_description = 'Always betray.'
    
def move(my_history, their_history, my_score, their_score):
    ''''''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    ''''''
    
    #This example player always betrays.      
    return 'b'''

team_name = 'The Semi Competent Programmers' # Only 10 chars displayed.
strategy_name = 'Tit-For-Tat'
strategy_description = 'Depending on the opponents last move, I will copy their move. Essentially, I will betray each time my opponent has betrayed because this method is a tit-for-tat. So, you are hurting them is response to them hurting you.'
    
def move(my_history, their_history, my_score, their_score):
  first_turn = True
  if first_turn == True:
    return 'c'
    first_turn = False
  else:
    while their_history[-1] == 'b':
      return 'b'
    else:
      return 'c'

