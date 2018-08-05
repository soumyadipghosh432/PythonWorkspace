import song as songClass
import artist as artistClass


class Album:
	""" This is a class to capture the details for albums.
		This class will have the following member attributes :
			1. albumName : String
			2. artist : Object of Artist
			3. songs : dictionary of { track# : (object of song, duration in seconds) }
			4. publishYear : number
			5. trackCount : Class level variable
		This class will have folowwing member functions :
			1. printAlbum() : this will print the album details in formatted way
			2. addSong() : Add song to album
			3. addArtist() : Add artist to album
	"""
	trackCount = 0

	def __init__(self, albumName="", publishYear=0):
		self.albumName = albumName
		self.artist = []
		self.songs = {}
		self.publishYear = publishYear

	def printAlbum(self):
		print("======== Details for Album : {} ========".format(self.albumName))
		print("Album composed by : {}".format(self.getArtists()))
		print("Album published on : {}".format(self.publishYear))
		print("Album tracks === >")
		for track in range(self.trackCount):
			song, dur = self.songs[track]
			songName = song.songName
			print("\t{} # {} : {:6} seconds".format(track, songName, dur))


	def addSong(self, song, duration):
		self.songs[self.trackCount] = (song, duration)
		self.trackCount += 1

	def addArtist(self, artist):
		if not self.isContainsArtist(artist):
			self.artist.append(artist)

	def getArtists(self):
		art = ""
		for x in self.artist:
			if len(art) > 2:
				art += ", " + x.artistName
			else:
				art += x.artistName
		return art

	def isContainsSong(self, song):
		counter = 0
		for x in self.songs:
			songObj, duration = self.songs[x]
			if songObj.songName == song:
				counter += 1
		if counter > 0:
			return True
		else:
			return False

	def isContainsArtist(self, artist):
		if not artist in self.artist:
			return False
		else:
			return True



if __name__ == '__main__':
	abc = songClass.Song("abc", "someArtist","someAlbum")
	xyz = songClass.Song("xyz", "someArtist","someAlbum")

	someArtist = artistClass.Artist("Some Artist")
	someAnotherArtist = artistClass.Artist("Some Another Artist")

	myAlbum = Album("New Album", 2018)
	myAlbum.addArtist(someArtist)
	myAlbum.addArtist(someAnotherArtist)
	myAlbum.addSong(abc, 300)
	myAlbum.addSong(xyz, 250)

	myAlbum.printAlbum()
