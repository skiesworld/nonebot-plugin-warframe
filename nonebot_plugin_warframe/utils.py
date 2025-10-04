from datetime import datetime


def format_timestamp(timestamp: int, include_date: bool = False) -> str:
    """格式化时间戳为指定日期格式


    :param timestamp: 时间戳
    :param include_date: 是否包含年月日，默认 False


    :return: 格式化后的时间字符串
    """
    format_str = "%Y-%m-%d %H:%M:%S" if include_date else "%H:%M:%S"
    return datetime.fromtimestamp(timestamp).strftime(format_str)
