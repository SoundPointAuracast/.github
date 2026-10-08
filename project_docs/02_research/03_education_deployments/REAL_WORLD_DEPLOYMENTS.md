# REAL_WORLD_DEPLOYMENTS

GATE 2.4. Дата: 2026-09-26. Только web-источники. PRIMARY = SIG/vendor/
университет official; SECONDARY = отраслевая пресса.

## Образование

### D-EDU-01 — University of Oxford (Бодлианские библиотеки → стандарт кампуса)
- **Страна:** UK. **Место:** библиотека Blackwell Hall, Weston Library +
  общеуниверситетский стандарт.
- **Проблема:** нет ALS в зале; мрамор/историческое здание исключают
  индукционные петли; разрозненный AV/Dante.
- **Система:** Ampetronic | Listen **Auri** (Auracast). Трансмиттер
  **Auri TX2N-D** через Dante. Приёмники **16× Auri RX1** (8 neckloop,
  8 наушников), доки D4/D16.
- **Год:** пилот ~2 года; принят как стандарт ноябрь–декабрь 2025.
- **Особенности:** Auracast YES; HA/CI YES; telecoil — через neckloop;
  интернет не нужен; multi-room YES; captions нет.
- **Ограничения:** посетители без Auracast берут RX1 напрокат; rollout
  поэтапный, масштаб на дату — UNKNOWN.
- **Источники:** auriaudio.com/case-studies/university-of-oxford/ (PRIMARY);
  listentech.com/case-studies/auracast-assistive-listening-system-oxford/
  (PRIMARY); avinteractive.com 16.12.2025 (SECONDARY).

### D-EDU-02 — University of the Arts London (UAL), Creative Computing Institute
- **Страна:** UK. **Место:** 2 аудитории по 96 мест + 1 на 48.
- **Система:** Auri; **3× TX2N-D (Dante)**; **4× RX1**; DIY-монтаж ~1 час.
- **Год:** 2024–2025.
- **Особенности:** Auracast YES; multi-room YES (3 зала); captions/translation
  нет; интернет не нужен.
- **Ограничения:** малый пилот; нужны заёмные приёмники.
- **Источники:** bluetooth.com/auracast/auracast-location-cci/ (PRIMARY);
  listentech.com/case-studies/university-of-the-arts-london/ (PRIMARY).

### D-EDU-03 — University of Queensland (UQ) — крупнейшее развёртывание в вузе
- **Страна:** Australia. **Место:** **65 лекционных аудиторий** (несколько
  кампусов), залы 300+.
- **Система:** **Audeara** Auracast transmitters; уникальные Broadcast ID
  вида «building-room» (1-e212); QR-инструкции; приёмники Audeara напрокат
  на семестр (3.5 мм).
- **Год:** 2025–2026 (анонс 05.03.2026).
- **Особенности:** Auracast YES; свои HA/CI YES; telecoil — через neckloop
  к заёмному приёмнику; app-ассистент на телефоне; multi-room YES;
  интернет не нужен; translation/transcription — заявлено vendor-ом, live
  captions как сервис НЕ подтверждены.
- **Ограничения:** **официально: «iPhones do not currently support this
  feature»**; заёмные приёмники; IR сохранён.
- **Источники:** news.uq.edu.au 05.03.2026 (PRIMARY);
  my.uq.edu.au (PRIMARY); audeara.com (PRIMARY).

### D-EDU-04 — Academy of Hearing Acoustics (Lübeck, Германия)
- Учебный кампус (~3000 студентов/год). Несколько производителей Auracast-
  трансмиттеров (в т.ч. Bettear). Auracast как **дополнение**, не замена.
  Используется и telecoil. Источник: bluetooth.com location profile (PRIMARY).

### D-EDU-05 — Ono Academic College (Израиль)
- Bettear Auracast, образование. Детали за формой — UNKNOWN. Источник:
  bettear.com (PRIMARY, слабый).

## Публичные пространства (кратко)

| ID | Организация | Место | Система | Особенности | Источник |
|---|---|---|---|---|---|
| D-PUB-01 | Sydney Opera House | концертные залы | Auracast + существующие loops/FM | loops сохранены; multi-room; SD | SIG blog 02.06.2025 |
| D-PUB-02 | Bristol Temple Meads | ж/д станция | Ampetronic Auri TX2N + RX1 | «первое транспортное внедрение»; пилот, RNID | ampetronic.com |
| D-PUB-03 | Contact Theatre (Manchester) | театр 300 мест | Auri TX2N + 4× RX1 | первый театр Англии с Auracast | SIG profile |
| D-PUB-04 | Stadium Taranaki (NZ) | стадион 21 000 | Auri TX2N-D + PA | места, лаунжи | SIG profile |
| D-PUB-05 | MOVIX (Shochiku, Japan) | кинотеатры | Bettear **CASTER** + **RTX** | первый постоянный в Японии; CI ждут вендоров | SIG profile |
| D-PUB-06 | World/venues | церкви, клиники, театры | Auri, Bettear, EarisMax | ~35 SIG location profiles на дату | SIG location profiles |

## Выводы

1. `FACT` Auracast ALS **реально развёрнут** в вузах: UQ (65 залов) — самое
   масштабное; Oxford — стандарт кампуса; UAL — малый пилот.
2. `FACT` Везде сохраняется **парк заёмных приёмников** для устройств без
   Auracast; telecoil используется через neckloop.
3. `FACT` **Live captions из того же источника в развёртываниях не
   подтверждены**; максимум — записи vendor-ов о transcription/translation.
4. `FACT` iPhone-ассистент официально не поддержан (по данным UQ).
5. `INFERENCE` Рынок ALS смещается к Auracast, но парк совместимых
   слуховых устройств невелик (см. `05_hearing_devices/`).
6. `INFERENCE` Для проекта: развёртывания подтверждают
   жизнеспособность аудиотракта; ниша «аудио + текст из одного источника»
   остаётся незанятой в реальных внедрениях.

## Итоговый список вендоров (трансмиттеры/приёмники)

- **Трансмиттеры:** Auri TX2N/TX2N-D; Bettear CASTER/RTX; Audeara BT-03 и
  Transceiver/Lapel; Venucast AirCast/NetCast/AuraMic; HUMANTECHNIK EarisMax;
  Nexum VOCE/VOCE+; Sennheiser BTA1/BTD700; MoerLab MoerLink.
- **Приёмники (в т.ч. в T/MT):** Auri RX1 + neckloop; Bettear RTX/RTX GO +
  neckloop; Audeara; Venucast/Avantree Aura C/AuraCoil/AuraClip;
  Humantechnik earisMAX; Williams AV Infinium BA-R1; Moor MoerDuo.

## Источники (сводно)

Bluetooth SIG: auracast-location-profiles, case-study index, CCI, Academy of
Hearing Acoustics, Contact Theatre, Stadium Taranaki, MOVIX, Sydney Opera
House blog, location profiles. Vendors: Auri/Ampetronic/Listen,
Bettear, Audeara, Venucast, Avantree, Humantechnik. Университеты: UQ
official. Третичное: AV Magazine.
