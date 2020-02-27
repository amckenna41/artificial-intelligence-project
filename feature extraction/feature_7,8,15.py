#File for neigh1, neigh5 and neigh8 (feature 15)

#import pandas and openpyxl libraries
import pandas as pd
import openpyxl  #used for append to excel function
import os #os module - used to create the relative file paths

#features_path variable to hold the relative pathname for features file

current_working_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_working_dir)
parent_dir = os.path.abspath(os.path.join(current_working_dir, os.pardir))
features_path =  parent_dir + '/section2_features'

#To execute files in Terminal, right click on section2_code folder and open new Terminal window
#this sets the correct directory for execution

#import all file paths from allfile_paths file
from allfile_paths import *
#import all cell values from allcell_values file
from allcell_values import *

#Variables below are the initialisation of lists that are used to store the values that are to be written
#to their coresponding feature cell values in allcell_values file

neigh1_values = []
neigh5_values = []
neigh8_values = []

#Below code creates a subset of lists for each of the images from their respective  main cell values list in allcell_values file
#Each list subset has length = 20 as it contains 20 cell values. 20 cell values for the 20 images for each image type.
#This code ensures that the correct value is being written to the correct cell in the excel file.
#There are 8 subset lists for the 8 images for each individual feature

neigh1_cherry_cell_values = neigh1cell_values[:20]
neigh1_flower_cell_values = neigh1cell_values[20:41]
neigh1_banana_cell_values = neigh1cell_values[40:61]
neigh1_pear_cell_values = neigh1cell_values[60:81]
neigh1_envelope_cell_values = neigh1cell_values[80:101]
neigh1_golfclub_cell_values = neigh1cell_values[100:121]
neigh1_pencil_cell_values = neigh1cell_values[120:141]
neigh1_wineglass_cell_values = neigh1cell_values[140:161]

neigh5_cherry_cell_values = neigh5cell_values[:20]
neigh5_flower_cell_values = neigh5cell_values[20:41]
neigh5_banana_cell_values = neigh5cell_values[40:61]
neigh5_pear_cell_values = neigh5cell_values[60:81]
neigh5_envelope_cell_values = neigh5cell_values[80:101]
neigh5_golfclub_cell_values = neigh5cell_values[100:121]
neigh5_pencil_cell_values = neigh5cell_values[120:141]
neigh5_wineglass_cell_values = neigh5cell_values[140:161]

neigh8_cherry_cell_values = neigh8cell_values[:20]
neigh8_flower_cell_values = neigh8cell_values[20:41]
neigh8_banana_cell_values = neigh8cell_values[40:61]
neigh8_pear_cell_values = neigh8cell_values[60:81]
neigh8_envelope_cell_values = neigh8cell_values[80:101]
neigh8_golfclub_cell_values = neigh8cell_values[100:121]
neigh8_pencil_cell_values = neigh8cell_values[120:141]
neigh8_wineglass_cell_values = neigh8cell_values[140:161]

#neigh1 function calculates how many black pixels have exactly one neighbouring black pixel

def neigh1(path):

    #initialise variables, set neigh1_values to global so it can be locally used
    global neigh1_values
    num_true_bools = 0
    neigh_one = 0

    #convert csv file to dataframe
    dataframe = pd.read_csv(path)


    #for loop iterates through each column and row
    #nested if statements checks if left, right, upper, lower, upper right/left & lower right/left are also black pixels
    #if nested if statement is true then a counter is incremented

    for row in range(1, dataframe.shape[0]-1):
         for col in range(1, dataframe.shape[1]-1):
            if dataframe.values[row][col] == 1:
                if dataframe.values[row][col - 1] == 1:
                     num_true_bools = num_true_bools + 1

                if dataframe.values[row][col + 1] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row-1][col] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row+1][col] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row-1][col - 1] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row-1][col +1] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row+1][col - 1] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row+1][col + 1] == 1:
                    num_true_bools = num_true_bools + 1

            #if there is exactly 1 black pixel neighbouring pixel then
            #neighbour one variable is incremented
            if num_true_bools == 1:
                neigh_one = neigh_one + 1
            num_true_bools = 0

    #resultant neigh_one value is appended to the neigh1_values list
    neigh1_values.append(neigh_one)

#neigh1_all function is used to call the neigh1 function to calculate
#neigh1 value for each image

def neigh1_all():

        #set variables to global so that they can be used locally
        global neigh1_values
        global neigh1cell_values

        #for loops to calculate black pixels with exactly 1 neighbour for each image
        #append_to_excel function is called with the parameters of - values calculated from neigh1 function
        #and the cell values at which these neigh_1 values are to be written to
        #list to store neigh1 values is set to 0 after every image type has been iterated through

        for i in range(0, len(cherry_path)):
            neigh1(cherry_path[i])

        append_to_excel(neigh1_cherry_cell_values, neigh1_values)
        neigh1_values = []

        for i in range(0, len(cherry_path)):
            neigh1(flower_path[i])

        append_to_excel(neigh1_flower_cell_values, neigh1_values)
        neigh1_values = []

        for i in range(0, len(cherry_path)):
            neigh1(banana_path[i])

        append_to_excel(neigh1_banana_cell_values, neigh1_values)
        neigh1_values = []

        for i in range(0, len(cherry_path)):
            neigh1(pear_path[i])

        append_to_excel(neigh1_pear_cell_values, neigh1_values)
        neigh1_values = []

        for i in range(0, len(cherry_path)):
            neigh1(envelope_path[i])

        append_to_excel(neigh1_envelope_cell_values, neigh1_values)
        neigh1_values = []

        for i in range(0, len(cherry_path)):
            neigh1(golfclub_path[i])

        append_to_excel(neigh1_golfclub_cell_values, neigh1_values)
        neigh1_values = []

        for i in range(0, len(cherry_path)):
            neigh1(pencil_path[i])

        append_to_excel(neigh1_pencil_cell_values, neigh1_values)
        neigh1_values = []

        for i in range(0, len(cherry_path)):
            neigh1(wineglass_path[i])

        append_to_excel(neigh1_wineglass_cell_values, neigh1_values)
        neigh1_values = []

        print('Total pixels with one neighbour successfully calculated')

#neigh5 function calculates how many black pixels have five or more neighbouring black pixels

def neigh5(path):

    #initialise variables
    global neigh5_values
    num_true_bools = 0
    neigh_five = 0

    #convert csv to dataframe
    dataframe = pd.read_csv(path)

    #for loop iterates through each column and row
    #nested if statements checks if left, right, upper, lower, upper right/left & lower right/left are also black pixels
    #if nested if statement is true then a counter is incremented

    for row in range(1, dataframe.shape[0]-1):
         for col in range(1, dataframe.shape[1]-1):
            if dataframe.values[row][col] == 1:
                if dataframe.values[row][col - 1] == 1:
                     num_true_bools = num_true_bools + 1

                if dataframe.values[row][col + 1] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row-1][col] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row+1][col] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row-1][col - 1] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row-1][col +1] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row+1][col - 1] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row+1][col + 1] == 1:
                    num_true_bools = num_true_bools + 1

            #if there are 5 or more black pixels surrounding pixel then
            #neigh_five variable is incremented
            if num_true_bools >= 5:
                neigh_five = neigh_five + 1
            num_true_bools = 0

    #resultant neigh_five value is appended to the neigh5_values list
    neigh5_values.append(neigh_five)

#neigh5_all function is used to call the neigh5 function to calculate
#neigh5 values for each image

def neigh5_all():

        #set variables to global so that they can be used locally
        global neigh5_values
        global neigh5cell_values

        #for loops to calculate black pixels with 5 or more neighbours for each image
        #append_to_excel function is called with the parameters of - values calculated from neigh5 function
        #and the cell values at which these neigh5 values are to be written to
        #list to store neigh5 values is set to 0 after every image type has been iterated through

        for i in range(0, len(cherry_path)):
            neigh5(cherry_path[i])

        append_to_excel(neigh5_cherry_cell_values, neigh5_values)
        neigh5_values = []

        for i in range(0, len(cherry_path)):
            neigh5(flower_path[i])

        append_to_excel(neigh5_flower_cell_values, neigh5_values)
        neigh5_values = []

        for i in range(0, len(cherry_path)):
            neigh5(banana_path[i])

        append_to_excel(neigh5_banana_cell_values, neigh5_values)
        neigh5_values = []

        for i in range(0, len(cherry_path)):
            neigh5(pear_path[i])

        append_to_excel(neigh5_pear_cell_values, neigh5_values)
        neigh5_values = []

        for i in range(0, len(cherry_path)):
            neigh5(envelope_path[i])

        append_to_excel(neigh5_envelope_cell_values, neigh5_values)
        neigh5_values = []

        for i in range(0, len(cherry_path)):
            neigh5(golfclub_path[i])

        append_to_excel(neigh5_golfclub_cell_values, neigh5_values)
        neigh5_values = []

        for i in range(0, len(cherry_path)):
            neigh5(pencil_path[i])

        append_to_excel(neigh5_pencil_cell_values, neigh5_values)
        neigh5_values = []

        for i in range(0, len(cherry_path)):
            neigh5(wineglass_path[i])

        append_to_excel(neigh5_wineglass_cell_values, neigh5_values)
        neigh5_values = []

        print('Total pixels with five or more neighbours successfully calculated')


#neigh8 function calculates how many black pixels have exactly 8 neighbouring black pixels

def neigh8(path):

    #initialise variables
    global neigh8_values
    num_true_bools = 0
    neigh_eight = 0

    #convert csv to dataframe
    dataframe = pd.read_csv(path)


    #for loop iterates through each column and row
    #nested if statements checks if left, right, upper, lower, upper right/left & lower right/left are also black pixels
    #if nested if statement is true then a counter is incremented

    for row in range(1, dataframe.shape[0]-1):
         for col in range(1, dataframe.shape[1]-1):
            if dataframe.values[row][col] == 1:
                if dataframe.values[row][col - 1] == 1:
                     num_true_bools = num_true_bools + 1

                if dataframe.values[row][col + 1] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row-1][col] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row+1][col] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row-1][col - 1] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row-1][col +1] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row+1][col - 1] == 1:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row+1][col + 1] == 1:
                    num_true_bools = num_true_bools + 1

            #if the pixel is compleely surrounded by black pixels / has 8 neighbours
            #neighbour eight variable is incremented
            if num_true_bools == 8:
                neigh_eight = neigh_eight + 1
            num_true_bools = 0

    #resultant neigh_eight value is appended to the neigh8_values list
    neigh8_values.append(neigh_eight)


#neigh8_all function is used to call the neigh8 function to calculate
#neigh8 values for each image

def neigh8_all():

        #set variables to global so they can be used locally
        global neigh8_values
        global neigh8cell_values

        #for loops to calculate black pixels with exactly 8 neighbours for each image
        #append_to_excel function is called with the parameters of - values calculated from neigh8 function
        #and the cell values at which these neigh8 values are to be written to
        #list to store neigh8 values is set to 0 after every image type has been iterated through

        for i in range(0, len(cherry_path)):
            neigh8(cherry_path[i])

        append_to_excel(neigh8_cherry_cell_values, neigh8_values)
        neigh8_values = []

        for i in range(0, len(cherry_path)):
            neigh8(flower_path[i])

        append_to_excel(neigh8_flower_cell_values, neigh8_values)
        neigh8_values = []

        for i in range(0, len(cherry_path)):
            neigh8(banana_path[i])

        append_to_excel(neigh8_banana_cell_values, neigh8_values)
        neigh8_values = []

        for i in range(0, len(cherry_path)):
            neigh8(pear_path[i])

        append_to_excel(neigh8_pear_cell_values, neigh8_values)
        neigh8_values = []

        for i in range(0, len(cherry_path)):
            neigh8(envelope_path[i])

        append_to_excel(neigh8_envelope_cell_values, neigh8_values)
        neigh8_values = []

        for i in range(0, len(cherry_path)):
            neigh8(golfclub_path[i])

        append_to_excel(neigh8_golfclub_cell_values, neigh8_values)
        neigh8_values = []

        for i in range(0, len(cherry_path)):
            neigh8(pencil_path[i])

        append_to_excel(neigh8_pencil_cell_values, neigh8_values)
        neigh8_values = []

        for i in range(0, len(cherry_path)):
            neigh8(wineglass_path[i])

        append_to_excel(neigh8_wineglass_cell_values, neigh8_values)
        neigh8_values = []

        print('Total pixels with eight neighbours successfully calculated')

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
        for i in range(0, len(neigh1_cherry_cell_values)):
            sheet[column_list[i]].value = values[i]

        #save excel file with updated cell values
        wb.save(features_path + "/40175607_features.xlsx")

#call all functions
neigh1_all()
neigh5_all()
neigh8_all()
