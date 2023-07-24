# Convolutional Neural Network Filter Visualization

## Project Media
![Dxxxxx](https://github.com/omerfaruktekin13/CNN_Filter_Visualization/blob/main/Media/1.png "Deneme ")
|:--:|
| *Random Picture from VGG16* |
![Dxxxxx](https://github.com/omerfaruktekin13/CNN_Filter_Visualization/blob/main/Media/2.png "Deneme ")
| *Filter at Block 1 Convolution 1/23* |
![Dxxxxx](https://github.com/omerfaruktekin13/CNN_Filter_Visualization/blob/main/Media/3.png "Deneme ") 
| *Filter at Block 2 Convolution 1/51* |
![Dxxxxx](https://github.com/omerfaruktekin13/CNN_Filter_Visualization/blob/main/Media/4.png "Deneme ") 
| *Filter at Block 2 Convolution 2/40* |
![Dxxxxx](https://github.com/omerfaruktekin13/CNN_Filter_Visualization/blob/main/Media/5.png "Deneme ") 
| *Filter at Block 3 Convolution 3/80* |
![Dxxxxx](https://github.com/omerfaruktekin13/CNN_Filter_Visualization/blob/main/Media/6.png "Deneme ") 
| *Filter at Block 5 Convolution 3/302* |

## Description
Ever wondered what filters created in Convolutional Neural Network layers look like? I have used the popular VGG16 model and visualized various filters from different layers of CNN. I did this by using the gradient ascent optimization algorithm to visualize images that maximally activate specific filters from different layers of the model. I have chosen TensorFlow as my machine learning framework. The first image represents the random picture that is chosen by the algorithm. 2nd, 3rd, 4th, and 5th images are randomly selected filters at a variety of blocks and convolutional layers, and their locations have shown in their title. It is obvious that, as you progress through the convolutional layers and blocks, you see that the images are more detailed and suitable for detailed filtering. At the last block of the VGG16 model, the trained network is already created its filter for the corresponding picture for classification. Furthermore, the loss function of the images increases as the block number increases because of its complex characterization but it is 0 at the block 5 location.

## Tools and Languages
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<p> * Python3 </p>
<p> * TensorFlow </p>
<p> * Keras </p>
<p> * Jupyter Notebook or any suitable integrated development environment (IDE) </p>

## Installation
> 1. Download the Main.py
> 2. Open it with any IDE which is suitable for Python Machine Learning.
> 3. You can change the iteration number to observe further information about filters and loss functions in the system.
> 4. Additionally, you can try other trained CNNs and look at image classification accuracy.

## Open to Development
Please share your comments and ideas about the project with me. Thank you for your time.
