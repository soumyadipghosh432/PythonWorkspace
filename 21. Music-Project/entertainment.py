import album as albumClass
import artist as artistClass
import song as songClass


allSongs = []
allArtists = []
allAlbums = []

def printAllSongs():
	print("=" * 35, "Printing all songs ", "=" * 35, ">")
	for x in allSongs:
		x.printSong()

def printAllArtists():
	print("=" * 35, "Printing all artists ", "=" * 33, ">")
	for x in allArtists:
		x.printArtist()

def printAllAlbums():
	print("=" * 35, "Printing all albums ", "=" * 34, ">")
	for x in allAlbums:
		x.printAlbum()


def getArtist(artistName):
	for x in allArtists:
		if x.artistName == artistName:
			return x

def getSong(name):
	for x in allSongs:
		if x.songName == name:
			return x

def getAlbum(name):
	for x in allAlbums:
		if x.albumName == name:
			return x



if __name__ == "__main__":

	

	with open("listOfSongs.txt", "r") as listOfSongs:
		
		songObj = songClass.Song()
		artistObj = artistClass.Artist()
		albumObj = albumClass.Album()

		for record in listOfSongs:
			albumName, publishYr, artistName, songName, duration = tuple(record.strip("\n").split("\t"))
			
			#  Create / Retrieve Song
			if songObj.songName != songName:
				if not songName in allSongs:
					songObj = songClass.Song(songName, artistName, albumName)
					allSongs.append(songObj)
				else:
					songObj = getSong(songName)


			#  Create / Retrieve Artist
			if artistObj.artistName != artistName:
				if not artistName in allArtists:
					artistObj = artistClass.Artist(artistName)
					allArtists.append(artistObj)
				else:
					artistObj = getArtist(artistName)

			if not artistObj.isContainsSong(songName):
				artistObj.addSong(songName)

			if not artistObj.isContainsAlbum(albumName):
				artistObj.addAlbum(albumName)


			#  Create / Retrieve Album
			if albumObj.albumName != albumName:
				if not albumName in allAlbums:
					albumObj = albumClass.Album(albumName, publishYr)
					allAlbums.append(albumObj)
				else:
					albumObj = getArtist(albumName)

			if not albumObj.isContainsSong(songName):
				albumObj.addSong(songObj, duration)
			
			if not albumObj.isContainsArtist(artistName):
				albumObj.addArtist(artistObj)
	
	printAllSongs()
	printAllArtists()
	printAllAlbums()
