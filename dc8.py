"""
To increase the odds of the old fashioned game (Rock, Paper, Scissors) Sam Kass and Karen Bryla reinvented the game with 5 different items instead of 3: Rock, Paper, Scissor, Lizard, Spock. It was later also featured in the sitcom "The Big Bang Theory".


Game rules:
    rock crushes paper and lizard
    paper covers rock and disproves Spock
    lizard poisons spock and eats paper
    Spock mashes scissor and vapurizes rock
    scissor cuts paper and decapiates lizard

Eg:

"rock", "spock"       -->  "Player 2 won!"      because Spock vaporizes rock
"scissor", "lizard"   -->  "Player 1 won!"      because scissor decapitates lizard
"scissor", "Scissor"  -->  "Draw!"              because they are the same
"foo", "Bar"          -->  "Oh, Unknown Thing"  because they are not valid
"""

def result(p1, p2):
    game_dict = {'rock':0, 'spock':1, 'paper':2, 'lizard':3, 'scissor':4}
    p1 = p1.lower()
    p2 = p2.lower()
    try:
        res = (game_dict[p1] - game_dict[p2]) % 5
        if res == 1 or res == 2:
            return 'Player 1 won!'
        elif res == 3 or res == 4:
            return 'Player 2 won!'
        else:
            return 'Draw!'
    except:
        return 'Oh, Unknown Thing'

print(result('lizard', 'scissor'))
print(result('Spock', 'Rock'))
print(result('R0CK', 'SPOCK'))
print(result('Paper', 'papeR'))

