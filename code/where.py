from manim import *
import addons

class Where(Scene, addons.Say):
    def construct(self):
        LABEL_OFFSET = 0.15*UP
        self.wait()
        
        spots = ['ORIGIN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'UL', 'UR', 'DL', 'DR']

        self.comment = Text(' ')
        self.add(self.comment)

        mobs = {}  # 'spot': {text, dot}
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
                    self.play(self.addon_write(f"""
                from manim import *

                class MyPresentation(Scene):
                    def construct(self):
                        dot = Dot()
                        self.add(dot)
                        dot.move_to({spot})
                        self.wait(3)"""))
                else:
                    self.play(self.addon_write(f"dot.move_to({spot})"))
                self.wait(2)

            last_text.set_color(GRAY)
            last_dot.set_color(GRAY)

        if True:
            t, dot = mobs['ORIGIN'].values()
            t.set_color(WHITE)
            dot.set_color(WHITE)

            self.play(
                self.addon_write(f"self.play( dot.animate.move_to(LEFT * 3) )"),
                dot.animate.move_to(LEFT * 3), run_time=2)
            self.wait(2)

            self.play(
                self.addon_write(f"self.play( dot.animate.move_to(LEFT * -4) )"),
                dot.animate.move_to(LEFT * -4), run_time=2)
            self.wait(2)

            self.play(
                self.addon_write(f"""
                    self.play(
                        dot.animate.move_to(dot.get_center() + UL * 2)
                    )"""),
                dot.animate.move_to(dot.get_center() + UL * 2),
                run_time=2)
            self.wait(2)

            t, dot2 = mobs['LEFT'].values()
            dot2.set_color(WHITE)
            self.play(
                self.addon_write(f"""
                    self.play(
                        dot.animate.move_to(dot.get_center() + DOWN),
                        dot2.animate.move_to(dot2.get_center() + DOWN),
                        run_time=4
                    )"""),
                dot.animate.move_to(dot.get_center() + DOWN),
                dot2.animate.move_to(dot2.get_center() + DOWN),
                run_time=4
            )
            self.wait(2)