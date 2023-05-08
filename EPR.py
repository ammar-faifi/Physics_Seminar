import manim as ma
from manim import Scene


class EPRQuotes(Scene):
    def construct(self):

        title = ma.Title("EPR Paper").set_color(ma.BLUE)
        self.add(title)

        criterion_of_reality = ma.Text(
            '''"If, without in any way disturbing a system, we can predict with certainty
(i.e., with probability equal to unity) the value of a physical quantity,
then there exists an element of physical reality corresponding to this physical quantity."''',
            slant=ma.ITALIC,
        ).scale(0.5)

        self.play(ma.Write(criterion_of_reality))
        self.play(ma.FadeOut(criterion_of_reality))

        self.wait()

        fund_concept = ma.Tex(
            r"""The fundamental concept of the theory is the concept of \textit{state}"""
        )

        self.play(ma.Write(fund_concept))

        self.wait()
        self.play(fund_concept.animate.move_to(title.get_bottom() * 0.8).scale(0.7))

        observable = ma.MathTex(r"\psi' \equiv A \psi = a\psi")
        self.play(ma.Create(observable))
        self.play(observable.animate.next_to(fund_concept, ma.DOWN).shift(5 * ma.LEFT))

        define_psi = ma.MathTex(r"\psi = e^{(i/\hbar)p_0 x}").next_to(
            observable, buff=1
        )
        self.play(ma.Create(define_psi))

        p_operator = ma.MathTex(r"p = -\hbar i \frac{\partial}{\partial x}")
        self.play(ma.Create(p_operator))

        p_on_psi = ma.MathTex(
            r"\psi' = p \psi =-\hbar i \frac{\partial \psi}{\partial x} =", r"p_0 \psi"
        ).next_to(p_operator, ma.DOWN)
        self.play(ma.Create(p_on_psi))

        self.wait()
        self.play(ma.Create(ma.SurroundingRectangle(define_psi)))
        self.play(ma.Create(ma.SurroundingRectangle(p_on_psi[-1])))

        self.wait()

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
        self.wait()
        self.play(ma.Write(conc_bullet[1]))
        self.play(ma.Write(conc_bullet[2]))
        self.wait()

        # fade out all except title
        to_be_fade_out = {*self.mobjects} - {title}
        self.play(ma.FadeOut(*to_be_fade_out))

        x_on_psi = ma.MathTex(r"q \psi = x\psi", "=", r"a \psi")
        self.play(ma.Write(x_on_psi))
        self.wait()
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
        self.wait()
        self.play(ma.Create(prob_of_x[1]))

        self.wait()

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
        self.wait()
        self.play(ma.Write(conc_position[1]))
        self.wait()
        self.play(ma.Write(conc_position[2]))
        self.wait()

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
        self.wait()
        self.play(ma.Write(EPR_result.submobjects[1]))
        self.wait()
