# MOBILE_AURACAST_SUPPORT

GATE 2.6. Дата: 2026-09-26. Источники: developer.android.com, AOSP,
blog.google, samsung.com, support.apple.com, developer.apple.com.
Категории: PRIMARY (официальные доки) / SECONDARY.

## Ключевой вывод (для архитектуры Route+ App)

`FACT` На Android **роль Broadcast Assistant/Source реализована системно**,
а публичные API сторонних приложений её **не открывают**:
классы `BluetoothLeBroadcastAssistant`, `BluetoothLeBroadcast`,
`BluetoothLeBroadcastMetadata` и др. помечены `@SystemApi` и требуют
`BLUETOOTH_PRIVILEGED` (present в API 33 и по-прежнему в API 36).
Обычное приложение из Play не получает эту привилегию.

`FACT` Публично доступны только:
- `BluetoothLeAudio` (профиль; API 31) — запросы подключённых устройств;
- `BluetoothAdapter.isLeAudioSupported()` / `isLeAudioBroadcastAssistantSupported()`
  / `isLeAudioBroadcastSourceSupported()` (API 33).

`INFERENCE` **Route+ App не может сама реализовать полный Auracast stack.**
Это подтверждает исходное опасение из GATE 2.6. Discovery/join делает ОС
(или vendor-приложение приёмника), а не приложение проекта.

## Android

| Пункт | Статус | Источник |
|---|---|---|
| LE Audio в системе | Android 13 (API 33) — «built-in support for LE Audio» | developer.android.com Android 13 features (PRIMARY) |
| System UI «Find broadcasts» | существует в AOSP с Android 13 (фрагменты Settings, QR-сканер) | AOSP Settings 13 (PRIMARY) |
| «Audio sharing» строки | AOSP 15/16; флаг preview в AOSP 16 | AOSP strings (PRIMARY) |
| Пользовательский rollout Pixel | **сентябрь 2025**, Pixel 8 и новее | blog.google (PRIMARY) |
| Samsung | One UI 6.1–8.0; в One UI 8.5 переименовано в «Audio broadcast» | samsung.com (PRIMARY) |
| Xiaomi/POCO | 14T/14T Pro/14/15/14 Ultra/15 Ultra/MIX Flip; POCO X6 Pro/F6 Pro/F7 Pro/F7 Ultra | blog.google (PRIMARY) |
| QR URI | `BLUETOOTH:UUID:184F;...` (BASS UUID) | AOSP BluetoothBroadcastUtils (PRIMARY) |
| Приложение как generic assistant | **Нет** (SystemApi + BLUETOOTH_PRIVILEGED) | AOSP API 33–36 (PRIMARY) |
| Приложение как source (TX) | **Нет** публичного API | AOSP (PRIMARY) |
| Телефон как sink (свой динамик) | публично не подтверждено | — |

`FACT` Sony/Pixel/прочие vendor-app могут управлять **своими** аксессуарами
(механизм не раскрыт), но это не generic assistant.

## iOS / iPadOS

- `FACT` В официальной документации Apple **не найдено** LE Audio или
  Auracast (страницы iPhone, AirPods, accessibility). Это **отрицательное
  свидетельство**, а не прямое заявление Apple.
- `FACT` iPhone 17 и iPhone 18 Pro указывают **Bluetooth 6**, но без
  LE Audio/Auracast; текущий User Guide — iOS 27.
- `FACT` Apple поддерживает **MFi hearing devices** (Settings → Accessibility
  → Hearing Devices), Live Listen, AirPods Pro hearing-aid feature.
- `SECONDARY` ReSound/Starkey/Oticon **приложения на iOS** умеют
  «assist» свои СА (assistant внутри аксессуара/СА); это не системный
  Auracast на iPhone.
- `INFERENCE` Для iPhone прямой приём Auracast возможен только через
  внешний приёмник (например, Bridge-T/наушники), а не через телефон.

## Разделение ответственности

| Слой | Что делает для Auracast | Доступ стороннего приложения |
|---|---|---|
| App | UI, QR-скан, управление своим устройством, captions | полный, но без привилегий |
| OS framework | Broadcast Assistant/Source services, Settings UI | нет |
| Bluetooth host stack | BASS client, PBP/BAP, PA sync, BIG/BIS, ISO | нет публичного API |
| Controller | LE Isochronous Channels, LC3, PAST/BIG | нет |
| Sink (HA/КИ/buds) | принимает аудио; может быть «принуждён» ассистентом | vendor-специфично |

`ENGINEERING DECISION` Route+ App должна строиться по модели:
1. Auracast-подключение — через **системный UI** (Android) или **vendor app
   приёмника**;
2. приложение проекта — **QR-навигация + текстовый слой** (captions, «Не
   расслышал», заметки) и, где возможно, запуск системного flow;
3. **не обещать** «подключение к Auracast из приложения проекта» на iOS.

## Последствия для UX (важно)

- `INFERENCE` Если аудио рендерит слуховой аппарат, телефон **не в
  аудиотракте** → системные live captions телефона **не могут** субтитрировать
  Auracast-звук. Поэтому текстовый слой проекта должен получать **собственный
  clean-feed ASR** (см. `04_architecture/DATA_PIPELINE.md`), а не слушать
  микрофон телефона.
- `INFERENCE` Одновременные captions с микрофона телефона + Auracast-звук
  конфликтуют: микрофон телефона слышит зал, но не чистый фид.

## Открытые вопросы

- Точное поведение системы Android 16 при QR-join с HA.
- Возможность vendor SDK для ассистирования своим приёмникам (нужны
  договорённости с вендорами).
- iOS: появление LE Audio в будущих версиях (мониторить).

## Источники

developer.android.com/blog (Android 13, 16); AOSP prebuilts API 33/36;
blog.google «LE Audio & Auracast support» (сент. 2025); support.google.com
share audio; samsung.com support ANS10001042/ANS10003615; apple.com
iPhone 17/18 specs; developer.apple.com; support.apple.com MFi hearing
devices; Zephyr LE Audio doc (ограничение BASS UUID).
