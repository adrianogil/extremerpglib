import random


def get_random_element(list_obj):
    '''
        Returns random element from list object
    '''
    return list_obj[random.randint(0, len(list_obj) - 1)]
