# AURACAST_TELECOIL_PRIOR_ART

GATE 2.7. Дата: 2026-09-26. Web-источники, доступ 2026-09-26.

## Главный ответ

`FACT` **Да, устройства «Auracast → telecoil/индукция» уже существуют
коммерчески (2024–2026).** Bridge-T как класс продукта **не является новым**.

Существующие продукты:

| Продукт | Вендор | Вход | Выход | Статус |
|---|---|---|---|---|
| Auri RX1 + Auri Neckloop (LA-438/439) | Ampetronic/Listen | Auracast | 2× 3.5 мм + neckloop | в продаже |
| Infinium BA-R1 | Williams AV | Auracast | 3.5 мм → neckloop | 2025–2026 |
| **AuraCoil** | Avantree/Venucast | Auracast | **встроенный T-coil neckloop** | pre-order, 30.11.2026, €179.99 |
| HearCoil | Avantree | 3.5 мм | пассивный neckloop | pre-order, €69.99 |
| RTX + Neck-Loop | Bettear | Auracast | 3.5 мм TRRS | в продаже |
| NL-100 | Univox (Bo Edin) | 3.5 мм | neckloop | каталог |
| Teleschlinge | Humantechnik | 3.5 мм | neckloop | в продаже |
| NKL 001 / 008 | Williams AV | 3.5 мм | neckloop 8–16 Ω | в продаже |
| Minō | Bellman & Symfon | 3.5 мм | neckloop + встроенный T-coil | в продаже |
| B-CASTER X | Univox | Auracast **передатчик** | — | новость 22.09.2026 |

## Стандарты и нормы

- `FACT` **IEC 60118-4:2014 (+AMD1:2017)** — индукционные петли: 0 dB =
  400 мА/м; долговременное среднее поле **100 мА/м** на 1 кГц; полоса
  **100 Гц – 5 кГц ±3 дБ**; измеритель 100 Гц – 5 кГц.
- `FACT` **ADA 2010 Standards §219/§706**: в assembly areas 25% (или ≥2)
  приёмников должны быть hearing-aid compatible; разъём 1/8"(3.2 мм) моно
  (§706.2); hearing-aid-compatible приёмники должны **интерфейсировать с
  telecoil через neckloops** (§706.3).
- `FACT` ANSI S3.22 — измерения telecoil (HFA/SPLITS/RSETS); EN 60118-1
  (1995) — эквивалентность T-coil и микрофона при 31.6 мА/м.
- `FACT` IEC TR 63079 / BS 7594 — кодекс практики проектирования петель.

## Технические ограничения telecoil

- `FACT` Полоса telecoil **уже**, чем у микрофона, и уже входного сигнала
  (Valente, AudiologyOnline). Числового end-to-end значения не найдено (UNKNOWN).
- `FACT` Направленность: axial vs radial ≈ 6 дБ; типичный монтаж ~45°.
- `FACT` Гул/помехи от трансформаторов, освещения, поездов; существуют
  патенты на «telecoil hum filter».
- `FACT` Малые петли/шейные петли имеют локальные «мёртвые зоны».
- `FACT` Не у всех слуховых аппаратов есть telecoil: оценки ~70% моделей в
  активном использовании (в странах с развитыми петлями до 95%; в США до
  50% могут не иметь). (Ampetronic FAQ; HLAA — SECONDARY).
- `FACT` Поле петли моно (baseband), ADA требует моно-разъём.

## Что это значит для старого «беспроводного индуктора»

`INFERENCE` Старый индуктор (печатная спиральная катушка на FR4, ~5.1 мГн,
50 Гц–10 кГц) физически — **тот же режим** магнитной индукции, что и
neckloop (Faraday), но **другая геометрия**:
- neckloop — крупная петля вокруг шеи (поле вокруг головы);
- PCB-спираль — плоский источник малой геометрии (локальная связь).
- 5.1 мГн при 1 кГц ≈ 32 Ω реактивного сопротивления — сопоставимо с
  нагрузкой Auri RX1 (32 Ω), тогда как коммерческие neckloops 5–16 Ω.
- Ориентация на «катушку КИ»: если это T-coil режим — тот же режим; если
  ВЧ-катушка импланта — иной (RF power/data link), см.
  `05_hardware/existing_inductor/LEGACY_INDUCTOR_ANALYSIS.md`.

`FACT` Отличие от стандартного neckloop: у устройства проекта **нет**
стандартного 3.5 мм интерфейса и нет сертификации по IEC 60118-4.

## Патентный ландшафт (предварительно)

- US 2,252,641 (Poliakoff, 1937/1941) — первая патентная система индукции.
- US 10,219,065 (Otojoy, 2017/2019) — telecoil-адаптер.
- US 8,300,865 (AT&T, 2005/2012) — управляемая решётка telecoil.
- US 9,344,543 (Wistron, 2014/2016) — telecoil-совместимость мобильного устройства.
- **WO 2026/071900 A1** — «Personal induction loop» (PCT/RU2025/000034),
  Bluetooth neck loop (QCC3005/AB398) с микрофоном и усилителем — **ближайший
  к классу проекта**.
- EP 2,660,929 — neckloop с защитой от удушения.
- US 9,859,990 / 10,476,609 / 12,501,222 — hum/interference фильтры.
- US 2016/0255444 (Starkey) — companion mic + neck loop → NFMI → telecoil.
- US 2025/0110688 (GN Hearing) — приём broadcast в слуховых устройствах.

`FACT` Поиск Google Patents частично недоступен (503); список неполный.
`FACT` Плотность «telecoil AND bluetooth» ≈ 2409 результатов, «neck loop
telecoil» ≈ 408 (FreePatentsOnline).

## Вывод для Bridge-T

`ENGINEERING DECISION` Формулировка «Bridge-T уникален» — **неверна**.
Правильная рамка: «Bridge-T — это Auracast-приёмник с индукционным выходом;
класс существует (Auri RX1, AuraCoil, Bettear RTX). Возможные отличия — в
конкретной геометрии катушки/интеграции и в связке с текстовым слоем, что
требует отдельного prior-art поиска».

## Открытые вопросы

- Существует ли продукт «Auracast + встроенная катушка, ориентированная
  именно на процессор КИ» (не neckloop)? Не найдено.
- Патентоспособность конкретной схемы/геометрии Bridge-T — GATE 7.

## Источники

IEC 60118-4 (webstore.iec.ch); ADA.gov 2010 Standards; Ampetronic FAQ;
Valente, AudiologyOnline; Williams AV; Avantree; Bettear; Univox;
Humantechnik; Google Patents; FreePatentsOnline; Bluetooth SIG.
