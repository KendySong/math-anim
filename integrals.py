from manim import *

class Integral_0(Scene) :
    def construct(self):
        baseIntegral = MathTex(r'\int_{-1}^{1} \frac{5}{(2x+3)^2} \,dx', font_size=96).shift(LEFT * 3)
        uSub_u = MathTex(r'u = 2x + 3', font_size=72).shift(UP * 2).next_to(baseIntegral, direction=UP + RIGHT*4)
        uSub_du = MathTex(r'du = 2 \,dx', font_size=72).next_to(uSub_u, direction=DOWN).align_to(uSub_u, direction=LEFT)
        uSub_dx =  MathTex(r'dx = \frac{du}{2}', font_size=72).next_to(uSub_du, direction=DOWN).align_to(uSub_u, direction=LEFT)

        subIntegral = MathTex(r'\int_{1}^{5} \frac{5}{u^2}\, \frac{du}{2}', font_size=96)
        subFracIntegral = MathTex(r'\frac{5}{2} \int_{1}^{5} \frac{1}{u^2}\, du', font_size=96)
        equal = MathTex('=', font_size=96)
        primitive = MathTex(r'\frac{5}{2} (-\frac{1}{5} + \frac{5}{5})', font_size=96).next_to(equal, direction=DOWN*1.5)


        self.play(Create(baseIntegral))
        self.play(FadeIn(uSub_u))
        self.wait(0.1)
        self.play(FadeIn(uSub_du))
        self.wait(0.1)
        self.play(FadeIn(uSub_dx))

        self.play(
            Transform(baseIntegral, subIntegral), 
            Transform(uSub_u, subIntegral), 
            Transform(uSub_du, subIntegral), 
            Transform(uSub_dx, subIntegral)
        )
        
        self.remove(uSub_u)
        self.remove(uSub_du)
        self.remove(uSub_dx)

        self.play(Transform(baseIntegral, subIntegral))
        self.wait(0.05)
        self.play(Transform(baseIntegral, subFracIntegral))
        self.remove(baseIntegral)

        self.play(subFracIntegral.animate.shift(UP * 2.5))
        self.play(Create(equal))
        self.play(Create(primitive))
        
        self.play(FadeOut(subFracIntegral), primitive.animate.move_to(ORIGIN+LEFT*2), equal.animate.shift(RIGHT))
        self.play(Create(MathTex('2', font_size=96).next_to(equal, direction=RIGHT)))

        self.wait(0.2)



