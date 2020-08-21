#Section 3 task 6 - Finding linear association between height and span variable for living, non-living and both things

#To import excel file '40175607_features.xlsx' go to File - > Import Dataset - > From Excel -> 
#browse for file - > Import

#import csv file and convert to dataframe 
features_df<-as.data.frame(X40175607_features) ## data as dataframe

#get all rows and columns for living and non-living things
features_df_living <- features_df[1:80,] #get all rows of living things
features_df_nonliving <- features_df[81:160,] #get all rows of non-living things

#get height and span columns for living things
living_height <- features_df_living$height
living_height
living_span <- features_df_living$span
living_span

#get height and span columns for non-living things
nonliving_height <- features_df_nonliving$height
nonliving_height
nonliving_span <- features_df_nonliving$span
nonliving_span

#get height and span columns for all things
all_height <- features_df$height
all_height
all_span <- features_df$span
all_span

#plot scatterplot for height and span for living things 
#Scatterplot used to show the linear association , if any , between x and y variables 

plot(living_height, living_span , main="Scatterplot Span ~ Height \n for living things",
     xlab="Height ", ylab="Span")

#add lowess line of fit
lines(lowess(living_height, living_span), col = "green", lwd = 3)


#plot scatterplot for height and span for non-living things 

plot(nonliving_height, nonliving_span , main="Scatterplot Span ~ Height \n for non-living things",
     xlab="Height ", ylab="Span")

#add lowess line of fit
lines(lowess(nonliving_height, nonliving_span), col = "blue", lwd = 3)


#plot scatterplot for height and span for all things 

plot(all_height, all_span , main="Scatterplot Span ~ Height \n for all things",
     xlab="Height ", ylab="Span")

#add lowess line of fit
lines(lowess(all_height, all_span), col = "cyan", lwd = 3)


#Pearson coorelation coefficent between height and span of living, non-living and all things

#Value will be between -1 and 1. 1 = Strong positive correlation, -1 = Strong negative correclation 
cor.test(living_height,living_span)

cor.test(nonliving_height,nonliving_span)

cor.test(all_height,all_span)
