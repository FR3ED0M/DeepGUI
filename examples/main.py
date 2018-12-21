from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
parent = Tk()

# -------------------------------------------
# images have to be 640 x 480
# images are now being resized to 250 x 250
#  ------------------------------------------


# creates a popup for the user to select
# pictures from the those that come with the program
def do_popup(event):
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        popup.grab_release()


# this class opens up the different images that
# are on file that come packaged with the program
class openImage:
    def openPlains(self):
        image = Image.open("images/plains.jpg")        # opens an image from database
        image.save('images/new_image.png')             # saves the image under a new name and datatype
        image = image.resize((250, 250), Image.ANTIALIAS)   # resizes the image to 250x250
        photo = ImageTk.PhotoImage(image)       # creates image as a "photo" so .jpg can be opened
        label4 = Label(image=photo)             # creates label where image will be placed
        label4.image = photo                    # put image into the label placeholder
        label4.place(x=10, y=75)                # geometry as to where image will go when opened
        return

    def openBoxy(self):
        image = Image.open("images/boxy.jpg")
        image.save('images/new_image.png')
        image = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label4 = Label(image=photo)
        label4.image = photo
        label4.place(x=10, y=75)
        return

    def openColors(self):
        image = Image.open("images/colors.jpg")
        image.save('images/new_image.png')
        image = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label4 = Label(image=photo)
        label4.image = photo
        label4.place(x=10, y=75)
        return

    def openSpace(self):
        image = Image.open("images/space.jpg")
        image.save('images/new_image.png')
        image = image.resize((250, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label4 = Label(image=photo)
        label4.image = photo
        label4.place(x=10, y=75)
        return

    def openPlasma(self):
        im = Image.open("images/plasma.jpg")
        im.save('images/new_image.png')
        im = im.resize((250, 250), Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(im)
        label4 = Label(image=ph)
        label4.image = ph
        label4.place(x=10, y=75)
        return


# Changes pixel color to either red, green, and blue
# based on the width and height of the image
def rgbPixel():
    im2 = Image.open("images/new_image.png")            # opens the new image file after it was opened above
    im2 = im2.resize((250, 250), Image.ANTIALIAS)       # resized to 250x250
    im2.getpixel((0, 0))                                # gets the pixel (R,G,B) data from the image

    for i in range(0, 50):                              # inside the inner range of 50 of the width
        for j in range(0, 50):                          # inside the inner range of 50 of the height
            im2.putpixel((i * 5, j * 5), (255, 0, 0))   # changes pixel color to Red
            im2.putpixel((i * 5, j * 5), (255, 0, 0))   # changes pixel color to Red
            im2.putpixel((5 * i + 1, 5 * j + 1), (0, 0, 255))   # changes pixel color to Green
            im2.putpixel((5 * i + 2, 5 * j + 2), (0, 0, 255))   # changes pixel color to Green
            im2.putpixel((5 * i + 3, 5 * j + 3), (0, 255, 0))   # changes pixel color to Blue
            im2.putpixel((5 * i + 4, 5 * j + 4), (0, 255, 0))   # changes pixel color to Blue
    ph2 = ImageTk.PhotoImage(im2)                       # standard placement of image just like used above
    label8 = Label(image=ph2)
    label8.image = ph2
    label8.place(x=300, y=75)
    im2 = im2.resize((640, 480), Image.ANTIALIAS)       # resizes the image back to 640x480
    im2.save("images/dead_pixels.png")                  # saves the image to the database
    return


# converts the image to grayscale using a PIL function
# the PIL function used is .convert() in 'L' mode
# which cross references R, G, B pixels and times each by 1000
def grayscale():
    im3 = Image.open("images/new_image.png").convert('L')     # open and convert image to grayscale
    im3 = im3.resize((250, 250), Image.ANTIALIAS)
    ph3 = ImageTk.PhotoImage(im3)
    label8 = Label(image=ph3)
    label8.image = ph3
    label8.place(x=300, y=75)
    im3 = im3.resize((640, 480), Image.ANTIALIAS)       # resizes the image back to 640x480
    im3.save("images/grayscale.png")                    # saves the image to the database
    return


# creates the popup menu to choose images from database
x = openImage()

# tear off the menu from the button
popup = Menu(parent, tearoff=0)

# choice of 640 x 480 images
popup.add_command(label="Boxy", command=x.openBoxy)
popup.add_command(label="Colors", command=x.openColors)
popup.add_command(label="Space", command=x.openSpace)
popup.add_command(label="Plains", command=x.openPlains)
popup.add_command(label="Plasma", command=x.openPlasma)

# title of window
parent.title('Image Process')

# frame of the window
frame = ttk.Frame(parent, borderwidth=5)

# buttons, as well as the bind for clicking to get the popup menu
select = ttk.Button(parent, text="Select Image")
select.bind("<Button-1>", do_popup)
processBttn = ttk.Button(parent, text="Dead Pixels", command=rgbPixel)
grayscaleBttn = ttk.Button(parent, text="Grayscale", command=grayscale)

# placement geometry of frame and buttons
select.place(x=10, y=15)
processBttn.place(x=300, y=15)
grayscaleBttn.place(x=390, y=15)

# geometry of the main "parent" frame and window
parent.geometry("565x375")

parent.mainloop()
