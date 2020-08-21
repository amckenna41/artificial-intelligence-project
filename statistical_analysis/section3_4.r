#Section 3 Task 4

#To import excel file '40175607_features.xlsx' go to File - > Import Dataset - > From Excel -> 
#browse for file - > Import

#import the tigerstats library which will be used to plot the cut-off value and percentile using the pnormGC function
require(tigerstats)
#https://cran.r-project.org/web/packages/tigerstats/index.html

#convert csv file to dataframe
features_df<-as.data.frame(X40175607_features) ## data as dataframe

#Data set for all 160 items
features_df_all <- features_df[c(1:160),] 

#Calculate sample mean and standard deviation for the nr_pix variable for all 160 items 
sample_mean <- mean(features_df_all$nr_pix)
sample_mean
standard_dev <- sd(features_df_all$nr_pix)
standard_dev

#Calculate the cut-off value for the nr_pix variable such that if a random sample was taken
#95% of the time the sample will contain a value below this cut-off value and 5% of the time the sample
#will contain a value above this cut-off value 
#qnorm function has the arguments - percentile, mean, standard deviation 

y <- qnorm(0.95, sample_mean, standard_dev)
y

#plot a graph showing the shaded area of the 95% percentile for nr_pix

pnormGC(y,region="below",sample_mean,
        standard_dev,graph=TRUE)

