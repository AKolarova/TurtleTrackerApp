#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Andrea Kolarova (andrea.kolarova@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#Create a variable poiting to the data file
file_name = 'data/raw/Sara.txt'

#Create a file object from the file name
file_object = open(file=file_name, mode='r')


#Read contents of file into a list
line_list = file_object.readlines()


#Print information to the user
#print(f'Record {record_id} indicates Sara was seen at {obs_lat}N.{obs_lon}W on {obs_date}.')

