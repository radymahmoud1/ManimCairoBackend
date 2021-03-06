from manimlib.imports import *
from numpy import *
from math import *

class sin2x(Scene):
    def construct(self):
        # Defining each line and letter and showing them with self.play command
        title0=TexMobject(r"Proof").move_to(array([0,1,0]))
        title1=TexMobject(r"\sin(\alpha+\theta)|\sin(2 x)").next_to(title0,DOWN)
        title2=TexMobject(r"\cos(\alpha+\theta)|\cos(2 x)").next_to(title1,DOWN)
        title3=TexMobject(r"\tan(\alpha+\theta)|\tan(2 x)").next_to(title2,DOWN)
        gtitle=VGroup(title1,title2,title3)
        credit=TextMobject("By: Rady Mahmoud").scale(0.5).to_corner(DL,buff=0.1)
        self.play(Write(title0),Write(credit),run_time=2)
        self.play(Write(gtitle),run_time=2)
        self.wait(5)
        self.play(FadeOut(title0),FadeOut(gtitle))
        self.wait()
        circ = Circle(radius = 3,color=RED)
        fa= Line(ORIGIN,array([3,0,0]))
        f=TextMobject("f").scale(0.7).next_to(fa,RIGHT)
        a=TextMobject("a").scale(0.7).next_to(ORIGIN,LEFT)
        ca= fa.copy().rotate(30*DEGREES,about_point=ORIGIN)
        ea= fa.copy().rotate(45*DEGREES,about_point=ORIGIN)
        cb= Line(array([3*cos(30*DEGREES),0,0]),array([3*cos(30*DEGREES),3*sin(30*DEGREES),0]))
        kd= Line(array([3*cos(45*DEGREES),0,0]),array([3*cos(45*DEGREES),3*sin(30*DEGREES),0]))
        ek=Line(array([3*cos(45*DEGREES),3*sin(30*DEGREES),0]),array([3*cos(45*DEGREES),3*sin(45*DEGREES),0]))
        
        ck=DashedLine(array([3*cos(30*DEGREES),3*sin(30*DEGREES),0]),array([3*cos(45*DEGREES),3*sin(30*DEGREES),0]))
        
        c=TextMobject("c").scale(0.7).next_to(ck,RIGHT)
        b=TextMobject("b").scale(0.7).next_to(cb,DOWN)
        ed= Line(array([3*cos(45*DEGREES),0,0]),array([3*cos(45*DEGREES),3*sin(45*DEGREES),0]))
        da= Line(array([0,0,0]),array([3*cos(45*DEGREES),0,0]))
        e=TextMobject("e").scale(0.7).next_to(ed,UP)
        d=TextMobject("d").scale(0.7).next_to(ed,DOWN)
        l1=Line(array([0,0,0]),array([0,0.2,0]))
        l2=Line(array([0,0.2,0]),array([0.2,0.2,0]))
        right_angle =VGroup(l1,l2)
        angle1=right_angle.copy().move_to(array([3*cos(45*DEGREES)-0.1,0.1,0]))
        angle2=right_angle.copy().move_to(array([3*cos(30*DEGREES)-0.1,0.1,0]))
        self.play(ShowCreation(circ),run_time=2)
        self.wait()
        self.play(ShowCreation(fa),ShowCreation(ca),ShowCreation(ea),run_time=2)
        self.wait()
        self.play(Write(a),Write(c),Write(e),Write(f),run_time=2)
        self.play(ShowCreation(cb),ShowCreation(ed),run_time=2)
        self.wait()
        self.play(Write(d),Write(b),run_time=2)
        self.wait()
        self.play(ShowCreation(angle1),ShowCreation(angle2),run_time=2)
        self.wait()
        ce=Line(array([3*cos(45*DEGREES),3*sin(45*DEGREES),0]),array([3*cos(30*DEGREES),3*sin(30*DEGREES),0]))
        bd=Line(array([3*cos(30*DEGREES),0,0]),array([3*cos(45*DEGREES),0,0]))
        k= TextMobject("k").scale(0.7).next_to(ck,LEFT).shift(0.1*RIGHT)
        angle3=right_angle.copy().move_to(array([3*cos(30*DEGREES)-0.16,3*sin(30*DEGREES)+0.035,0])).rotate(30*DEGREES)
        angle4=right_angle.copy().move_to(array([3*cos(45*DEGREES)+0.05,3*sin(30*DEGREES)+0.05,0])).scale(0.5).rotate(-90*DEGREES)
        self.play(ShowCreation(ce),ShowCreation(angle3),run_time=2)
        self.play(ShowCreation(ck),Write(k),run_time=2)
        self.wait()
        arc1 = Arc(radius=1.5,arc_center=ORIGIN,start_angle=0, angle=30*DEGREES).set_color(RED)
        arc2 = Arc(radius=1.5,arc_center=ORIGIN,start_angle=30*DEGREES, angle=15*DEGREES).set_color(BLUE)
        theta=TexMobject(r"\theta",color=RED).scale(0.5).next_to(arc1,LEFT).shift(0.1*(DOWN))
        alpha=TexMobject(r"\alpha",color=BLUE).scale(0.5).next_to(arc2,LEFT).shift(0.2*(DOWN+RIGHT))
        theta_copy=theta.copy().move_to(array([3*cos(45*DEGREES)+0.1,3*sin(30*DEGREES)+0.3,0]))
        self.play(ShowCreation(arc1),ShowCreation(arc2),ShowCreation(angle4),Write(theta),Write(alpha),run_time=2)
        self.wait()
        self.play(ReplacementTransform(theta.copy(),theta_copy),run_time=2)
        self.wait()
        ba= Line(ORIGIN,array([3*cos(30*DEGREES),0,0]))

        # grouping every thing for making everythinh easier to call or mension on screen

        #             0  1  2  3  4  5  6 7 8 9 10 11 12  13     14     15     16     17   18   19    20       21     22 23 24 25
        group=VGroup(ba,ca,ea,cb,ed,ce,ck,a,b,c,d, e, k, angle1,angle2,angle3,angle4,arc1,arc2,theta,alpha,theta_copy,bd,kd,da,ek)
       
        self.play(FadeOut(circ),run_time=2)
        self.wait()
        self.play(FadeOut(f),ReplacementTransform(fa,ba),run_time=2)
        self.wait()
        self.play(group.scale,1.5,group.move_to,array([4,1,0]),run_time=2)
        self.wait()
        self.play(ck.set_color,PURPLE,bd.set_color,PURPLE,run_time=2)
        self.wait()
        eq1=TexMobject(r"\overline{c b} = \overline{k d}").scale(0.7).move_to(array([-6,3,0]))
        self.play(Write(eq1),run_time=2)
        self.wait()
        self.play(cb.set_color,ORANGE,kd.set_color,ORANGE,run_time=2)
        self.wait()
        eq2=TexMobject(r"\overline{c k} = \overline{b d}").scale(0.7).move_to(array([-6,2.5,0]))
        self.play(Write(eq2),run_time=2)
        self.wait()
        group_2=VGroup(eq1,eq2)
        rect1=SurroundingRectangle(mobject=group_2,color=YELLOW)
        self.play(ShowCreation(rect1),run_time=2)
        self.wait()
        self.play(ck.set_color,WHITE,FadeOut(bd),cb.set_color,WHITE,FadeOut(kd),run_time=1)
        cb.set_color(WHITE)
        kd.set_color(WHITE)
        ck.set_color(WHITE)
        bd.set_color(WHITE)
        
        tr0=TexMobject(r"\vartriangle (ade) ").scale(0.7).move_to(array([-3,3,0]))
        eq3=TexMobject(r"\sin(\alpha + \theta) = \frac{\overline{ed}}{\overline{ea}}").scale(0.7).move_to(array([-3,2,0]))
        eq4=TexMobject(r"\cos(\alpha + \theta) = \frac{\overline{da}}{\overline{ea}}").scale(0.7).move_to(array([-3,1,0]))
        self.play(Write(tr0),group[2].set_color,GREEN,group[4].set_color,GREEN,group[24].set_color,GREEN,group[25].set_color,GREEN,run_time=3)
        group2=VGroup(tr0,eq3,eq4)
        rect2=SurroundingRectangle(mobject=group2,color=YELLOW)
        self.play(Write(eq3),run_time=2)
        self.wait()
        self.play(Write(eq4),run_time=2)
        self.play(ShowCreation(rect2),run_time=2)
        self.wait()
        group[24].set_color(WHITE)
        self.play(group[2].set_color,WHITE,group[4].set_color,WHITE,FadeOut(group[24]),group[25].set_color,WHITE,run_time=2)
        self.wait()
        tr1=TexMobject(r"\vartriangle (abc) ").scale(0.7).move_to(array([-0.5,3,0]))
        self.play(Write(tr1),group[0].set_color,RED,group[1].set_color,RED,group[3].set_color,RED,run_time=2)
        eq5=TexMobject(r"\sin(\theta) = \frac{\overline{cb}}{\overline{ca}}").scale(0.7).move_to(array([-0.5,2,0]))
        eq6=TexMobject(r"\cos(\theta) = \frac{\overline{ba}}{\overline{ca}}").scale(0.7).move_to(array([-0.5,1,0]))
        group3=VGroup(tr1,eq5,eq6)
        rect3=SurroundingRectangle(mobject=group3,color=YELLOW)
        self.play(Write(eq5),run_time=2)
        self.wait()
        self.play(Write(eq6),run_time=2)
        self.play(ShowCreation(rect3),run_time=2)
        self.wait()

        self.play(group[0].set_color,WHITE,group[1].set_color,WHITE,group[3].set_color,WHITE,run_time=2)
        self.wait()
        tr2=TexMobject(r"\vartriangle (ace) ").scale(0.7).move_to(array([-5.8,1,0]))
        self.play(Write(tr2),group[1].set_color,BLUE,group[2].set_color,BLUE,group[5].set_color,BLUE,run_time=2)
        eq7=TexMobject(r"\sin(\alpha) = \frac{\overline{ce}}{\overline{ea}}").scale(0.7).move_to(array([-5.8,0,0]))
        eq8=TexMobject(r"\cos(\alpha) = \frac{\overline{ca}}{\overline{ea}}").scale(0.7).move_to(array([-5.8,-1,0]))
        group4=VGroup(tr2,eq7,eq8)
        rect4=SurroundingRectangle(mobject=group4,color=YELLOW)
        self.play(Write(eq7),run_time=2)
        self.wait()
        self.play(Write(eq8),run_time=2)
        self.play(ShowCreation(rect4),run_time=2)
        self.wait()

        
        self.play(group[1].set_color,WHITE,group[2].set_color,WHITE,group[5].set_color,WHITE,run_time=2)
        self.wait()
        tr3=TexMobject(r"\vartriangle (cke) ").scale(0.7).move_to(array([1.7,3,0]))
        self.play(Write(tr3),group[5].set_color,YELLOW,group[6].set_color,YELLOW,group[25].set_color,YELLOW,run_time=2)
        eq9=TexMobject(r"\cos(\theta) = \frac{\overline{ek}}{\overline{ce}}").scale(0.7).move_to(array([1.7,2,0]))
        eq10=TexMobject(r"\sin(\theta) = \frac{\overline{ck}}{\overline{ce}}").scale(0.7).move_to(array([1.7,1,0]))
        group5=VGroup(tr3,eq9,eq10)
        rect5=SurroundingRectangle(mobject=group5,color=YELLOW)
        self.play(Write(eq9),run_time=2)
        self.wait()
        self.play(Write(eq10),run_time=2)
        self.play(ShowCreation(rect5),run_time=2)
        self.wait()
        self.play(Write(tr3),group[5].set_color,WHITE,group[6].set_color,WHITE,group[25].set_color,WHITE,run_time=2)

        # Writing equations using latex commands

        feq0=TexMobject(r"\sin(\alpha + \theta) = \frac{\overline{ed}}{\overline{ea}}").scale(0.7).move_to(array([-1,-1.5,0]))
        feq1=TexMobject(r"\sin(\alpha + \theta) = \frac{\overline{ek}+\overline{kd}}{\overline{ea}}").scale(0.7).move_to(array([-1,-1.5,0]))
        feq2=TexMobject(r"\sin(\alpha + \theta) = \frac{\overline{ek}+\overline{cb}}{\overline{ea}}").scale(0.7).move_to(array([-1,-1.5,0]))
        feq3=TexMobject(r"\sin(\alpha + \theta) = \frac{\overline{ce}\cos(\theta)+\overline{ca}\sin(\theta)}{\overline{ea}}").scale(0.7).move_to(array([-1,-1.5,0]))
        #feq4=TexMobject(r"\sin(\alpha + \theta) = \frac{\overline{ea}\sin(\alpha)\cos(\theta)+\overline{ea}\cos(\alpha)\sin(\theta)}{\overline{ea}}").scale(0.7).move_to(array([-1,-1.5,0]))
        feq5=TexMobject(r"\sin(\alpha + \theta) = ",r"\frac{\overline{ea}\sin(\alpha)\cos(\theta)+\overline{ea}\cos(\alpha)\sin(\theta)}{\overline{ea}}").scale(0.7).move_to(array([-1,-1.5,0]))
        feq6=TexMobject(r"\sin(\alpha + \theta) = \sin(\alpha)\cos(\theta)+\cos(\alpha)\sin(\theta)}}").scale(0.7).move_to(array([-1,-1.5,0]))
        feq7=TexMobject(r"\textbf{if}\ \alpha = \theta = x}").scale(0.7).move_to(array([0,-2,0]))
        feq8=TexMobject(r"\sin(x + x) = \sin(x)\cos(x)+\cos(x)\sin(x)}}").scale(0.7).move_to(array([0,-2.5,0]))
        feq9=TexMobject(r"\sin(2 x) = 2\sin(x)\cos(x)}").scale(0.7).move_to(array([0,-2.5,0]))
        self.play(Write(feq0),run_time=3)
        self.wait(5)
        self.play(ReplacementTransform(feq0,feq1),run_time=3)
        self.wait(5)
        self.play(eq1.scale,2,run_time=2)
        self.play(eq1.scale,0.5,run_time=2)
        self.play(ReplacementTransform(feq1,feq2),run_time=3)
        self.play(eq9.set_color,YELLOW,eq5.set_color,YELLOW,run_time=2)
        self.wait(3)
        self.play(ReplacementTransform(feq2,feq3),run_time=3)
        self.play(eq7.set_color,YELLOW,eq8.set_color,YELLOW,run_time=2)
        self.wait(3)
        self.play(ReplacementTransform(feq3,feq5),run_time=3)
        self.wait(5)
        self.play(feq5[1][0:3].set_color,RED,feq5[1][16:19].set_color,RED,feq5[1][32:35].set_color,RED,run_time=3)
        self.play(FadeOut(feq5[1][0:3]),FadeOut(feq5[1][16:19]),FadeOut(feq5[1][32:35]))
        self.wait(5)
        rect6=SurroundingRectangle(mobject=feq6,color=YELLOW)
        self.play(ReplacementTransform(feq5[0],feq6),ReplacementTransform(feq5[1][3:16],feq6),ReplacementTransform(feq5[1][19:32],feq6),run_time=3)
        self.wait()
        self.play(ShowCreation(rect6))
        self.wait(5)
        self.play(Write(feq7),run_time=3)
        self.wait(5)        
        self.play(Write(feq8),run_time=3)
        self.wait(5)
        self.play(ReplacementTransform(feq8,feq9),run_time=3)
        rect7=SurroundingRectangle(mobject=feq9,color=YELLOW)
        self.play(ShowCreation(rect7))
        self.wait(5)
        g2=VGroup(group2,rect2)
        g3=VGroup(group3,rect3)
        g4=VGroup(group4,rect4)
        g5=VGroup(group5,rect5)
        g6=VGroup(feq6,rect6)
        g7=VGroup(feq9,rect7)
        self.play(g2[0].set_color,WHITE,g3[0].set_color,WHITE,g4[0].set_color,WHITE,g5[0].set_color,WHITE)
        self.play(g2.scale,0.8,g2.next_to,rect1,RIGHT)
        self.play(g3.scale,0.8,g3.next_to,g2[1],RIGHT)
        self.play(g4.scale,0.8,g4.next_to,g3[1],RIGHT)
        self.play(g5.scale,0.8,g5.next_to,g4[1],RIGHT)
        self.play(group.shift,0.5*(RIGHT+UP))
        self.play(FadeOut(feq7))
        self.play(g6.scale,0.8,g6.move_to,array([-4.5,1,0]))
        self.play(g7.scale,0.8,g7.next_to,g6,DOWN)

        feq10=TexMobject(r"\cos(\alpha + \theta) = \frac{\overline{da}}{\overline{ea}}").scale(0.7).move_to(array([-1,-1.5,0]))
        feq11=TexMobject(r"\cos(\alpha + \theta) = \frac{\overline{ba}-\overline{bd}}{\overline{ea}}").scale(0.7).move_to(array([-1,-1.5,0]))
        feq12=TexMobject(r"\cos(\alpha + \theta) = \frac{\overline{ba}-\overline{ck}}{\overline{ea}}").scale(0.7).move_to(array([-1,-1.5,0]))
        feq13=TexMobject(r"\cos(\alpha + \theta) = \frac{\overline{ca}\cos(\theta)-\overline{ce}\sin(\theta)}{\overline{ea}}").scale(0.7).move_to(array([-1,-1.5,0]))
        feq14=TexMobject(r"\cos(\alpha + \theta) = ",r"\frac{\overline{ea}\cos(\alpha)\cos(\theta)-\overline{ea}\sin(\alpha)\sin(\theta)}{\overline{ea}}").scale(0.7).move_to(array([-1,-1.5,0]))
        feq15=TexMobject(r"\cos(\alpha + \theta) = \cos(\alpha)\cos(\theta)-\sin(\alpha)\sin(\theta)").scale(0.7).move_to(array([-1,-1.5,0]))
        feq16=TexMobject(r"\textbf{if}\ \alpha = \theta = x}").scale(0.7).move_to(array([0,-2,0]))
        feq17=TexMobject(r"\cos(x + x) = \cos(x)\cos(x)+\sin(x)\sin(x)}}").scale(0.7).move_to(array([0,-2.5,0]))
        feq18=TexMobject(r"\cos(2 x) = \cos^2(x)-\sin^2(x)}").scale(0.7).move_to(array([0,-2.5,0]))
        feq18_copy=feq18.copy().move_to(array([1,-0.5,0]))
        feq19=TexMobject(r"\because \sin^2(\theta)+\cos^2(\theta) = (\frac{\overline{cb}}{\overline{ca}})^2+(\frac{\overline{ba}}{\overline{ca}})^2").scale(0.7).move_to(array([0,-2.5,0]))
        feq20=TexMobject(r"\because \sin^2(\theta)+\cos^2(\theta) = \frac{\overline{cb}^2+\overline{ba}^2}{\overline{ca}^2}").scale(0.7).move_to(array([1,-1.5,0]))
        feq21=TexMobject(r"\because \sin^2(\theta)+\cos^2(\theta) = \frac{\overline{cb}^2+\overline{ba}^2}{\overline{ca}^2}").scale(0.7).move_to(array([1,-1.5,0]))
        note=TexMobject(r"from\ Pythagorean\ theorem\ \overline{cb}^2 + \overline{ba}^2 = \overline{ca}^2}").scale(0.7).next_to(feq21,DOWN)
        note2=TexMobject(r"if\ \theta = x").scale(0.7).next_to(feq21,DOWN)

        feq22=TexMobject(r"\therefore \sin^2(\theta)+\cos^2(\theta) = \frac{\overline{ca}^2}{\overline{ca}^2}").scale(0.7).next_to(note,DOWN)
        feq23=TexMobject(r"\therefore \sin^2(\theta)+\cos^2(\theta) = 1").scale(0.7).next_to(note,DOWN)
        feq23_1=TexMobject(r"\therefore \sin^2(x)+\cos^2(x) = 1").scale(0.7).next_to(note,DOWN)
        feq24=TexMobject(r"\cos^2(\theta) = 1 - \sin^2(\theta)").scale(0.7).next_to(feq18_copy,RIGHT+DOWN)
        feq25=TexMobject(r"\sin^2(\theta) = 1 - \cos^2(\theta)").scale(0.7).next_to(feq24,DOWN)
        feq26=TexMobject(r"\cos(2 x) = \cos^2(x)-\sin^2(x)}").scale(0.7).next_to(feq18_copy,2*DOWN)
        feq27=TexMobject(r"\cos(2 x) = 1 - \sin^2(\theta)-\sin^2(x)}").scale(0.7).next_to(feq26,1.5*DOWN)
        feq28=TexMobject(r"\cos(2 x) = \cos^2(x) - (1 - \cos^2(\theta))}").scale(0.7).next_to(feq27,1.5*DOWN)
        feq29=TexMobject(r"\cos(2 x) = 1 - 2\sin^2(\theta)}").scale(0.7).next_to(feq26,DOWN)
        feq30=TexMobject(r"\cos(2 x) = \cos^2(x) + 1 + \cos^2(\theta)}").scale(0.7).next_to(feq27,DOWN)
        feq31=TexMobject(r"\cos(2 x) = 2\cos^2(x) + 1}").scale(0.7).next_to(feq27,DOWN)
        
        self.play(Write(feq10),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(feq10,feq11),run_time=2)
        self.wait(2)
        self.play(eq2.scale,2,run_time=2)
        self.play(eq2.scale,0.5,run_time=2)
        self.play(ReplacementTransform(feq11,feq12),run_time=2)
        self.play(g3[0][2].set_color,YELLOW,g5[0][2].set_color,YELLOW,run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(feq12,feq13),run_time=2)
        self.play(g4[0][1].set_color,YELLOW,g4[0][2].set_color,YELLOW,run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(feq13,feq14),run_time=3)
        self.wait(2)
        self.play(feq14[1][0:3].set_color,RED,feq14[1][16:19].set_color,RED,feq14[1][32:35].set_color,RED,run_time=2)
        self.play(FadeOut(feq14[1][0:3]),FadeOut(feq14[1][16:19]),FadeOut(feq14[1][32:35]))
        self.wait(2)
        rect8=SurroundingRectangle(mobject=feq15,color=YELLOW)
        self.play(ReplacementTransform(feq14[0],feq15),ReplacementTransform(feq14[1][3:16],feq15),ReplacementTransform(feq14[1][19:32],feq15),run_time=2)
        self.wait()
        self.play(ShowCreation(rect8))
        self.wait(2)
        self.play(Write(feq16),run_time=2)
        self.wait(2)        
        self.play(Write(feq17),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(feq17,feq18),run_time=2)
        rect9=SurroundingRectangle(mobject=feq18,color=YELLOW)
        self.play(ShowCreation(rect9))
        self.wait(2)
        self.play(FadeOut(feq16))
        self.play(g3[0][2].set_color,WHITE,g5[0][2].set_color,WHITE,g4[0][1].set_color,WHITE,g4[0][2].set_color,WHITE,run_time=2)

        g8=VGroup(feq15,rect8)
        g9=VGroup(feq18,rect9)
        
        self.play(g8.scale,0.8,g8.next_to,g7,DOWN)
        self.play(g9.scale,0.8,g9.next_to,g8,DOWN)

        self.play(Write(feq18_copy))
        self.play(Write(feq19),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(feq19,feq20),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(feq20,feq21),run_time=2)
        self.wait(2)
        self.play(Write(note),run_time=2)
        self.wait(2)
        self.play(Write(feq22),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(feq22,feq23),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(note,note2),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(feq23,feq23_1),run_time=2)
        self.wait(2)
        self.play(FadeOut(feq21),FadeOut(note2),feq23_1.next_to,feq18_copy,DOWN)
        self.wait(2)
        
        self.play(Write(feq24),Write(feq25),run_time=2)
        self.wait(2)
        self.play(feq24.set_color,YELLOW, Write(feq27),feq27.set_color,YELLOW,run_time=2)
        self.play(feq25.set_color,RED, Write(feq28),feq28.set_color,RED,run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(feq27,feq29))
        rect10=SurroundingRectangle(mobject=feq29,color=YELLOW)
        self.play(ShowCreation(rect10))
        self.wait(2)
        self.play(ReplacementTransform(feq28,feq30))
        self.wait(2)
        self.play(ReplacementTransform(feq30,feq31))
        rect11=SurroundingRectangle(mobject=feq31,color=YELLOW)
        self.play(ShowCreation(rect11))
        self.wait(2)
        g10=VGroup(feq29,rect10)
        g11=VGroup(feq31,rect11)
        self.play(g10.scale,0.8,g10.next_to,g9,DOWN)
        self.play(g11.scale,0.8,g11.next_to,g10,DOWN)
        self.play(FadeOut(feq18_copy),FadeOut(feq24),FadeOut(feq25),FadeOut(feq23_1),run_time=2)
        self.wait(2)
        
        feq32=TexMobject(r"\tan(\alpha + \theta) = \frac{\sin(\alpha + \theta)}{\cos(\alpha + \theta)}").scale(0.7).move_to(array([1,-2,0]))
        feq33=TexMobject(r"\tan(\alpha + \theta) = \frac{\sin(\alpha)\cos(\theta)+\cos(\alpha)\sin(\theta)}{\cos(\alpha)\cos(\theta)-\sin(\alpha)\sin(\theta)}").scale(0.7).move_to(array([1,-2,0]))
        note3=TexMobject(r"\cross\ \frac{\frac{1}{\cos(\alpha)\cos(\theta)}}{\frac{1}{\cos(\alpha)\cos(\theta)}}").scale(0.5).next_to(feq33,RIGHT)
        feq34=TexMobject(r"\tan(\alpha + \theta) = \frac{\frac{\sin(\alpha)\cos(\theta)}{\cos(\alpha)\cos(\theta)}+\frac{\cos(\alpha)\sin(\theta)}{\cos(\alpha)\cos(\theta)}}{\frac{\cos(\alpha)\cos(\theta)}{\cos(\alpha)\cos(\theta)}-\frac{\sin(\alpha)\sin(\theta)}{\cos(\alpha)\cos(\theta)}}").scale(0.7).move_to(array([1,-2,0]))
        feq35=TexMobject(r"\tan(\alpha + \theta) = \frac{\frac{\sin(\alpha)}{\cos(\alpha)}+\frac{\sin(\theta)}{\cos(\theta)}}{1-\tan(\alpha)\tan(\theta)}").scale(0.7).move_to(array([1,-2,0]))
        feq36=TexMobject(r"\tan(\alpha + \theta) = \frac{\tan(\alpha)+\tan(\theta)}{1-\tan(\alpha)\tan(\theta)}").scale(0.7).move_to(array([1,-2,0]))
        note4=TexMobject(r"if\ \alpha = \theta = x").scale(0.7).next_to(feq36,RIGHT)
        feq37=TexMobject(r"\tan(x + x) = \frac{\tan(x)+\tan(x)}{1-\tan(x)\tan(x)}").scale(0.7).next_to(feq36,DOWN)
        feq38=TexMobject(r"\tan(2 x) = \frac{2 \tan(x)}{1-\tan^2(x)}").scale(0.7).next_to(feq36,DOWN)

        self.play(Write(feq32),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(feq32,feq33),run_time=2)
        self.wait(2)
        self.play(Write(note3),run_time=2)
        self.wait(2)
        self.play(FadeOut(note3),run_time=2)
        self.play(ReplacementTransform(feq33,feq34),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(feq34,feq35),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(feq35,feq36),run_time=2)
        rect12=SurroundingRectangle(mobject=feq36,color=YELLOW)
        self.play(ShowCreation(rect12))
        self.wait(2)
        self.play(Write(note4),run_time=2)
        self.wait(2)
        self.play(Write(feq37),run_time=2)
        self.wait(3)
        self.play(ReplacementTransform(feq37,feq38),run_time=2)
        rect13=SurroundingRectangle(mobject=feq38,color=YELLOW)
        self.play(ShowCreation(rect13),FadeOut(note4))
        g12=VGroup(feq36,rect12)
        g13=VGroup(feq38,rect13)
        self.wait(2)
        self.play(g12.scale,0.8,g12.next_to,g6,RIGHT)
        self.play(g13.scale,0.8,g13.next_to,g12,DOWN)
        self.wait(5)
        self.play(FadeOut(group),FadeOut(g2),FadeOut(group_2),FadeOut(g3),FadeOut(g4),FadeOut(g5),FadeOut(rect1),
                  FadeOut(g6),FadeOut(g7),FadeOut(g8),FadeOut(g9),FadeOut(g10),FadeOut(g11),FadeOut(g12),FadeOut(g13),FadeOut(feq6),
                  FadeOut(feq9),run_time=3)
        statement=TextMobject("BE CURIOUS").scale(2)
        self.play(FadeIn(statement),run_time=3)
        self.wait(5)
