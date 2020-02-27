#Section 3 task 10 - Randomisation test for top2tile feature  

#To import excel file '40175607_features.xlsx' go to File - > Import Dataset - > From Excel -> 
#browse for file - > Import

#import csv file and convert to dataframe 
features_df_living <- features_df[1:80,] 
features_df_nonliving <- features_df[81:160,] 


#Boxplot for features 2 - 6 

boxplot_height <- boxplot(features_df_living$height, features_df_nonliving$height,
            main = "Boxplot for the height values", ylab = "Height",
            names = c("Height for living things", "Height for non-living things"),                                                               
            col = "orange")
boxplot_height

boxplot_width<- boxplot(features_df_living$width, features_df_nonliving$width,
                          main = "Boxplot for the width values", ylab = "Width",
                          names = c("Width for living things", "Width for non-living things"),                                                               
                          col = "orange")
boxplot_width 

boxplot_span <- boxplot(features_df_living$span, features_df_nonliving$span,
                          main = "Boxplot for the span values", ylab = "Span",
                          names = c("Span for living things", "Span for non-living things"),                                                               
                          col = "orange")
boxplot_span

boxplot_rows_with_5 <- boxplot(features_df_living$rows_with_5, features_df_nonliving$rows_with_5,
                        main = "Boxplot for the rows with 5 values", ylab = "Rows with 5",
                        names = c("Rows with 5 for living things", "Rows with 5 for non-living things"),                                                               
                        col = "orange")
boxplot_rows_with_5 

boxplot_cols_with_5 <- boxplot(features_df_living$cols_with_5, features_df_nonliving$cols_with_5,
                               main = "Boxplot for the columns with 5 values", ylab = "Columns with 5",
                               names = c("Columns with 5 for living things", "Columns with 5 for non-living things"),                                                               
                               col = "orange")
boxplot_cols_with_5 


#For each feature, bind the living and non-living data into a dataframe 
#and then combine the data in the dataframe into a stack 

height_combined_values <-data.frame((cbind(features_df_living$height, features_df_nonliving$height)))
height_combined_values

height_stacked_values <- stack(height_combined_values)
height_stacked_values


width_combined_values <-data.frame((cbind(features_df_living$width, features_df_nonliving$width)))
width_combined_values

width_stacked_values <- stack(width_combined_values)
width_stacked_values


span_combined_values <-data.frame((cbind(features_df_living$span, features_df_nonliving$span)))
span_combined_values

span_stacked_values <- stack(span_combined_values)
span_stacked_values


rowswith5_combined_values <-data.frame((cbind(features_df_living$rows_with_5, features_df_nonliving$rows_with_5)))
rowswith5_combined_values

rowswith5_stacked_values <- stack(rowswith5_combined_values)
rowswith5_stacked_values


colswith5_combined_values <-data.frame((cbind(features_df_living$cols_with_5, features_df_nonliving$cols_with_5)))
colswith5_combined_values

colswith5_stacked_values <- stack(colswith5_combined_values)
colswith5_stacked_values


#Anova test for each of the features 2 - 6

#Anova for height
height_anova <- aov(values ~ ind, data = height_stacked_values)
summary(height_anova)

#Anova for width
width_anova <- aov(values ~ ind, data = width_stacked_values)
summary(width_anova)

#Anova for span
span_anova <- aov(values ~ ind, data = span_stacked_values)
summary(span_anova)

#Anova rows_with_5
rowswith5_anova <- aov(values ~ ind, data = rowswith5_stacked_values)
summary(rowswith5_anova)

#Anova cols_with_5
colswit5_anova <- aov(values ~ ind, data = colswith5_stacked_values)
summary(colswit5_anova)

#pairwise t-test on feature with largest f-value
t.test(features_df_living$height, features_df_nonliving$height, paired =TRUE)

