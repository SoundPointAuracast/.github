# MASTER_REPORT

GATE 2–4A. Дата: 2026-09-26. Сводный отчёт; подробности — по ссылкам.
Статус: содержательный черновик (не реклама).

---

## 1. Executive Summary
Проект «Инклюзивный маршрут+ / Точка звука» — ассистивная система
персональной передачи речи для образования. Концепция: один чистый источник
речи → (а) низколатентное аудио (Auracast; при необходимости Bridge-T →
T/MT) и (б) синхронизированный текстовый слой (clean-feed ASR → Route+
App). Исследование подтвердило жизнеспособность аудиотракта (реальные
внедрения Auracast в вузах), техническую реализуемость Bridge-T (но не
новизну класса) и оставило открытыми вопросы чистого фида, синхронизации и
патентоспособности.

## 2. Personal Motivation
Автор проекта — человек с нарушением слуха (S004). Мотивация — доступ к
информации, а не «гаджет».

## 3. Problem
Человек с нарушением слуха теряет часть речевой информации в аудитории
из-за акустики, расстояния, шума, реверберации.
`SOURCE` BB93: шум ≤35/40 дБ, но +15 дБ SNR недостаточно для младших
(Bradley & Sato 2008). См. `CLEAN_FEED_ASR_RESEARCH.md`.

## 4. Target Audience
PRIMARY: слабослышащие, СА, КИ. SECONDARY: широкая аудитория (дальние ряды,
иностранные студенты, шумные залы). См. `PROJECT_EVOLUTION.md`.

## 5. User Scenario
Варианты A (прямой Auracast), B (Bridge-T → T/MT), C (Route+ текст),
D (аудио+текст). См. `03_requirements/USER_REQUIREMENTS.md`.

## 6. Evolution
Индуктор → индукция для СА/КИ → «Инклюзивный маршрут» (вокзалы) →
локальный аудиоретранслятор (образование) → «Точка звука».
См. `12_reports/PROJECT_EVOLUTION.md`.

## 7. Existing Technologies
Auracast ALS (Auri, Bettear, Audeara), индукционные петли (IEC 60118-4),
FM/IR, live captions (Ava, Live Transcribe, HearAura).
См. `REAL_WORLD_DEPLOYMENTS.md`, `ASSISTIVE_APP_LANDSCAPE.md`.

## 8. Auracast
Возможность LE Audio, определяемая PBP; роли PBS/PBK/PBA; BASS обязателен
на приёмниках; телефон не в аудиотракте; без интернета.
См. `AURACAST_TECHNICAL_MAP.md`, `PROFILE_REQUIREMENTS.md`.

## 9. Bluetooth LE Audio
Core 5.2+ (ISO channels) — необходим, но недостаточен. Профили BAP/PBP/
BASS; LC3. См. `02_research/01_auracast_standard/`.

## 10. LC3
7.5/10 мс кадры; 8–48 кГц; base 16/24 кГц. Codec delay 11.5–12.5 мс.
См. `LC3_CONFIGURATION_MATRIX.md`.

## 11. Latency
Спецификационный минимум ~42–62 мс + обработка источника. SIG не публикует
e2e. При смешении с живым звуком 300 мс неприемлемы (эхо). Цель ≤60 мс,
допустимо ≤100 мс. См. `LATENCY_DEEP_DIVE.md`.

## 12. Hearing Devices
Прямой Auracast: ReSound Nexia/Vivia/Savi, Oticon Intent (FW 1.3.0)/Zeal,
Starkey Edge/Omega, Phonak EON (авг. 2026); из CI — только Baha 7.
Установленный парк — через Bridge-T (telecoil). См.
`DEVICE_COMPATIBILITY_MATRIX.md`.

## 13. Telecoil
IEC 60118-4 (100 мА/м, 100 Гц–5 кГц); ADA 706.3 (neckloop); полоса уже,
гул, моно. См. `AURACAST_TELECOIL_PRIOR_ART.md`.

## 14. Bridge-T
Класс продуктов существует (Auri RX1, AuraCoil, Bettear RTX); не уникален.
Старый индуктор — та же физика, другая геометрия. См. `BRIDGE_T_EVOLUTION.md`.

## 15. Route+ App
Текстовый слой; не реализует Auracast stack (ограничения OS).
См. `APP_ARCHITECTURE.md`, `APP_MVP_SPEC.md`.

## 16. Clean-feed ASR
**Использование чистого фида для STT не является новым**: Roger NeckLoop
официально отдаёт аудио Roger-микрофона по USB в сторонний STT с апреля
2021 (`competitor_cards/PHONAK_ROGER.md`). H1 (clean feed точнее телефона)
остаётся гипотезой и проверяется в E05. См. `CLEAN_FEED_ASR_RESEARCH.md`,
`07_experiments/asr_accuracy/ASR_COMPARISON_PROTOCOL.md`.

## 17. Missed Speech
Функция «N-секундный дословный replay» в продуктах не найдена; механика
известна (Bionica 2007). См. `MISSED_SPEECH_CONCEPT.md`,
`MISSED_SPEECH_PRIOR_ART.md`.

## 18. Accessibility Profile
Известная практика (платформы/приложения). Дифференциатор, не патент.
См. `NOVELTY_MAP.md`.

## 19. AI Perspectives
Optional слой: translation, summary, semantics, confidence-aware captions.
Не реализовано; N07 — самый интересный для поиска. См. `NOVELTY_MAP.md`.

## 20. Competitor Analysis
Auri, Bettear, HearAura, Ava, Live Transcribe. См. `COMPETITOR_MATRIX.md`.

## 21. Real Deployments
UQ (65 залов), Oxford, UAL, Academy of Hearing Acoustics, MOVIX, театры.
См. `REAL_WORLD_DEPLOYMENTS.md`.

## 22. Novelty
Не ново: Auracast, telecoil, ASR, **parallel split (Roger 2021)**,
Bridge-T как класс. N09 понижен до INSUFFICIENT_EVIDENCE. Потенциал для
поиска: N07 (confidence-aware) и узкая системная формулировка N09
(общий timestamp-domain + сессия). См. `NOVELTY_MAP.md`,
`DIFFERENTIATION_STATEMENT.md`, `PRIOR_ART.md`, `ANALOG_RED_TEAM.md`.

## 23. Architecture
Слои: SOURCE / AUDIO / ACCESSIBILITY DATA / USER DEVICE / BRIDGE-T /
APPLICATION / OPTIONAL AI. См. `SYSTEM_ARCHITECTURE.md`.

## 24. Software MVP
Route+ App: 10 MUST-функций, demo mode. См. `APP_MVP_SPEC.md`.

## 25. Hardware MVP
Стенд nRF5340 Audio DK ×2 (или FMA120 + AuraClip); Bridge-T через
neckloop. См. `AUDIO_MVP_SPEC.md`, `BRIDGE_T_MVP_SPEC.md`,
`DEVKIT_COMPARISON.md`.

## 26. Experiments
E01–E10. См. `EXPERIMENT_MASTER_PLAN.md`.

## 27. Risks
Технические/правовые/организационные. См. `09_novelty_rid/RISKS.md`;
обновление — ниже в RED TEAM.

## 28. Economics
Placeholder. Старые цифры не переносить (`10_economics/LEGACY_ECONOMICS.md`).
BOM — после выбора железа.

## 29. IP Strategy
Без заявлений о новизне. План: профессиональный патентный поиск, claim
charts, решение по GATE 7. См. `PRIOR_ART.md`, `DECISIONS.md` D-003.

## 30. Roadmap
GATE 0–7. Текущий — GATE 4A. См. `00_project_control/ROADMAP.md`.

## 31. Confirmed / Unconfirmed Claims
- **Confirmed (FACT, с источниками):** обязательные роли PBP/BAP/BASS;
  телефон не в аудиотракте; широковещательный режим без интернета;
  LC3 параметры; обязательные конфигурации 16/24 кГц; presentation delay
  40 мс; реальные внедрения Auracast; ограничения OS для сторонних
  приложений; существование Auracast→telecoil продуктов; телефоны-микрофоны
  хуже close-talk в исследованиях.
- **Unconfirmed (REQUIRES EXPERIMENT/RESEARCH):** end-to-end latency стенда;
  покрытие/ёмкость; WER clean-feed vs телефон в реальном зале; синхронизация
  текста; точность «Не расслышал»; совместимость Bridge-T с моделями;
  патентоспособность.
- **Rejected (REJECTED LEGACY):** BT 5.2 = Auracast; ~100 м как гарантия;
  неограниченное число слушателей как гарантия; задержка 30/50/300 мс как
  факт; «работает со всеми СА/КИ»; «революционное/аналогов нет».

## 32. Предшествующие технологии персональной передачи речи

(Добавлено GATE 6A; подробности — в карточках конкурентов.)

### 32.1 СОНЕТ 2.0 (ГК «Исток-Аудио»)
Проприетарная UHF FM-система (863–865 МГц, 15 каналов) для инклюзивного
образования: петличный микрофон → передатчик → приёмник → заушный
индуктор/neckloop → СА/КИ в T/TM; до 11 приёмников в кейсе; активно
продаётся в 2026. **Решает** доставку чистого звука и групповое
использование; **не решает** текст/captions/приложение.
См. `08_competitor_analysis/competitor_cards/SONET_2_0.md`.

### 32.2 Phonak Roger
Проприетарный 2.4 ГГц цифровой канал (<20 мс), RogerDirect внутри СА,
встроенные приёмники для КИ, сеть до 35 микрофонов, образование
(Roger for Education). **Референс по SNR, задержке и зрелости.**

### 32.3 Roger MyLink (историческое решение)
Универсальный индукционный neckloop-приёмник (T-coil, любые бренды),
2.4 ГГц/FM; **без USB**; EOL/legacy. Предшественник класса Bridge-T.

### 32.4 Roger NeckLoop (актуальный аналог)
Универсальный neckloop-приёмник с **USB-C audio interface**: аудио
Roger-микрофона можно подать в компьютер → сторонний STT → live captions.
Официально документировано с апреля 2021. **CRITICAL PRIOR ART** для
«clean-feed ASR». См. `competitor_cards/PHONAK_ROGER.md` (ROGER_STT_PRIOR_ART).

### 32.5 Auracast ALS
Открытый транспорт: Auri, Bettear, Audeara; реальные внедрения (UQ — 65
аудиторий, Oxford). Текстовый слой отсутствует; парк совместимых СА/КИ
ограничен; ALS-стандарт IEC 60118-17 ожидается после 2027.

### 32.6 Как от этого пришли к исследуемой архитектуре
От FM-радиокласса и Roger — понимание ценности близкого к источнику
микрофона, индукционного выхода и низкой задержки; от Auracast —
открытый транспорт и массовые устройства; от Roger NeckLoop — знание,
что clean feed уже используется для STT. Исследуемый слой — **единая
образовательная сессия** с общим временны́м доменом аудио и текста.
См. `12_reports/ASSISTIVE_AUDIO_EVOLUTION.md`,
`11_presentations/inclusion/SLIDE_ASSISTIVE_AUDIO_EVOLUTION.md`.
