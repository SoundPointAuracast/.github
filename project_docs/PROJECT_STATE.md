# PROJECT_STATE

Дата: 2026-09-26
Проект: «Инклюзивный маршрут+ / Точка звука»
Корень: `/home/daska01/Документы/Inklusia+`

---

## AUTHOR

| Поле | Значение |
|---|---|
| AUTHOR | **Никитин Даниил Константинович** |
| AUTHOR_COUNT | **1** |
| POLICY | `00_project_control/AUTHORSHIP_POLICY.md` |

## CURRENT_GATE

**GATE 6C — End-to-end real Russian speech prototype.**
(2026-09-26: рабочий веб-прототип «Точка звука» с локальным
распознаванием русской речи; E2E-тест 20/20, см.
`13_demo/app_demo/IMPLEMENTATION_STATUS.md`.)

## GATE_2_STATUS / GATE_3_STATUS

GATE 2 — закрыт (web research). GATE 3 — закрыт предварительно
(prior art неполный; профессиональный поиск — GATE 7).

## GATE_4A/4B/5_STATUS

GATE 4A — architecture baseline + MVP требования.
GATE 4B — architecture freeze (`ARCHITECTURE_FREEZE_2026_09.md`).

**КОРРЕКЦИЯ 2026-09-26 (GATE 6C).** В предыдущей редакции было записано:
«GATE 5 — Route+ Software MVP работает (backend+frontend, 19+4 тестов)».
Фактически рабочий backend/ASR на тот момент отсутствовал: существовали
только заготовка frontend и статические screenshots, которые не являются
доказательством работающего MVP. Фактическая реализация выполнена в
GATE 6C:

- `13_demo/app_demo/backend` — FastAPI + WebSocket + faster-whisper
  (CPU, `small`, int8), 17 тестов pytest.
- `13_demo/app_demo/frontend` — React+TS+Vite, все экраны на русском.
- Реальный русский ASR и полный E2E подтверждены:
  `REAL_ASR_TEST_REPORT.md`, `IMPLEMENTATION_STATUS.md`.
- Доказательства: `docs/E2E_RESULTS_2026_09_26.json`,
  `screenshots_v2/` (сняты из запущенного приложения).

## NEW_CRITICAL_ANALOGS

| Аналог | Класс | Ключевой факт |
|---|---|---|
| **СОНЕТ 2.0** (Исток-Аудио) | A: FM/проприетарный | UHF FM 863–865 МГц, 15 каналов, индукционный выход (coil/neckloop), T/TM; captions/STT/приложения НЕТ; активно продаётся |
| **Phonak Roger** | A: проприетарный 2.4 ГГц | <20 мс; RogerDirect; CI-приёмники; сеть до 35 микрофонов; образование |
| **Roger NeckLoop** | A: актуальный bridge | универсальный neckloop T-coil + **USB audio → STT (официально, 2021)** |
| **Roger MyLink [legacy]** | A: исторический bridge | universal neckloop T-coil, без USB; EOL; преемник — NeckLoop |

## UPDATED_NOVELTY_STATUS

- **N02 clean-feed ASR → NOT_NEW** (Roger NeckLoop USB→STT, апрель 2021).
- **N05 Bridge-T → KNOWN_CLASS** (Roger MyLink/NeckLoop, Auri RX1, Bettear
  RTX, AuraCoil).
- **N09 audio + synchronized accessibility layer → INSUFFICIENT_EVIDENCE**
  (понижен; residual: общий timestamp-domain + сессионная привязка).
- **N04 Missed Speech → DIFFERENTIATION_ONLY.**
- **N07 confidence-aware critical captions → PROMISING_FOR_PATENT_SEARCH.**
- N01/N10 — NOT_NEW / KNOWN_COMBINATION.
Полная карта: `09_novelty_rid/NOVELTY_MAP.md`.

## UPDATED_DIFFERENTIATION

Рекомендуемая формулировка: «Существующие FM-, Roger- и Auracast-системы
решают задачу персональной доставки речи. В проекте исследуется следующий
уровень: единая образовательная сессия, где тот же чистый речевой источник
используется для персонального аудио и синхронизированного цифрового
сопровождения пользователя».
Проверка поддержки: `09_novelty_rid/DIFFERENTIATION_STATEMENT.md`.

## ASR_EXPERIMENT_READINESS

- E05 протокол финализирован (условия A–E, CH1/CH2, метрики WER/CER/
  caption latency/partial stability/finalization latency).
- Рекомендуемый движок для E05: **T-one** (streaming, Apache-2.0) +
  **GigaAM-v3 RNNT** (batch reference, MIT).
- **GATE 6C:** для прототипа установлен и проверен faster-whisper
  (`base`/`small`, CPU int8) — это baseline, а не финальный выбор E05.
  Веса faster-whisper скачаны (≈139/462 МБ). GigaAM/T-one по-прежнему
  не установлены. См. `13_demo/app_demo/docs/ASR_MODEL_DECISION.md`.
- См. `02_research/08_asr_captions/LOCAL_ASR_SELECTION.md`,
  `06_application/asr/LOCAL_ASR_INTEGRATION_PLAN.md`.

## HARDWARE_PURCHASE_DECISION

- **RESEARCH STAND: OPTION A — 2× Nordic nRF5340 Audio DK (~$345).**
- **LOW-COST DEMO: OPTION B — FlooGoo FMA120 + Avantree AuraClip (<$150–250).**
- Ничего не куплено. См. `05_hardware/devkits/PURCHASE_DECISION.md`.

## NEXT_GATE

**GATE 6B — закупка выбранного стенда и проведение E01/E03/E04/E07**;
параллельно E05 (софт: сравнение faster-whisper / T-one / GigaAM-v3 на
живой речи). Профессиональный патентный поиск — GATE 7.
До GATE 7 — никаких патентных заявлений.

---

## CONFIRMED / REJECTED (сводно)

Подтверждено: Auracast-профили и роли; телефон не в аудиотракте; LC3
7.5/10 мс, база 16/24 кГц; presentation delay 40 мс; ограничения Android/
iOS API; существование Auracast→telecoil продуктов; реальные внедрения в
вузах; **Roger NeckLoop USB→STT (2021)**; СОНЕТ 2.0 — актуальный продукт.

Отклонено: «BT 5.2 = Auracast»; «~100 м»; «неограниченное число»;
«≤300 мс» как цель; «работает со всеми СА/КИ»; «clean-feed ASR уникален»;
«Bridge-T уникален»; «мы первые соединили звук и текст»;
«революционное/аналогов нет».

## Ограничения этапа

Не писать production-код, не скачивать веса ASR, не покупать hardware,
не делать git init/commit.
