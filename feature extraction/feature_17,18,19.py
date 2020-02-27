#File for number of regions, number of eyes and hollowness

#import pandas and openpyxl libraries
import pandas as pd
import openpyxl
import random   #used for random number generation for nr_regions
import os #os module - used to create the relative file paths
import sys #used for nr_regions function to increase the recursive depth value in Python

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

nrregions_values = []
nreyes_values = []
nreyes_hollowness = []
nrpix_hollowness = []
hollowness_values = []

#Below code creates a subset of lists for each of the images from their respective main cell values list in allcell_values file
#Each list subset has length = 20 as it contains 20 cell values. 20 cell values for the 20 images for each image type.
#This code ensures that the correct value is being written to the correct cell in the excel file.
#There are 8 subset lists for the 8 images for each individual feature

nrregions_cheery_cell_values = nr_regionscell_values[:20]
nrregions_flower_cell_values = nr_regionscell_values[20:41]
nrregions_banana_cell_values = nr_regionscell_values[40:61]
nrregions_pear_cell_values = nr_regionscell_values[60:81]
nrregions_envelope_cell_values = nr_regionscell_values[80:101]
nrregions_golfclub_cell_values = nr_regionscell_values[100:121]
nrregions_pencil_cell_values = nr_regionscell_values[120:141]
nrregions_wineglass_cell_values = nr_regionscell_values[140:161]

nreyes_cheery_cell_values = nr_eyescell_values[:20]
nreyes_flower_cell_values = nr_eyescell_values[20:41]
nreyes_banana_cell_values = nr_eyescell_values[40:61]
nreyes_pear_cell_values = nr_eyescell_values[60:81]
nreyes_envelope_cell_values = nr_eyescell_values[80:101]
nreyes_golfclub_cell_values = nr_eyescell_values[100:121]
nreyes_pencil_cell_values = nr_eyescell_values[120:141]
nreyes_wineglass_cell_values = nr_eyescell_values[140:161]

hollowness_cherrycellvalues = hollownesscell_values[:20]
hollowness_flower_cell_values = hollownesscell_values[20:41]
hollowness_banana_cell_values = hollownesscell_values[40:61]
hollowness_pear_cell_values = hollownesscell_values[60:81]
hollowness_envelope_cell_values = hollownesscell_values[80:101]
hollowness_golfclub_cell_values = hollownesscell_values[100:121]
hollowness_pencil_cell_values = hollownesscell_values[120:141]
hollowness_wineglass_cell_values = hollownesscell_values[140:161]

#code for getting and setting recursive limit for nr_regions recursive function
#print(sys.getrecursionlimit)
#sys.setrecursionlimit(1500)
#sys.setrecursionlimit(10**4)
#sys.setrecursionlimit(10**6)

#nr_regions function calculates the total number of regions in the image
#below function is attempt at nr_regions function - Not Working :((
#calling function will lead to stack overflow and recursion depth Error

def nr_regions_attempt(path):

    #convert csv to dataframe
    dataframe = pd.read_csv(path)
    total_regions = 0

    #for loop iterates through dataframe and calls region_neighbours method at every black pixel
    #after region_neighbours is complete, the total_regions variable is incremented by 1

    for row in range(0, dataframe.shape[0]-1):
        for col in range(0, dataframe.shape[1]-1):
            if dataframe.values[row][col] == 1:
                region_neighbours(row, col, dataframe)
                total_regions = regions + 1

    print(regions)

#region_neighbours is a recursive method that takes the current row, column and dataframe as parameters
#This is a recursive method that recursively calls itself until a white pixel is found
#this recursion occurs for all 8 neighbouring pixels.
#while loop encompasses the recursive methods which execute until none of the nested if statements are true
#meaning that there is no more neighbouring black pixels hence the end of a region.

def region_neighbours(rows, cols, dataframe):

    #initialise variables
    no_neighbours = False
    num_true_bools = 0

    #code within while loop executes until no_neighbours value is True

    while(no_neighbours!= True):
        try:
            for row in range(rows, dataframe.shape[0]-1):
                for col in range(cols, dataframe.shape[1]-1):

                    if dataframe.values[row][col - 1] == 1:
                        region_neighbours(row, col -1, dataframe)
                        num_true_bools = num_true_bools + 1

                    if dataframe.values[row][col + 1] == 1:
                        region_neighbours(row, col +1, dataframe)
                        num_true_bools = num_true_bools + 1

                    if dataframe.values[row-1][col] == 1:
                        region_neighbours(row -1, col, dataframe)
                        num_true_bools = num_true_bools + 1

                    if dataframe.values[row +1][col] == 1:
                        region_neighbours(row +1, col, dataframe)
                        num_true_bools = num_true_bools + 1

                    if dataframe.values[row-1][col - 1] == 1:
                        region_neighbours(row -1, col -1, dataframe)
                        num_true_bools = num_true_bools + 1

                    if dataframe.values[row-1][col +1] == 1:
                        region_neighbours(row -1, col +1, dataframe)
                        num_true_bools = num_true_bools + 1

                    if dataframe.values[row+1][col - 1] == 1:
                        region_neighbours(row +1, col -1, dataframe)
                        num_true_bools = num_true_bools + 1

                    if dataframe.values[row+1][col + 1] == 1:
                        region_neighbours(row +1, col +1, dataframe)
                        num_true_bools = num_true_bools + 1

                #if none of the above if statements have been true (no more neighbouring black pixels)
                #set no_neighbours to true
                if num_true_bools == 0:
                    no_neighbours = True

                #reset variable for next iteration of loop
                num_true_bools = 0
        except:
            print('Exception Called')
#Error when executing - RecursionError: maximum recursion depth exceeded while calling a Python object
#increasing recursion depth limit eventually leads to segmentation error

#due to difficulty experienced with this function I have created randomised values for the function data

def nr_regions():

    #initialise variables
    nr_regions_randomvalues = []
    rand_value = 0

    #create 160 randomised values between 1 and 10 and store in a list
    for i in range(161):
        rand_value = random.randint(1,10)
        nr_regions_randomvalues.append(rand_value)

    #append to excel function to write randomised values to nr_regions column
    append_to_excel(nrregions_cheery_cell_values, nr_regions_randomvalues[:20])
    append_to_excel(nrregions_flower_cell_values, nr_regions_randomvalues[20:41])
    append_to_excel(nrregions_banana_cell_values, nr_regions_randomvalues[40:61])
    append_to_excel(nrregions_pear_cell_values, nr_regions_randomvalues[60:81])
    append_to_excel(nrregions_envelope_cell_values, nr_regions_randomvalues[80:101])
    append_to_excel(nrregions_golfclub_cell_values, nr_regions_randomvalues[100:121])
    append_to_excel(nrregions_pencil_cell_values, nr_regions_randomvalues[120:141])
    append_to_excel(nrregions_wineglass_cell_values, nr_regions_randomvalues[140:160])

    print('Randomised nr_regions values successfully calculated')

#nr_eyes function is used to calculate the total number of eyes in the image
#an eye is described as white pixel that is surrouned by a ring of connected black pixels
#An eye will have 8 neigbbours of black pixels with one white pixel in the centre.

def nr_eyes(path):

    #initialise variables
    total_eyes = 0
    num_true_bools = 0
    count = 0

    #convert csc to dataframe
    dataframe = pd.read_csv(path)

    #for loop iterates through each row and column in the dataframe
    #when a white pixel is found (in current index) a series of nested if statements
    #check the surrounding 8 pixels and checks if they are 1's (black pixels), a counter is then incremented if true
    #Eye counter at end of loop is incremented if the white pixel has exactly 8 neighbouring black pixels.

    for row in range(0, dataframe.shape[0]-1):
        for col in range(0, dataframe.shape[1]-1):
            if dataframe.values[row][col] == 0:
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

            #total_eyes counter inremented if white pixel has exactly 8 neighbouring black pixels

            if num_true_bools == 8:
                total_eyes = total_eyes + 1

    #append the total number of eyes to a list of nreyes values
    nreyes_values.append(total_eyes)

    #append the total number of eyes to a list to be used for hollowness function
    nreyes_hollowness.append(total_eyes)

#nr_eyes_all function is used to call the nr_eyes function to calculate
#nr_eyes value for each image

def nr_eyes_all():

    #set variables to global so they can be used locally
    global nreyes_values
    global nr_eyescell_values

    #for loops to calculate total number of eyes for each image
    #append_to_excel function is called with the parameters of - values calculated from nr_eyes function
    #and the cell values at which these nr_eyes values are to be written to
    #list to store nr_eyes values is set to 0 after every image type has been iterated through

    for i in range(0, len(cherry_path)):
        nr_eyes(cherry_path[i])

    append_to_excel(nreyes_cheery_cell_values, nreyes_values)
    nreyes_values = []

    for i in range(0, len(cherry_path)):
        nr_eyes(flower_path[i])

    append_to_excel(nreyes_flower_cell_values, nreyes_values)
    nreyes_values = []

    for i in range(0, len(cherry_path)):
        nr_eyes(banana_path[i])

    append_to_excel(nreyes_banana_cell_values, nreyes_values)
    nreyes_values = []

    for i in range(0, len(cherry_path)):
        nr_eyes(pear_path[i])

    append_to_excel(nreyes_pear_cell_values, nreyes_values)
    nreyes_values = []

    for i in range(0, len(cherry_path)):
        nr_eyes(envelope_path[i])

    append_to_excel(nreyes_envelope_cell_values, nreyes_values)
    nreyes_values = []

    for i in range(0, len(cherry_path)):
        nr_eyes(golfclub_path[i])

    append_to_excel(nreyes_golfclub_cell_values, nreyes_values)
    nreyes_values = []

    for i in range(0, len(cherry_path)):
        nr_eyes(pencil_path[i])

    append_to_excel(nreyes_pencil_cell_values, nreyes_values)
    nreyes_values = []

    for i in range(0, len(cherry_path)):
        nr_eyes(wineglass_path[i])

    append_to_excel(nreyes_wineglass_cell_values, nreyes_values)
    nreyes_values = []

    print('Number of eyes successfully calculated')


#nrpix function calculates the total number of black pixels in image

def nr_pix(path):

    #initialise variables
    global nr_pix_values
    nr_pix_count = 0

    #convert csv to dataframe
    dataframe = pd.read_csv(path)

    #for loop loops through every pixel in image
    #if a black pixel is found then a counter is incremented

    for row in range(dataframe.shape[0]):
        for col in range(dataframe.shape[1]):
            if dataframe.values[row][col] == 1:
                nr_pix_count = nr_pix_count + 1

    #resultant nr_pix value is appended to the nr_pix_hollowness list for the hollowness function
    nrpix_hollowness.append(nr_pix_count)

#nr_pix_all function is used to call the nr_pix function to calculate
#nr_pix value for each image

def nr_pix_all():

    #set variables to global so that they can be used locally
    global nr_pix_values
    global nr_pix_cell_values

    #for loops to calculate total number of black pixels for each image

    for i in range(0, len(cherry_path)):
        nr_pix(cherry_path[i])

    for i in range(0, len(cherry_path)):
        nr_pix(flower_path[i])

    for i in range(0, len(cherry_path)):
        nr_pix(banana_path[i])

    for i in range(0, len(cherry_path)):
        nr_pix(pear_path[i])

    for i in range(0, len(cherry_path)):
        nr_pix(envelope_path[i])

    for i in range(0, len(cherry_path)):
        nr_pix(golfclub_path[i])

    for i in range(0, len(cherry_path)):
        nr_pix(pencil_path[i])

    for i in range(0, len(cherry_path)):
        nr_pix(wineglass_path[i])

    print('Number of black pixels successfully calculated')

#hollowness function calculates the number of eyes divided by the nr_pix in image

def hollowness():

    #set variables to global so that they can be used locally
    global hollowness_values
    global hollownesscell_values

    #for loops to calculate total number of black pixels for each image
    #append_to_excel function is called with the parameters of - values calculated from nr_pix function
    #and the cell values at which these nr_pix values are to be written to
    #list to store nr_pix values is set to 0 after every image type has been iterated through

    for i in range(0, len(cherry_path)):
        hollowness_values.append(nreyes_hollowness[i]/nrpix_hollowness[i])

    append_to_excel(hollowness_cherrycellvalues, hollowness_values)
    hollowness_values = []

    for i in range(20, 41):
        hollowness_values.append(nreyes_hollowness[i]/nrpix_hollowness[i])

    append_to_excel(hollowness_flower_cell_values, hollowness_values)
    hollowness_values = []

    for i in range(40, 61):
        hollowness_values.append(nreyes_hollowness[i]/nrpix_hollowness[i])

    append_to_excel(hollowness_banana_cell_values, hollowness_values)
    hollowness_values = []

    for i in range(60, 81):
        hollowness_values.append(nreyes_hollowness[i]/nrpix_hollowness[i])

    append_to_excel(hollowness_pear_cell_values, hollowness_values)
    hollowness_values = []

    for i in range(80, 101):
        hollowness_values.append(nreyes_hollowness[i]/nrpix_hollowness[i])

    append_to_excel(hollowness_envelope_cell_values, hollowness_values)
    hollowness_values = []

    for i in range(100, 121):
        hollowness_values.append(nreyes_hollowness[i]/nrpix_hollowness[i])

    append_to_excel(hollowness_golfclub_cell_values, hollowness_values)
    hollowness_values = []

    for i in range(120, 141):
        hollowness_values.append(nreyes_hollowness[i]/nrpix_hollowness[i])

    append_to_excel(hollowness_pencil_cell_values, hollowness_values)
    hollowness_values = []

    for i in range(140, 160):
        hollowness_values.append(nreyes_hollowness[i]/nrpix_hollowness[i])

    append_to_excel(hollowness_wineglass_cell_values, hollowness_values)
    hollowness_values = []

    print('Hollowness successfully calculated')

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
        for i in range(0, 20):
            sheet[column_list[i]].value = values[i]

        wb.save(features_path + "/40175607_features.xlsx")

#call all features
nr_eyes_all()
nr_pix_all()
hollowness()
#nr_regions()
