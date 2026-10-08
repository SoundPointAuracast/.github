# LEGACY_AURACAST_CLAIMS

Аудит **всех** утверждений про Bluetooth / LE Audio / Auracast, извлечённых из
локальных исходников. Дата: 2026-09-26, GATE 1.

**Правило GATE 1: утверждения только фиксируются. Web-проверка (Bluetooth SIG
и др.) НЕ проводилась. `current_status` отражает лишь внутреннюю оценку риска.**

## Легенда

- **claim_type:** SOURCE_CLAIM | TARGET | ASSUMPTION | MARKETING | FUNCTIONAL
- **current_status:** UNVERIFIED | LIKELY_CORRECT | QUESTIONABLE |
  LIKELY_INCORRECT | OUTDATED | NEEDS_EXPERIMENT

## Таблица

| claim_id | source_id | slide | original_claim | claim_type | current_status | verification_needed | notes |
|---|---|---|---|---|---|---|---|
| C-AUR-001 | S002 | 6 | «Bluetooth LE Audio для трансляции аудиопотока на множество устройств одновременно с минимальным энергопотреблением» | SOURCE_CLAIM | UNVERIFIED | да | нет ссылки на спецификацию |
| C-AUR-002 | S002 | 6 | «AURACAST — …с низкой задержкой» | MARKETING | NEEDS_EXPERIMENT | да | число отсутствует |
| C-AUR-003 | S004 | 4 | «система… на основе стандарта Bluetooth LE Audio 5.2+» | SOURCE_CLAIM | LIKELY_INCORRECT | да | отождествление «BT 5.2 = Auracast» сомнительно |
| C-AUR-004 | S004 | 4 | «Работает БЕЗ интернета и сотовой связи» | FUNCTIONAL | LIKELY_CORRECT | да | broadcast локален, но зависит от сценария |
| C-AUR-005 | S004 | 4 | «транслирует… на неограниченное количество устройств-приёмников» | MARKETING | QUESTIONABLE | да | реальные ограничения пропускной способности |
| C-AUR-006 | S004 | 4,5 | «диаметр действия ~100 м»; «до 100 м» | TARGET | QUESTIONABLE | да | зависит от мощности/антенны/среды |
| C-AUR-007 | S004 | 4,13 | «Работает напрямую со слуховыми аппаратами, кохлеарными имплантами, наушниками, смартфонами…» | MARKETING | QUESTIONABLE | да | зависит от поддержки у конкретных устройств |
| C-AUR-008 | S004 | 5 | «Помещение… с индукционной петлёй… зона… 30–40 м²» | SOURCE_CLAIM | UNVERIFIED | да | классика индукционных петель |
| C-AUR-009 | S004 | 6 | «Bluetooth-сигнал проникает через металлоконструкции» | SOURCE_CLAIM | QUESTIONABLE | да | требует RF-обследования |
| C-AUR-010 | S004 | 4 | «Ретрансляторы AURACAST с индукторами (типовое решение)» | MARKETING | QUESTIONABLE | да | «типовое» не доказано |
| C-AUR-011 | S004 | 9 | «12–15 ретрансляторов; перекрытие 20–30%; шаг 70–80 м; RSSI/FER/MOS; ≥5 000/мес; ≥20 000/мес; покрытие 100%» | TARGET | UNVERIFIED | да | плановые KPI, не измерения |
| C-AUR-012 | S004 | 4,5 | «компенсирует отсутствие Bluetooth 5.2+ в старых версиях СА и КИ» | ASSUMPTION | QUESTIONABLE | да | смешивает версию BT и поддержку Auracast |
| C-AUR-013 | S004 | 3,12 | «приложение РЖД», RuStore/AppStore/Google Play | FUNCTIONAL | OUTDATED | нет | план, не реализовано |
| C-AUR-014 | S004 | 9,14 | «BIG/BIS», «ImmediateRendering», «BroadcastName» | SOURCE_CLAIM | UNVERIFIED | да | терминология требует сверки со спецификацией |
| C-AUR-015 | S006 | 4 | «Bluetooth LE Audio 5.2+; без интернета; неограниченное количество; ~100 м» | SOURCE_CLAIM | QUESTIONABLE | да | унаследовано из S004 |
| C-AUR-016 | S006 | 14 | «закладываем реалистичный показатель ≤300 мс» | TARGET | NEEDS_EXPERIMENT | да | см. LEGACY_LATENCY_CLAIMS |
| C-AUR-017 | S006 | 9 | «передача от 2 источников» | TARGET | UNVERIFIED | да | план НИОКР |
| C-AUR-018 | S004, S006 | 5 | «подключение по QR-коду» | FUNCTIONAL | UNVERIFIED | да | реализуемость |
| C-AUR-019 | S007 | схема | «зона покрытия определяется RF-обследованием площадки» | ENGINEERING | LIKELY_CORRECT | да | корректный подход |
| C-AUR-020 | S007 | схема | «LE Audio / LC3 • низкая задержка • параметры подтверждаются испытаниями» | TARGET | UNVERIFIED | да | аккуратная формулировка |
| C-AUR-021 | S007 | схема | Bridge-T: Auracast → LC3 → PCM → DAC → усилитель → индукционная катушка → T/MT | ASSUMPTION | NEEDS_EXPERIMENT | да | см. BRIDGE_T_EVOLUTION |
| C-AUR-022 | S007 | схема | «Интернет нужен только для AI-сервисов» | FUNCTIONAL | UNVERIFIED | да | зависит от архитектуры ASR |
| C-AUR-023 | S007 | схема | «индукционная зона / локальный контур для T/MT» | FUNCTIONAL | UNVERIFIED | да | размеры/совместимость |
| C-AUR-024 | S008 | p.1 | «совместим с устройствами Bluetooth 5.2 или выше» | SOURCE_CLAIM | LIKELY_INCORRECT | да | ИИ-заметка; смешивает BT-версию и Auracast |
| C-AUR-025 | S008 | p.1 | «многие устройства… можно сделать совместимыми… через обновления ПО» | SOURCE_CLAIM | QUESTIONABLE | да | ИИ-заметка, не проверено |
| C-AUR-026 | S008 | p.2-3 | список моделей наушников/передатчиков с Auracast | SOURCE_CLAIM | UNVERIFIED | да | данные 2024–2025, требуют перепроверки |
| C-AUR-027 | S008 | p.1 | «без необходимости традиционного сопряжения» | SOURCE_CLAIM | LIKELY_CORRECT | да | соответствует идее broadcast |
| C-AUR-028 | S009 | схема | «до ~100 м на узел» | TARGET | QUESTIONABLE | да | то же, что C-AUR-006 |
| C-AUR-029 | S009 | схема | «ASR + AI» (субтитры, ключевые события, AI-конспект) | FUNCTIONAL | UNVERIFIED | да | часть — перспектива |
| C-AUR-030 | S009 | схема | «Интеграция с существующей аудиоинфраструктурой (DSP, Dante)» | FUNCTIONAL | UNVERIFIED | да | требует проверки на оборудовании |
| C-AUR-031 | S009 | схема | «Не расслышал» — последние 10–15 секунд | TARGET | UNVERIFIED | да | зависит от буферизации |
| C-AUR-032 | S005 | 5 | «устройства улавливают звук через магнитное поле, что даёт более чистое звучание» | SOURCE_CLAIM | QUESTIONABLE | да | качественное утверждение |

## Сводка

- Всего утверждений: **32**.
- LIKELY_CORRECT: C-AUR-004, 019, 027.
- LIKELY_INCORRECT / QUESTIONABLE: C-AUR-003, 005, 006, 007, 009, 010, 012,
  015, 024, 025, 028, 032.
- NEEDS_EXPERIMENT: C-AUR-002, 016, 021.
- Все остальные — UNVERIFIED / OUTDATED / TARGET.

## Вывод GATE 1

Ни одно из ключевых утверждений (задержка, дальность, число слушателей,
«BT 5.2 = Auracast», прямая совместимость с СА/КИ) **не подтверждено**.
Проверка переносится на GATE 2 (режим MAX, Bluetooth SIG и др.).
