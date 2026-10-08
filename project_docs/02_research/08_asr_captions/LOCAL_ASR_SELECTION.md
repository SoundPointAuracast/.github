# LOCAL_ASR_SELECTION

GATE 6A. Дата: 2026-09-26. Web-исследование (доступ 2026-09-26).
**Модели НЕ скачивались и не запускались.**

## Требования к движку для E05

- русский язык;
- streaming + partial results;
- timestamps;
- CPU-friendly (GPU опционально);
- offline;
- permissive licence;
- Python.

## Сравнительная таблица

| Движок (версия/дата) | Русский WER (лучшие публичные) | Streaming/partials | Word timestamps | CPU | GPU/VRAM | Latency-модель | Install | Licence | Статус |
|---|---|---|---|---|---|---|---|---|---|
| **T-one** 71.7M (repo 2025-12) | CV19 5.32; call-center 8.63; Farfield 12.2 (GigaAM table: avg 16.3) | **ДА** (300 мс chunks, `new_phrases`) | заявлены word-level; pipeline даёт phrase-level (проверить) | demo 4 ядра/8 ГБ | TensorRT/T4/A100 | 300 мс + phrase splitter | Docker/Poetry; KenLM | Apache-2.0 | active |
| **GigaAM v3** RNNT (2025-11) | avg 8.3 по 10 наборам; Golos Crowd 2.4; Farfield 3.9; RuLS 4.4 | НЕТ (≤25 с вызов; longform через VAD) | да (с 2026-04, short clips) | PyTorch/ONNX; RTF не опубликован | CUDA/ONNX/TensorRT | окна 25 с | repo / HF (trust_remote_code); HF-token для longform | MIT | very active |
| **faster-whisper** 1.2.1 | как Whisper (avg 21.0; Farfield 16.6) | нет native; community-обёртки | да | **хорошо**: small int8 RTF ≈0.13 | CUDA 12, large fp16 ~4.5 ГБ | batch / обёртки ~секунды | pip | MIT | active |
| **Vosk** 0.3.45/0.3.50 | small 45 МБ: Golos Crowd 11.79; big 1.8 ГБ: 4.4; calls 36.0 | **ДА** (true streaming) | да (`SetWords`) | очень лёгкий, ~300 МБ RAM (small) | нет | chunk-based | pip | Apache-2.0 (ru) | wheels stale (2022) |
| **openai-whisper** 20250625 | как above | нет | экспериментально | медленнее f-w 2–4× | CUDA ~10 ГБ (large) | 30-с окна | pip + ffmpeg | MIT | active |
| **whisper.cpp** v1.9.4 | нет ru-оценки | naive stream | экспериментально | очень хороший (tiny 273 МБ) | CUDA/Vulkan/Metal | 0.5 с шаг/5 с окно | C++ build | MIT | active |
| **NeMo ru** (2023-04) | MCV10 4.0; Farfield 7.6 | не документировано | не документировано | н/д | CUDA | batch | nemo_toolkit (тяжёлый) | CC-BY-4.0 | stale |
| **Whisper ru fine-tune** podlodka-turbo | CV11 5.22; Farfield 11.61; long-form 7.84 | нет | chunk-level | 809M (тяжёл) | ~6 ГБ | 30-с окна | HF pipeline | Apache-2.0 | maintained |
| **Silero** | русский **STT отсутствует** (только TTS/VAD) | — | — | — | — | — | — | — | — |

## RECOMMENDED FOR EXPERIMENT

**Основной streaming-движок: T-one** (Apache-2.0, 71.7M, 300 мс чанки,
partial results, offline, CPU-sized) — единственный, кто одновременно
закрывает русский + streaming + partials + timestamps.
**Batch-reference: GigaAM-v3 RNNT** (MIT, 449 МБ) — точный эталон для
подсчёта WER.

## ALTERNATIVE

1. **faster-whisper small/large-v3** (MIT) + VAD/обёртка — если важнее
   word-level timestamps и простота установки, чем истинные partials.
2. **Vosk** (small-ru-0.22, 45 МБ) — если жёсткие ограничения по CPU/памяти.
3. **GigaAM-v3** для всего, кроме partials (если ослабить требование
   streaming).

## NOT RECOMMENDED

- **openai-whisper** (та же точность, что faster-whisper, но медленнее).
- **whisper.cpp** (нет официального Python-пакета и настоящего streaming).
- **NeMo ru** (карточки 2023, тяжёлая установка, нет streaming/timestamps).
- **Silero** (русского STT нет).
- Whisper tiny/base для телефонного рукава (резкая деградация в дальнем
  поле/шуме).

## Минимальная конфигурация (без загрузки сейчас)

- 8-ядерный x86, ≥8 ГБ RAM (T-one demo baseline 4 ядра/8 ГБ).
- Python 3.10–3.12.
- Установить: `pip install faster-whisper` (fallback), репозиторий T-one
  (или Docker `tinkoffcreditsystems/t-one:0.1.0`), репозиторий GigaAM.
- **Загрузка весов — отдельным решением пользователя** (не на этом этапе):
  T-one ~287 МБ fp32; GigaAM-v3 RNNT 449 МБ.

## UNKNOWN

- Точность word timestamps T-one (card vs pipeline).
- CPU RTF T-one и GigaAM.
- Vosk 0.54 ru-модели (65M/20M) — вне страницы моделей Vosk.

## Источники (PRIMARY)

github.com/voicekit-team/T-one; huggingface.co/t-tech/T-one;
github.com/salute-developers/GigaAM; huggingface.co/ai-sage/GigaAM-v3;
github.com/SYSTRAN/faster-whisper; alphacephei.com/vosk/models;
github.com/openai/whisper; github.com/ggml-org/whisper.cpp;
NGC NeMo ru model cards; huggingface.co/bond005/whisper-podlodka-turbo.
