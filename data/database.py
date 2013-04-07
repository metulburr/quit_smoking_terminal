import json
import os

class QSDatabase:
	def __init__(self):
		self.filename = os.path.join('data', 'quitsmoking.dat')
		
	def save(self, obj):
		f = open(self.filename, 'w')
		f.write(json.dumps(obj))
		f.close()

	def load(self):
		json_data = open(self.filename)
		j = json.load(json_data)
		json_data.close()
		return j

if __name__ == '__main__':
	j = QSDatabase()
	obj = {'hello test':123}
	j.save(obj)
	data = j.load()
