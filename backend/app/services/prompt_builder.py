def build_section_prompt(section_name, user_data):
    return f"""
You are a top-tier investment analyst and McKinsey-level consultant.

Your task is to generate a highly detailed, professional report section.

SECTION:
{section_name}

DECK DATA:
{user_data}

-----------------------------------
STRICT INSTRUCTIONS (VERY IMPORTANT)
-----------------------------------

• Base your analysis STRICTLY on the provided deck data
• If data is missing, clearly mention assumptions
• Do NOT invent unrealistic numbers or fake metrics
• Use logical reasoning and business understanding

• Avoid generic statements — be specific and analytical
• Avoid repetition across paragraphs
• Add insights, comparisons, and interpretations

-----------------------------------
OUTPUT RULES (CRITICAL)
-----------------------------------

• Output MUST be clean HTML only
• DO NOT use markdown or ```
• DO NOT include the word "html" anywhere
• DO NOT add inline styles or broken tags

• Allowed tags ONLY:
<h1>, <h2>, <h3>, <p>, <ul>, <li>, <table>, <tr>, <th>, <td>

• Every paragraph must be inside <p>
• Properly close all HTML tags

-----------------------------------
CONTENT REQUIREMENTS
-----------------------------------

• Start with:
<h1>{section_name}</h1>

• Use structured flow:
    - Explanation
    - Analysis
    - Insights
    - (Optional) Table
    - (Optional) Bullet points

• Include at least:
    - 5–8 detailed paragraphs
    - 1 table (if applicable)
    - 1 bullet list

• Tables must be properly structured:
<table>
<tr><th>Metric</th><th>Value</th></tr>
<tr><td>Example</td><td>Data</td></tr>
</table>

-----------------------------------

Generate a detailed, insight-rich section (~1200–1800 words).
"""