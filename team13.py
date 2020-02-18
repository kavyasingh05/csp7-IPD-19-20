####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The Semi Competent Programmers' # Only 10 chars displayed.
strategy_name = 'Two Wrongs Might Make a Right'
strategy_description = '''/
Betray until the opponent betrays twice in a row,
then collude until the opponent betrays again'''
    
def move(my_history, their_history, my_score, their_score):
    


    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    if their_history[-1] != "b" and their_history[-2] != b:
      return 'b'
    else:
      if their_history[-1] != "b":
        return 'c'
'''
bbbbbbbbbbbbbbbbbbbb
cbcbcbcbcbcbcbcbcbcb
'''

team_name = 'The Semi Competent Programmers' # Only 10 chars displayed.
strategy_name = 'Tit-For-Tat'
strategy_description = 'Depending on the opponents last move, I will copy their move. Essentially, I will betray each time my opponent has betrayed because this method is a tit-for-tat. So, you are "hurting" them is response to them "hurting" you.'
    
def move(my_history, their_history, my_score, their_score):

  if my_history[-1] == 'b':
    return 'b'
  else:
    return 'c'

'''
ccbcbcbcbcbcbcbcbcbc
cbcbcbcbcbcbcbcbcbcb
'''

team_name = 'The Semi Competent Programmers' # Only 10 chars displayed.
strategy_name = "As Long As We're Winning"
strategy_description = "Betray until our score is higher than the opponent's
"    
def move(my_history, their_history, my_score, their_score):
  if my_score > their_score:
    return c
  else:
    return b