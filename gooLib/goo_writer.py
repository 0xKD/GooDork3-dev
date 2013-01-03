"""
	Handles writing to specific outfile/ printing to stdout in case outfile not specified.
"""
import goo_csv
import goo_xml
import goo_JSON
import goo_html

class goo_writer:
	def __init__(self,config):
		self.config = config	
	def gooWriter(self,result):
		# Writes to specified outfile.
		print result