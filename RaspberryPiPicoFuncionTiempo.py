def format_timestamp(timestamp):
    year, month, day, hour, minute, second, *_ = timestamp
    timestamp_str = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(year, month, day, hour, minute, second)
    return timestamp_str
