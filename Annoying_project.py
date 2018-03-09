import PIL
import matplotlib.pyplot as plt 
import os.path
import numpy as np
from PIL import Image
from PIL import ImageDraw
def frame(original_image, color, frame_width):
    """ Put a frame around a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with a frame, where
    0 < frame_width < 1
    is the border as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    thickness = int(frame_width * min(width, height)) # thickness in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    r, g, b = color
    frame_mask = PIL.Image.new('RGBA', (width, height), (0,0,0,0))
    drawing_layer = PIL.ImageDraw.Draw(frame_mask)
    
    drawing_layer.rectangle((0,0,width,thickness), fill=(r,g,b,255))
    drawing_layer.rectangle((0,0,thickness, height), fill=(r,g,b,255))
    drawing_layer.rectangle((0,height,width,height - thickness), fill=(r,g,b,255))
    drawing_layer.rectangle((width,height,width - thickness,0), fill=(r,g,b,255))
    
    # Make the new image, starting with all transparent
    result = original_image.copy()
    result.paste(frame_mask, (0,0), mask=frame_mask)
    return result
    
    '''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'Wolfhead')
# Read the image data into an array
img = plt.imread(filename)
    
    ###
# Make a rectangle of pixels yellow
###

height = len(img)
width = len(img[0])
for row in range(200, 220):
    for column in range(50, 100):
        img[row][column] = [255, 255, 0] # red + green = yellow
    
# Opening the file gg.png
imageFile = "WolfHead.png"
im1=Image.open(imageFile)
 
# Drawing the text on the picture
draw = ImageDraw.Draw(im1)
draw.text((0, 0),"Wolf Cola",(254,75,67))
draw = ImageDraw.Draw(im1)
plt.savefig('WolfHead.png')
# Save the image with a new name
im1.save("WolfHead.png")