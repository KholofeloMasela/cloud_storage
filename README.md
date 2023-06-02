## This is a cloud storage application, where you can upload your local images to your dropbox app folder


#Prerequisites

Before running this app, make sure you have the following prerequisites:

Python 3.6 or higher installed on your system.

The dropbox Python library installed. You can install it using pip:

`pip install dropbox`

A Dropbox account. If you don't have one, you can create one at https://www.dropbox.com/.

A Dropbox API app. You need to create a new app in your Dropbox developer console to obtain the API credentials (app key and app secret) required for authentication. You can create an app at https://www.dropbox.com/developers/apps.

#Setup

Download the source code files.

Open the cloud_storage.py file:
Update line 3 with your app token:  `Token = 'Your app token'`
Update line 40 with the file of your choosing in your app: `file_to = "folder_img"` so that you use the file in your app

And save the file

#Run the app:

`cloud_storage.py`

#Usage
Follow the instructions printed in the console to upload files.

To exit the app type "n" when the app asks you this:
 `would you like to upload files to dropbox ? Enter y or n:`








