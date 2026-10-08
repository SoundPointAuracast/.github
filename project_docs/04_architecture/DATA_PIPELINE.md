# DATA_PIPELINE

GATE 2.9 / 4A. Обновлено: 2026-09-26. Статус: CURRENT_CONCEPT.
Категории: [CONFIRMED], [CURRENT], [REQUIRES_RESEARCH], [REQUIRES_EXPERIMENT].

## Поток

```
clean feed (mic/mixer) ──[электрический split]──┐
                                               ▼
                                         ASR engine
                                               │
                        partial results + final results + word timestamps
                                               │
                          source_clock / segment timeline (server)
                                               │
                     ┌─────────────────────────┴───────────────────┐
                     ▼                                              ▼
             Route+ App (live view)                        session store (history)
             - live captions (partial→final)               - segments + timestamps
             - «Не расслышал» (окно N сек)                 - notes/bookmarks
             - notes / bookmarks                           - (PHASE 2) translation
             - accessibility profile                       - (FUTURE) summary/semantics
```

## Модель времени (source_clock)

```
source_clock   — монотонное время сессии (сервер)
audio_timestamp — метка кадра/сегмента в источнике
asr_start/asr_end — границы распознанного сегмента
partial_result — промежуточная гипотеза (нестабильна)
final_result   — финализированный сегмент
client_timestamp — время на устройстве (для UI, не для синхронизации)
```

`[REQUIRES_EXPERIMENT]` Точность привязки текста к аудио: word-level
timestamps от ASR шумные (WhisperX: ~60% recall при допуске 200 мс на AMI).
Рекомендуется VAD + forced alignment. Подробнее —
`06_application/missed_speech/MISSED_SPEECH_CONCEPT.md`.

## «Не расслышал»

Нажатие → показать сегменты в окне [now−N, now], N = 10–15 с (стартовое
допущение). Для MVP — **только текст** (без аудио) ради приватности.
Аудио-фрагмент — PHASE 2.

## Решения по обработке

| Вопрос | Решение на сейчас | Категория |
|---|---|---|
| Откуда ASR берёт сигнал | PCM **до** LC3 (электрический split чистого фида) | [CURRENT] — обоснование: не зависит от кодека; max качество |
| Где ASR | сервер/локально-серверно (лабораторно — сервер) | [CURRENT] |
| Хранение аудио | **не хранить** в MVP | [CURRENT] |
| Хранение текста | сессия; политика ретенции — исследовать | [REQUIRES_RESEARCH] |
| Confidence | получать от ASR; показ — research | [REQUIRES_RESEARCH] |
| Синхронизация текста и аудио | по source_clock; точность — эксперимент | [REQUIRES_EXPERIMENT] |

## Приватность

- Лекционный звук и текст могут содержать персональные данные.
- Нужны: политика хранения/удаления, согласие, разграничение доступа.
- В MVP — минимизация: без аудиоархива, без постоянного хранения текста.

## Связанные документы

`CLEAN_FEED_ASR_RESEARCH.md`, `ASR_COMPARISON_PROTOCOL.md`,
`MISSED_SPEECH_CONCEPT.md`, `APP_MVP_SPEC.md`, `SYSTEM_ARCHITECTURE.md`.
