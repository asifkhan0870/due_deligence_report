# app/services/pdf_generator.py

from weasyprint import HTML
import os

from weasyprint import HTML
import re
import os

def clean_html(html):
    # remove garbage
    html = re.sub(r'[`"]+', '', html)
    html = re.sub(r'html', '', html)

    # remove inline styles that break layout
    html = re.sub(r'style="[^"]*"', '', html)

    return html


def create_pdf(html_content, pdf_file, report_name="Report"):
    os.makedirs(os.path.dirname(pdf_file), exist_ok=True)

    html_content = clean_html(html_content)

    styled_html = f"""
    <html>
    <head>
        <style>

            @page {{
                size: A4;
                margin: 20mm;
            }}

            body {{
                font-family: Arial, sans-serif;
                font-size: 12px;
                line-height: 1.6;
                color: #222;
            }}

            h1 {{
                font-size: 22px;
                color: #0d47a1;
                margin-top: 20px;
                page-break-before: always;
            }}

            h2 {{
                font-size: 18px;
                margin-top: 15px;
            }}

            h3 {{
                font-size: 15px;
            }}

            p {{
                text-align: justify;
                margin-bottom: 10px;
            }}

            ul {{
                margin-left: 20px;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 15px;
            }}

            th, td {{
                border: 1px solid #ccc;
                padding: 6px;
                text-align: left;
            }}

            th {{
                background-color: #1e88e5;
                color: white;
            }}

            tr:nth-child(even) {{
                background-color: #f5f5f5;
            }}

        </style>
    </head>

    <body>
        <h1>{report_name}</h1>
        {html_content}
    </body>
    </html>
    """

    HTML(string=styled_html).write_pdf(pdf_file)