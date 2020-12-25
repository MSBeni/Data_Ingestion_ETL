import time
import sys
import sqlite3
from datetime import datetime

DB_NAME = "db.sqlite"


def create_table():
    """
    Checking if the table does not exist, create a table in sqlite DB
    :return: nothing, executing table creation
    """
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS logs (
      raw_log TEXT NOT NULL UNIQUE,
      remote_addr TEXT,
      time_local TEXT,
      request_type TEXT,
      request_path TEXT,
      status INTEGER,
      body_bytes_sent INTEGER,
      http_referer TEXT,
      http_user_agent TEXT,
      created DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    """)
    conn.close()


def parse_line(line):
    """
    Receiving a line of the logs and spiliting it to extract the data
    Sample log: 57.95.176.149 - - [24/Dec/2020:17:46:10 +0000] "PUT /search/app HTTP/1.1" 200 108 "http://mejia.info/" "Mozilla/5.0 (Windows; U; Windows 98) AppleWebKit/531.23.2 (KHTML, like Gecko) Version/5.0.1 Safari/531.23.2"
    :param line: line refers to a line of the logs which is read from the saved data
    :return: the information embedded in the line of the data logs
    """
    split_line = line.split(" ")
    if len(split_line) < 12:
        return []
    remote_addr = split_line[0]
    time_local = split_line[3] + " " + split_line[4]
    request_type = split_line[5]
    request_path = split_line[6]
    status = split_line[8]
    body_bytes_sent = split_line[9]
    http_referer = split_line[10]
    http_user_agent = " ".join(split_line[11:])
    created = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    return [
        remote_addr,
        time_local,
        request_type,
        request_path,
        status,
        body_bytes_sent,
        http_referer,
        http_user_agent,
        created
    ]


def insert_record(line, parsed):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    args = [line] + parsed
    cur.execute('INSERT INTO logs VALUES (?,?,?,?,?,?,?,?,?,?)', args)
    conn.commit()
    conn.close()


LOG_FILE_A = "log_a.txt"
LOG_FILE_B = "log_b.txt"

if __name__ == "__main__":
    create_table()
    try:
        f_a = open(LOG_FILE_A, 'r')
        f_b = open(LOG_FILE_B, 'r')
        while True:
            where_a = f_a.tell()
            line_a = f_a.readline()
            where_b = f_b.tell()
            line_b = f_b.readline()

            if not line_a and not line_b:
                time.sleep(1)
                f_a.seek(where_a)
                f_b.seek(where_b)
                continue
            else:
                if line_a:
                    line = line_a
                else:
                    line = line_b

                line = line.strip()
                parsed = parse_line(line)
                if len(parsed) > 0:
                    insert_record(line, parsed)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    finally:
        f_a.close()
        f_b.close()
        sys.exit()
