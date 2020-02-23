# artificial-intelligence-project
Repository for artificial intelligence project for respective computer science module. 

Objective:
The objective of this project was to create a variety of machine learning and classification algorithms and techniques for a 
given dataset of images. The dataset consisted of 8 types of images, split into a living and non-living dataset with image
types: cherry, banana, pear, flower as living and envelope, pencil, golfclub, wineglasss as non-living. All of these images 
were made up of a simple 50x50 black and white image array with the object in the image made up of black pixels with the rest as white pixels. The first part of this project involved creating 20 images for each type myself with a total of 160 images to use for classification and feature extraction. The second part of the project involved a total of 4000 training images from the image types in the aim of training machine learning models. Ultiamtely, the aim of the feature extraction and model training was to be able to successfully classify new images tas the correct type hat were input into the models. 

Languages Used:
In this project I mainly used R but for the intial image dataset creation and the feature engineering I used Python. To intially create the dataset I had to convert the raw images of the objects into matrices and dataframes and export to CSV files which I used the Python Pandas framework for. I also used Python for creating features that would be useful in classifying the different image types. The remainder of the project inclduing statistic analysis, machine learning modelling and classification was all done in R. 

Feature Engineering/Extraction:
After creating the image datasets I implemented various features that would be useful in differentiating the image types. These features were implemented in Python and some features included height and width of the image, number of pixels in image, max euclidean distance between 2 pixel, number of regions, number of eyes and many more. Ultimately these features will then be used to determine which variables and classifiers will be most useful in differentiating the image types, when building the machine learning models. 

Statistical Analysis:
I carried out various statistical analysis on the feature data and visualised the data using a variety of techniques in R. I calculated summary statistics for each feature visualising the spread of the features in histograms, scatterplots, boxplots, graphs etc. I calculated the probability distribution of each feature along with its probability density function. I carried out various statistical comparisons techniques between features including t-tests, ANOVA, F-distribution, hypothesis testing, correlation testing/coefficents etc. 

Classification Model:
The features that were created from the images were used to decide on the appropriate classifiers/variables used in the creation of the machine learning models. I used various models and techniques including: regression (logistic and multiple regression), 5-Fold Cross-Validation, KNN, bagging, decision trees, random forests, pruning etc. The reliability and performance of each of these models was worked out using a test dataset of images. The best performing model would then be used as the model of preference for classifcation of future similar images. 
