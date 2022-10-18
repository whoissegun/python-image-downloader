import urllib.request

def dl_jpg(url,file_path,file_name):
    # functions requires the url of the image the user wants to download
    # function requires the path the user wants to save the image in 
    # function requires the name the user wants to save the picture as
    # function will save the image as a jpg file
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url,full_path)


url = input("Enter image URL to download: ")
file_name = input("Enter file name to save as: ")

# I creater a folder called images in the same directory as the file. The images folder is the default place the image will be saved. 
# However it can still be changed 
dl_jpg(url,'images/',file_name)

