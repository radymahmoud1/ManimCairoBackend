from manimlib.imports import *
from numpy import *

class Group(GraphScene):
    CONFIG={
        "x_min":0,
        "x_max":2.25*pi,
        "x_axis_label": r"$\theta$",
        "x_labeled_nums": None,
        "y_min":-2,
        "y_max":2,
        "y_axis_label":r"f($\theta$)",
        "graph_origin":ORIGIN+LEFT,
        "x_axis_width": 2.25*pi,
        "y_axis_height": 4,
        "y_tick_frequency" : 4,
        "x_tick_frequency" : 2.25*pi,  
        "default_graph_colors": [BLUE],
        "axes_color": RED,
        "y_labeled_nums": None
        }

    def graph(self):
        self.setup_axes(animate=True)
        
    def construct(self):

        #text of graph

        text=TexMobject(r"f(\theta)=Sin(\theta)").to_corner(UP)
        
        self.play(Write(text),run_time=2)
        self.wait()
        self.graph()
        #define the graph of sin(x) using the function (SIN)
        def SIN(x):
            return np.sin(x)
        sin=self.get_graph(SIN,x_min=0,x_max=2*pi)

        #Show the Graph

        self.play(ShowCreation(sin),run_time=3)
        self.wait()

        #Define a circle, line from circles radius to graph, line of circle's radius, and dots on graph's axis, circle's radius, circle's origin 

        #circle 

        circle=Circle(radius=1,color=GREEN).shift(4*LEFT)

        #dots

        dot_on_circle=Dot(color=BLUE).move_to(circle.point_from_proportion(0))
        dot_on_axis=Dot(self.graph_origin)
        dot_at_center_of_circle=Dot(color=BLUE).move_to(circle)

        #lines

        line_to_sin_graph=Line(dot_on_circle,dot_on_axis,buff=0)
        line_of_circle_radius=Line(dot_at_center_of_circle,dot_on_circle,color=BLUE)

        # add theta number, text, and align them together 
        theta_text = TexMobject("\\theta =").next_to(circle,DOWN)
        theta_number = DecimalNumber(0,unit=r"^\circ")
        theta_number.next_to(theta_text, RIGHT)
        theta_number.align_to(theta_text, DOWN)

        #show the circle, dots, lines, theta number and text

        self.play(GrowFromCenter(circle),run_time=2)
        self.play(Write(dot_on_circle),ShowCreation(line_to_sin_graph),Write(theta_text),Write(theta_number),
                  Write(dot_on_axis),Write(dot_at_center_of_circle),ShowCreation(line_of_circle_radius),run_time=2)
        self.wait()
        
        def update_line_to_sin_graph(obj):
            obj.put_start_and_end_on(dot_on_circle.point_from_proportion(0),dot_on_axis.point_from_proportion(0))
        
        def update_radius(obj):
            obj.put_start_and_end_on(dot_at_center_of_circle.get_center(),dot_on_circle.get_center())

        #add updaters

        line_to_sin_graph.add_updater(update_line_to_sin_graph)
        line_of_circle_radius.add_updater(update_radius).set_color(BLUE)

        #define intital values of time, rate, and dt

        self.t=0
        rate=0.1
        dt=0.01

        # define the time of rotation of dot_on_circle by function (update_point)
        # moving the point_on_axis on the graph sin(x) by a function (update_point_on_axis)
        # add updater to theta number
        
        def update_point(mob,dt):
            self.t += (dt*rate)
            mob.move_to(circle.point_from_proportion(self.t))
            def update_point_on_axis(obj):

       #move the point to an array-->x: origin of the curve + time t , y: value of dot on circle ups and downs, z=zero 
                obj.move_to(array([self.graph_origin[0]+self.t*(2*pi),dot_on_circle.point_from_proportion(0)[1],0]))
            dot_on_axis.add_updater(update_point_on_axis)   

        #add theta number updater

        theta_number.add_updater(lambda mob: mob.set_value((self.t *360)))
            
        #add updater    
        dot_on_circle.add_updater(update_point)

        self.wait(10+dt)

        #remove updaters

        line_to_sin_graph.remove_updater(update_line_to_sin_graph)
        line_of_circle_radius.remove_updater(update_radius)
        dot_on_circle.remove_updater(update_point)
        
        self.wait(2)
