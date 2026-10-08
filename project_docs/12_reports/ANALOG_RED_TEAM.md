# ANALOG_RED_TEAM

GATE 6A. Дата: 2026-09-26.

Вопрос: «Если эксперт Phonak, Исток-Аудио, Auri или Bettear посмотрит
презентацию, какое утверждение он первым назовёт неправдой?»

Ниже — 14 потенциальных возражений (claim → objection → evidence →
correction → safe wording).

---

### AR-01 — «Clean-feed → speech-to-text — наша идея»
- **Возражение:** «Это делается с 2021 года: Roger NeckLoop отдаёт аудио
  Roger-микрофона по USB в сторонний STT».
- **Evidence:** Phonak Installation guide «Roger NeckLoop for speech-to-text»
  V1.00/2021-04: «generate live, automated captions using 3rd party
  speech-to-text software».
- **Correction:** идея **NOT_NEW**. N02 понижен.
- **Safe wording:** «Мы используем известный принцип clean-feed
  распознавания и исследуем его в связке с сессионной привязкой и
  синхронизацией аудио/текста».

### AR-02 — «Bridge-T уникален»
- **Возражение:** «Wireless receiver → neckloop → T-coil продаётся с 2009
  года (Phonak MyLink), сейчас — Roger NeckLoop. Плюс Auri RX1, Bettear RTX,
  Avantree AuraCoil».
- **Evidence:** MyLink User Guide 029-0265; Roger NeckLoop datasheet;
  Auri RX1; AuraCoil (pre-order).
- **Correction:** Bridge-T — **KNOWN_CLASS**.
- **Safe wording:** «Bridge-T — реализация известного класса; мы исследуем
  конкретную геометрию/форм-фактор/интеграцию, а не класс».

### AR-03 — «Auracast автоматически лучше FM/Roger»
- **Возражение:** «Auracast не standardized для ALS: IEC 60118-17 ожидается
  не ранее 2027; парк совместимых СА/КИ мал; CI почти нет. Roger даёт
  +SNR и сеть микрофонов сегодня».
- **Evidence:** Phonak: «Very few hearing devices currently support
  Auracast…»; Bluetooth SIG location profiles; device matrix.
- **Correction:** не сравнивать «лучше/хуже»; разные свойства.
- **Safe wording:** «Auracast — открытый и массовый путь; FM/Roger зрелее по
  совместимости и SNR сегодня. Мы исследуем их сочетание, а не замену».

### AR-04 — «Auracast = Bluetooth 5.2»
- **Возражение:** «Нужны PBP, LE Audio stack и квалификация, а не просто
  5.2».
- **Evidence:** Bluetooth SIG «Communicating supported functionality»
  (14.01.2025); PBP §2.5.
- **Correction:** формулировка REJECTED.
- **Safe wording:** «Auracast — возможность LE Audio, определяемая PBP;
  требуется Core 5.2+ **и** профили, а не только версия ядра».

### AR-05 — «100 метров и неограниченное число слушателей»
- **Возражение:** «Это vendor-оценка SIG для питаемого передатчика; нет
  нормативного числа; приёмники имеют конечные ресурсы».
- **Evidence:** SIG CES handout «Range»; BAP/BASS.
- **Correction:** не переносить как гарантию.
- **Safe wording:** «Дальность и ёмкость определяются RF-обследованием и
  конкретными приёмниками».

### AR-06 — «Задержка ≤300 мс достаточна»
- **Возражение:** «При смешении с живым голосом 300 мс — это эхо; Roger
  работает <20 мс, а мы заявляем 300».
- **Evidence:** ITU-R BT.1359; Stone & Moore; Roger datasheet.
- **Correction:** 300 мс REJECTED как цель для живого зала.
- **Safe wording:** цель ≤60 мс, допустимо ≤100 мс (TARGET).

### AR-07 — «Приложение подключит к Auracast»
- **Возражение:** «Стороннее приложение не имеет доступа к BASS/Assistant
  на Android (SystemApi + BLUETOOTH_PRIVILEGED); iOS не поддерживает».
- **Evidence:** AOSP API 33–36; Zephyr BASS UUID warning.
- **Correction:** приложение не реализует Auracast.
- **Safe wording:** «Подключение выполняется средствами совместимого
  устройства; приложение — текстовый слой».

### AR-08 — «Мы соединили звук и текст — это новое»
- **Возражение:** «Bettear уже даёт venue captions + Auracast; HearAura —
  assistant + captions; Roger + STT — с 2021».
- **Evidence:** как выше.
- **Correction:** N09 понижен до INSUFFICIENT_EVIDENCE.
- **Safe wording:** «Отдельные блоки известны; мы проверяем системный
  эффект общего timestamp-domain и сессионной привязки».

### AR-09 — «Missed Speech — уникальная функция»
- **Возражение:** «US20090076804 (Bionica, 2007) — ALS-буфер с instant
  replay и STT; Apple TV/Roku делают replay субтитров».
- **Evidence:** Google Patents; Apple/Roku docs.
- **Correction:** N04 — DIFFERENTIATION_ONLY.
- **Safe wording:** «Дословный N-секундный фрагмент live-транскрипта —
  UX-дифференциатор; патентоспособность не установлена».

### AR-10 — «ASR на чистом фиде точнее — это факт»
- **Возражение:** «Нет прямых измерений „AV-фид vs телефон“ в реальной
  аудитории; современные массивы и DSP телефонов сокращают разрыв».
- **Evidence:** DiPCo/AMI дают направление, но не этот контраст;
  CLEAN_FEED_ASR_RESEARCH.
- **Correction:** H1 — гипотеза, не факт.
- **Safe wording:** «Мы планируем измерить разницу (E05)».

### AR-11 — «СОНЕТ устарел»
- **Возражение:** «СОНЕТ 2.0 активно продаётся (2026), есть свежие
  поставки и испытания; продукт решает свою задачу».
- **Evidence:** официальный каталог; статьи 2024–2025; dealer pricing.
- **Correction:** не называть устаревшим.
- **Safe wording:** «СОНЕТ 2.0 — зрелое решение аудио-половины задачи;
  проект исследует текстовый слой и открытый транспорт».

### AR-12 — «Roger устарел / проприетарный значит плохой»
- **Возражение:** «Roger — актуальная линейка с RogerDirect, CI-приёмниками
  и <20 мс; проприетарность даёт SNR-контроль и сеть микрофонов».
- **Evidence:** Roger portfolio 2026; vendor studies.
- **Correction:** не оценивать негативно.
- **Safe wording:** «Roger — референс по управляемому SNR и задержке;
  мы исследуем открытую альтернативу с текстовым слоем».

### AR-13 — «Патент: у нас есть новизна»
- **Возражение:** «Поиск неполный (Google Patents 503, Espacenet/USPTO
  недоступны, 18-мес. лаг); заявлений делать нельзя».
- **Evidence:** RED TEAM RT-07; PRIOR_ART.
- **Correction:** никаких патентных заявлений до GATE 7.
- **Safe wording:** «Потенциальные отличия требуют профессионального
  поиска».

### AR-14 — «Мы работаем без интернета — значит текст тоже»
- **Возражение:** «Captions зависят от STT; on-device ASR не проверен;
  Roger STT зависит от компьютера».
- **Evidence:** DATA_PIPELINE; LOCAL_ASR_SELECTION.
- **Correction:** разделять «аудио локально» и «текст зависит от тракта».
- **Safe wording:** «Аудио локально; работа текста — предмет
  исследования (on-device/локальный сервер)».

---

## Сводка

| # | Тема | Статус после red team |
|---|---|---|
| AR-01 | clean-feed STT | NOT_NEW |
| AR-02 | Bridge-T | KNOWN_CLASS |
| AR-03 | Auracast vs Roger | не сравнивать оценочно |
| AR-04 | BT 5.2 | REJECTED |
| AR-05 | 100 м / unlimited | не гарантия |
| AR-06 | 300 мс | REJECTED |
| AR-07 | App + Auracast | невозможно публично |
| AR-08 | audio+text новизна | INSUFFICIENT_EVIDENCE |
| AR-09 | Missed Speech | DIFFERENTIATION_ONLY |
| AR-10 | clean-feed точнее | HYPOTHESIS |
| AR-11 | СОНЕТ | зрелое решение |
| AR-12 | Roger | референс |
| AR-13 | патентная новизна | нет заявлений |
| AR-14 | offline text | research |

## Что эксперт, вероятнее всего, назовёт первым

**AR-01/AR-08:** «clean-feed → STT уже продаётся у Phonak с 2021».
Это главный риск позиционирования; ответ — переход к системным отличиям
(общий timestamp-domain, сессия, missed speech) и честное признание
известности блоков.
