from zxcvbn import zxcvbn

def estimatestrength(password):
    result = zxcvbn(password)
    score = result["score"]
    levels = ["Very Weak","Weak","Fair","Strong","Very Strong"]
    return levels[score]