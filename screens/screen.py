import pygame

class Screen(object):
    def __init__(self, screen):
        self.screen = screen
        self.objects = []

    def render(self):
        for o in self.objects:
            o.render()

    def events(self, events):
        for o in self.objects:
            o.events(events)
