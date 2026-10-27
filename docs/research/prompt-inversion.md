# Prompt inversion and skill reconstruction: research notes

Checked 2026-10-26. Primary sources only: arXiv pages, ACL/ICLR/USENIX pages, and two cloned repos.
Repos read locally: [collinzrj/output2prompt](https://github.com/collinzrj/output2prompt) at `65d3bf6`, [morluto/rea](https://github.com/morluto/rea) at `c2b0c95`.
Anything marked **UNVERIFIED** was seen only in a search snippet or abstract without numbers.


## 1. TL;DR

- Black-box prompt inversion from plain outputs works for meaning, not wording. output2prompt gets cosine 96.7 but exact match 21.1% on Llama-2 Chat from 64 outputs ([arXiv 2405.15012](https://arxiv.org/abs/2405.15012)). Aim for a functionally equivalent skill, not the original text.
- More outputs help, then plateau. o2p cosine goes 0.930 (1 output) to 0.967 (64) on Llama-2; BLEU 0.30 to 0.57 ([NUMBERS.md](https://github.com/collinzrj/output2prompt/blob/main/NUMBERS.md)). 256 outputs add almost nothing.
- Training-free loops are now competitive. RPE uses 5 outputs plus a generate, replay, compare, revise loop (ROUGE-1 vs originals, 5 iterations, about 230 LLM calls) and beats output2prompt by 6.2% to 10.9% cosine ([arXiv 2411.06729](https://arxiv.org/abs/2411.06729)). This is the template for our tool.
- "Negate" maps to PRSA's pruning step. It masks words tied to the user input and replaces them with placeholders so the stolen prompt generalizes ([arXiv 2402.19200](https://arxiv.org/abs/2402.19200)). Keep what is invariant across outputs; strip what varies per post.
- rea is a binary/app reverse-engineering MCP, not a prompt tool. It never uses the words "negate" or "neglect". Its transferable principles are: separate observation, inference and unknown; absence proves nothing outside the examined scope; verify against an independent oracle; a surface match (size, length) is a diagnostic, not acceptance; optimise only measured, completed tasks.


## 2. output2prompt deep notes

Paper: "Extracting Prompts by Inverting LLM Outputs", Collin Zhang, John X. Morris, Vitaly Shmatikov. EMNLP 2024 main, pp. 14753 to 14777 ([ACL 2024.emnlp-main.819](https://aclanthology.org/2024.emnlp-main.819/), [arXiv 2405.15012](https://arxiv.org/abs/2405.15012), [HTML](https://arxiv.org/html/2405.15012)).

### Problem setup
- Input: N text outputs from an LLM for normal queries. No logits. No jailbreak or adversarial queries.
- Target: the user prompt, or the hidden system prompt of an LLM app (GPTs).
- Claim: because queries are normal, detection and filtering defenses do not apply. Authors state "LLM prompts should not be seen as secrets" (Potential Risks section).

### Method
- Inverter: T5-base encoder-decoder, 222M params, fine-tuned. Greedy decoding at inference.
- Sparse encoding: each output is encoded alone; the decoder cross-attends to the concatenation of all encoded outputs.
  - Memory O(n·l²) instead of O(n²·l²) for full self-attention over all outputs.
  - Code: `T5SparseEncoder.my_encoder`, mode `just_sparse` reshapes `(batch, n_outputs, len)` to `(batch*n, len)`, encodes, then concatenates hidden states to `(batch, n*len, d)` ([my_t5_base.py L33 to L49](https://github.com/collinzrj/output2prompt/blob/main/vec2text/models/my_t5_base.py)). Other modes in code: `single_sentence`, `full_attention`, `last_token`, `average_pooling`.
  - Appendix A (16 outputs, len 64): sparse vs full attention. Cosine 96.7 vs 97.0, BLEU 56.8 vs 60.6, memory 7.4 GB vs 29.6 GB, 4.98 vs 1.22 batches/s. Full attention cannot fit 128 outputs on a 48 GB A40.
- Training: 64 outputs per prompt. Max output length 64 tokens (user prompts) or 256 (system prompts). 3 epochs, Adam, lr 2e-4, bf16.
- Sampling the target: temperature 1.5 for user prompts (Llama-2 7B and Llama-2 Chat 7B). Dropping to temperature 1.0 lowers cosine 96.7 to 94.7 and BLEU 56.9 to 45.0. Diversity in outputs helps inversion.
- System prompts: GPT-3.5 at temperature 0.8, 44 fixed normal queries giving 64 non-repeating outputs.
- Repo usage tip for real GPTs: ask 4 questions, 16 answers each, 64 outputs total ("Give me 16 short sentences that best describe yourself", "16 example questions", "16 scenarios", "16 sentences comparing yourself with ChatGPT") ([README](https://github.com/collinzrj/output2prompt/blob/main/README.md)).
- Pretrained inverters and datasets on Zenodo record 12759549. Requires `transformers==4.36.0` per README.

### Data
- User prompts: Instructions-2M (30K train, 1K test). Zero-shot and finetune transfer sets: ShareGPT and Unnatural Instructions (100 finetune, 400 test each).
- System prompts: Synthetic GPTs, about 26K prompts generated from real GPT names and descriptions (25K train, 1K test). Real GPTs, 79 English prompts (50 finetune, 29 test). Awesome-ChatGPT-Prompts, 153 (50 finetune, 103 test).
- Lesson for us: they bootstrapped training data synthetically from names and descriptions. We can do the same: write known skills, generate outputs, train or tune on the pairs.

### Metrics
- BLEU, exact match, token F1, cosine similarity (OpenAI text-embedding-ada-002).
- "LLM Eval": GPT-4o judges whether two prompts would produce similar outputs (YES/NO/UNCLEAR). Authors say it is noisy: one extraction at cosine 85.7 got YES, another at 94.6 got NO (Appendix H).
- No human study.

### Key numbers (Instructions-2M; cosine / BLEU / exact / token F1)
| Target | Method | Cos | BLEU | Exact | F1 |
|---|---|---|---|---|---|
| Llama-2 Chat | output2prompt | 96.7 | 56.8 | 21.1 | 79.5 |
| Llama-2 Chat | logit2text (Morris 2023) | 93.5 | 53.4 | 26.6 | 75.7 |
| Llama-2 Chat | Jailbreak | 85.8 | 11.1 | 0.0 | 37.3 |
| Llama-2 Chat | Jailbreak oracle | 92.9 | 31.2 | 0.0 | 60.1 |
| Llama-2 Chat | LLM few-shot | 94.1 | 25.9 | 4.0 | 61.2 |
| Llama-2 base | output2prompt | 96.7 | 67.7 | 41.0 | 83.8 |
| Llama-2 base | logit2text | 94.0 | 55.6 | 28.5 | 77.3 |

- Note: logit2text has higher exact match on Chat (26.6 vs 21.1). Logits carry more literal detail; outputs carry meaning.

### Number of outputs (from repo NUMBERS.md, Figure 2 data)
| N outputs | Llama cos | GPT-3.5 cos | Llama BLEU | GPT-3.5 BLEU |
|---|---|---|---|---|
| 1 | 0.930 | 0.887 | 0.299 | 0.157 |
| 4 | 0.951 | 0.907 | 0.422 | 0.231 |
| 16 | 0.961 | 0.921 | 0.517 | 0.287 |
| 64 | 0.967 | 0.930 | 0.569 | 0.334 |

- With 2 outputs cosine already beats logit2text. At 256 outputs: BLEU 56.8 to 57.7, cosine 96.8 to 96.5. Plateau near 64.

### Transfer across LLMs
- User-prompt inverter trained on Llama-2 Chat outputs, tested on others: cosine GPT-3.5 93.0, Mistral 7B Instruct 93.4, Gemma 2B 92.4. BLEU falls to about 31 to 33.
- logit2text does not transfer (vocabularies differ).
- System-prompt inverter (trained on GPT-3.5 outputs), cosine on other targets: GPT-4 97.2, Llama-3-70B 97.9, Mixtral-8x22B 98.4, Qwen1.5-110B 97.3.
- Dataset shift: ShareGPT 84.2 zero-shot, 88.8 after 50-sample finetune. Unnatural 83.3 to 94.6. Awesome 83.9 to 92.0. Real GPTs 89.9 zero-shot, 88.8 finetuned.
- Synthetic GPTs test: cosine 98.1, BLEU 36.8, F1 73.8, LLM Eval 99.0.

### Prompt length
- Ground-truth prompts of about 108, 192, 277, 433 tokens give cosine 97.8, 97.8, 97.7, 97.4. Extractions cluster at 170 to 200 tokens. Long prompts get compressed.

### Limitations (stated)
- Exact recovery not guaranteed. In-context examples inside the prompt are often not reproduced.
- Conditional behaviour (their "CHANGE" keyword example) is only partly recovered, because outputs only show the branches that fired.
- Functional equivalence is measured by a noisy LLM judge, not by replaying the prompt.

### What is recovered
- Functional and semantic content: role, task, tone, topics. Not literal wording, not hidden few-shot examples, not rarely triggered rules.


## 3. Related work

| Name | Input | Method | Recovers | Key number | Link |
|---|---|---|---|---|---|
| Language Model Inversion (Morris et al., ICLR 2024). o2p calls it logit2text | Next-token probability vector | T5 inverter conditioned on unrolled logits | Exact prompt text | Llama-2 7B: BLEU 59, token F1 78, 27% exact | [arXiv 2311.13647](https://arxiv.org/abs/2311.13647), [ICLR](https://iclr.cc/virtual/2024/poster/17623) |
| PILS (Nazir, Finlayson, Morris et al., 2025) | Logprob sequences over many steps | Linear compression of next-token distributions | Exact prompt, system messages | Exact recovery 2x to 3.5x prior SOTA; one set 17% to 60% | [arXiv 2506.17090](https://arxiv.org/abs/2506.17090) |
| vec2text (Morris et al., EMNLP 2023) | Text embedding vector | Iterative correct and re-embed | Exact text | 92% of 32-token inputs exactly | [arXiv 2310.06816](https://arxiv.org/abs/2310.06816) |
| output2prompt (Zhang, Morris, Shmatikov, EMNLP 2024) | 1 to 64+ text outputs | T5-base sparse encoder inverter | Functional prompt | Cos 96.7, exact 21.1% | [arXiv 2405.15012](https://arxiv.org/abs/2405.15012) |
| Effective Prompt Extraction (Zhang, Carlini, Ippolito) | Responses to attack queries | 105 attack queries (5 seed, 100 GPT-4 paraphrases) plus DeBERTa verifier | Verbatim system prompt | Approx match 67.9% to 95.2% across 11 models; GPT-4 86.0%. Verifier precision >90% (Alpaca 80%). 5-gram filter drops some to 0% | [arXiv 2307.06865](https://arxiv.org/abs/2307.06865) |
| PRSA (Yang et al., USENIX Security 2025) | 1 input/output pair, or few app chats | LLM generation with "prompt attention" on output differences, then pruning of input-tied words to placeholders | Functional surrogate prompt | PromptBase GPT-4 ASR 46.1% vs 17.8% baseline. GPT Store ASR 52% vs 39% (output2prompt). Cost 1.3% to 12.3% of prompt price | [arXiv 2402.19200](https://arxiv.org/abs/2402.19200) |
| Reverse Prompt Engineering, RPE (Li, Klabjan, EMNLP 2025) | 5 text outputs | Training-free LLM loop: 5 candidates, replay, ROUGE-1 vs originals, critique diffs, revise, 5 iterations | Functional prompt, system prompt | +6.2% (Llama-2 Chat) and +10.9% (GPT-3.5) cosine over o2p; system prompts +5.8% over o2p with 64 outputs. About 230 calls per recovery | [arXiv 2411.06729](https://arxiv.org/abs/2411.06729) |
| PTP (Suhail et al., Jul 2026) | Responses only | Inverse LM trained from scratch with previous-token prediction on target-generated data | Near-exact prompt, multiple candidates | Abstract gives no numbers. **UNVERIFIED numbers** | [arXiv 2607.29378](https://arxiv.org/abs/2607.29378) |
| Inversion learning for NLG eval prompts (Hong et al., TACL) | 1 evaluation sample | Learn output to instruction mapping | Model-specific eval prompt | Abstract gives no numbers | [arXiv 2504.21117](https://arxiv.org/abs/2504.21117) |
| PromptStealer (Shen et al.) | Generated image | BLIP subject generator plus ML-Decoder modifier detector | T2I prompt: subject plus modifiers | Semantic sim 0.70 vs CLIP Interrogator 0.52; modifier Jaccard 0.43 vs 0.01; human 4.45/5. Lexica set 61,467 pairs | [arXiv 2302.09923](https://arxiv.org/abs/2302.09923) |
| PEZ, Hard Prompts Made Easy (Wen et al.) | Image (via CLIP) or text task | Gradient on continuous embeddings, project to nearest tokens | Short readable hard prompt | 8 tokens, CLIP score 0.711 on Lexica vs CLIP Interrogator 0.762 at ~77 tokens and 0.532 at 8 tokens. 16 tokens transfer best | [arXiv 2302.03668](https://arxiv.org/abs/2302.03668) |
| CLIP Interrogator | Image | BLIP caption plus CLIP ranking of candidate terms | T2I prompt | No paper. MIT. 0.6.0 adds BLIP-2. Pipeline details not stated on README page | [GitHub](https://github.com/pharmapsychotic/clip-interrogator) |
| PromptMiner (Li et al., Nov 2025) | Image, black box | RL for subject, fuzzing for style modifiers | T2I prompt | CLIP sim up to 0.958, SBERT up to 0.751; +7.5% CLIP on in-the-wild images | [arXiv 2511.22119](https://arxiv.org/abs/2511.22119) |
| PromptEvolver (Buchnick et al., Apr 2026) | Image, black box | Genetic algorithm over natural-language prompts, VLM-guided | Readable T2I prompt | Abstract gives no numbers | [arXiv 2604.06061](https://arxiv.org/abs/2604.06061) |
| PROVE (Mallick et al., Aug 2026) | Image | Training-free; build prompt from verifiable scene claims, precision-constrained recall | Auditable T2I prompt | Abstract gives no numbers | [arXiv 2608.13671](https://arxiv.org/abs/2608.13671) |
| Cross-Modal Prompt Inversion (Ye et al., USENIX Sec 2025) | Text, image, video outputs | Train inverter, then RL fine-tune | Prompt across modalities | Page gives no numbers. **UNVERIFIED numbers** | [USENIX](https://www.usenix.org/conference/usenixsecurity25/presentation/ye-inversion) |
| VI-Bench (Xie et al., Sep 2026) | AI-generated video | Benchmark; predicted prompt is replayed through the generator | Replayable video prompt (subject, action, scene, style, camera) | 900 human-verified videos; 18 VLMs; best Inversion Score 0.632 | [arXiv 2609.08079](https://arxiv.org/abs/2609.08079) |
| Meta Inverse Prompting for Video Generative Models | Video | Not read | Video prompt | **UNVERIFIED**: seen only as a NeurIPS 2026 poster listing in search | [NeurIPS listing](https://neurips.cc/virtual/2026/poster/150385) |
| APE (Zhou et al.) | Input/output demos | LLM proposes instructions, scored by another LLM, resample | Instruction that reproduces I/O | Human-level or better on 19/24 instruction-induction tasks | [arXiv 2211.01910](https://arxiv.org/abs/2211.01910) |
| OPRO (Yang et al., ICLR 2024) | Task plus scored history | LLM sees past prompts with scores, proposes better ones | Optimised prompt | Up to +8% GSM8K, up to +50% BBH over human prompts | [arXiv 2309.03409](https://arxiv.org/abs/2309.03409) |
| ProTeGi / APO (Pryzant et al., EMNLP 2023) | Prompt plus minibatch errors | Text "gradients" (critiques), edit, beam search plus bandit | Optimised prompt | Up to +31% over initial prompt | [arXiv 2305.03495](https://arxiv.org/abs/2305.03495) |
| DSPy (Khattab et al.) | Program plus metric | Compile declarative modules; bootstrap demos | Prompts and demos per module | >25% over few-shot on GPT-3.5, 65% on llama2-13b-chat | [arXiv 2310.03714](https://arxiv.org/abs/2310.03714) |
| MIPRO (Opsahl-Ong et al., EMNLP 2024) | Multi-stage program plus metric | Surrogate model over instruction and demo choices | Instructions and demos | Wins 5 of 7 programs, up to +13% (Llama-3-8B) | [arXiv 2406.11695](https://arxiv.org/abs/2406.11695) |
| TextGrad (Yuksekgonul et al.) | Any text variable plus loss | Backprop of LLM feedback through a graph | Optimised text components | GPQA 51% to 55% (GPT-4o); +20% relative LeetCode-Hard | [arXiv 2406.07496](https://arxiv.org/abs/2406.07496) |
| GEPA (Agrawal et al., ICLR 2026 oral) | Program plus traces plus metric | Reflect on trajectories, propose edits, keep Pareto frontier | Optimised prompts | +6% avg (up to +20%) over GRPO with up to 35x fewer rollouts; >10% over MIPROv2 | [arXiv 2507.19457](https://arxiv.org/abs/2507.19457) |

Takeaways from the table:
- Logit or embedding access gives exact text. We only have outputs, so we get function.
- The best output-only methods are loops: propose, replay, compare to originals, revise (RPE, PRSA, PromptEvolver, VI-Bench's replay scoring).
- Decomposition helps: subject vs modifiers (PromptStealer, PromptMiner); input-tied words vs reusable instruction (PRSA). This is the "negate" step.
- No verified 2025/2026 paper targets "agent skill" reconstruction (multi-file instructions, tools, templates). Closest: RPE and PRSA system prompt work. Treat skills as an open problem.


## 4. rea (morluto/rea)

### What it is
- "REA: Reverse Engineer Anything. One MCP for reverse engineering across binaries, applications, and runtime behavior" ([README L6 to L8](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/README.md#L6-L8)).
- Goal: "See a feature you like. Understand how it works, down to the binary level" ([README L10](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/README.md#L10)). Inspect an app without source, explain, show evidence, build a version ([L61 to L63](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/README.md#L61-L63)).
- npm `rea-agents` 6.8.0, MIT, Node 22/24/26. Runs locally. Uses Hopper, Ghidra, IDA, JADX, browsers, captures etc. 30+ target types ([README L189 to L226](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/README.md#L189-L226)).
- It does not handle prompts, LLM outputs, or content. Relevance to us is by analogy only. Site [rea.tools](https://rea.tools/) responded HTTP 200 on 2026-10-26.

### Architecture
- Layers, dependencies flow inward: domain contracts, provider adapters, shared application workflows, CLI/MCP adapters ([AGENTS.md L17](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/AGENTS.md#L17), [docs/architecture.mermaid](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/docs/architecture.mermaid)).
- Every tool returns an "Evidence" record with ID, normalized result, limitations, coverage, unknowns ([evidence-workflows.md L3 to L12](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/.agents/skills/reverse-engineer-anything/references/evidence-workflows.md#L3-L12)).
- Agent workflow is shipped as a skill: `.agents/skills/reverse-engineer-anything/SKILL.md` (509 lines). Separate internal skills for optimisation, tool design, CI audit.

### Pipeline (as documented)
```
 user question about a target
          |
          v
 route target -> pick first tool          (SKILL.md L93-L139)
          |
          v
 summary-first result + Evidence ID       (SKILL.md L395-L413)
          |
          v
 focused follow-up only if a specific question is open
          |
          v
 ledger: observation | inference | unknown (SKILL.md L441-L444, L478-L480)
          |
          v
 reconstruct (write code) -> verify vs original (oracle)
          |                         |
          | pass: keep + evidence   | mismatch: back to investigation
          v                         v
 revisit checklist: answered / partial / unresolved (SKILL.md L482-L485)
```

### Principles, with citations
"Negate / neglect": these words do not appear as principles anywhere in the repo (grep over docs, skills, website, AGENTS.md). The closest real concepts:
- **Absence is not proof.** "An empty result proves absence only within the actually examined scope" ([rea-analysis-optimization SKILL.md L40](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/.agents/skills/rea-analysis-optimization/SKILL.md#L40)). "keep bounded negative searches bounded" ([SKILL.md L484](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/.agents/skills/reverse-engineer-anything/SKILL.md#L482-L485)). "Unresolved identity or applicability must remain unknown rather than be treated as absent" ([AGENTS.md L21](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/AGENTS.md#L21)). `only_left`/`only_right` "do not prove source addition/removal" ([native-function-matching.md L55 to L57](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/docs/native-function-matching.md#L55-L57)).
- **Ignore surface cues.** "do not infer behavior from filenames, strings, or layout alone" ([SKILL.md L466 to L468](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/.agents/skills/reverse-engineer-anything/SKILL.md#L466-L468)). "Exact names establish name correspondence, not unchanged code" ([native-function-matching.md L25](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/docs/native-function-matching.md#L25)).
- **Surface match is a diagnostic, not acceptance.** A 1,825-byte candidate had the target's exact length but 467 differences; "using size as a diagnostic rather than final acceptance" ([reverse-engineering-models.md L150 to L153](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/website/evidence/reverse-engineering-models.md#L150-L153)). Matching frame size "concealed" real differences ([L42 to L44](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/website/evidence/reverse-engineering-models.md#L42-L44)).
- **Negative controls.** Verification notes use deliberate failing inputs to prove a check can fail, e.g. "Five new negative controls fail before correction" (`docs/verification/android-manifest-components-2026-10-24.md` L246); TH08 fix added "deliberately invalid literal declarations" to tests ([touhou-reconstruction-method.md L221 to L222](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/website/evidence/touhou-reconstruction-method.md#L216-L222)).
- **Never upgrade weak results.** "`fail`, `unknown`, `unsupported`, `truncated`, and `skipped` never aggregate to `pass`" ([reconstruction-readiness.md L76 to L77](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/docs/reconstruction-readiness.md#L76-L77)). Reject if "truncation, instability, unavailable authority, or contradiction is labeled equivalent" (L88 to L89). An unrelated observed record "cannot repair a result that cites only inference" ([reconstruction-coverage.md L43 to L45](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/docs/reconstruction-coverage.md#L43-L45)).
- **Separate observation, inference, unknown.** "Every conclusion must distinguish observations, inferences, and unknowns" ([SKILL.md L441](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/.agents/skills/reverse-engineer-anything/SKILL.md#L441-L444)). Track open questions with `record_unknown` ([evidence-workflows.md L38 to L43](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/.agents/skills/reverse-engineer-anything/references/evidence-workflows.md#L38-L43)).
- **Verified claims are scoped.** `verify_reconstruction` "pass covers only declared comparable claims, not global equivalence" ([evidence-workflows.md L61 to L62](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/.agents/skills/reverse-engineer-anything/references/evidence-workflows.md#L61-L62)). Obligation ledgers close only with an owner, fixtures, and a passing verifier ([reconstruction-obligation-ledgers.md L10 to L18](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/docs/reconstruction-obligation-ledgers.md#L10-L18)).

"Optimisation": two real meanings in the repo.
- **Engineering optimisation** of the tool. Order: agent tokens and context, then analysis time, then CPU and memory ([AGENTS.md L43 to L54](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/AGENTS.md#L43-L54)). "Find a concrete source of unnecessary work... A useful outcome can also be a measured decision to leave an implementation alone" ([rea-analysis-optimization SKILL.md L8 to L10](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/.agents/skills/rea-analysis-optimization/SKILL.md#L8-L10)). Use an oracle "independent of the changed implementation" (L35 to L38). Compare completed tasks before and after (L95 to L105). "Smaller JSON alone establishes neither fewer model tokens nor better investigation quality" (L110). Stop "when the demonstrated bottleneck is resolved or further benefit remains speculative" (L116 to L117). Summary-first, no repeated identical calls ([SKILL.md L395 to L413](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/.agents/skills/reverse-engineer-anything/SKILL.md#L395-L413)).
- **Reconstruction loop** (case studies). Agents have broad autonomy; "hypotheses are tested by oracles with concrete references and explicit acceptance conditions"; pass keeps the result, mismatch returns to investigation; lessons compound across projects ([touhou-reconstruction-method.md L177 to L190](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/website/evidence/touhou-reconstruction-method.md#L177-L190)). DX-Ball: 3,205 differential cases plus 63 matching bytes ([dx-ball-sound-pan.md L99 to L108](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/website/evidence/dx-ball-sound-pan.md#L99-L108)).
- **Oracle quality is part of the loop.** TH08: a check compared instruction bytes but not the constant data, so source `0.0` passed against target `128.0`. Audit then fixed 12 stale rows out of 1,548 references ([touhou-reconstruction-method.md L197 to L229](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/website/evidence/touhou-reconstruction-method.md#L197-L229)). "a reward based on the earlier check could reinforce wrong source" ([reverse-engineering-models.md L140 to L144](https://github.com/morluto/rea/blob/c2b0c955cd9935886dc24fdb02c031f955476457/website/evidence/reverse-engineering-models.md#L140-L144)). Blog line: "As the learner gets better at optimizing the feedback we give it, understanding that feedback becomes more important too" (`website/locales/messages.pot` L1128 to L1131).

### Mapping rea principles onto skill reverse-engineering
| rea principle | Our equivalent |
|---|---|
| Observation vs inference vs unknown | Tag every rule in the reconstructed skill: observed in N/N outputs, inferred from K/N, or unknown |
| Absence proves nothing outside examined scope | "Never uses emojis" is only a hypothesis. Confidence depends on N and on whether inputs would have triggered emojis |
| Do not infer from names/strings alone | Do not infer the skill from one viral post's topic or hashtags. Use cross-output invariants |
| Size match is diagnostic, not acceptance | Same word count or slide count is not success. Judge on structure, voice, and blind discrimination |
| Independent oracle | Score against held-out original outputs, never against outputs the optimiser has already seen |
| Negative controls | Feed the scorer known-bad candidates (generic prompt, different creator's skill). If they score high, the metric is broken |
| Never aggregate weak to pass | A skill passes only if every declared dimension passes; unknown dimensions stay unknown |
| Optimise measured, completed tasks; tokens first | Budget the loop per reconstruction (RPE: about 230 calls). Stop at plateau |
| Compounding lessons | Store each reconstruction's failure modes as reusable checks for the next one |


## 5. Principles for our tool

Model: `output_i = Skill(input_i) + noise`. The skill is what stays constant across i. The input (topic, brief, data) and sampling noise vary.

### Negate (strip or ignore)
- Per-output content: topic nouns, named entities, numbers, facts, quotes, product names. PRSA does exactly this with POS tagging plus word2vec similarity, replacing with placeholders ([arXiv 2402.19200](https://arxiv.org/abs/2402.19200)).
- Sampling noise: wording that appears in only one output. o2p shows a single output gives cosine 0.93 but BLEU 0.30; literal phrasing is mostly noise.
- Platform artifacts not under the skill's control: auto-captions, platform UI, compression, music chosen by the platform.
- Human edits after generation, if known. They pollute the signal.
- Surface metrics as goals: length, slide count, duration. Keep them as features, not as the score.

### Keep (skill-invariant structure)
- Structure: hook type, section order, slide roles (hook, problem, steps, CTA), paragraph count, list style.
- Voice: person, tense, reading level, sentence length distribution, punctuation habits, emoji rate, banned or favoured phrases.
- Format rules: headings, line breaks, hashtag count and position, CTA wording pattern.
- Visual system (carousel): palette, font pairing, text density per slide, layout grid, image style.
- Video system: hook length in seconds, cut rate, caption style, shot types, camera moves, voiceover style, duration band. VI-Bench dims: subject, action, scene, style, camera.
- Negative constraints, only with evidence: a feature absent in N outputs where inputs would plausibly trigger it. Record N and confidence.
- Conditional rules: if outputs split into clusters (e.g. listicle vs story), the skill likely branches. o2p notes conditional rules are only partly recoverable; expect gaps.

### Optimise (loop)
1. Infer the per-output input brief for each original (the negated part). Needed to replay.
2. Propose K candidate skills (RPE uses 5) from a train split of outputs.
3. Replay: run each candidate on the inferred briefs.
4. Compare replays to originals on several axes (section 7).
5. Critique: LLM lists concrete differences per axis (RPE diff summary; ProTeGi text gradient).
6. Revise candidates; keep a Pareto set across axes, not one scalar (GEPA).
7. Stop at plateau or budget. RPE used 5 iterations.
8. Final check on held-out outputs the loop never saw. Run negative controls.


## 6. Proposed pipeline

```
 originals (N outputs: text posts | carousels | videos)
        |
        v
 [1] INGEST + NORMALISE per modality
     text      -> raw text
     carousel  -> per-slide OCR text + layout + palette/fonts (VLM)
     video     -> ASR transcript + shot list + cut times + caption style (VLM)
        |
        v
 [2] SPLIT  train (70%) | held-out (30%)
        |
        v
 [3] DECOMPOSE each output (train)
     content brief  (topic, facts, entities)   -> NEGATE: set aside as replay input
     form features  (structure, voice, format, visual, timing)
        |
        v
 [4] INVARIANTS across outputs
     feature in >= X% of outputs -> rule (observed)
     feature in some clusters    -> conditional rule (inferred)
     never seen                  -> candidate negative rule (unknown until tested)
        |
        v
 [5] DRAFT K candidate skills (rules + template + tagged confidence)
        |
        v
 [6] REPLAY  candidate x brief_i -> regenerated output_i
        |
        v
 [7] SCORE vs original_i   (embedding, structure, style stats, judge)
        |
        +-> plateau or budget hit? yes -> [9]
        |                         no
        v
 [8] CRITIQUE diffs -> REVISE -> keep Pareto set -> back to [6]
        |
 [9] HELD-OUT TEST on unseen briefs + NEGATIVE CONTROLS
        |
        +-> fail: back to [4] with failure notes
        |
        v
 [10] EXPORT skill: rules (observed/inferred/unknown), template, examples-free,
      per-axis scores, open unknowns
```

Notes:
- For video, invert to the intermediate spec (script, shot list, caption style), not to pixels. A skill usually writes a script; a video model or editor renders it. VI-Bench shows pixel-level replay is hard (best 0.632).
- Leave few-shot examples out of the exported skill by default. o2p cannot recover them, and copying originals into the skill is a content leak.


## 7. Evaluation

Ground truth path (offline benchmark):
- Write 30 to 100 known skills ourselves (o2p bootstrapped 26K synthetic GPT prompts from names and descriptions). Generate outputs. Invert. Compare recovered skill to the true skill and replays to originals. This is the only setting where we can measure recall of rules.

Metrics, from cheap to expensive:
- Prompt to prompt (only with ground truth): embedding cosine (o2p, RPE use text-embedding-ada-002 / 3-large), rule-level precision and recall after an LLM extracts rules from both.
- Output to output: embedding cosine and ROUGE-1 per pair (RPE inner loop uses ROUGE-1). BLEU is weak for function; o2p BLEU is 0.33 on GPT-3.5 even when cosine is 0.93.
- PRSA's three axes: semantic (sentence-transformer cosine), syntactic (FastKASSIM), structural (reciprocal Jensen-Shannon divergence). ASR thresholds 0.75 / 0.75 / 0.9.
- Distribution match across the set: compare histograms of length, sentence length, emoji rate, hashtag count, slide count, cut rate, hook length. Use JS divergence. A set-level match matters more than any single pair.
- LLM judge, pairwise: "Which of these two came from the same creator as reference set R?" Randomise order, swap positions, use a different model family from the generator. o2p reports its GPT-4o judge is noisy, so average many pairs.
- Discriminator test: mix originals and replays, ask a judge or classifier to spot replays. Target accuracy near 50%. Report with confidence interval.
- Blind human A/B: show original vs replay on the same brief, ask "same author?" or "which is better?". RPE's human study used blind preference (73.8% to 90.5% preferred RPE content over templates).
- Negative controls: score a generic "write a LinkedIn post" prompt and a different creator's skill. Both must score clearly lower. If not, the metric is broken (rea TH08 lesson).
- Report per axis. Do not average axes into one pass. Unknown axes stay unknown.


## 8. Open questions and risks

- Ethics, ToS, IP. Prompt marketplaces and GPT stores treat prompts as paid assets; PRSA calls stealing them an IP threat and disclosed to providers. PromptStealer frames it the same way for images. o2p argues prompts are not secrets. Platform terms of service for scraping outputs and reproducing a creator's style were **not checked here**. Safe default: run on the user's own outputs, or with the creator's consent; do not market it as copying others.
- Style vs content leak. A reconstructed skill can memorise phrases or facts from originals. Enforce n-gram overlap limits against originals (Zhang et al. used a 5-gram filter as a defense; reuse it as a guard).
- How many outputs are enough for a skill? o2p plateaus near 64 for a prompt; RPE works with 5. Multi-part skills with branches probably need more. Unmeasured.
- Input recovery is lossy. If the brief inferred in step [3] is wrong, replays diverge for reasons unrelated to the skill.
- Generator mismatch. Originals may come from another model or temperature. o2p transfer drops cosine about 3 to 4 points across model families.
- Conditional and rare rules: only observed branches are recoverable (o2p "CHANGE" limitation).
- Judge bias and Goodhart: optimising against one judge or one metric overfits it (rea: "a reward based on the earlier check could reinforce wrong source"). Use held-out data and several metrics.
- Cost: RPE about 230 calls, 100K input tokens, 30K output tokens per recovery. Video and carousel add VLM calls. Budget per run.
- Multimodal fidelity: best VLM gets 0.632 on VI-Bench; models write plausible prompts whose regenerated videos drift.
- No verified literature on reconstructing multi-file agent skills (tools, templates, scripts). This is new ground.


## 9. Sources

Papers
- Zhang, Morris, Shmatikov. Extracting Prompts by Inverting LLM Outputs. EMNLP 2024. [arXiv 2405.15012](https://arxiv.org/abs/2405.15012), [ACL Anthology](https://aclanthology.org/2024.emnlp-main.819/)
- Morris et al. Language Model Inversion. ICLR 2024. [arXiv 2311.13647](https://arxiv.org/abs/2311.13647), [ICLR page](https://iclr.cc/virtual/2024/poster/17623)
- Nazir et al. Better Language Model Inversion by Compactly Representing Next-Token Distributions. [arXiv 2506.17090](https://arxiv.org/abs/2506.17090)
- Morris et al. Text Embeddings Reveal (Almost) As Much As Text. EMNLP 2023. [arXiv 2310.06816](https://arxiv.org/abs/2310.06816)
- Zhang, Carlini, Ippolito. Effective Prompt Extraction from Language Models. [arXiv 2307.06865](https://arxiv.org/abs/2307.06865)
- Yang et al. PRSA: Prompt Stealing Attacks against Real-World Prompt Services. USENIX Security 2025 (extended version). [arXiv 2402.19200](https://arxiv.org/abs/2402.19200)
- Li, Klabjan. Reverse Prompt Engineering. EMNLP 2025. [arXiv 2411.06729](https://arxiv.org/abs/2411.06729), [ACL preview](https://preview.aclanthology.org/setup/2025.emnlp-main.1333)
- Suhail et al. PTP. [arXiv 2607.29378](https://arxiv.org/abs/2607.29378)
- Hong et al. Inversion Learning for NLG Evaluation Prompts. TACL. [arXiv 2504.21117](https://arxiv.org/abs/2504.21117)
- Shen et al. Prompt Stealing Attacks Against Text-to-Image Generation Models. [arXiv 2302.09923](https://arxiv.org/abs/2302.09923)
- Wen et al. Hard Prompts Made Easy (PEZ). [arXiv 2302.03668](https://arxiv.org/abs/2302.03668)
- Li et al. PromptMiner. [arXiv 2511.22119](https://arxiv.org/abs/2511.22119)
- Buchnick et al. PromptEvolver. [arXiv 2604.06061](https://arxiv.org/abs/2604.06061)
- Mallick et al. PROVE. [arXiv 2608.13671](https://arxiv.org/abs/2608.13671)
- Ye et al. Cross-Modal Prompt Inversion. USENIX Security 2025. [USENIX page](https://www.usenix.org/conference/usenixsecurity25/presentation/ye-inversion)
- Xie et al. VI-Bench. [arXiv 2609.08079](https://arxiv.org/abs/2609.08079)
- Meta Inverse Prompting for Video Generative Models. **UNVERIFIED**. [NeurIPS 2026 listing](https://neurips.cc/virtual/2026/poster/150385)
- Zhou et al. APE. [arXiv 2211.01910](https://arxiv.org/abs/2211.01910)
- Yang et al. OPRO. ICLR 2024. [arXiv 2309.03409](https://arxiv.org/abs/2309.03409)
- Pryzant et al. ProTeGi / APO. EMNLP 2023. [arXiv 2305.03495](https://arxiv.org/abs/2305.03495)
- Khattab et al. DSPy. [arXiv 2310.03714](https://arxiv.org/abs/2310.03714)
- Opsahl-Ong et al. MIPRO. EMNLP 2024. [arXiv 2406.11695](https://arxiv.org/abs/2406.11695)
- Yuksekgonul et al. TextGrad. [arXiv 2406.07496](https://arxiv.org/abs/2406.07496)
- Agrawal et al. GEPA. ICLR 2026. [arXiv 2507.19457](https://arxiv.org/abs/2507.19457)

Code and tools
- [collinzrj/output2prompt](https://github.com/collinzrj/output2prompt): `README.md`, `NUMBERS.md`, `main.py`, `vec2text/models/my_t5_base.py`
- [pharmapsychotic/clip-interrogator](https://github.com/pharmapsychotic/clip-interrogator)
- [morluto/rea](https://github.com/morluto/rea) at commit `c2b0c955cd9935886dc24fdb02c031f955476457`: `README.md`, `AGENTS.md`, `.agents/skills/reverse-engineer-anything/SKILL.md`, `.agents/skills/reverse-engineer-anything/references/evidence-workflows.md`, `.agents/skills/rea-analysis-optimization/SKILL.md`, `docs/reconstruction-coverage.md`, `docs/reconstruction-readiness.md`, `docs/reconstruction-obligation-ledgers.md`, `docs/native-function-matching.md`, `website/evidence/touhou-reconstruction-method.md`, `website/evidence/reverse-engineering-models.md`, `website/evidence/dx-ball-sound-pan.md`
- [rea.tools](https://rea.tools/)
