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

print("=" * 25)
print("Using OS module for operating system operations")
print("=" * 25)

cmd = "pwd"
os.system(cmd)

print(os.getcwd())  # Returns current working directory\
print(os.environ["LANGUAGE"])  # Returns the env variable specified. Get full from linux using 'env' command in terminal
print(os.getgid())  # Return the real group id of the current process.
print(os.getuid())  # Return the current process’s user id
print(os.getpid())  # Returns the real process ID of the current process
print(os.uname())   # Return information identifying the current operating system

uname = list(os.uname())
print(uname[1])  # returns only the nodename

# few other commands with parameters. params need to be defiuned manually
os.umask(mask)       # Set the current numeric umask and return the previous umask
os.chroot(path)      # Change the root directory of the current process to path.   
os.listdir(path)     # Return a list of the entries in the directory given by path.
os.mkdir(path)       # Create a directory named path with numeric mode mode.
os.makedirs(path)    # Recursive directory creation function.
os.remove(path)      # Remove (delete) the file path.
os.removedirs(path)  # Remove directories recursively.
os.rename(src, dst)  # Rename the file or directory src to dst.
os.rmdir(path)       # Remove (delete) the directory path.
