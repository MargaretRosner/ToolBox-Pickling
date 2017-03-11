""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load

print('fooooo')
def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    print("gooo")
    if exists(file_name):
        if reset == False:
            new_doc = open(file_name, 'rb+')
            counter = load(new_doc)+1
            new_doc.close()
            P = open(file_name, 'wb')
            dump(counter, P)
            return counter
        else:
            P = open(file_name, 'wb')
            dump(1, P)
            return 1
    else:
        P = open(file_name, 'wb')
        dump(1,P)
        return 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
