# ReadmeGenerator

Automated README generation pipeline: ingest a GitHub repo into a token-budgeted text file, optionally fine-tune a local LLM on (code → README) pairs, then evaluate the generated docs against ground truth.

---

## Files

### `repo_ingest.py`

CLI tool that is the first step in the pipeline. Given one or more GitHub repos it:

1. Clones (or zip-downloads) the repo into a temp directory.
2. Scores every file by priority tier — manifests and deploy configs first, then CI workflows, root-level configs, likely entrypoints, then everything else.
3. Filters noise: vendored deps, build outputs, binaries, minified assets, generated stubs, lock files, etc.
4. For large source files (> 150 lines) applies **structural extraction** — Python files use the built-in `ast` module; JS/TS/Java/Go/Rust/Kotlin files use a regex skeleton extractor; tree-sitter is used instead if its grammar packages are installed.
5. Enforces a **total token budget** so the output never overwhelms a context window.
6. Writes two files per repo: the original `README.md` (ground truth) and a `parsed_code.txt` (model input).

Also exposes a `chunk` sub-command that splits a `parsed_code.txt` into overlapping JSONL chunks for RAG pipelines.

### `readme_generator.ipynb`

Single-repo generation and eval notebook, designed to run on Google Colab. Supports Gemini (Google AI Studio), Hugging Face Transformers models, and GGUF models via llama-cpp-python. For a given `parsed_code.txt` it generates a README and scores it with ROUGE-L, GPT-2 perplexity, an LLM rubric (1–5), and an LLM win-rate judge (A vs B).

### `readme_generator_colab.ipynb`

Batch generation and eval notebook. Processes every `parsed_code.txt` in `out/` against both a baseline model and the fine-tuned model, writing results to separate output folders. Evaluation covers ROUGE-L, perplexity, rubric scoring, and head-to-head win-rate comparisons (finetuned vs baseline, finetuned vs Gemma, etc.) using a judge LLM via OpenRouter.

### `readme_model_finetune.ipynb`

Fine-tuning notebook. Reads `(parsed_code.txt, README.md)` pairs from `train/`, formats them as instruction–response prompts, and fine-tunes `Qwen3-4B-Instruct` with QLoRA (4-bit quantization, LoRA rank 8). Merges the adapters back into the base weights, then converts the merged model to a GGUF file via llama.cpp for local inference.

---

## Folder structure

```
ReadmeGenerator/
├── repo_ingest.py               # CLI ingest + chunk tool
├── readme_generator.ipynb       # Single-repo generation & eval (Colab)
├── readme_generator_colab.ipynb # Batch generation & eval (Colab)
├── readme_model_finetune.ipynb  # QLoRA fine-tune + GGUF export (Colab)
├── requirements.txt
│
├── train/                       # Fine-tuning dataset
│   ├── <repo>_parsed_code.txt   # Model input (repo_ingest.py output)
│   └── <repo>_README.md         # Ground truth label
│
├── out/                         # Evaluation dataset (same format as train/)
│   ├── <repo>_parsed_code.txt
│   └── <repo>_README.md
│
├── llm_output/                  # Single test generation output
├── llm_output_baseline/         # Baseline Qwen-generated READMEs
├── llm_output_finetuned/        # Fine-tuned Qwen-generated READMEs
├── gemma_output_baseline/       # Gemma baseline READMEs (via OpenRouter)
│
└── eval_results/                # Plain-text evaluation reports
    ├── baseline_eval_report.txt
    ├── finetuned_eval_report.txt
    ├── gemma_baseline_eval_report.txt
    └── ...
```

---

## Running `repo_ingest.py`

### Installation

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install requests tiktoken
```

`tiktoken` is optional — token counts will show `N/A` without it. To enable tree-sitter structural extraction (optional upgrade over the built-in regex/ast extractors):

```powershell
pip install tree-sitter tree-sitter-python tree-sitter-javascript tree-sitter-typescript
```

---

### `ingest` — clone and parse a repo

```
python repo_ingest.py ingest <user/repo> [user/repo ...] [options]
```

| Option | Default | Description |
|---|---|---|
| `--out DIR` | `./out` | Output directory |
| `--prefix STR` | `user_repo_` | Prefix for output filenames |
| `--max-lines N` | `3000` | Per-file line cap (config files exempt) |
| `--max-bytes N` | `2000000` | Per-file byte cap (config files get 5×) |
| `--budget-tokens N` | `80000` | Total token budget for the output. Tier-0 manifests always bypass this. |
| `--no-ast` | off | Disable structural extraction; include raw file content |

**Examples:**


```powershell
# Get full test data parses
python repo_ingest.py ingest pallets/click psf/requests-html sindresorhus/got psf/requests apache/parquet-format apache/nano apache/rocketmq-docker apache/cordova-plugin-splashscreen apache/openserverless apache/flink-docker apache/skywalking-eyes apache/couchdb-docker apache/predictionio-sdk-ruby  --out ./out

#Get full train data parses
python repo_ingest.py ingest apache/airflow-client-go apache/bahir-flink apache/calcite-avatica-go apache/cordova-plugin-battery-status apache/cordova-plugin-device apache/cordova-plugin-geolocation apache/cordova-plugin-statusbar apache/cordova-plugin-vibration apache/dubbo-go-hessian2 apache/dubbo-proxy apache/dubbo-python apache/dubbo-rust apache/flink-connector-jdbc apache/hbase-connectors apache/incubator-retired-gossip apache/maven-wrapper apache/paimon-rust apache/predictionio-sdk-ruby apache/rocketmq-client-go apache/rocketmq-client-nodejs apache/rocketmq-client-python apache/shardingsphere-elasticjob-ui apache/skywalking-client-js apache/skywalking-eyes apache/skywalking-nodejs apache/skywalking-python apache/spark-connect-go apache/tika-docker apache/dubbo-spring-boot-project apache/rocketmq-spring apache/parquet-format apache/nano apache/flink-training apache/apisix-docker apache/rocketmq-docker apache/servicecomb-mesher apache/cordova-plugin-splashscreen apache/cordova-plugin-wkwebview-engine apache/cordova-plugin-file-transfer apache/openserverless apache/skywalking-helm apache/servicecomb-samples apache/cordova-plugin-network-information apache/cordova-plugin-whitelist apache/cordova-plugin-media apache/doris-flink-connector apache/rocketmq-operator apache/skywalking-go apache/cordova apache/cordova-node-xcode apache/cordova-plugin-console apache/cordova-plugin-contacts apache/cordova-plugin-dialogs apache/cordova-plugin-file apache/cordova-plugin-media-capture apache/cordova-plugin-screen-orientation apache/openwhisk-deploy-kube apache/openwhisk-external-resources apache/skywalking-swck apache/skywalking-showcase apache/skywalking-satellite apache/skywalking-rover apache/skywalking-nginx-lua apache/rocketmq-exporter apache/rocketmq-mqtt apache/rocketmq-flink apache/apisix-go-plugin-runner apache/apisix-java-plugin-runner apache/oltu apache/opendal-reqsign apache/maven-build-cache-extension apache/maven-sources apache/tomcat-jakartaee-migration apache/flink-playgrounds apache/flink-benchmarks apache/nifi-minifi apache/mynewt-mcumgr apache/doris-manager apache/incubator-pagespeed-cpanel apache/pulsar-helm-chart apache/shardingsphere-elasticjob-example apache/skywalking-php apache/skywalking-data-collect-protocol apache/predictionio-sdk-python apache/predictionio-sdk-java apache/predictionio-sdk-php apache/hbase-operator-tools apache/dubbo-rpc-jsonrpc apache/flink-docker apache/couchdb-docker apache/skywalking-docker apache/spark-kubernetes-operator apache/datafusion-ray apache/doris-spark-connector apache/bahir apache/flink-shaded apache/incubator-crail apache/maven-compiler-plugin apache/maven-shade-plugin apache/spark-docker apache/tvm-vta apache/brooklyn apache/commons-cli apache/commons-codec apache/commons-csv apache/commons-io apache/commons-lang apache/commons-text apache/commons-compress apache/commons-configuration apache/commons-validator apache/commons-net apache/commons-email apache/commons-fileupload apache/commons-rng apache/commons-math apache/commons-collections apache/commons-pool apache/commons-dbcp apache/commons-beanutils --out ./train2


# Basic ingest
python repo_ingest.py ingest pallets/click

# Multiple repos with a custom output dir
python repo_ingest.py ingest apache/kafka apache/flink --out ./train

# Specific branch, tighter budget
python repo_ingest.py ingest microsoft/TypeScript/main --budget-tokens 60000

# Disable structural extraction (full raw source, larger output)
python repo_ingest.py ingest pallets/flask --no-ast
```

Each run produces two files in `--out`:
- `<prefix>README.md` — the repo's original README (ground truth, not fed to the model)
- `<prefix>parsed_code.txt` — priority-filtered, token-budgeted source text (model input)

---

### `chunk` — split a parsed file into overlapping chunks

```
python repo_ingest.py chunk <parsed_code.txt> [options]
```

| Option | Default | Description |
|---|---|---|
| `--out FILE` | `./out/chunks.jsonl` | Output JSONL file |
| `--chunk-tokens N` | `800` | Approximate tokens per chunk |
| `--overlap N` | `80` | Approximate token overlap between chunks |

**Example:**

```powershell
python repo_ingest.py chunk ./out/pallets_click_parsed_code.txt --out ./out/click_chunks.jsonl
```

Each line in the output JSONL has `{ "file": "...", "chunk": "...", "chunk_id": 0 }`.

---

## Pipeline overview

```
GitHub repo
    │
    ▼
repo_ingest.py ingest          →  out/<repo>_parsed_code.txt
                                   out/<repo>_README.md
    │
    ├──► readme_generator.ipynb          (single-repo test generation + eval)
    │
    └──► readme_generator_colab.ipynb    (batch generation + eval)
              ▲
              │  fine-tuned model (GGUF)
    readme_model_finetune.ipynb          (train/ → QLoRA → GGUF)
```
