# APP_REQUIREMENTS — Route+ App

Статус: DRAFT. Future-функции **не** считать реализованными.

Приложение — не «пульт подключения», а самостоятельный ассистивный слой.

---

## MVP

| ID | Функция | Категория |
|---|---|---|
| APP-01 | Вход в сессию (QR / код) | TARGET |
| APP-02 | Отображение активной лекции | TARGET |
| APP-03 | Live transcript | TARGET |
| APP-04 | Timestamp | TARGET |
| APP-05 | «Не расслышал» | TARGET |
| APP-06 | Заметка | TARGET |
| APP-07 | Bookmark | TARGET |
| APP-08 | Accessibility settings | TARGET |

---

## PHASE 2

| ID | Функция | Категория |
|---|---|---|
| APP-20 | Перевод | TARGET |
| APP-21 | Ключевые слова | TARGET |
| APP-22 | Персональные уведомления | TARGET |
| APP-23 | Confidence indication | HYPOTHESIS |
| APP-24 | История лекции | TARGET |

---

## RESEARCH / FUTURE

| ID | Функция | Категория |
|---|---|---|
| APP-40 | Semantic extraction | HYPOTHESIS |
| APP-41 | AI summary | HYPOTHESIS |
| APP-42 | Объяснение сложной фразы | HYPOTHESIS |
| APP-43 | Автоматический конспект | HYPOTHESIS |
| APP-44 | Персональный профиль доступности | HYPOTHESIS |

---

## Принципы

- Текст доступен даже без аудиоканала.
- Никаких обещаний о точности ASR до экспериментов
  (`07_experiments/asr_accuracy/`).
- AI — вспомогательный слой, не главный продукт.

## Открыто

- Платформы (Android / iOS) и минимальные версии ОС.
- Архитектура frontend/backend — см. `04_architecture/APP_ARCHITECTURE.md`.
- Синхронизация текста и аудио во времени.
