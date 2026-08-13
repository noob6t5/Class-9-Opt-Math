from manim import *


class QuartileDeviationVisualizer(Scene):

    # ============================================================
    # HELPER FUNCTIONS
    # ============================================================

    def make_cell(
        self,
        text,
        width,
        height,
        font_size=15,
        color=WHITE
    ):
        rect = Rectangle(
            width=width,
            height=height,
            stroke_width=1
        )

        label = Text(
            str(text),
            font_size=font_size,
            color=color
        )

        label.move_to(rect.get_center())

        return VGroup(rect, label)

    def make_table(
        self,
        data,
        widths,
        row_height=0.45,
        font_size=15,
        header_color=BLUE
    ):
        rows = []

        for r, row_data in enumerate(data):

            row = VGroup()

            for c, value in enumerate(row_data):

                color = (
                    header_color
                    if r == 0
                    else WHITE
                )

                cell = self.make_cell(
                    value,
                    widths[c],
                    row_height,
                    font_size,
                    color
                )

                row.add(cell)

            row.arrange(
                RIGHT,
                buff=0
            )

            rows.append(row)

        table = VGroup(*rows)

        table.arrange(
            DOWN,
            buff=0
        )

        return table

    def make_panel(
        self,
        width,
        height,
        position,
        color
    ):
        box = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.12,
            stroke_color=color,
            stroke_width=2
        )

        box.move_to(position)

        return box

    # ============================================================
    # CONSTRUCT
    # ============================================================

    def construct(self):

        # ========================================================
        # INTRO
        # ========================================================

        title = Text(
            "Quartile Deviation",
            font_size=38,
            color=BLUE
        )

        subtitle = Text(
            "Q₁ • Q₃ • Quartile Deviation • Coefficient",
            font_size=21,
            color=GRAY
        )

        intro = VGroup(
            title,
            subtitle
        ).arrange(
            DOWN,
            buff=0.25
        )

        self.play(
            Write(title),
            run_time=1.2
        )

        self.play(
            FadeIn(subtitle),
            run_time=1
        )

        self.wait(1.5)

        self.play(
            FadeOut(intro),
            run_time=0.8
        )

        # ========================================================
        # PART 1 — INDIVIDUAL DATA
        # ========================================================

        part1_title = Text(
            "PART 1 — INDIVIDUAL DATA",
            font_size=27,
            color=YELLOW
        )

        part1_title.to_edge(
            UP,
            buff=0.15
        )

        self.play(
            Write(part1_title),
            run_time=1
        )

        # ========================================================
        # TWO PANELS
        # ========================================================

        left_box = self.make_panel(
            5.2,
            6.4,
            LEFT * 3.55 + DOWN * 0.25,
            BLUE_B
        )

        right_box = self.make_panel(
            7.1,
            6.4,
            RIGHT * 2.65 + DOWN * 0.25,
            GREEN_B
        )

        left_title = Text(
            "SORTED DATA",
            font_size=20,
            color=BLUE
        )

        right_title = Text(
            "SOLUTION",
            font_size=20,
            color=GREEN
        )

        left_title.move_to(
            left_box.get_top() + DOWN * 0.3
        )

        right_title.move_to(
            right_box.get_top() + DOWN * 0.3
        )

        self.play(
            Create(left_box),
            Create(right_box),
            Write(left_title),
            Write(right_title),
            run_time=1
        )

        # ========================================================
        # DATA TABLE
        # ========================================================

        data = [
            2.5,
            4.0,
            5.5,
            7.0,
            8.5,
            10.0,
            12.0,
            15.0
        ]

        n = len(data)

        table_data = [
            ["ITEM", "VALUE"]
        ]

        for i, value in enumerate(
            data,
            start=1
        ):
            table_data.append([
                str(i),
                f"{value:.1f}"
            ])

        data_table = self.make_table(
            table_data,
            [1.4, 2.6],
            row_height=0.52,
            font_size=17
        )

        data_table.move_to(
            left_box.get_center() +
            DOWN * 0.1
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(row)
                    for row in data_table
                ],
                lag_ratio=0.08
            ),
            run_time=2
        )

        # ========================================================
        # DECIMAL ITEM INTERPOLATION
        # ========================================================

        decimal_title = Text(
            "Decimal Item Interpolation",
            font_size=21,
            color=ORANGE
        )

        decimal_title.move_to(
            right_box.get_center() +
            UP * 2.0
        )

        self.play(
            Write(decimal_title),
            run_time=1
        )

        position_formula = MathTex(
            r"6.38=6+0.38",
            font_size=27
        )

        position_formula.move_to(
            right_box.get_center() +
            UP * 1.45
        )

        self.play(
            Write(position_formula),
            run_time=1
        )

        explanation = Text(
            "6th item + 0.38 of the distance to 7th item",
            font_size=14,
            color=GRAY
        )

        explanation.move_to(
            right_box.get_center() +
            UP * 1.02
        )

        self.play(
            FadeIn(explanation),
            run_time=0.8
        )

        # Highlight 6th and 7th

        row6 = data_table[6]
        row7 = data_table[7]

        highlight6 = SurroundingRectangle(
            row6,
            color=ORANGE,
            buff=0.04
        )

        highlight7 = SurroundingRectangle(
            row7,
            color=YELLOW,
            buff=0.04
        )

        self.play(
            Create(highlight6),
            Create(highlight7),
            run_time=0.8
        )

        values = VGroup(
            MathTex(
                r"T_6=10",
                font_size=21,
                color=ORANGE
            ),
            MathTex(
                r"T_7=12",
                font_size=21,
                color=YELLOW
            )
        ).arrange(
            RIGHT,
            buff=0.7
        )

        values.move_to(
            right_box.get_center() +
            UP * 0.55
        )

        self.play(
            Write(values),
            run_time=1
        )

        # ========================================================
        # INTERPOLATION VISUAL
        # ========================================================

        gap_line = Line(
            LEFT * 1.65,
            RIGHT * 1.65,
            stroke_width=5,
            color=GRAY
        )

        gap_line.move_to(
            right_box.get_center() +
            DOWN * 0.05
        )

        start_dot = Dot(
            gap_line.get_start(),
            color=ORANGE
        )

        end_dot = Dot(
            gap_line.get_end(),
            color=YELLOW
        )

        start_label = MathTex(
            r"10",
            font_size=17
        ).next_to(
            start_dot,
            DOWN,
            buff=0.1
        )

        end_label = MathTex(
            r"12",
            font_size=17
        ).next_to(
            end_dot,
            DOWN,
            buff=0.1
        )

        self.play(
            Create(gap_line),
            FadeIn(start_dot),
            FadeIn(end_dot),
            Write(start_label),
            Write(end_label),
            run_time=1
        )

        moving_dot = Dot(
            gap_line.get_start(),
            radius=0.09,
            color=ORANGE
        )

        fraction = MathTex(
            r"0.38",
            font_size=21,
            color=ORANGE
        )

        fraction.move_to(
            gap_line.get_start() +
            UP * 0.35
        )

        self.play(
            FadeIn(moving_dot),
            Write(fraction)
        )

        target_point = gap_line.point_from_proportion(
            0.38
        )

        self.play(
            moving_dot.animate.move_to(
                target_point
            ),
            fraction.animate.move_to(
                target_point + UP * 0.35
            ),
            run_time=2
        )

        interpolation = MathTex(
            r"T_{6.38}"
            r"=T_6+0.38(T_7-T_6)",
            font_size=20
        )

        interpolation.move_to(
            right_box.get_center() +
            DOWN * 0.65
        )

        interpolation_calc = MathTex(
            r"=10+0.38(12-10)"
            r"=\boxed{10.76}",
            font_size=20,
            color=ORANGE
        )

        interpolation_calc.next_to(
            interpolation,
            DOWN,
            buff=0.12
        )

        self.play(
            Write(interpolation),
            run_time=1
        )

        self.play(
            Write(interpolation_calc),
            run_time=1
        )

        self.wait(2)

        interpolation_group = VGroup(
            decimal_title,
            position_formula,
            explanation,
            values,
            highlight6,
            highlight7,
            gap_line,
            start_dot,
            end_dot,
            start_label,
            end_label,
            moving_dot,
            fraction,
            interpolation,
            interpolation_calc
        )

        self.play(
            FadeOut(interpolation_group),
            run_time=0.8
        )

        # ========================================================
        # STEP 1 — Q1
        # ========================================================

        step1 = Text(
            "Step 1 — Find Q₁",
            font_size=21,
            color=BLUE
        )

        step1.move_to(
            right_box.get_center() +
            UP * 2.0
        )

        self.play(
            Write(step1),
            run_time=1
        )

        q1_position = MathTex(
            r"Q_1\text{ position}"
            r"=\frac{n+1}{4}"
            r"=\frac{9}{4}"
            r"=2.25",
            font_size=21
        )

        q1_position.move_to(
            right_box.get_center() +
            UP * 1.4
        )

        self.play(
            Write(q1_position),
            run_time=1
        )

        q1_class = Text(
            "2.25 lies between 2nd and 3rd items",
            font_size=14,
            color=BLUE
        )

        q1_class.move_to(
            right_box.get_center() +
            UP * 0.92
        )

        self.play(
            Write(q1_class),
            run_time=1
        )

        q1_row1 = SurroundingRectangle(
            data_table[2],
            color=BLUE,
            buff=0.04
        )

        q1_row2 = SurroundingRectangle(
            data_table[3],
            color=BLUE,
            buff=0.04
        )

        self.play(
            Create(q1_row1),
            Create(q1_row2),
            run_time=0.7
        )

        q1_formula = MathTex(
            r"Q_1=T_2+0.25(T_3-T_2)",
            font_size=20
        )

        q1_formula.move_to(
            right_box.get_center() +
            UP * 0.35
        )

        q1_calc = MathTex(
            r"=4+0.25(5.5-4)"
            r"=\boxed{4.375}",
            font_size=20,
            color=BLUE
        )

        q1_calc.move_to(
            right_box.get_center() +
            DOWN * 0.25
        )

        self.play(
            Write(q1_formula),
            run_time=1
        )

        self.play(
            Write(q1_calc),
            run_time=1
        )

        self.wait(1.5)

        q1_group = VGroup(
            step1,
            q1_position,
            q1_class,
            q1_row1,
            q1_row2,
            q1_formula,
            q1_calc
        )

        self.play(
            FadeOut(q1_group),
            run_time=0.7
        )

        # ========================================================
        # STEP 2 — Q3
        # ========================================================

        step2 = Text(
            "Step 2 — Find Q₃",
            font_size=21,
            color=GREEN
        )

        step2.move_to(
            right_box.get_center() +
            UP * 2.0
        )

        self.play(
            Write(step2),
            run_time=1
        )

        q3_position = MathTex(
            r"Q_3\text{ position}"
            r"=\frac{3(n+1)}{4}"
            r"=\frac{27}{4}"
            r"=6.75",
            font_size=21
        )

        q3_position.move_to(
            right_box.get_center() +
            UP * 1.4
        )

        self.play(
            Write(q3_position),
            run_time=1
        )

        q3_class = Text(
            "6.75 lies between 6th and 7th items",
            font_size=14,
            color=GREEN
        )

        q3_class.move_to(
            right_box.get_center() +
            UP * 0.92
        )

        self.play(
            Write(q3_class),
            run_time=1
        )

        q3_row1 = SurroundingRectangle(
            data_table[6],
            color=GREEN,
            buff=0.04
        )

        q3_row2 = SurroundingRectangle(
            data_table[7],
            color=GREEN,
            buff=0.04
        )

        self.play(
            Create(q3_row1),
            Create(q3_row2),
            run_time=0.7
        )

        q3_formula = MathTex(
            r"Q_3=T_6+0.75(T_7-T_6)",
            font_size=20
        )

        q3_formula.move_to(
            right_box.get_center() +
            UP * 0.35
        )

        q3_calc = MathTex(
            r"=10+0.75(12-10)"
            r"=\boxed{11.5}",
            font_size=20,
            color=GREEN
        )

        q3_calc.move_to(
            right_box.get_center() +
            DOWN * 0.25
        )

        self.play(
            Write(q3_formula),
            run_time=1
        )

        self.play(
            Write(q3_calc),
            run_time=1
        )

        self.wait(1.5)

        q3_group = VGroup(
            step2,
            q3_position,
            q3_class,
            q3_row1,
            q3_row2,
            q3_formula,
            q3_calc
        )

        self.play(
            FadeOut(q3_group),
            run_time=0.7
        )

        # ========================================================
        # STEP 3 — QUARTILE DEVIATION
        # ========================================================

        step3 = Text(
            "Step 3 — Quartile Deviation",
            font_size=21,
            color=ORANGE
        )

        step3.move_to(
            right_box.get_center() +
            UP * 1.8
        )

        self.play(
            Write(step3),
            run_time=1
        )

        qd_formula = MathTex(
            r"QD=\frac{Q_3-Q_1}{2}",
            font_size=25
        )

        qd_formula.move_to(
            right_box.get_center() +
            UP * 1.15
        )

        qd_calc = MathTex(
            r"=\frac{11.5-4.375}{2}"
            r"=\boxed{3.5625}",
            font_size=23,
            color=ORANGE
        )

        qd_calc.move_to(
            right_box.get_center() +
            UP * 0.45
        )

        self.play(
            Write(qd_formula),
            run_time=1
        )

        self.play(
            Write(qd_calc),
            run_time=1
        )

        # ========================================================
        # STEP 4 — COEFFICIENT
        # ========================================================

        step4 = Text(
            "Step 4 — Coefficient of QD",
            font_size=20,
            color=PURPLE
        )

        step4.move_to(
            right_box.get_center() +
            DOWN * 0.25
        )

        self.play(
            Write(step4),
            run_time=1
        )

        coefficient_formula = MathTex(
            r"\text{Coefficient}"
            r"=\frac{Q_3-Q_1}{Q_3+Q_1}",
            font_size=22
        )

        coefficient_formula.move_to(
            right_box.get_center() +
            DOWN * 0.8
        )

        coefficient_calc = MathTex(
            r"=\frac{11.5-4.375}"
            r"{11.5+4.375}"
            r"\approx\boxed{0.449}",
            font_size=21,
            color=PURPLE
        )

        coefficient_calc.move_to(
            right_box.get_center() +
            DOWN * 1.45
        )

        self.play(
            Write(coefficient_formula),
            run_time=1
        )

        self.play(
            Write(coefficient_calc),
            run_time=1
        )

        self.wait(3)

        # ========================================================
        # CLEAR PART 1
        # ========================================================

        part1_group = VGroup(
            part1_title,
            left_box,
            right_box,
            left_title,
            right_title,
            data_table,
            step3,
            qd_formula,
            qd_calc,
            step4,
            coefficient_formula,
            coefficient_calc
        )

        self.play(
            FadeOut(part1_group),
            run_time=1
        )

        # ========================================================
        # PART 2 — CONTINUOUS DATA
        # ========================================================

        part2_title = Text(
            "PART 2 — CONTINUOUS DATA",
            font_size=27,
            color=YELLOW
        )

        part2_title.to_edge(
            UP,
            buff=0.15
        )

        self.play(
            Write(part2_title),
            run_time=1
        )

        # ========================================================
        # PANELS
        # ========================================================

        left_box2 = self.make_panel(
            6.0,
            6.5,
            LEFT * 3.15 + DOWN * 0.25,
            BLUE_B
        )

        right_box2 = self.make_panel(
            6.3,
            6.5,
            RIGHT * 3.0 + DOWN * 0.25,
            GREEN_B
        )

        left_title2 = Text(
            "FREQUENCY TABLE",
            font_size=19,
            color=BLUE
        )

        right_title2 = Text(
            "QUARTILE SOLUTION",
            font_size=19,
            color=GREEN
        )

        left_title2.move_to(
            left_box2.get_top() +
            DOWN * 0.3
        )

        right_title2.move_to(
            right_box2.get_top() +
            DOWN * 0.3
        )

        self.play(
            Create(left_box2),
            Create(right_box2),
            Write(left_title2),
            Write(right_title2),
            run_time=1
        )

        # ========================================================
        # CONTINUOUS TABLE
        # ========================================================

        continuous_data = [
            ["Class", "f", "cf"],
            ["0–10", "4", "4"],
            ["10–20", "6", "10"],
            ["20–30", "10", "20"],
            ["30–40", "5", "25"],
            ["Total", "25", "—"]
        ]

        continuous_table = self.make_table(
            continuous_data,
            [2.2, 1.1, 1.3],
            row_height=0.65,
            font_size=17
        )

        continuous_table.move_to(
            left_box2.get_center()
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(row)
                    for row in continuous_table
                ],
                lag_ratio=0.08
            ),
            run_time=2
        )

        # ========================================================
        # STEP 1 — Q1
        # ========================================================

        step_c1 = Text(
            "Step 1 — Locate Q₁",
            font_size=21,
            color=BLUE
        )

        step_c1.move_to(
            right_box2.get_center() +
            UP * 2.15
        )

        self.play(
            Write(step_c1),
            run_time=1
        )

        q1_cont_position = MathTex(
            r"\frac{N}{4}"
            r"=\frac{25}{4}"
            r"=6.25",
            font_size=23
        )

        q1_cont_position.move_to(
            right_box2.get_center() +
            UP * 1.65
        )

        self.play(
            Write(q1_cont_position),
            run_time=1
        )

        q1_cont_class = Text(
            "6.25 → 10–20 class",
            font_size=17,
            color=BLUE
        )

        q1_cont_class.move_to(
            right_box2.get_center() +
            UP * 1.18
        )

        self.play(
            Write(q1_cont_class),
            run_time=1
        )

        q1_cont_highlight = SurroundingRectangle(
            continuous_table[2],
            color=BLUE,
            buff=0.04
        )

        self.play(
            Create(q1_cont_highlight),
            run_time=0.7
        )

        q1_cont_formula = MathTex(
            r"Q_1=L+\left("
            r"\frac{\frac{N}{4}-cf}{f}"
            r"\right)h",
            font_size=20
        )

        q1_cont_formula.move_to(
            right_box2.get_center() +
            UP * 0.62
        )

        self.play(
            Write(q1_cont_formula),
            run_time=1
        )

        q1_cont_calc = MathTex(
            r"=10+\left(\frac{6.25-4}{6}\right)(10)"
            r"=\boxed{13.75}",
            font_size=19,
            color=BLUE
        )

        q1_cont_calc.move_to(
            right_box2.get_center() +
            DOWN * 0.05
        )

        self.play(
            Write(q1_cont_calc),
            run_time=1
        )

        self.wait(1.5)

        # ========================================================
        # CLEAR Q1
        # ========================================================

        q1_cont_group = VGroup(
            step_c1,
            q1_cont_position,
            q1_cont_class,
            q1_cont_highlight,
            q1_cont_formula,
            q1_cont_calc
        )

        self.play(
            FadeOut(q1_cont_group),
            run_time=0.7
        )

        # ========================================================
        # STEP 2 — Q3
        # ========================================================

        step_c2 = Text(
            "Step 2 — Locate Q₃",
            font_size=21,
            color=GREEN
        )

        step_c2.move_to(
            right_box2.get_center() +
            UP * 2.15
        )

        self.play(
            Write(step_c2),
            run_time=1
        )

        q3_cont_position = MathTex(
            r"\frac{3N}{4}"
            r"=\frac{3(25)}{4}"
            r"=18.75",
            font_size=23
        )

        q3_cont_position.move_to(
            right_box2.get_center() +
            UP * 1.65
        )

        self.play(
            Write(q3_cont_position),
            run_time=1
        )

        q3_cont_class = Text(
            "18.75 → 20–30 class",
            font_size=17,
            color=GREEN
        )

        q3_cont_class.move_to(
            right_box2.get_center() +
            UP * 1.18
        )

        self.play(
            Write(q3_cont_class),
            run_time=1
        )

        q3_cont_highlight = SurroundingRectangle(
            continuous_table[3],
            color=GREEN,
            buff=0.04
        )

        self.play(
            Create(q3_cont_highlight),
            run_time=0.7
        )

        q3_cont_formula = MathTex(
            r"Q_3=L+\left("
            r"\frac{\frac{3N}{4}-cf}{f}"
            r"\right)h",
            font_size=20
        )

        q3_cont_formula.move_to(
            right_box2.get_center() +
            UP * 0.62
        )

        self.play(
            Write(q3_cont_formula),
            run_time=1
        )

        q3_cont_calc = MathTex(
            r"=20+\left(\frac{18.75-10}{10}\right)(10)"
            r"=\boxed{28.75}",
            font_size=19,
            color=GREEN
        )

        q3_cont_calc.move_to(
            right_box2.get_center() +
            DOWN * 0.05
        )

        self.play(
            Write(q3_cont_calc),
            run_time=1
        )

        self.wait(1.5)

        # ========================================================
        # CLEAR Q3
        # ========================================================

        q3_cont_group = VGroup(
            step_c2,
            q3_cont_position,
            q3_cont_class,
            q3_cont_highlight,
            q3_cont_formula,
            q3_cont_calc
        )

        self.play(
            FadeOut(q3_cont_group),
            run_time=0.7
        )

        # ========================================================
        # STEP 3 — CONTINUOUS QD
        # ========================================================

        step_c3 = Text(
            "Step 3 — Quartile Deviation",
            font_size=21,
            color=ORANGE
        )

        step_c3.move_to(
            right_box2.get_center() +
            UP * 1.8
        )

        self.play(
            Write(step_c3),
            run_time=1
        )

        qd_cont_formula = MathTex(
            r"QD=\frac{Q_3-Q_1}{2}",
            font_size=25
        )

        qd_cont_formula.move_to(
            right_box2.get_center() +
            UP * 1.15
        )

        self.play(
            Write(qd_cont_formula),
            run_time=1
        )

        qd_cont_calc = MathTex(
            r"=\frac{28.75-13.75}{2}"
            r"=\boxed{7.5}",
            font_size=23,
            color=ORANGE
        )

        qd_cont_calc.move_to(
            right_box2.get_center() +
            UP * 0.45
        )

        self.play(
            Write(qd_cont_calc),
            run_time=1
        )

        # ========================================================
        # STEP 4 — CONTINUOUS COEFFICIENT
        # ========================================================

        step_c4 = Text(
            "Step 4 — Coefficient of QD",
            font_size=20,
            color=PURPLE
        )

        step_c4.move_to(
            right_box2.get_center() +
            DOWN * 0.25
        )

        self.play(
            Write(step_c4),
            run_time=1
        )

        coeff_cont_formula = MathTex(
            r"\text{Coefficient}"
            r"=\frac{Q_3-Q_1}{Q_3+Q_1}",
            font_size=22
        )

        coeff_cont_formula.move_to(
            right_box2.get_center() +
            DOWN * 0.8
        )

        self.play(
            Write(coeff_cont_formula),
            run_time=1
        )

        coeff_cont_calc = MathTex(
            r"=\frac{28.75-13.75}"
            r"{28.75+13.75}",
            font_size=21
        )

        coeff_cont_calc.move_to(
            right_box2.get_center() +
            DOWN * 1.35
        )

        self.play(
            Write(coeff_cont_calc),
            run_time=1
        )

        coeff_cont_result = MathTex(
            r"=\frac{15}{42.5}"
            r"=\boxed{0.3529}",
            font_size=24,
            color=PURPLE
        )

        coeff_cont_result.move_to(
            right_box2.get_center() +
            DOWN * 1.9
        )

        self.play(
            Write(coeff_cont_result),
            run_time=1.2
        )

        self.wait(3)

        # ========================================================
        # FINAL SUMMARY
        # ========================================================

        all_part2 = VGroup(
            part2_title,
            left_box2,
            right_box2,
            left_title2,
            right_title2,
            continuous_table,
            step_c3,
            qd_cont_formula,
            qd_cont_calc,
            step_c4,
            coeff_cont_formula,
            coeff_cont_calc,
            coeff_cont_result
        )

        self.play(
            FadeOut(all_part2),
            run_time=1
        )

        summary_title = Text(
            "QUARTILE DEVIATION — FINAL RESULTS",
            font_size=29,
            color=YELLOW
        )

        individual_title = Text(
            "Individual Data",
            font_size=21,
            color=BLUE
        )

        individual_results = VGroup(
            MathTex(
                r"Q_1=4.375",
                font_size=23
            ),
            MathTex(
                r"Q_3=11.5",
                font_size=23
            ),
            MathTex(
                r"QD=3.5625",
                font_size=23,
                color=ORANGE
            ),
            MathTex(
                r"\text{Coefficient}=0.449",
                font_size=23,
                color=PURPLE
            )
        ).arrange(
            RIGHT,
            buff=0.65
        )

        continuous_title = Text(
            "Continuous Data",
            font_size=21,
            color=GREEN
        )

        continuous_results = VGroup(
            MathTex(
                r"Q_1=13.75",
                font_size=23
            ),
            MathTex(
                r"Q_3=28.75",
                font_size=23
            ),
            MathTex(
                r"QD=7.5",
                font_size=23,
                color=ORANGE
            ),
            MathTex(
                r"\text{Coefficient}=0.3529",
                font_size=23,
                color=PURPLE
            )
        ).arrange(
            RIGHT,
            buff=0.65
        )

        final_group = VGroup(
            summary_title,
            individual_title,
            individual_results,
            continuous_title,
            continuous_results
        ).arrange(
            DOWN,
            buff=0.4
        )

        self.play(
            Write(summary_title),
            run_time=1
        )

        self.play(
            Write(individual_title),
            run_time=0.8
        )

        self.play(
            LaggedStart(
                *[
                    Write(item)
                    for item in individual_results
                ],
                lag_ratio=0.15
            ),
            run_time=1.5
        )

        self.play(
            Write(continuous_title),
            run_time=0.8
        )

        self.play(
            LaggedStart(
                *[
                    Write(item)
                    for item in continuous_results
                ],
                lag_ratio=0.15
            ),
            run_time=1.5
        )

        self.wait(4)

        self.play(
            FadeOut(final_group)
        )