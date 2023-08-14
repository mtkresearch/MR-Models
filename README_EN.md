# MediaTek Research Foundation Models

[MediaTek Research](https://www.mtkresearch.com/) is dedicated to researching foundational models. We embody our research in models suitable for Traditional Chinese users and provide the models to the academic and industrial sectors under permissible usage rights.

## Trial

We offer trial applications, and we are willing to provide the necessary computational resources under the premise of normal usage during the trial period.

The application method is as follows: Please read and agree to our [Terms of Use](./APP-LICENSE) first. After uploading the application form ([link](https://www.surveycake.com/s/y6yDM)), we will send a notification email containing the usage link based on the information you provided. Please wait a moment.

We particularly value your valuable feedback. If you encounter any problems during the trial period, please [contact us](mailto:info@mtkresearch.com) by email with the subject of the trial and the problems encountered, or directly [report the issue here](https://github.com/mtkresearch/MR-LLM/issues).

Currently, we are trialing in the form of a Playground familiar to the open-source community. Of course, if you need other interfaces or collaborations, we also welcome you to [contact us](mailto:info@mtkresearch.com) to discuss other possibilities.

## News

[2023.08.15] Model 7 - B open for trial

[2023.04.10] Open source Bloom-zh 3B [model](https://huggingface.co/ckip-joint/bloom-3b-zh) and [paper](https://arxiv.org/abs/2303.04715)

[2023.03.07] Open source Bloom-zh 1B1 [model](https://huggingface.co/ckip-joint/bloom-1b1-zh) and [paper](https://arxiv.org/abs/2303.04715)

## Models

### Model 7

Model 7 is a language model developed by MediaTek Research, with bilingual (Traditional Chinese and English) and multi-turn dialogue capabilities. Version B was open for trial on 2023-08-15 and scheduled to stop updating on 2023-08-31.

#### Test Examples

```
<<Example: Reading Comprehension>>

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
<<Example: Output in Specific Format>>

👩🏻 USER: 生成一本假的中文書籍，並附上它們的相關資訊。以JSON格式表示，需包含以下Key：標題、作者、類型、年份。

💬 MODEL7: { "title": "我的心之歌", "author": "李小龍", "type": "小說", "year": "1980" }

👩🏻 USER: 幫我轉成markdown表格格式

💬 MODEL7:
  |標題      |作者   |類型 | 年份 |
  | ------- | ----- | --- | --- |
  |我的心之歌 |李小龍 |小說 | 1980 |
```

```
<<Example: Letter Writing>>

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

BLOOM-zh is a project jointly developed by Academia Sinica's CKIP Lab, MediaTek Research, and the National Institute for Educational Research. The released model is only for non-commercial research purposes. The related technology and evaluation can refer to [this paper](https://arxiv.org/abs/2303.04715).

The model was [released](https://huggingface.co/ckip-joint/bloom-3b-zh) on 2023-04-10 and will not be updated afterwards.

### BLOOM-zh-1B1

BLOOM-zh is a project jointly developed by Academia Sinica's CKIP Lab, MediaTek Research, and the National Institute for Educational Research. The released model is only for non-commercial research purposes. For model weight download, please refer to the following table. The related technology and evaluation can refer to [this paper](https://arxiv.org/abs/2303.04715).

The model was [released](https://huggingface.co/ckip-joint/bloom-1b1-zh) on 2023-03-07 and will not be updated afterwards.

## Team

Supervisor: Da-Shan Shiu (許大山)  
  
Members (in alphabetical order):  
- Chan-Jan Hsu (許湛然)
- Chang-Le Liu (劉昶樂)
- Chi-Ming Chung (鍾起鳴)
- Feng-Ting Liao (廖峰挺)
- Philipp Ennen
- Po-Chun Hsu (許博竣)
- Yen-Chen Wu (吳彥諶)
- Yi-Chang Chen (陳宜昌)
