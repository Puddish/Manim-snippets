from manim import * 
class MuoviOggetti(Scene):
    def construct(self):
        axes = Axes(x_range = [-3,3,1], y_range=[-3,3,1], x_length= 5, y_length=5)
        rectangle = Rectangle(color= WHITE)
        #axes.to_edge(LEFT, buff =0.5)
        self.play(Write(axes))
        self.add(rectangle)
        self.play(Write(rectangle))
        self.play(rectangle.animate.shift(RIGHT))

