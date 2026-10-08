# ARCHITECTURE_FREEZE_2026_09

GATE 4B — Architecture Freeze. Дата: 2026-09-26. Статус: **FROZEN для MVP**.
Изменения — только через новое решение в `DECISIONS.md`.

## 1. SOURCE

```
микрофон преподавателя / микшер
        |
      PCM (clean audio)
```

- Источник — чистый электрический фид (не акустика зала).
- В лаборатории: line-in / mock. В реальной системе: микрофон/микшер.

## 2. Разветвление

```
                         CLEAN AUDIO (PCM)
                               |
                 +-------------+-------------+
                 |                           |
                 v                           v
            AUDIO PATH                    DATA PATH
                 |                           |
                LC3                         ASR
                 |                           |
            Auracast                   transcript (segments)
                 |                           |
          compatible sink                 WebSocket
                 |                           |
              audio                     Route+ App
```

## 3. Отдельный путь (независимый от App)

```
Auracast Sink -> Bridge-T -> T/MT -> слуховой аппарат / КИ
```

## 4. Критические ограничения (FROZEN)

1. Route+ App **НЕ находится** в основном Auracast audio path.
2. Route+ App **НЕ реализует** собственный generic Auracast stack.
3. Route+ App **НЕ обещает** управление Auracast на любом смартфоне.
4. ASR получает **PCM до LC3** (отдельная ветка).
5. Аудио и текст — **независимые транспорты**; их объединяет только
   общий источник и сессионное время.

## 5. ENGINEERING BASELINE

### LC3

| Параметр | Значение |
|---|---|
| Конфигурация | **24_2_1** |
| Частота | 24 кГц |
| Кадр | 10 мс |
| Октетов/кадр | 60 |
| Битрейт | 48 кбит/с |
| Обязательная альтернатива | **16_2_1** (учитывать при hardware testing) |

**Статус: ENGINEERING BASELINE — НЕ measured result.**
Обоснование: `02_research/02_lc3_latency/LC3_CONFIGURATION_MATRIX.md`.

### Latency

| Критерий | Значение |
|---|---|
| TARGET | ≤ 60 мс |
| ACCEPTABLE | ≤ 100 мс |
| REJECT | > 150 мс |

**Статус: TARGET / ACCEPTANCE CRITERIA — значения НЕ достигнуты и НЕ измерены.**
Обоснование: `02_research/02_lc3_latency/LATENCY_DEEP_DIVE.md`.

## 6. Границы MVP (software)

- Реализуется: текстовый слой (captions, missed speech, notes, bookmarks,
  a11y, demo).
- Не реализуется: Bluetooth stack, Auracast-подключение, firmware, PCB,
  AI-функции как рабочие.

## 7. Технологический baseline

- Frontend: React + TypeScript + Vite (responsive web / PWA-подобный).
- Backend: Python + FastAPI + WebSocket.
- ASR: интерфейс `ASRProvider`, в MVP — `MockASRProvider`.

## 8. Privacy baseline

privacy-by-default: сырое аудио не хранится постоянно; заметки — локально.
См. `03_requirements/PRIVACY_REQUIREMENTS.md`.

## 9. Связанные документы

`04_architecture/SYSTEM_ARCHITECTURE.md`, `APP_ARCHITECTURE.md`,
`DATA_PIPELINE.md`, `13_demo/app_demo/APP_MVP_SPEC.md`.
