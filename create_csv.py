#create_csv file used to convert all the 160 pgm files into csv files to be used in section 2 and 3

import numpy as np #numpy module - used to create the 2 dimensional array object
import pandas as pd #pandas module - used to create dataframe from numpy array
import os #os module - used to create the relative file paths

#using os module, set current execution path to current working dir
#get parent directory - '/assignment2_40175607'
#set main_path to parent_directory + 'section1_images'

current_working_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_working_dir)
parent_dir = os.path.abspath(os.path.join(current_working_dir, os.pardir))
main_path =  parent_dir + '/section1_images'


#main_path  = os.path.join(os.path.realpath("../"), 'Documents/assignment2_40175607/section1_images')

#To execute files in Terminal, right click on section1_code folder and open new Terminal window
#this sets the correct directory for execution

#list of source paths for cherry images
cherry_path = [main_path + "/Images/Cherry/cherry_01.pgm",
            main_path + "/Images/Cherry/cherry_02.pgm",
            main_path + "/Images/Cherry/cherry_03.pgm",
            main_path + "/Images/Cherry/cherry_04.pgm",
            main_path + "/Images/Cherry/cherry_05.pgm",
            main_path + "/Images/Cherry/cherry_06.pgm",
            main_path + "/Images/Cherry/cherry_07.pgm",
            main_path + "/Images/Cherry/cherry_08.pgm",
            main_path + "/Images/Cherry/cherry_09.pgm",
            main_path + "/Images/Cherry/cherry_10.pgm",
            main_path + "/Images/Cherry/cherry_11.pgm",
            main_path + "/Images/Cherry/cherry_12.pgm",
            main_path + "/Images/Cherry/cherry_13.pgm",
            main_path + "/Images/Cherry/cherry_14.pgm",
            main_path + "/Images/Cherry/cherry_15.pgm",
            main_path + "/Images/Cherry/cherry_16.pgm",
            main_path + "/Images/Cherry/cherry_17.pgm",
            main_path + "/Images/Cherry/cherry_18.pgm",
            main_path + "/Images/Cherry/cherry_19.pgm",
            main_path + "/Images/Cherry/cherry_20.pgm"]

#list of destination paths for cherry images
destination_cherry_path = [main_path + "/40175607_cherry_01.csv",
                         main_path + "/40175607_cherry_02.csv",
                         main_path + "/40175607_cherry_03.csv",
                         main_path + "/40175607_cherry_04.csv",
                         main_path + "/40175607_cherry_05.csv",
                         main_path + "/40175607_cherry_06.csv",
                         main_path + "/40175607_cherry_07.csv",
                         main_path + "/40175607_cherry_08.csv",
                         main_path + "/40175607_cherry_09.csv",
                         main_path + "/40175607_cherry_10.csv",
                         main_path + "/40175607_cherry_11.csv",
                         main_path + "/40175607_cherry_12.csv",
                         main_path + "/40175607_cherry_13.csv",
                         main_path + "/40175607_cherry_14.csv",
                         main_path + "/40175607_cherry_15.csv",
                         main_path + "/40175607_cherry_16.csv",
                         main_path + "/40175607_cherry_17.csv",
                         main_path + "/40175607_cherry_18.csv",
                         main_path + "/40175607_cherry_19.csv",
                         main_path + "/40175607_cherry_20.csv"]


#list of source paths for flower images
flower_path = [main_path+'/Images/Flower/flower_01.pgm',
                    main_path + '/Images/Flower/flower_02.pgm',
                    main_path + '/Images/Flower/flower_03.pgm',
                    main_path + '/Images/Flower/flower_04.pgm',
                    main_path + '/Images/Flower/flower_05.pgm',
                    main_path + '/Images/Flower/flower_06.pgm',
                    main_path + '/Images/Flower/flower_07.pgm',
                    main_path + '/Images/Flower/flower_08.pgm',
                    main_path + '/Images/Flower/flower_09.pgm',
                    main_path + '/Images/Flower/flower_10.pgm',
                    main_path + '/Images/Flower/flower_11.pgm',
                    main_path + '/Images/Flower/flower_12.pgm',
                    main_path + '/Images/Flower/flower_13.pgm',
                    main_path + '/Images/Flower/flower_14.pgm',
                    main_path + '/Images/Flower/flower_15.pgm',
                    main_path + '/Images/Flower/flower_16.pgm',
                    main_path + '/Images/Flower/flower_17.pgm',
                    main_path + '/Images/Flower/flower_18.pgm',
                    main_path + '/Images/Flower/flower_19.pgm',
                    main_path + '/Images/Flower/flower_20.pgm']

#list of destination paths for flower images
destination_flower_path = [main_path + '/40175607_flower_01.csv',
                    main_path + '/40175607_flower_02.csv',
                    main_path + '/40175607_flower_03.csv',
                    main_path + '/40175607_flower_04.csv',
                    main_path + '/40175607_flower_05.csv',
                    main_path + '/40175607_flower_06.csv',
                    main_path + '/40175607_flower_07.csv',
                    main_path + '/40175607_flower_08.csv',
                    main_path + '/40175607_flower_09.csv',
                    main_path + '/40175607_flower_10.csv',
                    main_path + '/40175607_flower_11.csv',
                    main_path + '/40175607_flower_12.csv',
                    main_path + '/40175607_flower_13.csv',
                    main_path + '/40175607_flower_14.csv',
                    main_path + '/40175607_flower_15.csv',
                    main_path + '/40175607_flower_16.csv',
                    main_path + '/40175607_flower_17.csv',
                    main_path + '/40175607_flower_18.csv',
                    main_path + '/40175607_flower_19.csv',
                    main_path + '/40175607_flower_20.csv']


#list of source paths for banana images
banana_path = [main_path + '/Images/Banana/banana_01.pgm',
                    main_path + '/Images/Banana/banana_02.pgm',
                    main_path + '/Images/Banana/banana_03.pgm',
                    main_path + '/Images/Banana/banana_04.pgm',
                    main_path + '/Images/Banana/banana_05.pgm',
                    main_path + '/Images/Banana/banana_06.pgm',
                    main_path + '/Images/Banana/banana_07.pgm',
                    main_path + '/Images/Banana/banana_08.pgm',
                    main_path + '/Images/Banana/banana_09.pgm',
                    main_path + '/Images/Banana/banana_10.pgm',
                    main_path + '/Images/Banana/banana_11.pgm',
                    main_path + '/Images/Banana/banana_12.pgm',
                    main_path + '/Images/Banana/banana_13.pgm',
                    main_path + '/Images/Banana/banana_14.pgm',
                    main_path + '/Images/Banana/banana_15.pgm',
                    main_path + '/Images/Banana/banana_16.pgm',
                    main_path + '/Images/Banana/banana_17.pgm',
                    main_path + '/Images/Banana/banana_18.pgm',
                    main_path + '/Images/Banana/banana_19.pgm',
                    main_path + '/Images/Banana/banana_20.pgm']

#list of destination paths for banana images
destination_banana_path = [main_path + '/40175607_banana_01.csv',
                    main_path + '/40175607_banana_02.csv',
                    main_path + '/40175607_banana_03.csv',
                    main_path + '/40175607_banana_04.csv',
                    main_path + '/40175607_banana_05.csv',
                    main_path + '/40175607_banana_06.csv',
                    main_path + '/40175607_banana_07.csv',
                    main_path + '/40175607_banana_08.csv',
                    main_path + '/40175607_banana_09.csv',
                    main_path + '/40175607_banana_10.csv',
                    main_path + '/40175607_banana_11.csv',
                    main_path + '/40175607_banana_12.csv',
                    main_path + '/40175607_banana_13.csv',
                    main_path + '/40175607_banana_14.csv',
                    main_path + '/40175607_banana_15.csv',
                    main_path + '/40175607_banana_16.csv',
                    main_path + '/40175607_banana_17.csv',
                    main_path + '/40175607_banana_18.csv',
                    main_path + '/40175607_banana_19.csv',
                    main_path + '/40175607_banana_20.csv']


#list of source paths for pear images
pear_path = [main_path + '/Images/Pear/pear_01.pgm',
                    main_path + '/Images/Pear/pear_02.pgm',
                    main_path + '/Images/Pear/pear_03.pgm',
                    main_path + '/Images/Pear/pear_04.pgm',
                    main_path + '/Images/Pear/pear_05.pgm',
                    main_path + '/Images/Pear/pear_06.pgm',
                    main_path + '/Images/Pear/pear_07.pgm',
                    main_path + '/Images/Pear/pear_08.pgm',
                    main_path + '/Images/Pear/pear_09.pgm',
                    main_path + '/Images/Pear/pear_10.pgm',
                    main_path + '/Images/Pear/pear_11.pgm',
                    main_path + '/Images/Pear/pear_12.pgm',
                    main_path + '/Images/Pear/pear_13.pgm',
                    main_path + '/Images/Pear/pear_14.pgm',
                    main_path + '/Images/Pear/pear_15.pgm',
                    main_path + '/Images/Pear/pear_16.pgm',
                    main_path + '/Images/Pear/pear_17.pgm',
                    main_path + '/Images/Pear/pear_18.pgm',
                    main_path + '/Images/Pear/pear_19.pgm',
                    main_path + '/Images/Pear/pear_20.pgm']


#list of destination paths for pear images
destination_pear_path = [main_path + '/40175607_pear_01.csv',
                    main_path + '/40175607_pear_02.csv',
                    main_path + '/40175607_pear_03.csv',
                    main_path + '/40175607_pear_04.csv',
                    main_path + '/40175607_pear_05.csv',
                    main_path + '/40175607_pear_06.csv',
                    main_path + '/40175607_pear_07.csv',
                    main_path + '/40175607_pear_08.csv',
                    main_path + '/40175607_pear_09.csv',
                    main_path + '/40175607_pear_10.csv',
                    main_path + '/40175607_pear_11.csv',
                    main_path + '/40175607_pear_12.csv',
                    main_path + '/40175607_pear_13.csv',
                    main_path + '/40175607_pear_14.csv',
                    main_path + '/40175607_pear_15.csv',
                    main_path + '/40175607_pear_16.csv',
                    main_path + '/40175607_pear_17.csv',
                    main_path + '/40175607_pear_18.csv',
                    main_path + '/40175607_pear_19.csv',
                    main_path + '/40175607_pear_20.csv']


#list of source paths for envelope images
envelope_path = [main_path + '/Images/Envelope/envelope_01.pgm',
                    main_path + '/Images/Envelope/envelope_02.pgm',
                    main_path + '/Images/Envelope/envelope_03.pgm',
                    main_path + '/Images/Envelope/envelope_04.pgm',
                    main_path + '/Images/Envelope/envelope_05.pgm',
                    main_path + '/Images/Envelope/envelope_06.pgm',
                    main_path + '/Images/Envelope/envelope_07.pgm',
                    main_path + '/Images/Envelope/envelope_08.pgm',
                    main_path + '/Images/Envelope/envelope_09.pgm',
                    main_path + '/Images/Envelope/envelope_10.pgm',
                    main_path + '/Images/Envelope/envelope_11.pgm',
                    main_path + '/Images/Envelope/envelope_12.pgm',
                    main_path + '/Images/Envelope/envelope_13.pgm',
                    main_path + '/Images/Envelope/envelope_14.pgm',
                    main_path + '/Images/Envelope/envelope_15.pgm',
                    main_path + '/Images/Envelope/envelope_16.pgm',
                    main_path + '/Images/Envelope/envelope_17.pgm',
                    main_path + '/Images/Envelope/envelope_18.pgm',
                    main_path + '/Images/Envelope/envelope_19.pgm',
                    main_path + '/Images/Envelope/envelope_20.pgm']

#list of destination paths for envelope images
destination_envelope_path = [main_path + '/40175607_envelope_01.csv',
                    main_path + '/40175607_envelope_02.csv',
                    main_path + '/40175607_envelope_03.csv',
                    main_path + '/40175607_envelope_04.csv',
                    main_path + '/40175607_envelope_05.csv',
                    main_path + '/40175607_envelope_06.csv',
                    main_path + '/40175607_envelope_07.csv',
                    main_path + '/40175607_envelope_08.csv',
                    main_path + '/40175607_envelope_09.csv',
                    main_path + '/40175607_envelope_10.csv',
                    main_path + '/40175607_envelope_11.csv',
                    main_path + '/40175607_envelope_12.csv',
                    main_path + '/40175607_envelope_13.csv',
                    main_path + '/40175607_envelope_14.csv',
                    main_path + '/40175607_envelope_15.csv',
                    main_path + '/40175607_envelope_16.csv',
                    main_path + '/40175607_envelope_17.csv',
                    main_path + '/40175607_envelope_18.csv',
                    main_path + '/40175607_envelope_19.csv',
                    main_path + '/40175607_envelope_20.csv']


#list of source paths for golfclub images
golfclub_path = [main_path + '/Images/Golfclub/golfclub_01.pgm',
                    main_path + '/Images/Golfclub/golfclub_02.pgm',
                    main_path + '/Images/Golfclub/golfclub_03.pgm',
                    main_path + '/Images/Golfclub/golfclub_04.pgm',
                    main_path + '/Images/Golfclub/golfclub_05.pgm',
                    main_path + '/Images/Golfclub/golfclub_06.pgm',
                    main_path + '/Images/Golfclub/golfclub_07.pgm',
                    main_path + '/Images/Golfclub/golfclub_08.pgm',
                    main_path + '/Images/Golfclub/golfclub_09.pgm',
                    main_path + '/Images/Golfclub/golfclub_10.pgm',
                    main_path + '/Images/Golfclub/golfclub_11.pgm',
                    main_path + '/Images/Golfclub/golfclub_12.pgm',
                    main_path + '/Images/Golfclub/golfclub_13.pgm',
                    main_path + '/Images/Golfclub/golfclub_14.pgm',
                    main_path + '/Images/Golfclub/golfclub_15.pgm',
                    main_path + '/Images/Golfclub/golfclub_16.pgm',
                    main_path + '/Images/Golfclub/golfclub_17.pgm',
                    main_path + '/Images/Golfclub/golfclub_18.pgm',
                    main_path + '/Images/Golfclub/golfclub_19.pgm',
                    main_path + '/Images/Golfclub/golfclub_20.pgm']


#list of destination paths for golfclub images
destination_golfclub_path = [main_path + '/40175607_golfclub_01.csv',
                    main_path + '/40175607_golfclub_02.csv',
                    main_path + '/40175607_golfclub_03.csv',
                    main_path + '/40175607_golfclub_04.csv',
                    main_path + '/40175607_golfclub_05.csv',
                    main_path + '/40175607_golfclub_06.csv',
                    main_path + '/40175607_golfclub_07.csv',
                    main_path + '/40175607_golfclub_08.csv',
                    main_path + '/40175607_golfclub_09.csv',
                    main_path + '/40175607_golfclub_10.csv',
                    main_path + '/40175607_golfclub_11.csv',
                    main_path + '/40175607_golfclub_12.csv',
                    main_path + '/40175607_golfclub_13.csv',
                    main_path + '/40175607_golfclub_14.csv',
                    main_path + '/40175607_golfclub_15.csv',
                    main_path + '/40175607_golfclub_16.csv',
                    main_path + '/40175607_golfclub_17.csv',
                    main_path + '/40175607_golfclub_18.csv',
                    main_path + '/40175607_golfclub_19.csv',
                    main_path + '/40175607_golfclub_20.csv']


#list of source paths for pencil images
pencil_path = [main_path + '/Images/Pencil/pencil_01.pgm',
                    main_path + '/Images/Pencil/pencil_02.pgm',
                    main_path + '/Images/Pencil/pencil_03.pgm',
                    main_path + '/Images/Pencil/pencil_04.pgm',
                    main_path + '/Images/Pencil/pencil_05.pgm',
                    main_path + '/Images/Pencil/pencil_06.pgm',
                    main_path + '/Images/Pencil/pencil_07.pgm',
                    main_path + '/Images/Pencil/pencil_08.pgm',
                    main_path + '/Images/Pencil/pencil_09.pgm',
                    main_path + '/Images/Pencil/pencil_10.pgm',
                    main_path + '/Images/Pencil/pencil_11.pgm',
                    main_path + '/Images/Pencil/pencil_12.pgm',
                    main_path + '/Images/Pencil/pencil_13.pgm',
                    main_path + '/Images/Pencil/pencil_14.pgm',
                    main_path + '/Images/Pencil/pencil_15.pgm',
                    main_path + '/Images/Pencil/pencil_16.pgm',
                    main_path + '/Images/Pencil/pencil_17.pgm',
                    main_path + '/Images/Pencil/pencil_18.pgm',
                    main_path + '/Images/Pencil/pencil_19.pgm',
                    main_path + '/Images/Pencil/pencil_20.pgm']


#list of destination paths for pencil images
destination_pencil_path = [main_path + '/40175607_pencil_01.csv',
                    main_path + '/40175607_pencil_02.csv',
                    main_path + '/40175607_pencil_03.csv',
                    main_path + '/40175607_pencil_04.csv',
                    main_path + '/40175607_pencil_05.csv',
                    main_path + '/40175607_pencil_06.csv',
                    main_path + '/40175607_pencil_07.csv',
                    main_path + '/40175607_pencil_08.csv',
                    main_path + '/40175607_pencil_09.csv',
                    main_path + '/40175607_pencil_10.csv',
                    main_path + '/40175607_pencil_11.csv',
                    main_path + '/40175607_pencil_12.csv',
                    main_path + '/40175607_pencil_13.csv',
                    main_path + '/40175607_pencil_14.csv',
                    main_path + '/40175607_pencil_15.csv',
                    main_path + '/40175607_pencil_16.csv',
                    main_path + '/40175607_pencil_17.csv',
                    main_path + '/40175607_pencil_18.csv',
                    main_path + '/40175607_pencil_19.csv',
                    main_path + '/40175607_pencil_20.csv']


#list of source paths for wineglass images
wineglass_path = [main_path + '/Images/Wineglass/wineglass_01.pgm',
                    main_path + '/Images/Wineglass/wineglass_02.pgm',
                    main_path + '/Images/Wineglass/wineglass_03.pgm',
                    main_path + '/Images/Wineglass/wineglass_04.pgm',
                    main_path + '/Images/Wineglass/wineglass_05.pgm',
                    main_path + '/Images/Wineglass/wineglass_06.pgm',
                    main_path + '/Images/Wineglass/wineglass_07.pgm',
                    main_path + '/Images/Wineglass/wineglass_08.pgm',
                    main_path + '/Images/Wineglass/wineglass_09.pgm',
                    main_path + '/Images/Wineglass/wineglass_10.pgm',
                    main_path + '/Images/Wineglass/wineglass_11.pgm',
                    main_path + '/Images/Wineglass/wineglass_12.pgm',
                    main_path + '/Images/Wineglass/wineglass_13.pgm',
                    main_path + '/Images/Wineglass/wineglass_14.pgm',
                    main_path + '/Images/Wineglass/wineglass_15.pgm',
                    main_path + '/Images/Wineglass/wineglass_16.pgm',
                    main_path + '/Images/Wineglass/wineglass_17.pgm',
                    main_path + '/Images/Wineglass/wineglass_18.pgm',
                    main_path + '/Images/Wineglass/wineglass_19.pgm',
                    main_path + '/Images/Wineglass/wineglass_20.pgm']


#list of destination paths for wineglass images
destination_wineglass_path = [main_path + '/40175607_wineglass_01.csv',
                    main_path + '/40175607_wineglass_02.csv',
                    main_path + '/40175607_wineglass_03.csv',
                    main_path + '/40175607_wineglass_04.csv',
                    main_path + '/40175607_wineglass_05.csv',
                    main_path + '/40175607_wineglass_06.csv',
                    main_path + '/40175607_wineglass_07.csv',
                    main_path + '/40175607_wineglass_08.csv',
                    main_path + '/40175607_wineglass_09.csv',
                    main_path + '/40175607_wineglass_10.csv',
                    main_path + '/40175607_wineglass_11.csv',
                    main_path + '/40175607_wineglass_12.csv',
                    main_path + '/40175607_wineglass_13.csv',
                    main_path + '/40175607_wineglass_14.csv',
                    main_path + '/40175607_wineglass_15.csv',
                    main_path + '/40175607_wineglass_16.csv',
                    main_path + '/40175607_wineglass_17.csv',
                    main_path + '/40175607_wineglass_18.csv',
                    main_path + '/40175607_wineglass_19.csv',
                    main_path + '/40175607_wineglass_20.csv']

#create_csv function used to convert all of the pgm files into csv

def create_csv(path, destination_path):

    #open pgm files
    with open(path, 'r') as f:
        data = f.read().split('\n')

    #removes the leading meta data
    numpy_data = np.asarray(data[5:])

    #this method verifies the size of the array = 2500
    def verification():
        assert (len(numpy_data) == 2500), "Size of object is not correct"  #validate the size of the array object

    #create dataframe from numpy array
    dataframe = pd.DataFrame(numpy_data.reshape(50,50))

    #loop through dataframe creating the 1's and 0's
    for i in dataframe:
        for j in dataframe:
            if dataframe[i][j] == '255':
                dataframe[i][j] = '0'
            else:
                dataframe[i][j] = '1'

    verification()

    #export image to csv format
    print('CSV Created')

    #**remove # in below line to export the csv's to the destination path**#

    #csv_image_export = dataframe.to_csv(destination_path, index = False , header = False)


#create_all_csv function used to loop through each set of images and export them as a csv

def create_all_csv():


        #for loops loop through each image type and calls the create_csv method to convert images to csv
        for i in range(0, len(cherry_path)):
            create_csv(cherry_path[i], destination_cherry_path[i])

        for i in range(0, len(flower_path)):
           create_csv(flower_path[i], destination_flower_path[i])

        for i in range(0, len(banana_path)):
            create_csv(banana_path[i], destination_banana_path[i])

        for i in range(0, len(pear_path)):
            create_csv(pear_path[i], destination_pear_path[i])

        for i in range(0, len(envelope_path)):
            create_csv(envelope_path[i], destination_envelope_path[i])

        for i in range(0, len(golfclub_path)):
            create_csv(golfclub_path[i], destination_golfclub_path[i])

        for i in range(0, len(pencil_path)):
            create_csv(pencil_path[i], destination_pencil_path[i])

        for i in range(0, len(wineglass_path)):
            create_csv(wineglass_path[i], destination_wineglass_path[i])

        print('All CSVs created successfully')

#call main csv function 
create_all_csv()
