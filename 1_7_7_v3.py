import PIL
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFont
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
    
    drawing_layer.rectangle((0,0,width,thickness), fill=(255,235,228,255))
    drawing_layer.rectangle((0,0,thickness, height), fill=(255,235,228,255))
    drawing_layer.rectangle((0,height,width,height - thickness), fill=(255,235,228,255))
    drawing_layer.rectangle((width,height,width - thickness,0), fill=(255,235,228,255))
    
    # Make the new image, starting with all transparent
    result = original_image.copy()
    result.paste(frame_mask, (0,0), mask=frame_mask)
    return result
 
image = Image.open('WolfHead4.png')
draw = ImageDraw.Draw(image)
txt = "Wolf Cola"
fontsize = 20 # starting font size

# portion of image width you want text width to be
img_fraction = 0.10

font = ImageFont.truetype("arial.ttf", fontsize)
while font.getsize(txt)[0] < img_fraction*image.size[0]:
    # iterate until the text size is just larger than the criteria
    fontsize += 1
    font = ImageFont.truetype("arial.ttf", fontsize)

# optionally de-increment to be sure it is less than criteria
fontsize -= 1
font = ImageFont.truetype("arial.ttf", fontsize)

print 'final font size',fontsize
draw.text((100,200), txt, font=font) # put the text on the image
image.save('WolfHead4.png') # save it

       
# Opening the file gg.png
imageFile = "WolfHead4.png"
im1=Image.open(imageFile)
 
# Drawing the text on the picture
draw = ImageDraw.Draw(im1)
draw.text((600, 70),"Wolf Cola",(254,75,67))
draw = ImageDraw.Draw(im1)
plt.savefig('WolfHead4.png')
# Save the image with a new name
im1.save("WolfHead4.png")