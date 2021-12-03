from manim import *
import addons

WAIT_BETWEEN = 2
LABEL_OFFSET = 0.15*UP

class Where(Scene, addons.Say):
    def construct(self):
        self.wait()
        
        spots = ['ORIGIN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'UL', 'UR', 'DL', 'DR']

        self.comment = Text(' ')
        self.add(self.comment)

        mobs = {}
        for spot in spots:
            place = globals()[spot]
            text = Text(spot, font_size=10, color=BLACK).move_to(place + LABEL_OFFSET)
            mobs[spot] = {'text': text}
            self.add(text)

            dot = Dot(place, color=BLACK)
            mobs[spot]['dot'] = dot
            self.add(dot)

        last_text = last_dot = None
        if True:
            first = True
            for spot, item in mobs.items():
                if last_text:
                    last_text.set_color(GRAY)
                    last_dot.set_color(GRAY)
                
                last_text, last_dot = item.values()
                last_text.set_color(WHITE)
                last_dot.set_color(WHITE)

                if first:
                    first = False
                    self.say(f"""
                from manim import *

                class MyPresentation(Scene):
                    def construct(self):
                        dot = Dot()
                        self.add(dot)
                        dot.move_to({spot})
                        self.wait(3)""")
                else:
                    self.say(f"dot.move_to({spot})")
                self.wait(WAIT_BETWEEN)

            last_text.set_color(GRAY)
            last_dot.set_color(GRAY)

        if True:
            t, dot = mobs['ORIGIN'].values()
            t.set_color(WHITE)
            dot.set_color(WHITE)

            self.say(f"self.play( dot.animate.move_to(LEFT * 3) )")
            self.play(dot.animate.move_to(LEFT * 3), run_time=2)
            self.wait(2)

            self.say(f"self.play( dot.animate.move_to(LEFT * -4) )")
            self.play(dot.animate.move_to(LEFT * -4), run_time=2)
            self.wait(2)

            self.say(f"""
                self.play(
                    dot.animate.move_to(dot.get_center() + UL * 2)
                )""")
            self.play(dot.animate.move_to(dot.get_center() + UL * 2), run_time=2)
            self.wait(2)

