import pdb 
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository  
import repositories.album_repository as album_repository

artist1 = Artist('Mac DeMarco')
artist_repository.save(artist1)
