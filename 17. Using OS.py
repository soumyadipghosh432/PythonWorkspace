import os

def listing(loc):

	def list_dir(d):
		nonlocal tab_stop
		items = os.listdir(d)
		for record in items:
			curr_dir = os.path.join(d, record)
			if os.path.isdir(curr_dir):
				print("\t" * tab_stop + "Directory : "+ record)
				tab_stop += 1 # incrementing tab_stop for sublevel
				list_dir(curr_dir) # Recursion for further level digging
				tab_stop -= 1
			else:
				print("\t" * tab_stop + record)


	tab_stop = 0
	if os.path.exists(loc):
		print("Dicrectory Listing for : "+ loc)
		list_dir(loc)
	else:
		print("Input directory does not exists in the system")


def listing_using_walk(d):
	listing = os.walk(d)
	print("=" * 15)
	for root, directories, files in listing:
		print("Root: " + root)
		print("=" * 15)
		for d in directories:
			print("Directory : "+ d)
		print("=" * 15)
		for f in files:
			print("File : "+ f)



listing("/home/soumyadip/PythonWorkspace")
listing_using_walk("/home/soumyadip/PythonWorkspace")
