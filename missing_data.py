# step in bash =
# sort -k1,1 -t ',' -k4,4 data.csv > data_sorted.csv

import re

my_input = ''
start_ID = ''
end_ID = ''
unrecorded = 0
missing = 0
No_data_points = float(0)
bike_ID = ''
hire_period = []
Hour_count = 3600
Day_count = 86400
Min_count = 60
Jan = 31 * Day_count
Feb = 28 * Day_count
Mar = 31 * Day_count
Apr = 30 * Day_count
May = 31 * Day_count
Jun = 30 * Day_count
Jul = 31 * Day_count
Aug = 31 * Day_count
First_8_months = Jan + Feb + Mar + Apr + May + Jun + Jul + Aug
Sep = 30 * Day_count + First_8_months
Oct = 31 * Day_count + Sep
Nov = 30 * Day_count + Oct
Dec = 31 * Day_count + Nov
unrecorded_time = float(0)
Total_start_time = 0
Total_end_time = 0

my_input = open('data_sorted.csv')
for f in my_input:
	if re.search("starttime", f): 
		pass
	else:
		new_bike_ID = f.split(",")[0]
		No_data_points += 1
		if bike_ID == new_bike_ID:
			#print "passed 1st criteria"
			start_ID = f.split(",")[2]
			start_time = f.split(",")[3]
			s_time = start_time.replace("2013-","")
			start_t = s_time.replace("-",",")
			s_t = start_t.replace(":",",")
			start = s_t.replace(" ",",")
			starting_time = start.split(",")
			if end_ID != start_ID:
				#print "passed 2nd criteria"
				missing += 1
				if starting_time[0] == '09':
					month_in_s = int(First_8_months)
					day_in_s = int(starting_time[1]) * Day_count
					hour_in_s = int(starting_time[2]) * Hour_count
					min_in_s = int(starting_time[3]) * Min_count
					sec_in_s = int(starting_time[4])
				elif starting_time[0] == '10':
					month_in_s = int(Sep)
					day_in_s = int(starting_time[1]) * Day_count
					hour_in_s = int(starting_time[2]) * Hour_count
					min_in_s = int(starting_time[3]) * Min_count
					sec_in_s = int(starting_time[4])
				elif starting_time[0] == '11':
					month_in_s = Oct
					day_in_s = int(starting_time[1]) * Day_count
					hour_in_s = int(starting_time[2]) * Hour_count
					min_in_s = int(starting_time[3]) * Min_count
					sec_in_s = int(starting_time[4])
				elif starting_time[0] == '12':
					month_in_s = Nov
					day_in_s = int(starting_time[1]) * Day_count
					hour_in_s = int(starting_time[2]) * Hour_count
					min_in_s = int(starting_time[3]) * Min_count
					sec_in_s = int(starting_time[4])
				Total_start_time = month_in_s + day_in_s + hour_in_s + min_in_s + sec_in_s
				unrecorded_time = Total_start_time - Total_end_time
				#print unrecorded_time
				unrecorded += 1
		end_ID = f.split(",")[1]
		bike_ID = f.split(",")[0]
		end_time = f.split(",")[4]
		e_time = end_time.replace("2013-","")
		end_t = e_time.replace("-",",")
		e_t = end_t.replace(":",",")
		end = e_t.replace(" ",",")
		ending_time = end.split(",")
		if ending_time[0] == '09':
			month_in_s = int(First_8_months)
			day_in_s = int(ending_time[1]) * Day_count
			hour_in_s = int(ending_time[2]) * Hour_count
			min_in_s = int(ending_time[3]) * Min_count
			sec_in_s = int(ending_time[4])
		elif ending_time[0] == '10':
			month_in_s = Sep
			day_in_s = int(ending_time[1]) * Day_count
			hour_in_s = int(ending_time[2]) * Hour_count
			min_in_s = int(ending_time[3]) * Min_count
			sec_in_s = int(ending_time[4])
		elif ending_time[0] == '11':
			month_in_s = Oct
			day_in_s = int(ending_time[1]) * Day_count
			hour_in_s = int(ending_time[2]) * Hour_count
			min_in_s = int(ending_time[3]) * Min_count
			sec_in_s = int(ending_time[4])
		elif ending_time[0] == '12':
			month_in_s = Nov
			day_in_s = int(ending_time[1]) * Day_count
			hour_in_s = int(ending_time[2]) * Hour_count
			min_in_s = int(ending_time[3]) * Min_count
			sec_in_s = int(ending_time[4])
		Total_end_time = month_in_s + day_in_s + hour_in_s + min_in_s + sec_in_s
missing_fraction = unrecorded / No_data_points
#print unrecorded
#print No_data_points
print missing_fraction