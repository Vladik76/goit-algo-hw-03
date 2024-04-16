import random

def get_numbers_ticket(min: int, max: int, quantity:int) -> list:

    """
        This function returns a sorted list of unique numbers or an empty list if parameters do not fit the rules
        min - minumal value in a range of numbers
        max - maximal value in a range of numbers
        quantity - the number of elements in the returned list of unique values
    """
    
    lottery_numbers=set() ##Initialise list with lottery numbers
    

    #Check input values

    try:
        min_value=int(min)
        if min_value < 1:
            return list()
    except (ValueError, TypeError):
        return "The minimal value should be an integer value bigger or equal to 1"
    
    try:
        max_value=int(max)
        if max_value > 100:
            return list()
    except (ValueError, TypeError):
        return "The maximal value should be an integer value less or equal to 100"
    
    if min_value >= max_value:
        return list()
    
    if max_value - min_value+1 < quantity:
        return list()
    
    #main logic. Get random values and creating list of unique lottery numbers

    while len(lottery_numbers)<quantity:
        lottery_numbers.add(random.randint(min,max))
    
    return sorted(lottery_numbers)
