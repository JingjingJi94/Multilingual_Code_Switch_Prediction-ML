
======================================================================
QUALITATIVE EXAMPLES — XLMR
======================================================================

--- Successful Predictions — Inter-sentential (3 examples) ---
  [Spanish-English]  pos=28
  tokens : en zu ela , ▁right ? ▁La ▁próxima ▁vez ▁que
  langs  : es es es punct en punct es es es es
  ysw_true=1  ysw_pred=1  ydur_true=2
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?

  [Spanish-English]  pos=47
  tokens : ▁of ▁him , ▁for ▁sure . ▁Definitiv amente ▁sentir é
  langs  : en en punct en en punct es es es es
  ysw_true=1  ysw_pred=1  ydur_true=2
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?

  [Chinese-English]  pos=70
  tokens : 特别是 那些 年纪 大 的人 。 " How ▁could ▁this
  langs  : zh zh zh zh zh punct punct en en en
  ysw_true=1  ysw_pred=1  ydur_true=1
  text   : 那个银行职员说得真好，"Trust me, it's a good investment," 但我还是有点不放心。 她想去银行存款，结果被保险公司的人忽悠，"It's just a small risk," 他说。 银行和保险公司一起欺骗了


--- Successful Predictions — Intra-sentential (3 examples) ---
  [Spanish-English]  pos=1
  tokens : ▁Vo y ▁a ▁recordar ▁siempre ▁la ▁época
  langs  : es es en es es es es
  ysw_true=1  ysw_pred=1  ydur_true=0
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?

  [Spanish-English]  pos=2
  tokens : ▁Vo y ▁a ▁recordar ▁siempre ▁la ▁época ▁de
  langs  : es es en es es es es es
  ysw_true=1  ysw_pred=1  ydur_true=2
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?

  [Spanish-English]  pos=14
  tokens : , ▁you ▁know ? ▁Me ▁emocion a ▁mucho ▁pensar ▁en
  langs  : punct en en punct en es es es es es
  ysw_true=1  ysw_pred=1  ydur_true=2
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?


--- False Alarms — Inter-sentential (0 examples) ---

--- False Alarms — Intra-sentential (0 examples) ---

--- Missed Switches — Inter-sentential (3 examples) ---
  [Chinese-English]  pos=24
  tokens : ▁will ▁try ▁to ▁play ▁better . ▁ 我覺得 吉林 男
  langs  : en en en en en punct punct zh zh zh
  ysw_true=1  ysw_pred=0  ydur_true=2
  text   : 浙江稠州這場比賽贏得很輕鬆。 Next time, I believe the Jilin team will try to play better. 我覺得吉林男籃下次要加強防守。 If they work on their teamwo

  [Chinese-English]  pos=78
  tokens : ▁out ▁in ▁the ▁C BA . ▁ 這麼 大的 比分
  langs  : en en en en en punct punct zh zh zh
  ysw_true=1  ysw_pred=0  ydur_true=1
  text   : 浙江稠州這場比賽贏得很輕鬆。 Next time, I believe the Jilin team will try to play better. 我覺得吉林男籃下次要加強防守。 If they work on their teamwo

  [Spanish-English]  pos=17
  tokens : , ▁me ▁emocion é ▁mucho . ▁It ' s ▁amazing
  langs  : punct en es es es punct en punct en en
  ysw_true=1  ysw_pred=0  ydur_true=2
  text   : Cuando leí sobre el lanzamiento de GTA 5 Enhanced PC, me emocioné mucho. It's amazing how Rockstar keeps improving their


--- Missed Switches — Intra-sentential (3 examples) ---
  [Spanish-English]  pos=9
  tokens : ▁la ▁época ▁de ▁Fernando mania , ▁you ▁know ? ▁Me
  langs  : es es es es es punct en en punct en
  ysw_true=1  ysw_pred=0  ydur_true=1
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?

  [Spanish-English]  pos=37
  tokens : ▁que ▁vaya ▁al ▁esta dio , ▁I ' ll ▁think
  langs  : es es es es es punct en punct en en
  ysw_true=1  ysw_pred=0  ydur_true=2
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?

  [Chinese-English]  pos=8
  tokens : 员 说 得 真 好 ， " T rust ▁me
  langs  : zh zh zh zh zh punct punct en en en
  ysw_true=1  ysw_pred=0  ydur_true=2
  text   : 那个银行职员说得真好，"Trust me, it's a good investment," 但我还是有点不放心。 她想去银行存款，结果被保险公司的人忽悠，"It's just a small risk," 他说。 银行和保险公司一起欺骗了


======================================================================
QUALITATIVE EXAMPLES — MBERT
======================================================================

--- Successful Predictions — Inter-sentential (3 examples) ---
  [Spanish-English]  pos=29
  tokens : Vale ##nzu ##ela , right ? La próxima vez que
  langs  : es es es punct en punct es es es es
  ysw_true=1  ysw_pred=1  ydur_true=2
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?

  [Spanish-English]  pos=48
  tokens : of him , for sure . Def ##ini ##tiva ##mente
  langs  : en en punct en en punct es es es es
  ysw_true=1  ysw_pred=1  ydur_true=2
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?

  [Chinese-English]  pos=92
  tokens : 年 纪 大 的 人 。 " How could this
  langs  : zh zh zh zh zh punct punct en en en
  ysw_true=1  ysw_pred=1  ydur_true=1
  text   : 那个银行职员说得真好，"Trust me, it's a good investment," 但我还是有点不放心。 她想去银行存款，结果被保险公司的人忽悠，"It's just a small risk," 他说。 银行和保险公司一起欺骗了


--- Successful Predictions — Intra-sentential (3 examples) ---
  [Spanish-English]  pos=1
  tokens : Vo ##y a record ##ar siempre la
  langs  : es es en es es es es
  ysw_true=1  ysw_pred=1  ydur_true=0
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?

  [Spanish-English]  pos=2
  tokens : Vo ##y a record ##ar siempre la época
  langs  : es es en es es es es es
  ysw_true=1  ysw_pred=1  ydur_true=2
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?

  [Spanish-English]  pos=15
  tokens : , you know ? Me em ##oci ##ona mucho pensar
  langs  : punct en en punct en es es es es es
  ysw_true=1  ysw_pred=1  ydur_true=2
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?


--- False Alarms — Inter-sentential (0 examples) ---

--- False Alarms — Intra-sentential (0 examples) ---

--- Missed Switches — Inter-sentential (3 examples) ---
  [Chinese-English]  pos=98
  tokens : " How could this happen ? " 她 心 想
  langs  : punct en en en en punct punct zh zh zh
  ysw_true=1  ysw_pred=0  ydur_true=2
  text   : 那个银行职员说得真好，"Trust me, it's a good investment," 但我还是有点不放心。 她想去银行存款，结果被保险公司的人忽悠，"It's just a small risk," 他说。 银行和保险公司一起欺骗了

  [Chinese-English]  pos=132
  tokens : 保 险 销 售 员 。 " What a surprise
  langs  : zh zh zh zh zh punct punct en en en
  ysw_true=1  ysw_pred=0  ydur_true=1
  text   : 那个银行职员说得真好，"Trust me, it's a good investment," 但我还是有点不放心。 她想去银行存款，结果被保险公司的人忽悠，"It's just a small risk," 他说。 银行和保险公司一起欺骗了

  [Arabic-English]  pos=78
  tokens : ##جر ##بة التي تقدم ##ها . It ' s ex
  langs  : ar ar ar ar ar punct en punct en en
  ysw_true=1  ysw_pred=0  ydur_true=2
  text   : هل سمعتم عن لعبة Mighty Morphin' Power Rangers: Rita's Rewind التي ستصدر على Nintendo Switch في ديسمبر؟ Yes, the retro a


--- Missed Switches — Intra-sentential (3 examples) ---
  [Spanish-English]  pos=10
  tokens : la época de Fernando ##mania , you know ? Me
  langs  : es es es es es punct en en punct en
  ysw_true=1  ysw_pred=0  ydur_true=1
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?

  [Spanish-English]  pos=38
  tokens : que va ##ya al estadio , I ' ll think
  langs  : es es es es es punct en punct en en
  ysw_true=1  ysw_pred=0  ydur_true=2
  text   : Voy a recordar siempre la época de Fernandomania, you know? Me emociona mucho pensar en el impacto de Valenzuela, right?

  [Chinese-English]  pos=9
  tokens : 员 说 得 真 好 ， " Trust me ,
  langs  : zh zh zh zh zh punct punct en en punct
  ysw_true=1  ysw_pred=0  ydur_true=2
  text   : 那个银行职员说得真好，"Trust me, it's a good investment," 但我还是有点不放心。 她想去银行存款，结果被保险公司的人忽悠，"It's just a small risk," 他说。 银行和保险公司一起欺骗了