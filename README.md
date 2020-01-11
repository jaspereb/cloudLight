# cloudLight

This project is an arduino based lamp in the shape of a cloud. It is controlled with an IR remote. 

# States
* Lightning
* Lamp mode (white)
* Disco
* Colour Gradient
* Relax (Slow Gradient)
* Solid Colour

# Independent Variables
* Brightness
* Cycle Time

It also has a timeout.

# Button Assignment
0 - Off
1 - Lamp
2 - Solid Colour
3 - Colour Gradient
4 - Relax
5 - Lightning
6 - Disco

Up - Increase Brightness
Down - Decrease Brightness
Left - Decrease Cycle Time
Right - Increase Cycle Time
 
# Libraries
Both IR and neopixels require interrupts so using them together is tricky. That's why the refactored IRLib2 library is needed. 