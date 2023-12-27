from manim import *
import config

class PlotFunction(Scene):
    def construct(self):
        axes = Axes()
        graph = axes.plot(lambda x : x + 1, color=BLUE)
        graph_label = axes.get_graph_label(graph, label="x+1", direction=DOWN*2, x_val=1)

        self.play(
            Create(axes),
            Create(graph),
            Write(axes.get_axis_labels()),
            Write(graph_label)
        )

        self.wait()
        pass

class ThreeDGraph(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        graph = axes.plot(lambda x : np.cos(x), color=BLUE)

        self.play(
            Create(axes),
            Create(graph)
        )

        self.move_camera(theta=3, run_time=3)
        self.wait()
        pass

#https://github.com/brianamedee/Manim-Tutorials-2021/blob/main/7SAofRevolution.py#L98
class FunctionRevolution(ThreeDScene):
    def construct(self):
        text = Tex("Surface Area of a Solid Revolutions?")
        self.play(Write(text))
        self.play(FadeOut(text))

        self.begin_ambient_camera_rotation()
        self.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes(
            x_range=[0, 4.1, 1],
            x_length=5,
            y_range=[-4, 4.1, 1],
            y_length=5,
            z_range=[-4, 4, 1],
            z_length=5,
        ).add_coordinates()

        #Graph
        function = axes.plot(lambda x: 0.25 * x ** 2, x_range=[0, 4], color=YELLOW)
        area = axes.get_area(graph=function, x_range=[0, 4], color=[BLUE_B, BLUE_D])

        #Surface
        e = ValueTracker(2 * PI)
        surface = always_redraw(
            lambda: Surface(
                lambda u, v: axes.c2p(
                    v, 0.25 * v ** 2 * np.cos(u), 0.25 * v ** 2 * np.sin(u)
                ),
                u_range=[0, e.get_value()],
                v_range=[0, 4],
                checkerboard_colors=[BLUE_B, BLUE_D],
            )
        )

        #Graph creation
        self.play(
            LaggedStart(Create(axes), Create(function), Create(area), Create(surface)),
            run_time=4,
            lag_ratio=0.5,
        )

        self.play(
            Rotating(
                VGroup(function, area),
                axis=RIGHT,
                radians=2 * PI,
                about_point=axes.c2p(0, 0, 0),
            ),
            e.animate.set_value(2 * PI),
            run_time=5,
            rate_func=linear,
        )
        self.wait()
        pass