team_name = 'The Semi C(ompetent Programmers)' # Only 10 chars displayed.
strategy_name = 'Two Wrongs Might Make a Right'
strategy_description = '''Betray until the opponent betrays twice in a row, then collude until the opponent betrays again'''
    
def move(my_history, their_history, my_score, their_score):
    first_turn = True
    second_turn = True
    if first_turn == True:
      first_turn = False
      return 'b'
    elif second_turn == True:
      second_turn = False
      return 'b'
    while their_history[-1] != "b" and their_history[-2] != b:
      return 'b'
    else:
      while their_history[-1] != "b":
        return 'c'
    