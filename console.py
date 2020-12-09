import pdb 
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository  
import repositories.album_repository as album_repository

artist1 = Artist('Mac DeMarco')
artist_repository.save(artist1)

album1 = Album('Salad Days', 'Rock', artist1)
album_repository.save(album1)

artist_repository.select_all()
