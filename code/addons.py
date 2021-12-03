from manim import *

class Say:
    def say(self, text):
        self.comment.become(Text(text, font_size=13, font='Droid Sans Mono').move_to(DR * 2 + RIGHT))

