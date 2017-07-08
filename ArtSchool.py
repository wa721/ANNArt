#exploration


#import the packages.
from sklearn.neural_network import MLPRegressor #the regressor
import pandas as pd #data wrangling
import matplotlib as plot #for plotting of the ANN structure or "art"
import cv2 #for presenting the "art"
import numpy as np #for some image transformations
import urllib #to scrape the images from URLs

#import some training da
URLs = pd.read_csv("painting_dataset.csv")

def url_to_image(url):
    #pull the image
    resp = urllib.urlopen(url)
    #convert it to an array
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    #resize it to 100:110 (landscape)
    image = cv2.resize(image, (100,75))
    return image

#create a container for the image arrays
ExampleArt = []
labels = []
#specify the number of images (n-1)
maxNumImages = 0

#scrape the images
for image in range(0,1000):
    #attribute the image in question
    IIQ = url_to_image(URLs.iloc[image,0]) #image in question
    #pull the label
    labels.append(URLs.iloc[image,3])
    artItem = []
    for pixel in range(0,74):
        for section in range(0,99):
            artItem.append(IIQ[pixel][section][0])
            artItem.append(IIQ[pixel][section][1])
            artItem.append(IIQ[pixel][section][2])
    ExampleArt.append(artItem)

#for the label, lets generate it as an array specifying
# the number of legs,
# the approximate height
# the apprximate length
# has wings?


labelDF = pd.DataFrame(index=range(1,len(labels)), columns=["legs","height","length","wings"])
labelDF = adjacency.fillna(0)

for item in range(0,len(labels)):
    if labels[item] == "cow":
        labelDF.iloc[item,1] = 4
        labelDF.iloc[item,2] = 117
        labelDF.iloc[item,3] = 259
        labelDF.iloc[item,4] = 0
    elif labels[item] == "sheep":
        labelDF.iloc[item,1] = 4
        labelDF.iloc[item,2] = 76
        labelDF.iloc[item,3] = 130
        labelDF.iloc[item,4] = 0
    elif labels[item] == "dog":
        labels[item] = [4,57,90,0]
        labelDF.iloc[item,1] = 4
        labelDF.iloc[item,2] = 57
        labelDF.iloc[item,3] = 90
        labelDF.iloc[item,4] = 0
    elif labels[item] == "horse":
        labelDF.iloc[item,1] = 4
        labelDF.iloc[item,2] = 160
        labelDF.iloc[item,3] = 240
        labelDF.iloc[item,4] = 0
    elif labels[item] == "bird":
        labelDF.iloc[item,1] = 2
        labelDF.iloc[item,2] = 20
        labelDF.iloc[item,3] = 15
        labelDF.iloc[item,4] = 1
#build the regressor

#this is the basic structure from sklearn including all of the parameters as a placeholder
artist = MLPRegressor(hidden_layer_sizes=(2,5,25,100), activation='relu', solver='adam', alpha=0.0001, batch_size='auto', learning_rate="constant")

#train the artist!
#example art is the y variable, labels is the x (remember we are telling the machine what to paint!)

artist.fit(labelDF,ExampleArt)


import pickle
Savedartist = pickle.dumps(artist)
print "School's out"
