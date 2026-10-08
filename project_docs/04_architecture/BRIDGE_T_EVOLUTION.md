# BRIDGE_T_EVOLUTION

GATE 1 + GATE 2.7. Обновлено: 2026-09-26.

## Ответ после web-исследования

**Bridge-T — продолжение идеи старого индуктора + НОВАЯ архитектура входа.
Как класс продукта — НЕ уникален.**
См. `02_research/07_induction_telecoil/AURACAST_TELECOIL_PRIOR_ART.md`.

## Существующие аналоги (FACT)

- **Auri RX1 + neckloop** (Ampetronic/Listen) — Auracast → 3.5 мм/neckloop.
- **Infinium BA-R1** (Williams AV) — Auracast → 3.5 мм → neckloop.
- **AuraCoil** (Avantree) — Auracast-приёмник со **встроенным T-coil neckloop**
  (pre-order 30.11.2026).
- **Bettear RTX + neckloop**; **Univox NL-100**; **Humantechnik Teleschlinge**.
- Патент **WO 2026/071900 A1** «Personal induction loop» (Bluetooth neckloop).

## Схема эволюции

```
OLD DEVICE (S001): источник → печатный индуктор (FR4, ~5.1 мГн, 50 Гц–10 кГц)
                   → магнитное поле → катушка СА/КИ (T/MT)
        |
        | WHAT CHANGES
        v
+ цифровой вход: Auracast Broadcast Sink (PBP PBK + BAP Sink + BASS)
+ LC3 decode → PCM → DAC
+ усилитель, согласование с катушкой
+ автономность, QR
BRIDGE-T (S007): Auracast → LC3 → PCM → DAC → усилитель → катушка → T/MT
```

## Что действительно своё (кандидаты, без заявлений о новизне)

1. `HYPOTHESIS` Конкретная **геометрия/интеграция** катушки (плоская PCB-
   спираль vs wearable loop) и её согласование.
2. `HYPOTHESIS` Компактное автономное устройство, ориентированное на
   **процессор КИ**, а не только на СА (патентов/продуктов именно под это
   не найдено — но поиск неполный).
3. `HYPOTHESIS` Связка Bridge-T с **текстовым слоем** (один источник:
   аудио через Bridge-T + captions через Route+) — требует prior art GATE 7.

## Ограничения telecoil (влияют на продукт)

- Полоса telecoil уже микрофона; IEC 60118-4 гарантирует лишь 100 Гц–5 кГц.
- Направленность ≈6 дБ (axial vs radial); положение катушки важно.
- Гул/помехи (трансформаторы, освещение); существуют hum-filter патенты.
- Моно.
- Не все СА имеют telecoil; **новые RIC без T** (Phonak Infinio, Widex
  SmartRic/Allure) не являются целями Bridge-T.

## Категории

Все элементы Bridge-T — `CURRENT_CONCEPT` / `REQUIRES_EXPERIMENT`.
Новизна — `POTENTIAL_NOVELTY` только после GATE 7.

## Открыто

- Схемотехника, элементная база, нормы индукции/ЭМС.
- Совместимость с реальными моделями СА/КИ.
- Энергопотребление/автономность.
- Сертификация по IEC 60118-4 применима ли к персональному устройству.
