# PHONAK ROGER — карточка конкурента

Источники: web-исследование по официальным материалам Phonak/Sonova,
доступ 2026-09-26. Класс: **A. proprietary assistive listening**
(2.4 ГГц цифровая радиосистема).

## Сводка

| Поле | Значение |
|---|---|
| Производитель | Sonova / Phonak (Швейцария) |
| Тип | Проприетарный **2.4 ГГц цифровой** канал с адаптивной перестройкой частот |
| Задержка RF | **<20 мс** (официально); развивалось под end-to-end <25 мс |
| Дальность | мин. 15 м; отдельные микрофоны >100 м |
| Полоса аудио | 100 Гц – 7 кГц; адаптивное усиление до +20 дБ |
| Микрофоны | Roger On (v3), Roger Select (3), Roger Touchscreen Mic (3) — образовательный, Roger Table Mic II/3, Roger Clip-On; legacy Roger Pen/EasyPen |
| Приёмники | RogerDirect (внутри СА Phonak), Roger X (DAI), встроенные Roger-приёмники для КИ (Cochlear/MED-EL/AB), **Roger NeckLoop** (универсальный, T-coil) |
| Roger NeckLoop | универсальный индукционный neckloop-приёмник; T-coil любых СА/КИ; **USB Type-C audio interface**; выход на наушники; поле 1.25 A/m на 150 мм |
| Roger MyLink | **исторический** универсальный neckloop-приёмник (2.4 ГГц, 2013; Classic FM MyLink 2009); **без USB** (разъём 2.5 мм); снят с поддержки/EOL |
| Образование | Roger for Education: Touchscreen Mic, Pass-around, Multimedia Hub, DigiMaster 5000/7000 (до ~300 м²/300 слушателей), WallPilot (авто-подключение), Repeater; MultiTalker Network до 35 микрофонов |
| Внедрения | именованные школы/вузы в официальных источниках **не найдены** (UNKNOWN) |
| Статус | Roger — актуальная линейка; Roger NeckLoop — актуальный; Roger MyLink — legacy/EOL |

## Roger NeckLoop: USB audio → STT (CRITICAL PRIOR ART)

**Подтверждено официальной документацией Phonak.**

Точные формулировки (PRIMARY, доступ 2026-09-26):

1. **Installation guide «Roger NeckLoop for speech-to-text», V1.00/2021-04**:
   > «Roger NeckLoop can be connected to a computer, tablet or smartphone to
   > generate live, automated captions using 3rd party speech-to-text
   > software.»
   > «Now speak into the Roger microphone and the speech-to-text software or
   > MS Word will transcribe the spoken words into text.»
2. **Product FAQ (en-US)**: «The USB audio interface makes it possible to use
   a Roger microphone as input for e.g., **speech-to-text** or online meeting
   applications on a computer or smartphone that supports USB audio devices.»
3. **User Guide §4 «Using USB for audio» (модели 02/03, CE 2020)**:
   «Roger NeckLoop can be connected to a compatible computer or smart device
   with USB cable to listen to, or record audio transmitted from a Roger
   microphone.»
4. **Datasheet V1.10/2020-12**: «Features… Headphone output • **USB audio
   interface**»; «Compatibility: Any hearing aid or sound processor featuring
   a T-coil».
5. **Education brochure**: «Roger NeckLoop… compatible with any hearing aid or
   cochlear implant with T-coil. **Can also be used for speech-to-text.**»
6. **How-to video library**: видео «Using USB for audio» и «Using
   Speech-to-text».

### Архитектура prior art

```
преподаватель → Roger microphone → 2.4 ГГц Roger → Roger NeckLoop
   ├── индукция → T-coil СА/КИ (аудио)
   └── USB audio → компьютер/планшет → сторонний STT → live captions
```

**Дата prior art: апрель 2021** (STT-guide V1.00).

### Насколько это близко к clean-feed → Auracast + ASR → Route+

- **Совпадает**: один чистый микрофонный фид преподавателя используется и
  для персонального аудио (T-coil), и как **вход для STT**; есть
  документально подтверждённый сценарий live captions.
- **Отличается**:
  1. транспорт аудио — проприетарный 2.4 ГГц + индукция, а не Auracast;
  2. USB-фид привязан к **компьютеру**, не к серверной сессии; нет
     привязки к конкретной образовательной сессии/аудитории;
  3. нет общего timestamp-домена аудио и текста;
  4. нет функции «Не расслышал» и нет единого accessibility layer;
  5. нет синхронизированного распространения текста нескольким студентам
     через их устройства (текст остаётся на том компьютере, куда подключён
     NeckLoop).

**Вывод:** идея «clean-feed → STT» **не является новой**. N09 должен быть
пересмотрен (см. `09_novelty_rid/NOVELTY_MAP.md`).

## ROGER_STT_PRIOR_ART (сводно)

| Пункт | Статус |
|---|---|
| USB audio interface у Roger NeckLoop | ПОДТВЕРЖДЕНО |
| Официальный сценарий speech-to-text | ПОДТВЕРЖДЕНО (2021) |
| Использование Roger-микрофона как входа для STT | ПОДТВЕРЖДЕНО |
| Аудио на USB = речь с Roger-микрофона | ПОДТВЕРЖДЕНО (не room mix) |
| Живые captions через сторонний STT | ПОДТВЕРЖДЕНО (MS Word Dictate, Google Transcribe) |
| Задержка USB-пути | UNKNOWN |
| Привязка текста к сессии/студенту | НЕ подтверждено |
| «Не расслышал» | НЕ найдено |

## ROGER_MYLINK_STATUS

`FACT` Roger MyLink — **историческое решение**, не текущий конкурент:
- универсальный индукционный neckloop-приёмник (T-coil, любые бренды,
  включая ITE/micro-BTE);
- 2.4 ГГц (Roger) / FM (Classic MyLink, 2009);
- **без USB audio** (только 2.5 мм headphone и зарядный разъём);
- Phonak France phase-out notice (окт. 2025) перечисляет MyLink (03) среди
  уже завершённых по сервису; новые «Roger-приёмники (02) 14/18/19» —
  fin de commercialisation 31.12.2025;
- преемник по нише — **Roger NeckLoop** (2020/2021, + USB audio).

**Идеи MyLink как prior art для Bridge-T:** wireless receiver → neckloop →
T-coil (тот же класс, что и современные Auracast-решения).

## Образовательные сценарии Roger

- Touchscreen Mic — микрофон преподавателя, до неограниченного числа
  приёмников; режимы lanyard / Small Group / Pointing.
- MultiTalker Network — до 35 микрофонов.
- DigiMaster 5000/7000 — звуковое поле (до ~300 м²/300 слушателей).
- WallPilot — автоматическое подключение к нужной комнате.
- Roger Focus II — для детей с односторонней потерей слуха/APD/ASD.
- Vendor-исследование (Lejon & Smith, 2021): разборчивость 27% → 81% в
  шуме 60 дБ(A) с Roger против СА без Roger (vendor, n=14).

## Что Roger решает, чего Auracast сегодня не решает

- близкий к источнику захват речи с адаптивным +20 дБ;
- сеть многих микрофонов (до 35) и авто-подключение (WallPilot);
- широкая совместимость, включая legacy T-coil/DAI/КИ;
- не требует инфраструктуры площадки и телефона;
- продаётся и внедрён сегодня.

## Что Auracast решает, чего Roger не решает

- открытый стандарт, любой бренд;
- неограниченное число получателей от одного передатчика без приёмного
  оборудования;
- потребительские устройства (смартфоны, earbuds);
- дешевле и проще в развёртывании площадок.
(Оговорка Phonak: рынок/инфраструктура Auracast незрелые; ALS-стандарт
IEC 60118-17 ожидается не ранее 2027.)

## Источники (PRIMARY, доступ 2026-09-26)

- phonak.com/.../roger-neckloop (product page + FAQ)
- Installation guide «Roger NeckLoop for speech-to-text» V1.00/2021-04 (PDF)
- Roger NeckLoop User Guide (02/03); Datasheet V1.10/2020-12 (PDF)
- phonak.com/.../roger-receivers, /roger-for-education, /roger-on,
  /roger-touchscreen-mic, /roger-device-videos
- Phonak France phase-out notice, окт. 2025 (PDF)
- Roger MyLink User Guide 029-0265 и datasheets V3.00/2013, V2.00/2013
  (Wayback Machine, archived)
- Lejon & Smith 2021 (FSN), Roh et al. 2025 (FSN) — vendor field studies
