import random

throws = {
    0: "rock",
    1: "paper",
    2: "scissors",
    3: "bomb"
}

def botThrowing(canUsebomb):
    throw = throws.get(random.randint(0,2))
    if canUsebomb and throw == "paper":
        return "bomb"
    else:
        return throw

def playGame(p1Throw, p2Throw):
    if p1Throw == "rock":
        if p2Throw == "paper" or p2Throw == "bomb":
            return "lose"
        elif p2Throw == "scissors":
            return "win"
        else:
            return "tie"
    elif p1Throw == "paper":
        if p2Throw == "scissors" or p2Throw == "bomb":
            return "lose"
        elif p2Throw == "rock":
            return "win"
        else:
            return "tie"
    if p1Throw == "scissors":
        if p2Throw == "rock":
            return "lose"
        elif p2Throw == "paper" or p2Throw == "bomb":
            return "win"
        else:
            return "tie"
    if p1Throw == "bomb":
        if p2Throw == "scissors":
            return "lose"
        elif p2Throw == "paper" or p2Throw == "rock":
            return "win"
        else:
            return "tie"
