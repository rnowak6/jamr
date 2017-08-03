import spotipy
import pprint
import sys
import spotipy.util as util
import os
from spotipy.oauth2 import SpotifyClientCredentials
import json
from spotipyintegration import getGenres

def playlistGenre(getGenres):
    genreDict = {
        "rock" : 0,
        "pop" : 0,
        "metal" : 0,
        "blues" : 0,
        "dancepop" : 0,
        "rap" : 0,
        "tropicalHouse" : 0,
        "trapMusic" : 0,
        "modernRock" : 0,
        "hipHop" : 0,
        "classical" : 0,
        "latin" : 0,
        "edm" : 0,
        "alternative" : 0
    }
    for item in getGenres:
        if item == "rock" or item == "classic rock" or item == "hard rock" or item == "garage rock":
            genreDict["rock"] = genreDict["rock"] + 1
        if item == "pop" or item == "pop rap" or item == "post-teen pop" or item == "pop rock" or item == "viral pop":
            genreDict['pop'] = genreDict['pop'] + 1
        if item == "metal" or item == "alternative metal" or item == "nu metal" or item == "rap metal":
            genreDict["metal"] = genreDict["metal"] + 1
        if item == "blues" or item == "soul" or item == "blues rock" or item == "jazz blues":
            genreDict["blues"] = genreDict["blues"] + 1
        if item == "dance pop":
            genreDict["dancepop"] = genreDict["dancepop"] + 1
        if item == "rap" or item == "urban contemporary" or item == "dirty south rap" or item == "gangster rap":
            genreDict["rap"] = genreDict["rap"] + 1
        if item == "tropical house" or item =="neo mellow" or item == "mello gold" or item == "indietronica" or item == "synthpop" or item == "tropical":
            genreDict["tropicalHouse"] = genreDict["tropicalHouse"] + 1
        if item == "trap music" or item == "dwn trap" or item == "trap latino" or item == "electric trap" or item == "bass trap":
            genreDict["trapMusic"] = genreDict["trapMusic"] + 1
        if item == "modern rock" or item == "":
            genreDict["modernRock"] = genreDict["modernRock"] + 1
        if item == "hip hop" or item == "latin hip hop" or item == "underground hip hop" or item == "deep german hip hop" or item == "hardcore hip hop" or item == "east coast hip hop":
            genreDict["hipHop"] = genreDict["hipHop"] + 1
        if item == "classical":
            genreDict["classical"] = genreDict["classical"] + 1
        if item == "latin" or item == "latin hip hip" or item == "latin pop" or item == "latin alternative" or item == "spanish pop" or item == "trap latino":
            genreDict["latin"] = genreDict["latin"] + 1
        if item == "edm" or item == "progressive electro house" or item == "noise pop" or item == "tracestep":
            genreDict["edm"] = genreDict["edm"] + 1
        if item == "alternative" or item == "alternative rock" or item == "indie pop" or item == "soft rock" or item == "indie folk" or item == "alternative dance" or item == "christian alternative rock":
            genreDict["alternative"] = genreDict["alternative"] + 1

        maxNumber = 0
        maxGenre = ""
        for genre in genreDict:
            if genreDict[genre] > maxNumber:
                maxNumber = genreDict[genre]
                maxGenre = genre
    # print genreDict
    # print maxGenre
    return maxGenre


def assignLocation(playlistGenre):

    genreReference = {
        "pop" : "beach",
        "dancepop" : "zumba",
        "metal" : "motorcycles",
        "classical" : "Art Institute",
        "tropicalhouse" : "coffee shop",
        "trap" : "tattoo",
        "rap" : "Home depot",
        "modernRock" : "barber shop",
        "hiphop": "dance class",
        "latin" : "salon",
        "edm" : "nightclubs",
        "country" : "old crow",
        "alternative" : "urban outfitters"
    }
    found=genreReference.get(playlistGenre,None)
    if found is None:
        return genreReference['country']
    else:
        return genreReference[playlistGenre]
# user=raw_input("Username: ")
# playlistGenre(getGenres(user))
