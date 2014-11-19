import csv
import re
import numpy

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

my_input = open('data.csv')
for f in my_input:
	if re.search("starttime", f): 
		pass
	else:
		start_time = f.split(",")[3]
		end_time = f.split(",")[4]
		s_time = start_time.replace("2013-","")
		e_time = end_time.replace("2013-","")
		start_t = s_time.replace("-",",")
		end_t = e_time.replace("-",",")
		s_t = start_t.replace(":",",")
		e_t = end_t.replace(":",",")
		start = s_t.replace(" ",",")
		end = e_t.replace(" ",",")
		starting_time = start.split(",")
		ending_time = end.split(",")
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
		#print Total_start_time
		#print Total_end_time
		hire_time = Total_end_time - Total_start_time
		hire_period.append(hire_time)

#print hire_period
print numpy.mean(hire_period)
#3253 characters