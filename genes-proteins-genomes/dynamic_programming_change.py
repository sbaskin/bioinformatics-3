import math

def dp_change(money, coins):
    minnumcoins = {0: 0}
    for m in range(1, money+1):
        minnumcoins[m] = math.inf
        for coin in coins:
            if m >= coin and minnumcoins[m - coin] + 1 < minnumcoins[m]:
                minnumcoins[m] = minnumcoins[m - coin] + 1
    return minnumcoins[money]


money = 18662
coins = [14,10,6,5,3,1]

change = dp_change(money, coins)
print(change)