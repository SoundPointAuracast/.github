#!/usr/bin/env python3
"""Build the final engineering workbook (XLSX) for the «Точка звука» project.

Author: Никитин Даниил Константинович (AUTHOR_COUNT = 1).
Evidence-based: no invented measurements or prices. Unknown -> UNKNOWN /
NEEDS QUOTE / NOT MEASURED.
"""
from __future__ import annotations

import os

from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.properties import PageSetupProperties

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "final")
OUT = os.path.join(OUT_DIR, "Точка_звука_Инженерный_пакет_FINAL.xlsx")

# ---------------------------------------------------------------- styles
NAVY = "12305C"
BLUE = "1F6FD0"
LIGHT = "E7F0FB"
LIGHT2 = "F4F6F9"
GREEN = "1E7A46"
GREEN_F = "E3F4E8"
ORANGE = "B35C00"
ORANGE_F = "FDF0E0"
RED_F = "FBE4E4"
GRAY_F = "ECECEC"
YELLOW_F = "FFF6D6"
BLUE_F = "DCEBFB"

H_FONT = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
T_FONT = Font(name="Calibri", size=10)
T_FONT_WRAP = Font(name="Calibri", size=10)
LINK_FONT = Font(name="Calibri", size=10, color="0563C1", underline="single")
BOLD = Font(name="Calibri", size=10, bold=True)
H_FILL = PatternFill("solid", fgColor=NAVY)
THIN = Side(style="thin", color="D7DEE8")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)


def style_header(ws, row: int, ncols: int) -> None:
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = H_FONT
        cell.fill = H_FILL
        cell.alignment = CENTER
        cell.border = BORDER
    ws.row_dimensions[row].height = 30


def write_table(ws, headers, rows, start_row=1, widths=None, freeze=None):
    for j, h in enumerate(headers, 1):
        ws.cell(row=start_row, column=j, value=h)
    style_header(ws, start_row, len(headers))
    for i, row in enumerate(rows, start_row + 1):
        for j, val in enumerate(row, 1):
            cell = ws.cell(row=i, column=j, value=val)
            cell.font = T_FONT
            cell.border = BORDER
            cell.alignment = WRAP
    if widths:
        for j, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(j)].width = w
    last = start_row + len(rows)
    ws.auto_filter.ref = f"A{start_row}:{get_column_letter(len(headers))}{last}"
    if freeze:
        ws.freeze_panes = freeze
    return last


def add_dv(ws, formula1, cell_range):
    dv = DataValidation(type="list", formula1=formula1, allow_blank=True, showDropDown=False)
    ws.add_data_validation(dv)
    dv.add(cell_range)


def status_cf(ws, cell_range):
    """Consistent status colouring."""
    rules = [
        ("DONE", GREEN_F), ("COMPLETED", GREEN_F), ("IMPLEMENTED_MVP", GREEN_F),
        ("READY", GREEN_F), ("YES", GREEN_F), ("SOURCE PRICE", GREEN_F),
        ("CURRENT", BLUE_F), ("READY-ON-HW", BLUE_F), ("PARTIAL", BLUE_F),
        ("NEXT", YELLOW_F), ("PLANNED", YELLOW_F), ("PROPOSED", YELLOW_F),
        ("RESEARCH", YELLOW_F), ("NEEDS QUOTE", ORANGE_F), ("ESTIMATE", ORANGE_F),
        ("FUTURE", GRAY_F), ("UNKNOWN", GRAY_F), ("NOT MEASURED", GRAY_F),
        ("NOT PURCHASED", GRAY_F), ("NO", GRAY_F), ("LEGACY", GRAY_F),
    ]
    for text, fill in rules:
        ws.conditional_formatting.add(
            cell_range,
            CellIsRule(operator="equal", formula=[f'"{text}"'],
                       fill=PatternFill("solid", fgColor=fill)),
        )
    ws.conditional_formatting.add(
        cell_range, CellIsRule(operator="equal", formula=['"HIGH"'],
                               fill=PatternFill("solid", fgColor=RED_F)))


# ---------------------------------------------------------------- data
ANALOG_HEADERS = [
    "ID", "Solution", "Manufacturer", "Current / Legacy / Proposed", "Target users",
    "Education scenario", "Teacher microphone", "Wireless technology", "FM",
    "Proprietary digital", "Auracast", "Dedicated receiver", "Consumer Auracast devices",
    "Direct HA/CI", "T-coil", "Neckloop", "Clean audio output", "USB audio output",
    "Speech-to-text", "Same-source STT", "Live captions", "Timestamped transcript",
    "Missed Speech", "Notes (feature)", "Translation", "AI summary",
    "Confidence handling", "Accessibility profile", "Audio without Internet",
    "Text without Internet", "Special receiver required", "Major strength",
    "Major limitation", "Source ID", "Evidence quality", "Notes",
]

ANALOG_ROWS = [
    ["A-01", "СОНЕТ 2.0", "Исток-Аудио", "Current", "Слабослышащие, СА/КИ",
     "Радиокласс: школа/вуз", "YES", "UHF FM 863–865 МГц", "YES", "NO", "NO", "YES",
     "NO", "PARTIAL", "PARTIAL", "YES", "YES", "NO", "NO", "NO", "NO", "NO", "NO", "NO",
     "NO", "NO", "NO", "NO", "YES", "NO", "YES",
     "Зрелое решение доставки чистого звука; групповое использование; индукционный выход",
     "Нет текстового слоя; закрытый UHF; спец. приёмник у каждого", "SRC-SONET",
     "PRIMARY (vendor official)", "vendor-испытания без peer review"],
    ["A-02", "Phonak Roger ecosystem", "Sonova/Phonak", "Current", "СА/КИ; образование",
     "Удалённый микрофон в классе", "YES", "2.4 ГГц proprietary", "NO", "YES", "NO",
     "YES", "NO", "YES", "PARTIAL", "PARTIAL", "YES", "PARTIAL", "PARTIAL", "PARTIAL",
     "PARTIAL", "UNKNOWN", "NO", "NO", "NO", "NO", "NO", "PARTIAL", "YES", "PARTIAL",
     "YES", "Управляемый SNR; <20 мс; экосистема; приёмники для КИ",
     "Проприетарный транспорт; цена", "SRC-PHONAK", "PRIMARY (vendor official)", ""],
    ["A-03", "Roger NeckLoop", "Sonova/Phonak", "Current", "Любые СА/КИ с T-coil",
     "Универсальный T-coil приёмник", "YES (через Roger mic)", "2.4 ГГц proprietary",
     "NO", "YES", "NO", "YES", "NO", "PARTIAL", "YES", "YES", "YES", "YES", "YES",
     "YES", "PARTIAL", "PARTIAL", "NO", "NO", "NO", "NO", "NO", "PARTIAL", "YES",
     "PARTIAL", "YES", "T-coil + USB audio; официальный сценарий speech-to-text (2021)",
     "Текст на подключённом компьютере; нет привязки к сессии", "SRC-PHONAK",
     "PRIMARY (vendor official)", "CRITICAL PRIOR ART для clean-feed → STT"],
    ["A-04", "Roger MyLink", "Sonova/Phonak", "Legacy", "Любые СА/КИ с T-coil",
     "Исторический T-coil приёмник", "YES (через Roger mic)", "2.4 ГГц proprietary",
     "NO", "YES", "NO", "YES", "NO", "PARTIAL", "YES", "YES", "YES", "NO", "NO", "NO",
     "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "YES", "NO", "YES",
     "Ранний пример класса wireless→neckloop→T-coil", "EOL; без USB; снят с поддержки",
     "SRC-PHONAK", "PRIMARY (archived official)", "legacy/исторический аналог"],
    ["A-05", "Auri", "Ampetronic/Listen", "Current", "Учреждения, вузы",
     "Auracast ALS (Dante)", "YES (через аудиосистему)", "Auracast (BLE)", "NO", "NO",
     "YES", "YES", "YES", "PARTIAL", "YES", "YES", "YES", "UNKNOWN", "NO", "NO", "NO",
     "NO", "NO", "NO", "NO", "NO", "NO", "NO", "YES", "NO", "YES",
     "Auracast + RX1 + neckloop; внедрения (Oxford, UAL)", "Нет текста; нужен приёмник",
     "SRC-AURI", "PRIMARY (vendor/SIG)", ""],
    ["A-06", "Bettear", "Bettear", "Current", "Учреждения, вузы",
     "Auracast + venue captions", "YES (через аудиосистему)", "Auracast (BLE)", "NO",
     "NO", "YES", "YES", "YES", "PARTIAL", "YES", "YES", "YES", "YES", "PARTIAL",
     "PARTIAL", "PARTIAL", "PARTIAL", "NO", "NO", "PARTIAL", "NO", "NO", "UNKNOWN",
     "NO", "PARTIAL", "YES", "Auracast + venue transcription + RTX USB feed",
     "Нет дословного «Не расслышал»; venue-инфраструктура", "SRC-BETTEAR",
     "PRIMARY (vendor)", ""],
    ["A-07", "HearAura", "HearAura (indie)", "Current", "Пользователи iPhone",
     "Auracast assistant + captions", "NO", "Auracast (assistant) + mic", "NO", "NO",
     "YES", "NO", "YES", "PARTIAL", "NO", "NO", "PARTIAL", "NO", "YES", "PARTIAL",
     "YES", "PARTIAL", "PARTIAL (summary)", "NO", "UNKNOWN", "YES", "NO", "YES", "YES",
     "YES", "NO", "Единственное найденное сочетание Auracast + captions",
     "iOS-centric; «Catch me up» — summary, не дословный replay", "SRC-HEARAURA",
     "PRIMARY (product site)", ""],
    ["A-08", "Ava", "Ava", "Current", "Школы/вузы, DHH",
     "Live captions в классе", "NO", "BT / mic", "NO", "NO", "NO", "NO", "NO", "NO",
     "NO", "NO", "NO", "NO", "YES", "NO", "YES", "YES", "NO (scrollback)", "YES", "YES",
     "YES", "NO", "YES", "PARTIAL", "PARTIAL", "NO",
     "Зрелые live captions, заметки, Scribe", "Не ALS; зависит от микрофона/облака",
     "SRC-AVA", "PRIMARY (product site)", ""],
    ["A-09", "Google Live Transcribe", "Google", "Current", "Широкая аудитория",
     "Captions на Android", "NO", "Device audio / mic", "NO", "NO", "NO", "NO", "NO",
     "NO", "NO", "NO", "NO", "NO", "YES", "NO", "YES", "YES", "PARTIAL (Hold/scrollback)",
     "NO", "PARTIAL", "NO", "NO", "YES", "PARTIAL", "YES", "NO",
     "Доступно; on-device; hold/scrollback", "Мic-based; не связано с ALS",
     "SRC-GOOGLE", "PRIMARY (official docs)", ""],
    ["A-10", "Точка звука / Route+ [PROPOSED]", "Никитин Д.К. (автор проекта)",
     "Proposed", "PRIMARY: СА/КИ; SECONDARY: широкая аудитория", "Единая образовательная сессия",
     "PROPOSED (clean feed)", "Auracast (PROPOSED)", "NO", "NO", "PROPOSED", "RESEARCH",
     "PROPOSED", "PROPOSED", "PROPOSED", "PROPOSED", "PROPOSED", "PROPOSED", "PROPOSED",
     "PROPOSED", "IMPLEMENTED_MVP", "IMPLEMENTED_MVP", "IMPLEMENTED_MVP",
     "IMPLEMENTED_MVP", "PROPOSED (PHASE_2)", "RESEARCH", "RESEARCH", "IMPLEMENTED_MVP",
     "PROPOSED", "RESEARCH", "PARTIAL",
     "Единая сессия: аудио + синхронизированный текст; «Не расслышал»",
     "Hardware не закуплен; реальный ASR не реализован; часть — research",
     "SRC-INTERNAL", "PROJECT (implementation evidence)", "clean-feed и Bridge-T не заявлены новизной"],
]

BOM_HEADERS = [
    "Item ID", "Subsystem", "Item", "Manufacturer", "Model", "Purpose",
    "Required / Optional", "Quantity", "Unit", "Unit Price", "Currency",
    "Estimated Total", "Price Status", "Price Date", "Source", "Purchased?",
    "Existing?", "Experiment IDs", "Notes",
]
# rows: unit price blank when no verified price; Estimated Total is a formula.
BOM_ROWS = [
    ["BOM-A-01", "A. Research stand", "LE Audio devkit (Broadcast Source + Sink)",
     "Nordic Semiconductor", "nRF5340 Audio DK", "Source и sink, контроль LC3/QoS",
     "Required", 2, "pcs", 172.57, "USD", None, "Estimate", None,
     "https://www.nordicsemi.com/Products/Development-hardware/nRF5340-Audio-DK",
     "NOT PURCHASED", "NO", "E01;E03;E04", "Ориентир ~$172.57/pc (DigiKey); цену подтвердить"],
    ["BOM-A-02", "A. Research stand", "Microphone / audio source", "TBD", "TBD",
     "Подача речи на line-in", "Required", 1, "pcs", None, "USD", None, "NEEDS QUOTE",
     None, "PURCHASE_DECISION.md", "NO", "UNKNOWN", "E01;E04", "Модель не выбрана"],
    ["BOM-A-03", "A. Research stand", "3.5 mm cables / adapters", "TBD", "TBD",
     "Подключение line-in/out", "Required", 4, "pcs", None, "USD", None, "NEEDS QUOTE",
     None, "PURCHASE_DECISION.md", "NO", "UNKNOWN", "E01;E04;E07", ""],
    ["BOM-A-04", "A. Research stand", "USB cables", "TBD", "TBD", "Питание/данные devkit",
     "Optional", 2, "pcs", None, "USD", None, "NEEDS QUOTE", None,
     "PURCHASE_DECISION.md", "NO", "UNKNOWN", "E01;E03", "Часто идут в комплекте"],
    ["BOM-A-05", "A. Research stand", "PC / laptop", "Existing", "TBD",
     "Управление, логи, ASR", "Required", 1, "pcs", None, "USD", None, "NOT PURCHASED",
     None, "EXISTING", "YES", "E01;E03;E04;E05", "Предполагается имеющимся"],
    ["BOM-A-06", "A. Research stand", "Measurement audio interface / oscilloscope",
     "TBD", "TBD", "Измерение задержки", "Required", 1, "pcs", None, "USD", None,
     "NEEDS QUOTE", None, "LATENCY_TEST_PROTOCOL.md", "NO", "UNKNOWN", "E01",
     "Наличие не подтверждено"],
    ["BOM-B-01", "B. Low-cost demo", "Auracast USB transmitter/receiver",
     "Flairmesh", "FlooGoo FMA120", "Быстрый источник/приёмник для демо",
     "Optional", 1, "pcs", None, "USD", None, "NEEDS QUOTE", None,
     "https://www.flairmesh.com/Dongle/FMA120.html", "NO", "NO", "DEMO",
     "Vendor-диапазон ~$45–130; точную цену подтвердить"],
    ["BOM-B-02", "B. Low-cost demo", "Auracast receiver with analog out",
     "Avantree", "AuraClip (RC240)", "Приёмник с 3.5 мм выходом", "Optional", 1, "pcs",
     69.99, "EUR", None, "SOURCE PRICE", "2026-09-26",
     "https://avantree.com/products/auraclip-auracast-receiver", "NO", "NO",
     "DEMO;E07", ""],
    ["BOM-B-03", "B. Low-cost demo", "Auracast USB transmitter", "MoerLab",
     "MoerLink / DB100", "Альтернативный источник", "Optional", 1, "pcs", 59.00, "USD",
     None, "SOURCE PRICE", "2026-09-26", "https://www.moor-audio.com/collections/transmitter",
     "NO", "NO", "DEMO", "Альтернатива, не совместная обязательная закупка"],
    ["BOM-C-01", "C. Bridge-T experiment", "Auracast sink (analog output)",
     "Avantree", "AuraClip (RC240) / nRF5340 DK", "Источник аудио для индукции",
     "Required", 1, "pcs", 69.99, "EUR", None, "SOURCE PRICE", "2026-09-26",
     "BRIDGE_T_MVP_SPEC.md", "NO", "NO", "E07", "Может быть взят из B"],
    ["BOM-C-02", "C. Bridge-T experiment", "Induction neckloop", "Williams AV",
     "NKL 001", "Магнитное поле для T/MT", "Required", 1, "pcs", 78.00, "USD", None,
     "SOURCE PRICE", "2026-09-26", "https://williamsav.com/product/nkl-001/", "NO",
     "NO", "E07", "Альтернатива HearCoil"],
    ["BOM-C-03", "C. Bridge-T experiment", "Induction neckloop (alternative)",
     "Avantree", "HearCoil", "Альтернативный neckloop", "Optional", 1, "pcs", 69.99,
     "EUR", None, "SOURCE PRICE", "2026-09-26", "https://avantree.com/collections/t-coil-accessories",
     "NO", "NO", "E07", "Pre-order"],
    ["BOM-C-04", "C. Bridge-T experiment", "Hearing aid / CI with T/MT access",
     "TBD (participant device)", "TBD", "Приём T/MT сигнала", "Required", 1, "pcs",
     None, "USD", None, "NEEDS QUOTE", None, "BRIDGE_T_MVP_SPEC.md", "NO", "UNKNOWN",
     "E07", "Наличие подходящего устройства не подтверждено"],
    ["BOM-C-05", "C. Bridge-T experiment", "Cables / adapters", "TBD", "TBD",
     "Подключение индукционного каскада", "Required", 2, "pcs", None, "USD", None,
     "NEEDS QUOTE", None, "BRIDGE_T_MVP_SPEC.md", "NO", "UNKNOWN", "E07", ""],
    ["BOM-C-06", "C. Bridge-T experiment", "Measurement equipment (field/level)",
     "TBD", "TBD", "Измерение индукционного поля", "Optional", 1, "pcs", None, "USD",
     None, "NEEDS QUOTE", None, "BRIDGE_T_MVP_SPEC.md", "NO", "UNKNOWN", "E07", ""],
    ["BOM-D-01", "D. ASR experiment", "Smartphone for phone-mic arm", "TBD", "TBD",
     "Канал PHONE_MIC в E05", "Required", 2, "pcs", None, "USD", None, "NEEDS QUOTE",
     None, "ASR_COMPARISON_PROTOCOL.md", "NO", "UNKNOWN", "E05",
     "Разные классы телефонов; наличие не подтверждено"],
    ["BOM-D-02", "D. ASR experiment", "Clean-feed capture device", "TBD", "TBD",
     "Канал CLEAN_FEED в E05", "Required", 1, "pcs", None, "USD", None, "NEEDS QUOTE",
     None, "ASR_COMPARISON_PROTOCOL.md", "NO", "UNKNOWN", "E05", ""],
    ["BOM-D-03", "D. ASR experiment", "Local ASR software (T-one)", "VoiceKit/T-Bank",
     "T-one (Apache-2.0)", "Streaming распознавание для E05", "Required", 1, "license",
     0.00, "USD", None, "SOURCE PRICE", "2026-09-26",
     "https://github.com/voicekit-team/T-one", "NO", "NO", "E05", "Бесплатно; веса НЕ скачаны"],
    ["BOM-D-04", "D. ASR experiment", "Local ASR software (GigaAM-v3)", "Sber",
     "GigaAM-v3 RNNT (MIT)", "Batch-эталон для WER", "Optional", 1, "license", 0.00,
     "USD", None, "SOURCE PRICE", "2026-09-26", "https://github.com/salute-developers/GigaAM",
     "NO", "NO", "E05", "Бесплатно; веса НЕ скачаны"],
]

PURCHASE_HEADERS = [
    "Scenario", "Item", "Qty", "Currency", "Unit Price", "Cost", "Mandatory?",
    "Why", "Blocks experiment?", "Purchase priority", "Source", "Status",
]
PURCHASE_ROWS = [
    ["SCENARIO A — Research", "Nordic nRF5340 Audio DK", 2, "USD", "='02_BOM'!J2",
     None, "YES", "Полный контроль LC3/QoS/PD", "YES", "P1",
     "https://www.nordicsemi.com/Products/Development-hardware/nRF5340-Audio-DK",
     "NOT PURCHASED"],
    ["SCENARIO A — Research", "Microphone / audio source", 1, "USD", "='02_BOM'!J3",
     None, "YES", "Подача речи для E01/E04", "YES", "P1", "PURCHASE_DECISION.md",
     "NEEDS QUOTE"],
    ["SCENARIO A — Research", "3.5 mm cables / adapters", 4, "USD", "='02_BOM'!J4",
     None, "YES", "Коммутация стенда", "YES", "P2", "PURCHASE_DECISION.md", "NEEDS QUOTE"],
    ["SCENARIO A — Research", "Measurement audio interface / oscilloscope", 1, "USD",
     "='02_BOM'!J7", None, "YES", "Измерение задержки E01", "YES", "P1",
     "LATENCY_TEST_PROTOCOL.md", "NEEDS QUOTE"],
    ["SCENARIO B — Low-cost demo", "FlooGoo FMA120", 1, "USD", "='02_BOM'!J8", None,
     "NO", "Быстрый источник/приёмник", "NO", "P2",
     "https://www.flairmesh.com/Dongle/FMA120.html", "NEEDS QUOTE"],
    ["SCENARIO B — Low-cost demo", "Avantree AuraClip (RC240)", 1, "EUR",
     "='02_BOM'!J9", None, "NO", "Приёмник с аналоговым выходом", "NO", "P2",
     "https://avantree.com/products/auraclip-auracast-receiver", "NOT PURCHASED"],
    ["SCENARIO B — Low-cost demo", "MoerLab MoerLink / DB100", 1, "USD", "='02_BOM'!J10",
     None, "NO", "Альтернативный источник", "NO", "P3",
     "https://www.moor-audio.com/collections/transmitter", "NOT PURCHASED"],
    ["SCENARIO C — Minimum E05 (software)", "PC / laptop", 1, "USD", "='02_BOM'!J6",
     None, "YES", "Хостинг ASR и логирование", "NO", "P0",
     "ASR_COMPARISON_PROTOCOL.md", "EXISTING"],
    ["SCENARIO C — Minimum E05 (software)", "Smartphone for phone-mic arm", 2, "USD",
     "='02_BOM'!J17", None, "YES", "Канал PHONE_MIC", "YES", "P1",
     "ASR_COMPARISON_PROTOCOL.md", "NEEDS QUOTE"],
    ["SCENARIO C — Minimum E05 (software)", "Local ASR software (T-one + GigaAM-v3)",
     2, "USD", "='02_BOM'!J19", None, "YES", "Распознавание и WER", "YES", "P0",
     "https://github.com/voicekit-team/T-one", "SOURCE PRICE"],
]

EXP_HEADERS = [
    "Experiment ID", "Title", "Purpose", "Status", "Hardware Required",
    "Software Required", "Input", "Output", "Primary Metric", "Secondary Metrics",
    "Independent Variables", "Controlled Variables", "Number of Repetitions",
    "Acceptance Criterion", "CSV File", "Responsible", "Planned Date", "Actual Date",
    "Result Status", "Result", "Notes",
]
AUTHOR = "Никитин Даниил Константинович"
EXP_ROWS = [
    ["E01", "Audio latency", "Измерить сквозную задержку аудиотракта", "PLANNED",
     "2× nRF5340 Audio DK; measurement interface/oscilloscope",
     "nRF Connect SDK (broadcast source/sink)", "Электрический вход TX (burst/чирп)",
     "Аналоговый выход RX", "end-to-end latency (mean/median/p95/max)",
     "jitter; потери; разложение по звеньям", "QoS (16_2_1/16_2_2/24_2_1/24_2_2); PD 20/30/40 мс",
     "Материал сигнала; условия помещения", "≥100 на конфигурацию", "TARGET ≤60 мс; ≤100 допустимо; >150 — брак",
     "e01_latency.csv", AUTHOR, None, None, "NOT MEASURED", None,
     "SOURCE POINT = электрический вход TX; END POINT = аналоговый выход RX"],
    ["E03", "Packet stability", "Оценить устойчивость потока во времени", "PLANNED",
     "Стенд E01", "Логирование", "Непрерывный аудиопоток", "Выход RX + логи",
     "Разрывы/глитчи/потери", "Длительность без сбоев", "Условия эфира/движение людей",
     "QoS; дистанция", "≥3 прогона по ≥1 ч", "Нет разрывов в сценарии лекции",
     "e03_stability.csv", AUTHOR, None, None, "NOT MEASURED", None, ""],
    ["E04", "LC3 configuration comparison", "Сравнить конфигурации LC3", "PLANNED",
     "Стенд E01", "Управление конфигурациями", "Один речевой материал",
     "Записи выходов + субъективные оценки", "Субъективное/объективное качество",
     "Latency; airtime; совместимость", "16_2_1;16_2_2;24_2_1;24_2_2;48_2",
     "Материал; слушатели", "≥3 фрагмента × ≥8 слушателей, слепое сравнение",
     "Выбранная база проходит и технически, и субъективно", "e04_lc3.csv", AUTHOR,
     None, None, "NOT MEASURED", None, "Baseline 24_2_1 — не победитель, а стартовая гипотеза"],
    ["E05", "Clean-feed vs smartphone ASR", "Сравнить WER/CER на чистом фиде и микрофоне",
     "PLANNED", "ПК; 2 телефона; clean-feed capture", "T-one; GigaAM-v3 (эталон)",
     "Синхронная запись CLEAN_FEED и PHONE_MIC", "Транскрипты + метрики",
     "WER", "CER; caption latency; finalization latency; partial revisions",
     "Условия A–E; канал", "Материал; модель ASR; параметры декодирования",
     "≥10 повторов на условие", "Измеримое преимущество clean-feed (или его отсутствие)",
     "e05_asr.csv", AUTHOR, None, None, "NOT MEASURED", None,
     "См. лист 05_E05_ASR (template)"],
    ["E07", "Bridge-T audio transfer", "Проверить Auracast → индукция → T/MT", "PLANNED",
     "Auracast sink с аналоговым выходом; neckloop; СА/КИ с T/MT",
     "Без ПО (аудиотракт)", "Эфир Auracast", "Слышимость/разборчивость в T-режиме",
     "Уровень/разборчивость (субъективно)", "Гул; влияние расстояния 1–10 см",
     "Катушка; расстояние; экранирование", "Источник; материал", "≥10 прослушиваний",
     "Стабильный разборчивый сигнал без гула сверх ожидаемого", "e07_bridge.csv",
     AUTHOR, None, None, "NOT MEASURED", None, "Класс устройств известен (Roger/Auri/Bettear/AuraCoil)"],
]

E05_HEADERS = [
    "Trial ID", "Speech Material ID", "Condition", "Distance (m)", "Noise Condition",
    "Reverberation Condition", "Channel", "ASR Model", "Reference Text",
    "Recognized Text", "Word Count Reference (N)", "Substitutions (S)",
    "Deletions (D)", "Insertions (I)", "WER", "Reference Characters",
    "Character Errors", "CER", "Caption Start Latency ms", "Finalization Latency ms",
    "Partial Revisions", "Notes",
]
E05_ROWS = []
for cond, dist, noise, rev in [
    ("A quiet / near", 1, "None", "Low"),
    ("B far row", "10-20", "None", "Medium"),
    ("C background noise", "5-10", "Recorded hall noise", "Medium"),
    ("D reverberation", "5-10", "None", "High"),
    ("E noise + distance", "10-20", "Recorded hall noise", "High"),
]:
    for ch in ("CLEAN_FEED", "PHONE_MIC"):
        E05_ROWS.append(["", "", cond, dist, noise, rev, ch, "", "", "", None, None, None,
                         None, None, None, None, None, None, None, None, ""])
# Pre-fill WER/CER formulas for all rows (blank if inputs blank / div by zero)
for idx in range(len(E05_ROWS)):
    r = idx + 2
    E05_ROWS[idx][14] = f'=IFERROR(IF(N(K{r})=0,"",(N(K{r})+N(L{r})+N(M{r}))/K{r}),"")'
    E05_ROWS[idx][17] = f'=IFERROR(IF(N(P{r})=0,"",N(Q{r})/P{r}),"")'

RISK_HEADERS = [
    "Risk ID", "Category", "Risk", "Evidence", "Probability", "Impact", "Priority",
    "Mitigation", "Trigger", "Owner", "Status", "Source",
]
RISK_ROWS = [
    ["R-01", "Novelty", "Roger NeckLoop уже реализует clean-feed → STT (prior art)",
     "Phonak STT guide V1.00/2021-04; product FAQ", "HIGH", "HIGH", None,
     "Не заявлять clean-feed как новизну; сместить отличие в системный слой",
     "Попытка позиционировать clean-feed как новизну", AUTHOR, "OPEN", "AR-01"],
    ["R-02", "Novelty", "Bridge-T — известный класс устройств", "Roger MyLink/NeckLoop, Auri RX1, Bettear RTX, AuraCoil",
     "HIGH", "HIGH", None, "Исследовать только конкретные технические отличия", "Патентная заявка на класс",
     AUTHOR, "OPEN", "AR-02"],
    ["R-03", "Competition", "Bettear/HearAura уже соединяют аудио и текст", "vendor sites; COMPETITOR_MATRIX",
     "MEDIUM", "HIGH", None, "Дифференциация: сессия, общий таймлайн, missed speech",
     "Конкурент выпускает аналог", AUTHOR, "OPEN", "AR-08"],
    ["R-04", "Novelty", "Missed Speech имеет предшественников", "US20090076804 (Bionica, 2007); Apple TV/Roku",
     "MEDIUM", "MEDIUM", None, "Позиционировать как UX-дифференциатор, не патент",
     "Патентная заявка на механику", AUTHOR, "OPEN", "AR-09"],
    ["R-05", "Legal", "Неполный патентный поиск", "Google Patents частично недоступен; 18-мес. лаг; Espacenet/USPTO недоступны",
     "HIGH", "HIGH", None, "Профессиональный поиск (GATE 7) до любых заявлений",
     "Подача заявки без поиска", AUTHOR, "OPEN", "RED TEAM RT-07"],
    ["R-06", "Market", "Малый установленный парк Auracast-устройств СА/КИ",
     "DEVICE_COMPATIBILITY_MATRIX; Phonak: «very few hearing devices support Auracast»",
     "HIGH", "HIGH", None, "Bridge-T для T/MT; text-only путь", "Массовое развёртывание без совместимости",
     AUTHOR, "OPEN", "AR-03"],
    ["R-07", "Technical", "Фрагментация совместимости Auracast", "DEVICE_COMPATIBILITY_MATRIX; vendor statements",
     "MEDIUM", "HIGH", None, "Матрица совместимости; тесты E02/E04", "Несовместимость на пилоте",
     AUTHOR, "OPEN", "AR-05"],
    ["R-08", "Methodology", "Смешение TARGET и RESULT", "LATENCY_DEEP_DIVE; legacy «≤300 мс»",
     "MEDIUM", "MEDIUM", None, "Явные маркеры TARGET/ACCEPTANCE; NOT MEASURED в отчётах",
     "Публикация целевых значений как результатов", AUTHOR, "OPEN", "AR-06"],
    ["R-09", "Technical", "Нет собственных аппаратных измерений", "EXPERIMENT_READINESS_GATE6: E01/E03/E04/E07 не выполнены",
     "HIGH", "MEDIUM", None, "Провести E01/E03/E04/E07 после закупки стенда", "Заявления без измерений",
     AUTHOR, "OPEN", "PROJECT_STATE"],
    ["R-10", "Dependency", "Зависимость от совместимого приёмного оборудования",
     "DEVICE_COMPATIBILITY_MATRIX; special receiver required", "MEDIUM", "HIGH", None,
     "Прямой Auracast + Bridge-T + text-only; заёмные приёмники для пилота",
     "Отсутствие устройств у участников", AUTHOR, "OPEN", "AR-14"],
    ["R-11", "Privacy", "Обработка речи и персональных данных", "PRIVACY_REQUIREMENTS",
     "MEDIUM", "HIGH", None, "privacy-by-default; без хранения аудио; политика ретенции",
     "Пилот без процедуры согласия", AUTHOR, "OPEN", "PRIVACY_REQUIREMENTS"],
    ["R-12", "Operational", "Hardware не закуплен, сроки поставки", "PURCHASE_DECISION; availability notes",
     "MEDIUM", "MEDIUM", None, "Закупка по решению руководителя; low-cost альтернатива",
     "Задержка поставки", AUTHOR, "OPEN", "PURCHASE_DECISION"],
]

ROADMAP_HEADERS = [
    "Stage", "Task", "Status", "Prerequisite", "Deliverable", "Start", "Finish",
    "Evidence", "Notes",
]
ROADMAP_ROWS = [
    ["DONE", "Source audit", "DONE", "—", "SOURCE_INVENTORY; source_register",
     "—", "—", "01_sources/", ""],
    ["DONE", "Standards & Auracast research", "DONE", "Source audit",
     "AURACAST_TECHNICAL_MAP; PROFILE_REQUIREMENTS", "—", "—", "02_research/", ""],
    ["DONE", "Competitor analysis", "DONE", "Research", "COMPETITOR_MATRIX; SONET/Roger cards",
     "—", "—", "08_competitor_analysis/", ""],
    ["DONE", "Software MVP (Route+)", "DONE", "Architecture", "APP_MVP_SPEC; working MVP",
     "—", "—", "06_application/", "19+4 теста; demo mode"],
    ["DONE", "Final presentation", "DONE", "Research", "FINAL.pptx / FINAL.pdf",
     "—", "—", "11_presentations/final/", ""],
    ["DONE", "Final article", "DONE", "Research", "FINAL.docx / FINAL.pdf",
     "—", "—", "12_reports/article/", "2 страницы"],
    ["CURRENT", "Engineering workbook (this package)", "CURRENT", "Research",
     "Инженерный пакет FINAL.xlsx", "—", "—", "12_reports/excel/", ""],
    ["NEXT", "Hardware purchase", "NEXT", "Workbook + lead decision",
     "Закупленный стенд", None, None, "PURCHASE_DECISION.md", "Не закуплено"],
    ["NEXT", "E05 Local ASR integration", "NEXT", "PC + ASR software",
     "ASR_COMPARISON results", None, None, "LOCAL_ASR_INTEGRATION_PLAN.md", "Веса не скачаны"],
    ["NEXT", "E01 latency", "NEXT", "Research stand", "e01_latency.csv + отчёт",
     None, None, "LATENCY_TEST_PROTOCOL.md", ""],
    ["NEXT", "E03 stability", "NEXT", "Research stand", "e03_stability.csv", None, None,
     "EXPERIMENT_READINESS_GATE6.md", ""],
    ["NEXT", "E04 LC3 configurations", "NEXT", "Research stand", "e04_lc3.csv", None, None,
     "EXPERIMENT_READINESS_GATE6.md", ""],
    ["NEXT", "E07 Bridge-T", "NEXT", "Auracast sink + neckloop + HA/CI", "e07_bridge.csv",
     None, None, "BRIDGE_T_MVP_SPEC.md", ""],
    ["FUTURE", "Patent search (professional)", "FUTURE", "Differentiation ready",
     "Patent search report", None, None, "PRIOR_ART.md", "GATE 7"],
    ["FUTURE", "Pilot classroom", "FUTURE", "Experiments E05/E01/E03 passing",
     "Pilot report", None, None, "ROADMAP.md", ""],
    ["FUTURE", "Optional RID", "FUTURE", "Patent search + MVP",
     "RID materials", None, None, "09_novelty_rid/", "Только после поиска"],
]

SOURCE_HEADERS = [
    "Source ID", "Title", "Organisation / Author", "Year", "Type", "PRIMARY?",
    "PEER-REVIEWED?", "SECONDARY?", "URL / File", "Access Date", "Claims Supported",
    "Used In", "Current?", "Notes",
]
SOURCE_ROWS = [
    ["SRC-SIG-PBP", "Public Broadcast Profile 1.0.1", "Bluetooth SIG", "2023",
     "Specification", "YES", "NO", "NO",
     "https://www.bluetooth.com/specifications/specs/public-broadcast-profile/",
     "2026-09-26", "Auracast, роли PBS/PBK/PBA, SQ/HQ", "Article; AURACAST_TECHNICAL_MAP",
     "YES", ""],
    ["SRC-SIG-BAP", "Basic Audio Profile 1.0.1", "Bluetooth SIG", "2023",
     "Specification", "YES", "NO", "NO",
     "https://www.bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/",
     "2026-09-26", "Роли BAP; конфигурации 16/24/48 кГц; QoS; PD", "Article; LC3_CONFIGURATION_MATRIX",
     "YES", ""],
    ["SRC-SIG-BASS", "Broadcast Audio Scan Service 1.0", "Bluetooth SIG", "2022",
     "Specification", "YES", "NO", "NO",
     "https://www.bluetooth.com/specifications/specs/broadcast-audio-scan-service/",
     "2026-09-26", "Обязательность BASS на приёмнике", "AURACAST_TECHNICAL_MAP", "YES",
     "В статью не вошёл (лимит 2 стр.)"],
    ["SRC-PHONAK", "Roger NeckLoop: USB audio and speech-to-text (incl. STT guide V1.00/2021-04)",
     "Sonova / Phonak", "2021", "Vendor documentation", "YES", "NO", "NO",
     "https://www.phonak.com/en-us/hearing-devices/microphones/roger-neckloop",
     "2026-09-26", "USB→STT prior art; T-coil; задержка <20 мс", "Article; PHONAK_ROGER",
     "YES", "CRITICAL PRIOR ART"],
    ["SRC-SONET", "Радиокласс «СОНЕТ 2.0»", "Исток-Аудио", "2026",
     "Vendor documentation (official catalog)", "YES", "NO", "NO",
     "https://www.istok-audio.com/catalog/product/radioklass_sonet_2_0/", "2026-09-26",
     "СОНЕТ 2.0: характеристики, T/TM, группы", "Article; SONET_2_0", "YES",
     "Vendor-run tests без peer review"],
    ["SRC-ANDROID", "Bluetooth LE Audio", "Android Developers / Google", "2026",
     "Platform documentation", "YES", "NO", "NO",
     "https://developer.android.com/develop/connectivity/bluetooth/ble-audio/overview",
     "2026-09-26", "Ограничения API для сторонних приложений", "Article; MOBILE_AURACAST_SUPPORT",
     "YES", ""],
    ["SRC-BRADLEY", "The intelligibility of speech in elementary school classrooms",
     "Bradley J.S., Sato H.", "2008", "Peer-reviewed research", "NO", "YES", "NO",
     "DOI: 10.1121/1.2839285", "2026-09-26", "Акустика класса; +15 дБ SNR",
     "Article; CLEAN_FEED_ASR_RESEARCH", "YES", "JASA 123(4):2078–2086"],
    ["SRC-UQ", "UQ creates change for accessibility students",
     "University of Queensland", "2026", "University official news", "YES", "NO", "NO",
     "https://news.uq.edu.au/2026-03-uq-creates-change-accessibility-students",
     "2026-09-26", "Auracast в 65 аудиториях; ограничение iPhone-assistant",
     "Article; REAL_WORLD_DEPLOYMENTS", "YES", "PRIMARY для собственного внедрения"],
    ["SRC-AURI", "Auri ALS; кейсы Oxford/UAL", "Ampetronic / Listen Technologies",
     "2025", "Vendor documentation + case studies", "YES", "NO", "PARTIAL",
     "https://www.auriaudio.com/", "2026-09-26", "Реальные внедрения Auracast ALS",
     "REAL_WORLD_DEPLOYMENTS; COMPETITOR_MATRIX", "YES", "Vendor + press для Oxford"],
    ["SRC-BETTEAR", "Bettear: education и RTX USB feed", "Bettear", "2026",
     "Vendor documentation", "YES", "NO", "NO", "https://bettear.com/", "2026-09-26",
     "Auracast + venue captions + RTX STT feed", "COMPETITOR_MATRIX", "YES", ""],
    ["SRC-HEARAURA", "HearAura — Auracast assistant + captions", "HearAura (indie)",
     "2026", "Product site", "YES", "NO", "NO", "https://hearaura.app/", "2026-09-26",
     "Auracast + captions; «Catch me up»", "ASSISTIVE_APP_LANDSCAPE", "YES", ""],
    ["SRC-AVA", "Ava live captions", "Ava", "2026", "Product site", "YES", "NO", "NO",
     "https://www.ava.me/", "2026-09-26", "Функции live captions/notes", "ASSISTIVE_APP_LANDSCAPE",
     "YES", ""],
    ["SRC-GOOGLE", "Google Live Transcribe / Live Caption", "Google", "2026",
     "Official product docs", "YES", "NO", "NO",
     "https://support.google.com/accessibility/android/answer/9158064", "2026-09-26",
     "Captions/hold/scrollback", "ASSISTIVE_APP_LANDSCAPE", "YES", ""],
    ["SRC-NORDIC", "nRF5340 Audio DK", "Nordic Semiconductor", "2026",
     "Vendor documentation", "YES", "NO", "NO",
     "https://www.nordicsemi.com/Products/Development-hardware/nRF5340-Audio-DK",
     "2026-09-26", "Характеристики devkit", "DEVKIT_COMPARISON; PURCHASE_DECISION",
     "YES", ""],
    ["SRC-INTERNAL", "Проектные документы (MVP, архитектура, эксперименты, статья, презентация)",
     "Никитин Даниил Константинович", "2026", "Internal project evidence", "YES", "NO", "NO",
     "PROJECT_STATE.md", "2026-09-26", "Реализация Route+; архитектура; протоколы",
     "PROJECT_STATE; MASTER_REPORT", "YES", "AUTHOR_COUNT = 1"],
    ["SRC-LEGACY", "Исторические материалы проекта (S001–S011)", "автор проекта",
     "2024–2026", "Internal legacy/current sources", "NO", "NO", "YES",
     "01_sources/", "2026-09-26", "Историческое развитие проекта", "SOURCE_INVENTORY",
     "LEGACY", "Не source of truth"],
]

DECISION_HEADERS = [
    "Decision ID", "Date", "Decision", "Reason", "Alternatives", "Evidence", "Status",
    "Impact", "Source",
]
DECISION_ROWS = [
    ["D-003", "2026-09-26", "Не заявлять мировую новизну", "Нет патентного поиска",
     "Заявлять новизну", "DIFFERENTIATION_STATEMENT", "ACCEPTED", "Высокое",
     "DECISIONS.md"],
    ["D-015", "2026-09-26", "Route+ вне аудио-цепочки Auracast", "Ограничения API мобильных ОС",
     "Собственный Auracast stack", "MOBILE_AURACAST_SUPPORT", "ACCEPTED", "Высокое",
     "DECISIONS.md"],
    ["D-012", "2026-09-26", "ASR питается от PCM до LC3", "Независимость от кодека; качество ASR",
     "Декодированный LC3 поток", "SYSTEM_ARCHITECTURE", "ACCEPTED", "Высокое",
     "DECISIONS.md"],
    ["D-013", "2026-09-26", "24_2_1 — engineering baseline", "SIG-рекомендация HA-HQ",
     "16_2_1; 48 кГц", "LC3_CONFIGURATION_MATRIX", "ACCEPTED", "Среднее",
     "DECISIONS.md"],
    ["D-014", "2026-09-26", "Latency ≤60 мс target; ≤100 acceptable", "Эхо при смешении с живым звуком",
     "≤300 мс (отклонено)", "LATENCY_DEEP_DIVE", "ACCEPTED", "Высокое", "DECISIONS.md"],
    ["D-022", "2026-09-26", "Bridge-T не заявлен новизной (KNOWN_CLASS)",
     "Roger MyLink/NeckLoop, Auri, Bettear, AuraCoil", "Заявлять класс как новизну",
     "AURACAST_TELECOIL_PRIOR_ART", "ACCEPTED", "Высокое", "DECISIONS.md"],
    ["D-021", "2026-09-26", "Clean-feed STT не является новизной",
     "Roger NeckLoop USB→STT (2021)", "Заявлять clean-feed как новизну",
     "PHONAK_ROGER", "ACCEPTED", "Высокое", "DECISIONS.md"],
    ["D-020", "2026-09-26", "AUTHOR_COUNT = 1 (Никитин Д.К.)",
     "Единоличное авторство концепции", "Коллективное авторство", "AUTHORSHIP_POLICY",
     "ACCEPTED", "Среднее", "DECISIONS.md"],
    ["D-024", "2026-09-26", "nRF5340 Audio DK ×2 — research stand",
     "Полный контроль LC3/QoS", "FMA120 + AuraClip", "PURCHASE_DECISION", "ACCEPTED",
     "Среднее", "DECISIONS.md"],
    ["D-019", "2026-09-26", "Никаких фиктивных функций Auracast/AI",
     "Честность демонстрации", "Показать неработающие кнопки", "APP_MVP_SPEC",
     "ACCEPTED", "Среднее", "DECISIONS.md"],
]

REF_HEADERS = ["List", "Values"]
YN = "YES,NO,PARTIAL,UNKNOWN,PROPOSED"
STATUSES = "DONE,CURRENT,NEXT,FUTURE"
LEVELS = "LOW,MEDIUM,HIGH"
EXPSTAT = "NOT MEASURED,PLANNED,READY,READY-ON-HW,COMPLETED"
CUR = "USD,RUB,EUR"
PRICESTAT = "SOURCE PRICE,ESTIMATE,NEEDS QUOTE,NOT PURCHASED"
ROLE = "IMPLEMENTED_MVP,PROPOSED,RESEARCH,UNKNOWN"
COND = "A quiet / near,B far row,C background noise,D reverberation,E noise + distance"
CHANNEL = "CLEAN_FEED,PHONE_MIC"
MODELS = "T-one,GigaAM-v3 RNNT,faster-whisper,Vosk"


def build() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    wb = Workbook()

    # ---------------- 00 Dashboard ----------------
    ws = wb.active
    ws.title = "00_Дашборд"
    ws.column_dimensions["A"].width = 3
    for col, w in [("B", 34), ("C", 26), ("D", 26), ("E", 26)]:
        ws.column_dimensions[col].width = w

    def dash_cell(cell, value, size=12, bold=False, color="16233A", fill=None):
        c = ws[cell]
        c.value = value
        c.font = Font(name="Calibri", size=size, bold=bold, color=color)
        c.alignment = Alignment(vertical="center", horizontal="left", wrap_text=True)
        if fill:
            c.fill = PatternFill("solid", fgColor=fill)
        return c

    ws.merge_cells("B2:E2")
    dash_cell("B2", "ТОЧКА ЗВУКА / ИНКЛЮЗИВНЫЙ МАРШРУТ+ — Инженерный пакет", 18, True, "FFFFFF", NAVY)
    ws.row_dimensions[2].height = 34
    dash_cell("B3", "Автор", 11, True)
    dash_cell("C3", "Никитин Даниил Константинович")
    ws.row_dimensions[3].height = 30
    dash_cell("B4", "AUTHOR_COUNT", 11, True)
    dash_cell("C4", 1)
    dash_cell("B5", "CURRENT GATE", 11, True)
    dash_cell("C5", "6B-3")

    dash_cell("B7", "СТАТУСЫ", 13, True, NAVY)
    statuses = [
        ("Software MVP", "IMPLEMENTED"),
        ("Real ASR", "PLANNED"),
        ("Auracast hardware", "NOT PURCHASED"),
        ("Bridge-T hardware", "PLANNED / research"),
        ("Experimental measurements", "NOT MEASURED"),
        ("Article", "FINAL"),
        ("Presentation", "FINAL / current version"),
    ]
    r = 8
    for k, v in statuses:
        dash_cell(f"B{r}", k, 11, True)
        dash_cell(f"C{r}", v)
        r += 1

    dash_cell(f"B{r+1}", "NEXT", 11, True)
    dash_cell(f"C{r+1}", "hardware + Local ASR + experiments")
    dash_cell(f"B{r+2}", "PIPELINE", 11, True)
    dash_cell(f"C{r+2}", "Software MVP → Hardware stand → Experiments → Pilot")

    # KPI computed from workbook
    k0 = r + 4
    dash_cell(f"B{k0}", "KPI (вычисляется автоматически)", 13, True, NAVY)
    kpis = [
        ("Аналоги (кол-во)", "=COUNTA('01_Аналоги'!A2:A1000)"),
        ("Эксперименты (кол-во)", "=COUNTA('04_Эксперименты'!A2:A1000)"),
        ("BOM items (кол-во)", "=COUNTA('02_BOM'!A2:A1000)"),
        ("HIGH risks (кол-во)", "=COUNTIF('06_Риски'!F2:F500,\"HIGH\")"),
        ("Actual measurements (кол-во)",
         "=COUNTIF('04_Эксперименты'!S2:S500,\"COMPLETED\")"),
    ]
    rr = k0 + 1
    for k, f in kpis:
        dash_cell(f"B{rr}", k, 11, True)
        c = ws[f"C{rr}"]
        c.value = f
        c.font = Font(name="Calibri", size=14, bold=True, color=BLUE)
        c.alignment = Alignment(horizontal="left", vertical="center")
        rr += 1

    # ---------------- 01 Analogs ----------------
    ws = wb.create_sheet("01_Аналоги")
    write_table(ws, ANALOG_HEADERS, ANALOG_ROWS, widths=[6, 26, 20, 12, 20, 20, 16,
                18, 7, 9, 9, 10, 12, 10, 8, 9, 11, 11, 11, 11, 10, 12, 11, 9, 10, 10,
                11, 12, 11, 11, 12, 34, 34, 14, 20, 26], freeze="C2")
    status_cf(ws, "G2:AE1000")
    # single dropdown for feature/value columns
    add_dv(ws, f'"{YN},IMPLEMENTED_MVP,RESEARCH"', "G2:AE1000")

    # ---------------- 02 BOM ----------------
    ws = wb.create_sheet("02_BOM")
    last = write_table(ws, BOM_HEADERS, BOM_ROWS, widths=[10, 16, 26, 18, 22, 22, 12,
                      8, 7, 11, 8, 12, 13, 11, 34, 12, 9, 13, 34], freeze="C2")
    # Estimated Total formulas: qty * price (blank-safe)
    for i in range(2, last + 1):
        ws.cell(row=i, column=12).value = f'=IF(N(J{i})=0,"",H{i}*J{i})'
        ws.cell(row=i, column=12).number_format = "#,##0.00"
    add_dv(ws, f'"{CUR}"', f"K2:K{last}")
    add_dv(ws, f'"{PRICESTAT}"', f"M2:M{last}")
    add_dv(ws, '"NOT PURCHASED,PURCHASED"', f"P2:P{last}")
    add_dv(ws, '"YES,NO,UNKNOWN,EXISTING"', f"Q2:Q{last}")
    status_cf(ws, f"M2:M{last}")

    # totals block by currency
    t = last + 2
    ws.cell(row=t, column=3, value="TOTAL by currency").font = Font(bold=True, color=NAVY)
    for k, cur in enumerate(["USD", "RUB", "EUR"]):
        rr = t + 1 + k
        ws.cell(row=rr, column=3, value=f"Total {cur}")
        ws.cell(row=rr, column=11, value=cur)
        ws.cell(row=rr, column=12,
                value=f'=SUMIF($K$2:$K${last},"{cur}",$L$2:$L${last})').number_format = "#,##0.00"
    ws.cell(row=t + 4, column=3,
            value="Примечание: валюты не суммируются между собой; конвертация не выполняется.")
    ws.cell(row=t + 4, column=3).font = Font(italic=True, size=9, color="5B6B83")

    # ---------------- 03 Purchase ----------------
    ws = wb.create_sheet("03_Закупка")
    last = write_table(ws, PURCHASE_HEADERS, PURCHASE_ROWS,
                       widths=[26, 30, 6, 8, 11, 11, 11, 30, 12, 12, 34, 13], freeze="C2")
    for i in range(2, last + 1):
        ws.cell(row=i, column=6).value = f'=IF(OR(N(D{i})=0,N(E{i})=0),"",C{i}*E{i})'
        ws.cell(row=i, column=6).number_format = "#,##0.00"
    add_dv(ws, f'"{CUR}"', f"D2:D{last}")
    add_dv(ws, '"YES,NO"', f"G2:G{last}")
    add_dv(ws, '"P0,P1,P2,P3"', f"J2:J{last}")
    add_dv(ws, '"NOT PURCHASED,NEEDS QUOTE,SOURCE PRICE,EXISTING,ESTIMATE"', f"L2:L{last}")
    status_cf(ws, f"L2:L{last}")
    t = last + 2
    ws.cell(row=t, column=2, value="Totals per scenario and currency (formulas)").font = Font(bold=True, color=NAVY)
    rr = t + 1
    for scen in ["SCENARIO A — Research", "SCENARIO B — Low-cost demo",
                 "SCENARIO C — Minimum E05 (software)"]:
        for cur in ["USD", "EUR", "RUB"]:
            ws.cell(row=rr, column=2, value=scen)
            ws.cell(row=rr, column=4, value=cur)
            ws.cell(row=rr, column=6,
                    value=f'=SUMIFS($F$2:$F${last},$A$2:$A${last},$B{rr},$D$2:$D${last},"{cur}")'
                    ).number_format = "#,##0.00"
            rr += 1
    ws.cell(row=rr + 1, column=2,
            value="Цены с Price Status = NEEDS QUOTE не входят в суммы (Unit Price пуст).").font = Font(italic=True, size=9, color="5B6B83")

    # ---------------- 04 Experiments ----------------
    ws = wb.create_sheet("04_Эксперименты")
    last = write_table(ws, EXP_HEADERS, EXP_ROWS,
                       widths=[10, 24, 30, 12, 26, 24, 22, 20, 20, 24, 22, 18, 14, 28,
                               14, 24, 11, 11, 13, 10, 30], freeze="C2")
    add_dv(ws, f'"{EXPSTAT}"', f"D2:D{last}")
    add_dv(ws, f'"{EXPSTAT}"', f"S2:S{last}")
    status_cf(ws, f"D2:D{last}")
    status_cf(ws, f"S2:S{last}")

    # ---------------- 05 E05 ASR ----------------
    ws = wb.create_sheet("05_E05_ASR")
    last = write_table(ws, E05_HEADERS, E05_ROWS,
                       widths=[9, 14, 18, 8, 16, 14, 13, 16, 30, 30, 11, 9, 9, 9, 9, 11,
                               10, 9, 12, 13, 10, 24], freeze="C2")
    add_dv(ws, f'"{COND}"', f"C2:C{last}")
    add_dv(ws, f'"{CHANNEL}"', f"G2:G{last}")
    add_dv(ws, f'"{MODELS}"', f"H2:H{last}")
    for i in range(2, last + 1):
        ws.cell(row=i, column=15).number_format = "0.0%"
        ws.cell(row=i, column=18).number_format = "0.0%"

    # legend block
    lg = last + 2
    ws.cell(row=lg, column=1, value="E05 — условия и справочные данные").font = Font(bold=True, color=NAVY, size=12)
    legend = [
        ("Условия", "A quiet/near; B far row; C background noise; D reverberation; E noise+distance"),
        ("Каналы", "CLEAN_FEED; PHONE_MIC"),
        ("ASR модели", "T-one (RECOMMENDED, не установлена); GigaAM-v3 RNNT (batch reference); faster-whisper; Vosk"),
        ("WER формула", "(S + D + I) / N; пусто при N = 0"),
        ("CER формула", "Character Errors / Reference Characters; пусто при 0"),
        ("Статус", "Все измерения = NOT MEASURED; заполняется после эксперимента"),
    ]
    rr = lg + 1
    for k, v in legend:
        ws.cell(row=rr, column=1, value=k).font = BOLD
        ws.cell(row=rr, column=3, value=v).font = T_FONT
        rr += 1

    # ---------------- 06 Risks ----------------
    ws = wb.create_sheet("06_Риски")
    last = write_table(ws, RISK_HEADERS, RISK_ROWS,
                       widths=[9, 14, 44, 44, 12, 9, 10, 40, 30, 22, 10, 18], freeze="C2")
    add_dv(ws, f'"{LEVELS}"', f"E2:E{last}")
    add_dv(ws, f'"{LEVELS}"', f"F2:F{last}")
    add_dv(ws, '"OPEN,MITIGATED,CLOSED"', f"K2:K{last}")
    # Priority formula from probability/impact
    for i in range(2, last + 1):
        ws.cell(row=i, column=7,
                value=(f'=IF(OR(E{i}="HIGH",F{i}="HIGH"),"CRITICAL",'
                       f'IF(OR(E{i}="MEDIUM",F{i}="MEDIUM"),"MEDIUM","LOW"))'))
    status_cf(ws, f"E2:F{last}")

    # ---------------- 07 Roadmap ----------------
    ws = wb.create_sheet("07_Roadmap")
    last = write_table(ws, ROADMAP_HEADERS, ROADMAP_ROWS,
                       widths=[10, 34, 10, 26, 34, 10, 10, 30, 30], freeze="C2")
    add_dv(ws, f'"{STATUSES}"', f"C2:C{last}")
    status_cf(ws, f"A2:A{last}")
    status_cf(ws, f"C2:C{last}")

    # ---------------- 08 Sources ----------------
    ws = wb.create_sheet("08_Источники")
    last = write_table(ws, SOURCE_HEADERS, SOURCE_ROWS,
                       widths=[14, 46, 24, 8, 26, 9, 13, 11, 40, 12, 42, 30, 10, 26],
                       freeze="C2")
    add_dv(ws, '"YES,NO,PARTIAL"', f"F2:H{last}")
    add_dv(ws, '"YES,NO,LEGACY"', f"M2:M{last}")
    # hyperlinks for URL cells
    for i in range(2, last + 1):
        cell = ws.cell(row=i, column=9)
        url = str(cell.value or "")
        if url.startswith("http"):
            cell.hyperlink = url
            cell.font = LINK_FONT
            cell.value = url

    # ---------------- 09 Decisions ----------------
    ws = wb.create_sheet("09_Решения")
    last = write_table(ws, DECISION_HEADERS, DECISION_ROWS,
                       widths=[11, 12, 40, 34, 24, 30, 12, 10, 16], freeze="C2")
    add_dv(ws, '"ACCEPTED,SUPERSEDED,REJECTED"', f"G2:G{last}")

    # ---------------- 10 Reference lists ----------------
    ws = wb.create_sheet("10_Справочники")
    refs = [("YN", YN), ("Statuses", STATUSES), ("Levels", LEVELS),
            ("Experiment status", EXPSTAT), ("Currencies", CUR),
            ("Price status", PRICESTAT), ("Role", ROLE), ("Conditions", COND),
            ("Channels", CHANNEL), ("ASR models", MODELS)]
    write_table(ws, REF_HEADERS, [[k, v] for k, v in refs],
                widths=[20, 90], freeze=None)

    # print setup for preview
    for sheet in wb.worksheets:
        sheet.page_setup.orientation = "landscape"
        sheet.page_setup.fitToWidth = 1
        sheet.page_setup.fitToHeight = 0
        sheet.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    # dashboard should print on a single page
    dash = wb["00_Дашборд"]
    dash.page_setup.fitToWidth = 1
    dash.page_setup.fitToHeight = 1
    dash.print_area = "B1:E30"

    wb.save(OUT)
    print("saved:", OUT)
    print("sheets:", wb.sheetnames)


if __name__ == "__main__":
    build()
