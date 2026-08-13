from manim import *


class StatisticsVisualizer(Scene):

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

    def make_data_table(
        self,
        data,
        col_widths,
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
                    col_widths[c],
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

    def panel(
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
    # MAIN
    # ============================================================

    def construct(self):

        # ========================================================
        # INTRO
        # ========================================================

        title = Text(
            "Mean Deviation",
            font_size=38,
            color=BLUE
        )

        subtitle = Text(
            "Decimal Item Interpolation • Individual Data • Continuous Data",
            font_size=20,
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
        # PART 1
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
        # TWO-COLUMN FRAME
        # ========================================================

        left_box = self.panel(
            5.2,
            6.4,
            LEFT * 3.55 + DOWN * 0.25,
            BLUE_B
        )

        right_box = self.panel(
            7.1,
            6.4,
            RIGHT * 2.65 + DOWN * 0.25,
            GREEN_B
        )

        left_title = Text(
            "DATA",
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
        # INDIVIDUAL DATA
        # ========================================================

        raw_x = [
            2.5,
            4.0,
            5.5,
            7.0,
            8.5,
            10.0,
            12.0,
            15.0
        ]

        n = len(raw_x)
        total = sum(raw_x)
        mean = total / n

        # --------------------------------------------------------
        # DATA TABLE
        # --------------------------------------------------------

        table_data = [
            ["ITEM", "VALUE"]
        ]

        for i, value in enumerate(
            raw_x,
            start=1
        ):
            table_data.append([
                str(i),
                f"{value:.1f}"
            ])

        data_table = self.make_data_table(
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
                    FadeIn(
                        row,
                        shift=RIGHT * 0.2
                    )
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
            "Decimal Item: 6.38th",
            font_size=22,
            color=ORANGE
        )

        decimal_title.move_to(
            right_box.get_center() +
            UP * 1.95
        )

        self.play(
            Write(decimal_title),
            run_time=1
        )

        # --------------------------------------------------------
        # 6.38 = 6 + 0.38
        # --------------------------------------------------------

        position_formula = MathTex(
            r"6.38 = 6 + 0.38",
            font_size=28
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
            "6th item + 0.38 of the distance to the 7th item",
            font_size=15,
            color=GRAY
        )

        explanation.move_to(
            right_box.get_center() +
            UP * 1.05
        )

        self.play(
            FadeIn(explanation),
            run_time=0.8
        )

        # --------------------------------------------------------
        # HIGHLIGHT 6TH / 7TH
        # --------------------------------------------------------

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

        # --------------------------------------------------------
        # VALUES
        # --------------------------------------------------------

        value6 = MathTex(
            r"T_6 = 10.0",
            font_size=23,
            color=ORANGE
        )

        value7 = MathTex(
            r"T_7 = 12.0",
            font_size=23,
            color=YELLOW
        )

        values = VGroup(
            value6,
            value7
        ).arrange(
            RIGHT,
            buff=0.8
        )

        values.move_to(
            right_box.get_center() +
            UP * 0.55
        )

        self.play(
            Write(value6),
            Write(value7),
            run_time=1
        )

        # ========================================================
        # VISUAL INTERPOLATION
        # ========================================================

        gap_line = Line(
            LEFT * 1.7,
            RIGHT * 1.7,
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

        # --------------------------------------------------------
        # MOVE 0.38 ALONG GAP
        # --------------------------------------------------------

        moving_dot = Dot(
            gap_line.get_start(),
            radius=0.09,
            color=ORANGE
        )

        fraction = MathTex(
            r"0.38",
            font_size=23,
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

        # ========================================================
        # INTERPOLATION CALCULATION
        # ========================================================

        interpolation = MathTex(
            r"T_{6.38}"
            r"=T_6+0.38(T_7-T_6)",
            font_size=22
        )

        interpolation.move_to(
            right_box.get_center() +
            DOWN * 0.65
        )

        self.play(
            Write(interpolation),
            run_time=1.2
        )

        interpolation_calc = MathTex(
            r"=10+0.38(12-10)"
            r"=10.76",
            font_size=22,
            color=ORANGE
        )

        interpolation_calc.next_to(
            interpolation,
            DOWN,
            buff=0.15
        )

        self.play(
            Write(interpolation_calc),
            run_time=1
        )

        self.wait(2)

        # ========================================================
        # CLEAR RIGHT SIDE
        # ========================================================

        interpolation_group = VGroup(
            decimal_title,
            position_formula,
            explanation,
            value6,
            value7,
            gap_line,
            start_dot,
            end_dot,
            start_label,
            end_label,
            moving_dot,
            fraction,
            interpolation,
            interpolation_calc,
            highlight6,
            highlight7
        )

        self.play(
            FadeOut(interpolation_group),
            run_time=0.8
        )

        # ========================================================
        # NOW ACTUAL MEAN DEVIATION
        # ========================================================

        md_title = Text(
            "Mean Deviation from Mean",
            font_size=23,
            color=ORANGE
        )

        md_title.move_to(
            right_box.get_center() +
            UP * 1.95
        )

        self.play(
            Write(md_title),
            run_time=1
        )

        # ========================================================
        # STEP 1 — FIND MEAN
        # ========================================================

        step1 = Text(
            "Step 1 — Find the Mean",
            font_size=18,
            color=BLUE
        )

        step1.move_to(
            right_box.get_center() +
            UP * 1.45
        )

        mean_formula = MathTex(
            r"\bar{x}"
            r"=\frac{\sum x}{n}"
            r"=\frac{64.5}{8}"
            r"=8.0625"
            r"\approx8.06",
            font_size=21
        )

        mean_formula.move_to(
            right_box.get_center() +
            UP * 0.98
        )

        self.play(
            Write(step1),
            Write(mean_formula),
            run_time=1.5
        )

        self.wait(1)

        # ========================================================
        # STEP 2 — DEVIATIONS
        # ========================================================

        step2 = Text(
            "Step 2 — Find |x − Mean| for every item",
            font_size=18,
            color=ORANGE
        )

        step2.move_to(
            right_box.get_center() +
            UP * 0.45
        )

        self.play(
            Write(step2),
            run_time=1
        )

        # --------------------------------------------------------
        # DEVIATION TABLE
        # --------------------------------------------------------

        deviation_data = [
            ["x", "|x − 8.0625|"]
        ]

        deviations = []

        for x in raw_x:

            deviation = abs(
                x - mean
            )

            deviations.append(
                deviation
            )

            deviation_data.append([
                f"{x:.1f}",
                f"{deviation:.4f}"
            ])

        deviation_table = self.make_data_table(
            deviation_data,
            [1.2, 2.2],
            row_height=0.31,
            font_size=12,
            header_color=ORANGE
        )

        deviation_table.scale(
            0.82
        )

        deviation_table.move_to(
            right_box.get_center() +
            DOWN * 0.55
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(row)
                    for row in deviation_table
                ],
                lag_ratio=0.08
            ),
            run_time=1.8
        )

        # ========================================================
        # SHOW DEVIATION CONCEPT
        # ========================================================

        example = MathTex(
            r"|2.5-8.0625|=5.5625",
            font_size=18,
            color=ORANGE
        )

        example.move_to(
            right_box.get_center() +
            DOWN * 2.05
        )

        self.play(
            Write(example),
            run_time=1
        )

        self.wait(1.5)

        # ========================================================
        # STEP 3 — SUM DEVIATIONS
        # ========================================================

        sum_deviations = sum(
            deviations
        )

        sum_text = MathTex(
            rf"\sum|x-\bar{{x}}|"
            rf"={sum_deviations:.4f}"
            rf"\approx26.50",
            font_size=21,
            color=BLUE
        )

        sum_text.move_to(
            right_box.get_center() +
            DOWN * 2.45
        )

        self.play(
            Write(sum_text),
            run_time=1.2
        )

        # ========================================================
        # STEP 4 — FINAL MD
        # ========================================================

        md_formula = MathTex(
            r"MD"
            r"=\frac{\sum|x-\bar{x}|}{n}"
            rf"=\frac{{26.50}}{{8}}"
            rf"=\boxed{{3.31}}",
            font_size=23,
            color=GREEN
        )

        md_formula.move_to(
            right_box.get_center() +
            DOWN * 2.95
        )

        self.play(
            Write(md_formula),
            run_time=1.5
        )

        self.wait(3)

        # ========================================================
        # CLEAN PART 1
        # ========================================================

        part1_group = VGroup(
            part1_title,
            left_box,
            right_box,
            left_title,
            right_title,
            data_table,
            md_title,
            step1,
            mean_formula,
            step2,
            deviation_table,
            example,
            sum_text,
            md_formula
        )

        self.play(
            FadeOut(part1_group),
            run_time=1
        )

        # ========================================================
        # PART 2
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
        # CONTINUOUS DATA PANELS
        # ========================================================

        left_box2 = self.panel(
            6.2,
            6.4,
            LEFT * 3.1 + DOWN * 0.25,
            BLUE_B
        )

        right_box2 = self.panel(
            6.1,
            6.4,
            RIGHT * 3.1 + DOWN * 0.25,
            GREEN_B
        )

        left_title2 = Text(
            "FREQUENCY TABLE",
            font_size=19,
            color=BLUE
        )

        right_title2 = Text(
            "STEP-BY-STEP SOLUTION",
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
            ["Class", "f", "x", "cf"],
            ["0–10", "4", "5", "4"],
            ["10–20", "6", "15", "10"],
            ["20–30", "10", "25", "20"],
            ["30–40", "5", "35", "25"],
            ["Total", "25", "—", "—"]
        ]

        continuous_table = self.make_data_table(
            continuous_data,
            [2.0, 0.9, 1.1, 1.2],
            row_height=0.62,
            font_size=16
        )

        continuous_table.move_to(
            left_box2.get_center() +
            UP * 0.15
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(row)
                    for row in continuous_table
                ],
                lag_ratio=0.08
            ),
            run_time=1.8
        )

        # ========================================================
        # CONTINUOUS CALCULATIONS
        # ========================================================

        mean_label = Text(
            "1. Mean",
            font_size=21,
            color=BLUE
        )

        mean_label.move_to(
            right_box2.get_center() +
            UP * 2
        )

        mean_step1 = MathTex(
            r"\sum fx"
            r"=4(5)+6(15)+10(25)+5(35)",
            font_size=18
        )

        mean_step1.move_to(
            right_box2.get_center() +
            UP * 1.48
        )

        mean_step2 = MathTex(
            r"\sum fx=535",
            font_size=21
        )

        mean_step2.move_to(
            right_box2.get_center() +
            UP * 1.03
        )

        mean_step3 = MathTex(
            r"\bar{x}"
            r"=\frac{535}{25}"
            r"=\boxed{21.4}",
            font_size=22,
            color=BLUE
        )

        mean_step3.move_to(
            right_box2.get_center() +
            UP * 0.57
        )

        self.play(
            Write(mean_label),
            Write(mean_step1),
            run_time=1.3
        )

        self.play(
            Write(mean_step2),
            Write(mean_step3),
            run_time=1.3
        )

        # ========================================================
        # MEDIAN
        # ========================================================

        median_label = Text(
            "2. Median",
            font_size=21,
            color=GREEN
        )

        median_label.move_to(
            right_box2.get_center() +
            DOWN * 0.05
        )

        median_step1 = MathTex(
            r"\frac{N}{2}"
            r"=\frac{25}{2}"
            r"=12.5",
            font_size=19
        )

        median_step1.move_to(
            right_box2.get_center() +
            DOWN * 0.5
        )

        median_step2 = MathTex(
            r"12.5\Rightarrow[20,30]"
            r"\quad\text{Median Class}",
            font_size=18
        )

        median_step2.move_to(
            right_box2.get_center() +
            DOWN * 0.95
        )

        self.play(
            Write(median_label),
            Write(median_step1),
            Write(median_step2),
            run_time=1.4
        )

        median_row = continuous_table[3]

        median_highlight = SurroundingRectangle(
            median_row,
            color=GREEN,
            buff=0.04
        )

        self.play(
            Create(median_highlight),
            run_time=0.7
        )

        median_formula = MathTex(
            r"M_e"
            r"=20+\left(\frac{12.5-10}{10}\right)(10)"
            r"=\boxed{22.5}",
            font_size=19,
            color=GREEN
        )

        median_formula.move_to(
            right_box2.get_center() +
            DOWN * 1.45
        )

        self.play(
            Write(median_formula),
            run_time=1.4
        )

        # ========================================================
        # CONTINUOUS MD
        # ========================================================

        md_cont_title = Text(
            "3. Mean Deviation",
            font_size=20,
            color=ORANGE
        )

        md_cont_title.move_to(
            right_box2.get_center() +
            DOWN * 1.95
        )

        md_cont_formula = MathTex(
            r"MD_{\bar{x}}"
            r"=\frac{\sum f|x-\bar{x}|}{N}"
            r"=\frac{208}{25}"
            r"=\boxed{8.32}",
            font_size=18,
            color=BLUE
        )

        md_cont_formula.move_to(
            right_box2.get_center() +
            DOWN * 2.4
        )

        md_cont_formula2 = MathTex(
            r"MD_{M_e}"
            r"=\frac{\sum f|x-M_e|}{N}"
            r"=\frac{202.5}{25}"
            r"=\boxed{8.10}",
            font_size=18,
            color=GREEN
        )

        md_cont_formula2.move_to(
            right_box2.get_center() +
            DOWN * 2.85
        )

        self.play(
            Write(md_cont_title),
            Write(md_cont_formula),
            Write(md_cont_formula2),
            run_time=2
        )

        self.wait(3)

        # ========================================================
        # OUTRO
        # ========================================================

        all_part2 = VGroup(
            part2_title,
            left_box2,
            right_box2,
            left_title2,
            right_title2,
            continuous_table,
            mean_label,
            mean_step1,
            mean_step2,
            mean_step3,
            median_label,
            median_step1,
            median_step2,
            median_formula,
            md_cont_title,
            md_cont_formula,
            md_cont_formula2,
            median_highlight
        )

        self.play(
            FadeOut(all_part2),
            run_time=1
        )

        final = Text(
            "MEAN DEVIATION — COMPLETE",
            font_size=30,
            color=GREEN
        )

        self.play(
            Write(final),
            run_time=1.5
        )

        self.wait(2)

        self.play(
            FadeOut(final)
        )