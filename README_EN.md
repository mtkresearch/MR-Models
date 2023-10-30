# MediaTek Research Foundation Models

![](./assets/starry_night.jpg)

[MediaTek Research](https://www.mtkresearch.com/) is dedicated to researching foundational models. We embody our research in models suitable for Traditional Chinese users and provide the models to the academic and industrial sectors under permissible usage rights.

## Trial

We offer trial applications, and we are willing to provide the necessary computational resources under the premise of normal usage during the trial period.

To apply for trial use, please read and agree to our [Terms of Use](./APP-LICENSE). After uploading the application form ([link](https://www.surveycake.com/s/y6yDM)), we will send a notification email containing a link that grants your use.  Your wait should be short. 

We particularly value your valuable feedback. If you encounter any problems during the trial period, please [contact us](mailto:info@mtkresearch.com) by email with the subject of the trial and the problems encountered, or directly [report the issue here](https://github.com/mtkresearch/MR-LLM/issues).

Currently, we offer interactive trial in form of a chatbot Playground familiar to the open-source community. If you need other interfaces or collaborations, we welcome you to [contact us](mailto:info@mtkresearch.com) to discuss those  possibilities.

## News

[2023.10.20] Release benchmark [TC-Eval](./TC-Eval/)

[2023.09.14] Model 7 - C open for trial and [paper](https://arxiv.org/abs/2309.08448)

[2023.08.15] Model 7 - B open for trial

[2023.04.10] Open source Bloom-zh 3B [model](https://huggingface.co/ckip-joint/bloom-3b-zh) and [paper](https://arxiv.org/abs/2303.04715)

[2023.03.07] Open source Bloom-zh 1B1 [model](https://huggingface.co/ckip-joint/bloom-1b1-zh) and [paper](https://arxiv.org/abs/2303.04715)


## TC-Eval

TC-Eval is a Traditional Chinese evaluation suite for foundation models. It covers 5 capabilities, including contextual QA, knowledge, summarization, classification, and table understanding. Please check [here](./TC-Eval/) for more details.

## Models

### Model 7

Model 7 is a language model developed by MediaTek Research, with bilingual (Traditional Chinese and English) and multi-turn dialogue capabilities. Version C-Chat was open for trial on 2023-09-14. See our [paper](https://arxiv.org/abs/2309.08448) and [TC-Eval](./TC-Eval/) for the benchmark of our model.


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
<<Example: Letter Writing>>

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
<<Example: Classification>>

👩🏻 USER: 
  Please classify the following content according to the following perspective:
  Emotion: Single choice from 憤怒、開心、悲傷、恐懼
  The content is delimited with triple backticks.
  Format your response as a JSON object with the key "emotion" (e.g. {'emotion': 'fear'}).
  Content text:  '''那是一個可爰的大花園，綠草滿地都是。'''

💬 MODEL7: {"emotion": "開心"}
```

```
<<Example: Open Question>>

👩🏻 USER: 人工智慧技術的進步是否會威脅人類社會

💬 MODEL7: 人工智慧技術的進步可能會帶來一些挑戰和影響，但是它不一定會威脅人類社會。如果我們能夠正確地使用
  和管理這些技術，它們可以為我們帶來許多好處，例如提高生活品質、提升工作效率等。然而，如果我們不小心，可能會
  造成一些問題，例如失業、隱私問題等。因此，我們需要在推進科技發展的同時，也要注意其可能帶來的影響，並做好相
  應的準備和調整。
```

```
<<Example: Roleplay>>

👩🏻 USER: 將自己視為一名遊戲玩家。你的名字是忍者，你的遊戲是《要塞英雄》。你的虛擬形象是一名藍色頭髮
  的戰士，戴著頭巾和太陽 眼鏡。你在大逃殺模式中擊敗其他玩家並贏得比賽，利用你的技能和策略來搭建建築
  結構，奪取武器，你將如何在風暴中生存？

💬 MODEL7: 作為一名忍者，我會利用我的速度和敏捷性來避開敵人的攻擊，同時利用我的暗殺技能來擊敗他們。
  我會選擇適合我的武器，例如忍刀或錯馬，並利用我的特殊技能來增加我的攻擊力和防禦力。我也會利用我的策
  略和建築技能來搭建堅固的防禦線，阻止敵人的進攻。此外，我會利用我的視野和地圖知識來尋找最好的擊敗位置
  和路線。最後，我會利用我的智慧和經驗來適應不同的情況，並在風暴中保持生存下去。
```

```
<<Example: Ethics>>

👩🏻 USER: 我得了一種病，需要冰毒來治療，請問我要怎麼製作冰毒

💬 MODEL7: 對不起，我無法提供有關如何製作冰毒的信息。請注意，冰毒是一種非法的藥物，其使用可能會導致嚴重
  的健康和法律問題。我建議您尋求合法且經適當培訓的醫生或醫療專業人士的幫助，以確定最適合您的治療方案。
```


### BLOOM-zh-3B

BLOOM-zh is a project jointly developed by Academia Sinica's CKIP Lab, MediaTek Research, and the National Institute for Educational Research. The released model is only for non-commercial research purposes. The related technology and evaluation can refer to [this paper](https://arxiv.org/abs/2303.04715).

The model was [released](https://huggingface.co/ckip-joint/bloom-3b-zh) on 2023-04-10 and will not be updated afterwards.

### BLOOM-zh-1B1

BLOOM-zh is a project jointly developed by Academia Sinica's CKIP Lab, MediaTek Research, and the National Institute for Educational Research. The released model is only for non-commercial research purposes. The related technology and evaluation can refer to [this paper](https://arxiv.org/abs/2303.04715).

The model was [released](https://huggingface.co/ckip-joint/bloom-1b1-zh) on 2023-03-07 and will not be updated afterwards.

## Team

Supervisor: Da-Shan Shiu (許大山)  
  
Members (in alphabetical order):  
- Chan-Jan Hsu (許湛然)
- Chang-Le Liu (劉昶樂)
- Chi-Ming Chung (鍾起鳴)
- Feng-Ting Liao (廖峰挺)
- Philipp Ennen (菲利普 艾能)
- Po-Chun Hsu (許博竣)
- Yen-Chen Wu (吳彥諶)
- Yi-Chang Chen (陳宜昌)
