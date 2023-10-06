# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 02:06:38 2023

@author: ludej
"""
#Import required module
import ftplib

#Fill Required Information

HOSTNAME = "" #Enter remote FTP Server IP here
USERNAME = "" #Enter the username of the remote FTP Server here
PASSWORD = "" #Enter the password of the remote FTP server here

#Note: Hostinger uses Port 21

# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
 
# force UTF-8 encoding
ftp_server.encoding = "utf-8"


#Upload the File (To upload a file, we will use storbinary() method)


# Enter File Name with Extension
filename = "" #Enter file name to be downloaded here with the file extension ie. ".mp4"
 
# Read file in binary mode
with open(filename, "rb") as file:
    # Command for Uploading the file "STOR filename"
    ftp_server.storbinary(f"STOR {filename}", file)
    
    

# Get list of files
ftp_server.dir()
