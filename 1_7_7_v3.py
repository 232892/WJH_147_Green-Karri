import PIL
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.patches as patches
import numpy as np

im = np.array(Image.open('WolfHead.png'), dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)

# Create a Rectangle patch
rect = patches.Rectangle((71,378),356,75,linewidth=1,edgecolor='r',facecolor='red')

# Add the patch to the Axes
ax.add_patch(rect)

plt.show()
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
draw.text((50 ,200), txt, font=font) # put the text on the image
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