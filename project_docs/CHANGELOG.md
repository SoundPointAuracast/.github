# CHANGELOG

Формат: дата — этап — изменения.

## 2026-09-26 — GATE 0 (инициализация)

- Обследован корень проекта `/home/daska01/Документы/Inklusia+` — каталог был пуст.
- Создана целевая структура каталогов (00…99).
- Созданы корневые документы: `README.md`, `SOURCE_OF_TRUTH.md`,
  `AI_WORKFLOW.md`, `CHANGELOG.md`.
- Создан реестр источников `01_sources/source_register.csv`
  (пустой, т.к. исходников не найдено).
- Создан `01_sources/SOURCE_INVENTORY.md` с фиксацией отсутствия материалов.
- Созданы требования в `03_requirements/`.
- Создан аудит концепции `12_reports/CONCEPT_AUDIT.md`.
- Созданы документы `09_novelty_rid/`.
- Создан `PROJECT_STATE.md`.
- Вложенный корень проекта НЕ создавался. `git init` НЕ выполнялся
  (репозиторий отсутствовал).

## 2026-09-26 — GATE 1 (source ingestion + legacy audit)

- Локальный поиск: исходники обнаружены в `/home/daska01/Загрузки/`
  (в проекте их не было).
- Скопированы (не перемещены) 11 исходников S001–S011 в `01_sources/`;
  оригиналы не изменялись. Текстовые извлечения — в `01_sources/extracted_text/`.
- Заполнен `01_sources/source_register.csv` (11 записей).
- Полностью переписан `01_sources/SOURCE_INVENTORY.md`.
- Создан `12_reports/PROJECT_EVOLUTION.md` (эволюция, CORE/SECONDARY problems).
- Создан `02_research/01_auracast_standard/LEGACY_AURACAST_CLAIMS.md` (32 claim).
- Создан `02_research/02_lc3_latency/LEGACY_LATENCY_CLAIMS.md` (8 claim).
- Создан `05_hardware/existing_inductor/LEGACY_INDUCTOR_ANALYSIS.md`.
- Создан `06_application/APP_EVOLUTION.md`.
- Создан `04_architecture/BRIDGE_T_EVOLUTION.md`; обновлён `SYSTEM_ARCHITECTURE.md`.
- Создан `12_reports/CONTRADICTION_REGISTER.md` (18 записей).
- Создан `10_economics/LEGACY_ECONOMICS.md`.
- Создан `09_novelty_rid/LEGACY_NOVELTY_CLAIMS.md`.
- Обновлён `12_reports/CONCEPT_AUDIT.md` (20 разделов) и `PROJECT_STATE.md`.
- Обновлены `00_project_control/ROADMAP.md`, `DECISIONS.md` (D-007…D-011).
- Скопирована схема в `04_architecture/diagrams/`.
- Web-поиск, проверка Bluetooth SIG, патентный поиск — НЕ проводились.
- `git init` / `git commit` — НЕ выполнялись.

## 2026-09-26 — GATE 2 + GATE 3 + GATE 4A (global research, MAX)

- Проведено web-исследование (9 параллельных исследовательских потоков).
  Все источники с URL и датой доступа 2026-09-26.
- GATE 2 создано:
  - `02_research/01_auracast_standard/AURACAST_TECHNICAL_MAP.md`
  - `02_research/01_auracast_standard/PROFILE_REQUIREMENTS.md`
  - `02_research/02_lc3_latency/LC3_CONFIGURATION_MATRIX.md`
  - `02_research/02_lc3_latency/LATENCY_DEEP_DIVE.md`
  - `07_experiments/latency/LATENCY_TEST_PROTOCOL.md`
  - `02_research/03_education_deployments/REAL_WORLD_DEPLOYMENTS.md`
  - `02_research/05_hearing_devices/DEVICE_COMPATIBILITY_MATRIX.md`
  - `02_research/06_mobile_os_support/MOBILE_AURACAST_SUPPORT.md`
  - `02_research/07_induction_telecoil/AURACAST_TELECOIL_PRIOR_ART.md`
  - `02_research/08_asr_captions/CLEAN_FEED_ASR_RESEARCH.md`
  - `02_research/08_asr_captions/ASSISTIVE_APP_LANDSCAPE.md`
  - `07_experiments/asr_accuracy/ASR_COMPARISON_PROTOCOL.md`
  - `06_application/missed_speech/MISSED_SPEECH_CONCEPT.md`
- GATE 3 создано/обновлено:
  - `08_competitor_analysis/COMPETITOR_MATRIX.md` (обновлён)
  - `09_novelty_rid/PRIOR_ART.md` (45+ документов, PA-BRIDGET/AUDIO-TEXT)
  - `09_novelty_rid/MISSED_SPEECH_PRIOR_ART.md`
  - `09_novelty_rid/NOVELTY_MAP.md` (N01–N10)
  - `09_novelty_rid/DIFFERENTIATION_STATEMENT.md` (3 версии)
- GATE 4A создано/обновлено:
  - `04_architecture/SYSTEM_ARCHITECTURE.md` (7 слоёв, MVP/PHASE_2/RESEARCH)
  - `04_architecture/APP_ARCHITECTURE.md`, `DATA_PIPELINE.md`,
    `BRIDGE_T_EVOLUTION.md`
  - `13_demo/app_demo/APP_MVP_SPEC.md`
  - `05_hardware/devkits/DEVKIT_COMPARISON.md`
  - `13_demo/hardware_demo/AUDIO_MVP_SPEC.md`, `BRIDGE_T_MVP_SPEC.md`
  - `07_experiments/EXPERIMENT_MASTER_PLAN.md` (E01–E10)
  - `11_presentations/inclusion/PRESENTATION_REBUILD_PLAN.md`
  - `12_reports/MASTER_REPORT.md` (draft, 31 раздел)
  - `12_reports/GATE_2_3_RED_TEAM_REVIEW.md`
- Обновлён `PROJECT_STATE.md` (CURRENT_GATE = 4A).
- Обновлены `ROADMAP.md`, `DECISIONS.md` (D-012…D-016).
- Отвергнуты легаси-утверждения; обновлена архитектура; приоритеты новизны
  понижены (см. RED TEAM).
- Web-исследование проводилось; патентный поиск — только предварительный.
- `git init` / `git commit` — НЕ выполнялись. Код — НЕ писался.

## 2026-09-26 — GATE 4B + GATE 5 (architecture freeze + software MVP)

- GATE 4B: зафиксирован `00_project_control/ARCHITECTURE_FREEZE_2026_09.md`
  (LC3 baseline 24_2_1; latency target ≤60/≤100 мс; границы App).
- Создан `03_requirements/PRIVACY_REQUIREMENTS.md`.
- GATE 5: реализован работающий **Route+ Software MVP**:
  - backend `06_application/backend/` — FastAPI + WebSocket, `CaptionEvent`,
    ring buffer, missed-speech, demo runner, ASR-интерфейс
    (`MockASRProvider` + `LocalASRProvider` scaffold), notes/bookmarks;
  - frontend `06_application/frontend/` — React + TypeScript + Vite,
    маршруты `/`, `/session/:id`, `/history`, `/saved`,
    `/settings/accessibility`, `/about/audio`;
  - `06_application/shared/caption_event.schema.json` — общий контракт;
  - `06_application/README.md`, `13_demo/app_demo/DEMO_SCRIPT.md`.
- Тесты: backend 19 (pytest), frontend 4 (vitest). Сборка frontend проходит.
- Скриншоты: `13_demo/app_demo/screenshots/` (5 шт., headless Chrome).
- Проверено: demo mode, WebSocket, «Не расслышал», history, note, bookmark,
  accessibility, мобильная раскладка; ошибок консоли на всех маршрутах нет.
- Обновлён `PROJECT_STATE.md` (CURRENT_GATE = 5), `DECISIONS.md`
  (D-017…D-019), `ROADMAP.md`.
- Auracast/Bluetooth, firmware, PCB, AI — НЕ реализовывались.
- `git init` / `git commit` — НЕ выполнялись.

## 2026-09-26 — GATE 5.5 + GATE 6A (authorship + analog correction + readiness)

- **GATE 5.5 — Authorship audit.** Проведён аудит актуальных рабочих
  документов; исправлены формулировки, ошибочно создававшие впечатление
  коллективного авторства (SYSTEM_ARCHITECTURE, DIFFERENTIATION_STATEMENT,
  MASTER_REPORT, PRESENTATION_REBUILD_PLAN, GATE_2_3_RED_TEAM_REVIEW,
  ASSISTIVE_APP_LANDSCAPE, PROFILE_REQUIREMENTS, MOBILE_AURACAST_SUPPORT,
  DECISIONS, AURACAST_TELECOIL_PRIOR_ART, MISSED_SPEECH_PRIOR_ART,
  LATENCY_DEEP_DIVE, REAL_WORLD_DEPLOYMENTS, LEGACY_INDUCTOR_ANALYSIS,
  MISSED_SPEECH_CONCEPT, BRIDGE_T_MVP_SPEC). Исторические материалы в
  `01_sources/` не изменялись.
  Создан `00_project_control/AUTHORSHIP_POLICY.md` (AUTHOR_COUNT = 1).
- **GATE 6A — Analog correction.**
  - Web-исследование: **СОНЕТ 2.0** (Исток-Аудио) и **Phonak Roger**
    (включая Roger NeckLoop USB→STT и статус Roger MyLink).
  - Созданы карточки `competitor_cards/SONET_2_0.md`, `PHONAK_ROGER.md`
    (раздел ROGER_STT_PRIOR_ART — **CRITICAL PRIOR ART**, апрель 2021).
  - `COMPETITOR_MATRIX.md` перестроена по классам A–E, добавлены СОНЕТ,
    Roger, MyLink [legacy], транспонированная матрица (30 признаков).
  - `NOVELTY_MAP.md` пересмотрен: N02 → NOT_NEW; N05 → KNOWN_CLASS;
    N09 → INSUFFICIENT_EVIDENCE; N07 — главный кандидат для поиска.
  - `DIFFERENTIATION_STATEMENT.md` — новая основная формулировка.
  - Созданы `12_reports/ASSISTIVE_AUDIO_EVOLUTION.md`,
    `ANALOG_RED_TEAM.md` (14 возражений),
    `11_presentations/inclusion/SLIDE_ASSISTIVE_AUDIO_EVOLUTION.md`.
  - E05 протокол финализирован; созданы `LOCAL_ASR_SELECTION.md`
    (рекомендация: T-one + GigaAM-v3) и `LOCAL_ASR_INTEGRATION_PLAN.md`.
  - Созданы `05_hardware/devkits/PURCHASE_DECISION.md`
    (research: 2× nRF5340 Audio DK; demo: FMA120 + AuraClip) и
    `07_experiments/EXPERIMENT_READINESS_GATE6.md` (E01/E03/E04/E07).
  - Обновлены `SYSTEM_ARCHITECTURE.md` (v2) и созданы
    `04_architecture/diagrams/architecture_gate6.mmd` / `.drawio`.
  - `MASTER_REPORT.md` — глава 32 «Предшествующие технологии».
  - Обновлены `PROJECT_STATE.md`, `ROADMAP.md`, `DECISIONS.md`
    (D-020…D-024).
- Модели ASR НЕ скачивались; hardware НЕ покупался; production-код НЕ
  писался; `git init` / `git commit` — НЕ выполнялись.

## 2026-09-26 — GATE 6B-1 (final presentation rebuild)

- Найден исходник: `01_sources/applications/S006_fsi_start1_local_audio_repeater.pptx`
  (15 слайдов, 68,6 МБ). Backup: `11_presentations/archive/…_BACKUP_2026-09-26.pptx`.
  Исходник не изменялся.
- Создан `11_presentations/final/PRESENTATION_AUDIT.md` (аудит 15 слайдов:
  KEEP/UPDATE/REBUILD/DELETE + unsupported claims).
- Собран **реальный редактируемый PPTX**: 17 слайдов, авторские фигуры и
  текст (218 текстовых фигур, 159 autoshapes), 3 реальных скриншота Route+.
- Генератор: `11_presentations/final/build_presentation.py` (деку можно
  пересобрать).
- Visual QA: два прохода (PDF → PNG → контактные листы + zoom).
  Pass #1 нашёл 9 проблем (overlap бейджей, перенос текста, размеры);
  исправлено; Pass #2 — ACCEPTABLE.
- Файлы: `…_FINAL.pptx`, `…_FINAL.pdf`, `PRESENTATION_VISUAL_QA.md`.
- Заявления исправлены: BT 5.2 ≠ Auracast; нет «100 м»/«неограниченно»;
  ≤300 мс → TARGET ≤60/≤100 (to be verified); Bridge-T = известный класс;
  clean-feed STT назван известным (Roger, 2021); авторство — 1 автор.
- Оригинальный PPTX не редактировался; git init/commit не выполнялись.

## 2026-09-26 — GATE 6B-2 (final scientific article DOCX + PDF)

- Поиск требований: официальный шаблон статьи не найден (проект +
  локальные материалы); единственный релевантный материал — форма подачи
  доклада «Выступающий без публикации» (S010/S011). Применён FALLBACK.
- Создан `12_reports/article/ARTICLE_FORMAT_REQUIREMENTS.md`
  (FALLBACK LAYOUT, NOT DIRECTLY PRESCRIBED BY GOST; нормативная база:
  ГОСТ Р 7.0.7-2021, 7.0.5-2008, 7.0.100-2018, 7.0.99-2018, 7.0.108-2022).
- Создан `12_reports/article/ARTICLE_SOURCE_MAP.md` (прослеживаемость,
  7 источников, отказ от непроверяемых утверждений).
- Собрана статья: `final/Статья_Точка_звука_Никитин_ДК_FINAL.docx` +
  PDF + PLAIN.txt. Генератор: `build_article.py`.
- Объём: **2 страницы** (page 2 fill 90% ≈ 1,9 стр.), 834 слова,
  6141 знак без пробелов; 7 источников; 1 автор.
- Создан `12_reports/article/ARTICLE_QA.md` (чек-лист + измерения).
- Заявления смягчены: clean-feed и Bridge-T не заявлены новизной;
  Mock ASR указан явно; TARGET ≠ measured; эксперименты не выдуманы.
- Git init/commit не выполнялись.

## 2026-09-26 — GATE 6B-3 (engineering workbook XLSX)

- Создан генератор `12_reports/excel/build_workbook.py` (openpyxl).
- Собран `final/Точка_звука_Инженерный_пакет_FINAL.xlsx` — 11 листов:
  00_Дашборд, 01_Аналоги, 02_BOM, 03_Закупка, 04_Эксперименты, 05_E05_ASR,
  06_Риски, 07_Roadmap, 08_Источники, 09_Решения, 10_Справочники.
- 88 формул (KPI, Qty×Price, SUMIF/SUMIFS по валютам, WER/CER c IFERROR,
  Priority); 25 правил Data Validation; AutoFilter + freeze panes на всех
  рабочих таблицах; 13 hyperlinks; условное форматирование статусов.
- Превью: `final/Точка_звука_Инженерный_пакет_PREVIEW.pdf` (11 стр.).
- QA: `12_reports/excel/WORKBOOK_QA.md`. Найдено/исправлено 2 визуальных
  замечания (высота строки автора; печать дашборда на 1 стр.).
- Фиктивных измерений/цен нет: эксперименты NOT MEASURED; цены без
  подтверждения — NEEDS QUOTE; валюты не суммируются без курса.
- Автор: Никитин Даниил Константинович (AUTHOR_COUNT = 1).
- Source-файлы не изменялись; hardware не покупался; эксперименты не
  запускались; веса ASR не скачивались; git init/commit не выполнялись.

## 2026-09-26 — GATE 6C (end-to-end real Russian speech prototype)

- Создан рабочий веб-прототип «Точка звука»:
  `13_demo/app_demo/backend` (FastAPI + WebSocket + faster-whisper)
  и `13_demo/app_demo/frontend` (React + TS + Vite, полностью русский UI).
- Реальное локальное распознавание русской речи: faster-whisper `small`,
  CPU int8, 8 потоков. Smoke-тест: 3 фразы, WER 0, ≈1.3–1.5 с на фразу
  (base ≈0.48 с). См. `REAL_ASR_TEST_REPORT.md`,
  `docs/ASR_MODEL_DECISION.md`.
- Микрофон браузера: getUserMedia + AudioWorklet + потоковый ресемплинг
  в PCM16 16 кГц mono; передача по WebSocket.
- E2E-тест в Chrome (поддельный микрофон из WAV): 20/20 шагов,
  ошибок консоли нет; субтитры у слушателя, «Не расслышал», сохранение,
  заметки, закладки, доступность, LAN-адрес и QR проверены.
  Доказательства: `docs/E2E_RESULTS_2026_09_26.json`,
  `screenshots_v2/` (9 скриншотов из запущенного приложения).
- Тесты: pytest 17 passed; `npm run build` и `npm run lint` без ошибок.
- QR декодирован обратно в LAN URL (проверка zxing-cpp).
- Созданы документы Gate 6C: `IMPLEMENTATION_STATUS.md`,
  `REAL_ASR_TEST_REPORT.md`, `README.md`,
  `PRESENTATION_STATUS_CORRECTION.md`, `docs/*`.
- Обновлены `APP_MVP_SPEC.md`, `DEMO_SCRIPT.md`, `PROJECT_STATE.md`
  (исправлено не подтверждённое кодом утверждение о работавшем MVP).
- Демо-режим оставлен как явный fallback (`ASR_PROVIDER=demo`).
- Реальный телефон не тестировался (проверена LAN-доступность).
- Git init/commit не выполнялись; FINAL статья/презентация не изменялись;
  CUDA не устанавливалась; Auracast hardware не использовался.
