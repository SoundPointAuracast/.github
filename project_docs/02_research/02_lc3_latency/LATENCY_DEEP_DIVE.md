# LATENCY_DEEP_DIVE

GATE 2.3. Дата: 2026-09-26. Категории: [SPEC] / [SIG] / [VENDOR] /
[RESEARCH] / [SECONDARY]. Полный список источников — в конце.

## Главное различие

**Codec frame duration ≠ end-to-end latency.**
- Frame duration (7.5/10 мс) — параметр кодека.
- End-to-end = capture buffer + ADC + DSP + encode + ISO transport +
  presentation delay + decode + DAC + обработка слухового аппарата +
  акустический выход.

## Latency chain (полная цепочка)

| # | Этап | Что влияет | Кто управляет | Значение/оценка | Категория |
|---|---|---|---|---|---|
| 1 | Микрофон → ADC | аналоговый тракт, частота | источник | не нормировано | [SPEC] implementation-specific |
| 2 | Input buffer / DSP | размер буфера, обработка | источник | не нормировано (wired chain 10–20 мс по [SECONDARY]) | [SECONDARY] |
| 3 | LC3 encode | frame + look-ahead | источник | **11.5–12.5 мс** (44.1: 12.5–13.6) | [SPEC] |
| 4 | ISO transport (ISOAL + BIS + ретрансмиссии) | QoS RTN, Max_Transport_Latency | источник/контроллер | **8–31 мс** low latency; **45–100 мс** high reliability | [SPEC] BAP |
| 5 | Presentation delay (sink) | значение в BASE / capabilities sink | sink + источник | **обязательно уметь 40 мс**; HAP/TMAP 20–40 мс; <20 мс только через Immediate Rendering | [SPEC]/[SIG] |
| 6 | LC3 decode + DAC + HA DSP | реализация приёмника | sink/HA | входит в presentation delay; HA DSP не контролируется нами | [SPEC] |

**Спецификационно-ограниченный минимум** (24_2_1, presentation 20–40 мс):
LC3 12.5 + transport 10 + presentation 20–40 ≈ **42–62 мс** + обработка источника.
Это `INFERENCE`, не опубликованное число SIG.

One-way: Auracast — **broadcast (one-way)**; round-trip latency неприменим.

## Опубликованные числа

| Значение | Что измеряет | Источник | Категория |
|---|---|---|---|
| 12.5 / 11.5 мс | LC3 algorithmic delay (10/7.5 мс) | LC3 1.0 §2.1 | [SPEC] |
| 40 мс | presentation delay, обязательный к поддержке | BAP/SIG | [SPEC]/[SIG] |
| 10/60/20/65 мс | Max_Transport_Latency QoS-наборов | BAP/SIG | [SPEC] |
| ~20–30 мс | LE Audio по одной связи (оптимизировано) | audioXpress/Virscient | [SECONDARY] |
| «as low as 30 ms» | Auri (Auracast ALS) | Auri FAQ | [VENDOR] |
| <40 мс | Bettear CASTER | Bettear | [VENDOR] |
| 40–60 мс | наблюдения Avantree (support) | Avantree | [VENDOR] |
| «~20 мс / sub-50 мс» | маркетинг Avantree | Avantree | [VENDOR], противоречит их же support-странице |
| 30–70 мс, «max 40 мс» | IAHA Global (без ссылок) | IAHA | [SECONDARY], внутренне противоречиво |

`FACT` SIG **не публикует** числовое end-to-end latency Auracast.

## Перцептивные пороги (важно для лекции)

Студент слышит **одновременно** живой голос и Auracast-поток. Это смешение
прямого и задержанного сигналов → гребенчатая фильтрация / эхо.

| Порог | Что описывает | Источник | Категория |
|---|---|---|---|
| Detectability: +45…−125 мс; Acceptability: +90…−185 мс | lip-sync (звук vs видео) | ITU-R BT.1359-1 (1998) | [SPEC] |
| звук раньше ≤40 мс; позже ≤60 мс | EBU R37 (2007) | EBU | [SPEC] |
| audio lead ≤15 мс, lag ≤45 мс | ATSC IS-191 | ATSC | [STANDARD] |
| 0–150 мс preferred; 150–400 допустимо; >400 нет | разговорная речь | ITU-T G.114 | [SPEC] |
| >20–30 мс «disturbing» при смешении прямого и усиленного звука; ≤30 мс речь не страдает | HA direct+amplified | Stone & Moore 1999–2008 | [RESEARCH] |
| ~10 мс — гребенчатые эффекты становятся заметны; Haas-фьюжн ниже ~30 мс | live sound | QSC/SOS | [SECONDARY] |

`ENGINEERING DECISION` Именно смешение живого голоса и потока делает
**300 мс неприемлемыми** для лекции: это глубоко в зоне эха. Целевой KPI
легаси (≤300 мс) был ориентирован на иной сценарий и не подходит как цель
для аудитории, слышащей прямой звук.

## LATENCY TARGET (рекомендация)

| Параметр | Значение | Обоснование |
|---|---|---|
| Target (цель) | **≤ 60 мс** end-to-end | ниже порога detectability lip-sync; близко к минимуму спеки |
| Acceptable (допустимо) | **≤ 100 мс** | ниже типичных порогов раздражения при смешении |
| Reject (не принимать) | **> 150 мс** | зона заметного эха/задержки |
| Legacy ≤300 мс | **REJECTED как цель** | несовместимо со смешением с живым звуком |

Категория: `TARGET` / `ENGINEERING DECISION`. Не измерено.

## LATENCY ACCEPTANCE (criteria for experiments)

- E01 (latency): цель ≤60 мс; допустимо ≤100 мс; выше 150 мс — брак.
- Отдельно измерять вклад: encode, transport, presentation, decode, индукция.
- Измерять в условиях, когда пользователь слышит и прямой звук.

## LATENCY MEASUREMENT METHOD

См. `07_experiments/latency/LATENCY_TEST_PROTOCOL.md`. Кратко:
импульс/метка в источнике → запись акустического выхода приёмника →
определение задержки. Отдельно — измерение presentation delay через
сервисные данные (BASE/QoS) и через сравнение с прямым сигналом.

## Что зависит от кого

| Звено | Контролирует проект | Не контролирует |
|---|---|---|
| Source encode/transport | да (выбор QoS) | — |
| Presentation delay | частично (значение в BASE) | минимум приёмника, его DSP |
| Sink decode/DAC | да для Bridge-T | для чужих СА/КИ — нет |
| HA обработка | нет | вендор, модель, программа |

## Источники

- Bluetooth SIG: LC3 1.0; BAP 1.0.1; PBP 1.0.1; «How to build an Auracast
  transmitter»; «Overview of Auracast»; «Improving latency with LE Audio» blog.
- ITU-R BT.1359-1; ITU-T G.114; EBU R37; ATSC IS-191.
- Stone & Moore, Ear & Hearing (1999–2008).
- Auri FAQ; Bettear; Avantree support; IAHA Global; audioXpress (Virscient).
