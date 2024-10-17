from functools import wraps
from django.core.management import call_command


def load_fixture(fixture_name: str):
    """
    Decorator that loads a specific fixture for the test.
    """

    def decorator(test_func):
        @wraps(test_func)
        def wrapper(*args, **kwargs):
            call_command("loaddata", fixture_name, verbosity=0)
            return test_func(*args, **kwargs)

        return wrapper

    return decorator
