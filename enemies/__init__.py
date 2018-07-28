from importlib import import_module

from .enemy import Enemy


def build_enemy(enemy_name, *args, **kwargs):
    """
    Factory for building enemies by dynamically importing them and creating them using
    This function and set up was modified from https://www.bnmetrics.com/blog/factory-pattern-in-python3-simple-version
    Thank you to the author
    :param enemy_name:
    :param args: need to do some experimentation into *args and **kwargs - I know roughly what they do but need more
    specific information regarding them
    :param kwargs:
    :return:
    """

    try:
        # get the module
        if '.' in enemy_name:
            module_name, class_name = enemy_name.rsplit('.', 1)
        else:
            module_name = enemy_name
            class_name = enemy_name.capitalize()
        # import the module
        enemy_module = import_module('.' + module_name, package='enemies')
        # create the class from the module
        # print("enemy module : {0}".format(enemy_module))
        # print("class name: {0}".format(class_name))
        enemy_class = getattr(enemy_module, class_name)
        # instantiate the class into an obj
        instance = enemy_class(*args, **kwargs)
       # print("created {0}".format(instance))
    # handle any issues.
    except (AttributeError, ModuleNotFoundError):
        raise ImportError('{} is not part of our enemy collection!'.format(enemy_name))
    else:
        if not issubclass(enemy_class, Enemy):
            raise ImportError("We currently don't have {}, but you are welcome to send in the request for it!".format(enemy_class))

    # return the enemy
    return instance