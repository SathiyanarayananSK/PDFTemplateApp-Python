from fpdf import FPDF
import pandas as pd

# Initialize PDF object
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)  # Disable automatic page breaks
pg_num = 0  # Initialize page number counter

# Load topics from the CSV file
df = pd.read_csv("topics.csv", sep=",")

# Iterate through each topic in the CSV file
for index, row in df.iterrows():
    pdf.add_page()  # Add a new page for the topic

    # Add the topic title to the page
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=0, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 18, 200, 18)  # Add a horizontal line below the title

    y = 18  # Starting Y position for the lines
    pg_num += 1  # Increment page number

    # Add horizontal lines for writing/note-taking
    for brk_ln in range(18, 275, 10):
        y += 10
        pdf.line(10, y, 200, y)

    pdf.ln(275)  # Move to the bottom of the page

    # Add page number and topic name in the footer
    pdf.set_font(family="Times", style="I", size=9)
    pdf.set_text_color(160, 160, 160)
    pdf.cell(w=0, h=0, txt=str(pg_num), align="C")
    pdf.cell(w=0, h=0, txt=row["Topic"], align="R")

    # Add additional pages for the topic if specified
    for pg in range(row["Pages"] - 1):
        pdf.add_page()
        y = 18
        pg_num += 1
        for brk_ln in range(18, 275, 10):
            y += 10
            pdf.line(10, y, 200, y)

        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=9)
        pdf.set_text_color(160, 160, 160)
        pdf.cell(w=0, h=0, txt=str(pg_num), align="C")
        pdf.cell(w=0, h=0, txt=row["Topic"], align="R")

# Save the generated PDF
pdf.output("Output.pdf")
