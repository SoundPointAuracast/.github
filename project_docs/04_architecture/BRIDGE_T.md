# BRIDGE_T

Статус: DRAFT / HYPOTHESIS.

## Назначение

Переходное устройство для пользователей, чьи слуховые аппараты или
процессоры КИ не поддерживают Auracast напрямую.

## Предварительная архитектура (не считать уникальной)

```
Auracast Broadcast Sink
   -> LC3 decode
   -> PCM
   -> DAC / audio codec
   -> amplifier
   -> induction coil
   -> T / MT mode
   -> hearing aid / cochlear implant
```

## Обязательные проверки

- Анализ аналогов (существующие telecoil/loop продукты).
- Патентный prior art.
- Совместимость с реальными HA / CI (проверять, не обещать).
- Уровни поля и нормы безопасности.

## Категория новизны

**Не уникально** до результатов поиска. См. `09_novelty_rid/RISKS.md`.

## Где исследовать

`02_research/07_induction_telecoil/`, `02_research/10_patents_prior_art/`,
`05_hardware/bridge_t/`.
