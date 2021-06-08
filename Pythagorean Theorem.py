from manimlib.imports import  *
from numpy import *

class PythagoreanTheorem(Scene):
    #www.youtube.com/c/radymahmoud
    def construct(self):
        title=TextMobject("Pythagorean ","Theorem")
        title.move_to(ORIGIN)
        title.scale(2)
        credit=TextMobject("By:"," Rady"," Mahmoud")
        credit.shift(DOWN)
        credit.set_color_by_tex_to_color_map({"By:":GREEN," Rady":RED," Mahmoud":BLUE})
        
        square=Square(color=YELLOW,fill_opacity=0.3).scale(2)
        
        square.shift(3*LEFT+UP)
        #triangle1
        longside=Line(np.array([-4,3,0]),np.array([-1,3,0]))
        longside.set_color(RED)
        
        shortside=Line(np.array([-1,3,0]),np.array([-1,2,0]))
        shortside.set_color(BLUE)
        
        diagonal=Line(np.array([-4,3,0]),np.array([-1,2,0]))
        diagonal.set_color(GREEN)
        
        #group triangle1
        group_triangle1=VGroup(longside,shortside,diagonal)

        #triangle1 text

        longsidetext1=TextMobject("b").set_color(RED)
        longsidetext1.next_to(longside,0.5*UP)

        shortsidetext1=TextMobject("a").set_color(BLUE)
        shortsidetext1.next_to(shortside,0.5*RIGHT)

        diagonaltext1=TextMobject("c").set_color(GREEN)
        diagonaltext1.next_to(diagonal,0.5*DOWN)

        triangle1_text=VGroup(longsidetext1,shortsidetext1,diagonaltext1)

        #triangle2
        group_triangle2=group_triangle1.copy().shift(RIGHT+2*DOWN)
        group_triangle2.rotate(-90*DEGREES)

        #triangle2 text

        longsidetext2=TextMobject("b").set_color(RED)
        longsidetext2.next_to(group_triangle2,0.5*RIGHT)

        shortsidetext2=TextMobject("a").set_color(BLUE)
        shortsidetext2.next_to(group_triangle2,0.5*DOWN)

        diagonaltext2=TextMobject("c").set_color(GREEN)
        diagonaltext2.next_to(group_triangle2,0.5*LEFT)

        triangle2_text=VGroup(longsidetext2,shortsidetext2,diagonaltext2)
        #triangle3
        group_triangle3=group_triangle2.copy().shift(2*LEFT+DOWN)
        group_triangle3.rotate(-90*DEGREES)

        #triangle3 text

        longsidetext3=TextMobject("b").set_color(RED)
        longsidetext3.next_to(group_triangle3,0.5*DOWN)

        shortsidetext3=TextMobject("a").set_color(BLUE)
        shortsidetext3.next_to(group_triangle3,0.5*LEFT)

        diagonaltext3=TextMobject("c").set_color(GREEN)
        diagonaltext3.next_to(group_triangle3,0.5*UP)

        triangle3_text=VGroup(longsidetext3,shortsidetext3,diagonaltext3)
        
        #triangle4
        group_triangle4=group_triangle3.copy().shift(LEFT+2*UP)
        group_triangle4.rotate(-90*DEGREES)

        #triangle4 text

        longsidetext4=TextMobject("b").set_color(RED)
        longsidetext4.next_to(group_triangle4,0.5*LEFT)

        shortsidetext4=TextMobject("a").set_color(BLUE)
        shortsidetext4.next_to(group_triangle4,0.5*UP)

        diagonaltext4=TextMobject("c").set_color(GREEN)
        diagonaltext4.next_to(group_triangle4,0.5*RIGHT)

        triangle4_text=VGroup(longsidetext4,shortsidetext4,diagonaltext4)

        self.play(ShowCreation(title),run_time=2)
        self.wait()
        self.play(Write(credit))
        self.wait()
        self.play(title.scale,0.3,title.shift,3.7*UP,credit.to_edge,DL,credit.scale,0.5)
        self.wait()
        self.play(Write(square))
        self.wait()
        self.play(FadeOut(square),Write(group_triangle1),Write(group_triangle2),Write(group_triangle3),Write(group_triangle4))
        self.play(Write(triangle1_text),Write(triangle2_text),Write(triangle3_text),Write(triangle4_text))
        self.wait(2)

        #Copy Main Square
        longside_copy=Line(np.array([-4,3,0]),np.array([-1,3,0]))
        longside_copy.set_color(RED)
        
        shortside_copy=Line(np.array([-1,3,0]),np.array([-1,2,0]))
        shortside_copy.set_color(BLUE)
        
        side_group1=VGroup(longside_copy,shortside_copy)

        side_group2=side_group1.copy().shift(RIGHT+2*DOWN)
        side_group2.rotate(-90*DEGREES)

        side_group3=side_group2.copy().shift(2*LEFT+DOWN)
        side_group3.rotate(-90*DEGREES)

        side_group4=side_group3.copy().shift(LEFT+2*UP)
        side_group4.rotate(-90*DEGREES)

        sum_sides=VGroup(side_group1,side_group2,side_group3,side_group4)

        #Main square text
        #1
        longsidetext1_copy=TextMobject("b").set_color(RED)
        longsidetext1_copy.next_to(longside_copy,0.5*UP)

        shortsidetext1_copy=TextMobject("a").set_color(BLUE)
        shortsidetext1_copy.next_to(shortside_copy,0.5*RIGHT)

        side1_text=VGroup(longsidetext1_copy,shortsidetext1_copy)
        #2
        longsidetext2_copy=TextMobject("b").set_color(RED)
        longsidetext2_copy.next_to(side_group2,0.5*RIGHT)

        shortsidetext2_copy=TextMobject("a").set_color(BLUE)
        shortsidetext2_copy.next_to(side_group2,0.5*DOWN)

        side2_text=VGroup(longsidetext2_copy,shortsidetext2_copy)
        #3
        longsidetext3_copy=TextMobject("b").set_color(RED)
        longsidetext3_copy.next_to(side_group3,0.5*DOWN)

        shortsidetext3_copy=TextMobject("a").set_color(BLUE)
        shortsidetext3_copy.next_to(side_group3,0.5*LEFT)

        side3_text=VGroup(longsidetext3_copy,shortsidetext3_copy)
        #4
        longsidetext4_copy=TextMobject("b").set_color(RED)
        longsidetext4_copy.next_to(side_group4,0.5*LEFT)

        shortsidetext4_copy=TextMobject("a").set_color(BLUE)
        shortsidetext4_copy.next_to(side_group4,0.5*UP)

        side4_text=VGroup(longsidetext4_copy,shortsidetext4_copy)
        #sum sides texts
        sum_sides_text=VGroup(side1_text,side2_text,side3_text,side4_text)
        sum_triangle_text=sum_sides_text.copy()

        #Play the Result

        self.play(sum_sides_text.shift,6*RIGHT,sum_sides.shift,6*RIGHT)
        self.wait(2)
        area_a=TextMobject("Main"," Square Area").scale(0.5)
        area_a[0].set_color(RED)
        area_a[1].set_color(BLUE)
        area_b=TextMobject("=").scale(0.5)
        area_c=TextMobject("Triangles"," Area").scale(0.5)
        area_c[0].set_color(RED)
        area_c[1].set_color(BLUE)
        area_d=TextMobject("+").scale(0.5)
        area_e=TextMobject("Interior Square Area").scale(0.5)
        area_e.set_color(GREEN)
        
        #                   0    1    2    3     4      5   6     7          8       9    10   11   12   13   14   15 
        formula=TexMobject(r"(",r"a",r"+",r"b",r")^2",r"=",r"4",r"(",r"\frac{1}{2}",r"a",r"b",r")",r"+",r"(",r"c",r")^2")
        formula.shift(3*DOWN)
        formula.set_color_by_tex_to_color_map({"a":BLUE,"b":RED,"c":GREEN})
        formula_copy=formula.copy()
        
        #Mention
        
        area_b.next_to(area_a,RIGHT)
        area_c.next_to(area_b,RIGHT)
        area_d.next_to(area_c,RIGHT)
        area_e.next_to(area_d,RIGHT)
        
        area=VGroup(area_a,area_b,area_c,area_d,area_e)
        area.shift(2*DOWN+2*LEFT)

        self.play(Write(area))
        self.wait()
        self.play(ReplacementTransform(sum_sides,formula[0]),ReplacementTransform(sum_sides_text,formula[4]),Write(formula[1]),
                  Write(formula[3]),Write(formula[2]),Write(formula[5]))
        self.wait(2)
        
        #Copy Inner Square
        #1
        diagonal_copy1=Line(np.array([-4,3,0]),np.array([-1,2,0]))
        diagonal_copy1.set_color(GREEN)
        #2
        diagonal_copy2=diagonal_copy1.copy().shift(RIGHT+2*DOWN)
        diagonal_copy2.rotate(-90*DEGREES)
        #3
        diagonal_copy3=diagonal_copy2.copy().shift(2*LEFT+DOWN)
        diagonal_copy3.rotate(-90*DEGREES)
        #4
        diagonal_copy4=diagonal_copy3.copy().shift(LEFT+2*UP)
        diagonal_copy4.rotate(-90*DEGREES)

        sum_diagonal=VGroup(diagonal_copy1,diagonal_copy2,diagonal_copy3,diagonal_copy4)

        #copy inner texts
        #1
        diagonaltext1_copy=TextMobject("c").set_color(GREEN)
        diagonaltext1_copy.next_to(diagonal_copy1,0.5*DOWN)
        #2
        diagonaltext2_copy=TextMobject("c").set_color(GREEN)
        diagonaltext2_copy.next_to(diagonal_copy2,0.5*LEFT)
        #3
        diagonaltext3_copy=TextMobject("c").set_color(GREEN)
        diagonaltext3_copy.next_to(diagonal_copy3,0.5*UP)
        #4
        diagonaltext4_copy=TextMobject("c").set_color(GREEN)
        diagonaltext4_copy.next_to(diagonal_copy4,0.5*RIGHT)

        sum_diagonal_text=VGroup(diagonaltext1_copy,diagonaltext2_copy,diagonaltext3_copy,diagonaltext4_copy)

        self.play(sum_diagonal.shift,6*RIGHT,sum_diagonal_text.shift,6*RIGHT)
        self.play(Write(formula[12]),ReplacementTransform(sum_diagonal,formula[13]),ReplacementTransform(sum_diagonal_text,formula[15]),Write(formula[14]))
        self.wait(2)

        #copy triangles
        #1

        group_triangle1_copy=group_triangle1.copy()
        #2
        group_triangle2_copy=group_triangle2.copy()
        #3
        group_triangle3_copy=group_triangle3.copy()
        #4
        group_triangle4_copy=group_triangle4.copy()

        sum_triangle=VGroup(group_triangle1_copy,group_triangle2_copy,group_triangle3_copy,group_triangle4_copy)
        #copy triangles text
        #from line 157 and cmmand in 158 --> sum_triangle_text=sum_sides_text.copy()

        self.play(sum_triangle.shift,6*RIGHT,sum_triangle_text.shift,6*RIGHT)

        self.play(ReplacementTransform(group_triangle1_copy,formula[6]))
        self.play(ReplacementTransform(group_triangle2_copy,formula[6]))
        self.play(ReplacementTransform(group_triangle3_copy,formula[6]))
        self.play(ReplacementTransform(group_triangle4_copy,formula[6]))

        self.play(ReplacementTransform(sum_triangle_text,formula[8]),Write(formula[7]),Write(formula[11]),Write(formula[9]),Write(formula[10]))
        
        self.play(group_triangle1.shift,6*RIGHT+DOWN,group_triangle2.shift,6*RIGHT+DOWN,
                  group_triangle3.shift,6*RIGHT+DOWN,group_triangle4.shift,6*RIGHT+DOWN
                  ,triangle1_text.shift,6*RIGHT+DOWN,triangle2_text.shift,6*RIGHT+DOWN
                  ,triangle3_text.shift,6*RIGHT+DOWN,triangle4_text.shift,6*RIGHT+DOWN,FadeOut(area))

        #                     0    1    2     3    4    5   6     7   8     9    10  11    12  13   14   15   16    17    18
        formula2=TexMobject(r"(",r"a",r"^2",r"+",r"b",r"^2",r"+",r"2",r"a",r"b",r")",r"=",r"2",r"a",r"b",r"+",r"(",r"c",r")^2")
        formula2.shift(4*LEFT)
        formula2.set_color_by_tex_to_color_map({"a":BLUE,"b":RED,"c":GREEN})

        # We can assign each element in the list with a color and gives us the same result but I personally prefer the previous command in line 265
        """
        #for a
        formula2[1].set_color(BLUE)
        formula2[8].set_color(BLUE)
        formula2[13].set_color(BLUE)
        #for b
        formula2[4].set_color(RED)
        formula2[9].set_color(RED)
        formula2[14].set_color(RED)
        #for c
        formula2[17].set_color(GREEN)
        """
        #group for detection
        formula_set1=VGroup(formula2[7],formula2[8],formula2[9])
        formula_set2=VGroup(formula2[12],formula2[13],formula2[14])
        
        self.play(ReplacementTransform(formula,formula2))
        self.play(formula_set1.shift,UP)
        self.play(formula_set2.shift,UP)
        self.play(FadeOut(formula_set1),FadeOut(formula_set2))
   
        self.wait()

        #                         0   1    2   3   4    5   6   7
        final_formula=TexMobject("a","^2","+","b","^2","=","c","^2")
        final_formula.shift(4*LEFT)
        #for a
        final_formula[0].set_color(BLUE)
        #for b
        final_formula[3].set_color(RED)
        #for c
        final_formula[6].set_color(GREEN)
        #for transform
        formula2_fade=VGroup(formula2[0],formula2[1],formula2[2],formula2[3],formula2[4],formula2[5],
                             formula2[6],formula2[10],formula2[11],formula2[15],formula2[16],formula2[17],formula2[18])

        self.play(ReplacementTransform(formula2_fade,final_formula))

        self.play(FadeOut(group_triangle1),group_triangle2.shift,3*LEFT+UP,
                  FadeOut(group_triangle3),FadeOut(group_triangle4)
                  ,FadeOut(triangle1_text),triangle2_text.shift,3*LEFT+UP
                  ,FadeOut(triangle3_text),FadeOut(triangle4_text),final_formula.shift,2*RIGHT,credit.move_to,
                  np.array([0,-3,0]),credit.scale,2)


        self.wait(2)
        #the squares
        square1=Square(side_length=1,fill_opacity=0.2,color=BLUE)
        square2=Square(side_length=3,fill_opacity=0.2,color=RED)
        square3=Square(side_length=(10)**0.5,fill_opacity=0.2,color=GREEN)
        square1.shift(1.5*RIGHT+1.5*DOWN)
        square2.shift(3.5*RIGHT+0.5*UP)
        square3.rotate((71.75605118+90)*DEGREES)
        square3.shift(UP)
        square_group=VGroup(square1,square2,square3)
        #texts
        square_text1=TexMobject("a^2",tex_to_color_map={"a^2":BLUE})
        square_text1.next_to(square1,ORIGIN)

        square_text2=TexMobject("b^2",tex_to_color_map={"b^2":RED})
        square_text2.next_to(square2,ORIGIN)

        square_text3=TexMobject("c^2",tex_to_color_map={"a^2":GREEN})
        square_text3.next_to(square3,ORIGIN)

        square_text=VGroup(square_text1,square_text2,square_text3)

        self.play(final_formula.shift,2*LEFT)
        self.play(ShowCreation(square1),ShowCreation(square2),ShowCreation(square3)
                  ,ReplacementTransform(triangle2_text,square_text),FadeOut(group_triangle2),run_time=2)
        self.play(final_formula.scale,1.2,final_formula.shift,0.25*LEFT,square_group.scale,1.1,square_text.scale,1.1)
        self.wait(5)
        self.play(FadeOut(final_formula),FadeOut(square_group),FadeOut(square_text))
        self.play(title.move_to,ORIGIN,title.scale,3,credit.shift,2*UP)
        self.wait(2)
        self.play(FadeOut(title),FadeOut(credit))
        self.wait()
        