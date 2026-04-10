# from db import connect

# conn = connect()
# cur = conn.cursor()

# with open("sample.log", "r") as file:
#     for line in file:
#         parts = line.strip().split(" ", 3)
#         timestamp = parts[0] + " " + parts[1]
#         level = parts[2]
#         message = parts[3]

#         cur.execute(
#             "INSERT INTO logs (timestamp, level, message) VALUES (%s, %s, %s)",
#             (timestamp, level, message)
#         )

# conn.commit()
# cur.close()
# conn.close()

# print("Logs inserted successfully")





from db import connect
import random
from datetime import datetime, timedelta

conn = connect()
cur = conn.cursor()

levels = ["INFO", "ERROR", "WARNING"]
messages = [
    "Server started",
    "Database connection failed",
    "High memory usage",
    "User login successful",
    "Timeout occurred",
    "Disk space low"
]

start_time = datetime(2026, 4, 1, 10, 0, 0)

for i in range(100000):  # 100K logs
    timestamp = start_time + timedelta(seconds=i)
    level = random.choice(levels)
    message = random.choice(messages)

    cur.execute(
        "INSERT INTO logs (timestamp, level, message) VALUES (%s, %s, %s)",
        (timestamp, level, message)
    )

conn.commit()
cur.close()
conn.close()

print("100K logs inserted")