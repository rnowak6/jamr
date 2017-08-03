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
        if item == "rock":
            genreDict["rock"] = genreDict["rock"] + 1
        if item == "pop":
            genreDict['pop'] = genreDict['pop'] + 1
        if item == "metal":
            genreDict["metal"] = genreDict["metal"] + 1
        if item == "blues":
            genreDict["blues"] = genreDict["blues"] + 1
        if item == "dance pop":
            genreDict["dancepop"] = genreDict["dancepop"] + 1
        if item == "rap":
            genreDict["rap"] = genreDict["rap"] + 1
        if item == "tropical house":
            genreDict["tropicalHouse"] = genreDict["tropicalHouse"] + 1
        if item == "trap music":
            genreDict["trapMusic"] = genreDict["trapMusic"] + 1
        if item == "modern rock":
            genreDict["modernRock"] = genreDict["modernRock"] + 1
        if item == "hip hop":
            genreDict["hipHop"] = genreDict["hipHop"] + 1
        if item == "classical":
            genreDict["classical"] = genreDict["classical"] + 1
        if item == "latin":
            genreDict["latin"] = genreDict["latin"] + 1
        if item == "edm":
            genreDict["edm"] = genreDict["edm"] + 1
        if item == "alternative":
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
        "metal" : "burger place",
        "classical" : "Art Institute",
        "tropicalHouse" : "coffee shop",
        "trapMusic" : "road trip",
        "rap" : "park",
        "modernRock" : "",
        "hipHop": "dance class",
        "latin" : "fire house",
        "edm" : "nightclubs",
        "country" : "go south",
        "alternative" : "urban outfitters"
    }
    found=genreReference.get(playlistGenre,None)
    if found is None:
        return genreReference['country']
    else:
        return genreReference[playlistGenre]
# user=raw_input("Username: ")
# playlistGenre(getGenres(user))
