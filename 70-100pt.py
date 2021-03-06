##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

# This is the code for the outline and color of the house
houseoutline = drawpad.create_rectangle(230,170,470,450, fill = 'red')

# This is the code for the roof of my house
houseroof = drawpad.create_polygon(230,170,350,100,470,170, fill = 'black')

# This is the code for my windows
window1 = drawpad.create_rectangle(265,200,325,260, fill = 'white')
window2 = drawpad.create_rectangle(375,200,435,260, fill = 'white')
window3 = drawpad.create_rectangle(265,290,325,350, fill = 'white')
window4 = drawpad.create_rectangle(375,290,435,350, fill = 'white')


# This is the code for my door
frontdoor = drawpad.create_rectangle(325,370,375,450, fill = 'brown')

# This is code for my doorhandle
doorhandle = drawpad.create_rectangle(363,405,368,405, fill = 'black')

# This is the code for my chimney
chimney = drawpad.create_polygon(470,170,470,100,440,100,440,153, fill = 'burlywood4')

# This is the code for my green grass
grass = drawpad.create_rectangle(0,450,800,600, fill = 'dark green')


root.mainloop()