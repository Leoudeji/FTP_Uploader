# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 02:27:46 2023

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


# Enter File Name with Extension
filename = "" #Enter file name to be uploaded here with the file extension ie. ".mp4"
 
# Read file in binary mode
with open(filename, "wb") as file:
    # Command for Uploading the file "STOR filename"
    ftp_server.retrbinary(f"RETR {filename}", file.write)
    
    
# Get list of files
ftp_server.dir()


#Display the content of downloaded file
file= open(filename, "r")
print('File Content:', file.read())


# Close the Connection
ftp_server.quit()
