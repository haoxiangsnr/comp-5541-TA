---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: Welcome to Slidev
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# apply unocss classes to the current slide
class: text-center
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# https://sli.dev/guide/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/guide/syntax#mdc-syntax
mdc: true
---

# A Tutorial on LLaMA, Vicuna, and LoRA

Presentation slides for developers

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:edit />
  </button>
  <a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

---

# Components of a ChatGPT-like Model

1. **Pretrained Language Models**
   - Predict the next token given the previous tokens
   - Understand words and sentences in context
   - [GPT series](https://platform.openai.com/docs/models), [Falcon](https://github.com/falconry/falcon), [LLaMA](https://github.com/meta-llama/llama), etc.
2. **Supervised Fine-tuning**
   - Predict the next token given the previous tokens
   - Understand prompts and answers (Q&A style)
   - [ChatGPT](https://platform.openai.com/docs/guides/chat), [LLaMA-Chat](https://github.com/meta-llama/llama), [Vicuna](https://lmsys.org/blog/2023-03-30-vicuna/), [Alpaca-LoRA](https://github.com/tloen/alpaca-lora), etc.
3. **Reinforcement Learning from Human Feedback (RLHF)**
   - Generate tokens that maximize rewards
   - Understand human feedback, like a natural sentence a human would say
   - ChatGPT, [Claude](https://claude.ai/), etc.

---

# BigScience Large Open-science Open-access Multilingual Language Model (BLOOM)

BLOOM: A 176B-Parameter Open-Access Multilingual Language Model

![BLOOM](/bloom.png)

- 176B parameters
- 13 programming languages, 46 human languages (1.5 TB, 16.2% Chinese)
- 70 layers, 2048 tokens
- 384 A100
- 3~4 months


---

# Supervised Fine-Tuning

- [Alpaca](https://github.com/tatsu-lab/stanford_alpaca): An Instruction-following LLaMA Model
  - 52K instruction-following demonstrations generated from OpenAI’s text-davinci-003
- [Vicuna](https://github.com/lm-sys/FastChat): An Open-Source Chatbot Impressing GPT-4 with 90% ChatGPT Quality
  - Data from ShareGPT (0.2B users)
  - Has longer conversations and context windows
- LLaMA-Chat
  - Private datasets for tuning on chat data
  - Iteratively refined using Reinforcement Learning from Human Feedback (RLHF)


---

# LLM Application: Text-Guided Target Speaker Extraction

Leverage the power of a large language model (LLM) to extract meaningful semantic cues from the user's typed text input.

<img src="/diff.png" class="h-45" />


- Text acts as a standalone extraction cue, potentially addressing the privacy and instability issues inherent in predominant voiceprint-based target speaker extraction systems.
- By informing TSE models about the speaker's current state, text can help tackle intra-speaker variability, thereby enhancing the effectiveness of speaker extraction.


---
layout: image
image: /scenarios.png
backgroundSize: 95%
---


---

# LLM Application: Text-Guided Target Speaker Extraction (Cont.)

<img src="/model_arch.png" class="h-80" />

Demo: https://haoxiangsnr.github.io/llm-tse/