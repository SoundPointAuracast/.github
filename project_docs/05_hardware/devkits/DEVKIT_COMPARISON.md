# DEVKIT_COMPARISON

GATE 4A.3. Дата: 2026-09-26. Цены/наличие — на дату; проверять перед
покупкой. Источники: сайты вендоров + дистрибьюторы (цена — SECONDARY).

## Часть A. Программируемые платформы

| Платформа | Чип | LE Audio | Broadcast Source | Broadcast Sink | Auracast (PBP) | SDK | Audio in | Audio out | Цена | Наличие | Сложность |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **nRF5340 Audio DK** | nRF5340 | да (LC3, CIS, BIS) | да | да | да («all Auracast features») | nRF Connect SDK (Zephyr) | 2× 3.5 мм line-in, digital mic, USB | 3.5 мм headphone out (CS47L63), USB | ~$172.57 (DigiKey) | в наличии | средняя |
| nRF54H20 DK | nRF54H20 | не подтверждено в NCS | ? | ? | ? | NCS | нет кодека | I2S/PDM | UNKNOWN | новый | средняя-высокая |
| nRF54L15 DK | nRF54L15 | нет Audio PLL → ограничено | ограничено | ограничено | нет | NCS | — | внешний кодек | UNKNOWN | в наличии | средняя |
| nRF52840 DK | nRF52840 | **нет** (до 5.2 ISO) | нет | нет | нет | NCS | — | — | ~$50 | в наличии | низкая, но бесполезно |
| CC2755R10 LaunchPad | TI CC2755 | **нет** LE Audio/ISO/LC3 | нет | нет | нет | SimpleLink/Zephyr | I2S | — | UNKNOWN | в наличии | низкая, бесполезно |
| NXH3675 | NXP | да (LC3/LC3plus) | да | да | да (certified) | NXP SDK — **NDA** | PDM | внешний кодек | chip $2.61@10k | только по NDA | высокая |
| QCC5181 EVK | Qualcomm | да | да | да | да | ADK (лицензия) | зависит | зависит | ~£200 | под заказ | высокая |
| ESP32-H4 / S31 | Espressif | заявлено (BIS/CIS) | заявлено | да | **спорно** (issue: TX не поддержан) | ESP-IDF/ESP-BLE-AUDIO | I2S | I2S | UNKNOWN | новые | средняя-высокая |
| ESP32/C3/C5/C6/S3 | Espressif | **нет** | нет | нет | нет | — | — | — | $5–15 | везде | низкая, бесполезно |
| EFR32BG | Silicon Labs | нет LE Audio host-стека | нет | нет | нет | Simplicity | I2S | внешний кодек | — | везде | бесполезно |
| Feasycom FSC-BT1038A/B | QCC3083/3084 | да | приёмные модули | да | да | Feasycom FW | I2S/PCM | I2S/PCM | $8.90/9.50 | в наличии | средняя |
| Feasycom FSC-BT631D | nRF5340 | да | да | да | да | FW | I2S | I2S | $9.90 | в наличии | средняя |

## Часть B. Готовое Auracast-железо для стенда

| Устройство | Вендор | Роль | Выход | Цена | Примечание |
|---|---|---|---|---|---|
| **FlooGoo FMA120** | Flairmesh | TX/RX/relay, USB | USB audio | ~$45–130 | официально Auracast-квалифицирован; дешёвый источник с ПК |
| **FlooGoo FMA121** | Flairmesh | TX (USB-C + **3.5 мм вход**) | — | UNKNOWN | идеален для «line-in → Auracast» |
| MoerDuo (AHA02) | MoerLab | TX/RX переключаемый, 3.5 мм + mic | 3.5 мм line out | $99 | бюджетный стенд «всё в одном» |
| MoerLink / DB100 | MoerLab | TX, USB | — | $59 | источник с ПК |
| **Avantree AuraClip (RC240)** | Avantree | RX, Auracast | **3.5 мм AUX** | €69.99 | дешёвый sink с аналоговым выходом для Bridge-T |
| Oasis Aura | Avantree | TX, TV/venue | — | €129.99 | источник |
| AirCast | Venucast | TX, pro | — | €349.99 | XLR/6.35/AUX, 150 м LoS |
| Auri TX2N / RX1 | Ampetronic | pro TX/RX | проф. аудио/3.5 мм | quote | для полевых тестов |
| Bettear CASTER / RTX | Bettear | pro TX/RX | проф./3.5 мм | quote | для полевых тестов |
| NEXUM VOCE+ | Nexum | TX | — | от $79 | миниатюрный |
| Aurawave AW100 | Ezurio/Cloud2GND | TX (dev board) | аналог/цифра | quote | почти turnkey источник |

## Рекомендации

1. **Источник (лаборатория):** nRF5340 Audio DK — единый SDK для source и
   sink, 3.5 мм вход, поддержка broadcast applications. Альтернатива —
   FMA121/MoerLink для быстрого старта.
2. **Sink с аналоговым выходом (Bridge-T):** nRF5340 Audio DK (3.5 мм out)
   для программируемого стенда; **Avantree AuraClip** — моментальный
   дешёвый вариант; MoerDuo — если нужен TX/RX.
3. **Бюджетный набор:** FMA120 (или MoerLink) + AuraClip ≈ **<$150** —
   полный источник+приёмник с аналоговым выходом.
4. **Избегать:** nRF52840 (нет LE Audio), TI CC27xx (нет LE Audio),
   ESP32 классические (нет ISO), NXP NXH3675 (NDA), Qualcomm EVK (дорого/
   лицензия), Silicon Labs (нет стека).

## Открытые проверки

- Поддержка LE Audio на nRF54H20/L15 в актуальном NCS.
- Цена/наличие Aurawave AW100; analog output.
- Реальный статус Auracast TX на ESP32-H4.
- PBP-квалификация модулей Feasycom/MoerLab (логотипы ≠ квалификация).

## Связанные документы

`13_demo/hardware_demo/AUDIO_MVP_SPEC.md`, `BRIDGE_T_MVP_SPEC.md`,
`07_experiments/EXPERIMENT_MASTER_PLAN.md`.
