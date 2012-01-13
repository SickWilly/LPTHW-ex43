# LPTHW exercise #43 -- specifies each room should
# be its own class.
class room1(object):
    def room_desc(self):
        print "Room 1"

    # Dict of option user can input and where
    # option will take the user
    room_options = {'north': 'room2'}

class room2(object):
    def room_desc(self):
        print "Room 2"

    # Dict of option user can input and where
    # option will take the user
    room_options = {'south': 'room1'}


# this should do the major work with of the game
class engine(object):
    
    def __init__(self, start):
        self.start = start
        
    # This should print the current room's room_desc
    # then list the room's options so the user knows
    # valid options. Finally it should print the next
    # room's room_desc and cycle. This will go in a
    # while loop, once I get its basic functionality working.
    def play(self):
        # next should now be the string 'room1'
        next = self.start
        # this line doesn't work. And I'm not sure exactly why.
        next.room_desc()

a_game = engine('room1')
a_game.play()
