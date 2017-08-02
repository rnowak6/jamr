import spotipy
import pprint
import sys
import spotipy.util as util
import os
from spotipy.oauth2 import SpotifyClientCredentials
import json


def playlistGenre(ameliasMethodreturn):
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
        "alternative" : 0,
    }
    for item in listFromAmeliasMethodReturn():
        if item == "rock":
            genreDict["rock"] +=
        if item == "pop":
            genreDict['pop'] +=
        if item == "metal":
            genreDict["metal"] +=
        if item == "blues" or item == "blues-rock":
            genreDict["blues"] +=
        if item == "dance pop":
            genreDict["dancepop"] +=
        if item == "rap":
            genreDict["rap"] +=
        if item == "tropical house":
            genreDict["tropicalHouse"] +=
        if item == "trap music":
            genreDict["trapMusic"] +=
        if item == "modern rock":
            genreDict["modernRock"] +=
        if item == "hip hop":
            genreDict["hipHop"] +=
        if item == "classical":
            genreDict["classical"] +=
        if item == "latin":
            genreDict["latin"] +=
        if item == "edm":
            genreDict["edm"] +=
        if item == "alternative":
            genreDict["alternative"] +=
            
        maxNumber = 0
        maxGenre = ""
        for genre in genreDict:
            if genreDict[genre] > maxNumber:
                maxNumber = genreDict[genre]
                maxGenre = genre
    return maxGenre


def assignLocation(playlistGenre):

    genreReference = {
        "pop" : "go to the beach",
        "dance pop" : "zumba class",
        "metal" : "Eva's burger place",
        "classical" : "CSO, Art Institute",
        "tropical house" : "coffee shop",
        "trap" : "road trip",
        "rap" : "",
        "modern rock" : "",
        "hip hop": "dance class",
        "latin" : "",
        "edm" : "nightclubs",
        "country" : "go south",
        "alternative rock" : "urban outfitters"
    }
    return genreReference[playlistGenre]
