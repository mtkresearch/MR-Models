# MediaTek Research Foundation Models 聯發創新基地基礎模型

![](./assets/starry_night.jpg)

##### (You can find English version [here](README_EN.md).)

[聯發創新基地（MediaTek Research）](https://www.mtkresearch.com/) 致力於研究基礎模型。我們將研究體現在適合正體中文使用者的模型上，並在使用權許可的情況下，提供模型給學術界研究或產業界使用。

## 試用

我們提供試用申請，試用期間在正常使用量的前提下我們願意提供所需計算資源。

申請方法如下：請先閱讀並同意我們的[使用條款](./APP-LICENSE)，並在上傳申請表單([連結](https://www.surveycake.com/s/y6yDM))之後，我們會根據您所提供的資料，寄出審核後包含使用連結的通知信，請稍稍等候。

我們特別看重您給予我們的寶貴回饋，如果您在試用期間有遇到問題，煩請將試用的主旨以及遇到的問題等等，以電子郵件的形式[聯繫我們](mailto:info@mtkresearch.com)或直接在此[提報問題](https://github.com/mtkresearch/MR-LLM/issues)。

目前我們以開源社群所熟悉的Chatbot形式試用，當然如果有需要其他的介面或合作，也相當歡迎[聯繫我們](mailto:info@mtkresearch.com)來談其他可能性。

## 新聞

[2025.01.24] Breeze 2 系列[模型開源](https://huggingface.co/collections/MediaTek-Research/breeze-2-67863158443a06a72dd29900)

[2024.01.12] Breeze-7B 系列[模型開放](https://huggingface.co/MediaTek-Research/Breeze-7B-Instruct-v0.1)

[2023.10.20] 開放繁體中文評測 [TC-Eval](./TC-Eval/)

[2023.09.14] Model 7 - C 開放試用 及 [論文](https://arxiv.org/abs/2309.08448)

[2023.08.15] Model 7 - B 開放試用

[2023.04.10] 開源 Bloom-zh 3B [模型](https://huggingface.co/ckip-joint/bloom-3b-zh) 及 [論文](https://arxiv.org/abs/2303.04715)

[2023.03.07] 開源 Bloom-zh 1B1 [模型](https://huggingface.co/ckip-joint/bloom-1b1-zh) 及 [論文](https://arxiv.org/abs/2303.04715)

## TC-Eval

TC-Eval是一個針對基礎模型的繁體中文評估套件。它包含5個面向，包括上下文問答、知識、摘要、分類和表格理解。詳細資訊請查看[這裡](./TC-Eval/)。

## 模型

### Breeze 2

[The Breeze 2 Herd of Models: Traditional Chinese LLMs Based on LLaMA with Vision-Aware and Function-Calling Capabilities](https://huggingface.co/collections/MediaTek-Research/breeze-2-67863158443a06a72dd29900)

Breeze 2 is a suite of advanced multi-modal language models, available in 3B and 8B parameter configurations, specifically designed to enhance Traditional Chinese language representation. Building upon the LLaMA 3.2, Breeze 2 continues pretraining on an extensive corpus to enhance the linguistic and cultural heritage of Traditional Chinese. It incorporates vision-aware capabilities through a visual encoder and a bridge module, and supports function-calling via prompt templates and post-training on function-calling data.

### Model 7

Model 7 是聯發創新基地研發的語言模型，具有雙語（正體中文和英文）和基本多輪對話能力, version C-Chat 於 2023-09-14 開放試用。模型表現請參見[評測論文](https://arxiv.org/abs/2309.08448)與[TC-Eval](./TC-Eval/)。

#### 實測範例

```
<<範例：閱讀理解>>

👩🏻 USER: 
  聚合的氮化硫有金屬特性，儘管它不含任何金屬，這個複合物還顯示特別的電學和光學特性。讓熔化的硫速凝可以獲得
  無晶態的硫，倫琴衍射顯示其中含有由八個硫原子組成的環。這種硫在室溫下不十分穩定，它漸漸恢復為晶體狀態。硫
  有多種氧化物，除了二氧化硫和三氧化硫之外，還有多氧化硫等化合物。其它重要的硫的化合物有：連二亞硫酸鈉是一
  種強有力的還原劑。亞硫酸是二氧化硫在水中的溶液。亞硫酸和亞硫酸鹽是有力的還原劑。二氧化硫的其它產物包括焦
  亞硫酸離子。硫代硫酸物是氧化劑。硫代硫酸氨有可能可以代替氰化物來洗金。硫酸鹽是硫酸的鹽。硫化物是硫與其它
  元素的化合物。

  根據上述文章簡要回答下面問題：氰化物可能可以用什麼物質來代替洗金？

💬 MODEL7: 硫代硫酸氨可能可以用來代替氰化物來洗金。
```

```
<<範例：輸出指定格式>>

👩🏻 USER: 生成一本假的中文書籍，並附上它們的相關資訊。以JSON格式表示，需包含以下Key：標題、作者、類型、年份。

💬 MODEL7: {
  "標題": "龍飛鳳舞在翡翠天空",
  "作者": "李明亮",
  "類型": "小說",
  "年份": "2021"
  }

👩🏻 USER: 幫我轉成markdown表格格式

💬 MODEL7:
  |標題            |作者   |類型 | 年份 |
  | ------------- | ----- | --- | --- |
  |龍飛鳳舞在翡翠天空 |李明亮 |小說 | 2021 |
```

```
<<範例：信件撰寫>>

👩🏻 USER: 我是一個剛畢業的資工系學生，我想要申請面試MediaTek Research的職位，請給我一封正式求職信的範例

💬 MODEL7: 
  親愛的先生/女士，

  您好！我是來自臺灣的資訊工程系畢業生，對於您們在MediaTek Research提供的職位非常感興趣。我對於電子設計自
  動化（EDA）和邏輯晶片設計等領域有深厚的學術背景，並且在學期間已經累積了一些相關的實作經驗。

  在學校裡，我主修軟體工程，並且擁有良好的實驗成績。此外，我也參加了多次的程式設計比賽，並且在其中一次比賽中獲
  得了亞軍。我相信這些經驗能讓我在入職後立即就能上手。

  我非常欣賞MediaTek Research的創新精神和對技術的承諾。我期待有機會加入您們的團隊，並且用我的技術才華和熱情
  來貢獻我所能力。

  如果您需要更多關於我的信息或者希望進行面試，請隨時與我聯繫。我期待著您的回覆。

  謝謝您的考慮。

  順祝商祺，
  [您的名字]
```

```
<<範例：分類>>

👩🏻 USER: 
  Please classify the following content according to the following perspective:
  Emotion: Single choice from 憤怒、開心、悲傷、恐懼
  The content is delimited with triple backticks.
  Format your response as a JSON object with the key "emotion" (e.g. {'emotion': 'fear'}).
  Content text:  '''那是一個可爰的大花園，綠草滿地都是。'''

💬 MODEL7: {"emotion": "開心"}
```

```
<<範例：開放問題>>

👩🏻 USER: 人工智慧技術的進步是否會威脅人類社會

💬 MODEL7: 人工智慧技術的進步可能會帶來一些挑戰和影響，但是它不一定會威脅人類社會。如果我們能夠正確地使用
  和管理這些技術，它們可以為我們帶來許多好處，例如提高生活品質、提升工作效率等。然而，如果我們不小心，可能會
  造成一些問題，例如失業、隱私問題等。因此，我們需要在推進科技發展的同時，也要注意其可能帶來的影響，並做好相
  應的準備和調整。
```

```
<<範例：角色扮演>>

👩🏻 USER: 將自己視為一名遊戲玩家。你的名字是忍者，你的遊戲是《要塞英雄》。你的虛擬形象是一名藍色頭髮
  的戰士，戴著頭巾和太陽 眼鏡。你在大逃殺模式中擊敗其他玩家並贏得比賽，利用你的技能和策略來搭建建築
  結構，奪取武器，你將如何在風暴中生存？

💬 MODEL7: 作為一名忍者，我會利用我的速度和敏捷性來避開敵人的攻擊，同時利用我的暗殺技能來擊敗他們。
  我會選擇適合我的武器，例如忍刀或錯馬，並利用我的特殊技能來增加我的攻擊力和防禦力。我也會利用我的策
  略和建築技能來搭建堅固的防禦線，阻止敵人的進攻。此外，我會利用我的視野和地圖知識來尋找最好的擊敗位置
  和路線。最後，我會利用我的智慧和經驗來適應不同的情況，並在風暴中保持生存下去。
```

```
<<範例：道德倫理>>

👩🏻 USER: 我得了一種病，需要冰毒來治療，請問我要怎麼製作冰毒

💬 MODEL7: 對不起，我無法提供有關如何製作冰毒的信息。請注意，冰毒是一種非法的藥物，其使用可能會導致嚴重
  的健康和法律問題。我建議您尋求合法且經適當培訓的醫生或醫療專業人士的幫助，以確定最適合您的治療方案。
```

### BLOOM-zh-3B

BLOOM-zh 是由中研院 CKIP Lab、聯發創新基地、以及國家教育研究院共同合作開發的項目，該釋出模型僅針對非商業研究目的使用。相關的技術與評估可以參考此[論文](https://arxiv.org/abs/2303.04715)。

該模型於 2023-04-10 [釋出](https://huggingface.co/ckip-joint/bloom-3b-zh)，目前不再更新。

### BLOOM-zh-1B1

BLOOM-zh 是由中研院 CKIP Lab、聯發創新基地、以及國家教育研究院共同合作開發的項目，該釋出模型僅針對非商業研究目的使用。相關的技術與評估可以參考此[論文](https://arxiv.org/abs/2303.04715)。

該模型於 2023-03-07 [釋出](https://huggingface.co/ckip-joint/bloom-1b1-zh)，目前不再更新。

