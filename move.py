import logging


def another_func(*args, **kwargs):
    logging.info("A")
    print(kwargs)
    return args
