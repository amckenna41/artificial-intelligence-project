#Section3 Task #5 - identifying skewed feature data and transforming them

#To import excel file '40175607_features.xlsx' go to File - > Import Dataset - > From Excel -> 
#browse for file - > Import

#import e1071 library which has the skewness feature used for numerically getting skew of data

install.packages('e1071', dependencies=TRUE)
library(e1071)
#https://cran.r-project.org/web/packages/e1071/e1071.pdf

#import csv and convert to dataframe
features_df<-as.data.frame(X40175607_features) ## data as dataframe
features_df_all <- features_df[1:160, ] #get all rows for both

#####################################
#Histograms for features 1 - 14 
#####################################

#Histograms plotted to identify features that have extreme skew in either the left or right direction
#Features that possess a large skew will then be transformed 
#Red line on histogram = mean
#Grey line on histogram = standard deviation in +ve and -ve directions

hist(features_df_all$nr_pix, main = "Histogram for number of black pixels", breaks = 8, col ="cyan", xlab = "Number of pixels")
abline(v = mean_vector[1], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[1] + stddev_vector[1]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[1] - stddev_vector[1]) , col ="gray", lty = 1, lwd = 3)

hist(features_df_all$height, main = "Histogram for height", breaks = 8, col ="cyan", xlab = "Height")
abline(v = mean_vector[2], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[2] + stddev_vector[2]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[2] - stddev_vector[2]) , col ="gray", lty = 1, lwd = 3)

hist(features_df_all$width, main = "Histogram for width", breaks = 8, col ="cyan", xlab = "Width")
abline(v = mean_vector[3], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[3] + stddev_vector[3]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[3] - stddev_vector[3]) , col ="gray", lty = 1, lwd = 3)

hist(features_df_all$span, main = "Histogram for span", breaks = 8, col ="cyan", xlab = "Span")
abline(v = mean_vector[4], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[4] + stddev_vector[4]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[4] - stddev_vector[4]) , col ="gray", lty = 1, lwd = 3)

hist(features_df_all$rows_with_5, main = "Histogram for rows with \n 5 or more black pixels", breaks = 8, col ="cyan", xlab = "Rows with 5 or more black pixels")
abline(v = mean_vector[5], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[5] + stddev_vector[5]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[5] - stddev_vector[5]) , col ="gray", lty = 1, lwd = 3)

hist(features_df_all$cols_with_5, main = "Histogram for columns with \n 5 or more black pixels", breaks = 8, col ="cyan", xlab = "Columns with 5 or more black pixels")
abline(v = mean_vector[6], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[6] + stddev_vector[6]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[6] - stddev_vector[6]) , col ="gray", lty = 1, lwd = 3)

hist(features_df_all$neigh1, main = "Histogram for black pixels \n with exactly one neighbour", breaks = 8, col ="cyan", xlab = "Black pixels with 1 neighbour")
abline(v = mean_vector[7], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[7] + stddev_vector[7]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[7] - stddev_vector[7]) , col ="gray", lty = 1, lwd = 3)

hist(features_df_all$neigh5, main = "Histogram for black pixels \n with 5 or more neighbours", breaks = 8, col ="cyan", xlab = "Black pixels with 5 or more neighbours")
abline(v = mean_vector[8], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[8] + stddev_vector[8]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[8] - stddev_vector[8]) , col ="gray", lty = 1, lwd = 3)

hist(features_df_all$left2tile, main = "Histogram for left2tile", breaks = 8, col ="cyan", xlab = "left2tile value")
abline(v = mean_vector[9], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[9] + stddev_vector[9]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[9] - stddev_vector[9]) , col ="gray", lty = 1, lwd = 3)

hist(features_df_all$right2tile, main = "Histogram for right2tile", breaks = 8, col ="cyan", xlab = "right2tile value")
abline(v = mean_vector[10], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[10] + stddev_vector[10]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[10] - stddev_vector[10]) , col ="gray", lty = 1, lwd = 3)

hist(features_df_all$verticalness, main = "Histogram for verticalness", breaks = 8, col ="cyan", xlab = "Verticalness")
abline(v = mean_vector[11], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[11] + stddev_vector[11]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[11] - stddev_vector[11]) , col ="gray", lty = 1, lwd = 3)

hist(features_df_all$top2tile, main = "Histogram for top2tile", breaks = 8, col ="cyan", xlab = "top2tile value")
abline(v = mean_vector[12], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[12] + stddev_vector[12]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[12] - stddev_vector[12]) , col ="gray", lty = 1, lwd = 3)

hist(features_df_all$bottom2tile, main = "Histogram for bottom2tile", breaks = 8, col ="cyan", xlab = "bottom2tile value")
abline(v = mean_vector[13], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[13] + stddev_vector[13]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[13] - stddev_vector[13]) , col ="gray", lty = 1, lwd = 3)

hist(features_df_all$horizontalness, main = "Histogram for horizontalness", breaks = 8, col ="cyan", xlab = "horizontalness")
abline(v = mean_vector[14], col ="red", lty = 2, lwd = 3)
abline(v = (mean_vector[14] + stddev_vector[14]) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean_vector[14] - stddev_vector[14]) , col ="gray", lty = 1, lwd = 3)

#Variables that can be seen to have an extreme skew to the left or right are:
#rows_with_5, cols_with_5, neigh1, neigh5, top2tile, bottom2tile and horizontalness

#Log transformations of skewed features
#Red line represents the mean of the data 
#2 gray lines represent the upper and lower bounds of the standard deviation

log_rows_with_5 = log(features_df_all$rows_with_5)
hist(log_rows_with_5, main = "Log Transformation for rows with \n 5 or more black pixels", breaks = 8, col ="cyan", xlab = "Rows with 5 or more black pixels")
abline(v = mean(log_rows_with_5), col ="red", lty = 2, lwd = 3)
abline(v = (mean(log_rows_with_5) + sd(log_rows_with_5)) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean(log_rows_with_5) - sd(log_rows_with_5)) , col ="gray", lty = 1, lwd = 3)

log_cols_with_5 = log(features_df_all$cols_with_5)
hist(log_cols_with_5, main = "Log Transformation for columns with \n 5 or more black pixels", breaks = 8, col ="cyan", xlab = "Columns with 5 or more black pixels")
abline(v = mean(log_cols_with_5), col ="red", lty = 2, lwd = 3)
abline(v = (mean(log_cols_with_5) + sd(log_cols_with_5)) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean(log_cols_with_5) - sd(log_cols_with_5)) , col ="gray", lty = 1, lwd = 3)

log_neigh1 = log(features_df_all$neigh1)
hist(log_neigh1, main = "Log Transformation for black pixels \n with exactly one neighbour", breaks = 8, col ="cyan", xlab = "Black pixels with 1 neighbour")
abline(v = mean(log_neigh1), col ="red", lty = 2, lwd = 3)
abline(v = (mean(log_neigh1) + sd(log_neigh1)) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean(log_neigh1) - sd(log_neigh1)) , col ="gray", lty = 1, lwd = 3)

log_neigh5 = log(features_df_all$neigh5)
hist(log_neigh5, main = "Log Transformation for black pixels \n with 5 or more neighbours", breaks = 8, col ="cyan", xlab = "Black pixels with 5 or more neighbours")
abline(v = mean(log_neigh5), col ="red", lty = 2, lwd = 3)
abline(v = (mean(log_neigh5) + sd(log_neigh5)) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean(log_neigh5) - sd(log_neigh5)) , col ="gray", lty = 1, lwd = 3)

log_top2tile = log(features_df_all$top2tile)
hist(log_top2tile, main = "Log Transformation for top2tile", breaks = 8, col ="cyan", xlab = "Top2tile value")
abline(v = mean(log_top2tile), col ="red", lty = 2, lwd = 3)
abline(v = (mean(log_top2tile) + sd(log_top2tile)) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean(log_top2tile) - sd(log_top2tile)) , col ="gray", lty = 1, lwd = 3)

log_bottom2tile = log(features_df_all$bottom2tile)
hist(log_bottom2tile, main = "Log Transformation for bottom2tile", breaks = 8, col ="cyan", xlab = "Bottom2tile value")
abline(v = mean(log_bottom2tile), col ="red", lty = 2, lwd = 3)
abline(v = (mean(log_bottom2tile) + sd(log_bottom2tile)) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean(log_bottom2tile) - sd(log_bottom2tile)) , col ="gray", lty = 1, lwd = 3)

log_horizontalness = log(features_df_all$horizontalness)
hist(log_horizontalness, main = "Log Transformation for horizontalness", breaks = 8, col ="cyan", xlab = "Horizontalness")
abline(v = mean(log_horizontalness), col ="red", lty = 2, lwd = 3)
abline(v = (mean(log_horizontalness) + sd(log_horizontalness)) , col ="gray", lty = 1, lwd = 3)
abline(v = (mean(log_horizontalness) - sd(log_horizontalness)) , col ="gray", lty = 1, lwd = 3)

