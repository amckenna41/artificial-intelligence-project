#Section 3 Task 7 - check if nr_pix feature can be useful to discriminate between, wineglass, golfclub, pencil and envelope

#To import excel file '40175607_features.xlsx' go to File - > Import Dataset - > From Excel -> 
#browse for file - > Import

#convert csv file to dataframe
features_df<-as.data.frame(X40175607_features) ## data as dataframe

#get all of nr_pix values for the envelope, golfclub, pencil and wineglass images
nr_pix_envelope <- features_df$nr_pix[81:100]
nr_pix_golfclub <- features_df$nr_pix[101:120]
nr_pix_pencil <- features_df$nr_pix[121:140]
nr_pix_wineglass <- features_df$nr_pix[141:160]

#combine the four image nr_pix values into another dataframe 
combined_values <- data.frame((cbind(nr_pix_envelope, nr_pix_golfclub, nr_pix_pencil, nr_pix_wineglass)))
combined_values

boxplot_nrpix <- boxplot(nr_pix_envelope, nr_pix_golfclub, nr_pix_pencil, nr_pix_wineglass,
        main = "Boxplots for the number of pixels", ylab = "Number of pixels",
        names = c("Envelope", "Golfclub", "Pencil", "Wineglass"),                                                               
        col = "orange")
boxplot_nrpix

#combine each of the rows in the dataframe into a stack 
stacked_values <- stack(combined_values)
stacked_values

#Execute anova test on the four different classes of images. 
#An anova test is used to test statistical significance between more than 2 groups.
#test is being carried out between the values and the index from the stack 

nrpix_anova <- aov(values ~ ind, data = stacked_values)
nrpix_anova

#Calling the summary function on the anova test will give the statistical results of it 
#including: the degree of freedom, sum of squares, mean square, f value and p value 

summary(nrpix_anova)

#Anova test used to test the statistical significance between more than 2 independant groups by comparing the means of the populations.
#degres of fredom is 3. F value (result of anova) is 649.1. P value is 2 x 10^-16, a lot less than 0.05 so results are significant
#and I did not get them by random chance - reject the null hypothesis. 
