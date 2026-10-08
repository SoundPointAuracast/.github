# AUDIO_PIPELINE

Статус: DRAFT / HYPOTHESIS.

## Поток

```
mic / mixer
   -> gain / processing
   -> ADC (при аналоговом источнике)
   -> LC3 encode
   -> BLE Audio Broadcast (Auracast, BIS/BIG)
   -> radio
   -> receiver (LC3 decode)
   -> [direct to hearing device]
      или
      -> Bridge-T: LC3 decode -> PCM -> DAC -> amp
      -> induction coil -> T/MT -> HA/CI
```

## Вопросы

- Требуется ли и где обработка (AEC, NS, AGC)?
- Один ли поток LC3 одновременно для аудио и ASR, или ASR берёт
  PCM до кодирования LC3?
- Какая сквозная задержка достижима? (TARGET без числа.)

## Категории

- LC3 = стандарт кодека (FACT, при ссылке на спецификацию).
- Auracast = бренд LE Audio Broadcast (SOURCE, проверить формулировку).
- Реальная задержка/дальность — TARGET до измерений.
