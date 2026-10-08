# PRIOR_ART

GATE 3.2–3.4. Обновлено: 2026-09-26. **Предварительный поиск, не
юридическое заключение.** Полный отчёт по методу и списку — см. сводную
таблицу ниже. Все найденные документы — preliminary.

## Сводная таблица (наиболее близкие)

| № | Патент/публикация | Название | Assignee | Год | Область | Близость |
|---|---|---|---|---|---|---|
| 1 | US20090076804A1 | ALS with memory buffer for instant replay and speech to text | Bionica | 2007 | A+C | HIGH |
| 2 | US7881713B2 | Wirelessly triggering portable devices (venue captions/ALS/описание) | Disney | 2001 | A+E | HIGH |
| 3 | US9875753B2 | Hearing aid and method for improving speech intelligibility (HA→ASR) | Widex | 2012 | A | HIGH |
| 4 | CN108702580A | Hearing auxiliary with automatic speech transcription | Microsoft | 2016 | A | HIGH |
| 5 | WO2020142679A1 | Automatic transcription using ear-wearable device | Starkey | 2019 | A | HIGH |
| 6 | CN110798789A | HA с блоком распознавания речи и TTS | индивидуальный | 2018 | A | MEDIUM |
| 7 | US20250110688A1 | Hearing device and method of providing broadcasted audio stream | GN Hearing | 2023 | B | HIGH |
| 8 | WO2024182568A1 | Assistive listening system (time-aligned, loop/RF/BT) | Sensojoy | 2024 | B | HIGH |
| 9 | US10945082B2 | Configurable hearing device for ALS | Starkey | 2016 | B | HIGH |
| 10 | US20250030989A1 | Hearing assistance with automatic hearing loop memory | Starkey | 2019 | B | HIGH |
| 11 | US20250126419A1 | Telecoil tick-artifact mitigation | Starkey | 2023 | B | MEDIUM |
| 12 | US20160255444A1 | Companion mic + neck loop → telecoil | Starkey | 2015 | B | HIGH |
| 13 | US20160286323A1 | Wireless stereo hearing assistance (neck-loop unit) | Sonova | 2013 | B | MEDIUM |
| 14 | EP2464143B1 | Audio gateway with neck-loop antenna | Oticon | 2010 | B | MEDIUM |
| 15 | KR20210059843A | Magnetic induction loop hearing system | Baek Nam-chil | 2019 | B | MEDIUM |
| 16 | US20240430914A1 | BLE audio broadcasting method/system (Auracast) | Zgmicro | 2023 | B+E | MEDIUM |
| 17 | CN116032402A | Broadcast audio playing method (Auracast) | Goertek | 2022 | B | LOW |
| 18 | EP3021545B1 | Hearing instrument with authentication (broadcast security) | GN Resound | 2013 | B | LOW-MED |
| 19 | US20190278556A1 | Earphone hardware/software «instant replay last 30 s» | Staton Techiya | 2018 | C | HIGH |
| 20 | CA2774985C | Caption/metadata sync for replay | Caption Colorado | 2009 | C | MEDIUM |
| 21 | US11874942B1 | Meeting recordings with instant replay scrub-back | Fuze | 2019 | C | MEDIUM |
| 22 | US20230282215A1 | Transcription presentation incl. neck-loop devices | Sorenson IP | 2016 | C | MEDIUM |
| 23 | US10878721B2 | Semiautomated relay (caption service) | Ultratec | 2014 | C | MEDIUM |
| 24 | US9609395B2 | Second screen subtitles | Abecassis | 2012 | C | LOW-MED |
| 25 | CN116134836A | Sound processor (transcutaneous audio link) | Hemideina | 2020 | D | HIGH |
| 26 | US9716952B2 | Sound processing external/internal (CI link) | Cochlear Ltd | 2014 | D | HIGH |
| 27 | EP2466916B1 | Portable device HAC coil formed in PCB | BlackBerry | 2010 | D | HIGH |
| 28 | EP1250828A1 | Packaging/RF shielding for telecoils | Sonion | 2000 | D | MEDIUM |
| 29 | CN110474383B | Charger antenna (align telecoil field) | Oticon | 2018 | D | MEDIUM |
| 30 | AU2024354215A1 | Uninterrupted audio stream (roaming между TX) | Televic Rail | 2023 | E | HIGH |
| 31 | US20250300752A1 | Audio broadcast management (Auracast) | Motorola | 2024 | E | MEDIUM |
| 32 | US12418870B1 | Wi-Fi + BLE Auracast combining | Linkplay | 2024 | E | MEDIUM |
| 33 | CN117354820A | Extending Bluetooth audio network coverage | Shanghai Wuqi | 2023 | E | MEDIUM |
| 34 | WO2009137363A2 | Conversation assistant, multiple TX selection | Sensimetrics | 2008 | E | MEDIUM |
| 35 | WO2025117704A1 | Hearing-assist in performance venues | Epstein Hear Us Now | 2023 | E+A | MEDIUM |

## PA-BRIDGET (GATE 3.2)

`FACT` Класс «Auracast receiver → telecoil/neckloop» **уже существует**
продуктово (Auri RX1, Williams BA-R1, AuraCoil, Bettear RTX, Univox,
Humantechnik). Патентный ландшафт плотный: telecoil+bluetooth ~2400
документов, neck loop telecoil ~408 (FPO, preliminary).
`INFERENCE` Отдельная патентная новизна «bridge как таковой» —
**маловероятна**. Потенциально более узко: конкретная геометрия/схема
катушки, интеграция под КИ, связка с текстовым слоем.
`UNKNOWN` Выделенный патент именно на «Auracast → индукционную катушку под
процессор КИ» не найден (поиск неполный, Google Patents частично 503).

## PA-AUDIO-TEXT (GATE 3.3)

`FACT` Составляющие известны: ASR в слуховом устройстве (Widex,
Microsoft, Starkey), venue-доставка captions+ALS из одного источника
(Disney 2001, Sensojoy 2024).
`INFERENCE` Конкретная формула «один clean feed → (assistive audio path +
live ASR caption path) с синхронизацией» в выборке прямо не найдена, но
пространство плотное → **профессиональный поиск обязателен**.
`IMPORTANT` Сам по себе **parallel split** аудио на два тракта — известная
практика (broadcast, Teams); не заявлять как новизну.

## PA-MISSED (GATE 3.4)

`FACT` US20090076804 (Bionica, 2007) — ALS-буфер с instant replay + STT:
**ближайший предшественник**.
`FACT` US20190278556 (Staton Techiya, 2018) — «instant replay last 30 s».
`FACT` Replay/rewind механики широко покрыты в медиа/встречах/relay.
`INFERENCE` Специфическая связка «live captions из clean-feed Auracast +
дословный N-секундный фрагмент» может иметь узкое пространство, но
Bionica 2009 уже покрывает значительную часть комбинации.
Подробнее — `MISSED_SPEECH_PRIOR_ART.md`.

## PA-ROAMING (GATE 3.5, N10)

`FACT` Televic Rail AU2024354215A1 (2023) — очень близко к multi-node
handoff; Sensimetrics 2008 — выбор сильнейшего TX. Общая концепция
seamless roaming **вероятно покрыта**; ниша — hearing-specific Auracast.

## PA-CONFIDENCE

`FACT` Патентов/продуктов не искали отдельно на этом этапе (в список
задач не входило). `UNKNOWN` — требуется отдельный поиск.

## Итоговая оценка (предварительная, не юридическая)

| Область | Новизна | Риск prior art |
|---|---|---|
| Auracast audio | NOT_NEW | — |
| Clean-feed ASR (split) | известная практика | высокий |
| Route+ App (captions/notes) | отдельные функции известны | высокий |
| Missed speech (N-sec replay) | возможно узкая ниша | средний-высокий (Bionica) |
| Bridge-T | класс существует | высокий |
| Accessibility profile | известная практика | высокий |

## Рекомендация

- Профессиональный патентный поиск (CPC H04R25/00, H04R27/00, H04W4/80,
  G10L15/26, A61N1/372 и др.).
- Claim charts по: Bionica 2009, Starkey loop/telecoil family, Sensojoy
  WO2024182568, Televic AU2024354215, Microsoft CN108702580, Disney US7881713.
- **Не подавать заявок** до результатов (см. `DECISIONS.md` D-003).

## Ограничения поиска

Google Patents частично 503; Espacenet/USPTO/FreePatentsOnline недоступны;
публикации 2025–2026 могут быть не видны (18-мес. лаг). Полный метод —
в research-заметке GATE 3 (внутренний отчёт).
