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
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    #print image
	# return the image
    #cv2. imwrite( "image.jpg", image)
    return image

#create a container for the image arrays
ExampleArt = []
labels = []
#specify the number of images (n-1)
maxNumImages = 0

#scrape the images
for image in range(0,1):
    IIQ = url_to_image(URLs.iloc[image,0]) #image in question
    labels.append(URLs.iloc[image,3])
    artItem = []
    for pixel in range(0,len(IIQ)-1):
        for section in range(0,540):
            artItem.append(IIQ[pixel][section][0])
            artItem.append(IIQ[pixel][section][1])
            artItem.append(IIQ[pixel][section][2])
    ExampleArt.append(artItem)
    print len(IIQ[0])
    print len(IIQ)


for item in range(0,len(labels)):
    if labels[item] == "cow":
        labels[item] = 1
    else:
        labels[item] = 2

#build the regressor

#this is the basic structure from sklearn including all of the parameters as a placeholder
artist = MLPRegressor(hidden_layer_sizes=(3,5,10), activation='relu', solver='adam', alpha=0.0001, batch_size='auto', learning_rate="constant")

#train the artist!
#example art is the y variable, labels is the x (remember we are telling the machine what to paint!)

artist.fit(labels,ExampleArt)

#specify the parameters of the "art" to be produced.
# list as [reds,greens,blues,subject,#objects,mood]
inspiration = [2]

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
for pixel in range(0,len(IIQ)-1):
    ImageContainer.append([])
    for section in range(0,540):
        ImageContainer[pixel].append(np.array([artwork[pixelCount],artwork[pixelCount+1],artwork[pixelCount+2]]))
        pixelCount += 3
    ImageContainer[pixel] = np.asarray(ImageContainer[pixel])

ImageContainer = np.asarray(ImageContainer)

cv2.imwrite("masterpiece.jpg",ImageContainer)
