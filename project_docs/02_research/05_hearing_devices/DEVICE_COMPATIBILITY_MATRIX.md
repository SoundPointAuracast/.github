# DEVICE_COMPATIBILITY_MATRIX

GATE 2.5. Дата: 2026-09-26. Источники: сайты производителей, Bluetooth SIG
«Find an Auracast Product», HearingTracker (SECONDARY).
**Ключевой принцип: «LE Audio ready» ≠ «Auracast enabled».**

## Кохлеарные импланты и костные процессоры

| Производитель | Модель | LE Audio | Auracast приём | Telecoil | Требование | Источник |
|---|---|---|---|---|---|---|
| Cochlear | **Baha 7** | да | **ДА (enabled)** | нет/UNK | shipped enabled | cochlear.com (PRIMARY) |
| Cochlear | Nucleus 8 / 8 Nexa | HW ready | **НЕТ (прошивка ожидается)** | **да (встроенный)** | firmware «when available» | cochlear.com (PRIMARY) |
| Cochlear | Kanso 3 / Nexa | HW ready | нет (ожидается) | нет (через Mini Mic 2+) | firmware | cochlear.com (PRIMARY) |
| Cochlear | Nucleus 7 | нет | нет | **да** | — | Cochlear docs |
| Cochlear | Kanso 2 | нет | нет | нет | — | Cochlear docs |
| MED-EL | SONNET 3 | нет | **нет native**; через AudioLink XT + внешний Auracast-приёмник | нет | кабель/адаптер | medel.com; blog.medel.com |
| MED-EL | SONNET 2 | нет | нет native; через AudioLink | **да (интегр.)** | внешний приёмник | medel.com |
| MED-EL | RONDO 3 | нет | нет native | адаптер | внешний приёмник | medel.com |
| Advanced Bionics | Naída CI M (Marvel) | нет | нет | да (проверить) | Bridge-T | advancedbionics.com |
| Advanced Bionics | Sky CI M | нет | нет | UNK | Bridge-T? | advancedbionics.com |

`FACT` На дату **ни один крупный CI-процессор не имеет включённого
Auracast**; исключение — Cochlear Baha 7 (костная проводимость).

## Слуховые аппараты

| Производитель | Модель | LE Audio | Auracast приём | Telecoil | Примечание |
|---|---|---|---|---|---|
| GN/ReSound | **Nexia, Vivia, Savi, Enzo IA** | да | **ДА** (первый на рынке, с 2023) | да (часть моделей) | ReSound Smart 3D app v1.39+ assistant |
| GN (Beltone/Danalogic/Jabra) | Envision, Serene, Commence, Luvo, Enhance Pro 20/30 | да | **ДА** | UNK | |
| Demant | **Oticon Intent** | да | **ДА (FW 1.3.0+)** | да (miniRITE T) | Companion app |
| Demant | **Oticon Zeal** | да | **ДА** | нет | |
| Demant | Philips HearLink 50, Bernafon Encanta | да | **ДА** (SIG) | UNK | |
| Demant | Oticon Real/More/Opn | нет | нет | да (T-варианты) | Bridge-T |
| Starkey | **Edge AI, Omega AI** | да | **ДА** (SIG) | да (часть стилей) | My Starkey assistant |
| Starkey | Genesis AI | HW ready | нет (enabled) | да | Bridge-T |
| Phonak | **Audéo EON R / EON Sphere / CROS EON R** (авг. 2026) | да | **ДА** | нет (RIC) | первый Phonak; myPhonak QR |
| Phonak | Audéo Infinio Ultra / Sphere | да | **анонсировано, не включено** | нет (RIC) | даты нет |
| Phonak | Lumity/Paradise/Marvel, Naída Lumity UP/SP | нет | нет | да (T-варианты) | Bridge-T |
| Signia (WSA) | IX (Integrated Xperience) | «ready» (пресса) | **нет enabled** | да (T-часть) | Bridge-T |
| Widex (WSA) | SmartRic, Allure | нет | нет | UNK | T-моста может не быть |
| Widex | Moment | нет | нет | да (часть BTE) | Bridge-T |

`FACT` Signia и Widex на дату — **без включённого Auracast**; Phonak — только
с августа 2026; это существенно сужает парк прямых Auracast-пользователей.

## Потребительские наушники/вкладыши (приём Auracast)

Samsung Galaxy Buds2 Pro / Buds3 / Buds3 Pro; Sony WF-1000XM5; Sennheiser
Momentum TW4 / Accentum TW; JBL Tour Pro 3 / Tour One M3 / Vibe/Wave Buds3;
Jabra Elite 8/10; Technics EAH-AZ100; LG xboom; Creative Aurvana Ace;
Xiaomi Redmi Buds 6. `SIG-listed`. Google Pixel Buds Pro 2 — **UNKNOWN**
(не в SIG-списке; пресса сообщает о поддержке).

## Bridge-приёмники (Auracast → neckloop/3.5 мм)

| Продукт | Вендор | Выход | Статус |
|---|---|---|---|
| **Auri RX1 + neckloop (LA-438/439)** | Ampetronic/Listen | 3.5 мм + neckloop | в продаже |
| Infinium BA-R1 | Williams AV | 3.5 мм → neckloop | 2025–2026 |
| **AuraCoil** | Avantree | **встроенный T-coil neckloop** | pre-order, 30.11.2026, €179.99 |
| HearCoil | Avantree | проводной neckloop | pre-order, €69.99 |
| RTX + neckloop | Bettear | 3.5 мм TRRS | в продаже |
| NL-100 | Univox | neckloop | каталог |
| earisMAX + Teleschlinge | Humantechnik | 3.5 мм / neckloop | в продаже |
| NKL 001 | Williams AV | neckloop, 8–16 Ω | в продаже |

## DIRECT AURACAST USERS

Слуховые аппараты: ReSound Nexia/Vivia/Savi/Enzo IA (+ Beltone/Jabra),
Oticon Intent (FW 1.3.0)/Zeal (+ Philips/Bernafon), Starkey Edge AI/Omega AI,
Phonak Audéo EON (авг. 2026). CI: только Cochlear **Baha 7**.
Плюс потребительские earbuds/headphones из списка выше.

## BRIDGE-T TARGET USERS

Устройства **без** Auracast, но **с telecoil (T/MT)**:
Cochlear Nucleus 7/8 (N8 — до прошивки), MED-EL SONNET 2/RONDO 3,
Advanced Bionics Naída CI M, Phonak Lumity/Paradise/Marvel T-варианты и
Naída UP/SP, Oticon Real/More/Opn T, ReSound Omnia/One/LiNX/Enzo T,
Signia IX/AX/X T-модели, Starkey Genesis/legacy, Widex Moment.

`FACT` Важное исключение: RIC-модели без telecoil (Phonak Infinio,
Widex SmartRic/Allure) **не являются** целями Bridge-T — им нужен 3.5 мм
/ DAI путь или Auracast-поддержка.

## Итоговая оценка

- `INFERENCE` Парк **прямых** Auracast-слуховых устройств пока мал:
  массовые вендоры включили поддержку только 2023–2026, CI — почти нет.
- `INFERENCE` **Bridge-T критичен** для переходного периода (10+ лет):
  большая часть установленных СА/КИ имеет telecoil, но не Auracast.
- `INFERENCE` Одновременно многие новые RIC-модели **теряют telecoil** —
  значит Bridge-T не универсален; потребуется и 3.5 мм/DAI путь.

## Задачи верификации

- Региональные прошивки/приложения (Starkey, Phonak, Signia).
- Telecoil по конкретным стилям/моделям (даташиты).
- Pixel Buds Pro 2; Sony WF-1000XM6.

## Источники

cochlear.com; medel.com; blog.medel.com; advancedbionics.com; phonak.com;
oticon.com; resound.com; starkey.com; signia.net; widex.com;
bluetooth.com/auracast/find-a-product/; hearingtracker.com (SECONDARY);
avantree.com; williamsav.com; bettear.com; humantechnik.com.
