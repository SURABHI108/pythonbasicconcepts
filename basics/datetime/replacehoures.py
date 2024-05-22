import datetime
time_obj = datetime.time(10, 30, 0)
new_time_obj = time_obj.replace(hour=11)
print(new_time_obj)
