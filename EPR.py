import manim as ma
from manim import Scene, config


class EPRQuotes(Scene):
    def construct(self):

        title = ma.Title("EPR's Paper").set_color(ma.BLUE)
        self.add(title)

        criterion_of_reality = ma.Text(
            '''"If, without in any way disturbing a system, we can predict with certainty
(i.e., with probability equal to unity) the value of a physical quantity,
then there exists an element of physical reality corresponding to this physical quantity."''',
            slant=ma.ITALIC,
        ).scale(0.5)

        self.play(ma.Write(criterion_of_reality))
        self.next_section()
        self.play(ma.FadeOut(criterion_of_reality))

        fund_concept = ma.Tex(
            r"""The fundamental concept of the theory is the concept of \textit{state}"""
        )

        self.play(ma.Write(fund_concept))

        self.next_section()
        self.play(fund_concept.animate.move_to(title.get_bottom() * 0.8).scale(0.7))

        observable = ma.MathTex(r"\psi' \equiv A \psi = a\psi")
        self.play(ma.Create(observable))
        self.play(observable.animate.next_to(fund_concept, ma.DOWN).shift(5 * ma.LEFT))

        self.next_section()

        define_psi = ma.MathTex(r"\psi = e^{(i/\hbar)p_0 x}").next_to(
            observable, buff=1
        )
        self.play(ma.Create(define_psi))

        self.next_section()

        p_operator = ma.MathTex(r"p = -\hbar i \frac{\partial}{\partial x}")
        self.play(ma.Create(p_operator))

        self.next_section()

        p_on_psi = ma.MathTex(
            r"\psi' = p \psi =-\hbar i \frac{\partial \psi}{\partial x} =", r"p_0 \psi"
        ).next_to(p_operator, ma.DOWN)
        self.play(ma.Create(p_on_psi))

        self.next_section()
        self.play(ma.Create(ma.SurroundingRectangle(define_psi)))
        self.play(ma.Create(ma.SurroundingRectangle(p_on_psi[-1])))

        self.next_section()

        conc_bullet = (
            ma.BulletedList(
                "Thus, momentum has certinaly the value $p_0$.",
                "So it has meaning to say that momentum of the particle in this state is real.",
                "If first realtion doesn't hold, we cannot speak of physical $A$ having a particular value.",
            )
            .scale(0.6)
            .set_color(ma.YELLOW)
            .next_to(
                p_on_psi,
                ma.DOWN,
                buff=0.7,
            )
        )

        self.play(ma.Write(conc_bullet[0]))
        self.next_section()
        self.play(ma.Write(conc_bullet[1]))
        self.play(ma.Write(conc_bullet[2]))
        self.next_section()

        # fade out all except title
        to_be_fade_out = {*self.mobjects} - {title}
        self.play(ma.FadeOut(*to_be_fade_out))

        x_on_psi = ma.MathTex(r"q \psi = x\psi", "=", r"a \psi")
        self.play(ma.Write(x_on_psi))
        self.next_section()
        self.play(ma.Transform(x_on_psi[1], ma.MathTex(r"\ne").next_to(x_on_psi[0])))

        self.play(x_on_psi.animate.next_to(title, ma.DOWN))

        prob_of_x = (
            ma.MathTex(
                r"P(a, b)", r"= \int_a^b \bar{\psi}\psi\, dx = \int_a^b dx = b-a"
            )
            .next_to(x_on_psi, ma.DOWN)
            .scale(0.7)
        )
        self.play(ma.Create(prob_of_x[0]))
        self.next_section()
        self.play(ma.Create(prob_of_x[1]))

        self.next_section()

        conc_position = (
            ma.BulletedList(
                "We see all values of the coordinte are equally probable.",
                "A definite value of the coordinate, for a particle in the this state is not predictable.",
                "For incompatible observables, the knowledge of one of them prevents the knowledge of the other one",
            )
            .scale(0.7)
            .next_to(prob_of_x, ma.DOWN)
        )

        self.play(ma.Write(conc_position[0]))
        self.next_section()
        self.play(ma.Write(conc_position[1]))
        self.next_section()
        self.play(ma.Write(conc_position[2]))
        self.next_section()

        # fade out all except title
        to_be_fade_out = {*self.mobjects} - {title}
        self.play(ma.FadeOut(*to_be_fade_out))

        EPR_result = (
            ma.VGroup(
                ma.Text(
                    "1. The quantum-mechanical description of reality given by the wave function is not compelete, or",
                    slant=ma.ITALIC,
                ),
                ma.Text(
                    "2. when the operators corresponding to two physical quantities do not commute\n"
                    "    the two quantifies cannot have simultaneous reality.",
                    slant=ma.ITALIC,
                ),
            )
            .arrange(ma.DOWN, 2, aligned_edge=ma.LEFT)
            .scale(0.5)
            .set_color(ma.YELLOW)
        )
        self.play(ma.Write(EPR_result.submobjects[0]))
        self.next_section()
        self.play(ma.Write(EPR_result.submobjects[1]))
        self.next_section()


config.background_color = ma.DARKER_GRAY


class EPRExperiment(Scene):
    def construct(self):
        title = ma.Title("EPR's Paper").set_color(ma.BLUE)
        self.add(title)
        self.play(ma.Transform(title, ma.Title("EPR's experiment").set_color(ma.BLUE)))
        self.wait()
        self.next_section()

        particle1 = ma.VGroup(
            ma.Circle(0.4, ma.RED, fill_opacity=1),
            ma.Tex("1"),
        )
        particle2 = ma.VGroup(
            ma.Circle(0.4, ma.RED, fill_opacity=1),
            ma.Tex("2"),
        )
        numberline = ma.NumberLine(None, 10)
        x_label = ma.MathTex("x").next_to(numberline)
        self.play(ma.Create(numberline), ma.Create(x_label))
        self.play(ma.Create(particle1))
        self.wait()

        # throw them apart
        arrow1 = ma.Arrow(ma.LEFT, ma.RIGHT, color=ma.GOLD).next_to(
            particle1, ma.UP + 0.5 * ma.RIGHT
        )
        arrow2 = ma.Arrow(ma.RIGHT, ma.LEFT, color=ma.GOLD).next_to(
            particle2, ma.UP + 0.5 * ma.LEFT
        )

        self.play(
            ma.FadeIn(arrow1),
            arrow1.animate.shift(ma.RIGHT * 3),
            particle1.animate.shift(ma.RIGHT * 3),
            ma.FadeIn(arrow2),
            arrow2.animate.shift(ma.LEFT * 3),
            particle2.animate.shift(ma.LEFT * 3),
        )

        p_1 = ma.MathTex("p_1").next_to(arrow1, ma.UP)
        p_2 = ma.MathTex("p_2").next_to(arrow2, ma.UP)
        x_1 = ma.MathTex("x_1").next_to(particle1.submobjects[0], ma.DOWN)
        x_2 = ma.MathTex("x_2").next_to(particle2.submobjects[0], ma.DOWN)
        self.play(
            ma.FadeIn(p_1),
            ma.FadeIn(p_2),
            ma.FadeIn(x_1),
            ma.FadeIn(x_2),
        )

        self.wait()
        self.next_section()

        cond = (
            ma.VGroup(
                ma.MathTex(r"x_2 = -x_1"),
                ma.MathTex(r"p_2 = - p_1"),
                ma.MathTex(r"\Delta{x_1}\Delta{p_1} \ge \hbar/2"),
            )
            .arrange(ma.DOWN)
            .shift(1.4 * ma.UP)
            .scale(0.7)
        )
        self.play(ma.Create(cond))
        self.next_section()

        line1 = (
            ma.BulletedList(
                "Measuring $x_2$ allows you to predict $x_1$, so $x_1$ becomes `real.'",
                "Measuring $p_2$ allows you to predict $p_1$, so $p_1$ becomes `real.'",
                "Reality for particle 1 depends on measurements made on particle 2.",
            )
            .scale(0.7)
            .shift(2.3 * ma.DOWN)
        )

        self.play(ma.Write(line1[0]))
        self.next_section()
        self.play(ma.Write(line1[1]))
        self.next_section()
        self.play(ma.Write(line1[2]))
        self.next_section()
