class Artist:
	""" This is a class for capturing details for the artist.
		This will have member attributes of :
			1. artistName : String
			2. songList : Song[]
			3. albumList : Album[]
	"""

	def __init__(self, artistName=""):
		self.artistName = artistName		
		self.songList = []
		self.albumList = []
		

	def printArtist(self):
		print("Artist : ", self.artistName)
		print("=== Songs by artist ===")
		for track in self.songList:
			print("\t{}".format(track))
		print("=== Albums by artist ===")
		for album in self.albumList:
			print("\t{}".format(album))
	
	def addSong(self, song):
		self.songList.append(song)

	def addAlbum(self, album):
		self.albumList.append(album)

	def isContainsAlbum(self, album):
		if album in self.albumList:
			return True
		else:
			return False

	def isContainsSong(self, song):
		if song in self.songList:
			return True
		else:
			return False



if __name__ == '__main__':
	someArtist = Artist("Some Real Artist")
	someArtist.addSong("Song 1")
	someArtist.addSong("Song 2")
	someArtist.addSong("Song 3")
	someArtist.addAlbum("Album A")
	someArtist.addAlbum("Album B")

	someArtist.printArtist()
