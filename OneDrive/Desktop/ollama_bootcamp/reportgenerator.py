from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_pdf(report_text, output_path):
    """
    Generate a PDF report from analysis text.
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph("<b>AI Resume Analysis Report</b>", styles["Heading1"])
    story.append(title)

    story.append(Paragraph("<br/><br/>", styles["BodyText"]))

    for line in report_text.split("\n"):

        if line.strip():

            story.append(
                Paragraph(
                    line.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;"),
                    styles["BodyText"]
                )
            )

    doc.build(story)

    return output_path