#File for left2tile, right2tile, top2tile, bottom2tile, horizontalness, verticalness, white3tile

#import pandas and openpyxl library
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

left2tile_values = []
right2tile_values = []
verticalness_values = []
top2tile_values = []
bottom2tile_values = []
horizontalness_values = []
white3tile_values = []

#Below code creates a subset of lists for each of the images from their respective  main cell values list in allcell_values file
#Each list subset has length = 20 as it contains 20 cell values. 20 cell values for the 20 images for each image type.
#This code ensures that the correct value is being written to the correct cell in the excel file.
#There are 8 subset lists for the 8 images for each individual feature

cherry_cell_values = left2tile_cell_values[:20]
flower_cell_values = left2tile_cell_values[20:41]
banana_cell_values = left2tile_cell_values[40:61]
pear_cell_values = left2tile_cell_values[60:81]
envelope_cell_values = left2tile_cell_values[80:101]
golfclub_cell_values = left2tile_cell_values[100:121]
pencil_cell_values = left2tile_cell_values[120:141]
wineglass_cell_values = left2tile_cell_values[140:161]

right_cherry_cell_values = right2tile_cell_values[:20]
right_flower_cell_values = right2tile_cell_values[20:41]
right_banana_cell_values = right2tile_cell_values[40:61]
right_pear_cell_values = right2tile_cell_values[60:81]
right_envelope_cell_values = right2tile_cell_values[80:101]
right_golfclub_cell_values = right2tile_cell_values[100:121]
right_pencil_cell_values = right2tile_cell_values[120:141]
right_wineglass_cell_values = right2tile_cell_values[140:161]

top_cherry_cell_values = top2tile_cell_values[:20]
top_flower_cell_values = top2tile_cell_values[20:41]
top_banana_cell_values = top2tile_cell_values[40:61]
top_pear_cell_values = top2tile_cell_values[60:81]
top_envelope_cell_values = top2tile_cell_values[80:101]
top_golfclub_cell_values = top2tile_cell_values[100:121]
top_pencil_cell_values = top2tile_cell_values[120:141]
top_wineglass_cell_values = top2tile_cell_values[140:161]

bottom_cherry_cell_values = bottom2tile_cell_values[:20]
bottom_flower_cell_values = bottom2tile_cell_values[20:41]
bottom_banana_cell_values = bottom2tile_cell_values[40:61]
bottom_pear_cell_values = bottom2tile_cell_values[60:81]
bottom_envelope_cell_values = bottom2tile_cell_values[80:101]
bottom_golfclub_cell_values = bottom2tile_cell_values[100:121]
bottom_pencil_cell_values = bottom2tile_cell_values[120:141]
bottom_wineglass_cell_values = bottom2tile_cell_values[140:161]

vert_cherry_cell_values = verticalness_cell_values[:20]
vert_flower_cell_values = verticalness_cell_values[20:41]
vert_banana_cell_values = verticalness_cell_values[40:61]
vert_pear_cell_values = verticalness_cell_values[60:81]
vert_envelope_cell_values = verticalness_cell_values[80:101]
vert_golfclub_cell_values = verticalness_cell_values[100:121]
vert_pencil_cell_values = verticalness_cell_values[120:141]
vert_wineglass_cell_values = verticalness_cell_values[140:161]

horiz_cherry_cell_values = horizontalness_cell_values[:20]
horiz_flower_cell_values = horizontalness_cell_values[20:41]
horiz_banana_cell_values = horizontalness_cell_values[40:61]
horiz_pear_cell_values = horizontalness_cell_values[60:81]
horiz_envelope_cell_values = horizontalness_cell_values[80:101]
horiz_golfclub_cell_values = horizontalness_cell_values[100:121]
horiz_pencil_cell_values = horizontalness_cell_values[120:141]
horiz_wineglass_cell_values = horizontalness_cell_values[140:161]

white3tile_cherry_cell_values = white3tilecell_values[:20]
white3tile_flower_cell_values = white3tilecell_values[20:41]
white3tile_banana_cell_values = white3tilecell_values[40:61]
white3tile_pear_cell_values = white3tilecell_values[60:81]
white3tile_envelope_cell_values = white3tilecell_values[80:101]
white3tile_golfclub_cell_values = white3tilecell_values[100:121]
white3tile_pencil_cell_values = white3tilecell_values[120:141]
white3tile_wineglass_cell_values = white3tilecell_values[140:161]


#Initilisation of lists for calculating verticalness and horizontalness
#These lists are appeneded in their respective functions
#Lists are used in the verticalness and horizontalness functions

verticalness_total = []
vertical_lefttile = []
vertical_righttile = []
vertical_nr_pix = []

horizontalness_total = []
horizontalness_toptile = []
horizontalness_bottomtile = []
horizontalness_nr_pix = []

#left2tile function calculates the number of unique 2-tiles in the image
#where the leftmost 2 entries are black and the rightmost entries are white.

def left2tile(path):

    #initialise variables
    global left2tile_values
    global vertical_lefttile
    upper_black_tile = False
    lower_black_tile = False
    two_black_tiles = 0

    #convert csc to dataframe
    dataframe = pd.read_csv(path)

    #loop through each row & column and determine if upper and or lower pixel is black pixel
    #if statement to determine if two pixels to the right are white. If true, increment 2 black tiles counter

    for row in range(0, dataframe.shape[0]-1):
         for col in range(0, dataframe.shape[1]-1):
            if dataframe.values[row][col] == 1:
                if dataframe.values[row-1][col] ==1:        #upper pixel to central pixel is black
                    upper_black_tile = True
                if dataframe.values[row+1][col] == 1:       #lower pixel to central pixel is black
                    lower_black_tile = True

            #if statements to calculate if the 2 pixels to the right of black pixel are white
            #if two rightmost pixels are white then increment two_black_tiles counter
            if upper_black_tile and dataframe.values[row-1][col+1] !=1 and dataframe.values[row][col+1] !=1:
                two_black_tiles = two_black_tiles + 1

            #if statement below is neccessary since the 2-tiles may overlap
            #black pixel can have both upper and lower black pixels that can be part of a 2-tile
            #if statement validates that rightmost 2 pixels are white
            if lower_black_tile and dataframe.values[row+1][col+1] != 1 and dataframe.values[row][col+1] != 1:
                two_black_tiles = two_black_tiles + 1


            #reset bool values to False for next iteration
            upper_black_tile = False
            lower_black_tile = False

    #resultant left2tile value is appended to left2tile_values list
    left2tile_values.append(two_black_tiles)

    #resultant left2tile value is also apened to vertical_lefttile list for calculating the verticalness value later
    vertical_lefttile.append(two_black_tiles)

#left2tile_all function is used to call the left2tile function to calculate
#left2tile value for each image

def left2tile_all():

    #set variables to gloabl so that they can be used locally
    global left2tile_values
    global left2tile_cell_values

    #for loops to calculate total left2tile values for each image
    #append_to_excel function is called with the parameters of - values calculated from left2tile function
    #and the cell values at which these left2tile values are to be written to
    #list to store left2tile values is set to 0 after every image type has been iterated through

    for i in range(0, len(cherry_path)):
        left2tile(cherry_path[i])

    append_to_excel(cherry_cell_values, left2tile_values)
    left2tile_values = []

    for i in range(0, len(cherry_path)):
        left2tile(flower_path[i])

    append_to_excel(flower_cell_values, left2tile_values)
    left2tile_values = []

    for i in range(0, len(cherry_path)):
        left2tile(banana_path[i])

    append_to_excel(banana_cell_values, left2tile_values)
    left2tile_values = []

    for i in range(0, len(cherry_path)):
        left2tile(pear_path[i])

    append_to_excel(pear_cell_values, left2tile_values)
    left2tile_values = []

    for i in range(0, len(cherry_path)):
        left2tile(envelope_path[i])

    append_to_excel(envelope_cell_values, left2tile_values)
    left2tile_values = []

    for i in range(0, len(cherry_path)):
        left2tile(golfclub_path[i])

    append_to_excel(golfclub_cell_values, left2tile_values)
    left2tile_values = []

    for i in range(0, len(cherry_path)):
        left2tile(pencil_path[i])

    append_to_excel(pencil_cell_values, left2tile_values)
    left2tile_values = []

    for i in range(0, len(cherry_path)):
        left2tile(wineglass_path[i])

    append_to_excel(wineglass_cell_values, left2tile_values)
    left2tile_values = []

    print('Left 2-tile values successfully calculated')

#right2tile function calculates the number of unique 2-tiles in the image
#where the rightmost 2 entries are black and the leftmost entries are white.

def right2tile(path):

    #initialise variables
    global right2tile_values
    global vertical_righttile
    upper_black_tile = False
    lower_black_tile = False
    two_black_tiles = 0

    #convert csv to dataframe
    dataframe = pd.read_csv(path)

    #loop through each row & column and determine if upper and or lower pixel is black pixel
    #if statement to determine if two pixels to the right are black. If true, increment 2 black tiles counter

    for row in range(0, dataframe.shape[0]-1):
         for col in range(0, dataframe.shape[1]-1):
            if dataframe.values[row][col] == 1:
                if dataframe.values[row-1][col] ==1:        #upper pixel to central is black
                    upper_black_tile = True
                if dataframe.values[row+1][col] == 1:       #lower pixel to central is black
                    lower_black_tile = True

            #if statements to calculate if the 2 pixels to the left of black pixel are white
            #if two leftmost pixels are white then increment two_black_tiles counter
            if upper_black_tile and dataframe.values[row-1][col-1] !=1 and dataframe.values[row][col-1] !=1:
                two_black_tiles = two_black_tiles + 1

            #if statement below is neccessary since the 2-tiles may overlap
            #black pixel can have both upper and lower black pixels that can be part of a 2-tile
            #if statement validates that leftmost 2 pixels are white / rightmost are black
            if lower_black_tile and dataframe.values[row+1][col-1] != 1 and dataframe.values[row][col-1] != 1:
                two_black_tiles = two_black_tiles + 1

            #reset bool values to False for next iteration
            upper_black_tile = False
            lower_black_tile = False

    #resultant right2tile value is appended to right2tile_values list
    right2tile_values.append(two_black_tiles)

    #resultant right2tile value is also appended to vertical_righttile list for calculating the verticalness value later
    vertical_righttile.append(two_black_tiles)

#right2tile_all function is used to call the right2tile function to calculate
#right2tile value for each image

def right2tile_all():

        #set variables to global so that they can be used locally
        global right2tile_values
        global right2tile_cell_values

        #for loops below have the exact same functionality as the one in above function left2tile_all

        for i in range(0, len(cherry_path)):
            right2tile(cherry_path[i])

        append_to_excel(right_cherry_cell_values, right2tile_values)
        right2tile_values = []

        for i in range(0, len(cherry_path)):
            right2tile(flower_path[i])

        append_to_excel(right_flower_cell_values, right2tile_values)
        right2tile_values = []

        for i in range(0, len(cherry_path)):
            right2tile(banana_path[i])

        append_to_excel(right_banana_cell_values, right2tile_values)
        right2tile_values = []

        for i in range(0, len(cherry_path)):
            right2tile(pear_path[i])

        append_to_excel(right_pear_cell_values, right2tile_values)
        right2tile_values = []

        for i in range(0, len(cherry_path)):
            right2tile(envelope_path[i])

        append_to_excel(right_envelope_cell_values, right2tile_values)
        right2tile_values = []

        for i in range(0, len(cherry_path)):
            right2tile(golfclub_path[i])

        append_to_excel(right_golfclub_cell_values, right2tile_values)
        right2tile_values = []

        for i in range(0, len(cherry_path)):
            right2tile(pencil_path[i])

        append_to_excel(right_pencil_cell_values, right2tile_values)
        right2tile_values = []

        for i in range(0, len(cherry_path)):
            right2tile(wineglass_path[i])

        append_to_excel(right_wineglass_cell_values, right2tile_values)
        right2tile_values = []

        print('Right 2-tile values successfully calculated')

#nrpix function calculates the total number of black pixels in image
#This function is required for the horizontalness and verticalness functions

def nr_pix(path):

    #convert csv to dataframe
    dataframe = pd.read_csv(path)

    #initialise variables
    nr_pix_count = 0
    global vertical_nr_pix
    global horizontalness_nr_pix

    #for loop loops through every pixel in image
    #if a black pixel is found then a counter is incremented

    for row in range(dataframe.shape[0]):
        for col in range(dataframe.shape[1]):
            if dataframe.values[row][col] == 1:
                nr_pix_count = nr_pix_count + 1

    #resultant nr_pix value is appended to the vertical_nr_pix values list for verticalness function
    vertical_nr_pix.append(nr_pix_count)

    #resultant nr_pix value is appended to the horizontalness_nr_pix values list for horizontalness function
    horizontalness_nr_pix.append(nr_pix_count)

#nr_pix_all function is used to call the nr_pix function to calculate
#nr_pix value for each image

def nr_pix_all():

    #set variables to global so that they can be used locally
    global nr_pix_values
    global cell_values

    #for loops loop through all 8 image types and calls the nr_pix function

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

    print('Number of pixels successfully calculated')

#verticalness function calculates the sum of left2tile and right2tile, divided by the number of black pixels in the image

def verticalness():

    #set variables to global so they can be used locally
    global vertical_lefttile
    global vertical_righttile
    global vertical_nr_pix
    sum = []
    total_vert = []

    #for loop loops through each image, calculates its verticalness and writes to excel file
    #sum of left2tile and right2tile at specified index is calculated and stored in a list of sums at the same index value
    #verticalness is then calculated from the sum at index i divided by the number of pixels at index i in vertical_nr_pix list
    #append_to_excel function is then called with the parameters of the cell values to be written to and the data to be
    #written to these cell values (verticalness)

    for i in range(0, len(cherry_cell_values)):
        sum.append(vertical_lefttile[i] + vertical_righttile[i])
        total_vert.append(sum[i]/vertical_nr_pix[i])

    append_to_excel(vert_cherry_cell_values, total_vert)
    total_vert = []

    for i in range(20, 41):
        sum.append(vertical_lefttile[i] + vertical_righttile[i])
        total_vert.append(sum[i]/vertical_nr_pix[i])

    append_to_excel(vert_flower_cell_values, total_vert)
    total_vert = []

    for i in range(40, 61):
        sum.append(vertical_lefttile[i] + vertical_righttile[i])
        total_vert.append(sum[i]/vertical_nr_pix[i])

    append_to_excel(vert_banana_cell_values, total_vert)
    total_vert = []

    for i in range(60, 81):
        sum.append(vertical_lefttile[i] + vertical_righttile[i])
        total_vert.append(sum[i]/vertical_nr_pix[i])

    append_to_excel(vert_pear_cell_values, total_vert)
    total_vert = []

    for i in range(80, 101):
        sum.append(vertical_lefttile[i] + vertical_righttile[i])
        total_vert.append(sum[i]/vertical_nr_pix[i])

    append_to_excel(vert_envelope_cell_values, total_vert)
    total_vert = []

    for i in range(100, 121):
        sum.append(vertical_lefttile[i] + vertical_righttile[i])
        total_vert.append(sum[i]/vertical_nr_pix[i])

    append_to_excel(vert_golfclub_cell_values, total_vert)
    total_vert = []

    for i in range(120, 141):
        sum.append(vertical_lefttile[i] + vertical_righttile[i])
        total_vert.append(sum[i]/vertical_nr_pix[i])

    append_to_excel(vert_pencil_cell_values, total_vert)
    total_vert = []

    for i in range(140, 160):
        sum.append(vertical_lefttile[i] + vertical_righttile[i])
        total_vert.append(sum[i]/vertical_nr_pix[i])

    append_to_excel(vert_wineglass_cell_values, total_vert)
    total_vert = []

    print('Verticalness successfully calculated')

#top2tile function calculates the number of unique 2-tiles in image where the top two entries
#are black pixels and the bottomost two entries are white

def top2tile(path):

    #initialise variables
    left_black_tile = False
    right_black_tile = False
    two_black_tiles = 0
    global top2tile_values
    global horizontalness_toptile

    #convert csv to dataframe
    dataframe = pd.read_csv(path)

    #loop through each row & column and determine if right and or left pixel is black pixel
    #if statement to determine if topmost two pixels are black. If true, increment 2 black tiles counter

    for row in range(0, dataframe.shape[0]-1):
         for col in range(0, dataframe.shape[1]-1):
            if dataframe.values[row][col] == 1:
                if dataframe.values[row][col+1] ==1:        #right pixel to central pixel is black
                    right_black_tile = True
                if dataframe.values[row][col-1] == 1:       #left pixel to central pixel is black
                    left_black_tile = True

            #if statements to calculate if the 2 bottomost pixels are white
            #if two bottomost pixels are white and two topmost are black then increment two_black_tiles counter
            if right_black_tile and dataframe.values[row+1][col] !=1 and dataframe.values[row+1][col+1] !=1:
                two_black_tiles = two_black_tiles + 1

            #if statement below is neccessary since the 2-tiles may overlap
            #black pixel can have both left and right black pixels that can be part of a 2-tile
            #if statement validates that bottomost 2 pixels are white / topmost are black
            if left_black_tile and dataframe.values[row+1][col] != 1 and dataframe.values[row+1][col-1] != 1:
                two_black_tiles = two_black_tiles + 1


            #reset bool values to False for next iteration
            right_black_tile = False
            left_black_tile = False


    #resultant top2tile value is appended to top2tile_values list
    top2tile_values.append(two_black_tiles)

    #resultant top2tile value is also appended to horizontalness_toptile list for calculating the horizontalness value later
    horizontalness_toptile.append(two_black_tiles)

#top2tile_all function is used to call the top2tile function to calculate
#top2tile value for each image

def top2tile_all():

        #set variables to global so they can be used locally
        global top2tile_values
        global top2tile_cell_values

        #for loops below have the exact same functionality as the ones in above function left2tile_all and right2tile_all

        for i in range(0, len(cherry_path)):
            top2tile(cherry_path[i])

        append_to_excel(top_cherry_cell_values, top2tile_values)
        top2tile_values = []

        for i in range(0, len(cherry_path)):
            top2tile(flower_path[i])

        append_to_excel(top_flower_cell_values, top2tile_values)
        top2tile_values = []

        for i in range(0, len(cherry_path)):
            top2tile(banana_path[i])

        append_to_excel(top_banana_cell_values, top2tile_values)
        top2tile_values = []

        for i in range(0, len(cherry_path)):
            top2tile(pear_path[i])

        append_to_excel(top_pear_cell_values, top2tile_values)
        top2tile_values = []

        for i in range(0, len(cherry_path)):
            top2tile(envelope_path[i])

        append_to_excel(top_envelope_cell_values, top2tile_values)
        top2tile_values = []

        for i in range(0, len(cherry_path)):
            top2tile(golfclub_path[i])

        append_to_excel(top_golfclub_cell_values, top2tile_values)
        top2tile_values = []

        for i in range(0, len(cherry_path)):
            top2tile(pencil_path[i])

        append_to_excel(top_pencil_cell_values, top2tile_values)
        top2tile_values = []

        for i in range(0, len(cherry_path)):
            top2tile(wineglass_path[i])

        append_to_excel(top_wineglass_cell_values, top2tile_values)
        top2tile_values = []

        print('Top 2-tile values successfully calculated')

#bottom2tile function calculates the number of unique 2-tiles in image where the bottommost two entries
#are black pixels and the topmost two entries are white

def bottom2tile(path):

    #initialise variables
    global bottom2tile_values
    global horizontalness_bottomtile
    left_black_tile = False
    right_black_tile = False
    two_black_tiles = 0

    #convert csv to dataframe
    dataframe = pd.read_csv(path)

    #loop through each row & column and determine if left and or right pixel is black pixel
    #if statement to determine if bottommost two pixels are black. If true, increment 2 black tiles counter

    for row in range(0, dataframe.shape[0]-1):
         for col in range(0, dataframe.shape[1]-1):
            if dataframe.values[row][col] == 1:
                if dataframe.values[row][col+1] ==1:        #right pixel to central pixel is black
                    right_black_tile = True
                if dataframe.values[row][col-1] == 1:       #left pixel to central pixel is black
                    left_black_tile = True

            #if statements to calculate if the 2 topmost pixels pixels are white
            #if two topmost pixels are white and two bottomost pixels are black hen increment two_black_tiles counter
            if right_black_tile and dataframe.values[row-1][col] !=1 and dataframe.values[row-1][col+1] !=1:
                two_black_tiles = two_black_tiles + 1

            #if statement below is neccessary since the 2-tiles may overlap
            #black pixel can have both left and right black pixels that can be part of a 2-tile
            #if statement validates that topmost 2 pixels are white / bottomost are black
            if left_black_tile and dataframe.values[row-1][col] != 1 and dataframe.values[row-1][col-1] != 1:
                two_black_tiles = two_black_tiles + 1


            #reset bool values to False for next iteration
            right_black_tile = False
            left_black_tile = False

    #resultant bottom2tile value is appended to bottom2tile_values list
    bottom2tile_values.append(two_black_tiles)

    #resultant bottom2tile value is also appended to horizontalness_bottomtile list for calculating the horizontalness value later
    horizontalness_bottomtile.append(two_black_tiles)

#bottom2tile_all function is used to call the bottom2tile function to calculate
#bottom2tile value for each image

def bottom2tile_all():

        #set variables to global so they can be used locally
        global bottom2tile_values
        global bottom2tile_cell_values

        #for loops below have the exact same functionality as the ones in above function left2tile_all, right2tile_all and top2tile_all

        for i in range(0, len(cherry_path)):
            bottom2tile(cherry_path[i])

        append_to_excel(bottom_cherry_cell_values, bottom2tile_values)
        bottom2tile_values = []

        for i in range(0, len(cherry_path)):
            bottom2tile(flower_path[i])

        append_to_excel(bottom_flower_cell_values, bottom2tile_values)
        bottom2tile_values = []

        for i in range(0, len(cherry_path)):
            bottom2tile(banana_path[i])

        append_to_excel(bottom_banana_cell_values, bottom2tile_values)
        bottom2tile_values = []

        for i in range(0, len(cherry_path)):
            bottom2tile(pear_path[i])

        append_to_excel(bottom_pear_cell_values, bottom2tile_values)
        bottom2tile_values = []

        for i in range(0, len(cherry_path)):
            bottom2tile(envelope_path[i])

        append_to_excel(bottom_envelope_cell_values, bottom2tile_values)
        bottom2tile_values = []

        for i in range(0, len(cherry_path)):
            bottom2tile(golfclub_path[i])

        append_to_excel(bottom_golfclub_cell_values, bottom2tile_values)
        bottom2tile_values = []

        for i in range(0, len(cherry_path)):
            bottom2tile(pencil_path[i])

        append_to_excel(bottom_pencil_cell_values, bottom2tile_values)
        bottom2tile_values = []

        for i in range(0, len(cherry_path)):
            bottom2tile(wineglass_path[i])

        append_to_excel(bottom_wineglass_cell_values, bottom2tile_values)
        bottom2tile_values = []


        print('Bottom 2-tile values successfully calculated')

#horizontalness function calculates the sum of top2tile and bottom2tile, divided by the number of black pixels

def horizontalness():

    #set variables to gloabl so they can be used locally
    global horizontalness_toptile
    global horizontalness_bottomtile
    global vertical_nr_pix
    global horizontalness_nr_pix
    horizontal_sum = []
    total_horizontal = []

    #for loop loops through each image, calculates its horizontalness and writes to excel file
    #sum of top2tile and bottom2tile at specified index is calculated and stored in a list of sums at the same index value
    #horizontalness is then calculated from the sum at index i divided by the number of pixels at index i in horizontalness_nr_pix list
    #append_to_excel function is then called with the parameters of the cell values to be written to and the data to be
    #written to these cell values

    for i in range(0, len(cherry_cell_values)):
        horizontal_sum.append(horizontalness_toptile[i] + horizontalness_bottomtile[i])
        total_horizontal.append(horizontal_sum[i]/horizontalness_nr_pix[i])

    append_to_excel(horiz_cherry_cell_values, total_horizontal)
    total_horizontal = []

    for i in range(20, 41):
        horizontal_sum.append(horizontalness_toptile[i] + horizontalness_bottomtile[i])
        total_horizontal.append(horizontal_sum[i]/horizontalness_nr_pix[i])

    append_to_excel(horiz_flower_cell_values, total_horizontal)
    total_horizontal = []

    for i in range(40, 61):
        horizontal_sum.append(horizontalness_toptile[i] + horizontalness_bottomtile[i])
        total_horizontal.append(horizontal_sum[i]/horizontalness_nr_pix[i])

    append_to_excel(horiz_banana_cell_values, total_horizontal)
    total_horizontal = []

    for i in range(60, 81):
        horizontal_sum.append(horizontalness_toptile[i] + horizontalness_bottomtile[i])
        total_horizontal.append(horizontal_sum[i]/horizontalness_nr_pix[i])

    append_to_excel(horiz_pear_cell_values, total_horizontal)
    total_horizontal = []

    for i in range(80, 101):
        horizontal_sum.append(horizontalness_toptile[i] + horizontalness_bottomtile[i])
        total_horizontal.append(horizontal_sum[i]/horizontalness_nr_pix[i])

    append_to_excel(horiz_envelope_cell_values, total_horizontal)
    total_horizontal = []

    for i in range(100, 121):
        horizontal_sum.append(horizontalness_toptile[i] + horizontalness_bottomtile[i])
        total_horizontal.append(horizontal_sum[i]/horizontalness_nr_pix[i])

    append_to_excel(horiz_golfclub_cell_values, total_horizontal)
    total_horizontal = []

    for i in range(120, 141):
        horizontal_sum.append(horizontalness_toptile[i] + horizontalness_bottomtile[i])
        total_horizontal.append(horizontal_sum[i]/horizontalness_nr_pix[i])

    append_to_excel(horiz_pencil_cell_values, total_horizontal)
    total_horizontal = []

    for i in range(140, 160):
        horizontal_sum.append(horizontalness_toptile[i] + horizontalness_bottomtile[i])
        total_horizontal.append(horizontal_sum[i]/horizontalness_nr_pix[i])

    append_to_excel(horiz_wineglass_cell_values, total_horizontal)
    total_horizontal = []

    print('Horizontalness values successfully calculated')

#white3tile method is used to calculate the number of 3x3 tiles that are all white
#the 3x3 tile will contain just 0's and no 1's (black pixels)
#The output of this method will help in distinguishing between image types -- >
#smaller images (less black pixels) may have more 3x3 all white tiles, vice versa.
#This method will help in determining the amount of white space in the image and thus the size of the image itself.

def white3tile(path):

    #initialise variables
    global white3tile_values
    num_true_bools = 0
    allwhite_3tile = 0

    #convert csv to dataframe
    dataframe = pd.read_csv(path)

    #for loop iterates through each column and row
    #nested if statements checks if left, right, upper, lower, upper right/left & lower right/left are also black pixels
    #if nested if statement is true then a counter is incremented

    for row in range(1, dataframe.shape[0]-1):
         for col in range(1, dataframe.shape[1]-1):
            if dataframe.values[row][col] == 0:
                if dataframe.values[row][col - 1] == 0:
                     num_true_bools = num_true_bools + 1

                if dataframe.values[row][col + 1] == 0:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row-1][col] == 0:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row+1][col] == 0:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row-1][col - 1] == 0:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row-1][col +1] == 0:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row+1][col - 1] == 0:
                    num_true_bools = num_true_bools + 1

                if dataframe.values[row+1][col + 1] == 0:
                    num_true_bools = num_true_bools + 1

            #if there are exactly 8 white pixels surrounding centre white pixel then
            #allwhite_3tile variable is incremented
            if num_true_bools == 8:
                allwhite_3tile = allwhite_3tile + 1

            #reset variable for next iteration
            num_true_bools = 0

    #resultant allwhite_3tile value is appended to the white3tile_values list
    white3tile_values.append(allwhite_3tile)


#white3tile_all function is used to call the white3tile function to calculate
#white3tile values for each image

def white3tile_all():

        #set variables to global so they can be used locally
        global white3tile_values
        global white3tilecell_values

        #for loops to calculate white pixels with exactly 8 neighbouring white pixels for each image
        #append_to_excel function is called with the parameters of - values calculated from white3tile function
        #and the cell values at which these white3tile values are to be written to
        #list to store white3tile values is set to 0 after every image type has been iterated through

        for i in range(0, len(cherry_path)):
            white3tile(cherry_path[i])

        append_to_excel(white3tile_cherry_cell_values, white3tile_values)
        white3tile_values = []

        for i in range(0, len(cherry_path)):
            white3tile(flower_path[i])

        append_to_excel(white3tile_flower_cell_values, white3tile_values)
        white3tile_values = []

        for i in range(0, len(cherry_path)):
            white3tile(banana_path[i])

        append_to_excel(white3tile_banana_cell_values, white3tile_values)
        white3tile_values = []

        for i in range(0, len(cherry_path)):
            white3tile(pear_path[i])

        append_to_excel(white3tile_pear_cell_values, white3tile_values)
        white3tile_values = []

        for i in range(0, len(cherry_path)):
            white3tile(envelope_path[i])

        append_to_excel(white3tile_envelope_cell_values, white3tile_values)
        white3tile_values = []

        for i in range(0, len(cherry_path)):
            white3tile(golfclub_path[i])

        append_to_excel(white3tile_golfclub_cell_values, white3tile_values)
        white3tile_values = []

        for i in range(0, len(cherry_path)):
            white3tile(pencil_path[i])

        append_to_excel(white3tile_pencil_cell_values, white3tile_values)
        white3tile_values = []

        for i in range(0, len(cherry_path)):
            white3tile(wineglass_path[i])

        append_to_excel(white3tile_wineglass_cell_values, white3tile_values)
        white3tile_values = []

        print('Total 3x3 all white tiles successfully calculated')

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
        for i in range(0, len(cherry_cell_values)):
            sheet[column_list[i]].value = values[i]

        #save excel file with updated cell values
        wb.save(features_path + "/40175607_features.xlsx")

#call all functions
left2tile_all()
right2tile_all()
top2tile_all()
bottom2tile_all()
nr_pix_all()
verticalness()
horizontalness()
white3tile_all()
