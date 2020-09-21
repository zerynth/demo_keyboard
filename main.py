'''
Keyboard Project using Riverdi IoT Display.
featuring small and capital letters and numbers.
Make sure to pick the correct type of display used
Either resistive or capacitive and the number accordingly

only the resistive displays needs the calibration functions.

from riverdi.displays.bt81x import rtp50
rtp50 is current display used, adjust according to your hardware.
'''

import streams

from riverdi.displays.bt81x import rtp50
from bridgetek.bt81x import bt81x

# Create palletes

palette_R = bt81x.Palette((0xff, 0xff, 0xff), (0xff, 0, 0))
palette_G = bt81x.Palette((0xff, 0xff, 0xff), (0, 0xff, 0))
palette_B = bt81x.Palette((0xff, 0xff, 0xff), (0, 0, 0xff))

# Keyboard positioning variables

vSpac = 6               #   Vertical spacing between buttons
hSpac = 7               #   Vertical spacing between buttons
btnH = 50               #   Button Height
btnW = 70               #   Button Width
vOff = 204              #   Keyboard vertical offset
hOff_1 = 18             #   Keyboard horizontal offset (1)
hOff_2 = 53             #   Keyboard horizontal offset (2)

#  Global used to switch between screens
activeScreen = 0

#  Global used to display current text typed
textLabel = bt81x.Text(10,vOff-100,31,0,"",palette=palette_B)

#  Lowercase picker array
lowercaseArray = [ "",
                   "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                   "q", "w", "e", "r", "t", "z", "u", "i", "o", "p",
                     "a", "s", "d", "f", "g", "h", "j"," k", "l",
                        "y", "x", "c", "v", "b", "n", "m",
                          "shift", "bksp", " ", "-", "."
                  ]

#  Capital picker array
capitalArray = ["",
                "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                "Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P",
                   "A", "S", "D", "F", "G", "H", "J", "K", "L",
                      "Y", "X", "C", "V", "B", "N", "M",
                        "shift", "bksp", " ", "-", "."
                ]

# Numbers of the Keyboard - Common for both screens
btn_1 = bt81x.Button(hOff_1 + 0 * (btnW + hSpac), vOff, btnW, btnH, 31, 0, "1", palette=palette_B)
btn_2 = bt81x.Button(hOff_1 + 1 * (btnW + hSpac), vOff, btnW, btnH, 31, 0, "2", palette=palette_B)
btn_3 = bt81x.Button(hOff_1 + 2 * (btnW + hSpac), vOff, btnW, btnH, 31, 0, "3", palette=palette_B)
btn_4 = bt81x.Button(hOff_1 + 3 * (btnW + hSpac), vOff, btnW, btnH, 31, 0, "4", palette=palette_B)
btn_5 = bt81x.Button(hOff_1 + 4 * (btnW + hSpac), vOff, btnW, btnH, 31, 0, "5", palette=palette_B)
btn_6 = bt81x.Button(hOff_1 + 5 * (btnW + hSpac), vOff, btnW, btnH, 31, 0, "6", palette=palette_B)
btn_7 = bt81x.Button(hOff_1 + 6 * (btnW + hSpac), vOff, btnW, btnH, 31, 0, "7", palette=palette_B)
btn_8 = bt81x.Button(hOff_1 + 7 * (btnW + hSpac), vOff, btnW, btnH, 31, 0, "8", palette=palette_B)
btn_9 = bt81x.Button(hOff_1 + 8 * (btnW + hSpac), vOff, btnW, btnH, 31, 0, "9", palette=palette_B)
btn_0 = bt81x.Button(hOff_1 + 9 * (btnW + hSpac), vOff, btnW, btnH, 31, 0, "0", palette=palette_B)
btnNumList = [btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9, btn_0]         # List used for loop

# Special keys of the Keyboard - Common for both screens
btn_shift = bt81x.Button(hOff_1, vOff + 4 * ( vSpac + btnH), hOff_2 + btnW +60, btnH, 31, 0, "Shift", palette=palette_B)
btn_bksp =  bt81x.Button(hOff_2 + 8 * (btnW + hSpac), vOff + 3 * ( vSpac + btnH), hOff_2 + btnW - hOff_1, btnH, 31, 0, "Bksp", palette=palette_B)
btn_sym =   bt81x.Button(hOff_1, vOff + 4 * ( vSpac + btnH), hOff_2 + btnW - hOff_1, btnH, 31, 0, "Sym", palette=palette_B)
btn_space = bt81x.Button(hOff_2 + 2 * (btnW + hSpac), vOff + 4 * ( vSpac + btnH), (btnW * 5) + (hSpac * 4), btnH, 31, 0, " ", palette=palette_B)
btn_enter = bt81x.Button(hOff_2 + 8 * (btnW + hSpac), vOff + 4 * ( vSpac + btnH), hOff_2 + btnW - hOff_1, btnH, 31, 0, "Enter", palette=palette_B)
btn_comma = bt81x.Button(hOff_2 + 1 * (btnW + hSpac), vOff + 4 * ( vSpac + btnH), btnW, btnH, 31, 0, ",", palette=palette_B)
btn_dot =   bt81x.Button(hOff_2 + 7 * (btnW + hSpac), vOff + 4 * ( vSpac + btnH), btnW, btnH, 31, 0, ".", palette=palette_B)
btnSpecList = [btn_shift, btn_bksp, btn_space, btn_enter, btn_dot]                          # List used for loop

# First row of the Lowercase Keyboard
btn_q = bt81x.Button(hOff_1 + 0 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "q", palette=palette_B)
btn_w = bt81x.Button(hOff_1 + 1 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "w", palette=palette_B)
btn_e = bt81x.Button(hOff_1 + 2 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "e", palette=palette_B)
btn_r = bt81x.Button(hOff_1 + 3 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "r", palette=palette_B)
btn_t = bt81x.Button(hOff_1 + 4 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "t", palette=palette_B)
btn_z = bt81x.Button(hOff_1 + 5 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "z", palette=palette_B)
btn_u = bt81x.Button(hOff_1 + 6 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "u", palette=palette_B)
btn_i = bt81x.Button(hOff_1 + 7 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "i", palette=palette_B)
btn_o = bt81x.Button(hOff_1 + 8 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "o", palette=palette_B)
btn_p = bt81x.Button(hOff_1 + 9 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "p", palette=palette_B)
btnLower1List = [btn_q, btn_w, btn_e, btn_r, btn_t, btn_z, btn_u, btn_i, btn_o, btn_p]      # List used for loop

# Second row of the Lowercase Keyboard
btn_a = bt81x.Button(hOff_2 + 0 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "a", palette=palette_B)
btn_s = bt81x.Button(hOff_2 + 1 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "s", palette=palette_B)
btn_d = bt81x.Button(hOff_2 + 2 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "d", palette=palette_B)
btn_f = bt81x.Button(hOff_2 + 3 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "f", palette=palette_B)
btn_g = bt81x.Button(hOff_2 + 4 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "g", palette=palette_B)
btn_h = bt81x.Button(hOff_2 + 5 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "h", palette=palette_B)
btn_j = bt81x.Button(hOff_2 + 6 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "j", palette=palette_B)
btn_k = bt81x.Button(hOff_2 + 7 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "k", palette=palette_B)
btn_l = bt81x.Button(hOff_2 + 8 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "l", palette=palette_B)
btnLower2List = [btn_a, btn_s, btn_d, btn_f, btn_g, btn_h, btn_j, btn_k, btn_l]             # List used for loop

# Third row of the Lowercase Keyboard
btn_y = bt81x.Button(hOff_2 + 1 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "y", palette=palette_B)
btn_x = bt81x.Button(hOff_2 + 2 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "x", palette=palette_B)
btn_c = bt81x.Button(hOff_2 + 3 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "c", palette=palette_B)
btn_v = bt81x.Button(hOff_2 + 4 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "v", palette=palette_B)
btn_b = bt81x.Button(hOff_2 + 5 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "b", palette=palette_B)
btn_n = bt81x.Button(hOff_2 + 6 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "n", palette=palette_B)
btn_m = bt81x.Button(hOff_2 + 7 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "m", palette=palette_B)
btnLower3List = [btn_y,btn_x,btn_c,btn_v,btn_b,btn_n,btn_m]                                 # List used for loop

# Function to display lowercase keyboard
def displayLowercase():
    global btnNumList
    global btnLower1List
    global btnLower2List
    global btnLower3List
    global btnSpecList
    tagValue = 1
    offsetCounter = 0
    for btn in btnNumList:
        bt81x.track(hOff_1 + offsetCounter * (btnW + hSpac), vOff, btnW, btnH, tagValue)
        bt81x.tag(tagValue)
        bt81x.add_button(btn)
        tagValue +=1
        offsetCounter +=1

    offsetCounter = 0
    for btn in btnLower1List:
        bt81x.track(hOff_1 + offsetCounter * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, tagValue)
        bt81x.tag(tagValue)
        bt81x.add_button(btn)
        tagValue +=1
        offsetCounter +=1

    offsetCounter = 0
    for btn in btnLower2List:
        bt81x.track(hOff_2 + offsetCounter * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, tagValue)
        bt81x.tag(tagValue)
        bt81x.add_button(btn)
        tagValue +=1
        offsetCounter +=1

    offsetCounter = 0
    for btn in btnLower3List:
        bt81x.track(hOff_2 + offsetCounter * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, tagValue)
        bt81x.tag(tagValue)
        bt81x.add_button(btn)
        tagValue +=1
        offsetCounter +=1

    offsetCounter = 0
    for btn in btnSpecList:
        bt81x.track(hOff_2 + offsetCounter * (btnW + hSpac), vOff + 4 * (vSpac + btnH), btnW, btnH, tagValue)
        bt81x.tag(tagValue)
        bt81x.add_button(btn)
        tagValue +=1
        offsetCounter +=1

    bt81x.add_text(textLabel)


# Create button object (Capletters)

# First row of the Capletters Keyboard
btn_Q = bt81x.Button(hOff_1 + 0 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "Q", palette=palette_B)
btn_W = bt81x.Button(hOff_1 + 1 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "W", palette=palette_B)
btn_E = bt81x.Button(hOff_1 + 2 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "E", palette=palette_B)
btn_R = bt81x.Button(hOff_1 + 3 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "R", palette=palette_B)
btn_T = bt81x.Button(hOff_1 + 4 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "T", palette=palette_B)
btn_Z = bt81x.Button(hOff_1 + 5 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "Z", palette=palette_B)
btn_U = bt81x.Button(hOff_1 + 6 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "U", palette=palette_B)
btn_I = bt81x.Button(hOff_1 + 7 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "I", palette=palette_B)
btn_O = bt81x.Button(hOff_1 + 8 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "O", palette=palette_B)
btn_P = bt81x.Button(hOff_1 + 9 * (btnW + hSpac), vOff + (vSpac + btnH), btnW, btnH, 31, 0, "P", palette=palette_B)
btnCap1List = [btn_Q, btn_W, btn_E, btn_R, btn_T, btn_Z, btn_U, btn_I, btn_O, btn_P]

# Second row of the Capletters Keyboard

btn_A = bt81x.Button(hOff_2 + 0 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "A", palette=palette_B)
btn_S = bt81x.Button(hOff_2 + 1 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "S", palette=palette_B)
btn_D = bt81x.Button(hOff_2 + 2 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "D", palette=palette_B)
btn_F = bt81x.Button(hOff_2 + 3 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "F", palette=palette_B)
btn_G = bt81x.Button(hOff_2 + 4 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "G", palette=palette_B)
btn_H = bt81x.Button(hOff_2 + 5 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "H", palette=palette_B)
btn_J = bt81x.Button(hOff_2 + 6 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "J", palette=palette_B)
btn_K = bt81x.Button(hOff_2 + 7 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "K", palette=palette_B)
btn_L = bt81x.Button(hOff_2 + 8 * (btnW + hSpac), vOff + 2 * (vSpac + btnH), btnW, btnH, 31, 0, "L", palette=palette_B)
btnCap2List = [btn_A,btn_S,btn_D,btn_F,btn_G,btn_H,btn_J,btn_K,btn_L]

# Third row of the Capletters Keyboard
btn_Y = bt81x.Button(hOff_2 + 1 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "Y", palette=palette_B)
btn_X = bt81x.Button(hOff_2 + 2 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "X", palette=palette_B)
btn_C = bt81x.Button(hOff_2 + 3 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "C", palette=palette_B)
btn_V = bt81x.Button(hOff_2 + 4 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "V", palette=palette_B)
btn_B = bt81x.Button(hOff_2 + 5 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "B", palette=palette_B)
btn_N = bt81x.Button(hOff_2 + 6 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "N", palette=palette_B)
btn_M = bt81x.Button(hOff_2 + 7 * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, 31, 0, "M", palette=palette_B)
btnCap3List = [btn_Y, btn_X, btn_C, btn_V, btn_B, btn_N, btn_M]

# Function to display capital keyboard
def displayCapital( ) :
    global btnNumList
    global btnCap1List
    global btnCap2List
    global btnCap3List
    global btnSpecList
    tagValue = 1
    offsetCounter = 0
    for btn in btnNumList:
        bt81x.track(hOff_1 + offsetCounter * (btnW + hSpac), vOff, btnW, btnH, tagValue)
        bt81x.tag(tagValue)
        bt81x.add_button(btn)
        tagValue +=1
        offsetCounter +=1

    for btn in btnCap1List:
        bt81x.track(hOff_1 + offsetCounter * (btnW + hSpac), vOff, btnW, btnH, tagValue)
        bt81x.tag(tagValue)
        bt81x.add_button(btn)
        tagValue +=1
        offsetCounter +=1

    for btn in btnCap2List:
        bt81x.track(hOff_1 + offsetCounter * (btnW + hSpac), vOff, btnW, btnH, tagValue)
        bt81x.tag(tagValue)
        bt81x.add_button(btn)
        tagValue +=1
        offsetCounter +=1

    offsetCounter = 0
    for btn in btnCap3List:
        bt81x.track(hOff_2 + offsetCounter * (btnW + hSpac), vOff + 3 * (vSpac + btnH), btnW, btnH, tagValue)
        bt81x.tag(tagValue)
        bt81x.add_button(btn)
        tagValue +=1
        offsetCounter +=1

    offsetCounter = 0
    for btn in btnSpecList:
        bt81x.track(hOff_2 + offsetCounter * (btnW + hSpac), vOff + 4 * (vSpac + btnH), btnW, btnH, tagValue)
        bt81x.tag(tagValue)
        bt81x.add_button(btn)
        tagValue +=1
        offsetCounter +=1

    bt81x.add_text(textLabel)

# Function get character from Capital or Lowercase picker array
def tag2char(tag):
    global activeScreen
    if activeScreen == 0:
        return lowercaseArray[tag]
    elif activeScreen == 1:
        return capitalArray[tag]

# Update the screen
def updateScreen():
    global activeScreen
    bt81x.dl_start()
    bt81x.clear(1, 1, 1)
    if activeScreen == 0:
        displayLowercase()
    elif activeScreen == 1:
        displayCapital()
    bt81x.display()
    bt81x.swap_and_empty()

# Press event handler - called when press is detected
def pressed(tag, tracked, tp):
    global activeScreen
    letter = tag2char(tag)
    if letter == "bksp":
        # When Backspace is pressed delete the last char
        textLabel.text = textLabel.text[:-1]
    elif letter == "shift":
        '''
            When shift is pressed:
                - Toggle screen global
                - Clear the screen and switch to aother one
        '''
        activeScreen = not activeScreen
        bt81x.swap_and_empty()
    else:
        textLabel.text = textLabel.text + letter
    updateScreen()

streams.serial() # open serial channel to display debug messages

bt81x.init(SPI0, D4, D33, D34)
bt81x.touch_loop(((-1, pressed), ))
bt81x.dl_start()
bt81x.calibrate()
bt81x.swap_and_empty()

updateScreen()

