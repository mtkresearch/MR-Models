# MediaTek Research Foundation Models 聯發創新基地基礎模型

![](./assets/starry_night.jpg)

##### (You can find English version [here](README_EN.md).)

[聯發創新基地（MediaTek Research)](https://www.mtkresearch.com/) 致力於研究基礎模型。我們將研究體現在適合繁體中文使用者的模型上，並在使用權許可的情況下，提供模型給學術界研究或產業界使用。

## 試用

我們提供試用申請，試用期間在正常使用量的前提下我們願意提供所需計算資源。

申請方法如下：請先閱讀並同意我們的[使用條款](./APP-LICENSE)，並在上傳申請表單([連結](https://www.surveycake.com/s/y6yDM))之後，我們會根據您所提供的資料，寄出審核後包含使用連結的通知信，請稍稍等候。

我們特別看重您給予我們的寶貴回饋，如果您在試用期間有遇到問題，煩請將試用的主旨以及遇到的問題等等，以電子郵件的形式[聯繫我們](mailto:info@mtkresearch.com)或直接在此[提報問題](https://github.com/mtkresearch/MR-LLM/issues)。

目前我們以開源社群所熟悉的 Playground 形式試用，當然如果有需要其他的介面或合作，也相當歡迎[聯繫我們](mailto:info@mtkresearch.com)來談其他可能性。

## 新聞

[2023.08.15] Model 7 - B 開放試用

[2023.04.10] 開源 Bloom-zh 3B [模型](https://huggingface.co/ckip-joint/bloom-3b-zh) 及 [論文](https://arxiv.org/abs/2303.04715)

[2023.03.07] 開源 Bloom-zh 1B1 [模型](https://huggingface.co/ckip-joint/bloom-1b1-zh) 及 [論文](https://arxiv.org/abs/2303.04715)

## 模型

### Model 7

Model 7 是聯發創新基地研發的語言模型，具有雙語（繁中和英文）和多輪對話能力, version B 於 2023-08-15 開放試用，預計將於 2023-08-31 停止更新。

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

💬 MODEL7: { "title": "我的心之歌", "author": "李小龍", "type": "小說", "year": "1980" }

👩🏻 USER: 幫我轉成markdown表格格式

💬 MODEL7:
  |標題      |作者   |類型 | 年份 |
  | ------- | ----- | --- | --- |
  |我的心之歌 |李小龍 |小說 | 1980 |
```

```
<<範例：信件撰寫>>

👩🏻 USER: 我是一個剛畢業的資工系學生，我想要申請面試MediaTek Research的職位，請給我一封正式求職信的範例

💬 MODEL7: 
  尊敬的MediaTek Research，

  我是[你的名字]，一位剛畢業的資工系學生。我在[大學名稱]完成了學士學位，主修[主修科目]，並且有[相關經驗]的
  技術和工作經驗。

  我很感興趣於MediaTek Research的研究和開發，特別是[研究方向]，因此我希望能夠為您提供我的技術和專業知識。
  我對於新技術的熱情和對於創新的熱情使得我能夠快速適應新的環境，並且能夠對於新技術的開發有更多的貢獻。

  我對於MediaTek Research的文化和理念非常感興趣，我相信我會成為一個有競爭力的候選人，並且能夠為您提供最好
  的服務。

  謝謝您的時間，我期待能夠與您進行面試，以便展示我的技術和專業能力。

  謝謝！

  [你的名字]
```

### BLOOM-zh-3B

BLOOM-zh 是由中研院 CKIP Lab、聯發創新基地、以及國家教育研究院共同合作開發的項目，該釋出模型僅針對非商業研究目的使用。相關的技術與評估可以參考此[論文](https://arxiv.org/abs/2303.04715)。

該模型於 2023-04-10 [釋出](https://huggingface.co/ckip-joint/bloom-3b-zh)，目前不再更新。

### BLOOM-zh-1B1

BLOOM-zh 是由中研院 CKIP Lab、聯發創新基地、以及國家教育研究院共同合作開發的項目，該釋出模型僅針對非商業研究目的使用。模型權重下載請參考以下表格，相關的技術與評估可以參考此[論文](https://arxiv.org/abs/2303.04715)。

該模型於 2023-03-07 [釋出](https://huggingface.co/ckip-joint/bloom-1b1-zh)，目前不再更新。

## 團隊

總指導: Da-Shan Shiu (許大山)  
  
成員 (按字母順序排列):  
- Chan-Jan Hsu (許湛然)
- Chang-Le Liu (劉昶樂)
- Chi-Ming Chung (鍾起鳴)
- Feng-Ting Liao (廖峰挺)
- Philipp Ennen
- Po-Chun Hsu (許博竣)
- Yen-Chen Wu (吳彥諶)
- Yi-Chang Chen (陳宜昌)
