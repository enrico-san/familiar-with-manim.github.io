from manim import *

class Say:
    def say(self, text):
        self.comment.become(Text(text, font_size=13, font='Droid Sans Mono').move_to(DR * 2 + RIGHT))

    def addon_write(self, text):
        self.say(text)
        return Write(self.comment, run_time=1)  # TODO run_time is ignored by self.play