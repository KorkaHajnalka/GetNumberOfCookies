import numpy as np

def GetNumberOfCookies(money, price, wrap):

    # In the beginning of the process it should be calculated how many cookies can be bought for a given amount of money.
    # Number of cookies equals to quotient in this equation: money = quotient*price + rest
    NumberOfCookies = money // price

    # Number of extra cookies in the first step equals to quotient in this equation: NumberOfCookies = quotient*wrap + rest
    ExtraCookies = NumberOfCookies //wrap

    NumberOfCookies += ExtraCookies

    while ExtraCookies >= wrap:
        ExtraCookies = ExtraCookies // wrap
        NumberOfCookies += ExtraCookies

    return NumberOfCookies


GetNumberOfCookies(16,2,2)