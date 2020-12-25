import time
import sqlite3
from datetime import datetime

DB_NAME = "db.sqlite"


def get_lines(time_obj):
    """
    a function to return the remote_addr and time_local of the logs which are created after specific time
    :param time_obj: specific time determined to be a metric to return the logs after that time
    :return: the data logs, remote_addr and time_local, created after an specific time
    """
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT remote_addr,time_local FROM logs WHERE created > ?", [time_obj])
    resp = cur.fetchall()
    return resp


def get_time_and_ip(lines):
    """
    a function to return time and ip
    :param lines: the logs saved in the lines
    :return: ip addresses and the related times
    """
    ips_ = []
    times_ = []
    for line in lines:
        ips_.append(line[0])
        times_.append(parse_time(line[1]))
    return ips_, times_


def parse_time(time_str):
    """
    a function to parse the time in datetime format
    :param time_str: input time
    :return: converted str to datetime data
    """
    try:
        time_obj_ = datetime.strptime(time_str, '[%d/%b/%Y:%H:%M:%S %z]')
    except Exception:
        time_obj_ = ""
    return time_obj_


if __name__ == "__main__":
    unique_ips = {}
    counts = {}
    start_time = datetime(year=2017, month=3, day=9)
    while True:
        lines = get_lines(start_time)
        ips, times = get_time_and_ip(lines)
        if len(times) > 0:
            start_time = times[-1]
        for ip, time_obj in zip(ips, times):
            day = time_obj.strftime("%d-%m-%Y")
            if day not in unique_ips:
                unique_ips[day] = set()
            unique_ips[day].add(ip)

        for k, v in unique_ips.items():
            counts[k] = len(v)

        count_list = counts.items()
        count_list = sorted(count_list, key=lambda x: x[0])

        print("")
        print(datetime.now())
        for item in count_list:
            print("{}: {}".format(*item))

        time.sleep(5)
