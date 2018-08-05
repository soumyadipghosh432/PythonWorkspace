class Song:
	""" This is the class for capturing the details of songs.
		This will have member attributes :
			1. songName : String
			2. artistName : String
			3. albumName : String
		This will have member functions :
			1. __init__ : Constructor for object with input as 
							a. songName
							b. artistName
							c. albumName
	"""

	def __init__(self, songName="", artistName="", albumName=""):
		""" This is the constructor for Song class """
		self.songName = songName
		self.artistName = artistName
		self.albumName = albumName
	
	def printSong(self):
		print("{} is composed by {} in album {}".format(self.songName,self.artistName,self.albumName))



if __name__ == "__main__":
	abc = Song("abc", "artist", "someAlbum")
	abc.printSong()
	abc1 = Song("abc1", "artist", "someAlbum")
	abc1.printSong()
