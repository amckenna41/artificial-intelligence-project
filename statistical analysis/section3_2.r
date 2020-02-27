#Section 3 Task 2 

#To import excel file '40175607_features.xlsx' go to File - > Import Dataset - > From Excel -> 
#browse for file - > Import

#install ggplot2 module - for histograms, and e1071 module for numerically representing skew with skewness function
library(ggplot2)
install.packages('e1071', dependencies=TRUE)
library(e1071)
#https://cran.r-project.org/web/packages/e1071/e1071.pdf

#import data as dataframe
features_df<-as.data.frame(X40175607_features) 

features_df_living <- features_df[1:80,] #get all rows of living things
features_df_nonliving <- features_df[81:160,] #get all rows of non-living things
features_df_all <- features_df[1:160, ] #get all rows for both

#Summary statistics used for this task - mean, standard deviation, minimum value and max value
#variance statistic not used in report. 

#####################################
#Summary statistics for living things
#####################################

#initialise vectors to hold statistics
mean_vector <- vector()
stddev_vector <- vector()
min_vector <- vector()
max_vector <- vector()
var_vector <- vector()

#Summary statistics for nr_pix
mean_vector <- c(mean_vector, (mean(features_df_living$nr_pix)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$nr_pix)))
min_vector <- c(min_vector, (min(features_df_living$nr_pix)))
max_vector <- c(max_vector, (max(features_df_living$nr_pix)))
var_vector <- c(var_vector, (var(features_df_living$nr_pix)))

#Summary statistics for height
mean_vector <- c(mean_vector, (mean(features_df_living$height)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$height)))
min_vector <- c(min_vector, (min(features_df_living$height)))
max_vector <- c(max_vector, (max(features_df_living$height)))
var_vector <- c(var_vector, (var(features_df_living$height)))

#Summary statistics for width
mean_vector <- c(mean_vector, (mean(features_df_living$width)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$width)))
min_vector <- c(min_vector, (min(features_df_living$width)))
max_vector <- c(max_vector, (max(features_df_living$width)))
var_vector <- c(var_vector, (var(features_df_living$width)))

#Summary statistics for span
mean_vector <- c(mean_vector, (mean(features_df_living$span)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$span)))
min_vector <- c(min_vector, (min(features_df_living$span)))
max_vector <- c(max_vector, (max(features_df_living$span)))
var_vector <- c(var_vector, (var(features_df_living$span)))

#Summary statistics for rowswith5
mean_vector <- c(mean_vector, (mean(features_df_living$rows_with_5)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$rows_with_5)))
min_vector <- c(min_vector, (min(features_df_living$rows_with_5)))
max_vector <- c(max_vector, (max(features_df_living$rows_with_5)))
var_vector <- c(var_vector, (var(features_df_living$rows_with_5)))

#Summary statistics for colswith5
mean_vector <- c(mean_vector, (mean(features_df_living$cols_with_5)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$cols_with_5)))
min_vector <- c(min_vector, (min(features_df_living$cols_with_5)))
max_vector <- c(max_vector, (max(features_df_living$cols_with_5)))
var_vector <- c(var_vector, (var(features_df_living$cols_with_5)))

#Summary statistics for neigh1
mean_vector <- c(mean_vector, (mean(features_df_living$neigh1)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$neigh1)))
min_vector <- c(min_vector, (min(features_df_living$neigh1)))
max_vector <- c(max_vector, (max(features_df_living$neigh1)))
var_vector <- c(var_vector, (var(features_df_living$neigh1)))

#Summary statistics for neigh5
mean_vector <- c(mean_vector, (mean(features_df_living$neigh5)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$neigh5)))
min_vector <- c(min_vector, (min(features_df_living$neigh5)))
max_vector <- c(max_vector, (max(features_df_living$neigh5)))
var_vector <- c(var_vector, (var(features_df_living$neigh5)))

#Summary statistics for left2tile
mean_vector <- c(mean_vector, (mean(features_df_living$left2tile)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$left2tile)))
min_vector <- c(min_vector, (min(features_df_living$left2tile)))
max_vector <- c(max_vector, (max(features_df_living$left2tile)))
var_vector <- c(var_vector, (var(features_df_living$left2tile)))

#Summary statistics for right2tile
mean_vector <- c(mean_vector, (mean(features_df_living$right2tile)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$right2tile)))
min_vector <- c(min_vector, (min(features_df_living$right2tile)))
max_vector <- c(max_vector, (max(features_df_living$right2tile)))
var_vector <- c(var_vector, (var(features_df_living$right2tile)))

#Summary statistics for verticalness
mean_vector <- c(mean_vector, (mean(features_df_living$verticalness)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$verticalness)))
min_vector <- c(min_vector, (min(features_df_living$verticalness)))
max_vector <- c(max_vector, (max(features_df_living$verticalness)))
var_vector <- c(var_vector, (var(features_df_living$verticalness)))

#Summary statistics for top2tile
mean_vector <- c(mean_vector, (mean(features_df_living$top2tile)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$top2tile)))
min_vector <- c(min_vector, (min(features_df_living$top2tile)))
max_vector <- c(max_vector, (max(features_df_living$top2tile)))
var_vector <- c(var_vector, (var(features_df_living$top2tile)))

#Summary statistics for bottom2tile
mean_vector <- c(mean_vector, (mean(features_df_living$bottom2tile)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$bottom2tile)))
min_vector <- c(min_vector, (min(features_df_living$bottom2tile)))
max_vector <- c(max_vector, (max(features_df_living$bottom2tile)))
var_vector <- c(var_vector, (var(features_df_living$bottom2tile)))

#Summary statistics for horizontalness
mean_vector <- c(mean_vector, (mean(features_df_living$horizontalness)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$horizontalness)))
min_vector <- c(min_vector, (min(features_df_living$horizontalness)))
max_vector <- c(max_vector, (max(features_df_living$horizontalness)))
var_vector <- c(var_vector, (var(features_df_living$horizontalness)))

#Summary statistics for neigh8
mean_vector <- c(mean_vector, (mean(features_df_living$neigh8)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$neigh8)))
min_vector <- c(min_vector, (min(features_df_living$neigh8)))
max_vector <- c(max_vector, (max(features_df_living$neigh8)))
var_vector <- c(var_vector, (var(features_df_living$neigh8)))

#Summary statistics for white3tile
mean_vector <- c(mean_vector, (mean(features_df_living$white3tile)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$white3tile)))
min_vector <- c(min_vector, (min(features_df_living$white3tile)))
max_vector <- c(max_vector, (max(features_df_living$white3tile)))
var_vector <- c(var_vector, (var(features_df_living$white3tile)))

#Summary statistics for nr_regions
#Values for this may be different to the values used in the report due to the 
#nr_regions feature generating a random value during each execution of the feature
mean_vector <- c(mean_vector, (mean(features_df_living$nr_regions)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$nr_regions)))
min_vector <- c(min_vector, (min(features_df_living$nr_regions)))
max_vector <- c(max_vector, (max(features_df_living$nr_regions)))
var_vector <- c(var_vector, (var(features_df_living$nr_regions)))

#Summary statistics for nr_eyes
mean_vector <- c(mean_vector, (mean(features_df_living$nr_eyes)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$nr_eyes)))
min_vector <- c(min_vector, (min(features_df_living$nr_eyes)))
max_vector <- c(max_vector, (max(features_df_living$nr_eyes)))
var_vector <- c(var_vector, (var(features_df_living$nr_eyes)))

#Summary statistics for hollowness
mean_vector <- c(mean_vector, (mean(features_df_living$hollowness)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$hollowness)))
min_vector <- c(min_vector, (min(features_df_living$hollowness)))
max_vector <- c(max_vector, (max(features_df_living$hollowness)))
var_vector <- c(var_vector, (var(features_df_living$hollowness)))

#Summary statistics for black_pix_proportion
mean_vector <- c(mean_vector, (mean(features_df_living$black_pixel_proportion)))
stddev_vector <- c(stddev_vector, (sd(features_df_living$black_pixel_proportion)))
min_vector <- c(min_vector, (min(features_df_living$black_pixel_proportion)))
max_vector <- c(max_vector, (max(features_df_living$black_pixel_proportion)))
var_vector <- c(var_vector, (var(features_df_living$black_pixel_proportion)))

#get values of vectors holding statistics for each feature
mean_vector
stddev_vector
min_vector
max_vector

#########################################
#Summary statistics for non-living things
#########################################

#initialise vectors to hold statistics
mean_vector_nonliving <- vector()
stddev_vector_nonliving <- vector()
min_vector_nonliving <- vector()
max_vector_nonliving <- vector()
var_vector_nonliving <- vector()

#Summary statistics for nr_pix
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$nr_pix)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$nr_pix)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$nr_pix)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$nr_pix)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$nr_pix)))

#Summary statistics for height
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$height)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$height)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$height)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$height)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$height)))

#Summary statistics for width
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$width)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$width)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$width)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$width)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$width)))

#Summary statistics for span
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$span)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$span)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$span)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$span)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$span)))

#Summary statistics for rowswith5
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$rows_with_5)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$rows_with_5)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$rows_with_5)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$rows_with_5)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$rows_with_5)))

#Summary statistics for colswith5
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$cols_with_5)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$cols_with_5)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$cols_with_5)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$cols_with_5)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$cols_with_5)))

#Summary statistics for neigh1
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$neigh1)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$neigh1)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$neigh1)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$neigh1)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$neigh1)))

#Summary statistics for neigh5
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$neigh5)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$neigh5)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$neigh5)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$neigh5)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$neigh5)))

#Summary statistics for left2tile
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$left2tile)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$left2tile)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$left2tile)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$left2tile)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$left2tile)))

#Summary statistics for right2tile
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$right2tile)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$right2tile)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$right2tile)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$right2tile)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$right2tile)))

#Summary statistics for verticalness
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$verticalness)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$verticalness)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$verticalness)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$verticalness)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$verticalness)))

#Summary statistics for top2tile
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$top2tile)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$top2tile)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$top2tile)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$top2tile)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$top2tile)))

#Summary statistics for bottom2tile
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$bottom2tile)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$bottom2tile)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$bottom2tile)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$bottom2tile)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$bottom2tile)))

#Summary statistics for horizontalness
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$horizontalness)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$horizontalness)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$horizontalness)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$horizontalness)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$horizontalness)))

#Summary statistics for neigh8
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$neigh8)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$neigh8)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$neigh8)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$neigh8)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$neigh8)))

#Summary statistics for white3tile
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$white3tile)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$white3tile)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$white3tile)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$white3tile)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$white3tile)))

#Summary statistics for nr_regions
#Values for this may be different to the values used in the report due to the 
#nr_regions feature generating a random value during each execution of the feature
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$nr_regions)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$nr_regions)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$nr_regions)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$nr_regions)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$nr_regions)))

#Summary statistics for nr_eyes
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$nr_eyes)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$nr_eyes)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$nr_eyes)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$nr_eyes)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$nr_eyes)))

#Summary statistics for hollowness
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$hollowness)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$hollowness)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$hollowness)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$hollowness)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$hollowness)))

#Summary statistics for black_pix_proportion
mean_vector_nonliving <- c(mean_vector_nonliving, (mean(features_df_nonliving$black_pixel_proportion)))
stddev_vector_nonliving <- c(stddev_vector_nonliving, (sd(features_df_nonliving$black_pixel_proportion)))
min_vector_nonliving <- c(min_vector_nonliving, (min(features_df_nonliving$black_pixel_proportion)))
max_vector_nonliving <- c(max_vector_nonliving, (max(features_df_nonliving$black_pixel_proportion)))
var_vector_nonliving <- c(var_vector_nonliving, (var(features_df_nonliving$black_pixel_proportion)))

#get values of vectors holding statistics for each feature
mean_vector_nonliving
stddev_vector_nonliving
min_vector_nonliving
max_vector_nonliving

#####################################
#Summary statistics for all things
#####################################

#initialise vectors to hold statistics calculations
mean_vector_all <- vector()
stddev_vector_all <- vector()
min_vector_all <- vector()
max_vector_all <- vector()
var_vector_all <- vector()

#Summary statistics for nr_pix
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$nr_pix)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$nr_pix)))
min_vector_all <- c(min_vector_all, (min(features_df_all$nr_pix)))
max_vector_all <- c(max_vector_all, (max(features_df_all$nr_pix)))
var_vector_all <- c(var_vector_all, (var(features_df_all$nr_pix)))

#Summary statistics for height
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$height)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$height)))
min_vector_all <- c(min_vector_all, (min(features_df_all$height)))
max_vector_all <- c(max_vector_all, (max(features_df_all$height)))
var_vector_all <- c(var_vector_all, (var(features_df_all$height)))

#Summary statistics for width
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$width)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$width)))
min_vector_all <- c(min_vector_all, (min(features_df_all$width)))
max_vector_all <- c(max_vector_all, (max(features_df_all$width)))
var_vector_all <- c(var_vector_all, (var(features_df_all$width)))

#Summary statistics for span
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$span)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$span)))
min_vector_all <- c(min_vector_all, (min(features_df_all$span)))
max_vector_all <- c(max_vector_all, (max(features_df_all$span)))
var_vector_all <- c(var_vector_all, (var(features_df_all$span)))

#Summary statistics for rowswith5
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$rows_with_5)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$rows_with_5)))
min_vector_all <- c(min_vector_all, (min(features_df_all$rows_with_5)))
max_vector_all <- c(max_vector_all, (max(features_df_all$rows_with_5)))
var_vector_all <- c(var_vector_all, (var(features_df_all$rows_with_5)))

#Summary statistics for colswith5
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$cols_with_5)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$cols_with_5)))
min_vector_all <- c(min_vector_all, (min(features_df_all$cols_with_5)))
max_vector_all <- c(max_vector_all, (max(features_df_all$cols_with_5)))
var_vector_all <- c(var_vector_all, (var(features_df_all$cols_with_5)))

#Summary statistics for neigh1
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$neigh1)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$neigh1)))
min_vector_all <- c(min_vector_all, (min(features_df_all$neigh1)))
max_vector_all <- c(max_vector_all, (max(features_df_all$neigh1)))
var_vector_all <- c(var_vector_all, (var(features_df_all$neigh1)))

#Summary statistics for neigh5
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$neigh5)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$neigh5)))
min_vector_all <- c(min_vector_all, (min(features_df_all$neigh5)))
max_vector_all <- c(max_vector_all, (max(features_df_all$neigh5)))
var_vector_all <- c(var_vector_all, (var(features_df_all$neigh5)))

#Summary statistics for left2tile
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$left2tile)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$left2tile)))
min_vector_all <- c(min_vector_all, (min(features_df_all$left2tile)))
max_vector_all <- c(max_vector_all, (max(features_df_all$left2tile)))
var_vector_all <- c(var_vector_all, (var(features_df_all$left2tile)))

#Summary statistics for right2tile
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$right2tile)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$right2tile)))
min_vector_all <- c(min_vector_all, (min(features_df_all$right2tile)))
max_vector_all <- c(max_vector_all, (max(features_df_all$right2tile)))
var_vector_all <- c(var_vector_all, (var(features_df_all$right2tile)))

#Summary statistics for verticalness
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$verticalness)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$verticalness)))
min_vector_all <- c(min_vector_all, (min(features_df_all$verticalness)))
max_vector_all <- c(max_vector_all, (max(features_df_all$verticalness)))
var_vector_all <- c(var_vector_all, (var(features_df_all$verticalness)))

#Summary statistics for top2tile
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$top2tile)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$top2tile)))
min_vector_all <- c(min_vector_all, (min(features_df_all$top2tile)))
max_vector_all <- c(max_vector_all, (max(features_df_all$top2tile)))
var_vector_all <- c(var_vector_all, (var(features_df_all$top2tile)))

#Summary statistics for bottom2tile
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$bottom2tile)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$bottom2tile)))
min_vector_all <- c(min_vector_all, (min(features_df_all$bottom2tile)))
max_vector_all <- c(max_vector_all, (max(features_df_all$bottom2tile)))
var_vector_all <- c(var_vector_all, (var(features_df_all$bottom2tile)))

#Summary statistics for horizontalness
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$horizontalness)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$horizontalness)))
min_vector_all <- c(min_vector_all, (min(features_df_all$horizontalness)))
max_vector_all <- c(max_vector_all, (max(features_df_all$horizontalness)))
var_vector_all <- c(var_vector_all, (var(features_df_all$horizontalness)))

#Summary statistics for neigh8
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$neigh8)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$neigh8)))
min_vector_all <- c(min_vector_all, (min(features_df_all$neigh8)))
max_vector_all <- c(max_vector_all, (max(features_df_all$neigh8)))
var_vector_all <- c(var_vector_all, (var(features_df_all$neigh8)))

#Summary statistics for white3tile
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$white3tile)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$white3tile)))
min_vector_all <- c(min_vector_all, (min(features_df_all$white3tile)))
max_vector_all <- c(max_vector_all, (max(features_df_all$white3tile)))
var_vector_all <- c(var_vector_all, (var(features_df_all$white3tile)))

#Summary statistics for nr_regions
#Values for this may be different to the values used in the report due to the 
#nr_regions feature generating a random value during each execution of the feature
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$nr_regions)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$nr_regions)))
min_vector_all <- c(min_vector_all, (min(features_df_all$nr_regions)))
max_vector_all <- c(max_vector_all, (max(features_df_all$nr_regions)))
var_vector_all <- c(var_vector_all, (var(features_df_all$nr_regions)))

#Summary statistics for nr_eyes
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$nr_eyes)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$nr_eyes)))
min_vector_all <- c(min_vector_all, (min(features_df_all$nr_eyes)))
max_vector_all <- c(max_vector_all, (max(features_df_all$nr_eyes)))
var_vector_all <- c(var_vector_all, (var(features_df_all$nr_eyes)))

#Summary statistics for hollowness
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$hollowness)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$hollowness)))
min_vector_all <- c(min_vector_all, (min(features_df_all$hollowness)))
max_vector_all <- c(max_vector_all, (max(features_df_all$hollowness)))
var_vector_all <- c(var_vector_all, (var(features_df_all$hollowness)))

#Summary statistics for black_piexel_proportion
mean_vector_all <- c(mean_vector_all, (mean(features_df_all$black_pixel_proportion)))
stddev_vector_all <- c(stddev_vector_all, (sd(features_df_all$black_pixel_proportion)))
min_vector_all <- c(min_vector_all, (min(features_df_all$black_pixel_proportion)))
max_vector_all <- c(max_vector_all, (max(features_df_all$black_pixel_proportion)))
var_vector_all <- c(var_vector_all, (var(features_df_all$black_pixel_proportion)))

#get values of vectors holding statistics for each feature
mean_vector_all
stddev_vector_all
min_vector_all
max_vector_all

###########################################################
#Histograms for features that may be useful in distinguishing
#between living and non-living things 
##########################################################

#Red line in histogram represents the mean, 2 gray lines represent the mean +/- the standard deviation of the values from the mean in both directions
#Histograms for nr_pix for living things 
hist(features_df_living$nr_pix, main = "Histogram for number of pixels \n for living things", breaks = 8, col ="green", xlab = "Number of pixels")
abline(v = mean_vector[1], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[1] + stddev_vector[1]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[1] - stddev_vector[1]) , col ="gray", lty = 1, lwd = 3)
skewness(features_df_living$nr_pix)

#Histograms for nr_pix for non- living things 
hist(features_df_nonliving$nr_pix, main = "Histogram for number of pixels \n for non-living things", breaks = 8, col ="blue", xlab = "Number of pixels")
abline(v = mean_vector_nonliving[1], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector_nonliving[1] + stddev_vector_nonliving[1]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector_nonliving[1] - stddev_vector_nonliving[1]) , col ="gray", lty = 1, lwd = 3)
skewness(features_df_nonliving$nr_pix)

#Histograms for neigh5 for living things 
hist(features_df_living$neigh5, main = "Histogram for number of pixels with 5 neighbours \n for living things", breaks = 8, col ="green", xlab = "Number of pixels with 5 or more neighbours")
abline(v = mean_vector[8], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[8] + stddev_vector[8]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[8] - stddev_vector[8]) , col ="gray", lty = 1, lwd = 3)
skewness(features_df_living$neigh5)

#Histograms for neigh5 for non-living things 
hist(features_df_nonliving$neigh5, main = "Histogram for number of pixels with 5 neighbours \n for non-living things", breaks = 8, col ="blue", xlab = "Number of pixels with 5 or more neighbours")
abline(v = mean_vector_nonliving[8], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector_nonliving[8] + stddev_vector_nonliving[8]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector_nonliving[8] - stddev_vector_nonliving[8]) , col ="gray", lty = 1, lwd = 3)
skewness(features_df_nonliving$neigh5)

#Histograms for right2tile for living things 
hist(features_df_living$right2tile, main = "Histogram for number of right2tiles \n for living things", breaks = 8, col ="green", xlab = "Number of right2tiles")
abline(v = mean_vector[10], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[10] + stddev_vector[10]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[10] - stddev_vector[10]) , col ="gray", lty = 1, lwd = 3)
skewness(features_df_living$right2tile)

#Histograms for right2tile for non-living things 
hist(features_df_nonliving$right2tile, main = "Histogram for number of right2tiles\n for non-living things", breaks = 8, col ="blue", xlab = "Number of right2iles")
abline(v = mean_vector_nonliving[10], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector_nonliving[10] + stddev_vector_nonliving[10]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector_nonliving[10] - stddev_vector_nonliving[10]) , col ="gray", lty = 1, lwd = 3)
skewness(features_df_nonliving$right2tile)

#Histograms for top2tile for living things 
hist(features_df_living$top2tile, main = "Histogram for number of top2tiles \n for living things", breaks = 8, col ="green", xlab = "Number of top2tiles")
abline(v = mean_vector[12], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[12] + stddev_vector[12]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[12] - stddev_vector[12]) , col ="gray", lty = 1, lwd = 3)
skewness(features_df_living$top2tile)

#Histograms for top2tile for non-living things 
hist(features_df_nonliving$top2tile, main = "Histogram for number of top2tile \n for non-living things", breaks = 8, col ="blue", xlab = "Number of top2tiles")
abline(v = mean_vector_nonliving[12], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector_nonliving[12] + stddev_vector_nonliving[12]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector_nonliving[12] - stddev_vector_nonliving[12]) , col ="gray", lty = 1, lwd = 3)
skewness(features_df_nonliving$top2tile)

#Histograms for bottom2tile for living things 
hist(features_df_living$bottom2tile, main = "Histogram for number of bottom2tiles \n for living things", breaks = 8, col ="green", xlab = "Number of bottom2tiles")
abline(v = mean_vector[13], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[13] + stddev_vector[13]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[13] - stddev_vector[13]) , col ="gray", lty = 1, lwd = 3)
skewness(features_df_living$bottom2tile)

#Histograms for bottom2tile for non-living things 
hist(features_df_nonliving$bottom2tile, main = "Histogram for number of bottom2tiles \n for non-living things", breaks = 8, col ="blue", xlab = "Number of bottom2tiles")
abline(v = mean_vector_nonliving[13], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector_nonliving[13] + stddev_vector_nonliving[13]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector_nonliving[13] - stddev_vector_nonliving[13]) , col ="gray", lty = 1, lwd = 3)
skewness(features_df_nonliving$bottom2tile)

#Histograms for neigh8 for living things 
hist(features_df_living$neigh8, main = "Histogram for number of 8 neighbours \n for living things", breaks = 8, col ="green", xlab = "Number of pixels with 8 neighbours")
abline(v = mean_vector[15], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[15] + stddev_vector[15]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[15] - stddev_vector[15]) , col ="gray", lty = 1, lwd = 3)
skewness(features_df_living$neigh8)

#Histograms for neigh8 for non-living things 
hist(features_df_nonliving$neigh8, main = "Histogram for number of 8 neighbours \n for non-living things", breaks = 8, col ="blue", xlab = "Number of pixels with 8 neighbours")
abline(v = mean_vector_nonliving[15], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector_nonliving[15] + stddev_vector_nonliving[15]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector_nonliving[15] - stddev_vector_nonliving[15]) , col ="gray", lty = 1, lwd = 3)
skewness(features_df_nonliving$neigh8)

