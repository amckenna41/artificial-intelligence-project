#Section 3 - Task 9. Testing features to determine if they are useful for discriminating
#between living and non-living things 

#To import excel file '40175607_features.xlsx' go to File - > Import Dataset - > From Excel -> 
#browse for file - > Import

#import csv file and convert to dataframe 
features_df<-as.data.frame(X40175607_features) ## data as dataframe

#get all rows and columns for living and non-living things
features_df_living <- features_df[1:80,] 
features_df_nonliving <- features_df[81:160,] 

#Below are t-tests for each feature between the living and non-living data 
#Results of each t-test will be used to determine if the feature is useful in differentiating
#between the set of living and non-living things 

#significance level alpha = 0.05

#T-test nr_pix 
#p-value = 0.2061 - > p-vaue > 0.05 so difference in means are not significant, fail to reject null hypothesis 
t.test(features_df_living$nr_pix, features_df_nonliving$nr_pix)

#t-test height 
#p-value = <2.2e-16 - > p-vaue < 0.05 so difference in means are significant, reject null hypothesis
t.test(features_df_living$height, features_df_nonliving$height)

#t-test width
#p-value = 0.001 - > p-vaue < 0.05 so difference in means are significant, reject null hypothesis
t.test(features_df_living$width, features_df_nonliving$width)

#t-test span 
#p-value = 0.10 - > p-vaue > 0.05 so difference in means are not significant, fail to reject null hypothesis
t.test(features_df_living$span, features_df_nonliving$span)

#t-test rows_with_5
#p-value = 0.77 - > p-vaue > 0.05 so difference in means are not significant, fail to reject null hypothesis
t.test(features_df_living$rows_with_5, features_df_nonliving$rows_with_5)

#t-test cols_with_5
#p-value = 1.672e-10 - > p-vaue < 0.05 so difference in means are significant, reject null hypothesis
t.test(features_df_living$cols_with_5, features_df_nonliving$cols_with_5)

#t-test neigh1
#p-value = 2.352e-05 - > p-vaue < 0.05 so difference in means are significant, reject null hypothesis
t.test(features_df_living$neigh1, features_df_nonliving$neigh1)

#t-test neigh5
#p-value = 0.08 - > p-vaue > 0.05 so difference in means are not significant, fail to reject null hypothesis
t.test(features_df_living$neigh5, features_df_nonliving$neigh5)

#t-test left2tile 
#p-value = 0.0002 - > p-vaue < 0.05 so difference in means are significant, reject null hypothesis
t.test(features_df_living$left2tile, features_df_nonliving$left2tile)

#t-test right2tile
#p-value = 0.0002 - > p-vaue < 0.05 so difference in means are significant, reject null hypothesis
t.test(features_df_living$right2tile, features_df_nonliving$right2tile)

#t-test verticalness
#p-value = 0.03 - > p-vaue < 0.05 so difference in means are significant, reject null hypothesis
t.test(features_df_living$verticalness, features_df_nonliving$verticalness)

#t-test top2tile
#p-value = 0.04 - > p-vaue < 0.05 so difference in means are significant, reject null hypothesis
t.test(features_df_living$top2tile, features_df_nonliving$top2tile)

#t-test bottom2tile
#p-value = 0.06 - > p-vaue > 0.05 so difference in means are not significant, fail to reject null hypothesis
t.test(features_df_living$bottom2tile, features_df_nonliving$bottom2tile)

#t-test horizontalness
#p-value = 0.02 - > p-vaue < 0.05 so difference in means are significant, reject null hypothesis
t.test(features_df_living$horizontalness, features_df_nonliving$horizontalness)

#t-test neigh8
#p-value = 0.000045 - > p-vaue < 0.05 so difference in means are significant, reject null hypothesis
t.test(features_df_living$neigh8, features_df_nonliving$neigh8)

#t-test white3tile
#p-value = 0.02 - > p-vaue < 0.05 so difference in means are significant, reject null hypothesis
t.test(features_df_living$white3tile, features_df_nonliving$white3tile)

#t-test nr_regions
#p-value = 0.16 - > p-vaue > 0.05 so difference in means are not significant, fail to reject null hypothesis
t.test(features_df_living$nr_regions, features_df_nonliving$nr_regions)

#t-test nr_eyes
#p-value = 0.057 - > p-vaue > 0.05 so difference in means are not significant, fail to reject null hypothesis
t.test(features_df_living$nr_eyes, features_df_nonliving$nr_eyes)

#t-test hollowness
#p-value = 0.00097 - > p-vaue < 0.05 so difference in means are significant, reject null hypothesis
t.test(features_df_living$hollowness, features_df_nonliving$hollowness)

#t-test blackpixelproportion
#p-value = 1 - > p-vaue > 0.05 so difference in means are not significant, fail to reject null hypothesis
t.test(features_df_living$black_pixel_proportion, features_df_nonliving$black_pixel_proportion)

