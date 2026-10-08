# APP_ARCHITECTURE

GATE 2.6 / 4A. Обновлено: 2026-09-26. Код не пишется.

## Ограничение, определяющее архитектуру

`FACT` Стороннее приложение на Android **не может** выполнять роль
Broadcast Assistant/Source через публичные API (SystemApi +
BLUETOOTH_PRIVILEGED; API 33–36). iOS-поддержка LE Audio/Auracast
не заявлена. Источник: `02_research/06_mobile_os_support/`.

**Следствие:** Route+ App — это НЕ «Auracast-клиент». Это текстово-смысловой
слой + UI, который:
1. объясняет/запускает подключение к аудио (QR, системный UI, vendor app);
2. получает **собственный** поток транскрипта (clean-feed ASR);
3. не зависит от того, каким приёмником пользуется студент (СА, КИ,
   наушники, Bridge-T).

## Слои

```
UI (accessibility-first)
  - session screen (QR)
  - live captions (partial → final)
  - «Не расслышал» (окно N сек)
  - notes / bookmarks / history
  - settings (размер, контраст, тема, вибро)
        |
Client logic
  - session join (QR / код)
  - caption stream client (текст)
  - локальный рендер и буфер последних N секунд
  - опционально: запуск системного Auracast-flow (Android)
        |
Networking
  - streaming текст (WebSocket/SSE) от backend
  - НЕ: собственный Auracast stack
  - НЕ: приём аудио на iOS
        |
Platform
  - Android: system Auracast UI, QR, a11y API
  - iOS: MFi/HA vendor app, текстовый слой
```

## Что делает кто

| Действие | App | OS | Bluetooth stack | Hardware |
|---|---|---|---|---|
| Auracast discovery/join | нет | да (Android) | да | да |
| Assistant для HA | vendor app / системное | да | да | да |
| QR-скан сессии | да | — | — | камера |
| Транскрипт | да | — | — | backend/ASR |
| «Не расслышал» | да | — | — | — |
| Запись аудио | нет (MVP) | — | — | — |

## Офлайн

`[CURRENT]` Текстовый слой требует сети до backend (если ASR серверный).
`[REQUIRES_RESEARCH]` On-device ASR как офлайн-режим — отдельное
исследование (WhisperKit и др. показывают достижимость).

## Синхронизация текста и аудио

`[REQUIRES_EXPERIMENT]` По source_clock; см. `DATA_PIPELINE.md`.

## Связанные документы

`03_requirements/APP_REQUIREMENTS.md`, `13_demo/app_demo/APP_MVP_SPEC.md`,
`MOBILE_AURACAST_SUPPORT.md`, `DATA_PIPELINE.md`.
