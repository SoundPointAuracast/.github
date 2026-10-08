# MISSED_SPEECH_PRIOR_ART

GATE 3.4. Дата: 2026-09-26. Предварительный поиск.

## Задача

Существует ли UX-функция «я не услышал последние несколько секунд →
мгновенно показать соответствующий фрагмент транскрипта»?

## Что найдено

| Находка | Что это | Отличие от идеи проекта | Источник |
|---|---|---|---|
| **US20090076804A1** (Bionica, 2007) | ALS с буфером памяти: instant replay **и** speech-to-text | Ближайший предшественник: replay + STT в одном ALS-устройстве. Не live captions из clean-feed Auracast | Google Patents |
| **US20190278556A1** (Staton Techiya, 2018) | «instant replay: replay the last 30 seconds of the phone-call or ambient sound field» | Аудио, не транскрипт | Google Patents |
| **CA2774985C** (Caption Colorado, 2009) | Синхронизация captions/metadata при replay broadcast | Broadcast, не live lecture | Google Patents |
| **US11874942B1** (Fuze, 2019) | Instant replay scrub-back в записи встреч | Записанная встреча | Google Patents |
| Apple TV 4K | при откате на 10 с включаются субтитры | Prerecorded медиа | support.apple.com |
| Roku | «On instant replay» — субтитры | Prerecorded | developer.roku.com |
| **Google Live Transcribe** | Hold + scrollback до 3 дней | Ручной поиск, не «N секунд» | support.google.com |
| **HearAura «Catch me up»** | Summary недавних captions | **Summary, не дословный фрагмент** | hearaura.app |

## Вывод

`FACT` Точной функции «N секунд дословного live-транскрипта по нажатию»
в продуктах **не найдено**.
`FACT` Механика replay/rewind и даже «replay + STT» (Bionica 2007)
**известна**.
`INFERENCE` Потенциальная ниша — в **контексте** (live captions от
clean-feed в образовании + фиксированное окно + отсутствие аудио-хранения),
но это **не гарантирует** патентоспособность. N-секундный replay сам по
себе — очевидная UX-механика.

## Рекомендация для GATE 7

- Профессиональный поиск по CPC G10L15/26, H04R25/00, G09B21/00,
  H04N21/488 с ключами: caption replay, transcript rewind, missed speech,
  instant replay hearing.
- Claim chart по Bionica US20090076804.
- Если патентоспособность узкая — рассматривать как **UX-дифференциатор**,
  а не патентный актив.

## Категория

`DIFFERENTIATION_ONLY` (предварительно).
Не заявлять новизну.
