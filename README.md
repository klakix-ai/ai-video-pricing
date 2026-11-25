# AI Video Pricing

An open dataset of public list prices for AI video generation models, normalized to **USD per second of output video** so they can finally be compared side by side.

Providers publish video prices in different units: tokens (Seedance on BytePlus), credits (Runway, Luma), per-clip bundles (Hailuo, Luma), per-"count" (Vertex), or plain dollars per second. Resolution tiers, audio toggles and promotions make it worse. This repo converts every row to the same unit, keeps the raw published text next to the result, and records the formula used.

- Data: [`data/prices.json`](data/prices.json) (source of truth), [`data/prices.csv`](data/prices.csv) (generated), [`data/schema.json`](data/schema.json)
- Scripts: [`scripts/build.py`](scripts/build.py), [`scripts/validate.py`](scripts/validate.py) (Python 3.8+, standard library only)
- Prices checked: 2026-11-26. Each row carries its own source URL and check date.

## The data

Each row is one model x provider x resolution x audio combination, with the fields `usd_per_second`, `usd_per_5s` and `usd_per_10s`, the raw `list_price` text, an `assumptions` note, a `source_url`, a `checked_at` date and a `confidence` level. Providers covered: official vendor APIs (BytePlus ModelArk, Google Vertex AI, Gemini API, OpenAI, Runway, MiniMax, Alibaba Cloud Model Studio, Luma, Kling, Pika, Higgsfield) and the two big model marketplaces, fal.ai and Replicate.

Rows are grouped by model family below and sorted from cheapest to most expensive per second. Open a family to see its rows.

<!-- TABLE:START -->
332 rows, 12 model families, 13 providers. Last checked 2026-11-26.

| Model family | Rows | Cheapest (USD/s) | Most expensive (USD/s) |
|---|---:|---|---|
| Gemini Omni | 13 | $0.023 (Gemini Omni 1.2 Flash, Gemini API, 360p) | $0.310 (Gemini Omni 1.2 Flash, Replicate, 4k) |
| Kling | 50 | $0.042 (Kling 2.5 Turbo Standard, fal.ai, unspecified) | $0.549 (Kling 4.0, fal.ai, 4k) |
| LTX | 12 | $0.060 (LTX 2.3 Fast, fal.ai, 1080p) | $0.320 (LTX 2.3 Pro, fal.ai, 4k) |
| Luma Ray | 17 | $0.012 (Luma Ray 3.2, Luma API, 360p) | $0.400 (Luma Ray 3.2, fal.ai, 1080p) |
| MiniMax Hailuo | 42 | $0.0125 (MiniMax H3 Lite, Replicate, 480p) | $0.160 (MiniMax H3 Max, fal.ai, 1080p) |
| PixVerse | 14 | $0.035 (PixVerse V6, fal.ai, 540p) | $0.252 (PixVerse V6 Max, fal.ai, 1080p) |
| Runway | 4 | $0.050 (Runway Gen-4 Turbo, Runway API, unspecified) | $0.280 (Runway Aleph 2.0, Runway API, unspecified) |
| Seedance | 71 | $0.010 (Seedance 1.0 Pro Fast, BytePlus ModelArk, 480p) | $1.84 (Seedance 2.5 (US region endpoint), fal.ai, 4k) |
| Sora | 4 | $0.100 (Sora 2, OpenAI API, 720p) | $0.700 (Sora 2 Pro, OpenAI API, 1080p) |
| Veo | 40 | $0.030 (Veo 3.1 Lite, Google Cloud Vertex AI, 720p) | $0.600 (Veo 3.1, fal.ai, 4k) |
| Vidu | 14 | $0.035 (Vidu Q3 Turbo, fal.ai, 540p) | $0.390 (Vidu Q4, fal.ai, 4k) |
| Wan | 51 | $0.015 (Wan 2.2 image-to-video Flash (wan2.2-i2v-flash), Alibaba Cloud Model Studio, 480p) | $0.280 (Wan 3.0 Prime, fal.ai, 1080p) |

<details>
<summary><b>Gemini Omni</b> (13 rows, sorted by USD/s)</summary>

| Model | Provider | Res | Audio | USD/s | USD/5s | USD/10s | Conf | Source | Notes |
|---|---|---|---|---:|---:|---:|---|---|---|
| Gemini Omni 1.2 Flash | Gemini API | 360p | n/a | $0.023 | $0.115 | $0.230 | high | [link](https://ai.google.dev/gemini-api/docs/pricing) |  |
| Gemini Omni Flash 1.2 | fal.ai | 360p | n/a | $0.0273 | $0.1365 | $0.273 | high | [link](https://fal.ai/models/google/gemini-omni-flash/v1.2/text-to-video) |  |
| Gemini Omni 1.2 Flash | Replicate | 360p | n/a | $0.035 | $0.175 | $0.350 | high | [link](https://replicate.com/google/gemini-omni-1.2-flash) |  |
| Gemini Omni 1.2 Flash | Gemini API | 720p | n/a | $0.070 | $0.350 | $0.700 | high | [link](https://ai.google.dev/gemini-api/docs/pricing) |  |
| Gemini Omni Flash 1.2 | fal.ai | 720p | n/a | $0.0819 | $0.4095 | $0.819 | high | [link](https://fal.ai/models/google/gemini-omni-flash/v1.2/text-to-video) |  |
| Gemini Omni 1.1 Flash | Gemini API | 720p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://ai.google.dev/gemini-api/docs/pricing) |  |
| Gemini Omni 1.2 Flash | Gemini API | 1080p | n/a | $0.104 | $0.520 | $1.04 | high | [link](https://ai.google.dev/gemini-api/docs/pricing) |  |
| Gemini Omni 1.2 Flash | Replicate | 720p | n/a | $0.105 | $0.525 | $1.05 | high | [link](https://replicate.com/google/gemini-omni-1.2-flash) |  |
| Gemini Omni Flash 1.2 | fal.ai | 1080p | n/a | $0.1229 | $0.6145 | $1.23 | high | [link](https://fal.ai/models/google/gemini-omni-flash/v1.2/text-to-video) |  |
| Gemini Omni 1.2 Flash | Replicate | 1080p | n/a | $0.155 | $0.775 | $1.55 | high | [link](https://replicate.com/google/gemini-omni-1.2-flash) |  |
| Gemini Omni 1.2 Flash | Gemini API | 4k | n/a | $0.209 | $1.04 | $2.09 | high | [link](https://ai.google.dev/gemini-api/docs/pricing) |  |
| Gemini Omni Flash 1.2 | fal.ai | 4k | n/a | $0.2457 | $1.23 | $2.46 | high | [link](https://fal.ai/models/google/gemini-omni-flash/v1.2/text-to-video) |  |
| Gemini Omni 1.2 Flash | Replicate | 4k | n/a | $0.310 | $1.55 | $3.10 | high | [link](https://replicate.com/google/gemini-omni-1.2-flash) |  |

</details>

<details>
<summary><b>Kling</b> (50 rows, sorted by USD/s)</summary>

| Model | Provider | Res | Audio | USD/s | USD/5s | USD/10s | Conf | Source | Notes |
|---|---|---|---|---:|---:|---:|---|---|---|
| Kling 2.5 Turbo Standard | fal.ai | unspecified | n/a | $0.042 | $0.210 | $0.420 | high | [link](https://fal.ai/models/fal-ai/kling-video/v2.5-turbo/standard/image-to-video) |  |
| Kling 2.5 Turbo Pro | Replicate | unspecified | n/a | $0.070 | $0.350 | $0.700 | high | [link](https://replicate.com/kwaivgi/kling-v2.5-turbo-pro) |  |
| Kling 2.5 Turbo Pro | fal.ai | unspecified | n/a | $0.070 | $0.350 | $0.700 | high | [link](https://fal.ai/models/fal-ai/kling-video/v2.5-turbo/pro/text-to-video) |  |
| Kling 2.6 | Replicate | unspecified | no | $0.070 | $0.350 | $0.700 | high | [link](https://replicate.com/kwaivgi/kling-v2.6) |  |
| Kling 2.6 Pro | fal.ai | unspecified | no | $0.070 | $0.350 | $0.700 | high | [link](https://fal.ai/models/fal-ai/kling-video/v2.6/pro/text-to-video) |  |
| Kling 3.0 | Kling AI API | 720p | no | $0.084 | $0.420 | $0.840 | high | [link](https://kling.ai/dev/pricing) |  |
| Kling 3.0 Omni | Kling AI API | 720p | no | $0.084 | $0.420 | $0.840 | high | [link](https://kling.ai/dev/pricing) |  |
| Kling 3.0 Standard | fal.ai | 720p | no | $0.084 | $0.420 | $0.840 | medium | [link](https://fal.ai/models/fal-ai/kling-video/v3/standard/text-to-video) |  |
| Kling O3 Standard | fal.ai | 720p | no | $0.084 | $0.420 | $0.840 | medium | [link](https://fal.ai/models/fal-ai/kling-video/o3/standard/text-to-video) |  |
| Kling 4.0 Flash | Replicate | 720p | n/a | $0.094 | $0.470 | $0.940 | high | [link](https://replicate.com/kwaivgi/kling-v4-flash) |  |
| Kling 4.0 Flash | fal.ai | 720p | n/a | $0.094 | $0.470 | $0.940 | high | [link](https://fal.ai/models/kling/v4/flash/text-to-video) |  |
| Kling 4.0 Flash (hosted by Runway) | Runway API | 720p | yes | $0.094 | $0.470 | $0.940 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Kling 3.0 Turbo | Higgsfield API | 1080p | n/a | $0.105 | $0.525 | $1.05 | low | [link](https://open.higgsfield.ai/pricing) |  |
| Kling 3.0 | Kling AI API | 1080p | no | $0.112 | $0.560 | $1.12 | high | [link](https://kling.ai/dev/pricing) |  |
| Kling 3.0 Omni | Kling AI API | 720p | yes | $0.112 | $0.560 | $1.12 | high | [link](https://kling.ai/dev/pricing) |  |
| Kling 3.0 Omni | Kling AI API | 1080p | no | $0.112 | $0.560 | $1.12 | high | [link](https://kling.ai/dev/pricing) |  |
| Kling 3.0 Pro | fal.ai | 1080p | no | $0.112 | $0.560 | $1.12 | medium | [link](https://fal.ai/models/fal-ai/kling-video/v3/pro/text-to-video) |  |
| Kling 3.0 Turbo | Kling AI API | 720p | yes | $0.112 | $0.560 | $1.12 | high | [link](https://kling.ai/dev/pricing) |  |
| Kling O3 Pro | fal.ai | 1080p | no | $0.112 | $0.560 | $1.12 | medium | [link](https://fal.ai/models/fal-ai/kling-video/o3/pro/text-to-video) |  |
| Kling O3 Standard | fal.ai | 720p | yes | $0.112 | $0.560 | $1.12 | medium | [link](https://fal.ai/models/fal-ai/kling-video/o3/standard/text-to-video) |  |
| Kling 3.0 | Kling AI API | 720p | yes | $0.126 | $0.630 | $1.26 | high | [link](https://kling.ai/dev/pricing) |  |
| Kling 3.0 Standard | fal.ai | 720p | yes | $0.126 | $0.630 | $1.26 | medium | [link](https://fal.ai/models/fal-ai/kling-video/v3/standard/text-to-video) |  |
| Kling 2.6 | Replicate | unspecified | yes | $0.140 | $0.700 | $1.40 | high | [link](https://replicate.com/kwaivgi/kling-v2.6) |  |
| Kling 2.6 Pro | fal.ai | unspecified | yes | $0.140 | $0.700 | $1.40 | high | [link](https://fal.ai/models/fal-ai/kling-video/v2.6/pro/text-to-video) |  |
| Kling 3.0 Omni | Kling AI API | 1080p | yes | $0.140 | $0.700 | $1.40 | high | [link](https://kling.ai/dev/pricing) |  |
| Kling 3.0 Turbo | Kling AI API | 1080p | yes | $0.140 | $0.700 | $1.40 | high | [link](https://kling.ai/dev/pricing) |  |
| Kling O3 Pro | fal.ai | 1080p | yes | $0.140 | $0.700 | $1.40 | medium | [link](https://fal.ai/models/fal-ai/kling-video/o3/pro/text-to-video) |  |
| Kling 4.0 | Replicate | 720p | n/a | $0.157 | $0.785 | $1.57 | high | [link](https://replicate.com/kwaivgi/kling-v4.0) |  |
| Kling 4.0 | fal.ai | 720p | n/a | $0.157 | $0.785 | $1.57 | high | [link](https://fal.ai/models/kling/v4/text-to-video) |  |
| Kling 4.0 (hosted by Runway) | Runway API | 720p | yes | $0.157 | $0.785 | $1.57 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) | promo |
| Kling 3.0 | Kling AI API | 1080p | yes | $0.168 | $0.840 | $1.68 | high | [link](https://kling.ai/dev/pricing) |  |
| Kling 3.0 | Replicate | 720p | no | $0.168 | $0.840 | $1.68 | high | [link](https://replicate.com/kwaivgi/kling-v3-video) |  |
| Kling 3.0 Omni | Replicate | 720p | no | $0.168 | $0.840 | $1.68 | medium | [link](https://replicate.com/kwaivgi/kling-v3-omni-video) |  |
| Kling 3.0 Pro | fal.ai | 1080p | yes | $0.168 | $0.840 | $1.68 | medium | [link](https://fal.ai/models/fal-ai/kling-video/v3/pro/text-to-video) |  |
| Kling 3.0 | Replicate | 1080p | no | $0.224 | $1.12 | $2.24 | high | [link](https://replicate.com/kwaivgi/kling-v3-video) |  |
| Kling 3.0 Omni | Replicate | 720p | yes | $0.224 | $1.12 | $2.24 | medium | [link](https://replicate.com/kwaivgi/kling-v3-omni-video) |  |
| Kling 3.0 Omni | Replicate | 1080p | no | $0.224 | $1.12 | $2.24 | medium | [link](https://replicate.com/kwaivgi/kling-v3-omni-video) |  |
| Kling 4.0 | Replicate | 1080p | n/a | $0.235 | $1.18 | $2.35 | high | [link](https://replicate.com/kwaivgi/kling-v4.0) |  |
| Kling 4.0 | fal.ai | 1080p | n/a | $0.235 | $1.18 | $2.35 | high | [link](https://fal.ai/models/kling/v4/text-to-video) |  |
| Kling 4.0 (hosted by Runway) | Runway API | 1080p | yes | $0.235 | $1.18 | $2.35 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) | promo |
| Kling 3.0 | Replicate | 720p | yes | $0.252 | $1.26 | $2.52 | high | [link](https://replicate.com/kwaivgi/kling-v3-video) |  |
| Kling 3.0 Omni | Replicate | 1080p | yes | $0.280 | $1.40 | $2.80 | medium | [link](https://replicate.com/kwaivgi/kling-v3-omni-video) |  |
| Kling 3.0 4K | Higgsfield API | 4k | n/a | $0.315 | $1.57 | $3.15 | low | [link](https://open.higgsfield.ai/pricing) |  |
| Kling 3.0 | Replicate | 1080p | yes | $0.336 | $1.68 | $3.36 | high | [link](https://replicate.com/kwaivgi/kling-v3-video) |  |
| Kling 3.0 | Kling AI API | 4k | n/a | $0.420 | $2.10 | $4.20 | high | [link](https://kling.ai/dev/pricing) |  |
| Kling 3.0 | Replicate | 4k | n/a | $0.420 | $2.10 | $4.20 | high | [link](https://replicate.com/kwaivgi/kling-v3-video) |  |
| Kling 3.0 4K | fal.ai | 4k | n/a | $0.420 | $2.10 | $4.20 | high | [link](https://fal.ai/models/fal-ai/kling-video/v3/4k/text-to-video) |  |
| Kling 3.0 Omni | Kling AI API | 4k | n/a | $0.420 | $2.10 | $4.20 | high | [link](https://kling.ai/dev/pricing) |  |
| Kling 3.0 Omni | Replicate | 4k | n/a | $0.420 | $2.10 | $4.20 | high | [link](https://replicate.com/kwaivgi/kling-v3-omni-video) |  |
| Kling 4.0 | fal.ai | 4k | n/a | $0.549 | $2.75 | $5.49 | high | [link](https://fal.ai/models/kling/v4/text-to-video) |  |

</details>

<details>
<summary><b>LTX</b> (12 rows, sorted by USD/s)</summary>

| Model | Provider | Res | Audio | USD/s | USD/5s | USD/10s | Conf | Source | Notes |
|---|---|---|---|---:|---:|---:|---|---|---|
| LTX 2.3 Fast | fal.ai | 1080p | n/a | $0.060 | $0.300 | $0.600 | high | [link](https://fal.ai/models/fal-ai/ltx-2.3/text-to-video/fast) |  |
| LTX 2.3 Pro | fal.ai | 1080p | n/a | $0.080 | $0.400 | $0.800 | high | [link](https://fal.ai/models/fal-ai/ltx-2.3/text-to-video) |  |
| LTX 2.5 Fast | fal.ai | 720p | yes | $0.090 | $0.450 | $0.900 | high | [link](https://fal.ai/models/lightricks/ltx-2.5/text-to-video/fast) |  |
| LTX 2.3 Fast | fal.ai | 1440p | n/a | $0.120 | $0.600 | $1.20 | high | [link](https://fal.ai/models/fal-ai/ltx-2.3/text-to-video/fast) |  |
| LTX 2.5 Pro | fal.ai | 720p | n/a | $0.120 | $0.600 | $1.20 | high | [link](https://fal.ai/models/lightricks/ltx-2.5/text-to-video/pro) |  |
| LTX 2.5 Fast | fal.ai | 1080p | yes | $0.130 | $0.650 | $1.30 | high | [link](https://fal.ai/models/lightricks/ltx-2.5/text-to-video/fast) |  |
| LTX 2.3 Pro | fal.ai | 1440p | n/a | $0.160 | $0.800 | $1.60 | high | [link](https://fal.ai/models/fal-ai/ltx-2.3/text-to-video) |  |
| LTX 2.5 Pro | fal.ai | 1080p | n/a | $0.170 | $0.850 | $1.70 | high | [link](https://fal.ai/models/lightricks/ltx-2.5/text-to-video/pro) |  |
| LTX 2.5 Fast | fal.ai | 1440p | yes | $0.190 | $0.950 | $1.90 | high | [link](https://fal.ai/models/lightricks/ltx-2.5/text-to-video/fast) |  |
| LTX 2.3 Fast | fal.ai | 4k | n/a | $0.240 | $1.20 | $2.40 | high | [link](https://fal.ai/models/fal-ai/ltx-2.3/text-to-video/fast) |  |
| LTX 2.5 Fast | fal.ai | 4k | yes | $0.300 | $1.50 | $3.00 | high | [link](https://fal.ai/models/lightricks/ltx-2.5/text-to-video/fast) |  |
| LTX 2.3 Pro | fal.ai | 4k | n/a | $0.320 | $1.60 | $3.20 | high | [link](https://fal.ai/models/fal-ai/ltx-2.3/text-to-video) |  |

</details>

<details>
<summary><b>Luma Ray</b> (17 rows, sorted by USD/s)</summary>

| Model | Provider | Res | Audio | USD/s | USD/5s | USD/10s | Conf | Source | Notes |
|---|---|---|---|---:|---:|---:|---|---|---|
| Luma Ray 3.2 | Luma API | 360p | n/a | $0.012 | $0.060 | $0.120 | medium | [link](https://lumalabs.ai/api/pricing) |  |
| Luma Ray 3.2 | Luma API | 360p | n/a | $0.018 | $0.090 | $0.180 | medium | [link](https://lumalabs.ai/api/pricing) |  |
| Luma Ray 3.2 | Luma API | 540p | n/a | $0.030 | $0.150 | $0.300 | medium | [link](https://lumalabs.ai/api/pricing) |  |
| Luma Ray 3.2 | Replicate | 540p | n/a | $0.030 | $0.150 | $0.300 | high | [link](https://replicate.com/luma/ray-3.2) |  |
| Luma Ray 3.2 | fal.ai | 540p | n/a | $0.030 | $0.150 | $0.300 | high | [link](https://fal.ai/models/luma/agent/ray/v3.2/image-to-video) |  |
| Luma Ray 3.2 | Luma API | 540p | n/a | $0.045 | $0.225 | $0.450 | medium | [link](https://lumalabs.ai/api/pricing) |  |
| Luma Ray 3.2 | Luma API | 720p | n/a | $0.060 | $0.300 | $0.600 | medium | [link](https://lumalabs.ai/api/pricing) |  |
| Luma Ray 3.2 | Replicate | 720p | n/a | $0.060 | $0.300 | $0.600 | high | [link](https://replicate.com/luma/ray-3.2) |  |
| Luma Ray 3.2 | fal.ai | 720p | n/a | $0.060 | $0.300 | $0.600 | high | [link](https://fal.ai/models/luma/agent/ray/v3.2/image-to-video) |  |
| Luma Ray 3.2 | Luma API | 720p | n/a | $0.090 | $0.450 | $0.900 | medium | [link](https://lumalabs.ai/api/pricing) |  |
| Luma Ray 3.2 | fal.ai | 540p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://fal.ai/models/luma/agent/ray/v3.2/text-to-video) |  |
| Luma Ray 3.2 | fal.ai | 720p | n/a | $0.200 | $1.00 | $2.00 | high | [link](https://fal.ai/models/luma/agent/ray/v3.2/text-to-video) |  |
| Luma Ray 3.2 | Luma API | 1080p | n/a | $0.240 | $1.20 | $2.40 | medium | [link](https://lumalabs.ai/api/pricing) |  |
| Luma Ray 3.2 | Replicate | 1080p | n/a | $0.240 | $1.20 | $2.40 | high | [link](https://replicate.com/luma/ray-3.2) |  |
| Luma Ray 3.2 | fal.ai | 1080p | n/a | $0.240 | $1.20 | $2.40 | high | [link](https://fal.ai/models/luma/agent/ray/v3.2/image-to-video) |  |
| Luma Ray 3.2 | Luma API | 1080p | n/a | $0.360 | $1.80 | $3.60 | medium | [link](https://lumalabs.ai/api/pricing) |  |
| Luma Ray 3.2 | fal.ai | 1080p | n/a | $0.400 | $2.00 | $4.00 | high | [link](https://fal.ai/models/luma/agent/ray/v3.2/text-to-video) |  |

</details>

<details>
<summary><b>MiniMax Hailuo</b> (42 rows, sorted by USD/s)</summary>

| Model | Provider | Res | Audio | USD/s | USD/5s | USD/10s | Conf | Source | Notes |
|---|---|---|---|---:|---:|---:|---|---|---|
| MiniMax H3 Lite | Replicate | 480p | n/a | $0.0125 | $0.0625 | $0.125 | high | [link](https://replicate.com/minimax/h3-lite) | promo |
| MiniMax H3 Lite | Replicate | 768p | n/a | $0.020 | $0.100 | $0.200 | high | [link](https://replicate.com/minimax/h3-lite) | promo |
| MiniMax H3 Lite | MiniMax API Platform | 480p | n/a | $0.025 | $0.125 | $0.250 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax H3 Max Turbo | MiniMax API Platform | 480p | n/a | $0.025 | $0.125 | $0.250 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax H3 Max Turbo | fal.ai | 480p | n/a | $0.025 | $0.125 | $0.250 | high | [link](https://fal.ai/models/minimax/h3-max-turbo/text-to-video) |  |
| MiniMax H3 Highspeed | Replicate | 768p | n/a | $0.030 | $0.150 | $0.300 | high | [link](https://replicate.com/minimax/h3-highspeed) | promo |
| MiniMax Hailuo 2.3 Fast | MiniMax API Platform | 768p | n/a | $0.0317 | $0.1583 | $0.3167 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax Hailuo 2.3 Fast | Replicate | 768p | n/a | $0.0317 | $0.1583 | $0.3167 | high | [link](https://replicate.com/minimax/hailuo-2.3-fast) |  |
| MiniMax Hailuo 2.3 Fast Standard | fal.ai | 768p | n/a | $0.0317 | $0.1583 | $0.3167 | high | [link](https://fal.ai/models/fal-ai/minimax/hailuo-2.3-fast/standard/image-to-video) |  |
| MiniMax Hailuo 2.3 Fast | MiniMax API Platform | 768p | n/a | $0.032 | $0.160 | $0.320 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax Hailuo 2.3 Fast | Replicate | 768p | n/a | $0.032 | $0.160 | $0.320 | high | [link](https://replicate.com/minimax/hailuo-2.3-fast) |  |
| MiniMax Hailuo 2.3 Fast Standard | fal.ai | 768p | n/a | $0.032 | $0.160 | $0.320 | high | [link](https://fal.ai/models/fal-ai/minimax/hailuo-2.3-fast/standard/image-to-video) |  |
| MiniMax H3 Highspeed | MiniMax API Platform | 480p | n/a | $0.040 | $0.200 | $0.400 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax H3 Lite | MiniMax API Platform | 768p | n/a | $0.040 | $0.200 | $0.400 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax H3 Max Turbo | MiniMax API Platform | 768p | n/a | $0.040 | $0.200 | $0.400 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax H3 Max Turbo | fal.ai | 768p | n/a | $0.040 | $0.200 | $0.400 | high | [link](https://fal.ai/models/minimax/h3-max-turbo/text-to-video) |  |
| MiniMax Hailuo 2.3 | MiniMax API Platform | 768p | n/a | $0.0467 | $0.2333 | $0.4667 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax Hailuo 2.3 | Replicate | 768p | n/a | $0.0467 | $0.2333 | $0.4667 | high | [link](https://replicate.com/minimax/hailuo-2.3) |  |
| MiniMax Hailuo 2.3 Standard | fal.ai | 768p | n/a | $0.0467 | $0.2333 | $0.4667 | high | [link](https://fal.ai/models/fal-ai/minimax/hailuo-2.3/standard/text-to-video) |  |
| MiniMax H3 | fal.ai | 480p | n/a | $0.050 | $0.250 | $0.500 | high | [link](https://fal.ai/models/minimax/h3/text-to-video) |  |
| MiniMax H3 Max | MiniMax API Platform | 480p | n/a | $0.050 | $0.250 | $0.500 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax H3 Max | fal.ai | 480p | n/a | $0.050 | $0.250 | $0.500 | high | [link](https://fal.ai/models/minimax/h3-max/text-to-video) |  |
| MiniMax H3 Max Turbo | MiniMax API Platform | 480p | n/a | $0.050 | $0.250 | $0.500 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax Hailuo 2.3 Fast | MiniMax API Platform | 1080p | n/a | $0.055 | $0.275 | $0.550 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax Hailuo 2.3 Fast | Replicate | 1080p | n/a | $0.055 | $0.275 | $0.550 | high | [link](https://replicate.com/minimax/hailuo-2.3-fast) |  |
| MiniMax Hailuo 2.3 | MiniMax API Platform | 768p | n/a | $0.056 | $0.280 | $0.560 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax Hailuo 2.3 | Replicate | 768p | n/a | $0.056 | $0.280 | $0.560 | high | [link](https://replicate.com/minimax/hailuo-2.3) |  |
| MiniMax Hailuo 2.3 Standard | fal.ai | 768p | n/a | $0.056 | $0.280 | $0.560 | high | [link](https://fal.ai/models/fal-ai/minimax/hailuo-2.3/standard/text-to-video) |  |
| MiniMax H3 | fal.ai | 768p | n/a | $0.060 | $0.300 | $0.600 | high | [link](https://fal.ai/models/minimax/h3/text-to-video) |  |
| MiniMax H3 Highspeed | MiniMax API Platform | 768p | n/a | $0.060 | $0.300 | $0.600 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax H3 | MiniMax API Platform | 768p | n/a | $0.080 | $0.400 | $0.800 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax H3 Max | MiniMax API Platform | 768p | n/a | $0.080 | $0.400 | $0.800 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax H3 Max | fal.ai | 768p | n/a | $0.080 | $0.400 | $0.800 | high | [link](https://fal.ai/models/minimax/h3-max/text-to-video) |  |
| MiniMax H3 Max Turbo | MiniMax API Platform | 768p | n/a | $0.080 | $0.400 | $0.800 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax H3 Max Turbo | fal.ai | 1080p | n/a | $0.080 | $0.400 | $0.800 | high | [link](https://fal.ai/models/minimax/h3-max-turbo/text-to-video) |  |
| MiniMax Hailuo 2.3 | MiniMax API Platform | 1080p | n/a | $0.0817 | $0.4083 | $0.8167 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax Hailuo 2.3 | Replicate | 1080p | n/a | $0.0817 | $0.4083 | $0.8167 | high | [link](https://replicate.com/minimax/hailuo-2.3) |  |
| MiniMax Hailuo 2.3 Pro | fal.ai | 1080p | n/a | $0.0817 | $0.4083 | $0.8167 | medium | [link](https://fal.ai/models/fal-ai/minimax/hailuo-2.3/pro/text-to-video) |  |
| MiniMax H3 | MiniMax API Platform | 2k | n/a | $0.130 | $0.650 | $1.30 | high | [link](https://platform.minimax.io/docs/guides/pricing-paygo) |  |
| MiniMax H3 | fal.ai | 2k | n/a | $0.130 | $0.650 | $1.30 | high | [link](https://fal.ai/models/minimax/h3/text-to-video) |  |
| MiniMax H3 | fal.ai | 4k | n/a | $0.160 | $0.800 | $1.60 | high | [link](https://fal.ai/models/minimax/h3/text-to-video) |  |
| MiniMax H3 Max | fal.ai | 1080p | n/a | $0.160 | $0.800 | $1.60 | high | [link](https://fal.ai/models/minimax/h3-max/text-to-video) |  |

</details>

<details>
<summary><b>PixVerse</b> (14 rows, sorted by USD/s)</summary>

| Model | Provider | Res | Audio | USD/s | USD/5s | USD/10s | Conf | Source | Notes |
|---|---|---|---|---:|---:|---:|---|---|---|
| PixVerse V6 | fal.ai | 540p | no | $0.035 | $0.175 | $0.350 | high | [link](https://fal.ai/models/fal-ai/pixverse/v6/text-to-video) |  |
| PixVerse V6 | fal.ai | 540p | yes | $0.045 | $0.225 | $0.450 | high | [link](https://fal.ai/models/fal-ai/pixverse/v6/text-to-video) |  |
| PixVerse V6 | fal.ai | 720p | no | $0.045 | $0.225 | $0.450 | high | [link](https://fal.ai/models/fal-ai/pixverse/v6/text-to-video) |  |
| PixVerse V6 | fal.ai | 720p | yes | $0.060 | $0.300 | $0.600 | high | [link](https://fal.ai/models/fal-ai/pixverse/v6/text-to-video) |  |
| PixVerse V6 | Replicate | 720p | no | $0.090 | $0.450 | $0.900 | high | [link](https://replicate.com/pixverse/pixverse-v6) |  |
| PixVerse V6 | fal.ai | 1080p | no | $0.090 | $0.450 | $0.900 | high | [link](https://fal.ai/models/fal-ai/pixverse/v6/text-to-video) |  |
| PixVerse V6 Max | fal.ai | 720p | no | $0.099 | $0.495 | $0.990 | high | [link](https://fal.ai/models/pixverse/v6/max/text-to-video) |  |
| PixVerse V6 | fal.ai | 1080p | yes | $0.115 | $0.575 | $1.15 | high | [link](https://fal.ai/models/fal-ai/pixverse/v6/text-to-video) |  |
| PixVerse V6 | Replicate | 720p | yes | $0.120 | $0.600 | $1.20 | high | [link](https://replicate.com/pixverse/pixverse-v6) |  |
| PixVerse V6 Max | fal.ai | 720p | yes | $0.135 | $0.675 | $1.35 | high | [link](https://fal.ai/models/pixverse/v6/max/text-to-video) |  |
| PixVerse V6 | Replicate | 1080p | no | $0.180 | $0.900 | $1.80 | high | [link](https://replicate.com/pixverse/pixverse-v6) |  |
| PixVerse V6 Max | fal.ai | 1080p | no | $0.198 | $0.990 | $1.98 | high | [link](https://fal.ai/models/pixverse/v6/max/text-to-video) |  |
| PixVerse V6 | Replicate | 1080p | yes | $0.230 | $1.15 | $2.30 | high | [link](https://replicate.com/pixverse/pixverse-v6) |  |
| PixVerse V6 Max | fal.ai | 1080p | yes | $0.252 | $1.26 | $2.52 | high | [link](https://fal.ai/models/pixverse/v6/max/text-to-video) |  |

</details>

<details>
<summary><b>Runway</b> (4 rows, sorted by USD/s)</summary>

| Model | Provider | Res | Audio | USD/s | USD/5s | USD/10s | Conf | Source | Notes |
|---|---|---|---|---:|---:|---:|---|---|---|
| Runway Gen-4 Turbo | Runway API | unspecified | n/a | $0.050 | $0.250 | $0.500 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Runway Gen-4.5 | Replicate | unspecified | n/a | $0.120 | $0.600 | $1.20 | high | [link](https://replicate.com/runwayml/gen-4.5) |  |
| Runway Gen-4.5 | Runway API | unspecified | n/a | $0.120 | $0.600 | $1.20 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Runway Aleph 2.0 | Runway API | unspecified | n/a | $0.280 | $1.40 | $2.80 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |

</details>

<details>
<summary><b>Seedance</b> (71 rows, sorted by USD/s)</summary>

| Model | Provider | Res | Audio | USD/s | USD/5s | USD/10s | Conf | Source | Notes |
|---|---|---|---|---:|---:|---:|---|---|---|
| Seedance 1.0 Pro Fast | BytePlus ModelArk | 480p | n/a | $0.010 | $0.050 | $0.100 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 1.0 Lite | Replicate | 480p | n/a | $0.018 | $0.090 | $0.180 | high | [link](https://replicate.com/bytedance/seedance-1-lite) |  |
| Seedance 1.0 Pro Fast | BytePlus ModelArk | 720p | n/a | $0.020 | $0.100 | $0.200 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 1.0 Pro | BytePlus ModelArk | 480p | n/a | $0.024 | $0.120 | $0.240 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 1.0 Pro | Replicate | 480p | n/a | $0.030 | $0.150 | $0.300 | high | [link](https://replicate.com/bytedance/seedance-1-pro) |  |
| Seedance 1.0 Lite | Replicate | 720p | n/a | $0.036 | $0.180 | $0.360 | high | [link](https://replicate.com/bytedance/seedance-1-lite) |  |
| Seedance 2.0 Mini | BytePlus ModelArk | 480p | n/a | $0.040 | $0.200 | $0.400 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 1.0 Pro Fast | BytePlus ModelArk | 1080p | n/a | $0.048 | $0.240 | $0.480 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 1.0 Pro Fast | fal.ai | 1080p | n/a | $0.0486 | $0.243 | $0.486 | high | [link](https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/fast/image-to-video) |  |
| Seedance 1.0 Pro Fast | fal.ai | 1080p | n/a | $0.049 | $0.245 | $0.490 | high | [link](https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/fast/text-to-video) |  |
| Seedance 1.0 Pro | BytePlus ModelArk | 720p | n/a | $0.052 | $0.260 | $0.520 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 1.0 Pro | fal.ai | 720p | n/a | $0.054 | $0.270 | $0.540 | medium | [link](https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/text-to-video) |  |
| Seedance 1.0 Pro | Replicate | 720p | n/a | $0.060 | $0.300 | $0.600 | high | [link](https://replicate.com/bytedance/seedance-1-pro) |  |
| Seedance 2.0 Fast | BytePlus ModelArk | 480p | n/a | $0.060 | $0.300 | $0.600 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 2.0 | BytePlus ModelArk | 480p | n/a | $0.070 | $0.350 | $0.700 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 2.0 Fast | Replicate | 480p | n/a | $0.070 | $0.350 | $0.700 | high | [link](https://replicate.com/bytedance/seedance-2.0-fast) |  |
| Seedance 2.0 Mini (hosted by Runway) | Runway API | 480p | n/a | $0.070 | $0.350 | $0.700 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.5 Flash | BytePlus ModelArk | 480p | n/a | $0.070 | $0.350 | $0.700 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 1.0 Lite | Replicate | 1080p | n/a | $0.072 | $0.360 | $0.720 | high | [link](https://replicate.com/bytedance/seedance-1-lite) |  |
| Seedance 2.0 Mini | fal.ai | 480p | n/a | $0.0721 | $0.3605 | $0.721 | high | [link](https://fal.ai/models/bytedance/seedance-2.0/mini/text-to-video) |  |
| Seedance 2.0 | Higgsfield API | 480p | n/a | $0.080 | $0.400 | $0.800 | medium | [link](https://open.higgsfield.ai/pricing) |  |
| Seedance 2.0 | Replicate | 480p | n/a | $0.080 | $0.400 | $0.800 | high | [link](https://replicate.com/bytedance/seedance-2.0) |  |
| Seedance 2.0 Mini | BytePlus ModelArk | 720p | n/a | $0.080 | $0.400 | $0.800 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 2.5 | BytePlus ModelArk | 480p | n/a | $0.103 | $0.515 | $1.03 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 2.5 | Pika Developer API | 480p | n/a | $0.1079 | $0.5397 | $1.08 | medium | [link](https://dev.pika.art/models/bytedance/seedance-2.5/text-to-video/pricing) |  |
| Seedance 2.0 Fast (hosted by Runway) | Runway API | 480p | n/a | $0.110 | $0.550 | $1.10 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.5 | Higgsfield API | 480p | n/a | $0.118 | $0.590 | $1.18 | medium | [link](https://open.higgsfield.ai/pricing) |  |
| Seedance 2.0 Fast | BytePlus ModelArk | 720p | n/a | $0.120 | $0.600 | $1.20 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 1.0 Pro | BytePlus ModelArk | 1080p | n/a | $0.122 | $0.610 | $1.22 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 1.0 Pro | fal.ai | 1080p | n/a | $0.124 | $0.620 | $1.24 | high | [link](https://fal.ai/models/fal-ai/bytedance/seedance/v1/pro/text-to-video) |  |
| Seedance 2.5 Flash (hosted by Runway) | Runway API | 480p | n/a | $0.130 | $0.650 | $1.30 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.5 Flash | fal.ai | 480p | n/a | $0.1345 | $0.6725 | $1.34 | high | [link](https://fal.ai/models/bytedance/seedance-2.5/flash/text-to-video) |  |
| Seedance 2.0 (hosted by Runway) | Runway API | 480p | n/a | $0.140 | $0.700 | $1.40 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.0 (US region endpoint) | fal.ai | 480p | n/a | $0.1406 | $0.703 | $1.41 | high | [link](https://fal.ai/models/bytedance/seedance-2.0/us/text-to-video) |  |
| Seedance 1.0 Pro | Replicate | 1080p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://replicate.com/bytedance/seedance-1-pro) |  |
| Seedance 2.0 | BytePlus ModelArk | 720p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 2.0 Fast | Replicate | 720p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://replicate.com/bytedance/seedance-2.0-fast) |  |
| Seedance 2.0 Mini (hosted by Runway) | Runway API | 720p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.5 Flash | BytePlus ModelArk | 720p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 2.0 Mini | fal.ai | 720p | n/a | $0.1547 | $0.7735 | $1.55 | high | [link](https://fal.ai/models/bytedance/seedance-2.0/mini/text-to-video) |  |
| Seedance 2.0 | Replicate | 720p | n/a | $0.180 | $0.900 | $1.80 | high | [link](https://replicate.com/bytedance/seedance-2.0) |  |
| Seedance 2.5 (hosted by Runway) | Runway API | 480p | n/a | $0.200 | $1.00 | $2.00 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.5 Flash (hosted by Runway) | Runway API | 720p | n/a | $0.200 | $1.00 | $2.00 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.5 (US region endpoint) | fal.ai | 480p | n/a | $0.2205 | $1.10 | $2.21 | high | [link](https://fal.ai/models/bytedance/seedance-2.5/us/text-to-video) |  |
| Seedance 2.5 | BytePlus ModelArk | 720p | n/a | $0.231 | $1.16 | $2.31 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 2.0 Fast (hosted by Runway) | Runway API | 720p | n/a | $0.240 | $1.20 | $2.40 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.0 Fast | fal.ai | 720p | n/a | $0.2419 | $1.21 | $2.42 | high | [link](https://fal.ai/models/bytedance/seedance-2.0/fast/text-to-video) |  |
| Seedance 2.5 | Pika Developer API | 720p | n/a | $0.2427 | $1.21 | $2.43 | medium | [link](https://dev.pika.art/models/bytedance/seedance-2.5/text-to-video/pricing) |  |
| Seedance 2.0 (hosted by Runway) | Runway API | 720p | n/a | $0.300 | $1.50 | $3.00 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.5 (hosted by Runway) | Runway API | 720p | n/a | $0.300 | $1.50 | $3.00 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.0 (US region endpoint) | fal.ai | 720p | n/a | $0.3024 | $1.51 | $3.02 | high | [link](https://fal.ai/models/bytedance/seedance-2.0/us/text-to-video) |  |
| Seedance 2.5 Flash | fal.ai | 720p | n/a | $0.3024 | $1.51 | $3.02 | high | [link](https://fal.ai/models/bytedance/seedance-2.5/flash/text-to-video) |  |
| Seedance 2.0 | fal.ai | 720p | n/a | $0.3034 | $1.52 | $3.03 | high | [link](https://fal.ai/models/bytedance/seedance-2.0/text-to-video) |  |
| Seedance 2.0 | BytePlus ModelArk | 1080p | n/a | $0.370 | $1.85 | $3.70 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 2.0 (hosted by Runway) | Runway API | 1080p | n/a | $0.400 | $2.00 | $4.00 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.0 | Replicate | 1080p | n/a | $0.450 | $2.25 | $4.50 | high | [link](https://replicate.com/bytedance/seedance-2.0) |  |
| Seedance 2.5 (US region endpoint) | fal.ai | 720p | n/a | $0.473 | $2.37 | $4.73 | high | [link](https://fal.ai/models/bytedance/seedance-2.5/us/text-to-video) |  |
| Seedance 2.5 | BytePlus ModelArk | 1080p | n/a | $0.569 | $2.85 | $5.69 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 2.5 | Pika Developer API | 1080p | n/a | $0.5971 | $2.99 | $5.97 | medium | [link](https://dev.pika.art/models/bytedance/seedance-2.5/text-to-video/pricing) |  |
| Seedance 2.5 (hosted by Runway) | Runway API | 1080p | n/a | $0.680 | $3.40 | $6.80 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.0 | fal.ai | 1080p | n/a | $0.682 | $3.41 | $6.82 | high | [link](https://fal.ai/models/bytedance/seedance-2.0/text-to-video) |  |
| Seedance 2.0 (US region endpoint) | fal.ai | 1080p | n/a | $0.7484 | $3.74 | $7.48 | high | [link](https://fal.ai/models/bytedance/seedance-2.0/us/text-to-video) |  |
| Seedance 2.0 | BytePlus ModelArk | 4k | n/a | $0.780 | $3.90 | $7.80 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 2.5 | BytePlus ModelArk | 4k | n/a | $0.914 | $4.57 | $9.14 | high | [link](https://docs.byteplus.com/en/docs/modelark/model-pricing) |  |
| Seedance 2.0 | Replicate | 4k | n/a | $1.00 | $5.00 | $10.00 | high | [link](https://replicate.com/bytedance/seedance-2.0) |  |
| Seedance 2.5 | Pika Developer API | 4k | n/a | $1.01 | $5.03 | $10.05 | medium | [link](https://dev.pika.art/models/bytedance/seedance-2.5/text-to-video/pricing) |  |
| Seedance 2.5 (hosted by Runway) | Runway API | 4k | n/a | $1.10 | $5.50 | $11.00 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.5 (US region endpoint) | fal.ai | 1080p | n/a | $1.16 | $5.82 | $11.64 | high | [link](https://fal.ai/models/bytedance/seedance-2.5/us/text-to-video) |  |
| Seedance 2.0 (hosted by Runway) | Runway API | 4k | n/a | $1.50 | $7.50 | $15.00 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Seedance 2.0 (US region endpoint) | fal.ai | 4k | n/a | $1.56 | $7.78 | $15.55 | high | [link](https://fal.ai/models/bytedance/seedance-2.0/us/text-to-video) |  |
| Seedance 2.5 (US region endpoint) | fal.ai | 4k | n/a | $1.84 | $9.20 | $18.40 | high | [link](https://fal.ai/models/bytedance/seedance-2.5/us/text-to-video) |  |

</details>

<details>
<summary><b>Sora</b> (4 rows, sorted by USD/s)</summary>

| Model | Provider | Res | Audio | USD/s | USD/5s | USD/10s | Conf | Source | Notes |
|---|---|---|---|---:|---:|---:|---|---|---|
| Sora 2 | OpenAI API | 720p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://developers.openai.com/api/docs/models/sora-2) | discontinued |
| Sora 2 Pro | OpenAI API | 720p | n/a | $0.300 | $1.50 | $3.00 | high | [link](https://developers.openai.com/api/docs/models/sora-2-pro) | discontinued |
| Sora 2 Pro | OpenAI API | 1024p | n/a | $0.500 | $2.50 | $5.00 | high | [link](https://developers.openai.com/api/docs/models/sora-2-pro) | discontinued |
| Sora 2 Pro | OpenAI API | 1080p | n/a | $0.700 | $3.50 | $7.00 | high | [link](https://developers.openai.com/api/docs/models/sora-2-pro) | discontinued |

</details>

<details>
<summary><b>Veo</b> (40 rows, sorted by USD/s)</summary>

| Model | Provider | Res | Audio | USD/s | USD/5s | USD/10s | Conf | Source | Notes |
|---|---|---|---|---:|---:|---:|---|---|---|
| Veo 3.1 Lite | Google Cloud Vertex AI | 720p | no | $0.030 | $0.150 | $0.300 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 Lite | fal.ai | 720p | no | $0.030 | $0.150 | $0.300 | high | [link](https://fal.ai/models/fal-ai/veo3.1/lite/image-to-video) |  |
| Veo 3.1 Lite | Google Cloud Vertex AI | 720p | yes | $0.050 | $0.250 | $0.500 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 Lite | Google Cloud Vertex AI | 1080p | no | $0.050 | $0.250 | $0.500 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 Lite | fal.ai | 720p | yes | $0.050 | $0.250 | $0.500 | high | [link](https://fal.ai/models/fal-ai/veo3.1/lite/image-to-video) |  |
| Veo 3.1 Lite | fal.ai | 1080p | no | $0.050 | $0.250 | $0.500 | high | [link](https://fal.ai/models/fal-ai/veo3.1/lite/image-to-video) |  |
| Veo 3.1 Fast | Google Cloud Vertex AI | 720p | no | $0.080 | $0.400 | $0.800 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 Lite | Google Cloud Vertex AI | 1080p | yes | $0.080 | $0.400 | $0.800 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 Lite | fal.ai | 1080p | yes | $0.080 | $0.400 | $0.800 | high | [link](https://fal.ai/models/fal-ai/veo3.1/lite/image-to-video) |  |
| Veo 3.1 Fast | Google Cloud Vertex AI | 720p | yes | $0.100 | $0.500 | $1.00 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 Fast | Google Cloud Vertex AI | 1080p | no | $0.100 | $0.500 | $1.00 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 Fast | Replicate | unspecified | no | $0.100 | $0.500 | $1.00 | high | [link](https://replicate.com/google/veo-3.1-fast) |  |
| Veo 3.1 Fast | fal.ai | 720p | no | $0.100 | $0.500 | $1.00 | high | [link](https://fal.ai/models/fal-ai/veo3.1/fast/image-to-video) |  |
| Veo 3.1 Fast | fal.ai | 1080p | no | $0.100 | $0.500 | $1.00 | high | [link](https://fal.ai/models/fal-ai/veo3.1/fast/image-to-video) |  |
| Veo 3.1 Fast (hosted by Runway) | Runway API | unspecified | no | $0.100 | $0.500 | $1.00 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Veo 3.1 Fast | Google Cloud Vertex AI | 1080p | yes | $0.120 | $0.600 | $1.20 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 Fast | Replicate | unspecified | yes | $0.150 | $0.750 | $1.50 | high | [link](https://replicate.com/google/veo-3.1-fast) |  |
| Veo 3.1 Fast | fal.ai | 720p | yes | $0.150 | $0.750 | $1.50 | high | [link](https://fal.ai/models/fal-ai/veo3.1/fast/image-to-video) |  |
| Veo 3.1 Fast | fal.ai | 1080p | yes | $0.150 | $0.750 | $1.50 | high | [link](https://fal.ai/models/fal-ai/veo3.1/fast/image-to-video) |  |
| Veo 3.1 Fast (hosted by Runway) | Runway API | unspecified | yes | $0.150 | $0.750 | $1.50 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Veo 3.1 | Google Cloud Vertex AI | 720p | no | $0.200 | $1.00 | $2.00 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 | Google Cloud Vertex AI | 1080p | no | $0.200 | $1.00 | $2.00 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 | Replicate | unspecified | no | $0.200 | $1.00 | $2.00 | high | [link](https://replicate.com/google/veo-3.1) |  |
| Veo 3.1 | fal.ai | 720p | no | $0.200 | $1.00 | $2.00 | high | [link](https://fal.ai/models/fal-ai/veo3.1) |  |
| Veo 3.1 | fal.ai | 1080p | no | $0.200 | $1.00 | $2.00 | high | [link](https://fal.ai/models/fal-ai/veo3.1) |  |
| Veo 3.1 (hosted by Runway) | Runway API | unspecified | no | $0.200 | $1.00 | $2.00 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Veo 3.1 Fast | Google Cloud Vertex AI | 4k | no | $0.250 | $1.25 | $2.50 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 Fast | Google Cloud Vertex AI | 4k | yes | $0.300 | $1.50 | $3.00 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 Fast | fal.ai | 4k | no | $0.300 | $1.50 | $3.00 | high | [link](https://fal.ai/models/fal-ai/veo3.1/fast/image-to-video) |  |
| Veo 3.1 Fast | fal.ai | 4k | yes | $0.350 | $1.75 | $3.50 | high | [link](https://fal.ai/models/fal-ai/veo3.1/fast/image-to-video) |  |
| Veo 3.1 | Google Cloud Vertex AI | 720p | yes | $0.400 | $2.00 | $4.00 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 | Google Cloud Vertex AI | 1080p | yes | $0.400 | $2.00 | $4.00 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 | Google Cloud Vertex AI | 4k | no | $0.400 | $2.00 | $4.00 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 | Replicate | unspecified | yes | $0.400 | $2.00 | $4.00 | high | [link](https://replicate.com/google/veo-3.1) |  |
| Veo 3.1 | fal.ai | 720p | yes | $0.400 | $2.00 | $4.00 | high | [link](https://fal.ai/models/fal-ai/veo3.1) |  |
| Veo 3.1 | fal.ai | 1080p | yes | $0.400 | $2.00 | $4.00 | high | [link](https://fal.ai/models/fal-ai/veo3.1) |  |
| Veo 3.1 | fal.ai | 4k | no | $0.400 | $2.00 | $4.00 | high | [link](https://fal.ai/models/fal-ai/veo3.1) |  |
| Veo 3.1 (hosted by Runway) | Runway API | unspecified | yes | $0.400 | $2.00 | $4.00 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Veo 3.1 | Google Cloud Vertex AI | 4k | yes | $0.600 | $3.00 | $6.00 | medium | [link](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) |  |
| Veo 3.1 | fal.ai | 4k | yes | $0.600 | $3.00 | $6.00 | high | [link](https://fal.ai/models/fal-ai/veo3.1) |  |

</details>

<details>
<summary><b>Vidu</b> (14 rows, sorted by USD/s)</summary>

| Model | Provider | Res | Audio | USD/s | USD/5s | USD/10s | Conf | Source | Notes |
|---|---|---|---|---:|---:|---:|---|---|---|
| Vidu Q3 Turbo | fal.ai | 540p | n/a | $0.035 | $0.175 | $0.350 | high | [link](https://fal.ai/models/fal-ai/vidu/q3/text-to-video/turbo) |  |
| Vidu Q4 | fal.ai | 540p | n/a | $0.045 | $0.225 | $0.450 | high | [link](https://fal.ai/models/fal-ai/vidu/q4/image-to-video) | promo |
| Vidu Q3 | fal.ai | 540p | n/a | $0.070 | $0.350 | $0.700 | high | [link](https://fal.ai/models/fal-ai/vidu/q3/text-to-video) |  |
| Vidu Q3 Pro | Replicate | 540p | n/a | $0.070 | $0.350 | $0.700 | high | [link](https://replicate.com/vidu/q3-pro) |  |
| Vidu Q3 Turbo | fal.ai | 720p | n/a | $0.077 | $0.385 | $0.770 | medium | [link](https://fal.ai/models/fal-ai/vidu/q3/text-to-video/turbo) |  |
| Vidu Q3 Turbo | fal.ai | 1080p | n/a | $0.077 | $0.385 | $0.770 | medium | [link](https://fal.ai/models/fal-ai/vidu/q3/text-to-video/turbo) |  |
| Vidu Q4 | fal.ai | 720p | n/a | $0.095 | $0.475 | $0.950 | high | [link](https://fal.ai/models/fal-ai/vidu/q4/image-to-video) | promo |
| Vidu Q4 | fal.ai | 1080p | n/a | $0.120 | $0.600 | $1.20 | high | [link](https://fal.ai/models/fal-ai/vidu/q4/image-to-video) | promo |
| Vidu Q3 Pro | Replicate | 720p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://replicate.com/vidu/q3-pro) |  |
| Vidu Q3 | fal.ai | 720p | n/a | $0.154 | $0.770 | $1.54 | medium | [link](https://fal.ai/models/fal-ai/vidu/q3/text-to-video) |  |
| Vidu Q3 | fal.ai | 1080p | n/a | $0.154 | $0.770 | $1.54 | medium | [link](https://fal.ai/models/fal-ai/vidu/q3/text-to-video) |  |
| Vidu Q3 Pro | Replicate | 1080p | n/a | $0.160 | $0.800 | $1.60 | high | [link](https://replicate.com/vidu/q3-pro) |  |
| Vidu Q4 | fal.ai | 2k | n/a | $0.190 | $0.950 | $1.90 | high | [link](https://fal.ai/models/fal-ai/vidu/q4/image-to-video) | promo |
| Vidu Q4 | fal.ai | 4k | n/a | $0.390 | $1.95 | $3.90 | high | [link](https://fal.ai/models/fal-ai/vidu/q4/image-to-video) | promo |

</details>

<details>
<summary><b>Wan</b> (51 rows, sorted by USD/s)</summary>

| Model | Provider | Res | Audio | USD/s | USD/5s | USD/10s | Conf | Source | Notes |
|---|---|---|---|---:|---:|---:|---|---|---|
| Wan 2.2 image-to-video Flash (wan2.2-i2v-flash) | Alibaba Cloud Model Studio | 480p | no | $0.015 | $0.075 | $0.150 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.2 text-to-video Plus (wan2.2-t2v-plus) | Alibaba Cloud Model Studio | 480p | n/a | $0.020 | $0.100 | $0.200 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.6 image-to-video Flash (wan2.6-i2v-flash) | Alibaba Cloud Model Studio | 720p | no | $0.025 | $0.125 | $0.250 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 3.0 | Replicate | 480p | n/a | $0.035 | $0.175 | $0.350 | high | [link](https://replicate.com/alibaba/wan-3) |  |
| Wan 2.2 image-to-video Flash (wan2.2-i2v-flash) | Alibaba Cloud Model Studio | 720p | no | $0.036 | $0.180 | $0.360 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.6 image-to-video Flash (wan2.6-i2v-flash) | Alibaba Cloud Model Studio | 1080p | no | $0.0375 | $0.1875 | $0.375 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.5 (text-to-video) | Replicate | 480p | n/a | $0.050 | $0.250 | $0.500 | high | [link](https://replicate.com/wan-video/wan-2.5-t2v) |  |
| Wan 2.5 Preview | fal.ai | 480p | n/a | $0.050 | $0.250 | $0.500 | high | [link](https://fal.ai/models/fal-ai/wan-25-preview/text-to-video) |  |
| Wan 2.5 text-to-video preview (wan2.5-t2v-preview) | Alibaba Cloud Model Studio | 480p | n/a | $0.050 | $0.250 | $0.500 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.6 Flash | fal.ai | 720p | n/a | $0.050 | $0.250 | $0.500 | high | [link](https://fal.ai/models/wan/v2.6/image-to-video/flash) |  |
| Wan 2.6 image-to-video Flash (wan2.6-i2v-flash) | Alibaba Cloud Model Studio | 720p | yes | $0.050 | $0.250 | $0.500 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 3.0 | fal.ai | 480p | n/a | $0.050 | $0.250 | $0.500 | high | [link](https://fal.ai/models/alibaba/wan-3.0/text-to-video) |  |
| Wan 3.0 (hosted by Runway) | Runway API | 480p | n/a | $0.050 | $0.250 | $0.500 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Wan 3.0 (wan3.0-video) | Alibaba Cloud Model Studio | 480p | n/a | $0.050 | $0.250 | $0.500 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) | promo |
| Wan 3.0 Prime | fal.ai | 480p | n/a | $0.068 | $0.340 | $0.680 | high | [link](https://fal.ai/models/alibaba/wan-3.0-prime/text-to-video) |  |
| Wan 3.0 Prime (wan3.0-video-prime) | Alibaba Cloud Model Studio | 480p | n/a | $0.068 | $0.340 | $0.680 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 3.0 | Replicate | 720p | n/a | $0.070 | $0.350 | $0.700 | high | [link](https://replicate.com/alibaba/wan-3) |  |
| Wan 2.6 Flash | fal.ai | 1080p | n/a | $0.075 | $0.375 | $0.750 | high | [link](https://fal.ai/models/wan/v2.6/image-to-video/flash) |  |
| Wan 2.6 image-to-video Flash (wan2.6-i2v-flash) | Alibaba Cloud Model Studio | 1080p | yes | $0.075 | $0.375 | $0.750 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.2 text-to-video Plus (wan2.2-t2v-plus) | Alibaba Cloud Model Studio | 1080p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.5 (text-to-video) | Replicate | 720p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://replicate.com/wan-video/wan-2.5-t2v) |  |
| Wan 2.5 Preview | fal.ai | 720p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://fal.ai/models/fal-ai/wan-25-preview/text-to-video) |  |
| Wan 2.5 text-to-video preview (wan2.5-t2v-preview) | Alibaba Cloud Model Studio | 720p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.6 | fal.ai | 720p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://fal.ai/models/wan/v2.6/text-to-video) |  |
| Wan 2.6 image-to-video (wan2.6-i2v) | Alibaba Cloud Model Studio | 720p | yes | $0.100 | $0.500 | $1.00 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.6 text-to-video (wan2.6-t2v) | Alibaba Cloud Model Studio | 720p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.7 | fal.ai | 720p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://fal.ai/models/fal-ai/wan/v2.7/text-to-video) |  |
| Wan 2.7 (image-to-video) | Replicate | 720p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://replicate.com/wan-video/wan-2.7-i2v) |  |
| Wan 2.7 image-to-video (wan2.7-i2v) | Alibaba Cloud Model Studio | 720p | yes | $0.100 | $0.500 | $1.00 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.7 text-to-video (wan2.7-t2v) | Alibaba Cloud Model Studio | 720p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 3.0 | fal.ai | 720p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://fal.ai/models/alibaba/wan-3.0/text-to-video) |  |
| Wan 3.0 (hosted by Runway) | Runway API | 720p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Wan 3.0 (wan3.0-video) | Alibaba Cloud Model Studio | 720p | n/a | $0.100 | $0.500 | $1.00 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) | promo |
| Wan 3.0 | Replicate | 1080p | n/a | $0.140 | $0.700 | $1.40 | high | [link](https://replicate.com/alibaba/wan-3) |  |
| Wan 3.0 Prime | fal.ai | 720p | n/a | $0.140 | $0.700 | $1.40 | high | [link](https://fal.ai/models/alibaba/wan-3.0-prime/text-to-video) |  |
| Wan 3.0 Prime (wan3.0-video-prime) | Alibaba Cloud Model Studio | 720p | n/a | $0.140 | $0.700 | $1.40 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.5 (text-to-video) | Replicate | 1080p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://replicate.com/wan-video/wan-2.5-t2v) |  |
| Wan 2.5 Preview | fal.ai | 1080p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://fal.ai/models/fal-ai/wan-25-preview/text-to-video) |  |
| Wan 2.5 text-to-video preview (wan2.5-t2v-preview) | Alibaba Cloud Model Studio | 1080p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.6 | fal.ai | 1080p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://fal.ai/models/wan/v2.6/text-to-video) |  |
| Wan 2.6 image-to-video (wan2.6-i2v) | Alibaba Cloud Model Studio | 1080p | yes | $0.150 | $0.750 | $1.50 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.6 text-to-video (wan2.6-t2v) | Alibaba Cloud Model Studio | 1080p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.7 | fal.ai | 1080p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://fal.ai/models/fal-ai/wan/v2.7/text-to-video) |  |
| Wan 2.7 (image-to-video) | Replicate | 1080p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://replicate.com/wan-video/wan-2.7-i2v) |  |
| Wan 2.7 image-to-video (wan2.7-i2v) | Alibaba Cloud Model Studio | 1080p | yes | $0.150 | $0.750 | $1.50 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 2.7 text-to-video (wan2.7-t2v) | Alibaba Cloud Model Studio | 1080p | n/a | $0.150 | $0.750 | $1.50 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |
| Wan 3.0 | fal.ai | 1080p | n/a | $0.200 | $1.00 | $2.00 | high | [link](https://fal.ai/models/alibaba/wan-3.0/text-to-video) |  |
| Wan 3.0 (hosted by Runway) | Runway API | 1080p | n/a | $0.200 | $1.00 | $2.00 | high | [link](https://docs.dev.runwayml.com/guides/pricing/) |  |
| Wan 3.0 (wan3.0-video) | Alibaba Cloud Model Studio | 1080p | n/a | $0.200 | $1.00 | $2.00 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) | promo |
| Wan 3.0 Prime | fal.ai | 1080p | n/a | $0.280 | $1.40 | $2.80 | high | [link](https://fal.ai/models/alibaba/wan-3.0-prime/text-to-video) |  |
| Wan 3.0 Prime (wan3.0-video-prime) | Alibaba Cloud Model Studio | 1080p | n/a | $0.280 | $1.40 | $2.80 | high | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |  |

</details>

<!-- TABLE:END -->

## Method and normalization rules

- **Unit.** `usd_per_second` is the price of one second of generated output. `usd_per_5s` and `usd_per_10s` are exact multiples (5x and 10x), provided for convenience.
- **Per-second prices** are copied as published.
- **Per-clip prices** (some Hailuo and Luma tiers) are divided by the clip length.
- **Token prices** (Seedance on BytePlus, Pika, fal.ai) use the vendor's own formula: `tokens = width x height x frame rate x duration / 1024`, at 24 fps and 16:9 frame sizes (854x480, 1280x720, 1920x1080, 3840x2160). Where the vendor prints a 5-second example price, that figure divided by 5 is used. The rate and formula are in `assumptions`.
- **Credits.** Runway credits are $0.01 each (stated in its docs). Luma publishes credits only; $0.003 per credit is inferred from the examples on its own pricing page, so those rows are `medium` confidence. Kling states 1 Unit = $0.14.
- **Unit "count".** Google Vertex AI prints video prices per "1 count". This is read as one second of video (matching Veo's per-second history); rows are `medium` confidence.
- **Resolution.** Where a page names tiers instead of pixels (for example Kling Standard / Pro) the mapping is written in `assumptions`. If a page does not state a resolution, it is recorded as `unspecified`.
- **Audio.** `true` means the price covers output with audio, `false` a silent-video price, `n/a` that the page does not say or does not price it separately.
- **Promotions.** The price payable on the check date is recorded. When a time-limited discount applies, `promotion` is `true` and the details are in `assumptions`.
- **Discontinued models** are kept and marked (`status: discontinued`) as historical reference; they are not buyable.
- **Confidence.** `high` = read directly from an official page with arithmetic only; `medium` = a unit, resolution or credit value had to be interpreted; `low` = indirect or partial source.
- **Marketplaces.** fal.ai and Replicate rows use the price shown on the model page at the check date. Marketplace prices can differ from the vendor's own price for the same model.

## Limits

- **List price is not real cost.** Failed generations, retries, moderation rejections, discarded takes, minimum charges, input-video charges and volume or enterprise discounts are not included. What you spend per *usable* second is usually higher than the list price suggests.
- Not every model or provider is covered, and some official pages could not be read reliably (see below). Missing is better than guessed.
- Prices move often. Always click through to the source before budgeting.
- Roadmap: a "cost per usable second" measurement (list price adjusted for real-world success rates), alongside the open-source tool [clipcheck](https://github.com/klakix-ai/clipcheck).

### Known gaps at the check date

- Vidu's own platform prices only in credits/RMB; Vidu appears here through fal.ai and Replicate.
- LTX and PixVerse official API price pages were not readable; LTX appears through fal.ai only, PixVerse through fal.ai and Replicate.
- Pika is listed for its Seedance 2.5 resale price; its own models were not priced on a page we could read.
- Higgsfield rows are partial ("from" prices and an older comparison table), hence `medium` and `low` confidence.
- Kling 4.0 is not on Kling's static pricing snapshot; it appears via Runway, fal.ai and Replicate.
- OpenAI Sora 2 was shut down on 2026-09-24; its rows are historical.

## Contributing

Pull requests are welcome: new rows, corrections, and removals of stale prices. **A source URL is required** for every change. See [CONTRIBUTING.md](CONTRIBUTING.md) for the rules and the two commands that must pass:

```
python scripts/build.py && python scripts/validate.py
```

## License

- Data (`data/`, tables in this README): [CC BY 4.0](LICENSE).
- Scripts (`scripts/`): MIT, see [LICENSE-CODE](LICENSE-CODE).

Attribution example:

> AI Video Pricing by Klakix (https://klakix.com/ai-video-pricing), CC BY 4.0

Maintained by Klakix (https://klakix.com/?utm_source=github&utm_medium=readme&utm_campaign=ai-video-pricing).
