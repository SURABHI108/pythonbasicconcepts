from datetime import datetime
import pytz

# Get the current time in UTC
utc_now = datetime.utcnow()

# Convert UTC time to a specific timezone
desired_timezone = pytz.timezone('America/New_York')
local_time = utc_now.astimezone(desired_timezone)

desired_timezone_india = pytz.timezone('Asia/Kolkata')
local_time_india = utc_now.astimezone(desired_timezone_india)

print("UTC time:", utc_now)
print("Local time in New York:", local_time)
print("Local time in India:", local_time_india)

# this is for how we can convert utc to ist 

# from datetime import datetime, timezone, timedelta

# # Get the current UTC time
# utc_now = datetime.utcnow()

# # Define the Indian Standard Time (IST) timezone offset from UTC
# IST_offset = timedelta(hours=5, minutes=30)

# # Calculate the current time in IST
# ist_now = utc_now + IST_offset

# print("UTC time:", utc_now)
# print("Local time in India (IST):", ist_now)
