# PROFILE_REQUIREMENTS

GATE 2.1. Дата: 2026-09-26. Источник: Bluetooth SIG спецификации.
Категории: **[SPEC]** нормативно, **[SIG]** материал SIG (informative).

## Обязательные профили и роли

### Public Broadcast Profile (PBP 1.0.1) — [SPEC]
- Роли: **Public Broadcast Source (PBS)** — в тексте спецификации
  «PBK» для Public Broadcast Sink, **Public Broadcast Sink**, **Public
  Broadcast Assistant (PBA)**.
- Table 3.1: устройство **должно реализовать хотя бы одну** из ролей.
- PBS = CAP Initiator + **BAP Broadcast Source (M)**.
- PBK = CAP Acceptor + **BAP Broadcast Sink (M)** + **BAP Scan Delegator
  (M)**; **должен инстанцировать PACS**; Scan Delegator **должен
  инстанцировать BASS**.
- PBA = CAP Commander + **BAP Broadcast Assistant (M)**.
- Совместим с **Core 5.2+**. PBP 1.0.1 требует Erratum 29407 для compliance.

### Basic Audio Profile (BAP 1.0.1) — [SPEC]
- Роли: Unicast Server/Client, Broadcast Source, Broadcast Sink,
  Broadcast Assistant, Scan Delegator.
- Broadcast Source: создаёт один/несколько BIG, каждый содержит BIS(ы);
  рассылает discovery/config и BASE.
- Broadcast Sink: обнаруживает и принимает Broadcast Audio Streams,
  публикует свои capabilities (Sink PAC, Audio Locations).
- Broadcast Assistant: сканирует за Scan Delegator, читает capabilities,
  передаёт данные, включая **Broadcast_Codes**.
- Scan Delegator: solicits assistants, принимает transfers.
- GATT: Sink = GATT Server; Assistant = GATT Client; Scan Delegator = GATT Server.

### Broadcast Audio Scan Service (BASS 1.0) — [SPEC]
- Назначение: offload сканирования с энергонезависимых устройств
  (слуховые аппараты, гарнитуры).
- Обязательные характеристики: **Broadcast Audio Scan Control Point**
  (Write / Write Without Response) + ≥1 **Broadcast Receive State**
  (Read, Notify).
- Опкоды: 0x00 Remote Scan Stopped; 0x01 Remote Scan Started;
  0x02 Add Source; 0x03 Modify Source; 0x04 Set Broadcast_Code (16 октетов);
  0x05 Remove Source.
- BIG_Encryption state: 0x00 not encrypted, 0x01 code required,
  0x02 decrypting, 0x03 Bad_Code.
- BASS erratum 23366 обязателен для compliance.

## Quality levels (PBP) — [SPEC]

| Уровень | Определение | Конфигурации |
|---|---|---|
| Standard Quality | конфигурация BAP, обязательная для Broadcast Sink | 16 кГц и 24 кГц, 10 мс |
| High Quality | любые LC3 48 кГц конфигурации | 48_1_1 … 48_6_2 (PBP Table 4.2) |

- BAP Table 6.4: `16_2_1` — **M** и для Broadcast Source, и для Broadcast Sink;
  `24_2_1` — **M** для Broadcast Sink.
- Encryption: если флаг установлен, **весь BIG шифруется одним кодом**
  (или весь не шифруется).

## Сколько нужно «в аудиотракте»

| Роль | Кто | Нужна для звука? | Нужна для discovery? |
|---|---|---|---|
| Broadcast Source | станция аудитории | да | да |
| Broadcast Sink | наушники / СА / КИ / Bridge-T | да | да |
| Broadcast Assistant | телефон / часы / ТВ | **нет** | желательна |
| Scan Delegator | приёмник | да (BASS) | да |

`PRIMARY` Ключевой вывод: телефон **не обязателен** в аудиотраекте.

## Что должны реализовать будущие узлы проекта

### Аудиостанция (Broadcast Source)
- PBP PBS + BAP Broadcast Source; LC3 encode; BIG/BIS; advertising с
  Broadcast_Name, Broadcast_ID, Public Broadcast Announcement; BASE.
- Поддержка минимум 16_2_1 и 24_2_1 (Standard Quality); опционально HQ 48 кГц.

### Bridge-T (Broadcast Sink + вывод в индукцию)
- PBP PBK + BAP Broadcast Sink + Scan Delegator; **BASS**; PACS.
- LC3 decode; аналоговый выход на катушку.
- Если заявляется как «Auracast-совместимый» — квалификация по PBP
  (иначе можно говорить только «LE Audio broadcast audio»).

### Route+ App (Assistant / UI)
- `SPEC/RESEARCH` Публичные API мобильных ОС обычно **не позволяют**
  стороннему приложению выполнять роль Assistant (см.
  `02_research/06_mobile_os_support/MOBILE_AURACAST_SUPPORT.md`).
- Следовательно, App не должен обещать «мы реализуем Auracast внутри
  приложения»; App = UI + QR + captions + assistant через системное API
  (где доступно) либо через вендорское приложение приёмника.

## Роли и терминология (сводно)

| Термин | Значение |
|---|---|
| BIS | Broadcast Isochronous Stream |
| BIG | Broadcast Isochronous Group (≥1 BIS) |
| BASE | Broadcast Audio Stream Endpoint (описание потока) |
| PBP | Public Broadcast Profile |
| PBS/PBK/PBA | Public Broadcast Source/Sink/Assistant |
| BASS | Broadcast Audio Scan Service |
| PAD | Presentation Delay |

## Открытые вопросы

- Квалификационная стратегия для станции и Bridge-T (PBP-квалификация vs
  «LE Audio broadcast audio» без марки).
- Возможность использовать готовые квалифицированные модули (Nordic и др.)
  вместо собственной квалификации.
- Выбор SQ vs HQ для аудитории; совместимость с legacy-парком.

## Источники

- PBP 1.0.1, BAP 1.0.1, BASS 1.0 — bluetooth.com/specifications/
- BAP Table 3.5/3.11/6.4; PBP Table 3.1–3.3, 4.1–4.2; BASS Table 3.1–3.2, 3.7.
- SIG papers: «How to build an Auracast assistant», «Overview of Auracast»,
  «Developing Auracast receivers for legacy smartphones».
- Zephyr LE Audio architecture doc.
