# https://pypi.org/project/PyAutoIt/

## package from 8 years ago, looks like it has a problem with the pixel_search
# pip install -U pyautoit

## alternative package?
# pip install autoit

# Defaulting to user installation because normal site-packages is not writeable
# Collecting autoit
#   Downloading autoit-0.2.6-py3-none-any.whl (15 kB)
# Installing collected packages: autoit
# Successfully installed autoit-0.2.6

#----------------------------------------------------------------------------------

# taken from the example page
def fooExample():
    import autoit

    # autoit.run("notepad.exe")
    # autoit.win_wait_active("[CLASS:Notepad]", 3)
    # autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
    # autoit.win_close("[CLASS:Notepad]")
    # autoit.control_click("[Class:#32770]", "Button2")

    # new: change Jabber to active
    autoit.mouse_click("right",1596,1080,1)
    #autoit.win_wait_active("Cisco Jabber", 3)
    autoit.mouse_click("left", 1600, 920, 1)

    print(f"is_admin: {autoit.is_admin()}")
    coords = autoit.pixel_search(0, 0, 3840, 2173, 0xFFFFFF )
    print("coords white:", coords)
    coords = autoit.pixel_search(0, 0, 3840, 2173, 0x000000)
    print("coords black:", coords)
#    coords = autoit.pixel_search(0, 0, 3840, 2173, 0xFFEE4E, 128) # last value is the allowed variation, but this does not help
#    print("coords rotes TEN icon:", coords)
    # (right, top, left, bottom).
    # thought: left, top, right, bottom
    coords = autoit.pixel_search(3840, 0, 0, 2173, 0xFFEE4E, 100) # last value is the allowed variation, but this does not help
    print("coords rotes TEN icon:", coords)

#----------------------------------------------------------------------------------

def exampleAutoitPackage():
    import autoit # does not work

    # Click wherever the mouse is
    autoit.click()


# test call
#fooExample()

exampleAutoitPackage()

#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
