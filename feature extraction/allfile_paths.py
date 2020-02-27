#File to store all file paths for all 20 images for the 8 image types

import os #os module - used to create the relative file paths


#using os module, set current execution path to current working dir
#get parent directory - '/assignment2_40175607'
#set main_path to parent_directory + 'section1_images'

current_working_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_working_dir)
parent_dir = os.path.abspath(os.path.join(current_working_dir, os.pardir))
main_path =  parent_dir + '/section1_images'

#main_path  = os.path.join(os.path.realpath(".."), '/section1_images')

#list of paths for cherry images
cherry_path = [main_path + "/40175607_cherry_01.csv",
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

#list of paths for flower images
flower_path = [main_path + '/40175607_flower_01.csv',
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

#list of paths for banana images
banana_path = [main_path + '/40175607_banana_01.csv',
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

#list of paths for pear images
pear_path = [main_path + '/40175607_pear_01.csv',
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


#list of paths for envelope images
envelope_path = [main_path + '/40175607_envelope_01.csv',
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


#list of paths for golfclub images
golfclub_path = [main_path + '/40175607_golfclub_01.csv',
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

#list of paths for pencil images
pencil_path = [main_path + '/40175607_pencil_01.csv',
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


#list of paths for wineglass images
wineglass_path = [main_path + '/40175607_wineglass_01.csv',
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

print('All file paths successfully added')
