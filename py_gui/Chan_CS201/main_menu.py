import os

class MainMenu:
    def __init__(self, add, ss, prstu):
        self.add = add
        self.ss = ss
        self.prstu = prstu

    def main_menu(self, user):
        user_name, user_id = user.split()

#いや、もうねえわここ