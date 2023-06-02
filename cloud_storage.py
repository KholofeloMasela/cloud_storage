import dropbox

token = 'Your app token'


def uploadFile( file_from, file_to):
    f = open(file_from, 'rb')
    f = f.read()
    dbx = dropbox.Dropbox(token)
    if (file_from != '' and file_to !=''):
        dbx.files_upload(f, file_to)
        print("Your files have been uploaded succesfully")
    else:
        print("There was a problem locating the targeted folder")


def main():
    
    print("Welcome to Image storage!")
    print("")

    print("")
    while True:
        yes_no = input("Would you like to upload files to dropbox ? Enter y or n: ").lower()
        print("")
        if(yes_no == 'y'):
            
            file_from = input("Please enter the image or file you want to upload from the list below:\n ").lower()
           
            file_to = "folder_img"
            file_to = '/'+file_to+'/'+file_from
            print("")
            
            uploadFile(file_from,file_to)

            
        elif(yes_no == 'n'):
            print("Thanks for using our app")
            break
        else: 
            print("Answer in y or n")    
        print("") 

      
main()               