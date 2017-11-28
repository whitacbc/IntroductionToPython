"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Brian Whitacre.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg # import the rosegraphics
window = rg.TurtleWindow() # set up windows
# set up the names of the turtle
John = rg.SimpleTurtle()
Mike = rg.SimpleTurtle()
Shell = rg.SimpleTurtle()
# changes colors of the turtles
John.pen = rg.Pen("red",1)
Mike.pen = rg.Pen('blue',1)
Shell.pen = rg.Pen('green',1)
# moves the turtles John and Mike sideways
John.forward(100)
Mike.backward(100)
# change speed to be fast
John.speed = 30
Mike.speed= 30
Shell.speed = 30
size = 46 # size of the hexagon
for i  in range(47):
    # stat drawing hexagons larger and larger
    John.draw_regular_polygon(6, size)
    Mike.draw_regular_polygon(6, size)
    Shell.draw_regular_polygon(6, size)
    size = i # change size of hexagon
    print(size) # print size of hexagon
window.close_on_mouse_click()