import datetime
import time

class Timer:
	def __init__(self):
		self.time_string = ''
		self.time_pattern = '%m/%d/%Y %I:%M %p'
		self.time_stamp = 0
		self.time_since = self.time_since_stamp(self.time_stamp)
		
		#self.is_pc_daylight_saving_time_on = len(set(time.tzname)) != 1 #check if pc has daylight on or not
		#self.update(time_stamp=time.time()) #make default data
		
	def update(self, time_string=None, time_stamp=None, time_pattern=None):
		'''update class variables'''
		if time_string:
			dt = datetime.datetime.strptime(time_string, self.time_pattern)
			self.time_stamp =  int(time.mktime(dt.timetuple()))
			self.time_string = time_string
		elif time_stamp:
			self.time_stamp = int(time_stamp)
			self.time_string = time.strftime(self.time_pattern, time.localtime(time_stamp))
		elif time_pattern:
			self.time_string = time.strftime(time_pattern, time.localtime(self.time_stamp))
			self.time_pattern = time_pattern
		self.time_since = self.time_since_stamp(self.time_stamp)
		
	def time_since_stamp(self, time_stamp, dst_on_setting=False):
		'''update time since the timestamp'''
		current_time = time.time()
		diff = current_time - float(time_stamp)
		if dst_on_setting:
			if time.localtime().tm_isdst:
				diff += 3600 #add daylight savings time hour (in seconds)

		sincetime_sec = int(diff)

		sincetime_min = (diff / 60)
		sincetime_min_rem = int((diff % 60))

		sincetime_hour = (sincetime_min / 60)
		sincetime_hour_rem = int((sincetime_min % 60))

		sincetime_day = (sincetime_hour / 24)
		sincetime_day_rem = int((sincetime_hour % 24))

		data = {
			'day':int(sincetime_day),
			'hour':sincetime_day_rem,
			'sec':sincetime_min_rem,
			'min':sincetime_hour_rem,
			'total_sec':sincetime_sec
			}
		return data

if __name__ == '__main__':
	timer = Timer()
	print(timer.time_stamp)
	print(timer.time_pattern)
	print(timer.time_string)
	print(timer.time_since)

	print('\n---\n')

	timer.update(time_string='02/16/2013 02:30 AM')
	print(timer.time_stamp)
	print(timer.time_pattern)
	print(timer.time_string)
	print(timer.time_since)

	print('\n---\n')

	timer.update(time_stamp=time.time())
	print(timer.time_stamp)
	print(timer.time_pattern)
	print(timer.time_string)
	print(timer.time_since)

	print('\n---\n')

	timer.update(time_pattern='%m---%d---%Y %I:%M %p')
	print(timer.time_stamp)
	print(timer.time_pattern)
	print(timer.time_string)
	print(timer.time_since)

