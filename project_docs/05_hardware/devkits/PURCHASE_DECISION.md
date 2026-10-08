# PURCHASE_DECISION

GATE 6A. Дата: 2026-09-26. **Ничего не покупалось.**

Принцип: для научного проекта управляемость важнее красивого демо.

## Варианты

### OPTION A — 2× Nordic nRF5340 Audio DK
- Broadcast Source **и** Sink в одном SDK (nRF Connect SDK/Zephyr).
- 3.5 мм line-in (2 шт), on-board mic, 3.5 мм headphone out (CS47L63), USB.
- Полный контроль LC3-конфигурации и QoS (16_2_1/24_2_1/48_x, RTN,
  presentation delay).
- Доступ к коду → управляемые эксперименты по задержке/потерям.
- Цена ~$172/шт (≈$345 за пару).
- Минусы: devkit ≠ квалифицированный продукт; кривая обучения Zephyr.

### OPTION B — FlooGoo FMA120 + Avantree AuraClip
- FMA120: USB source/sink/relay, официальная Auracast-квалификация; ~$45–130.
- AuraClip: Auracast RX с **3.5 мм выходом**, €69.99 — моментальный sink для
  Bridge-T.
- Быстрый старт, низкая цена; но нет контроля LC3/QoS, ограниченная
  телеметрия.

### OPTION C — другие
- **Ezurio/Cloud2GND Aurawave AW100** — почти turnkey источник (AT-команды),
  цена не опубликована.
- **MoerLab MoerDuo** ($99) — TX/RX, 3.5 мм in/out, 22 ч.
- **Feasycom FSC-BT1038A/B** ($8.90–9.50, QCC3083/3084) — модули для
  будущего устройства.
- **ESP32-H4/S31** — заявлен LE Audio, но status Auracast TX спорный.
- **NXP NXH3675** — NDA; **Qualcomm EVK** — дорого/лицензия.

## Критерии (A/B/C)

| Критерий | A (nRF5340 ×2) | B (FMA120+AuraClip) | C |
|---|---|---|---|
| Broadcast Source | YES (полный) | YES (ограниченно) | зависит |
| Broadcast Sink | YES (полный) | YES | зависит |
| LC3 control | YES | NO | частично |
| Codec config control | YES | NO | частично |
| Debugging | YES (SWD, логи) | минимальный | разный |
| Analog input | YES (2× 3.5 мм) | YES (FMA121 3.5 мм) | частично |
| Analog output | YES (3.5 мм) | YES (AuraClip) | частично |
| Firmware access | YES (исходники) | NO | редко |
| Latency experiments | YES (QoS/PD) | ограниченно | частично |
| Packet experiments | YES | ограниченно | частично |
| Documentation | отличная | средняя | разная |
| Cost | ~$345 | ~$150–250 | от $60 |
| Availability | в наличии | в наличии | разная |
| Research value | **высокая** | средняя | средняя |

## RESEARCH STAND RECOMMENDATION

**OPTION A: 2× Nordic nRF5340 Audio DK.**
Обоснование: единственный вариант с полным контролем LC3-конфигураций, QoS
и presentation delay; позволяет выполнить E01/E03/E04 как научные
эксперименты, а не как «посмотрели, работает». Дополнительно можно
использовать как основу Bridge-T-стенда (3.5 мм выход).
Смета: ~$345 + микрофон/кабели; измерительное оборудование отдельно.

## LOW-COST DEMO RECOMMENDATION

**OPTION B: FlooGoo FMA120 (или MoerLink) + Avantree AuraClip.**
Обоснование: полный «источник + sink с аналоговым выходом» примерно за
<$150–250; не требует сборки и SDK. Годится для демонстрации тракта и
первичных прослушиваний, но не для измерений QoS/LC3.

## Что покупать первым

1. Если приоритет — **наука**: A (2× nRF5340 Audio DK).
2. Если приоритет — **демо для конкурса**: B.
3. Позже (после выбора архитектуры): модули Feasycom для прототипа
   Bridge-T.

## Не покупать сейчас

- NXP NXH3675 (NDA), Qualcomm EVK (цена/лицензия), ESP32-H4 (статус).
- Дорогие venue-системы (Auri/Bettear) — не для лабораторного стенда.

## Связанные документы

`DEVKIT_COMPARISON.md`, `13_demo/hardware_demo/AUDIO_MVP_SPEC.md`,
`BRIDGE_T_MVP_SPEC.md`, `07_experiments/EXPERIMENT_READINESS_GATE6.md`.
