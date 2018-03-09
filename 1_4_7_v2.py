

def frame_all_images(directory=None, color=(0,0,0),frame_width=(0.05)):
    """ Saves a modfied version of each image in directory.

    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """

    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified

    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'framed_images')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed

    #load all the images
    image_list, file_list = get_images(directory)

    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = file_list[n].split('.')

        # Round the corners with radius = 30% of short side
        new_image = frame(image_list[n],color, frame_width)

        # Add watermark picture to new_image
        logo = PIL.Image.open('WolfHead.png')
        position = ((new_image.width - logo.width), (new_image.height - logo.height))
        new_image.paste(logo, position)

        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename) 
# Add watermark picture to new_image
        logo = PIL.Image.open('WolfHead.png')
        position = ((new_image.width - logo.width), (new_image.height - logo.height))
        new_image.paste(logo, position) 

#def add_logo(directory=None):

    #image = PIL.Image.open('solar_flare.jpg')
    #logo = PIL.Image.open('image_120.png')
    #image_copy = image.copy()
    #position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
    #image_copy.paste(logo, position)
    #image_copy.save('pasted_image.jpg')
