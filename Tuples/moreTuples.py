# welcome = 'Welcome to my nightmare', 'Alice Cooper', 1975
# bad = 'Bad Company' 'Bad Company', 1974
# budgie = 'Nightflight', 'budgie', 1981
# imelda = 'More Mayhem', 'Emilda May', 2011, (
#     (1, 'Pulling the Rug'), (2, 'Pyscho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz'))
#
# print(imelda)
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# one way to indent the tracks in the tuple by a tab
# for song in tracks:
#     print('\t', song)

# another way to indent the tracks in the tuple by a tab
imelda = 'More Mayhem', 'Emilda May', 2011, (
    [(1, 'Pulling the Rug'), (2, 'Pyscho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')])

print(imelda)

imelda[3].append((5, 'All For You'))

title, artist, year, tracks = imelda
tracks.append((6, 'All For You'))
print(title)
print(artist)
print(year)

print(imelda)

for song in tracks:
    trackNumbers, title = song
    print('\tTrackNumber: {}, Title: {}'.format(trackNumbers, title))

# Tuples are immutable(can't change) however, if a tuple contains a list within itself, the list itself is mutable
# (can change)

