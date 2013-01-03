"""
	Handles writing to specific outfile/ printing to stdout in case outfile not specified.
"""
from goo_csv import goo_csv as csvwriter
import goo_xml
import goo_JSON
import goo_html

class goo_writer:
	def __init__(self,config):
		self.config = config	
	def gooWriter(self,result):
		self.result = result
		# Writes to specified outfile.
		if self.config.getOutFormat().lower() == 'csv':
			self.csv = csvwriter(self.config)
			self.csv.goo2CSV(self.result)