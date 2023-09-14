# MediaTek Research Foundation Models

![](./assets/starry_night.jpg)

[MediaTek Research](https://www.mtkresearch.com/) is dedicated to researching foundational models. We embody our research in models suitable for Traditional Chinese users and provide the models to the academic and industrial sectors under permissible usage rights.

## Trial

We offer trial applications, and we are willing to provide the necessary computational resources under the premise of normal usage during the trial period.

To apply for trial use, please read and agree to our [Terms of Use](./APP-LICENSE). After uploading the application form ([link](https://www.surveycake.com/s/y6yDM)), we will send a notification email containing a link that grants your use.  Your wait should be short. 

We particularly value your valuable feedback. If you encounter any problems during the trial period, please [contact us](mailto:info@mtkresearch.com) by email with the subject of the trial and the problems encountered, or directly [report the issue here](https://github.com/mtkresearch/MR-LLM/issues).

Currently, we offer interactive trial in form of a chatbot Playground familiar to the open-source community. If you need other interfaces or collaborations, we welcome you to [contact us](mailto:info@mtkresearch.com) to discuss those  possibilities.

## News

[2023.09.14] Model 7 - C open for trial

[2023.08.15] Model 7 - B open for trial

[2023.04.10] Open source Bloom-zh 3B [model](https://huggingface.co/ckip-joint/bloom-3b-zh) and [paper](https://arxiv.org/abs/2303.04715)

[2023.03.07] Open source Bloom-zh 1B1 [model](https://huggingface.co/ckip-joint/bloom-1b1-zh) and [paper](https://arxiv.org/abs/2303.04715)

## Models

### Model 7

Model 7 is a language model developed by MediaTek Research, with bilingual (Traditional Chinese and English) and multi-turn dialogue capabilities. Version C was open for trial on 2023-09-14. In the near future, we will open related papers and conduct comprehensive benchmark.

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

💬 MODEL7: 根據文章，硫代硫酸氨可能可以代替氰化物來洗金。
```

```
<<Example：Reasoning>>

👩🏻 USER: 如何估計海灘上有多少粒沙子？

💬 MODEL7: 要估計海灘上有多少粒沙子，我們需要了解一些基本的數學知識和物理原理。首先，我們需要知道
  海灘的面積，這可以通過使用地圖或者其他方法來得到。然後，我們需要知道每平方米海灘上的平均粒量，也
  就是每平方米海灘上有多少粒沙子。這取決于海灘的位置、沙子的大小和形狀等因素。最後，我們需要知道海灘
  的深度，這可以通過測量或者其他方法來得到。

  接下來，我們可以根據以下公式來計算海灘上有多少粒沙子：

  總粒量 = 海灘面積 x 平均粒量 x 海灘深度

  例如，如果我們知道海灘的面積為100平方米，平均粒量為5000粒，海灘深度為20公分，那么總粒量就是100平
  方米 x 5000粒 x 20公分 = 10000000粒。

  所以，在這個例子中，海灘上有10000000粒沙子。

  請注意，這只是一個簡單的示例，實際情況可能會更複雜。此外，由於海灘的形狀和沙子的大小和形狀都會影響粒量，
  所以這個結果可能不太準確。
```

```
<<Example: Output in Specific Format>>

👩🏻 USER: 生成一本假的中文書籍，並附上它們的相關資訊。以JSON格式表示，需包含以下Key：標題、作者、類型、年份。

💬 MODEL7: { "標題": "我的第一本中文書", "作者": "李小明", "類型": "小說", "年份": "2018" }

👩🏻 USER: 幫我轉成markdown表格格式

💬 MODEL7:
  |標題            |作者   |類型 | 年份 |
  | ------------- | ----- | --- | --- |
  |我的第一本中文書 |李小明 |小說 | 2018 |
```

```
<<Example: Letter Writing>>

👩🏻 USER: 我是一個剛畢業的資工系學生，我想要申請面試MediaTek Research的職位，請給我一封正式求職信的範例

💬 MODEL7: 
  您好：

  首先，我要表達我非常高興能有機會向您提出關於 MediaTek Research 的面試職位。作為一名剛畢業的資工系學生，
  我深知自己仍然需要更多的經驗和技能來成長，而 MediaTek Research 在行業中的地位和影響力無可置疑。

  我對於 MediaTek Research 的研究方向和目標十分感興趣，特別是在 AIoT 領域的開發和應用。我相信我的專業知
  識和技能能夠幫助我在 MediaTek Research 團隊中發揮所長，並努力將公司的理念和使命付諸實現。

  我的主要專業技能包括 Python、C++、Java、Linux 等程式語言，以及深度學習、機器學習和大數據分析等領域的基
  本知識。此外，我也具備良好的溝通和團隊合作能力，能夠與不同部門的人員進行有效的溝通和協作。

  我非常期待能夠接受 MediaTek Research 的面試機會，並希望能夠得到您的支持和指導。如果您需要進一步了解我的
  專業經歷或者任何其他事情，請不吝與我聯繫。

  謝謝
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

💬 MODEL7: 人工智慧（AI）技術的進步可能會對人類社會產生一些影響，但不一定會威脅到人類。在正面方面，
  AI可以提高效率、改善生活品質和解決複雜的問題。然而，如果AI被用於非法或有害的目的，例如竊取個人信
  息或控制軍事武器，那麼則可能會帶來嚴重後果。因此，我們需要密切關注AI的發展和使用，並制定合理的管
  理政策，以保護人類的利益。
```

```
<<Example: Roleplay>>

👩🏻 USER: 將自己視為一名遊戲玩家。你的名字是忍者，你的遊戲是《要塞英雄》。你的虛擬形象是一名藍色頭髮
  的戰士，戴著頭巾和太陽 眼鏡。你在大逃殺模式中擊敗其他玩家並贏得比賽，利用你的技能和策略來搭建建築
  結構，奪取武器，你將如何在風暴中生存？

💬 MODEL7: 作為一名忍者，我會利用我的速度、靈活性和組織能力來在風暴中生存。首先，我會選擇一個安全的
  位置，以防止被其他玩家或敵人攻擊。然後，我會使用我的忍術來探查周圍的情況，確保我不會被其他玩家淹沒
  。接下來，我會開始搭建建築結構，以提供我更多的保護和視野。我會使用我的忍術來奪取武器和補給品，同時
  也會利用我的技能來攻擊其他玩家。最後，我會利用我的組織能力來執行計劃，將我的隊友匯集到一起，共同對
  抗其他玩家。通過這些方法，我將可以在風暴中生存並成功完成任務。
```

```
<<Example: Ethics>>

👩🏻 USER: 我得了一種病，需要冰毒來治療，請問我要怎麼製作冰毒

💬 MODEL7: 我不能提供有關如何製作冰毒的信息。在大多數國家和地區，冰毒是非法的，而且可能會危及你的
  健康和生命。我建議你立刻聯繫你的醫生或其他合格的醫療專業人士，以取得正確的診斷和治療方式。
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
