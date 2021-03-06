"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jeremy Roy.
"""  # TODOne: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODOne: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------

    window = rg.RoseWindow(800, 800)

    center_point = rg.Point(200, 200)
    circle1 = rg.Circle(center_point, 69)
    circle1.fill_color = "red"
    circle1.attach_to(window)

    center_point = rg.Point(400, 400)
    circle2 = rg.Circle(center_point, 29)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # TODOne: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(1000,1000)

    x = 500
    y = 500
    center_point = rg.Point(x, y)
    circle = rg.Circle(center_point, 74)
    circle.fill_color = 'blue'
    circle.attach_to(window)

    x = 250
    y = 250
    corner1 = rg.Point(x, y)
    corner2 = rg.Point(200, 200)
    rectangle = rg.Rectangle(corner1, corner2)
    rectangle.fill_color = 'red'
    rectangle.attach_to(window)

    window.render()
    window.close_on_mouse_click()

    print(circle.outline_thickness)
    print(circle.fill_color)
    print(center_point)
    print("500")
    print('500')
    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print('Point(225.0, 225.0)')
    print('225')
    print('225')


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # done: 4. Implement and test this function.
    # ------------------------------------------------------------------

    window = rg.RoseWindow(1000, 1000)
    start = rg.Point(1, 1)
    end = rg.Point(750, 750)
    line1 = rg.Line(start, end)
    line1.color = 'green'
    line1.thickness = 15
    line1.attach_to(window)

    start = rg.Point(250, 250)
    end = rg.Point(550, 750)
    line2 = rg.Line(start, end)
    line2.color = 'red'
    line2.attach_to(window)

    window.render()
    window.close_on_mouse_click()

    print(line1.get_midpoint())
    print('375.5')
    print('375.5')
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
