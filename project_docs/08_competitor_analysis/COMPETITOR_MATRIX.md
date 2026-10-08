# COMPETITOR_MATRIX

GATE 6A. Обновлено: 2026-09-26. Источники: web-исследование (доступ
2026-09-26). Обозначения: **YES / NO / PARTIAL / UNKNOWN / PROPOSED**.
Правило: не подгонять таблицу под проект.

## Классы решений

| Класс | Описание | Примеры |
|---|---|---|
| **A. FM / proprietary assistive listening** | собственный радиоканал, спец. приёмники | **СОНЕТ 2.0**, **Phonak Roger** (+ NeсkLoop, MyLink legacy) |
| **B. Auracast ALS** | LE Audio broadcast + совместимые устройства | Auri, Bettear, Audeara, Venucast |
| **C. Caption / transcription apps** | текст без аудиосистемы | Ava, Google Live Transcribe, HearAura |
| **D. Hybrid systems** | аудио + accessibility data (частично) | Bettear (audio + venue captions), HearAura (Auracast + captions), Roger NeckLoop (audio + USB→STT) |
| **E. Proposed** | **Inclusive Route+ / Точка звука** | clean-feed → Auracast/Bridge-T + синхронизированный текст |

## Матрица (транспонированная: строки — признаки, столбцы — решения)

| Признак | СОНЕТ 2.0 | Roger + NeckLoop | Roger MyLink [legacy] | Auri | Bettear | HearAura | Ava | Google Live Transcribe | Inclusive Route+ [PROPOSED] |
|---|---|---|---|---|---|---|---|---|---|
| Target users | дети/взрослые с наруш. слуха, СА/КИ | любые СА/КИ (NeckLoop) | любые СА/КИ с T-coil | учреждения/вузы | учреждения/вузы | пользователи iPhone | школы/вузы | широкая аудитория | PRIMARY: СА/КИ/слабослышащие; SECONDARY: широкая |
| Education | YES | YES | YES (истор.) | YES | YES | PARTIAL | YES | YES | YES (фокус) |
| Teacher microphone | YES (петличный) | YES (Roger mic) | YES (Roger mic) | YES (через аудиосистему) | YES | NO | NO | NO | YES (clean feed) |
| Dedicated wireless | YES (863 МГц UHF) | YES (2.4 ГГц) | YES (2.4 ГГц) | YES (Auracast) | YES (Auracast) | NO | NO | NO | YES (Auracast) |
| FM/proprietary | YES (FM/UHF) | YES (проприетарный) | YES | NO | NO | NO | NO | NO | NO |
| Auracast | NO | NO | NO | YES | YES | YES (assistant) | NO | NO | YES (план) |
| Direct HA/CI | PARTIAL (через T/DAI) | YES (RogerDirect/CI-приёмники/NeckLoop) | YES (через T-coil) | PARTIAL (совместимые) | PARTIAL (через RX) | PARTIAL (vendors) | NO | NO (OS) | PARTIAL (совместимые) |
| Telecoil | PARTIAL (сам RX без T; формирует поле) | YES (NeckLoop → T-coil) | YES (neckloop → T-coil) | YES (RX1 + neckloop) | YES (RTX + neckloop) | NO | NO | NO | YES (Bridge-T) |
| Neckloop | YES (индукционная петля) | YES | YES | YES (аксессуар) | YES | NO | NO | NO | PROPOSED |
| Own receiver | YES | YES (Roger RX/NeckLoop) | YES (NeckLoop) | YES (RX1) | YES (RTX/B-PASS) | NO | NO | NO | RESEARCH (Bridge-T) |
| Consumer earbuds | NO | NO (кроме Roger Focus/наушников) | NO | YES (Auracast-наушники) | YES (Auracast) | YES | YES (BT) | YES (BT) | YES (Auracast) |
| Mobile app | NO | PARTIAL (MyRogerApp/myPhonak) | NO | PARTIAL (менеджер) | YES | YES | YES | YES | YES (Route+) |
| Clean audio output | YES (аудио с микрофона) | YES (Roger-mic audio) | YES | YES | YES | PARTIAL | NO | NO | YES |
| USB audio output | NO | **YES (NeckLoop, USB-C)** | NO | UNKNOWN | YES (RTX USB STT feed) | NO | N/A | N/A | YES (ASR-тракт) |
| Speech-to-text | NO | **YES (сторонний STT через USB, офиц. с 2021)** | NO | NO | PARTIAL (RTX → компьютер) | YES | YES | YES | YES (clean-feed, план) |
| Live captions | NO | YES (через сторонний STT) | NO | NO | PARTIAL (venue captions) | YES | YES | YES | YES (план) |
| Same-source STT | NO | **YES (Roger-mic → USB → STT)** | NO | NO | PARTIAL | PARTIAL (venue feed) | NO (микрофон) | NO (device audio) | YES (план) |
| Timestamped transcript | NO | PARTIAL (зависит от стороннего STT) | NO | NO | PARTIAL | PARTIAL | YES | YES | YES (план, source_clock) |
| Missed Speech | NO | NO | NO | NO | NO | PARTIAL («Catch me up» = summary) | NO | PARTIAL (Hold/scrollback) | YES (N-сек replay) |
| Notes | NO | NO | NO | NO | NO | NO | YES | NO | YES (MVP) |
| Translation | NO | NO (зависит от STT) | NO | NO | PARTIAL | UNKNOWN | YES | PARTIAL | PHASE_2 |
| AI summary | NO | NO | NO | NO | NO | YES («Catch me up») | YES | NO | RESEARCH |
| Confidence handling | NO | NO | NO | NO | NO | NO | NO | NO | PROPOSED (эксп.) |
| Accessibility profile | NO | PARTIAL (Phonak-экосистема) | NO | NO | UNKNOWN | YES | YES | YES (OS) | YES (MVP) |
| Works without Internet — audio | YES | YES | YES | YES | YES | YES | PARTIAL | PARTIAL | YES (локально) |
| Works without Internet — text | NO (нет текста) | PARTIAL (STT зависит от ПО) | NO | NO | PARTIAL | YES (on-device) | PARTIAL | YES (on-device) | RESEARCH (on-device ASR) |
| Special receiver required | YES (Исток RX) | YES (Roger RX/NeckLoop) | YES (MyLink) | YES (RX1 или своё Auracast-устр.) | YES (RX) | NO | NO | NO | PARTIAL (Bridge-T для T/MT) |
| Mass consumer device path | NO | NO | NO | YES (Auracast) | YES (Auracast) | YES (iPhone) | YES | YES | YES (Auracast) |
| Current/legacy status | current | current (NeckLoop); MyLink legacy | **legacy/EOL** | current | current | current | current | current | PROPOSED (not released) |
| Evidence quality | vendor tests (no peer review) | official docs + vendor studies; peer-reviewed citations | archived official docs | vendor/prima SIG cases | vendor/SIG cases | official site | official + independent reviews | official docs | research files + MVP |

## Три ближайших конкурента (по пересечению с проектом)

1. **Phonak Roger + Roger NeckLoop** — ближайший по функции
   «clean-feed → STT» (официально с 2021) и по мосту в T-coil; но
   проприетарный транспорт, текст не привязан к сессии/студенту.
2. **СОНЕТ 2.0** — ближайший по российскому образовательному сценарию и
   групповой доставке через индукцию; текста нет вообще.
3. **Bettear / HearAura** — ближайшие по «аудио + текст» в Auracast-среде;
   у Bettear — venue-инфраструктура, у HearAura — iPhone-центричность и
   «summary» вместо дословного replay.

## Связанные документы

`competitor_cards/SONET_2_0.md`, `competitor_cards/PHONAK_ROGER.md`,
`../09_novelty_rid/NOVELTY_MAP.md`, `../12_reports/ANALOG_RED_TEAM.md`,
`../12_reports/ASSISTIVE_AUDIO_EVOLUTION.md`.
