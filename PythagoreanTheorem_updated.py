from manimlib.imports import  *
from numpy import *

class PythagoreanTheorem(Scene):
    #www.youtube.com/c/radymahmoud
    def Title(self):
        self.title=TextMobject("Pythagorean ","Theorem")
        self.title.move_to(ORIGIN)
        self.title.scale(2)
    def Square(self):
        self.square=Square(color=YELLOW,fill_opacity=0.3).scale(2)
        self.square.shift(3*LEFT+UP)
    def Triangle(self):
        #triangle1
        self.longside=Line(np.array([-4,3,0]),np.array([-1,3,0])).set_color(RED)
        self.shortside=Line(np.array([-1,3,0]),np.array([-1,2,0])).set_color(BLUE)
        self.diagonal=Line(np.array([-4,3,0]),np.array([-1,2,0])).set_color(GREEN)
        #Dots
        self.dots1=VGroup(Dot(np.array([-4,3,0])),Dot(np.array([-1,3,0])),Dot(np.array([-1,2,0])))
        #group triangle1
        self.group_triangle1=VGroup(self.longside,self.shortside,self.diagonal)

        #triangle1 text
        self.longsidetext1=TextMobject("b").set_color(RED)
        self.longsidetext1.next_to(self.longside,0.5*UP)

        self.shortsidetext1=TextMobject("a").set_color(BLUE)
        self.shortsidetext1.next_to(self.shortside,0.5*RIGHT)

        self.diagonaltext1=TextMobject("c").set_color(GREEN)
        self.diagonaltext1.next_to(self.diagonal,0.5*DOWN)
        #group triangle 1 text
        self.triangle1_text=VGroup(self.longsidetext1,self.shortsidetext1,self.diagonaltext1)
        
        #triangle2
        self.group_triangle2=self.group_triangle1.copy().shift(RIGHT+2*DOWN).rotate(-90*DEGREES)
        self.dots2=self.dots1.copy().shift(RIGHT+2*DOWN).rotate(-90*DEGREES)
        #triangle2 text

        self.longsidetext2=TextMobject("b").set_color(RED)
        self.longsidetext2.next_to(self.group_triangle2,0.5*RIGHT)

        self.shortsidetext2=TextMobject("a").set_color(BLUE)
        self.shortsidetext2.next_to(self.group_triangle2,0.5*DOWN)

        self.diagonaltext2=TextMobject("c").set_color(GREEN)
        self.diagonaltext2.next_to(self.group_triangle2,0.5*LEFT)
        #group triangle 2 text
        self.triangle2_text=VGroup(self.longsidetext2,self.shortsidetext2,self.diagonaltext2)
       
        #triangle3
        self.group_triangle3=self.group_triangle2.copy().shift(2*LEFT+DOWN).rotate(-90*DEGREES)
        self.dots3=self.dots2.copy().shift(2*LEFT+DOWN).rotate(-90*DEGREES)
        
        #triangle3 text
        self.longsidetext3=TextMobject("b").set_color(RED)
        self.longsidetext3.next_to(self.group_triangle3,0.5*DOWN)

        self.shortsidetext3=TextMobject("a").set_color(BLUE)
        self.shortsidetext3.next_to(self.group_triangle3,0.5*LEFT)

        self.diagonaltext3=TextMobject("c").set_color(GREEN)
        self.diagonaltext3.next_to(self.group_triangle3,0.5*UP)
        #group trianlge 3 text
        self.triangle3_text=VGroup(self.longsidetext3,self.shortsidetext3,self.diagonaltext3)
        
        #triangle4
        self.group_triangle4=self.group_triangle3.copy().shift(LEFT+2*UP).rotate(-90*DEGREES)
        self.dots4=self.dots3.copy().shift(LEFT+2*UP).rotate(-90*DEGREES)
        
        #triangle4 text
        self.longsidetext4=TextMobject("b").set_color(RED)
        self.longsidetext4.next_to(self.group_triangle4,0.5*LEFT)

        self.shortsidetext4=TextMobject("a").set_color(BLUE)
        self.shortsidetext4.next_to(self.group_triangle4,0.5*UP)

        self.diagonaltext4=TextMobject("c").set_color(GREEN)
        self.diagonaltext4.next_to(self.group_triangle4,0.5*RIGHT)
        #group triangle 4 text
        self.triangle4_text=VGroup(self.longsidetext4,self.shortsidetext4,self.diagonaltext4)
       
        #-->Group Triangles
        self.group_triangles=VGroup(self.group_triangle1,self.group_triangle2,self.group_triangle3,self.group_triangle4)
        #group dots
        self.group_dots=VGroup(self.dots1,self.dots2,self.dots3,self.dots4)
        #-->Group Triangles Copy
        self.group_triangles_copy=VGroup(self.group_triangle1.copy(),self.group_triangle2.copy(),
                                         self.group_triangle3.copy(),self.group_triangle4.copy())
        #-->Group Triangle Texts
        self.group_triangle_texts=VGroup(self.triangle1_text,self.triangle2_text,self.triangle3_text,self.triangle4_text)
        #Group Triangle Texts copy
        self.group_triangle_texts_copy=VGroup(self.triangle1_text[0:2].copy(),self.triangle2_text[0:2].copy(),
                                              self.triangle3_text[0:2].copy(),self.triangle4_text[0:2].copy())
        #copy main square sides and texts
        self.group_sides=VGroup()
        self.group_side_texts=VGroup()

        for i in range(4):
            self.group_sides=self.group_sides.add(self.group_triangles[i][0:2].copy())
            self.group_side_texts=self.group_side_texts.add(self.group_triangle_texts[i][0:2].copy())
            i+=1
        
        #Copy Interior Square of diagonals
       
        self.group_diagonals= VGroup()
        self.group_diagonal_texts=VGroup()
        for i in range(4): 
            self.group_diagonals=self.group_diagonals.add(self.group_triangles[i][2].copy())
            self.group_diagonal_texts=self.group_diagonal_texts.add(self.group_triangle_texts[i][2].copy())
            i=i+1
        #Draw squares on final triangle
    def Final_Triangle_Squares(self):
        self.squareb=Square(side_length=3,color=RED,fill_opacity=0.7).move_to(self.group_triangles[1][0]).align_to(self.group_triangles[1][0],LEFT)
        self.squarea=Square(side_length=1,color=BLUE,fill_opacity=0.7).move_to(self.group_triangles[1][1]).align_to(self.group_triangles[1][1],UP)
        self.squarec=Square(side_length=10**0.5,
                            color=GREEN,fill_opacity=0.7).move_to(self.group_triangles[1][2]).rotate(degrees(arctan2(3,1))*DEGREES).align_to(self.group_triangles[1][2],
                                                                                                                                                DOWN+RIGHT)
        self.group_final_squares=VGroup(self.squarea,self.squareb,self.squarec)

    def Equations(self):
        #                            0            1        2        3         4     5              6             
        self.area_text=TextMobject("Main"," Square Area ","="," Triangles"," Area ","+"," Interior Square Area").scale(0.5).shift(2*DOWN)
        self.area_text.set_color_by_tex_to_color_map({"Main":RED," Square Area ":BLUE," Triangles":RED," Area":BLUE," Interior Square Area":GREEN})
        
        
        #                         0    1    2    3     4     5   6    7          8        9    10   11   12   13   14   15 
        self.formula=TexMobject(r"(",r"a",r"+",r"b",r")^2",r"=",r"4",r"(",r"\frac{1}{2}",r"a",r"b",r")",r"+",r"(",r"c",r")^2")
        self.formula.shift(3*DOWN)
        self.formula.set_color_by_tex_to_color_map({"a":BLUE,"b":RED,"c":GREEN})

        #                          0    1    2     3    4    5   6     7   8     9    10   11   12   13   14   15   
        self.formula2=TexMobject(r"a",r"^2",r"+",r"b",r"^2",r"+",r"2",r"a",r"b",r"=",r"2",r"a",r"b",r"+",r"c",r"^2")
        self.formula2.shift(0.5*DOWN+4*LEFT)
        self.formula2.set_color_by_tex_to_color_map({"a":BLUE,"b":RED,"c":GREEN})

        #                              0   1    2   3   4    5   6   7
        self.final_formula=TexMobject("a","^2","+","b","^2","=","c","^2")
        self.final_formula.shift(0.5*DOWN+4*LEFT)
        self.final_formula.set_color_by_tex_to_color_map({"a":BLUE,"b":RED,"c":GREEN})
        #construct functions and play animations
    def construct(self):
        self.Title()
        self.play(ShowCreation(self.title),run_time=2)
        self.wait()
        self.play(self.title.scale,0.3,self.title.shift,3.7*UP)
        self.wait()
        self.Square()
        self.play(ShowCreation(self.square))
        self.Triangle()
        self.play(FadeOut(self.square),ShowCreation(self.group_triangles))
        self.play(FadeIn(self.group_dots))
        self.wait()
        self.play(Write(self.group_triangle_texts))
        self.wait()
        self.Equations()
        self.play(Write(self.area_text))
        
        self.play(self.group_sides.shift,6*RIGHT,self.group_side_texts.shift,6*RIGHT)
        self.wait()

        self.play(ReplacementTransform(self.group_side_texts[0][1],self.formula[1]),ReplacementTransform(self.group_side_texts[1][0],self.formula[3]))
        self.wait()
        self.play(FadeOut(self.group_side_texts))
        self.play(ReplacementTransform(self.group_sides,self.formula[0:6]))
        self.wait()

        for i in range(4): self.play(self.group_triangles_copy[i].shift,6*RIGHT,self.group_triangle_texts_copy[i].shift,6*RIGHT)
        i+=1
        self.play(ReplacementTransform(self.group_triangle_texts_copy[1][0],self.formula[9]),
                  ReplacementTransform(self.group_triangle_texts_copy[1][1],self.formula[10]),
                  Write(self.formula[7:9]),Write(self.formula[11]))
        self.play(FadeOut(self.group_triangle_texts_copy))

        for i in range(4): self.play(ReplacementTransform(self.group_triangles_copy[i],self.formula[6]))
        i+=1
        
        self.wait()
        self.play(self.group_diagonals.shift,6*RIGHT,self.group_diagonal_texts.shift,6*RIGHT)
        self.play(ReplacementTransform(self.group_diagonal_texts[0:2],self.formula[14]),Write(self.formula[12]))
        self.play(FadeOut(self.group_diagonal_texts))
        self.play(ReplacementTransform(self.group_diagonals,self.formula[13:16]))
        self.wait(2)
        self.play(FadeOut(self.area_text))
        self.play(self.group_triangles.shift,6*RIGHT+0.5*DOWN,self.group_triangle_texts.shift,6*RIGHT+0.5*DOWN,
                  self.group_dots.shift,6*RIGHT+0.5*DOWN,self.formula.shift,2.5*UP+4*LEFT)
        self.wait()
        self.play(ReplacementTransform(self.formula,self.formula2))
        self.play(self.formula2[6:9].shift,UP,self.formula2[10:13].shift,UP)
        self.play(FadeOut(self.formula2[6:9]),FadeOut(self.formula2[10:13]))
        self.wait()
        self.play(ReplacementTransform(self.formula2[0:6],self.final_formula[0:5]),
                          ReplacementTransform(self.formula2[9],self.final_formula[5]),
                          ReplacementTransform(self.formula2[13:16],self.final_formula[6:8]))
        for f in range(4):
            if f!=1:
                self.play(FadeOut(self.group_triangles[f]),FadeOut(self.group_triangle_texts[f]),FadeOut(self.group_dots[f]))
        f+=1
        
        self.play(self.group_triangles[1].shift,2*LEFT,self.group_triangle_texts[1].shift,2*LEFT,self.group_dots[1].shift,2*LEFT)
        self.wait()
        self.Final_Triangle_Squares()
        self.play(Write(self.group_final_squares),FadeOut(self.group_triangles[1]),FadeOut(self.group_dots[1]))
        self.wait()
        a=self.final_formula[0:2].copy().move_to(self.group_final_squares[0],ORIGIN)
        b=self.final_formula[3:5].copy().move_to(self.group_final_squares[1],ORIGIN)
        c=self.final_formula[6:8].copy().move_to(self.group_final_squares[2],ORIGIN)
        group_final_squares_texts=VGroup(b,a,c)
        for i in range(3): self.play(ReplacementTransform(self.group_triangle_texts[1][i],group_final_squares_texts[i]))
        i+=1
        for i in range(3): self.play(ReplacementTransform(self.final_formula[3*i:i+2*(i+1)].copy(),group_final_squares_texts[(2**(i+1)-((2**i-1)+(i+1)))*(1-i)**i]))
        i+1
        self.wait()
        self.play(group_final_squares_texts.scale,1.1,group_final_squares_texts.shift,0.1*DOWN,
                  self.group_final_squares.scale,1.1,self.final_formula.scale,1.1)
        self.wait(3)
        self.play(FadeOut(self.group_final_squares),FadeOut(a),FadeOut(b),FadeOut(c),FadeOut(self.final_formula),
                  self.title.scale,3,self.title.move_to,ORIGIN)
        self.wait(3)
        self.play(FadeOut(self.title))
        self.wait(3)