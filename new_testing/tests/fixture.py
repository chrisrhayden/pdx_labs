

full_text = 'Python’s datetime.datetime objects have a tzinfo attribute that can be used to store time zone information, represented as an instance of a subclass of datetime.tzinfo.\n When this attribute is set and describes an offset, a datetime object is aware. Otherwise, it’s naive.\n You can use is_aware() and is_naive() to determine whether datetimes are aware or naive.\n When time zone support is disabled, Django uses naive datetime objects in local time.\n This is simple and sufficient for many use cases. In this mode, to obtain the current time, you would write:\n'


wanted = 'Python’s datetime.datetime objects have a tzinfo attribute that can be used to store time zone information, represented as an instance of a subclass of datetime.tzinfo. When this attribute is set and describes an offset, a datetime object is aware. Otherwise, it’s naive. You can use is_aware() and is_naive() to determine whether datetimes are aware or naive.'

