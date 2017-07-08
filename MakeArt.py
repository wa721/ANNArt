#exploration


#import the packages.
from sklearn.neural_network import MLPRegressor #the regressor
import pandas as pd #data wrangling
import matplotlib as plot #for plotting of the ANN structure or "art"
import cv2 #for presenting the "art"
import numpy as np #for some image transformations

#specify the parameters of the "art" to be produced.
# list as [#legs,height,length,wings?]
inspiration = [4,120,130,0]

artist = pickle.load(Savedartist)
#make the art
artwork = artist.predict(inspiration)
artwork = artwork[0]
m = max(artwork)
for colour in range(0,(len(artwork)-1)):
    artwork[colour] = int(artwork[colour]/m*255)
print artwork
#save the artwork!

ImageContainer = []
pixelCount = 0
for pixel in range(0,74):
    ImageContainer.append([])
    for section in range(0,99):
        ImageContainer[pixel].append(np.array([artwork[pixelCount],artwork[pixelCount+1],artwork[pixelCount+2]]))
        pixelCount += 3
    ImageContainer[pixel] = np.asarray(ImageContainer[pixel])

ImageContainer = np.asarray(ImageContainer)

cv2.imwrite("masterpiece.jpg",ImageContainer)
