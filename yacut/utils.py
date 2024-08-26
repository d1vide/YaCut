from random import randrange, choice

from .constants import SHORT_LINK_LENGTH


def get_unique_short_id():
    short_link = ''
    for _ in range(SHORT_LINK_LENGTH):
        digit = randrange(ord('0'), ord('9'))
        small_letter = randrange(ord('a'), ord('z'))
        big_letter = randrange(ord('A'), ord('Z'))
        rand_element_id = choice([digit,
                                 small_letter,
                                 big_letter])
        short_link += chr(rand_element_id)
    return short_link
