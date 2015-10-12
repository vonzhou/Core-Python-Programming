#P198

albums = ('Poe', 'Gaudi', 'Freud', 'Ppe2')
years = (1987, 2001, 2013, 2015)

for album in sorted(albums):
	print album,

for album in reversed(albums):
	print album,

print

for i, album in enumerate(albums):
	print i, album

for album,yr in zip(albums, years):
	print yr, album
	