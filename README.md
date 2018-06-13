# ANNArt
This project is concerned with making "art" using machine learning models.

The impetus behind this project is not to replace or make redundant art made by human artists; nor do I expect that the quality of the images produced will be anywhere near the quality required to achieve that.

Rather, this is an exploration of what algorithmic art might look like. How we might build these models, what works and what doesn't.

__

The first of these experiments was a single sample trained regressive ANN.

Provided with an input of 1 and output of an painting of a cow, the ANN was fit and then was asked to predict the image that 2 would represent.

Here it is!

![alt text](https://github.com/wa721/ANNArt/blob/master/masterpieceComparison.png?raw=true)

This is rather unsurprising given it was only trained on a single sample, however it does show how one might begin to build an "artistic" neural net, which, provided with a new subject, produces it's own piece.

__

The second example trained on the paintings dataset, generously made available through the Visual Geometr Group based out of Oxford (https://www.robots.ox.ac.uk/~vgg/data/paintings/). 

Trained on the animal images in this, with the number of legs and the height of the animal (sourced from my refined ability to know the number of legs a cow has and some wiki stats), asked the trained network to produce a four-legged, 120cm tall, 130cm long animal without wings. 

Here's it's result! 

![alt text](https://github.com/wa721/ANNArt/blob/master/ANNArt/masterpiece.jpg?raw=true)
