# Meg Veitz
# 4/14/21
# Given the following code, write multiple test cases to test the calculate_bonus function.


def calculate_bonus(tier, sales):
    '''This function takes in an employees tier (1-3) and sales total and determines a bonus'''
    if tier == 3:
        if sales > 10_000:
            return sales * .15
        else:
            return sales * .075
    elif tier == 2:
        if sales > 10_000:
            return sales * .1
        else:
            return sales * .05
    else:
        if sales > 10_000:
            return sales * .05
        else:
            return sales * .025
