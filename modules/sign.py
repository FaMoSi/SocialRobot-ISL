from location import Location
from movement import Movement


class Sign:
    def __init__(self, robot, l_r, location, configuration, orientation, movement):
        self.robot = robot
        self.l_r = l_r
        self.location = location
        self.configuration = configuration
        self.orientation = orientation
        self.movement = movement

    def perform_sign(self):
        Location(self.robot, self.location, self.l_r)
        # Configuration(self.config).setConfiguration()
        # Orientation(self.orientation).setOrientation()
        Movement(self.robot, self.movement, self.l_r)

