import hou
from canvaseventtypes import *
import nodegraphdisplay as display
import nodegraphview as view
from datetime import datetime


def your_function(uievent):
    ctrl = uievent.modifierstate.ctrl
    shift = uievent.modifierstate.shift

    if ctrl == 1 and shift == 0:
        print('registered')
        return True
    elif shift == 1 and ctrl == 1:
        print("ctrl shift")
        return True
    else:
        return False


def do_more(uievent):
    if isinstance(uievent, MouseEvent):
        if (uievent.eventtype == 'mousedown'):
            try:
                if not hou.session.first_click:
                    if hou.session.first_click - datetime.now() > 1000:
                        hou.session.first_click = datetime.now()
                else:
                    second = datetime.now()
                    diff = second - hou.session.first_click
                    mil_diff = diff.total_seconds() * 1000
                    if not mil_diff < 400:
                        hou.session.first_click = datetime.now()
                        return False
                    else:
                        return your_function(uievent)

            except:
                hou.session.first_click = datetime.now()
    return False


# def do_stuff(uievent):

#     if isinstance(uievent, MouseEvent):
#         if (uievent.eventtype == 'mousedown'):
#             try:
#                 if not hou.session.first_click:
#                     if hou.session.first_click - datetime.now() > 1000:
#                         hou.session.first_click = datetime.now()
#                 else:
#                     second = datetime.now()
#                     diff = second - hou.session.first_click
#                     mil_diff = diff.total_seconds() * 1000
#                     if not mil_diff < 200:
#                         hou.session.first_click = datetime.now()
#                         return True
#                     else:
#                         your_function(uievent)

#             except:
#                 hou.session.first_click = datetime.now()
