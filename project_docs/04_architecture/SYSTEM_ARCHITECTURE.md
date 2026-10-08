# SYSTEM_ARCHITECTURE

GATE 6A. Обновлено: 2026-09-26. Статус: ARCHITECTURE BASELINE (v2).

Маркеры: `MVP` / `PHASE_2` / `RESEARCH` / `OPTIONAL`.
Автор проекта: Никитин Даниил Константинович (см. `AUTHORSHIP_POLICY.md`).

## Ключевой принцип (концептуальная схема)

```
                    CLEAN SOURCE
                         |
               +---------+---------+
               |                   |
          AUDIO BRANCH          DATA BRANCH
               |                   |
              LC3                  ASR
               |                   |
            Auracast           transcript
          /         \               |
 direct sink       Bridge-T         |
     |                |             |
 headphones         T/MT          Route+
 HA/CI             HA/CI           App
```

**Route+ App не является частью аудиоцепочки Auracast.** Приложение
относится только к DATA BRANCH (текст). Пунктирная связь между
пользователем и Route+ App — логическая (одна сессия), а не аудиопоток.

Неподтверждённые цифры на схеме не используются.

## Слои

### 1. SOURCE LAYER — MVP
```
MIC (лапель/гул) ─┐
MIXER / PA ───────┼──► clean feed (электрический split)
                  │         ├──► аудиоветка (LC3/Auracast)
                  │         └──► ASR-ветка (PCM до LC3)
                  └──► зал (живой звук) — пользователь слышит и его
```
- `MVP` Микрофон/микшер; электрический split.
- `MVP` `source_clock` — общее время сессии.

### 2. AUDIO BRANCH — MVP
```
PCM → LC3 encode → BAP Broadcast Source (PBP PBS) → BIG/BIS
     → Auracast эфир
```
- `MVP` База 24_2_1; обязательна 16_2_1.
- `PHASE_2` HQ 48 кГц.
- `REQUIRES_EXPERIMENT` E01/E03/E04.

### 3. DATA BRANCH — MVP
```
PCM (до LC3) → ASR → segments + timestamps (+confidence)
             → session store → WebSocket → Route+ App
```
- `MVP` Live captions, timestamp, «Не расслышал» (текст).
- `PHASE_2` Перевод, keywords, notifications, confidence UI.
- `RESEARCH` Semantics/summary.
- `NOT_NEW` Использование clean feed для STT известно (Roger NeckLoop,
  2021). Отличие исследуется в системном слое.

### 4. BRIDGE-T LAYER — RESEARCH → MVP-стенд
```
Auracast Sink (PBP PBK + BASS) → LC3 decode → PCM → DAC → усилитель
   → индукционная катушка → T/MT
```
- `KNOWN_CLASS` wireless receiver → neckloop → T-coil (Roger MyLink 2009,
  Roger NeckLoop, Auri RX1, Bettear RTX, AuraCoil).
- `RESEARCH` только конкретные технические отличия.
- `REQUIRES_EXPERIMENT` E07.

### 5. DIRECT SINK LAYER — MVP
- `MVP` Прямой приём Auracast: совместимые наушники/СА/КИ (парк ограничен).
- `REQUIRES_RESEARCH` доля совместимого парка (см. device matrix).

### 6. APPLICATION LAYER — MVP
- `MVP` Route+ App: session screen, live captions, «Не расслышал»,
  notes/bookmarks, a11y settings, demo mode.
- App **не реализует** Auracast stack (Android SystemApi/iOS).
- App может показывать **текст без аудио** (text-only путь).

### 7. OPTIONAL AI LAYER
- `OPTIONAL` translation, semantic events, summary.
- `PROMISING_FOR_SEARCH` confidence-aware critical captions (N07).

## Что изменилось относительно v1

- ASR-ветка явно питается PCM **до** LC3.
- Bridge-T переклассифицирован в `KNOWN_CLASS`.
- Добавлено разделение AUDIO BRANCH / DATA BRANCH и запрет трактовать
  Route+ как часть аудиоцепочки.
- Убраны любые числовые характеристики с концептуальной схемы.

## Открыто

- Схема split (аппаратная/программная), тайминг.
- Выбор ASR-движка (LOCAL_ASR_SELECTION) и хостинга.
- Сертификация/квалификация аудиостанции.
- Масштабирование (multi-node) — `RESEARCH`.

## Связанные документы

`APP_ARCHITECTURE.md`, `DATA_PIPELINE.md`, `BRIDGE_T_EVOLUTION.md`,
`diagrams/architecture_gate6.mmd`, `diagrams/architecture_gate6.drawio`,
`../00_project_control/ARCHITECTURE_FREEZE_2026_09.md`.
