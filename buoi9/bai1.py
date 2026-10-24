from pathlib import Path
from zipfile import BadZipFile, ZipFile
from xml.etree import ElementTree
import re

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font


BASE_DIR = Path(__file__).resolve().parent
COVER_LETTERS_DIR = BASE_DIR / "cover_letters"
OUTPUT_FILE = BASE_DIR / "cover_letters.xlsx"
NOT_FOUND = "Không tìm thấy"

FIELD_NAMES = [
    "Tên file",
    "Họ và tên",
    "Giới tính",
    "Ngày sinh",
    "Nơi sinh",
    "Nguyên quán",
    "Hộ khẩu thường trú",
    "Chỗ ở hiện nay",
    "Điện thoại liên hệ",
    "Dân tộc",
    "Tôn giáo",
    "Số CCCD/CMND",
    "Ngày cấp CCCD/CMND",
    "Nơi cấp CCCD/CMND",
    "Trình độ văn hóa",
    "Sở trường",
]

WORD_NAMESPACE = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
}


def docx_to_text(file_path):
    with ZipFile(file_path) as archive:
        document_xml = archive.read("word/document.xml")

    root = ElementTree.fromstring(document_xml)
    paragraphs = []
    for paragraph in root.findall(".//w:p", WORD_NAMESPACE):
        text = "".join(
            node.text or ""
            for node in paragraph.findall(".//w:t", WORD_NAMESPACE)
        )
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs)


def find_value(text, pattern):
    match = re.search(pattern, text, flags=re.IGNORECASE)
    if not match:
        return NOT_FOUND
    return match.group(1).strip(" \t:-")


def extract_person_info(text):
    full_name = find_value(text, r"Họ và tên:\s*(.*?)(?=\s+Nam/Nữ:|$)")
    gender = find_value(text, r"Nam/Nữ:\s*(.*?)(?=\s*\n|$)")

    birth_match = re.search(
        r"Sinh ngày:\s*(\d{1,2}\s+tháng\s+\d{1,2}\s+năm\s+\d{4})"
        r"\s*Nơi sinh:\s*(.*?)(?=\s*\n|$)",
        text,
        flags=re.IGNORECASE,
    )
    birth_date = birth_match.group(1).strip() if birth_match else NOT_FOUND
    birth_place = birth_match.group(2).strip() if birth_match else NOT_FOUND

    id_match = re.search(
        r"Số CCCD/CMND:\s*(.*?)\s+Cấp ngày:\s*(.*?)\s+Nơi cấp:\s*(.*?)(?=\s*\n|$)",
        text,
        flags=re.IGNORECASE,
    )
    id_number = id_match.group(1).strip() if id_match else NOT_FOUND
    issue_date = id_match.group(2).strip() if id_match else NOT_FOUND
    issue_place = id_match.group(3).strip() if id_match else NOT_FOUND

    return {
        "Họ và tên": full_name,
        "Giới tính": gender,
        "Ngày sinh": birth_date,
        "Nơi sinh": birth_place,
        "Nguyên quán": find_value(
            text, r"Nguyên quán:\s*(.*?)(?=\s*\n|$)"
        ),
        "Hộ khẩu thường trú": find_value(
            text,
            r"Nơi đăng ký hộ khẩu thường trú:\s*(.*?)(?=\s*\n|$)",
        ),
        "Chỗ ở hiện nay": find_value(
            text, r"Chỗ ở hiện nay:\s*(.*?)(?=\s*\n|$)"
        ),
        "Điện thoại liên hệ": find_value(
            text, r"Điện thoại liên hệ:\s*(.*?)(?=\s*\n|$)"
        ),
        "Dân tộc": find_value(
            text, r"Dân tộc:\s*(.*?)(?=\s+Tôn giáo:|$)"
        ),
        "Tôn giáo": find_value(
            text, r"Tôn giáo:\s*(.*?)(?=\s*\n|$)"
        ),
        "Số CCCD/CMND": id_number,
        "Ngày cấp CCCD/CMND": issue_date,
        "Nơi cấp CCCD/CMND": issue_place,
        "Trình độ văn hóa": find_value(
            text, r"Trình độ văn hóa:\s*(.*?)(?=\s*\n|$)"
        ),
        "Sở trường": find_value(
            text, r"Sở trường:\s*(.*?)(?=\s*\n|$)"
        ),
    }


def adjust_column_widths(worksheet):
    for column_cells in worksheet.columns:
        column_letter = column_cells[0].column_letter
        longest_value = max(
            len(str(cell.value)) if cell.value is not None else 0
            for cell in column_cells
        )
        worksheet.column_dimensions[column_letter].width = min(
            max(longest_value + 2, 12),
            60,
        )


def export_cover_letters():
    records = []
    success_count = 0
    error_count = 0

    for file_path in sorted(COVER_LETTERS_DIR.glob("*.docx")):
        try:
            text = docx_to_text(file_path)
            info = extract_person_info(text)
            records.append(
                {
                    "Tên file": file_path.name,
                    **info,
                }
            )
            success_count += 1
        except (
            BadZipFile,
            OSError,
            ElementTree.ParseError,
            KeyError,
            ValueError,
        ) as error:
            error_count += 1
            print(f"Lỗi khi xử lý {file_path.name}: {error}")

    dataframe = pd.DataFrame(records, columns=FIELD_NAMES)
    dataframe.to_excel(
        OUTPUT_FILE,
        index=False,
        sheet_name="Cover letters",
    )

    workbook = load_workbook(OUTPUT_FILE)
    worksheet = workbook["Cover letters"]
    for cell in worksheet[1]:
        cell.font = Font(bold=True)

    worksheet.freeze_panes = "A2"
    worksheet.auto_filter.ref = worksheet.dimensions
    adjust_column_widths(worksheet)
    workbook.save(OUTPUT_FILE)

    print(f"Đã xử lý thành công: {success_count} file")
    print(f"Số file bị lỗi: {error_count} file")
    print(f"Đã xuất dữ liệu ra: {OUTPUT_FILE}")


if __name__ == "__main__":
    export_cover_letters()
