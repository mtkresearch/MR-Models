# MediaTek Research Foundation Models 聯發創新基地基礎模型

![](./assets/starry_night.jpg)

[聯發創新基地（MediaTek Research）](https://i.mediatek.com/mediatekresearch) 致力於研究基礎模型。我們將研究體現在適合正體中文使用者的模型上，並在使用權許可的情況下，提供模型給學術界研究或產業界使用。

## 新聞

[2025.01.24] Breeze 2 系列 [模型開源](https://huggingface.co/collections/MediaTek-Research/breeze-2-67863158443a06a72dd29900) 及 [論文發表](https://arxiv.org/abs/2501.13921)

[2024.09.23] Breeze FC [模型開源](https://huggingface.co/MediaTek-Research/Breeze-7B-FC-v1_0) 及 [論文發表](https://arxiv.org/abs/2412.01130)

[2024.08.10] BreeXe 系列 [模型開源](https://huggingface.co/MediaTek-Research/Breexe-8x7B-Instruct-v0_1)

[2024.05.24] Generative Fusion Decoding (GFD) [技術發表](https://arxiv.org/abs/2405.14259) 以及 Breezper [實作程式碼發布](https://github.com/mtkresearch/generative-fusion-decoding) 

[2024.01.12] Breeze-7B 系列 [模型開源](https://huggingface.co/MediaTek-Research/Breeze-7B-Instruct-v0.1) 及 [論文發表](https://arxiv.org/abs/2403.02712)

[2023.10.20] 開放繁體中文評測 [TC-Eval](./TC-Eval/)

[2023.09.14] Model 7 - C 開放試用 及 [論文](https://arxiv.org/abs/2309.08448)

[2023.08.15] Model 7 - B 開放試用

[2023.04.10] 開源 Bloom-zh 3B [模型](https://huggingface.co/ckip-joint/bloom-3b-zh) 及 [論文](https://arxiv.org/abs/2303.04715)

[2023.03.07] 開源 Bloom-zh 1B1 [模型](https://huggingface.co/ckip-joint/bloom-1b1-zh) 及 [論文](https://arxiv.org/abs/2303.04715)

## Next

- SEALION

## 模型

### Breeze 2

【[Paper](https://arxiv.org/abs/2501.13921)】【[Kaggle Demo](https://www.kaggle.com/code/ycckaggle/breeze-2-demo)】【[Collection](https://huggingface.co/collections/MediaTek-Research/breeze-2-67863158443a06a72dd29900)】 

Breeze 2 模型系列：具備視覺感知與函數調用能力的繁體中文大型語言模型

Breeze 2 是一套先進的多模態語言模型，提供 3B 和 8B 參數配置，專為加強繁體中文語言表示而設計。在 LLaMA 3.2 的基礎上，Breeze 2 持續在大規模語料庫上進行預訓練，以進一步加強繁體中文的語言與文化內涵。該模型結合了視覺編碼器與橋接模組，實現了視覺感知能力，同時通過提示模板與函數調用數據的後訓練，支持函數調用功能。

<details>
<summary>English Content</summary>
The Breeze 2 Herd of Models: Traditional Chinese LLMs Based on LLaMA with Vision-Aware and Function-Calling Capabilities

Breeze 2 is a suite of advanced multi-modal language models, available in 3B and 8B parameter configurations, specifically designed to enhance Traditional Chinese language representation. Building upon the LLaMA 3.2, Breeze 2 continues pretraining on an extensive corpus to enhance the linguistic and cultural heritage of Traditional Chinese. It incorporates vision-aware capabilities through a visual encoder and a bridge module, and supports function-calling via prompt templates and post-training on function-calling data.
</details>


### BreeXe
【[Collection](https://huggingface.co/collections/MediaTek-Research/breeze-7b-and-breexe-8x7b-65a67144880ad716173d7d87)】 

Breexe-8x7B 是一個語言模型家族，基於 Mixtral-8x7B 開發，專門針對繁體中文使用。

Breexe-8x7B-Base 是 Breexe-8x7B 系列的基礎模型。Breexe-8x7B-Base 擴展了原始詞彙表，新增了 30,000 個繁體中文詞彙。在詞彙表擴展的情況下，Breexe-8x7B 在繁體中文推理速度上是 Mixtral-8x7B 的兩倍。

Breexe-8x7B-Instruct 是基於 Breexe-8x7B-Base 的衍生模型，使得該模型可以直接用於常見任務，如問答、檔案檢索生成（RAG）、多輪對話和摘要。**Breexe-8x7B-Instruct 在繁體中文和英文基準測試中表現出色，與 OpenAI 的 gpt-3.5-turbo-1106 相媲美。**

<details>
<summary>English Content</summary>
Breexe-8x7B is a language model family that builds on top of Mixtral-8x7B, specifically intended for Traditional Chinese use.

Breexe-8x7B-Base is the base model for the Breexe-8x7B series. Breexe-8x7B-Base expands the original vocabulary with additional 
30,000 Traditional Chinese tokens. With the expanded vocabulary, Breexe-8x7B operates at twice the inference speed for Traditional 
Chinese to Mixtral-8x7B.

Breexe-8x7B-Instruct derives from the base model Breexe-8x7B-Base, 
making the resulting model amenable to be used as-is for commonly seen tasks, such as Q&A, RAG, multi-round chat, and summarization. 
**Breexe-8x7B-Instruct demonstrates impressive performance in benchmarks for Traditional Chinese and English, on par with OpenAI's gpt-3.5-turbo-1106.**
</details>

### Breeze
【[Paper](https://arxiv.org/abs/2403.02712)】【[Collection](https://huggingface.co/collections/MediaTek-Research/breeze-7b-and-breexe-8x7b-65a67144880ad716173d7d87)】 

Breeze-7B 是一個語言模型家族，基於 Mistral-7B 開發，專門針對繁體中文使用。
有關此模型的詳細資訊，請參閱我們的[論文](https://arxiv.org/abs/2403.02712)。

實用性方面：
- Breeze-7B-Base 擴增了原始詞表，新增了 30,000 個繁體中文詞彙。在詞彙表擴增且其他條件相同的情況下，Breeze-7B 在繁體中文推理速度上是 Mistral-7B 和 Llama 7B 的兩倍。
- Breeze-7B-Instruct 可直接用於常見任務，如問答、檔案檢索生成 (RAG)、多輪對話和摘要。

性能方面：
- Breeze-7B-Instruct 在繁體中文和英文基準測試中表現出色，與同類型的開源模型如 Taiwan-LLM-7B/13B-chat、QWen(1.5)-7B-Chat 和 Yi-6B-Chat 相比，具有顯著優勢。

<details>
<summary>English Content</summary>
Breeze-7B is a language model family that builds on top of Mistral-7B, specifically intended for Traditional Chinese use.

For details of this model please read our [paper](https://arxiv.org/abs/2403.02712).

Practicality-wise:
- Breeze-7B-Base expands the original vocabulary with an additional 30,000 Traditional Chinese tokens. With the expanded vocabulary, and everything else being equal, Breeze-7B operates at twice the inference speed for Traditional Chinese to Mistral-7B and Llama 7B. 
- Breeze-7B-Instruct can be used as is for common tasks such as Q&A, RAG, multi-round chat, and summarization.

Performance-wise:
- Breeze-7B-Instruct demonstrates impressive performance in benchmarks for Traditional Chinese and English when compared to similar-sized open-source contemporaries such as Taiwan-LLM-7B/13B-chat, QWen(1.5)-7B-Chat, and Yi-6B-Chat. 
</details>





