def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a


def rewardseq_to_returns(reward_list: list[float], gamma: float) -> list[float]:
    """
    Turns a list of rewards into the list of returns
    """
    G = 0
    returns_list = []
    for r in reward_list[::-1]:
        G = r + gamma * G
        returns_list.append(G)
    return returns_list[::-1]
