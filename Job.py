import random


class Job:
    def __init__(self):
        self.pages = random.randint(1, 10)

    def print_page(self):
        return self.pages - 1

    def check_complete(self):
        return self.pages == 0
