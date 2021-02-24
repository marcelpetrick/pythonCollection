# https://pypi.org/project/PyAutoIt/

# pip install -U pyautoit

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
    autoit.win_wait_active("Cisco Jabber", 3)
    autoit.mouse_click("left", 1600, 920, 1)

#----------------------------------------------------------------------------------

# test call
fooExample()

#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------


#----------------------------------------------------------------------------------

