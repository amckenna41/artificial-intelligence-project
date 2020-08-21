#File for nrpix, height, width and black pixel proportion (feature 20)

#import pandas and openpyxl library
import pandas as pd
import openpyxl
import os #os module - used to create the relative file paths

#features_path variable to hold the relative pathname for features file

current_working_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_working_dir)
parent_dir = os.path.abspath(os.path.join(current_working_dir, os.pardir))
features_path =  parent_dir + '/section2_features'

#To execute files in Terminal, right click on section2_code folder and open new Terminal window from here
#this sets the correct directory for execution

#import all file paths from allfile_paths file
from allfile_paths import *
#import all cell values from allcell_values file
from allcell_values import *

#Variables below are the initialisation of lists that are used to store the values that are to be written
#to their coresponding feature cell values in allcell_values file

nr_pix_values = []
height_values = []
width_values = []
nr_black_pix_values = []
nrwhitepix_values = []


#Below code creates a subset of lists for each of the images from their respective main cell values list in allcell_values file
#Each list subset has length = 20 as it contains 20 cell values. 20 cell values for the 20 images for each image type.
#This code ensures that the correct value is being written to the correct cell in the excel file.

nr_pix_cherry_cell_values = nr_pix_cell_values[:20]
nr_pix_flower_cell_values = nr_pix_cell_values[20:41]
nr_pix_banana_cell_values = nr_pix_cell_values[40:61]
nr_pix_pear_cell_values = nr_pix_cell_values[60:81]
nr_pix_envelope_cell_values = nr_pix_cell_values[80:101]
nr_pix_golfclub_cell_values = nr_pix_cell_values[100:121]
nr_pix_pencil_cell_values = nr_pix_cell_values[120:141]
nr_pix_wineglass_cell_values = nr_pix_cell_values[140:161]

height_cheery_cell_values = height_cell_values[:20]
height_flower_cell_values = height_cell_values[20:41]
height_banana_cell_values = height_cell_values[40:61]
height_pear_cell_values = height_cell_values[60:81]
height_envelope_cell_values = height_cell_values[80:101]
height_golfclub_cell_values = height_cell_values[100:121]
height_pencil_cell_values = height_cell_values[120:141]
height_wineglass_cell_values = height_cell_values[140:161]

width_cheery_cell_values = width_cell_values[:20]
width_flower_cell_values = width_cell_values[20:41]
width_banana_cell_values = width_cell_values[40:61]
width_pear_cell_values = width_cell_values[60:81]
width_envelope_cell_values = width_cell_values[80:101]
width_golfclub_cell_values = width_cell_values[100:121]
width_pencil_cell_values = width_cell_values[120:141]
width_wineglass_cell_values = width_cell_values[140:161]

blackpixprop_cherry_cell_values = black_pixel_proportion[:20]
blackpixprop_flower_cell_values = black_pixel_proportion[20:41]
blackpixprop_banana_cell_values = black_pixel_proportion[40:61]
blackpixprop_pear_cell_values = black_pixel_proportion[60:81]
blackpixprop_envelope_cell_values = black_pixel_proportion[80:101]
blackpixprop_golfclub_cell_values = black_pixel_proportion[100:121]
blackpixprop_pencil_cell_values = black_pixel_proportion[120:141]
blackpixprop_wineglass_cell_values = black_pixel_proportion[140:161]


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

    #resultant nr_pix value is appended to the nr_pix values list
    nr_pix_values.append(nr_pix_count)

    #nr_pix value also apeneded to other list that is used for the black pixel proportion feature
    nr_black_pix_values.append(nr_pix_count)

#nr_pix_all function is used to call the nr_pix function to calculate
#nr_pix value for each image

def nr_pix_all():

    #set variables to global so that they can be used locally
    global nr_pix_values
    global nr_pix_cell_values

    #for loops to calculate total number of black pixels for each image
    #append_to_excel function is called with the parameters of - values calculated from nr_pix function
    #and the cell values at which these nr_pix values are to be written to
    #list to store nr_pix values is set to 0 after every image type has been iterated through

    for i in range(0, len(cherry_path)):
        nr_pix(cherry_path[i])

    append_to_excel(nr_pix_cherry_cell_values, nr_pix_values)
    nr_pix_values = []

    #number of pix all
    for i in range(0, len(cherry_path)):
        nr_pix(flower_path[i])

    append_to_excel(nr_pix_flower_cell_values, nr_pix_values)
    nr_pix_values = []

    for i in range(0, len(cherry_path)):
        nr_pix(banana_path[i])

    append_to_excel(nr_pix_banana_cell_values, nr_pix_values)
    nr_pix_values = []

    for i in range(0, len(cherry_path)):
        nr_pix(pear_path[i])

    append_to_excel(nr_pix_pear_cell_values, nr_pix_values)
    nr_pix_values = []

    for i in range(0, len(cherry_path)):
        nr_pix(envelope_path[i])

    append_to_excel(nr_pix_envelope_cell_values, nr_pix_values)
    nr_pix_values = []

    for i in range(0, len(cherry_path)):
        nr_pix(golfclub_path[i])

    append_to_excel(nr_pix_golfclub_cell_values, nr_pix_values)
    nr_pix_values = []

    for i in range(0, len(cherry_path)):
        nr_pix(pencil_path[i])

    append_to_excel(nr_pix_pencil_cell_values, nr_pix_values)
    nr_pix_values = []

    for i in range(0, len(cherry_path)):
        nr_pix(wineglass_path[i])

    append_to_excel(nr_pix_wineglass_cell_values, nr_pix_values)
    nr_pix_values = []

    print('Number of black pixels successfully calculated')

#height function is used to calculate the vertical distance in images
#vertical distance is the distance between the topmost and bottommost black pixel

def height(path):

    #initialise variables
    global height_values
    top_pixel = 0
    bottom_pixel = 0
    black_pixel_found = False
    height = 0

    #convert csv to dataframe
    dataframe = pd.read_csv(path)


    #for loop to acquire the index of the topmost black pixel
    #once first black pixel is found, break statement used to break out of loop
    #Python has no functionality for breaking out of a nested loop hence the
    #need for the extra if statement in for loop

    for row in range(0, dataframe.shape[0]):
        for col in range(0, dataframe.shape[1]):
            if dataframe.values[row][col] == 1:
                        top_pixel = row
                        black_pixel_found = True
                        break
            if black_pixel_found:
                break


    #for loop to acquire index of the bottommost black pixel
    #at every iteration, the bottom_pixel value is set to the row value
    #the last iteration of the for loop will thus give the bottomost pixel / row

    for row in range(0, dataframe.shape[0]):
        for col in range(0, dataframe.shape[1]):
            if dataframe.values[row][col] == 1:
                bottom_pixel = row


    #calculate height by subtracting top_pixel from bottom_pixel
    height = bottom_pixel - top_pixel

    #resultant height value is appended to the height_values list
    height_values.append(height)

#height_all function is used to call the height function to calculate
#height value for each image

def height_all():

        #set variables to global so that they can be used locally
        global height_values
        global height_cell_values

        #for loops below has the exact same functionality as the one in above function nr_pix_all

        for i in range(0, len(cherry_path)):
            height(cherry_path[i])

        append_to_excel(height_cheery_cell_values, height_values)
        height_values = []

        for i in range(0, len(cherry_path)):
            height(flower_path[i])

        append_to_excel(height_flower_cell_values, height_values)
        height_values = []

        for i in range(0, len(cherry_path)):
            height(banana_path[i])

        append_to_excel(height_banana_cell_values, height_values)
        height_values = []

        for i in range(0, len(cherry_path)):
            height(pear_path[i])

        append_to_excel(height_pear_cell_values, height_values)
        height_values = []

        for i in range(0, len(cherry_path)):
            height(envelope_path[i])

        append_to_excel(height_envelope_cell_values, height_values)
        height_values = []

        for i in range(0, len(cherry_path)):
            height(golfclub_path[i])

        append_to_excel(height_golfclub_cell_values, height_values)
        height_values = []

        for i in range(0, len(cherry_path)):
            height(pencil_path[i])

        append_to_excel(height_pencil_cell_values, height_values)
        height_values = []

        for i in range(0, len(cherry_path)):
            height(wineglass_path[i])

        append_to_excel(height_wineglass_cell_values, height_values)
        height_values = []

        print('Height values successfully calculated')

#width function calculates the horizontal distance  of each image
#horizontal distance is the distance between leftmost and rightmost pixels

def width(path):

    #initialise variables
    global width_values
    left_pixel = 0
    right_pixel = 0
    width = 0
    col_list = []

    #convert csv to dataframe
    dataframe = pd.read_csv(path)


    #for loop to get the leftmost pixel
    #when a black pixel is found its respective column value is appended to a list of column values

    for row in range(0, dataframe.shape[0]):
        for col in range(0, dataframe.shape[1]):
            if dataframe.values[row][col] == 1:
                    col_list.append(col)

    #to get leftmost pixel value get the minimum value in column list
    #the smallest value in the column list = leftmost pixel column value

    left_pixel = min(col_list)

    #for loop to get the rightmost pixel
    #when a black pixel is found its respective column value is stored in right_pixel variable
    #last iteration of for loop = rightmost column value / rightmost black pixel value

    for row in range(0, dataframe.shape[0]):
        for col in range(0, dataframe.shape[1]):
            if dataframe.values[row][col] == 1:
                right_pixel = col


    #calculate width by subtracting leftmost from rightmost column values
    width = right_pixel - left_pixel

    #resultant width value is appended to the width_values list
    width_values.append(width)

#width_all function is used to call the width function to calculate
#width value for each image

def width_all():

    #set variables to global so that they can be accessed locally
    global width_values
    global width_cell_values

    #for loops below has the exact same functionality as the one in above functions nr_pix_all/height_all

    for i in range(0, len(cherry_path)):
        width(cherry_path[i])

    append_to_excel(width_cheery_cell_values, width_values)
    width_values = []

    for i in range(0, len(cherry_path)):
        width(flower_path[i])

    append_to_excel(width_flower_cell_values, width_values)
    width_values = []

    for i in range(0, len(cherry_path)):
        width(banana_path[i])

    append_to_excel(width_banana_cell_values, width_values)
    width_values = []

    for i in range(0, len(cherry_path)):
        width(pear_path[i])

    append_to_excel(width_pear_cell_values, width_values)
    width_values = []

    for i in range(0, len(cherry_path)):
        width(envelope_path[i])

    append_to_excel(width_envelope_cell_values, width_values)
    width_values = []

    for i in range(0, len(cherry_path)):
        width(golfclub_path[i])

    append_to_excel(width_golfclub_cell_values, width_values)
    width_values = []

    for i in range(0, len(cherry_path)):
        width(pencil_path[i])

    append_to_excel(width_pencil_cell_values, width_values)
    width_values = []

    for i in range(0, len(cherry_path)):
        width(wineglass_path[i])

    append_to_excel(width_wineglass_cell_values, width_values)
    width_values = []


    print('Width values successfully calculated')

#nr_white_pix function calculates the total number of white pixels in the image

def nr_white_pix(path):

    #initialise variables
    nr_white_pix_count = 0

    #convert csv to dataframe
    dataframe = pd.read_csv(path)


    #Similar functionality to nr_pix feature
    #Iterate through dataframe and increment counter by one every time a white pixel is found
    for row in range(dataframe.shape[0]):
        for col in range(dataframe.shape[1]):
            if dataframe.values[row][col] == 0:
                nr_white_pix_count = nr_white_pix_count + 1

    #white pixel count apened to a list of total white pixel values
    nrwhitepix_values.append(nr_white_pix_count)

#nr_white_pix_all function is used to call the nr_white_pix function for all the images
#to calculate the number of white pixels in each image

def nr_white_pix_all():

        #set variables to global so that they can be used locally
        global nrwhitepix_values
        global nrwhitepixcell_values

        #for loops below loop through all of the 20 images in each image type
        #calling the nr_white_pix function to calculate the total number of white pixels in the image

        for i in range(0, len(cherry_path)):
            nr_white_pix(cherry_path[i])

        for i in range(0, len(cherry_path)):
            nr_white_pix(flower_path[i])

        for i in range(0, len(cherry_path)):
            nr_white_pix(banana_path[i])

        for i in range(0, len(cherry_path)):
            nr_white_pix(pear_path[i])

        for i in range(0, len(cherry_path)):
            nr_white_pix(envelope_path[i])

        for i in range(0, len(cherry_path)):
            nr_white_pix(golfclub_path[i])

        for i in range(0, len(cherry_path)):
            nr_white_pix(pencil_path[i])

        for i in range(0, len(cherry_path)):
            nr_white_pix(wineglass_path[i])

        print('Total number of white pixels successfully calculated')

#getblackpixproportion function is used to call the nr_white_pix function and the nr_pix function
#to get the total white and black pixel number and then the proprotion of black pixels is calculated

def getblackpixproportion():

    #set variables to global so they can be used locally
    global nr_black_pix_values
    global nrwhitepix_values

    #initialise list
    total_prop = []

    #for loops below has the exact same functionality as the one in above functions nr_pix_all/height_all/width_all
    #the % of black pixels in the image is calculated by getting the black pixel value and the white pixel value
    #from their respective lists and dividing the value at the specified index and multipling by 100 to get as %

    for i in range(0, len(cherry_path)):
        total_prop.append((nr_black_pix_values[i] / nrwhitepix_values[i])* 100)

    append_to_excel(blackpixprop_cherry_cell_values, total_prop)

    for i in range(20, 41):
        total_prop.append((nr_black_pix_values[i] / nrwhitepix_values[i])* 100)

    append_to_excel(blackpixprop_flower_cell_values, total_prop)

    for i in range(40, 61):
        total_prop.append((nr_black_pix_values[i] / nrwhitepix_values[i])* 100)

    append_to_excel(blackpixprop_banana_cell_values, total_prop)

    for i in range(60, 81):
        total_prop.append((nr_black_pix_values[i] / nrwhitepix_values[i])* 100)

    append_to_excel(blackpixprop_pear_cell_values, total_prop)

    for i in range(80, 101):
        total_prop.append((nr_black_pix_values[i] / nrwhitepix_values[i])* 100)

    append_to_excel(blackpixprop_envelope_cell_values, total_prop)

    for i in range(100, 121):
        total_prop.append((nr_black_pix_values[i] / nrwhitepix_values[i])* 100)

    append_to_excel(blackpixprop_golfclub_cell_values, total_prop)

    for i in range(120, 141):
        total_prop.append((nr_black_pix_values[i] / nrwhitepix_values[i])* 100)

    append_to_excel(blackpixprop_pencil_cell_values, total_prop)

    for i in range(140, 160):
        total_prop.append((nr_black_pix_values[i] / nrwhitepix_values[i])* 100)

    append_to_excel(blackpixprop_wineglass_cell_values, total_prop)

    print('Black pixel proportion successfully calculated')

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
        for i in range(0, len(nr_pix_cherry_cell_values)):
            sheet[column_list[i]].value = values[i]

        #save excel file with updated cell values
        wb.save(features_path + "/40175607_features.xlsx")

#call all functions
nr_pix_all()
nr_white_pix_all()
getblackpixproportion()
height_all()
width_all()
