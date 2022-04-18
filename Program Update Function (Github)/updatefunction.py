# -----------------------------------------------
# Author: Nick V.
# Function to check version and if there is an
# update it asks to make an update
# Version: 1.0
# creation date: 15.04.2022
# -----------------------------------------------
# Just create a new Folder in a GitHub rep and
# upload there a version.txt. You can put in there
# float digits like "1.0","1.6","3.7","7.2","2.7"
# from this File the Func will get Information about
# Updates. The other link should be the raw url to
# your .exe
#-------------------------------------------------


# Downloading from GitHub
import webbrowser
# Access and get data from HTTP requests
import requests

# Put in here the Name of your Program
AppName = ''
# Put in here the current Version
version = ''



# Update Function
def check_updates():
    try:
        # Get Data from the version file we uploaded to a git Folder
        # Replace the url for your version.txt online with the one below.
        
        # Inspecting the results of the request
        response = requests.get('http://raw.githubusercontent.com/00111001/update/main/TestUpdate/version.txt?token=GHSAT0AAAAAABTNUDKKA2MVQY6EKGRX2NCEYSXQOTA')
        # Convert Data from raw bytes to str
        data = response.text
        
        # Comparing the versions from version.txt and the version in the file
        if float(data) > float(version):
            # Telling user some Information's
            print('Update!', f'{AppName} {version} needs to update to version {data}')
            # Asking user to update
            choice = input("Do you wanna update to a new Version?")
            # If User wants to update
            if choice == "Y":
            
                # Download the Program we uploaded to a git Folder
                # Replace the url for your file online with the one below.
                # HAS TO BE A ?raw=True LINK
                webbrowser.open_new_tab('https://github.com/00111001/update/blob/main/TestUpdate/test.exe?raw=True')
            # If user do not want the update - nothing
            else:
                pass
        # If no Update is available
        else:
            print('No Updates are Available.')
            
    # Exception Handling
    except Exception as e:
        print('Unable to Check for Update, Error:' + str(e))

# Here's the place for your Program
def main():
     #Write here your code or whatever



if __name__ == '__main__':
    # Calling Update Function
    check_updates()
    # After updating calling main function
    main()



