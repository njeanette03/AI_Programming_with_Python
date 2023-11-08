#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Jeanette Nguyen
# DATE CREATED:    11/4/23                              
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    # Create list of files in directory
    filename_list = listdir(image_dir)
    
    # Creates a dictionary of pet labels (results_dic) based upon the filenames 
    results_dic = dict()
    
    ## Determines number of items in dictionary
    items_in_dic = len(results_dic)
    print("\nEmpty Dictionary results_dic - n items=", items_in_dic)
    
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(filename_list), 1):
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it isn't an pet image file
        if filename_list[idx][0] != ".":
            # splits lower case string by _ to break into words 
            word_list_pet_label = filename_list[idx].split("_")
            # Creates temporary label variable to hold pet label name extracte
            pet_name = ""          
            
            # loop to check if word in pet name is only alphabetic characters - if true append word to pet_name separated by trailing spacefor word in word_list_pet_label:
            for word in word_list_pet_label:
                # set to lowercase and add whitespace between words
                if word.isalpha():
                    pet_name += word.lower() + " "
                               # if filename_list doesn't exist, add it and label
                if filename_list[idx] not in results_dic:
                    results_dic[filename_list[idx]] = [pet_name] 
                   
                # duplicate exist warning message
                else:  
                    print("Warning:  duplicate files exist in directory:", filename_list[idx])
                   
               
            # strip off starting/trailing whitespace characters
            pet_name = pet_name.rstrip()
           
        # iterate through dictionary and print keys and values
        print("\nAll key-value pairs in dictionary results_dic are as follow:\n")
        for key in results_dic:
            print("Filename = ", key, "    Pet Label = ", results_dic[key][0])
  
    return results_dic
