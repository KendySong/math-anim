from manim import *
import config

class Limit_0(Scene) :
    def construct(self):
        self.camera.background_color = BLACK
        
        limit_0 = MathTex(r'\lim_{x\to 0} \frac{sin(6x)}{2x}', font_size=config.TEX_SIZE)
        self.play(Create(limit_0))

        equal = MathTex('=', font_size=config.TEX_SIZE)
        self.play(
            limit_0.animate.shift(UP * 3),
            FadeIn(equal)
        )

        limit_1 = MathTex(r'\lim_{x\to 0} \frac{sin(6x)}{2x} \frac{6x}{6x}', font_size=config.TEX_SIZE).shift(DOWN * 3)
        self.play(FadeIn(limit_1))

        self.play(
            FadeOut(limit_0),
            FadeOut(equal),
            limit_1.animate.shift(UP * 6)
        )

        limit_2 = MathTex(r'\lim_{x\to 0} \frac{sin(6x)}{6x}', font_size=config.TEX_SIZE).shift(DOWN * 3).align_to(limit_1, direction=LEFT)
        limit_2_1 = MathTex(r'\frac{6x}{2x}', font_size=config.TEX_SIZE).shift(DOWN * 3).next_to(limit_2, RIGHT)
        self.play(
            FadeIn(equal),
            FadeIn(limit_2),
            FadeIn(limit_2_1)
        )

        self.play(
            FadeOut(limit_1),
            FadeOut(equal),
            limit_2.animate.shift(UP * 6),
            limit_2_1.animate.shift(UP * 6)
        )

        self.play(
            FadeOut(limit_2),
            limit_2_1.animate.shift(LEFT * 3),
        )
 
        self.play(
            limit_2_1.animate.move_to(ORIGIN)
        )

        result = MathTex(r'\frac{6}{2}', font_size=config.TEX_SIZE).move_to(limit_2_1)
        followText = Text('Follow for more', font_size=config.TEX_SIZE, color=BLUE).shift(UP * 4)
        self.play(
            Transform(limit_2_1, result),
            Create(followText)
        )

        self.wait()