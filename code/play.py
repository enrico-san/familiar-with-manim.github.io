from manim import *
import addons

class Play(Scene, addons.Say):
    def construct(self):
        self.wait()
        
        self.comment = Text(' ')
        
        self.wait(3)