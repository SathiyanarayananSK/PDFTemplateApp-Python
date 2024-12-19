from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
pg_num = 0
df = pd.read_csv("topics.csv", sep=",")


for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=0, txt=row["Topic"], align="L", ln=1)
    pdf.line(10,18, 200, 18)

    y = 18
    pg_num+=1


    for brk_ln in range(18,275,10):
        y+=10
        pdf.line(10, y, 200, y)


    pdf.ln(275)

    pdf.set_font(family="Times", style="I", size=9)
    pdf.set_text_color(160, 160, 160)
    pdf.cell(w=0, h=0, txt=str(pg_num), align="C")
    pdf.cell(w=0, h=0, txt=row["Topic"], align="R")

    for pg in range(row["Pages"] - 1):
        pdf.add_page()
        y = 18
        pg_num+=1
        for brk_ln in range(18, 275, 10):
            y += 10
            pdf.line(10, y, 200, y)

        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=9)
        pdf.set_text_color(160, 160, 160)
        pdf.cell(w=0, h=0, txt=str(pg_num), align="C")
        pdf.cell(w=0, h=0, txt=row["Topic"], align="R")

pdf.output("Output.pdf")