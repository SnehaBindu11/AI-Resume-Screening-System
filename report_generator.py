from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter


def generate_pdf_report(
    candidate_name,
    match_score,
    missing_skills,
    recommendations
):

    pdf_file = "resume_analysis_report.pdf"

    document = SimpleDocTemplate(
        pdf_file,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()

    elements = []


    # TITLE
    title = Paragraph(
        "<font size=24><b>SkillSync AI</b></font>",
        styles['Title']
    )

    subtitle = Paragraph(
        "<font size=14 color='grey'>AI Resume Analysis Report</font>",
        styles['Heading2']
    )

    elements.append(title)
    elements.append(subtitle)

    elements.append(Spacer(1, 25))


    # CANDIDATE NAME
    candidate = Paragraph(
        f"""
        <font size=14>
        <b>Candidate Name:</b> {candidate_name}
        </font>
        """,
        styles['BodyText']
    )

    elements.append(candidate)

    elements.append(Spacer(1, 20))


    # SCORE SECTION
    score_color = "red"

    if match_score >= 75:
        score_color = "green"

    elif match_score >= 50:
        score_color = "orange"

    score = Paragraph(
        f"""
        <font size=18>
        <b>ATS Match Score:</b>
        <font color="{score_color}">
        {match_score:.2f}%
        </font>
        </font>
        """,
        styles['Heading1']
    )

    elements.append(score)

    elements.append(Spacer(1, 20))


    # VERDICT
    verdict = "Low Match Candidate"

    if match_score >= 75:
        verdict = "Excellent Match Candidate"

    elif match_score >= 50:
        verdict = "Moderate Match Candidate"

    verdict_text = Paragraph(
        f"""
        <font size=14>
        <b>Final Verdict:</b> {verdict}
        </font>
        """,
        styles['BodyText']
    )

    elements.append(verdict_text)

    elements.append(Spacer(1, 25))


    # MISSING SKILLS TABLE
    missing_title = Paragraph(
        "<font size=16><b>Missing Skills</b></font>",
        styles['Heading2']
    )

    elements.append(missing_title)

    elements.append(Spacer(1, 10))

    table_data = [["Skill"]]

    for skill in missing_skills:
        table_data.append([skill.upper()])

    skill_table = Table(
        table_data,
        colWidths=[450]
    )

    skill_table.setStyle(TableStyle([

        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1f77b4")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),

        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f4f4f4")),

        ('GRID', (0, 0), (-1, -1), 1, colors.grey),

        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),

        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),

        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),

        ('BACKGROUND', (0, 1), (-1, -1), colors.beige)

    ]))

    elements.append(skill_table)

    elements.append(Spacer(1, 25))


    # RECOMMENDATIONS
    recommendation_title = Paragraph(
        "<font size=16><b>Recommendations</b></font>",
        styles['Heading2']
    )

    elements.append(recommendation_title)

    elements.append(Spacer(1, 10))

    for recommendation in recommendations:

        recommendation_text = Paragraph(
            f"""
            <font size=12>
            ✅ {recommendation}
            </font>
            """,
            styles['BodyText']
        )

        elements.append(recommendation_text)

        elements.append(Spacer(1, 8))


    elements.append(Spacer(1, 20))


    # AI SUMMARY
    summary_title = Paragraph(
        "<font size=16><b>AI Summary</b></font>",
        styles['Heading2']
    )

    elements.append(summary_title)

    elements.append(Spacer(1, 10))

    summary = Paragraph(
        """
        The candidate demonstrates foundational technical skills and
        relevant project exposure. Improving missing technical competencies
        and adding more industry-relevant AI and Cloud technologies can
        significantly improve ATS compatibility and job readiness.
        """,
        styles['BodyText']
    )

    elements.append(summary)

    document.build(elements)

    return pdf_file