# import datetime as built_in_datetime
import datetime

# You can't explicitly patch datetime due to
# TypeError: can't set attributes of built-in/extension type 'datetime.datetime'
# We could just use https://github.com/spulec/freezegun/
# but for fun, we'll write out own context class

_real_datetime = datetime.datetime
# Use a mutable object to mutate a nonlocal object
# acts as a singleton
_fixed_datetime = []


class _MockDateTime(_real_datetime):
    @classmethod
    def now(cls, tz=None):
        if len(_fixed_datetime):
            return _fixed_datetime[0]


class FreezeDateTime:
    def __init__(self, fixed_datetime: datetime.datetime):
        if len(_fixed_datetime):
            _fixed_datetime.pop()
        _fixed_datetime.append(fixed_datetime)

    def __enter__(self):
        datetime.datetime = _MockDateTime

    def __exit__(self, exc_type, exc_value, traceback):
        datetime.datetime = _real_datetime
