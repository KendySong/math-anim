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

class Updater(Scene):
    def construct(self):
        plane = NumberPlane().add_coordinates()

        rect = RoundedRectangle(
            width=3,
            height=2,
        ).set_fill(color=BLUE, opacity=1)
         
        equation = MathTex(r'\lim_{x\to\infty} \frac{1}{x}=0')
        equation.move_to(rect.get_center())
        equation.add_updater(lambda x : x.move_to(rect.get_center()))

        self.play(
            Create(plane),
            Create(rect),
            Create(equation)
        )

        self.play(rect.animate.shift(UP*3))
        self.play(rect.animate.shift(RIGHT*3))
        self.play(rect.animate.shift(LEFT*3))

        equation.clear_updaters()
        self.play(rect.animate.shift(DOWN*3))

        self.wait()
        pass

class ValTracker(Scene):
    def construct(self):
        r = ValueTracker(0.5)

        circle = always_redraw(lambda :
        Circle(
            radius=r.get_value(),
            color=BLUE,
        ))

        line = always_redraw(lambda :
        Line(
            start=circle.get_center(),
            end=circle.get_right(),
        )
        )

        self.play(
            Create(circle),
            Create(line)
        )

        self.play(
            r.animate.set_value(3),
            run_time=3
        )

        self.wait()

class GraphArea(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-7, 6],
            y_range=[-5, 5],           
        ).add_coordinates()

        limit = ValueTracker(0)
        graph = axes.plot(lambda x: 0.1*x*(x-5)*(x+5), color=YELLOW)
        area = always_redraw(lambda:axes.get_area(graph, x_range=[0, limit.get_value()], color=[BLUE, YELLOW]))

        integral_text = MathTex(
            r'\int_{0}^{6} \frac{1}{10}x(x-5)(x+5)\,dx',
            font_size=36
        ).shift(RIGHT*2.85+UP*2)

        self.play(
            Create(axes),
            Create(graph),
            Create(axes.get_axis_labels()),
            Create(area),
            Write(integral_text),
        )

        self.play(
            limit.animate.set_value(6),
            run_time=3
        )
        
        self.wait()

class RiemannGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5]
        )

        dx = ValueTracker(0.5)
        graph = axes.plot(lambda x : np.sin(x), color=BLUE, x_range=[-5, 5])
        rects = always_redraw(lambda : axes.get_riemann_rectangles(graph=graph, x_range=[-5, 5], stroke_color=WHITE, dx=dx.get_value()))

        self.play(
            Create(axes),
            Create(graph),
            Create(rects)
        )

        self.play(dx.animate.set_value(0.01), run_time=3)
        self.wait()

class GraphMovement3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            z_range=[-5, 5]
        )

        graph = axes.plot(lambda x : np.sin(x), color=BLUE, x_range=[-5, 5])
        rects = axes.get_riemann_rectangles(graph=graph, x_range=[-5, 5], stroke_color=WHITE, dx=0.1)

        graph_2 = axes.plot_parametric_curve(
            lambda t : np.array([np.cos(t), np.sin(t), t]),
            t_range=[-2*PI, 2*PI],
            color=RED
        )

        self.play(
            Create(axes),
            Create(graph),
            Create(rects)
        )

        #phi -> up and down
        #theta -> left and right
        #by default camera [theta = -PI/2, phi = 0]
        self.move_camera(
            phi=PI/3
        )

        self.move_camera(
            theta=0
        )

        #Animation by turn around graph_2
        self.begin_ambient_camera_rotation(
            rate=PI/5, #"Speed of rotation"
            about="theta"
        )
        self.wait()
        self.play(Create(graph_2))
        self.wait()       
        self.stop_ambient_camera_rotation()

class ParametricSurface3D(ThreeDScene) :
    def construct(self):
        axes = ThreeDAxes(

        )
        graph = axes.plot(lambda x : x**2, color=YELLOW)

        self.play(
            Create(axes),
            Create(axes.get_axis_labels()),
            Create(graph)
        )
        self.move_camera(phi=PI/3, theta=-PI/4)

        surface = Surface(
            lambda u, v: axes.c2p(u, v, u*v),
            u_range=[-PI, PI],
            v_range=[-2.5, 2.5],
            checkerboard_colors=[BLUE, YELLOW]
        )

        self.play(
            Create(surface)
        )

        self.begin_ambient_camera_rotation(
            rate=PI/5,
            about="theta"
        )
        self.wait(5)
        self.stop_ambient_camera_rotation()

        self.wait()

class RevolutionPOC(ThreeDScene) :
    def construct(self):

        
        self.wait()