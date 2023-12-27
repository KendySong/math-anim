from manim import *
import config

class SphereFormula(Scene) :
    def construct(self) :
        self.camera.background_color = BLACK

        intro_text = Text('Sphere formula proof', font_size=config.TITLE_SIZE).set_color(BLUE).shift(UP * 7)
        circle_equation_0 = MathTex(r'x^2+y^2=r^2', font_size=config.TEX_SIZE).shift(UP * 5)
        circle = Circle(3).set_stroke(color=GREEN, width=5)

        radius_line = Line(circle.get_center(), circle.get_right()).set_color(BLUE)
        radius_text = MathTex('r', font_size=config.TEX_SIZE-12).move_to(radius_line.get_bottom() + DOWN)

        self.play(
            Write(intro_text, run_time=0.5),
            Create(circle_equation_0),
            Create(circle),
            Create(radius_line),
            Create(radius_text)
        )

        circle_equation_1 = MathTex(r'y^2=r^2-x^2', font_size=config.TEX_SIZE).move_to(circle_equation_0)
        self.play(
            FadeOut(intro_text),
            Transform(circle_equation_0, circle_equation_1)
        )
        self.remove(circle_equation_0)

        circle_equation_2 = MathTex(r'y=\sqrt{r^2-x^2}', font_size=config.TEX_SIZE).move_to(circle_equation_0)
        self.play(
            Transform(circle_equation_1, circle_equation_2)
        )
        self.remove(circle_equation_1)
        circle_equation_3 = MathTex(r'f(x)=\sqrt{r^2-x^2}', font_size=config.TEX_SIZE, color=RED).move_to(circle_equation_0)

        axes = Axes(x_range=[-1.5, 1.5], y_range=[0, 1.5])
        circle_func = axes.plot(lambda x : np.sqrt(1-x*x), x_range=[-1, 1], color=RED)
        self.play(
            FadeOut(circle),
            FadeOut(radius_line),
            FadeOut(radius_text),
            Transform(circle_equation_2, circle_equation_3),
            Create(axes),
            Create(circle_func),
            Write(axes.get_axis_labels())
        )

        

        self.wait()