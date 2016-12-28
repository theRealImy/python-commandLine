#!/usr/bin/python3

if __name__ =='__main__':
	#0. working with files in Python
	import argparse
	import sys
	
	parser = argparse.ArgumentParser("read some arguments")
	parser.add_argument('input_file', type=str, help="Path to file to read")
	if len(sys.argv) < 1:
		parser.print_help()
		sys.exit(1)
	args = parser.parse_args()
	print ('file is ' + args.input_file)
	
	
