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