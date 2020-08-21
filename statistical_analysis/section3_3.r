#Section 3 Task 3

#To import excel file '40175607_features.xlsx' go to File - > Import Dataset - > From Excel -> 
#browse for file - > Import

#convert csv file to dataframe
features_df<-as.data.frame(X40175607_features) ## data as dataframe

#Data set for all 160 items
features_df_all <- features_df[c(1:160),] 

#Calculate sample mean, variance and standard dev
sample_mean <- mean(features_df_all$nr_pix)
sample_mean

sample_variance <- var(features_df_all$nr_pix)
sample_variance

standard_dev <- sqrt(sample_variance)
standard_dev

#x-axis created from a sequence of numbers 40 - 220 to incorporate all nr_pix values
x <- seq(40,220)

#Calculate the probability density for the normal distribution
#dnorm function takes aruments x, sample mean and standard deviation 
#x value is sequence of numbers 40 - 220, sample mean and standard dev values were calculated above

y <- dnorm(x, sample_mean, standard_dev)

#Plot normal distribution
plot(x, y, main="Normal distribution for nr_pix", type = "l",ylab ="Probability Density", xlab = "Number of pixels")

#place a line in the distribution where the sample mean is 
abline(v=sample_mean, col ="red", lty = 2, lwd =3)

#Histogram for nr_pix for living and non-living things
hist(features_df$nr_pix, main="Histogram of nr_pix for \n living and non-living things", xlab ="Nr_pix", col="cyan")
abline(v = mean(features_df$nr_pix), col ="red", lty = 2, lwd = 3)

