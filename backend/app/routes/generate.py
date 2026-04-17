# app/routes/generate.py

from fastapi import APIRouter
import os
import asyncio

from app.services.claude_service import generate_report_async
from app.services.prompt_builder import build_section_prompt
from app.services.pdf_generator import create_pdf
from app.services.zip_service import create_zip
from app.routes.upload import DATA_STORE

from app.data.reports_config import REPORTS, CATEGORY_SECTIONS

router = APIRouter()


# ✅ SMART SECTION RESOLVER
def get_sections_for_report(report_name):
    report_key = report_name.lower().replace(" ", "_")

    for category, reports in REPORTS.items():
        if report_key in reports:
            print(f"📊 Matched category: {category}")
            return CATEGORY_SECTIONS.get(category, [])

    # 🔁 fallback
    print("⚠️ Using fallback sections")

    readable_name = report_name.replace("_", " ").title()

    return [
        "Executive Summary",
        f"{readable_name} Overview",
        f"{readable_name} Analysis",
        f"{readable_name} Insights",
        "Risk Factors",
        "Recommendations",
        "Conclusion"
    ]


@router.post("/generate")
async def generate(data: dict):
    session_id = data["session_id"]
    selected_reports = data["reports"]

    print("\n📥 Incoming reports:", selected_reports)

    deck_text = DATA_STORE.get(session_id)

    if not deck_text:
        return {"error": "No data found"}

    # ✅ STORAGE PATH (keep outputs/)
    folder = f"outputs/{session_id}"
    os.makedirs(folder, exist_ok=True)

    generated_files = []

    # 🔥 LOOP PER REPORT
    for report in selected_reports:
        print(f"\n🚀 Generating report: {report}")

        try:
            sections = get_sections_for_report(report)

            tasks = []

            for section in sections:
                print(f"➡️ Queueing section: {section}")
                prompt = build_section_prompt(f"{report} - {section}", deck_text)
                tasks.append(generate_report_async(prompt))

            print("⚡ Running all sections in parallel...")
            results = await asyncio.gather(*tasks, return_exceptions=True)

            report_html = ""

            for idx, result in enumerate(results):
                section_name = sections[idx]

                if isinstance(result, Exception):
                    print(f"❌ Error in {section_name}: {result}")
                    report_html += f"<h2>{section_name}</h2><p>Error generating this section</p>"
                else:
                    print(f"✅ Completed section: {section_name}")
                    report_html += result + "\n"

            print(f"📄 Creating PDF for {report}")

            safe_name = report.replace(" ", "_")
            pdf_path = f"{folder}/{safe_name}.pdf"

            create_pdf(report_html, pdf_path, report)

            print(f"✅ PDF created: {pdf_path}")

            generated_files.append(pdf_path)

        except Exception as e:
            print(f"🔥 Error generating report {report}: {e}")

    # ✅ CREATE ZIP
    print("\n📦 Creating ZIP file...")
    zip_path = create_zip(generated_files, session_id)

    print("✅ ZIP ready:", zip_path)

    # 🔥 FINAL FIX: CLEAN PATHS (remove 'outputs/')
    clean_files = [file.replace("outputs/", "") for file in generated_files]
    clean_zip = zip_path.replace("outputs/", "")

    return {
        "files": clean_files,
        "zip": clean_zip
    }