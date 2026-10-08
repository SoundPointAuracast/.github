# AURACAST_TECHNICAL_MAP

GATE 2.1. Дата: 2026-09-26. Web-исследование (MAX-режим).
Все источники — доступ 2026-09-26. Категории: PRIMARY (спецификация/SIG/vendor
official) / SECONDARY.

## Ответы на 15 вопросов GATE 2.1

### 1. Что фактически является Auracast?
- `PRIMARY` Auracast™ — **торговая марка Bluetooth SIG**, а также «возможность»
  (capability): набор конфигураций broadcast audio, определённых в
  **Public Broadcast Profile (PBP)**. Auracast — это **не профиль**; профиль —
  PBP. Использование марки лицензируется после квалификации продукта по PBP.
  (bluetooth.com/auracast/faq/, bluetooth.com/auracast/how-it-works/;
  PBP 1.0.1 §1).
- `PRIMARY` Легаси-тезис «Auracast = Bluetooth LE Audio 5.2+» **некорректен**:
  5.2 — необходимое, но не достаточное условие (см. Q9–Q10).

### 2. Какие профили обязательны?
- `PRIMARY` PBP (профиль), BAP (управление потоками), CAP (роли),
  **BASS обязателен на приёмниках** (Broadcast Sink instantiate BASS),
  PACS обязателен на sink; для слуховых устройств — TMAP/HAP.
  VCP не обязателен для Auracast.
  (PBP §2.1/§3.1; BAP §3.8–3.9; SIG «How to build an Auracast assistant»).

### 3. Роль BAP?
- `PRIMARY` BAP определяет роли: Unicast Server/Client, **Broadcast Source**,
  **Broadcast Sink**, **Broadcast Assistant**, **Scan Delegator**; BIG/BIS,
  конфигурации LC3 и QoS (RTN, Max_Transport_Latency, Presentation_Delay).
  (BAP 1.0.1 §2.2, Table 6.4).

### 4. Роль PBP?
- `PRIMARY` PBP определяет, как **Broadcast Source сигнализирует о
  discoverable-трансляции** через extended advertising (Public Broadcast
  Announcement), и определяет **Standard Quality** (16/24 кГц) и
  **High Quality** (48 кГц конфигурации), а также правило единого шифрования
  BIG. (PBP 1.0.1 §4, Table 4.1–4.2).

### 5. Роль BASS?
- `PRIMARY` BASS — GATT-сервис, позволяющий приёмнику отдавать сканирование
  ассистенту и получать ссылки/Broadcast_Code. Обязательные характеристики:
  Broadcast Audio Scan Control Point + Broadcast Receive State. Опкоды:
  0x00 Stop, 0x01 Start, 0x02 Add Source, 0x03 Modify, 0x04 Set
  Broadcast_Code (16 октетов), 0x05 Remove. (BASS 1.0 §3, Table 3.1–3.2).

### 6. Как Assistant взаимодействует с Sink?
- `PRIMARY` Sink (Scan Delegator) рассылает solicitation с BASS UUID
  (0x184F) → Assistant сканирует эфир, читает capabilities sink (Sink PAC,
  Audio Locations) по GATT, затем пишет Add/Modify Source (Source_ID,
  PA_Sync, BIS_Sync) и при необходимости Set Broadcast_Code.
  Sink сообщает состояние BIG_Encryption: required / decrypting / Bad_Code.
  (BAP §3.9; BASS §3; SIG paper).
- `PRIMARY` Телефон **может** быть Broadcast Assistant для слухового
  аппарата; типовые assistant-устройства — смартфон, часы, ТВ.
- `PRIMARY` Zephyr предупреждает: многие ОС (особенно телефоны) не дают
  сторонним приложениям доступ к BASS UUID → свой assistant реализовать
  невозможно.

### 7. Нужен ли смартфон в аудиотракте?
- `PRIMARY` **Нет.** «At no point does the audio broadcast go through the
  phone» — аудио идёт transmitter → sink напрямую. Assistant только
  обнаруживает/выбирает и не принимает аудио. (SIG paper «Developing
  Auracast receivers…» §2; «Overview of Auracast» §2.4).

### 8. Может ли Auracast работать без Интернета?
- `PRIMARY` Да, по архитектуре: только BLE advertising + BASS/GATT. Интернет
  не задействован. (SIG pages; PBP/BAP/BASS — PRIMARY).
  Оговорка: это архитектурный вывод; прямой фразы «no internet required» в
  спецификации нет.

### 9. Что означает «Bluetooth 5.2+»?
- `PRIMARY` Core 5.2 ввёл **LE Isochronous Channels** (декабрь 2019), на
  которых строится LE Audio. PBP совместим с Core 5.2+; 5.2 — **порог**
  (bluetooth.com/auracast/faq/; PBP §2.5; SIG LE Audio specs page).

### 10. Почему 5.2 сам по себе не гарантирует Auracast?
- `PRIMARY` SIG прямо предупреждает не выводить функции из версии ядра:
  «the SIG does not endorse this, as it may lead to incorrect assumptions»
  (bluetooth.com/communicating-supported-bluetooth-functionality/, 14.01.2025).
- `PRIMARY` Нужны: LE Audio host stack + **PBP** + квалификация + фирменные
  требования. Auracast маркируется как «Layer: PBP», а не «Core 5.2».
- Пример: iPhone 17/18 указывают Bluetooth 6, но LE Audio/Auracast в
  спецификациях не заявлены.

### 11. Ограничения по числу слушателей?
- `PRIMARY` SIG: «An unlimited number of in-range Auracast receivers will be
  able to join», без роста трафика и деградации; transmitter не знает число
  слушателей (SIG FAQ; CES handout «unlimited»).
- `PRIMARY` Реальные ограничения: (a) приёмник должен быть **в зоне**;
  (b) поддерживать конфигурацию (16/24 кГц M; 48 кГц — опция);
  (c) BASS-сервер имеет **конечное** число записей Broadcast Receive State
  (рекомендуется ≥ числа BIG, которые он удерживает) — реализации должны
  управлять списком. Нормированного числового максимума нет.
- `INFERENCE` «Неограниченно» относится к эфиру, а не к ресурсам приёмника.

### 12. Ограничения по зоне?
- `PRIMARY` SIG handout: ~**100 м** для питаемого от сети публичного
  передатчика против ~10 м для paired-соединения; условия — мощность
  передатчика + антенна. Нормативного числа в PBP/BAP **нет**.
- `PRIMARY` Vendor-числа: Auri TX2N ~100 м/узел (расширяется репитерами);
  Bettear RTX 50 м; Venucast AirCast 150 м LOS (не для стадиона).
- `ENGINEERING DECISION` Для проекта: дальность — только по RF-обследованию
  конкретной площадки; число 100 м не переносить как гарантию.

### 13. Discovery?
- `PRIMARY` Primary advertising → extended advertising: Broadcast_Name
  (UTF-8, 4–32 символа), **Broadcast_ID**, Public Broadcast Announcement
  (PBP Service Data, биты encryption/SQ/HQ), затем periodic advertising с
  BIGInfo и **BASE** (Program_Info, Language). Assistant фильтрует по
  capabilities sink. (PBP §4–5; BAP §3.7; SIG paper).
- `PRIMARY` QR — «scan-to-listen»; единого стандартного формата полезной
  нагрузки QR на момент источников **нет** (SIG paper §4.7.1.2).
- `PRIMARY` Android-схема URI: `BLUETOOTH:UUID:184F;...` (AOSP 16,
  BluetoothBroadcastUtils).

### 14. Broadcast metadata?
- `PRIMARY` Broadcast_Name, Broadcast_ID, Language, Program_Info,
  Audio_Active_State, Broadcast_Audio_Immediate_Rendering_Flag,
  Appearance/Local Name, Streaming_Audio_Contexts, опционально Preferred
  Audio Contexts / Parental Rating. Формат LTV.

### 15. Защищённые трансляции?
- `PRIMARY` Шифрование **на уровне BIG**, один Broadcast_Code на все потоки
  BIG; флаг в Public Broadcast Announcement. Код передаётся в BASS
  (opcode 0x04). Способ получения кода — out-of-band: ручной ввод, QR/NFC;
  стандартного формата нет. Код нельзя менять в течение жизни BIG.
  (PBP §4.1; BASS Table 3.7; SIG paper §4.7.1).

## Схема тракта

```
MIC → PCM → LC3 encode → BAP (Broadcast Source) → PBP/BIG/BIS
    → ISO transport → Broadcast Sink → BASS/Scan Delegator
    → LC3 decode → DAC → user audio
Assistant (phone): только discovery + передача параметров в Sink,
                   в аудиотракт не входит
```

## Known limitations (для проекта)

1. `PRIMARY` Сторонние приложения на телефонах обычно **не могут** быть
   BASS-ассистентом (Zephyr doc) — discovery/join реализует ОС.
2. `PRIMARY` Только-48 кГц трансляция может быть недоступна части приёмников;
   база — 16/24 кГц (M).
3. `PRIMARY` Синхронизация stereo-пары зависит от активного ACL к одному
   assistant (SIG paper).
4. `PRIMARY` Encrypted stream требует out-of-band кода; стандарта QR нет.
5. `PRIMARY` Нет нормированной дальности/числа слушателей — только оценки.

## Что снято из легаси

- «BCS» — в спецификациях **не существует** (не найдено ни в одном
  источнике). Не использовать.
- «Bluetooth 5.2 = Auracast» — REJECTED (см. выше и RED TEAM).
- «Неограниченное количество» — применимо к эфиру, но не к ресурсам
  приёмников (см. Q11).

## Источники

- PBP 1.0.1 — bluetooth.com/specifications/specs/public-broadcast-profile/
- BAP 1.0.1 — bluetooth.com/specifications/specs/basic-audio-profile-1-0-1/
- BASS 1.0 — bluetooth.com/specifications/specs/broadcast-audio-scan-service/
- SIG FAQ — bluetooth.com/auracast/faq/
- SIG How it works — bluetooth.com/auracast/how-it-works/
- SIG paper «How to build an Auracast assistant» (PDF, 2024/2025)
- SIG paper «An Overview of Auracast» (PDF)
- SIG «Developing Auracast receivers… legacy smartphones» (PDF)
- SIG Communicating functionality guide (14.01.2025)
- SIG CES handout «Range» (PDF, 2024)
- Zephyr LE Audio architecture — docs.zephyrproject.org

## Связанные документы

`PROFILE_REQUIREMENTS.md`, `LEGACY_AURACAST_CLAIMS.md`,
`02_research/02_lc3_latency/`, `02_research/06_mobile_os_support/`.
