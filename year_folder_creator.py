import os
import calendar
from datetime import datetime

# Specify the year
year = 2024

# Base folder name
base_folder = str(year)

# List of month names
months = list(calendar.month_name)[1:]

# Create the base year folder
if not os.path.exists(base_folder):
    os.makedirs(base_folder)

# Create folders for each month within the year folder
for month in months:
    # Create the month folder inside the year folder
    month_folder_path = os.path.join(base_folder, month)
    if not os.path.exists(month_folder_path):
        os.makedirs(month_folder_path)

    # Get the month number (1 for January, 2 for February, etc.)
    month_num = datetime.strptime(month, "%B").month

    # Get the number of days in the month
    days_in_month = calendar.monthrange(year, month_num)[1]

    # Loop through each day in the month
    for day in range(1, days_in_month + 1):
        # Format the date as "dd-mm-yy"
        date_folder = datetime(year, month_num, day).strftime("%d-%m-%y")

        # Create the date folder inside the month folder
        day_folder_path = os.path.join(month_folder_path, date_folder)
        if not os.path.exists(day_folder_path):
            os.makedirs(day_folder_path)

print("Folders created successfully.")

