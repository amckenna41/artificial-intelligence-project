#Section 3 Task 1 Histograms for nr_pix, height and cols_with 5

#To import excel file '40175607_features.xlsx' go to File - > Import Dataset - > From Excel -> 
#browse for file - > Import

#import csv file as dataframe 
features_df<-as.data.frame(X40175607_features)

#dataframe for living things
features_df_living <- features_df[c(1:80),] #get all rows of living things
features_df_nonliving <- features_df[c(81:160),] #get all rows of living things
features_df_all <- features_df[c(1:160),] #get all rows for all things

#red dashed line represents mean of feature

#Histograms for living things
hist(features_df_living$nr_pix, main="Histogram of number of pixels for living things", xlab ="Number of pixels", col="green")
abline(v = mean(features_df_living$nr_pix), col ="red", lty = 2, lwd = 3)

hist(features_df_living$height, main="Histogram of height for living things", xlab ="Height", col="green")
abline(v = mean(features_df_living$height), col ="red", lty = 2, lwd = 3)

hist(features_df_living$cols_with_5, main="Histogram of columns with 5 or more black pixels \n for living things", xlab ="Cols with 5", col="green")
abline(v = mean(features_df_living$cols_with_5), col ="red", lty = 2, lwd = 3)
 

#Histograms for non-living things
hist(features_df_nonliving$nr_pix, main="Histogram of number of pixels for \n non-living things", xlab ="Number of pixels", col="blue")
abline(v = mean(features_df_nonliving$nr_pix), col ="red", lty = 2, lwd = 3)

hist(features_df_nonliving$height, main="Histogram of height for \n non-living things", xlab ="Height", col="blue")
abline(v = mean(features_df_nonliving$height), col ="red", lty = 2, lwd = 3)

hist(features_df_nonliving$cols_with_5, main="Histogram of columns with 5 or more black pixels \n for non-living things", xlab ="Cols with 5", col="blue")
abline(v = mean(features_df_nonliving$cols_with_5), col ="red", lty = 2, lwd = 3)


#Histograms for both things
hist(features_df_all$nr_pix, main="Histogram of number of pixels for \n non-living & living things", xlab="Number of pixels", col="cyan")
abline(v = mean(features_df_all$nr_pix), col ="red", lty = 2, lwd = 3)

hist(features_df_all$height, main="Histogram of height for \n non-living & living things", xlab="Height", col="cyan")
abline(v = mean(features_df_all$height), col ="red", lty = 2, lwd = 3)

hist(features_df_all$cols_with_5, main="Histogram of columns with 5 or more black pixels for \n non-living & living things", xlab="Cols with 5", col="cyan")
abline(v = mean(features_df_all$cols_with_5), col ="red", lty = 2, lwd = 3)
