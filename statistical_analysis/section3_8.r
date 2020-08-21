#Section 3 task 8 - Randomisation test for top2tile feature  

#To import excel file '40175607_features.xlsx' go to File - > Import Dataset - > From Excel -> 
#browse for file - > Import

#import csv file and convert to dataframe 
features_df<-as.data.frame(X40175607_features) ## data as dataframe

#get all of top2tile values for the envelope, golfclub, pencil and wineglass images
top2tile_envelope <- features_df$top2tile[81:100]
top2tile_golfclub <- features_df$top2tile[101:120]
top2tile_pencil <- features_df$top2tile[121:140]
top2tile_wineglass <- features_df$top2tile[141:160]

#boxplot for top2tile for all 4 images
boxplot_top2tile <- boxplot(top2tile_envelope, top2tile_golfclub, top2tile_pencil, top2tile_wineglass,
           main = "Boxplots for the top2tile values", ylab = "Top2tile",
           names = c("Envelope", "Golfclub", "Pencil", "Wineglass"),                                                               
           col = "orange")
boxplot_top2tile

#combine the four image top2tile values into another dataframe 
combined_values <- data.frame((cbind(top2tile_envelope, top2tile_golfclub, top2tile_pencil, top2tile_wineglass)))
combined_values

#combine each of the rows in the dataframe into a stack 
stacked_values <- stack(combined_values)
stacked_values

#set ranndom seed value to 3060
set.seed(3060)

#create random sample of 20 values from top2tile
randomTop2tile <- dplyr::sample_n(stacked_values, 20)
randomTop2tile

#generate anove test from random sample 
random_anova <- aov(values ~ ind, data = randomTop2tile)
summary(random_anova)

#non-sampled anova test for top2tile variable 
normal_anova <- aov(values ~ ind, data = stacked_values)
summary(normal_anova)
