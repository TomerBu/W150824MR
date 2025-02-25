def try_parse_int(value: str, default=None):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


# x = try_parse_int("hello", 0)
# x = try_parse_int("hello")
