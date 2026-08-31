<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg">
    <img alt="Nadeem Khan — Senior Software Engineer, AI Systems & Platform Engineering" src="assets/header-light.svg" width="100%">
  </picture>
</p>

<p align="center">
  <a href="https://codewithnk.com/"><img alt="Website" src="https://img.shields.io/badge/Website-codewithnk.com-1F6FEB?logo=googlechrome&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/nadeem-khan-75135210a/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white"></a>
  <a href="https://medium.com/learnwithnk"><img alt="Medium" src="https://img.shields.io/badge/Medium-12100E?logo=medium&logoColor=white"></a>
  <a href="https://x.com/codewithnk"><img alt="X" src="https://img.shields.io/badge/X-black.svg?logo=X&logoColor=white"></a>
  <a href="https://stackoverflow.com/users/8639962/nadeem-khan"><img alt="Stack Overflow" src="https://img.shields.io/badge/Stack%20Overflow-FE7A16?logo=stack-overflow&logoColor=white"></a>
  <a href="mailto:codewithnk@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white"></a>
</p>

---

## 🚀 What I'm Building

| Project | What it does | Stack |
| :--- | :--- | :--- |
| **[nl2sql](https://github.com/nadeem4/nl2sql)** | Enterprise-grade multi-agent NL→SQL system — schema retrieval, validation, and full observability for SQL that is accurate, safe, and deterministic. | Python · Multi-agent · Retrieval |
| **[medalflow](https://github.com/nadeem4/medalflow)** | dbt, but in Python classes. Declare Bronze/Silver/Gold models as classes; MedalFlow parses your SQL for dependencies and compiles a staged execution plan. | Python · Data platform |
| **[loglens](https://github.com/nadeem4/loglens)** | LLM-powered analysis bolted onto stdlib `logging` — severity-based model routing, PII scrubbing, async micro-batching, circuit breaking, Prometheus metrics. | Python · Observability |
| **[post_training](https://github.com/nadeem4/post_training)** | Small, runnable implementations of LLM post-training and alignment — RL fundamentals through DPO, RLHF, and RLAIF. | Python · PyTorch · RL |

<details>
<summary><b>Earlier work that people still use</b></summary>

<br>

| Project | Why it exists |
| :--- | :--- |
| **[microservice_demo](https://github.com/nadeem4/microservice_demo)** | A clean, minimal Spring Boot microservice reference — the version I wanted when I was learning the pattern. |
| **[spring_boot_multi_module_framework](https://github.com/nadeem4/spring_boot_multi_module_framework)** | Bootstraps a multi-module Spring Boot project so teams skip the first week of scaffolding. |
| **[chess_engine_using_python](https://github.com/nadeem4/chess_engine_using_python)** | Minimax, alpha-beta pruning, and quiescence search, written to be read rather than to win. |
| **[mini-gpt](https://github.com/nadeem4/mini-gpt)** | A decoder-only Transformer in pure PyTorch, stripped to the pieces that actually matter. |
| **[aurora](https://github.com/nadeem4/aurora)** | Semantic search engine on FastAPI and Sentence Transformers. |

</details>

---

## 📈 Impact

- Cut cloud spend **~30%** through architecture and execution-path optimization
- Reduced engineer onboarding from **months to weeks** via platform automation
- Delivered **end-to-end AI and data platforms** with explicit reliability guarantees
- Consistent bias toward **correctness, observability, and system clarity**

---

## 🧠 Technical Focus

<p align="center">
  <b>Languages &amp; Frameworks</b><br>
  <sub>Python · Java · TypeScript · Spring · Node.js · FastAPI · PyTorch · Angular</sub><br>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=python%2Cjava%2Cts%2Cspring%2Cnodejs%2Cfastapi%2Cpytorch%2Cangular&theme=dark">
    <img alt="Python, Java, TypeScript, Spring, Node.js, FastAPI, PyTorch, Angular" src="https://skillicons.dev/icons?i=python%2Cjava%2Cts%2Cspring%2Cnodejs%2Cfastapi%2Cpytorch%2Cangular&theme=light">
  </picture>
</p>

<p align="center">
  <b>Platform &amp; Infrastructure</b><br>
  <sub>Kubernetes · Docker · Azure · GitHub Actions · Postgres · Grafana · Git · Linux</sub><br>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=kubernetes%2Cdocker%2Cazure%2Cgithubactions%2Cpostgres%2Cgrafana%2Cgit%2Clinux&theme=dark">
    <img alt="Kubernetes, Docker, Azure, GitHub Actions, Postgres, Grafana, Git, Linux" src="https://skillicons.dev/icons?i=kubernetes%2Cdocker%2Cazure%2Cgithubactions%2Cpostgres%2Cgrafana%2Cgit%2Clinux&theme=light">
  </picture>
</p>

**AI Systems** — LLM inference efficiency · agentic systems · retrieval · execution feedback loops · cost/latency tradeoffs · agent safety

**Platform & Distributed Systems** — serverless · CI/CD · observability · private networking · fault tolerance

**Data Systems** — ETL platforms · lakehouse architectures · Apache Spark · SQL engines · cost optimization

<details>
<summary><b>How I think about each of these</b></summary>

<br>

**AI Systems.** The interesting problems are not in the model, they are around it: making a non-deterministic component behave predictably inside a system that has to be correct. Retrieval quality, validation layers, execution feedback, and hard safety constraints do more for output quality than prompt tuning does. Inference cost and latency are design inputs, not afterthoughts.

**Platform & Distributed Systems.** A platform succeeds when it makes the right thing the easy thing. Most of the value is in defaults, guardrails, and paved roads — not features. Failure modes should be boring and well-understood before traffic arrives.

**Data Systems.** Lineage and reproducibility beat cleverness. A pipeline you can explain, replay, and cost-attribute is worth more than a faster one you cannot reason about.

</details>

---

## ✍️ Latest Writing

<!-- BLOG-POST-LIST:START -->
- [pgvector Internals Overview: How Postgres Learned to Speak Vector](https://medium.com/learnwithnk/pgvector-internals-overview-how-postgres-learned-to-speak-vector-5a8c6f11b571) &nbsp;<sub>Aug 30, 2026</sub>
- [Hybrid Search: Combining Vector Similarity with Metadata Filters and Keyword Search](https://medium.com/learnwithnk/hybrid-search-combining-vector-similarity-with-metadata-filters-and-keyword-search-cb5f7cc419ad) &nbsp;<sub>Aug 29, 2026</sub>
- [Distributed Systems Concerns: Replication, Consistency, and Query Routing](https://medium.com/learnwithnk/distributed-systems-concerns-replication-consistency-and-query-routing-97f30840e7a7) &nbsp;<sub>Aug 27, 2026</sub>
- [Sharding and Partitioning at Scale: Splitting Billions of Vectors Across Machines](https://medium.com/learnwithnk/sharding-and-partitioning-at-scale-splitting-billions-of-vectors-across-machines-3ccebd409078) &nbsp;<sub>Aug 26, 2026</sub>
- [Storage Architecture: Memory, Disk, and Memory-Mapped Layouts at Billion-Vector Scale](https://medium.com/learnwithnk/storage-architecture-memory-disk-and-memory-mapped-layouts-at-billion-vector-scale-4c094bcadde6) &nbsp;<sub>Aug 26, 2026</sub><!-- BLOG-POST-LIST:END -->

More at **[medium.com/learnwithnk](https://medium.com/learnwithnk)** · **[codewithnk.com](https://codewithnk.com/)**

---

## 📊 GitHub

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com/?user=nadeem4&theme=dark&hide_border=true&date_format=M%20j%5B%2C%20Y%5D">
    <img alt="GitHub streak stats" src="https://streak-stats.demolab.com/?user=nadeem4&theme=default&hide_border=true&date_format=M%20j%5B%2C%20Y%5D" height="180">
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=nadeem4&theme=github_dark">
    <img alt="Repositories per language" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=nadeem4&theme=default" height="180">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=nadeem4&theme=github_dark">
    <img alt="Most committed languages" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=nadeem4&theme=default" height="180">
  </picture>
</p>

---

## 🧩 Engineering Philosophy

- Determinism before scale
- Observability before optimization
- Clear interfaces enable fast, safe systems
- Prefer boring, reliable systems over clever hacks

---

<p align="center">
  <sub>Reach me at <a href="mailto:codewithnk@gmail.com">codewithnk@gmail.com</a></sub>
</p>
