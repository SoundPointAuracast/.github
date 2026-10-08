# ARTICLE_SOURCE_MAP

GATE 6B-2. Дата: 2026-09-26.

## Решения по статье

| Вопрос | Решение | Обоснование |
|---|---|---|
| Название | **«Разработка локальной ассистивной аудиосистемы с синхронизированным текстовым сопровождением для образовательных пространств»** | рекомендуемый вариант задания; официального требования сохранить прежнее название проекта не найдено (шаблон отсутствует). Альтернативное (исходное) название: «Разработка локального аудиоретранслятора для персональной беспроводной передачи речи в общественных и образовательных пространствах» |
| Автор | Никитин Даниил Константинович (AUTHOR_COUNT = 1) | `AUTHORSHIP_POLICY.md` |
| Affiliation | МГТУ им. Н.Э. Баумана, Москва | подтверждено проектными материалами (S001/S002 — учебная группа автора; SUPERVISOR_BRIEF — «МГТУ им. Н. Э. Баумана»). Кафедра не указана: для текущего периода не подтверждена однозначно |
| Формат | FALLBACK (A4, TNR 12, 1.0, поля 20 мм) | официальный шаблон не найден — `ARTICLE_FORMAT_REQUIREMENTS.md` |

## Таблица прослеживаемости утверждений

| CLAIM | SECTION | SOURCE | P/S | VERIFIED | SAFE WORDING |
|---|---|---|---|---|---|
| Разборчивость речи в классе страдает от шума/реверберации; +15 дБ SNR недостаточно для младших школьников | 1 | Bradley & Sato, JASA 2008, DOI 10.1121/1.2839285 | PRIMARY (peer-reviewed) | да (PMID/DOI) | «исследования показывают…» |
| СОНЕТ 2.0 — FM/UHF-радиокласс, приёмник с индукционным выходом, T/TM, групповое использование | 2 | istok-audio.com (официальный каталог) | PRIMARY (vendor official) | да, 26.09.2026 | «применяется», «поддерживает» |
| Roger — проприетарный 2.4 ГГц удалённый микрофон, ресиверы, включая КИ | 2 | phonak.com (official) | PRIMARY (vendor official) | да, 26.09.2026 | «реализуют передачу…» |
| Roger NeckLoop: T-coil + USB audio interface; микрофон Roger как вход для STT (2021) | 2, 5 | Phonak STT installation guide V1.00/2021-04; product FAQ | PRIMARY (vendor official) | да, 26.09.2026 | «официальная инструкция описывает…» |
| Auracast — возможность LE Audio, профили PBP/BAP/BASS; без интернета; телефон не в аудиотракте | 2, 3 | Bluetooth SIG: PBP 1.0.1, BAP 1.0.1, BASS 1.0 | PRIMARY (spec) | да, 26.09.2026 | «стандарт определяет…» |
| Обязательные конфигурации 16/24 кГц; 24_2_1 — инженерный baseline | 3, 4 | Bluetooth SIG BAP Table 6.4; PBP §4.2 | PRIMARY (spec) | да | «инженерный baseline, подлежащий проверке» |
| Presentation delay 40 мс — обязателен к поддержке | 4 | Bluetooth SIG BAP/PBP | PRIMARY (spec) | да | «приёмник обязан поддерживать» |
| Стороннее приложение не управляет Auracast-подключением (ограничения ОС) | 3 | Android Developers Bluetooth LE Audio docs; AOSP SystemApi | PRIMARY (official docs) | да, 26.09.2026 | «ограничение операционных систем» |
| Класс Auracast→индукция существует: Roger MyLink/NeckLoop, Auri RX1, Bettear RTX, AuraCoil | 3 | project prior-art (PHONAK_ROGER.md, AURACAST_TELECOIL_PRIOR_ART.md) | PRIMARY (vendor docs) | да | «класс известен; новизна не заявляется» |
| Реальные внедрения Auracast в вузах: UQ (65 аудиторий), Oxford, UAL | 2 | news.uq.edu.au; auriaudio.com/listentech.com; bluetooth.com profiles | PRIMARY + SECONDARY | UQ — PRIMARY; Oxford — vendor+press | «подтверждено для UQ; Oxford — по данным вендора» |
| Route+ MVP: captions partial/final, timestamps, «Не расслышал» (15 с), notes, bookmarks, a11y, demo | 4 | 06_application (исходники и тесты) | PRIMARY (реализация) | да (тесты 19+4, сборка) | «реализовано в программном прототипе» |
| ASR в демо — MockASRProvider; реальный ASR — следующий этап | 4 | 06_application/README.md; LOCAL_ASR_SELECTION.md | PRIMARY (код/док) | да | «в демонстрационной конфигурации…» |
| Эксперименты E01/E03/E04/E05/E07; метрики WER/CER/latency | 4 | EXPERIMENT_READINESS_GATE6.md; ASR_COMPARISON_PROTOCOL.md | PRIMARY (проект) | да | «разработана программа проверки» |
| Latency ≤60/≤100 мс | 4 | LATENCY_DEEP_DIVE.md | проект | — | «TARGET, не измерено» |

## Что НЕ используется и почему

| Утверждение | Причина отказа |
|---|---|
| Численность аудитории (12/13/15/19,5 млн) | источники противоречивы, первоисточник не проверен |
| «~100 м», «неограниченное число слушателей» | vendor-оценки, не норматив |
| «≤300 мс» | отклонено как цель для живого зала |
| «Bluetooth 5.2 = Auracast» | неверно (нужны PBP/стек/квалификация) |
| «clean-feed — новизна проекта» | Roger NeckLoop USB→STT, 2021 |
| «Bridge-T уникален» | класс продуктов существует |
| Любые результаты экспериментов | не проведены |

## Источники статьи (финальный список, 7)

Нумерация соответствует финальному DOCX.

1. Bluetooth SIG. Public Broadcast Profile 1.0.1.
2. Bluetooth SIG. Basic Audio Profile 1.0.1.
3. Phonak. Roger NeckLoop: USB audio and speech-to-text (официальная страница
   и инструкция STT V1.00/2021-04).
4. Исток-Аудио. Радиокласс «СОНЕТ 2.0».
5. Android Developers. Bluetooth LE Audio (ограничение API мобильной ОС).
6. Bradley J. S., Sato H. The intelligibility of speech in elementary school
   classrooms // JASA. 2008. Vol. 123, № 4. P. 2078–2086. DOI: 10.1121/1.2839285.
7. University of Queensland. UQ creates change for accessibility students. 2026.

Примечания:
- BASS (Broadcast Audio Scan Service) исключён из финального списка:
  в сокращённом тексте на него нет внутритекстовой ссылки. Источник
  остаётся в исследовательской базе проекта (AURACAST_TECHNICAL_MAP.md).
- Полная PDF-инструкция Phonak STT (V1.00/2021-04) использована при
  верификации утверждения; в статье дан укороченный URL официальной
  страницы продукта для соблюдения лимита 2 страниц.
- Все источники реально открывались при исследовании (GATE 2, 6A).
  Фальшивые DOI/URL/годы не используются.

## Соответствие внутритекстовых ссылок

| Ссылка | Утверждение |
|---|---|
| [1, 2] | Auracast/LE Audio, обязательные конфигурации, presentation delay |
| [3] | Roger NeckLoop USB→STT (2021) |
| [4] | СОНЕТ 2.0 |
| [5] | ограничение мобильных ОС для управления Auracast |
| [6] | акустика класса, +15 дБ SNR |
| [7] | внедрения Auracast в вузах (UQ и др.) |
