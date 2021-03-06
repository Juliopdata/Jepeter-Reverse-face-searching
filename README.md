# <p align="center"> Jepeter </p>


  <p align="center"> <img  src="https://github.com/Juliopdata/Jepeter-Reverse-face-searching/blob/master/static/logo.png" width="600"></p>

## Description

**Jepeter** is my own testing lightweight reverse search engine with Python, OpenCV and an Autoencoder in Keras to find people with similar faces in an unlabeled image dataset that can be easily scaled. 

Face recognition performance is evaluated with the [LFW dataset](http://vis-www.cs.umass.edu/lfw/) which you can replace with your own custom dataset.

Detect, transform, and crop faces on input images, use the autoencoder to extract 128-dimensional representations, or embeddings, of faces from the aligned input images compare input embedding vectors to labeled embedding vectors in a database.


<p align="center"> <img  src="https://github.com/Juliopdata/Jepeter-Reverse-face-searching/blob/master/graphics/modelloss.png" width="400"></p>

## Used tools

For Jepeter to be built, these are the tools I used:
- **OpenCV** to frame the faces and for image processing
- **Keras** (**Tensorflow**) allows us to stack layers of different types to create a deep neural network 
- **Html** for the web interface
- **Flask** for the interactive interface

<p align="center"> <img  src="https://github.com/Juliopdata/Jepeter-Reverse-face-searching/blob/master/graphics/mush.png" width="500"></p>

## Next Steps

- Improve the image processing
- Test different kinds of deep neural networks
- A more robust approach using KNN classification with a Euclidean distance metric. Alternatively, a linear support vector machine (SVM)
