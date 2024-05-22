import datetime
# date_string = "2024-05-22 10:30:00"
# format_string = "%Y-%m-%d %H:%M:%S"
# parsed_datetime = datetime.datetime.strptime(date_string, format_string)
# print(parsed_datetime.strftime("%d-%m-%Y %H:%M:%S"))
# print(parsed_datetime)
date_obj = datetime.date(2024, 5, 22)
date_str = date_obj.strftime("%Y-%m-%d")

print(date_str)  # Output: '2024-05-22'

# Convert time object to string
time_obj = datetime.time(10, 30, 0)
print(type(time_obj))
time_str = time_obj.strftime("%H:%M:%S")

print(type(time_str))  # Output: '10:30:00' convert datetime.time object to string