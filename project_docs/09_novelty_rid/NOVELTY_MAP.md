# NOVELTY_MAP

GATE 6A (пересмотр). Обновлено: 2026-09-26.
Категории: NOT_NEW | KNOWN_COMBINATION | KNOWN_CLASS | DIFFERENTIATION_ONLY |
POTENTIAL_NOVELTY | PROMISING_FOR_PATENT_SEARCH | INSUFFICIENT_EVIDENCE.

## Критическое изменение после анализа СОНЕТ/Roger

**N09 больше не считается перспективным как «clean-feed → audio + text»**:
Phonak Roger NeckLoop официально (с апреля 2021) отдаёт аудио Roger-микрофона
по USB в сторонний STT. Идея «один чистый источник → аудио + распознавание»
**известна и продаётся**.

## Пересмотр N09

| Вопрос | Ответ |
|---|---|
| Что в N09 действительно известно? | Сам split чистого источника на аудио и STT — известен и задокументирован (Roger NeckLoop USB→STT, 2021; Bettear RTX USB feed; Teams; Apple «iPhone Audio»). |
| Что делает Roger? | Чистый микрофон → 2.4 ГГц → NeckLoop → (а) индукция в T-coil, (б) USB audio → сторонний STT → captions. |
| Что делает Bettear? | Auracast-аудио + venue live transcription + RTX USB как источник для speech-to-text. |
| Что делает HearAura? | Auracast assistant + captions (venue feed или микрофон телефона) + «Catch me up» (summary). |
| Что остаётся отличающимся? | См. ниже — только конкретные системные свойства, не сам split. |

### Возможные остаточные отличия (исследовать, не заявлять)

| # | Отличие | Предварительная оценка |
|---|---|---|
| 1 | **Общий timestamp-domain аудио и текста** (пользователь видит синхронно звук и текст одной сессии) | PROMISING_FOR_PATENT_SEARCH — у Roger/Bettear явно не документирован |
| 2 | **Согласованное состояние live audio / live transcript** (единая сессия, единый clock) | PROMISING_FOR_PATENT_SEARCH |
| 3 | **Автоматическая привязка транскрипта к конкретной образовательной сессии** (QR → session), а не к компьютеру | DIFFERENTIATION_ONLY |
| 4 | **«Не расслышал»** — retrieval последних N секунд дословного текста | DIFFERENTIATION_ONLY (Bionica 2007 — предшественник) |
| 5 | **Confidence-aware treatment** критичных фрагментов | PROMISING_FOR_PATENT_SEARCH |
| 6 | **Semantic educational events** | DIFFERENTIATION_ONLY |
| 7 | **Единый accessibility layer, синхронизированный с Auracast Source** | INSUFFICIENT_EVIDENCE |
| 8 | **Системная поддержка direct Auracast + Bridge-T + text-only** в одной сессии | DIFFERENTIATION_ONLY (продуктовая рамка) |

**Правило:** комбинация известных блоков **не становится новой** только
из-за объединения. Требуется доказать системный эффект, а не состав.

## Обновлённая карта

| ID | Feature | known_prior_art | closest_solution | our_difference | novelty_confidence | patentability_risk | next_action |
|---|---|---|---|---|---|---|---|
| N01 | Auracast audio | да (стандарт) | Auri/Bettear | нет | **NOT_NEW** | — | использовать |
| N02 | Clean-feed ASR | **да** (Roger USB→STT 2021; Bettear RTX; Teams) | **Roger NeckLoop** | привязка к сессии/студенту | **NOT_NEW** | очень высокий | не заявлять |
| N03 | Route+ App | да (Ava, Live Transcribe, HearAura) | HearAura | образовательный фокус + missed speech | **DIFFERENTIATION_ONLY** | высокий | UX-исследование |
| N04 | Missed Speech | да (Bionica 2007; Apple TV; Roku) | Bionica | live + N-сек + без аудио-хранения | **DIFFERENTIATION_ONLY** | средний-высокий | prior art GATE 7 |
| N05 | Bridge-T | да (Roger MyLink/NeckLoop, Auri, AuraCoil, Bettear RTX, WO2026/071900) | Roger NeckLoop | геометрия/интеграция/форм-фактор | **KNOWN_CLASS** | очень высокий | только конкретные технические отличия |
| N06 | Accessibility profile | да (платформы) | Android/Apple | интеграция в сессию | **DIFFERENTIATION_ONLY** | высокий | UX |
| N07 | Confidence-aware critical captions | research only | ConFides 2024 | live-лекция + критичные фрагменты | **PROMISING_FOR_PATENT_SEARCH** | средний | prior art GATE 7 |
| N08 | Semantic educational extraction | да (Otter/Ava) | Otter | образовательная семантика | **DIFFERENTIATION_ONLY** | высокий | research |
| N09 | Audio + synchronized accessibility layer | **да** (Roger+STT; Bettear; HearAura) | Roger NeckLoop | общий timestamp-domain, сессия, missed speech | **INSUFFICIENT_EVIDENCE** (понижен) | средний-высокий | prior art GATE 7 + E05/E06 |
| N10 | Distributed nodes / roaming | да (Televic 2023) | Televic | hearing-specific Auracast | **KNOWN_COMBINATION** | высокий | отложить |

## Что теперь точно НЕ является новизной

- Идея «clean-feed → STT / captions» (Roger, 2021; Bettear; Teams; Apple).
- Bridge-T как класс (Roger NeckLoop/MyLink, Auri RX1, AuraCoil, Bettear RTX).
- Auracast, telecoil, индукция, ASR, live captions.
- Мультиузловой roaming (Televic).
- Accessibility profile как таковой.

## Топ-3 потенциальных отличий (после пересмотра)

1. **N07 — confidence-aware critical captions** (PROMISING_FOR_SEARCH).
2. **N09 — общий timestamp-domain аудио и текста + сессионная привязка**
   (INSUFFICIENT_EVIDENCE → требуется prior art + эксперимент).
3. **N04 — Missed Speech как retrieval N секунд** (DIFFERENTIATION_ONLY).

Ни одно не считать патентоспособным до профессионального поиска (GATE 7).

## Связанные документы

`PRIOR_ART.md`, `MISSED_SPEECH_PRIOR_ART.md`, `DIFFERENTIATION_STATEMENT.md`,
`../12_reports/ANALOG_RED_TEAM.md`, `../08_competitor_analysis/competitor_cards/PHONAK_ROGER.md`.
