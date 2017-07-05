#exploration


#import the packages.
from sklearn.neural_network import MLPRegressor #the regressor
import pandas as pd #data wrangling
import matplotlib as plot #for plotting of the ANN structure or "art"
import cv2 #for presenting the "art"

#import some training da
ExampleArt = []
maxNumImages
for image in range(1,maxNumImages):
    ExampleArt[image] = pd.read_csv(####)

#to be determined

#build the regressor

#this is the basic structure from sklearn including all of the parameters as a placeholder
artist = MLPRegressor(hidden_layer_sizes=(3,5,10), activation='relu', solver='adam', alpha=0.0001, batch_size='auto', learning_rate='constant', learning_rate_init=0.001, power_t=0.5, max_iter=200, shuffle=True, random_state=None, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)


#train the artist!
artist.fit(TrainingParameters,ExampleArt)

#specify the parameters of the "art" to be produced.
# list as [reds,greens,blues,subject,#objects,mood]
inspiration = [20,50,20,2,50,10]

#make the art
artwork = artist.predict(inspiration)

#plot the artwork!
cv.imshow('dst_rt', artwork)
cv.waitKey(0)
cv.destroyAllWindows()
