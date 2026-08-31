from datetime import datetime

# 1. Current day, month, year, hour, minute, timestamp
now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print("Day:", day)
print("Month:", month)
print("Year:", year)
print("Hour:", hour)
print("Minute:", minute)
print("Timestamp:", timestamp)

# 2. Format current date as "%m/%d/%Y, %H:%M:%S"
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date:", formatted_date)

# 3. Change the string "December 5, 2019" to a datetime object
date_string = "December 5, 2019"
changed_date = datetime.strptime(date_string, "%B %d, %Y")
print("Parsed date:", changed_date)

# 4. Time difference between now and new year (next Jan 1)
new_year = datetime(year + 1, 1, 1)
time_diff_new_year = new_year - now
print("Time until new year:", time_diff_new_year)

# 5. Time difference between 1 January 1970 and now
epoch = datetime(1970, 1, 1)
time_diff_epoch = now - epoch
print("Time since epoch:", time_diff_epoch)

# 6. Uses of the datetime module (comment / reflection, no code needed)
# - Time series analysis (timestamping data points, resampling by day/week/month)
# - Logging timestamps of user activity in an application
# - Scheduling posts on a blog or social media platform
# - Calculating ages, durations, deadlines, or countdowns
# - Comparing/sorting events chronologically