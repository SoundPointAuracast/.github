# ASSISTIVE_APP_LANDSCAPE

GATE 2.10. Дата: 2026-09-26. Источники: официальные сайты/app-store/
документация; научные публикации.

## Матрица функций

Y = есть, «-» = нет, ? = UNKNOWN.

| Продукт | Платформа | Live captions | Speaker labels | History | Notes | Translation | Summary | Keywords | Haptics | Аудио-подключение | Auracast discovery | HA integration | Offline | A11y profile | Missed speech | Education | Цена |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Ava** | iOS/Android/Web/Win/Mac | Y (90–95%, Scribe 99%) | Y (SpeakerID) | Y | Y | Y (15–50+) | Y | Y (словарь) | ? | BT mic / интеграции | — | — | Y | Y | — (есть scrollback) | Y (K-12, вузы) | Free / $14.99 мес |
| **Google Live Transcribe** | Android | Y | — | Y (3 дня, поиск, Hold) | — | ограниченно | — | Y | Y (вибрация по имени) | BT / внешний mic | — | через OS ASHA/LE Audio | Y | Y | — (Hold + scrollback) | Y (класс) | Free |
| **Google Live Caption** | Android | Y (звук устройства/звонки) | — | — (не хранит) | — | Y (Pixel 6+) | — | — | — | BT | — | через OS | Y | Y | — | Y | Free |
| **Otter.ai** | Web/iOS/Android/desktop | Y | Y | Y (поиск, воспроизведение) | Y | Y | Y | Y | — | mic/loopback, боты | — | — | — | Y (generic) | — (scrollback) | Y (лекции) | Free / $19.99+ |
| **MS Group Transcribe** | iOS | Y | Y (мульти-устройство) | Y | ? | Y | — | — | — | mic каждого телефона | — | — | — | — | — | собрания/класс | Free (2021–22) |
| **MS Teams captions** | Teams | Y | Y | транскрипт (время + speaker) | Y | Y (Premium) | Y (Copilot) | — | — | **чистый микс встречи** | — | — | — | — | — | Y (EDU) | включено |
| **Apple Live Captions** | iPhone 11+/iPad/Mac/Vision | Y (on-device) | — | скриншот/копия | — | (отдельный Live Translation) | — | — | — | BT / MFi / в т.ч. **«iPhone Audio»** | — | MFi/LE Audio через OS | Y | Y (профиль слуха) | — (Apple TV 10-сек back + субтитры) | Y | Free |
| **Rylo (ex-Nagish)** | iOS/Android | Y (+звонки) | частично | локальные | — | Y (50+) | — | — | — | BT, HA/CI | — | Y (pairs) | Y (Live Transcribe) | Y (Deaf/HoH) | — | — | Free (FCC) |
| **Bettear App** | iOS/Android + venue HW | Y (venue transcription) | — | — | — | через RTX feed | — | — | — | Wi-Fi / **Auracast casters** | Частично (venue) | Y (receivers) | — | Y | — | Y (лекционные залы) | venue pricing |
| **HearAura** | iOS/iPad/Watch/Vision | Y (venue feed или mic) | — | Meeting Mode | Y | — | Y («Catch me up») | — | — | **Auracast assistant** (join в aids) | **Y (QR, scan)** | Y (LE Audio/MFi) | Y (captions; channels — LAN) | Y | **«Catch me up» = summary, не replay** | Y (залы) | Free |
| **Phonak Roger** | Hardware | — | — | — | — | — | — | — | — | Roger 2.4 ГГц → receivers | — | Y (Roger) | — | Y | — | Y (класс) | hardware |

## Q1. «Не расслышал» — приоритет

`FACT` Продукта с точной функцией «показать последние N секунд дословного
транскрипта» **не найдено**. Ближайшие:
- Apple TV 4K: при откате на 10 с авто-субтитры (prerecorded).
- Roku: «On instant replay» для субтитров.
- Google Live Transcribe: кнопка Hold + scrollback до 3 дней.
- HearAura «Catch me up» — **summary** недавних captions, не дословный replay.
- Патент US20090076804 (Bionica, 2007): ALS-буфер с instant replay + STT.

`INFERENCE` Ниша «N-секундный дословный replay в live-каптионс» вероятно
свободна как **UX-функция**, но механика replay/rewind широко известна.

## Q2. Captions из чистого фида

`FACT` Есть: Android Live Caption (звук устройства), Apple Live Captions
(режим «iPhone Audio»), MS Teams (чистый микс), Bettear RTX (USB → native
audio для transcription), HearAura (venue feed), AppTek appliance
(«plug in your audio feed»), NHK STRL (direct method).

## Q3. Auracast + captions из одного источника

`FACT` Найден **один продукт**: **HearAura** (assistant + captions;
venue feed опционально). Публикаций о синхронизации captions с Auracast
аудио **нет**. Реальных развёртываний Auracast+captions — **не подтверждено**.

## Q4/Q5. WER

- Far-field хуже close-talk: DiPCo 77.5% vs 42.1%; AMI/Whisper 36.4% vs 16.9%.
- NPTEL лекции (чистый фид): медиана Whisper base.en ~11.7%, YouTube ~14.4%,
  worst ~35%.
- Modern clean read speech: Whisper 2.7%, Conformer 1.9–2.1% (LibriSpeech clean).
- `UNKNOWN` публичного прямого сравнения mixer-feed vs phone-mic в зале.

## Q6. Caption latency

- TV captions: **7–12 с**; ASR captions: ~**2 с** (ASSETS 2026, DHH-оценки).
- Streaming ASR: finalization 18.1 с → **1.1 с** (Nguyen 2020).
- On-device: 0.46 с latency @2.2% WER (WhisperKit 2025).
- `ENGINEERING DECISION` Для Route+ цель по caption latency: partial ≤1 с,
  final ≤3 с (TARGET, проверять экспериментально).

## Q7. Confidence display

`FACT` В продакшене **не найдено**; только исследовательские прототипы
(ConFides 2024; Nowrin & Vertanen 2025). Значит идея проекта
confidence-aware captions — на уровне research; prior art в патентах
проверять отдельно.

## Q8. Diarization

- DER: 13.6% (AMI, виртуальный массив), 17.11% (AMI semi-sup), 7.64%
  (multi-channel overlap).
- Ava/Otter/Teams — speaker labels; Group Transcribe — мульти-устройство.
- Classroom/lecture DER — UNKNOWN.

## Q9. Руководства

- `FACT` WCAG 2.2 SC 1.2.4 (live captions, AA) — включая «identify who is
  speaking».
- `FACT` ADA Title II rule: WCAG 2.1 AA для гос. вузов; сроки 26.04.2027
  (≥50k) / 26.04.2028.
- `FACT` FCC 47 CFR 79.1: accurate, synchronous, complete; educational
  programming exempt.
- `UNKNOWN` EN 301 549 (страница 404).

## Вывод для Route+

`ENGINEERING DECISION` MVP-функции проекта (live captions, timestamp, missed
speech, notes, bookmarks, a11y) **не уникальны по отдельности**; уникальность
может быть в **связке** clean-feed ASR + Auracast + missed speech в
образовательном контексте. «Catch me up»/summary и «Missed speech» —
разные функции, не путать.

## Источники

ava.me; support.google.com; otter.ai; microsoft.com/learn.microsoft.com;
support.apple.com; rylo.com; bettear.com; hearaura.app; phonak.com;
w3.org/WAI; ada.gov; ecfr.gov; arxiv.org/abs/2609.11408; 2507.10860;
2003.09891; 1905.02545; 1910.11416; 2209.12002; 2405.00223; 2410.20564;
semanticscholar (Gelbart & Morgan 2002); roi/developer.roku.com.
