# ROADMAP

## Принцип

Двигаться гейтами (GATE). Не переходить к следующему гейту без
закрытия текущего и явного решения.

## GATE 0 — Инициализация проекта (ЗАКРЫТ)

- [x] Обследовать корень проекта
- [x] Создать структуру каталогов
- [x] Зафиксировать Source of Truth и AI Workflow
- [x] Создать реестр источников

## GATE 1 — Аудит исходных материалов (ЗАКРЫТ 2026-09-26)

- [x] Найти локальные исходники (в `/home/daska01/Загрузки/`)
- [x] Скопировать исходники в `01_sources/` (оригиналы не изменялись)
- [x] Прочитать содержимое, а не полагаться на имена файлов
- [x] Заполнить `SOURCE_INVENTORY.md` (S001–S011)
- [x] Проставить статусы в `source_register.csv`
- [x] Восстановить эволюцию (`12_reports/PROJECT_EVOLUTION.md`)
- [x] Аудиты: Auracast, latency, индуктор, приложение, экономика, новизна
- [x] Реестр противоречий (`CONTRADICTION_REGISTER.md`, 18 записей)
- [x] Обновить `CONCEPT_AUDIT.md` и `PROJECT_STATE.md`

## GATE 2 — Исследование (ЗАКРЫТ 2026-09-26)

- [x] Auracast / LE Audio (PBP/BAP/BASS/BIG/BIS) — `AURACAST_TECHNICAL_MAP.md`
- [x] LC3 и задержки — `LC3_CONFIGURATION_MATRIX.md`, `LATENCY_DEEP_DIVE.md`
- [x] Поддержка Android/iOS — `MOBILE_AURACAST_SUPPORT.md`
- [x] Поддержка слуховых аппаратов и КИ — `DEVICE_COMPATIBILITY_MATRIX.md`
- [x] Реальные внедрения — `REAL_WORLD_DEPLOYMENTS.md`
- [x] Telecoil/индукция — `AURACAST_TELECOIL_PRIOR_ART.md`
- [x] ASR и captions — `CLEAN_FEED_ASR_RESEARCH.md`, `ASSISTIVE_APP_LANDSCAPE.md`
- [x] Devkits — `DEVKIT_COMPARISON.md`

## GATE 3 — Конкуренты + prior art (ЗАКРЫТ ПРЕДВАРИТЕЛЬНО 2026-09-26)

- [x] Конкурентная матрица — `08_competitor_analysis/COMPETITOR_MATRIX.md`
- [x] Prior art (предварительно) — `09_novelty_rid/PRIOR_ART.md` (45+ документов)
- [x] Missed speech prior art — `MISSED_SPEECH_PRIOR_ART.md`
- [x] Novelty map — `NOVELTY_MAP.md`
- [x] Differentiation statement — `DIFFERENTIATION_STATEMENT.md`
- [ ] Профессиональный патентный поиск (GATE 7)

## GATE 4A — Architecture Baseline + MVP (ЗАКРЫТ DRAFT 2026-09-26)

- [x] Обновлена архитектура по слоям — `SYSTEM_ARCHITECTURE.md`
- [x] Software MVP — `13_demo/app_demo/APP_MVP_SPEC.md`
- [x] Hardware MVP — `AUDIO_MVP_SPEC.md`, `BRIDGE_T_MVP_SPEC.md`
- [x] План экспериментов E01–E10 — `EXPERIMENT_MASTER_PLAN.md`
- [x] План презентации — `PRESENTATION_REBUILD_PLAN.md`
- [x] Master report (draft) — `12_reports/MASTER_REPORT.md`
- [x] Red team review — `12_reports/GATE_2_3_RED_TEAM_REVIEW.md`

## GATE 4B — Architecture Freeze (ЗАКРЫТ 2026-09-26)

- [x] Зафиксировать архитектурный baseline — `ARCHITECTURE_FREEZE_2026_09.md`
- [x] Зафиксировать LC3 baseline и latency target
- [x] Privacy requirements — `03_requirements/PRIVACY_REQUIREMENTS.md`

## GATE 5 — Route+ App Software MVP (ЗАКРЫТ 2026-09-26)

- [x] Backend (FastAPI + WebSocket, demo, missed speech, tests)
- [x] Frontend (React + TS + Vite, 6 маршрутов, a11y, demo mode)
- [x] shared-контракт `caption_event.schema.json`
- [x] Тесты: backend 19, frontend 4 — проходят
- [x] Скриншоты `13_demo/app_demo/screenshots/`
- [x] README и DEMO_SCRIPT
- [ ] Реальный ASR (следующий этап)

## GATE 5.5 — Authorship Policy (ЗАКРЫТ 2026-09-26)

- [x] Аудит авторских формулировок в рабочих документах
- [x] `AUTHORSHIP_POLICY.md` (AUTHOR_COUNT = 1)
- [x] Исправления внесены; исторические материалы не изменялись

## GATE 6A — Analog Red Team + Readiness (ЗАКРЫТ 2026-09-26)

- [x] СОНЕТ 2.0 deep dive — `competitor_cards/SONET_2_0.md`
- [x] Phonak Roger deep dive + ROGER_STT_PRIOR_ART — `competitor_cards/PHONAK_ROGER.md`
- [x] Классы конкурентов A–E + матрица 30 признаков
- [x] Пересмотр N02/N05/N09 — `NOVELTY_MAP.md`
- [x] `ASSISTIVE_AUDIO_EVOLUTION.md` + слайд
- [x] `ANALOG_RED_TEAM.md` (14 возражений)
- [x] E05 финализирован; `LOCAL_ASR_SELECTION.md`; integration plan
- [x] `PURCHASE_DECISION.md`; `EXPERIMENT_READINESS_GATE6.md`
- [x] Схема `architecture_gate6.*` (редактируемая)

## GATE 6B — Hardware MVP + эксперименты

- [ ] latency
- [ ] audio_quality
- [ ] rf_coverage
- [ ] compatibility
- [ ] asr_accuracy
- [ ] induction
- [ ] user_testing

## GATE 5b — Экономика

- [ ] BOM_COST
- [ ] MVP_COST
- [ ] PILOT_COST

## GATE 6b — Демонстрация и пилот

- [ ] DEMO_PLAN
- [ ] пилот в образовательной среде

## GATE 7 — Новизна и защита

- [ ] NOVELTY_MAP
- [ ] PRIOR_ART
- [ ] CLAIM_CANDIDATES
- [ ] решение о патентной стратегии
