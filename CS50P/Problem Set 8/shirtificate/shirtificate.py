from fpdf import FPDF

class PDF(FPDF):
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, inp):
        self._text = inp

    def textget(self):
        self.text = input("Name: ").strip()

    def header(self):
        self.set_font("helvetica", "BU", 32)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(50, 150, 100)
        self.set_text_color(250, 75, 115)
        self.set_line_width(0.5)
        self.cell(
            w=None, h=None, border=1, text="CS50 Shirtficate", align="C",
            new_x="CENTER", new_y="NEXT", center=True, fill=True
            )

    def body(self):
        self.set_font("helvetica", "B", 24)
        self.set_text_color(255, 255, 255)
        self.set_fill_color(155, 32 , 120)
        self.set_draw_color(155, 120, 32)
        self.set_line_width(3)
        self.image(
            "https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png",
            x="C", y=50
        )
        self.set_y(120)
        self.cell(
            w=None, h=None, border=1, text=self.text+" took CS50", align="C",
            new_x="LMARGIN", new_y="NEXT", center=1, fill=1
            )
        #self.cell(
        #    w=15, h=None, text=" ", new_x="CENTER", new_y="LAST", center=1
        #)
#
        #self.set_text_shaping(use_shaping_engine=True, direction="rtl")
        #self.cell(
        #    w=None, h=None, border=1, text=text, align="L", new_x="END", new_y="LAST", center=0
        #    )
#
        #self.set_text_shaping(use_shaping_engine=True, direction="ltr")
        #self.cell(
        #    w=None, h=None, border=0, text=" took CS50", align="R", new_x="LMARGIN", new_y="NEXT", center=0
        #)
        self.set_auto_page_break(False)

def main():
    pdf = PDF(orientation = "P", unit = "mm", format = "A4")
    pdf.textget()
    pdf.add_page()
    pdf.body() #header is a preset called by FPDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
