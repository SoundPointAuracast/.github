# WORKBOOK_QA

GATE 6B-3. Дата: 2026-09-26.
Файл: `12_reports/excel/final/Точка_звука_Инженерный_пакет_FINAL.xlsx`
Генератор: `build_workbook.py`. Превью: `final/Точка_звука_Инженерный_пакет_PREVIEW.pdf`.

## Сводка по листам

| Sheet | Rows | Cols | Formulas | Validations | AutoFilter | Freeze | Проверено |
|---|---|---|---|---|---|---|---|
| 00_Дашборд | 24 | 5 | 5 | 0 | — (dashboard) | — | визуально: OK |
| 01_Аналоги | 11 | 36 | 0 | 1 | A1:AJ11 | C2 | визуально: OK |
| 02_BOM | 26 | 19 | 22 | 4 | A1:S20 | C2 | визуально: OK |
| 03_Закупка | 24 | 12 | 29 | 4 | A1:L11 | C2 | визуально: OK |
| 04_Эксперименты | 6 | 21 | 0 | 2 | A1:U6 | C2 | визуально: OK |
| 05_E05_ASR | 19 | 22 | 20 | 3 | A1:V11 | C2 | визуально: OK |
| 06_Риски | 13 | 12 | 12 | 3 | A1:L13 | C2 | визуально: OK |
| 07_Roadmap | 17 | 9 | 0 | 1 | A1:I17 | C2 | визуально: OK |
| 08_Источники | 17 | 14 | 0 | 2 | A1:N17 | C2 | визуально: OK |
| 09_Решения | 11 | 9 | 0 | 1 | A1:I11 | C2 | визуально: OK |
| 10_Справочники | 11 | 2 | 0 | 0 | A1:B11 | — | визуально: OK |

- **Всего формул: 88.** `#REF!` не найдено.
- **Data Validation: 25 правил** (dropdown: YES/NO/PARTIAL/UNKNOWN/PROPOSED;
  IMPLEMENTED_MVP/PROPOSED/RESEARCH; DONE/CURRENT/NEXT/FUTURE; LOW/MEDIUM/HIGH;
  NOT MEASURED/PLANNED/READY/READY-ON-HW/COMPLETED; USD/RUB/EUR;
  SOURCE PRICE/ESTIMATE/NEEDS QUOTE/NOT PURCHASED; условия A–E; каналы;
  ASR-модели; OPEN/MITIGATED/CLOSED; ACCEPTED/SUPERSEDED/REJECTED).
- **AutoFilter** включён на всех рабочих таблицах.
- **Freeze panes** C2 на всех рабочих таблицах.
- **Hyperlinks: 13** (лист 08_Источники и BOM/Purchase).
- **Placeholder TODO / lorem ipsum: нет.**

## Формулы

| Лист | Формулы |
|---|---|
| 00_Дашборд | KPI: `COUNTA` (аналоги/эксперименты/BOM), `COUNTIF` (HIGH risks, COMPLETED measurements) |
| 02_BOM | `Estimated Total = Qty × Unit Price` (blank-safe); `SUMIF` по валюте (USD/RUB/EUR) |
| 03_Закупка | `Cost = Qty × Unit Price` (ссылки на 02_BOM); `SUMIFS` по сценарию и валюте |
| 05_E05_ASR | `WER = (S+D+I)/N` и `CER = err/ref` через `IFERROR` (нет #DIV/0!) |
| 06_Риски | `Priority = f(Probability, Impact)` |

## Визуальный QA (LibreOffice → PDF, 11 страниц)

Проверены: 00_Дашборд, 01_Аналоги, 02_BOM, 03_Закупка, 04_Эксперименты,
05_E05_ASR, 06_Риски, 07_Roadmap, 08_Источники, 09_Решения, 10_Справочники.

**Найденные проблемы и исправления:**

| # | Проблема | Исправление |
|---|---|---|
| 1 | Ячейка автора на дашборде обрезалась (малая высота строки) | `row_dimensions[3].height = 30` |
| 2 | Дашборд при печати разбивался на 2 страницы | print_area `B1:E30`, `fitToHeight=1` |

Других проблем не найдено: обрезанного текста нет (ширины колонок заданы,
wrap text включён), «#####» отсутствует, сломанных формул нет, неуместных
merged cells нет (merged только заголовок дашборда), цветовое выделение
аккуратное.

## Отсутствие фиктивных данных

- Все эксперименты: `Result Status = NOT MEASURED`, `Result` пуст,
  `Actual Date` пуст.
- E01: TARGET ≤60 мс и ACCEPTANCE ≤100 мс отделены от результата.
- E04: actual values пусты; 24_2_1 помечен как baseline, не winner.
- E05: WER/CER — только формулы; исходные тексты/числа пусты.
- Риски: вероятности/влияние — только LOW/MEDIUM/HIGH (без процентов).
- BOM: при отсутствии цены `Unit Price` пуст, `Price Status = NEEDS QUOTE`.
- Roadmap: даты не выдуманы (пусто).

## Замечания

- 01_Аналоги очень широкий (36 колонок) — в PDF-превью уменьшен; в Excel
  читается при стандартных ширинах.
- Классификация источников исправлена: Bradley & Sato — PEER-REVIEWED
  (PRIMARY? = NO); SIG/производители/платформа/университет — PRIMARY для
  своих артефактов; исторические S001–S011 — SECONDARY/LEGACY.
