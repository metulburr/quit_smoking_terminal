
class Achievement:
	def __init__(self):
		'''
		some_list = [
			{'name':{'value':0, 'info':'INFO STRING'}},
			{'name':{'value':0, 'info':'INFO STRING'}},
			where value is seconds in time and life lists, and number of cigs in cigs list
		]
		'''
		
		self.time_list = [
			{'First Hour Smoke Free':{'value':3600, 'info':'You have started on your journey with the first hour'}},
			{'8 Hours Smoke Free':{'value':28800, 'info':'You have gone 8 hours without a cigarette'}},
			{'12 Hours Smoke Free':{'value':43200, 'info':'You have gone 12 hours without a cigarette'}},
			{'24 Hours Smoke Free':{'value':86400, 'info':'You have gone 24 hours without a cigarette'}},
			{'2 Days Smoke Free':{'value':172800, 'info':'You have gone 2 Days without a cigarette'}},
			{'3 Days Smoke Free':{'value':259200, 'info':'You have gone 3 days without a cigarette'}},
			{'5 Days Smoke Free':{'value':432000, 'info':'You are 5 days smoke-free'}},
			{'1 Week Smoke Free':{'value':604800, 'info':'You are 1 week smoke-free'}},
			{'10 Days Smoke Free':{'value':864000, 'info':'You are 10 days smoke-free'}},
			{'2 Weeks Smoke Free':{'value':1209600, 'info':'You are 2 weeks smoke-free'}},
			{'15 Days Smoke Free':{'value':1296000, 'info':'You are 15 days smoke-free'}},
			{'21 Days Smoke Free':{'value':1814400, 'info':'You are 21 days smoke-free'}},
			{'25 Days Smoke Free':{'value':2160000, 'info':'You are 25 days smoke-free'}},
			{'1 Month Smoke Free':{'value':2678400, 'info':'You are 1 month smoke-free'}},
			{'5 Weeks Smoke Free':{'value':3024000, 'info':'You are 5 weeks smoke-free'}},
			{'6 Weeks Smoke Free':{'value':3628800, 'info':'You are 6 weeks smoke-free'}},
			{'8 Weeks Smoke Free':{'value':4838400, 'info':'You are 8 weeks smoke-free'}},
			{'10 Weeks Smoke Free':{'value':6048000, 'info':'You are 10 weeks smoke-free'}},
			{'12 Weeks Smoke Free':{'value':7257600, 'info':'You are 12 weeks smoke-free'}},
			{'6 Months Smoke Free':{'value':15778454, 'info':'You are 6 months smoke-free'}},
			{'1 Year Smoke Free':{'value':31556908, 'info':'You are 1 year smoke-free'}},
			{'2 Years Smoke Free':{'value':63113817, 'info':'You are 2 years smoke-free'}},
			{'3 Years Smoke Free':{'value':94670725, 'info':'You are 3 years smoke-free'}},
			{'5 Years Smoke Free':{'value':157784540, 'info':'You are 5 years smoke-free'}},
			{'10 Years Smoke Free':{'value':315569080, 'info':'You are 10 years smoke-free'}},
			{'15 Years Smoke Free':{'value':473353620, 'info':'You are 15 years smoke-free'}},
			{'20 Years Smoke Free':{'value':631138160, 'info':'You are 20 years smoke-free'}},
		]
		
		self.life_list = [
			#{'Saved 1 hour':{'value':3600, 'info':'You have an extra hour of life'}},
			{'Saved 8 Hours':{'value':28800, 'info':'You have saved 8 hours of your life'}},
			{'Saved 12 Hours':{'value':43200, 'info':'You have saved 12 hours of your life'}},
			{'Saved 24 Hours':{'value':86400, 'info':'You have saved 24 hours of your life'}},
			{'Saved 2 Days':{'value':172800, 'info':'You have saved 2 days of your life'}},
			{'Saved 3 Days':{'value':259200, 'info':'You have saved 3 days of your life'}},
			{'Saved 5 Days':{'value':432000, 'info':'You have saved 5 days of your life'}},
			{'Saved 1 Week':{'value':604800, 'info':'You have saved 1 week of your life'}},
			{'Saved 10 Days':{'value':864000, 'info':'You have saved 10 days of your life'}},
			{'Saved 2 Weeks':{'value':1209600, 'info':'You have saved 2 weeks of your life'}},
			{'Saved 15 Days':{'value':1296000, 'info':'You have saved 15 days of your life'}},
			{'Saved 21 Days':{'value':1814400, 'info':'You have saved 21 days of your life'}},
			{'Saved 25 Days':{'value':2160000, 'info':'You have saved 25 days of your life'}},
			{'Saved 1 Month':{'value':2678400, 'info':'You have saved 1 month of your life'}},
			#{'Saved 5 Weeks':{'value':3024000, 'info':'You have saved 5 weeks of your life'}},
			{'Saved 6 Weeks':{'value':3628800, 'info':'You have saved 6 weeks of your life'}},
			{'Saved 8 Weeks':{'value':4838400, 'info':'You have saved 8 weeks of your life'}},
			{'Saved 10 Weeks':{'value':6048000, 'info':'You have saved 10 weeks of your life'}},
			{'Saved 12 Weeks':{'value':7257600, 'info':'You have saved 12 weeks of your life'}},
			{'Saved 6 Months':{'value':15778454, 'info':'You have saved 6 months of your life'}},
			{'Saved 1 Year':{'value':31556908, 'info':'You have saved 1 year of your life'}},
			{'Saved 2 Years':{'value':63113817, 'info':'You have saved 2 years of your life'}},
			{'Saved 3 Years':{'value':94670725, 'info':'You have saved 3 years of your life'}},
			{'Saved 5 Years':{'value':157784540, 'info':'You have saved 5 years of your life'}},
			{'Saved 10 Years':{'value':315569080, 'info':'You have saved 10 years of your life'}},
			#{'Saved 15 Years':{'value':473353620, 'info':'You have saved 15 years of your life'}},
			#{'Saved 20 Years':{'value':631138160, 'info':'You have saved 20 years of your life'}},
		]
		
		self.cig_list = [
			{'Avoided 20 Cigarettes':{'value':20, 'info':'You have not smoked 20 cigarettes'}},
			{'Avoided 50 Cigarettes':{'value':50, 'info':'You have not smoked 50 cigarettes'}},
			{'Avoided 100 Cigarettes':{'value':100, 'info':'You have not smoked 100 cigarettes'}},
			{'Avoided 250 Cigarettes':{'value':250, 'info':'You have not smoked 250 cigarettes'}},
			{'Avoided 500 Cigarettes':{'value':500, 'info':'You have not smoked 500 cigarettes'}},
			{'Avoided 750 Cigarettes':{'value':750, 'info':'You have not smoked 750 cigarettes'}},
			{'Avoided 1,000 Cigarettes':{'value':1000, 'info':'You have not smoked 1,000 cigarettes'}},
			{'Avoided 1,500 Cigarettes':{'value':1500, 'info':'You have not smoked 1,500 cigarettes'}},
			{'Avoided 2,000 Cigarettes':{'value':2000, 'info':'You have not smoked 2,000 cigarettes'}},
			{'Avoided 2,500 Cigarettes':{'value':2500, 'info':'You have not smoked 2,500 cigarettes'}},
			{'Avoided 5,000 Cigarettes':{'value':5000, 'info':'You have not smoked 5,000 cigarettes'}},
			{'Avoided 7,500 Cigarettes':{'value':7500, 'info':'You have not smoked 7,500 cigarettes'}},
			{'Avoided 10,000 Cigarettes':{'value':10000, 'info':'You have not smoked 10,000 cigarettes'}},
			{'Avoided 25,000 Cigarettes':{'value':25000, 'info':'You have not smoked 25,000 cigarettes'}},
			{'Avoided 50,000 Cigarettes':{'value':50000, 'info':'You have not smoked 50,000 cigarettes'}},
			{'Avoided 75,000 Cigarettes':{'value':75000, 'info':'You have not smoked 75,000 cigarettes'}},
			{'Avoided 100,000 Cigarettes':{'value':100000, 'info':'You have not smoked 100,000 cigarettes'}},
			{'Avoided 150,000 Cigarettes':{'value':150000, 'info':'You have not smoked 150,000 cigarettes'}},
		]
	def stringer(self, name, info):
		return 'Achievement: "{}" {}\n'.format(name, info)
		
		
if __name__ == '__main__':
	def ach_string(lister_type, obj):
		'''
		lister  = ('time', 'life', 'cig')
		'''
		ach_obj = obj
		if lister_type == 'time':
			lister = ach_obj.time_list
		elif lister_type == 'life':
			lister = ach_obj.life_list
		elif lister_type == 'cig':
			lister = ach_obj.cig_list
		#time_since = time.time() - d['epoch_stamp']
		#total_cigs = self.total_cigs_not_smoked()
		#life_saved = self.life_saved()['total_sec']
		ach_string = ''

		#testing
		time_since = 370000
		total_cigs = 301
		life_saved = 3700
		
		for ach in lister:
			for key, val in ach.items():
				name = key
				value = val['value']
				info = val['info']
				if lister_type == 'time':
					if time_since >= value:
						ach_string += ach_obj.stringer(name, info)
				elif lister_type == 'life':
					if life_saved >= value:
						ach_string += ach_obj.stringer(name, info)
				elif lister_type == 'cig':
					if total_cigs >= value:
						ach_string += ach_obj.stringer(name, info)
		return ach_string


	ach_obj = Achievement()
	print(ach_string('time', ach_obj))
	print(ach_string('life', ach_obj))
	print(ach_string('cig', ach_obj))


