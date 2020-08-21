#File for span rows_with_5 and cols_with_5

#import pandas, openpyxl and numpy libraries
import pandas as pd
import openpyxl  #used for the append to excel function
import numpy as np
import os #os module - used to create the relative file paths

#features_path variable to hold the relative pathname for features file

current_working_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_working_dir)
parent_dir = os.path.abspath(os.path.join(current_working_dir, os.pardir))
features_path =  parent_dir + '/section2_features'

print(current_working_dir)
print(features_path)

#To execute files in Terminal, right click on section2_code folder and open new Terminal window from here
#this sets the correct directory for execution


#import all file paths from allfile_paths file
from allfile_paths import *
#import all cell values from allcell_values file
from allcell_values import *


#Variables below are the initialisation of lists that are used to store the values that are to be written
#to their coresponding feature cell values in allcell_values file

span_values = []
rowswith5_values = []
colswith5_values = []

#Below code creates a subset of lists for each of the images from their respective main cell values list in allcell_values file
#Each list subset has length = 20 as it contains 20 cell values. 20 cell values for the 20 images for each image type.
#This code ensures that the correct value is being written to the correct cell in the excel file.
#There are 8 subset lists for the 8 images for each individual feature

span_cheery_cell_values = span_cell_values[:20]
span_flower_cell_values = span_cell_values[20:41]
span_banana_cell_values = span_cell_values[40:61]
span_pear_cell_values = span_cell_values[60:81]
span_envelope_cell_values = span_cell_values[80:101]
span_golfclub_cell_values = span_cell_values[100:121]
span_pencil_cell_values = span_cell_values[120:141]
span_wineglass_cell_values = span_cell_values[140:161]

rowswith5_cheery_cell_values = rowswith5_cell_values[:20]
rowswith5_flower_cell_values = rowswith5_cell_values[20:41]
rowswith5_banana_cell_values = rowswith5_cell_values[40:61]
rowswith5_pear_cell_values = rowswith5_cell_values[60:81]
rowswith5_envelope_cell_values = rowswith5_cell_values[80:101]
rowswith5_golfclub_cell_values = rowswith5_cell_values[100:121]
rowswith5_pencil_cell_values = rowswith5_cell_values[120:141]
rowswith5_wineglass_cell_values = rowswith5_cell_values[140:161]

colswith5_cheery_cell_values = colswith5_cell_values[:20]
colswith5_flower_cell_values = colswith5_cell_values[20:41]
colswith5_banana_cell_values = colswith5_cell_values[40:61]
colswith5_pear_cell_values = colswith5_cell_values[60:81]
colswith5_envelope_cell_values = colswith5_cell_values[80:101]
colswith5_golfclub_cell_values = colswith5_cell_values[100:121]
colswith5_pencil_cell_values = colswith5_cell_values[120:141]
colswith5_wineglass_cell_values = colswith5_cell_values[140:161]


#span function calculates the maximum eucledian distance between any 2 black pixels in the image
#Note - >
#**!!!For reproducing the span function please bare in mind that the function consists of
#4 for loops so takes very long to execute for all 160 images!!! (~1.5 hours)**

def span(path):

    #initialise variables
    eucled = 0
    precision = 2
    eucled_list = []

    #convert csv to dataframe
    dataframe = pd.read_csv(path)

    #This code block consists of of an outer for loop with 3 nested for loops
    #Firstly the rows & columns of the dataframe are iterated until a black pixel is found.
    #When a black pixel is found, the final 2 inner for loops iterate through the rest of
    #the dataframe until a black pixel is found, when one is found the eucledian distance between the two
    #black pixel positions (row, row1, col, col1) is calculated.
    #To get the eucledian distance I am using the numpy library along with the formula for calculating it.
    #The calculated eucledian distance is then stored in a list of all the eucledian distance values

    for row in range(0, dataframe.shape[0]-1):
        for col in range(0, dataframe.shape[1]-1):
            for row1 in range(1, dataframe.shape[0]-1):
                for col1 in range(1, dataframe.shape[1]-1):
                    if dataframe.values[row][col] == 1:
                        if dataframe.values[row1][col1] == 1:
                            eucled = np.sqrt((row1 - row)**2 + (col1 - col)**2)
                            eucled_list.append(eucled)

    #The eucled_list is a list consisting of all eucledian distances between all positions in the dataframe of the image
    #to get maximum value in this list, the max function is used on the list
    max_eucled = max(eucled_list)

    #append the max eucledian distance value to a list of span values
    span_values.append(max_eucled)

#span_all function is used to call the span function to calculate
#span value for each image

def span_all():

    #set variables to global so they can be used locally
    global span_values
    global span_cell_values

    #for loops to calculate maximm eucledian distance for each image
    #append_to_excel function is called with the parameters of - values calculated from span function
    #and the cell values at which these span values are to be written to
    #list to store span values is set to 0 after every image type has been iterated through

    for i in range(0, len(cherry_path)):
        span(cherry_path[i])

    append_to_excel(span_cheery_cell_values, span_values)
    span_values = []

    for i in range(0, len(cherry_path)):
        span(flower_path[i])

    append_to_excel(span_flower_cell_values, span_values)
    span_values = []

    for i in range(0, len(cherry_path)):
        span(banana_path[i])

    append_to_excel(span_banana_cell_values, span_values)
    span_values = []

    for i in range(0, len(cherry_path)):
        span(pear_path[i])

    append_to_excel(span_pear_cell_values, span_values)
    span_values = []

    for i in range(0, len(cherry_path)):
        span(envelope_path[i])

    append_to_excel(span_envelope_cell_values, span_values)
    span_values = []

    for i in range(0, len(cherry_path)):
        span(golfclub_path[i])

    append_to_excel(span_golfclub_cell_values, span_values)
    span_values = []

    for i in range(0, len(cherry_path)):
        span(pencil_path[i])

    append_to_excel(span_pencil_cell_values, span_values)
    span_values = []

    for i in range(0, len(cherry_path)):
        span(wineglass_path[i])

    append_to_excel(span_wineglass_cell_values, span_values)
    span_values = []

    print('Maximum eucledian distance successfully calculated')

#rows_with_5 function calculates the number of rows in the image with 5 or more black pixels

def rows_with_5(path):

    #set variable to gloabl so that it can be used locally
    global rowswith5_values
    total_rows = 0

    #convert csv file to dataframe
    dataframe = pd.read_csv(path)

    #loop through each row and if number of black pixels in row >=5 then add to sum total
    #inner sum function firstly stores the total number of black pixel values in the row
    #outer sum function stores the total number of rows with 5 or more black pixels
    total_rows = sum([sum(dataframe.values[x,:]) >= 5 for x in range(dataframe.shape[0])])

    #resultant total_rows value is appended to the rowswith5_values list
    rowswith5_values.append(total_rows)

#rows_with_5_all function is used to call the rows_with_5 function to calculate
#rows_with_5 value for each image

def rows_with_5_all():

    #set variables to global so they can be used locally
    global rowswith5_values
    global rowswith5_cell_values

    #for loops below has the exact same functionality as the one in above functions span_all

    for i in range(0, len(cherry_path)):
        rows_with_5(cherry_path[i])

    append_to_excel(rowswith5_cheery_cell_values, rowswith5_values)
    rowswith5_values = []

    for i in range(0, len(cherry_path)):
        rows_with_5(flower_path[i])

    append_to_excel(rowswith5_flower_cell_values, rowswith5_values)
    rowswith5_values = []

    for i in range(0, len(cherry_path)):
        rows_with_5(banana_path[i])

    append_to_excel(rowswith5_banana_cell_values, rowswith5_values)
    rowswith5_values = []

    for i in range(0, len(cherry_path)):
        rows_with_5(pear_path[i])

    append_to_excel(rowswith5_pear_cell_values, rowswith5_values)
    rowswith5_values = []

    for i in range(0, len(cherry_path)):
        rows_with_5(envelope_path[i])

    append_to_excel(rowswith5_envelope_cell_values, rowswith5_values)
    rowswith5_values = []

    for i in range(0, len(cherry_path)):
        rows_with_5(golfclub_path[i])

    append_to_excel(rowswith5_golfclub_cell_values, rowswith5_values)
    rowswith5_values = []

    for i in range(0, len(cherry_path)):
        rows_with_5(pencil_path[i])

    append_to_excel(rowswith5_pencil_cell_values, rowswith5_values)
    rowswith5_values = []

    for i in range(0, len(cherry_path)):
        rows_with_5(wineglass_path[i])

    append_to_excel(rowswith5_wineglass_cell_values, rowswith5_values)
    rowswith5_values = []

    print('Number of rows with 5 or more black pixels successfully calculated')

#cols_with_5 function calculates the total number of columns with 5 or more black pixels

def cols_with_5(path):

    #set variable to global so it can be used locally
    global colswith5_values
    total_cols = 0

    #convert csc to dataframe
    dataframe = pd.read_csv(path)

    #loop through each column and if number of black pixels in row >=5 then add to sum total
    #inner sum function firstly stores the total number of black pixel values in the column
    #outer sum function stores the total number of columns with 5 or more black pixels
    total_cols = sum([sum(dataframe.values[:,x]) >= 5 for x in range(dataframe.shape[1])])

    #resultant total_cols value is appended to the colswith5_values list
    colswith5_values.append(total_cols)

#cols_with_5_all function is used to call the cols_with_5 function to calculate
#cols_with_5 value for each image

def cols_with_5_all():

        #set variables to gloabl so that they can be used locally
        global colswith5_values
        global colswith5_cell_values

        #for loops below have the exact same functionality as the one in above functions span/rows_with_5_all

        for i in range(0, len(cherry_path)):
            cols_with_5(cherry_path[i])

        append_to_excel(colswith5_cheery_cell_values, colswith5_values)
        colswith5_values = []

        for i in range(0, len(cherry_path)):
            cols_with_5(flower_path[i])

        append_to_excel(colswith5_flower_cell_values, colswith5_values)
        colswith5_values = []

        for i in range(0, len(cherry_path)):
            cols_with_5(banana_path[i])

        append_to_excel(colswith5_banana_cell_values, colswith5_values)
        colswith5_values = []

        for i in range(0, len(cherry_path)):
            cols_with_5(pear_path[i])

        append_to_excel(colswith5_pear_cell_values, colswith5_values)
        colswith5_values = []

        for i in range(0, len(cherry_path)):
            cols_with_5(envelope_path[i])

        append_to_excel(colswith5_envelope_cell_values, colswith5_values)
        colswith5_values = []

        for i in range(0, len(cherry_path)):
            cols_with_5(golfclub_path[i])

        append_to_excel(colswith5_golfclub_cell_values, colswith5_values)
        colswith5_values = []

        for i in range(0, len(cherry_path)):
            cols_with_5(pencil_path[i])

        append_to_excel(colswith5_pencil_cell_values, colswith5_values)
        colswith5_values = []

        for i in range(0, len(cherry_path)):
            cols_with_5(wineglass_path[i])

        append_to_excel(colswith5_wineglass_cell_values, colswith5_values)
        colswith5_values = []

        print('Number of columns with 5 or more black pixels successfully calculated')

#I have used an excel file to export the features as I was unable to functionally export the data to a .txt or .csv format
#the openpyxl library for exporting to excel was the only export option I got working.

#append to excel function takes 2 parameters
#column_list - The list of cell values to which data is being written to
#values - the values to be written to the specified cell values
#function loops through all values in values list and writes them to the correct cell in excel sheet
#openpyxl library is used for writing and reading excel files

def append_to_excel(column_list, values):

        #open excel file
        wb = openpyxl.load_workbook(features_path + "/40175607_features.xlsx")

        #open worksheet
        sheet = wb["Sheet1"]

        #loop through values list and write value to cell
        for i in range(0, len(span_cheery_cell_values)):
            sheet[column_list[i]].value = values[i]

        #save excel file with updated cell values
        wb.save(features_path + "/40175607_features.xlsx")

#call all functions
#span_all()    #very slow executing function

rows_with_5_all()
cols_with_5_all()
