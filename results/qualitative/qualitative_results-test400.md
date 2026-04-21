# Qualitative Analysis Results

## Macro-Average Accuracy: Inter-sentential vs Intra-sentential

| Model | Type | F1 | Prec | Rec | DurAcc | #Switches |
|---|---|---|---|---|---|---|
| xlmr | inter | 0.7635 | 0.7408 | 0.7877 | 0.8361 | 537 |
| xlmr | intra | 0.4841 | 0.4919 | 0.4765 | 0.5548 | 894 |
| mbert | inter | 0.7078 | 0.7253 | 0.6911 | 0.8795 | 531 |
| mbert | intra | 0.4816 | 0.4700 | 0.4938 | 0.5614 | 887 |

## Qualitative Examples — XLMR

### Successful Predictions — Inter-sentential (10 examples)

```
[Chinese-English]  switch_type=inter  switch_token='经济发展'
  context : 有[zh]  决心[zh]  要[zh]  推动[zh]  >>经济发展[zh]<<  。[punct]  But[en]  ▁do[en]  ▁you[en]  ▁think[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='▁rate'
  context : ▁such[en]  ▁a[en]  ▁high[en]  ▁deficit[en]  >>▁rate[en]<<  ?[punct]  ▁[punct]  政府工作报告[zh]  说[zh]  要[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='活跃'
  context : ，[punct]  经济[zh]  可能会[zh]  更[zh]  >>活跃[zh]<<  。[punct]  How[en]  ever[en]  ,[punct]  ▁I[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='▁increasing'
  context : ▁the[en]  ▁deficit[en]  ▁keep[en]  s[en]  >>▁increasing[en]<<  .[punct]  ▁[punct]  赤[zh]  字[zh]  率[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='很强'
  context : 回[zh]  升[zh]  的[zh]  信心[zh]  >>很强[zh]<<  。[punct]  But[en]  ▁at[en]  ▁the[en]  ▁same[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁know'
  context : ▁있었[ko]  지[ko]  ,[punct]  ▁you[en]  >>▁know[en]<<  ?[punct]  ▁그때[ko]  는[ko]  ▁매일[ko]  매[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='ly'
  context : 했[ko]  어[ko]  ,[punct]  ▁honest[en]  >>ly[en]<<  .[punct]  ▁수[ko]  술[ko]  ▁받고[ko]  ▁나서[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁God'
  context : ▁있었[ko]  어[ko]  ,[punct]  ▁thank[en]  >>▁God[en]<<  .[punct]  ▁건강[ko]  을[ko]  ▁지키[ko]  는[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁है'
  context : ▁दौरान[hi]  ▁हिंसा[hi]  ▁भड़क[hi]  ▁गई[hi]  >>▁है[hi]<<  ।[punct]  ▁The[en]  ▁situation[en]  ▁in[en]  ▁Mur[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='ted'
  context : ▁the[en]  ▁protest[en]  s[en]  ▁escala[en]  >>ted[en]<<  .[punct]  ▁मु[hi]  र्[hi]  शि[hi]  द[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

### Successful Predictions — Intra-sentential (10 examples)

```
[Chinese-English]  switch_type=intra  switch_token='的作用'
  context : 发挥[zh]  民[zh]  营[zh]  经济[zh]  >>的作用[zh]<<  ，[punct]  drive[en]  ▁technolog[en]  ical[en]  ▁innovation[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='4%'
  context : 字[zh]  率[zh]  拟[zh]  按[zh]  >>4%[en]<<  左右[zh]  安排[zh]  ，[punct]  这[zh]  已经[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='4%'
  context : 赤[zh]  字[zh]  率[zh]  达到[zh]  >>4%[en]<<  左右[zh]  ，[punct]  其实[zh]  已经[zh]  超过[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='지'
  context : 었던[ko]  ▁시절[ko]  이[ko]  ▁있었[ko]  >>지[ko]<<  ,[punct]  ▁you[en]  ▁know[en]  ?[punct]  ▁그때[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='어'
  context : 일[ko]  이[ko]  ▁불안[ko]  했[ko]  >>어[ko]<<  ,[punct]  ▁honest[en]  ly[en]  .[punct]  ▁수[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='어'
  context : 심[ko]  할[ko]  ▁수[ko]  ▁있었[ko]  >>어[ko]<<  ,[punct]  ▁thank[en]  ▁God[en]  .[punct]  ▁건강[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='어'
  context : ▁한[ko]  ▁번[ko]  ▁느[ko]  꼈[ko]  >>어[ko]<<  ,[punct]  ▁right[en]  ?[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁han'
  context : ▁mostrando[es]  ▁lo[es]  ▁lejos[es]  ▁que[es]  >>▁han[en]<<  ▁llegado[es]  ▁en[es]  ▁tecnología[es]  ▁espacial[es]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='說'
  context : 新聞[zh]  ，[punct]  然後[zh]  會[zh]  >>說[zh]<<  ，[punct]  I[en]  ▁think[en]  ▁Tiger[en]  ▁Wood[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='s'
  context : ción[es]  ▁enfrenta[es]  ▁muchos[es]  ▁desafío[es]  >>s[es]<<  ,[punct]  ▁especially[en]  ▁regarding[en]  ▁political[en]  ▁stabilit[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

### False Alarms — Inter-sentential (10 examples)

```
[Chinese-English]  switch_type=inter  switch_token='▁development'
  context : ▁promote[en]  ▁high[en]  -[punct]  quality[en]  >>▁development[en]<<  。[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Spanish-English]  switch_type=inter  switch_token='▁involved'
  context : ▁think[en]  ▁about[en]  ▁the[en]  ▁challenges[en]  >>▁involved[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Hindi-English]  switch_type=inter  switch_token='▁order'
  context : ▁to[en]  ▁maintain[en]  ▁peace[en]  ▁and[en]  >>▁order[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Korean-English]  switch_type=inter  switch_token='s'
  context : ▁it[en]  ▁to[en]  ▁the[en]  ▁national[en]  >>s[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=inter  switch_token='s'
  context : ▁sports[en]  ▁and[en]  ▁entertainment[en]  ▁world[en]  >>s[en]<<  。[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Spanish-English]  switch_type=inter  switch_token='▁trust'
  context : ▁stabilit[en]  y[en]  ▁and[en]  ▁public[en]  >>▁trust[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[French-English]  switch_type=inter  switch_token='able'
  context : ’[punct]  émotion[fr]  ▁était[en]  ▁palp[en]  >>able[en]<<  .[punct]  ▁The[en]  ▁way[en]  ▁Key[en]  n[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[French-English]  switch_type=inter  switch_token='▁everywhere'
  context : ▁mud[en]  ▁is[en]  ▁still[en]  ▁left[en]  >>▁everywhere[en]<<  .[punct]  ▁J[en]  '[punct]  espère[fr]  ▁que[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[French-English]  switch_type=inter  switch_token='univers'
  context : ▁compréhension[fr]  ▁de[fr]  ▁l[fr]  ’[punct]  >>univers[fr]<<  .[punct]  ▁This[fr]  ▁is[en]  ▁exactly[en]  ▁why[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[French-English]  switch_type=inter  switch_token='line'
  context : ▁vraiment[en]  ▁la[fr]  ▁pun[fr]  ch[fr]  >>line[fr]<<  .[punct]  ▁La[fr]  ▁nation[fr]  ,[punct]  ▁c[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

### False Alarms — Intra-sentential (10 examples)

```
[Chinese-English]  switch_type=intra  switch_token='1'
  context : 已经[zh]  比[zh]  去年[zh]  提高了[zh]  >>1[zh]<<  个百分点[zh]  ，[punct]  政府[zh]  真的很[zh]  有[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=intra  switch_token='个百分点'
  context : 比[zh]  去年[zh]  提高了[zh]  1[zh]  >>个百分点[zh]<<  ，[punct]  政府[zh]  真的很[zh]  有[zh]  决心[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=intra  switch_token='决心'
  context : ，[punct]  政府[zh]  真的很[zh]  有[zh]  >>决心[zh]<<  要[zh]  推动[zh]  经济发展[zh]  。[punct]  But[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=intra  switch_token='▁deficit'
  context : ▁with[en]  ▁such[en]  ▁a[en]  ▁high[en]  >>▁deficit[en]<<  ▁rate[en]  ?[punct]  ▁[punct]  政府工作报告[zh]  说[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=intra  switch_token='高峰'
  context : 2020[zh]  年[zh]  疫[zh]  情[zh]  >>高峰[zh]<<  时[zh]  的[zh]  水平[zh]  ，[punct]  这[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=intra  switch_token='水平'
  context : 情[zh]  高峰[zh]  时[zh]  的[zh]  >>水平[zh]<<  ，[punct]  这[zh]  说明[zh]  中央[zh]  对[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Korean-English]  switch_type=intra  switch_token='지'
  context : 는[ko]  ▁게[ko]  ▁얼마나[ko]  ▁중요한[ko]  >>지[ko]<<  ▁다시[ko]  ▁한[ko]  ▁번[ko]  ▁느[ko]  꼈[ko]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Spanish-English]  switch_type=intra  switch_token='▁entre'
  context : ▁establecer[es]  ▁una[es]  ▁base[en]  ▁lunar[es]  >>▁entre[es]<<  ▁Estados[es]  ▁Unidos[es]  ▁y[es]  ▁China[es]  ▁está[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Spanish-English]  switch_type=intra  switch_token='▁China'
  context : ▁entre[es]  ▁Estados[es]  ▁Unidos[es]  ▁y[es]  >>▁China[es]<<  ▁está[es]  ▁aumentando[es]  ▁cada[es]  ▁día[es]  ,[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Spanish-English]  switch_type=intra  switch_token='▁aumentando'
  context : ▁Unidos[es]  ▁y[es]  ▁China[es]  ▁está[es]  >>▁aumentando[es]<<  ▁cada[es]  ▁día[es]  ,[punct]  ▁mostrando[es]  ▁lo[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

### Missed Switches — Inter-sentential (10 examples)

```
[Spanish-English]  switch_type=inter  switch_token='▁espacial'
  context : ▁han[en]  ▁llegado[es]  ▁en[es]  ▁tecnología[es]  >>▁espacial[es]<<  .[punct]  ▁Both[en]  ▁countries[en]  ▁want[en]  ▁to[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁निकाल'
  context : ▁में[hi]  ▁जु[hi]  लू[hi]  स[hi]  >>▁निकाल[hi]<<  ा[punct]  ।[punct]  ▁Author[en]  ities[en]  ▁are[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='진다'
  context : 흥[ko]  미[ko]  로[ko]  워[ko]  >>진다[ko]<<  .[punct]  ▁The[en]  ▁NC[en]  AA[en]  ▁just[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁ranking'
  context : ▁could[en]  ▁affect[en]  ▁your[en]  ▁national[en]  >>▁ranking[en]<<  .[punct]  ▁[punct]  컨[ko]  퍼[ko]  런[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='아'
  context : ▁영향을[ko]  ▁줄[ko]  ▁것[ko]  ▁같[ko]  >>아[ko]<<  .[punct]  ▁I[en]  ▁can[en]  '[punct]  t[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁know'
  context : ▁a[en]  ▁scientist[en]  ,[punct]  ▁you[en]  >>▁know[en]<<  ?[punct]  ▁Je[fr]  ▁vais[en]  ▁présenter[en]  ▁nos[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='아'
  context : ▁많이[ko]  ▁올[ko]  ▁것[ko]  ▁같[ko]  >>아[ko]<<  .[punct]  ▁The[en]  ▁news[en]  ▁said[en]  ▁there[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁해'
  context : ▁조[ko]  심[ko]  하[ko]  라고[ko]  >>▁해[ko]<<  .[punct]  ▁F[en]  lood[en]  s[en]  ▁can[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁twist'
  context : ▁especially[en]  ▁after[en]  ▁that[en]  ▁crazy[en]  >>▁twist[en]<<  ![punct]  ▁Seguro[es]  ▁que[es]  ▁van[en]  ▁a[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='ة'
  context : ▁ظروف[ar]  ▁ج[ar]  فاف[ar]  ▁شديد[ar]  >>ة[ar]<<  .[punct]  ▁Water[en]  ▁management[en]  ▁policies[en]  ▁have[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

### Missed Switches — Intra-sentential (10 examples)

```
[Chinese-English]  switch_type=intra  switch_token='按'
  context : 赤[zh]  字[zh]  率[zh]  拟[zh]  >>按[zh]<<  4%[en]  左右[zh]  安排[zh]  ，[punct]  这[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='达到'
  context : ▁[punct]  赤[zh]  字[zh]  率[zh]  >>达到[zh]<<  4%[en]  左右[zh]  ，[punct]  其实[zh]  已经[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁una'
  context : ▁La[es]  ▁competencia[es]  ▁por[es]  ▁establecer[es]  >>▁una[es]<<  ▁base[en]  ▁lunar[es]  ▁entre[es]  ▁Estados[es]  ▁Unidos[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁base'
  context : ▁competencia[es]  ▁por[es]  ▁establecer[es]  ▁una[es]  >>▁base[en]<<  ▁lunar[es]  ▁entre[es]  ▁Estados[es]  ▁Unidos[es]  ▁y[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁que'
  context : ,[punct]  ▁mostrando[es]  ▁lo[es]  ▁lejos[es]  >>▁que[es]<<  ▁han[en]  ▁llegado[es]  ▁en[es]  ▁tecnología[es]  ▁espacial[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='真的很'
  context : 這件事[zh]  ，[punct]  因為[zh]  這[zh]  >>真的很[zh]<<  ▁surprising[en]  ▁for[en]  ▁both[en]  ▁the[en]  ▁sports[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='émotion'
  context : ▁franchement[fr]  ,[punct]  ▁l[fr]  ’[punct]  >>émotion[fr]<<  ▁était[en]  ▁palp[en]  able[en]  .[punct]  ▁The[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='生活'
  context : 因为[zh]  这些问题[zh]  影响[zh]  了[zh]  >>生活[zh]<<  ,[punct]  ▁right[en]  ?[punct]  ▁[punct]  有时候[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='很'
  context : 状况[zh]  ，[punct]  我真的[zh]  觉得[zh]  >>很[zh]<<  sur[en]  pris[en]  ed[en]  ![punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁especially'
  context : ▁à[fr]  ▁netto[fr]  yer[fr]  ,[punct]  >>▁especially[fr]<<  ▁after[en]  ▁seeing[en]  ▁how[en]  ▁much[en]  ▁mud[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

## Qualitative Examples — MBERT

### Successful Predictions — Inter-sentential (10 examples)

```
[Chinese-English]  switch_type=inter  switch_token='展'
  context : 动[zh]  经[zh]  济[zh]  发[zh]  >>展[zh]<<  。[punct]  But[en]  do[en]  you[en]  think[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='rate'
  context : such[en]  a[en]  high[en]  deficit[en]  >>rate[en]<<  ?[punct]  政[zh]  府[zh]  工[zh]  作[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='跃'
  context : 能[zh]  会[zh]  更[zh]  活[zh]  >>跃[zh]<<  。[punct]  However[en]  ,[punct]  I[en]  '[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='increasing'
  context : if[en]  the[en]  deficit[en]  keeps[en]  >>increasing[en]<<  .[punct]  赤[zh]  字[zh]  率[zh]  达[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='强'
  context : 的[zh]  信[zh]  心[zh]  很[zh]  >>强[zh]<<  。[punct]  But[en]  at[en]  the[en]  same[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='know'
  context : ##었[ko]  ##지[ko]  ,[punct]  you[en]  >>know[en]<<  ?[punct]  그[ko]  ##때[ko]  ##는[ko]  매[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##ly'
  context : ##어[ko]  ,[punct]  hon[en]  ##est[en]  >>##ly[en]<<  .[punct]  수[ko]  ##술[ko]  받고[ko]  나[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='God'
  context : ##어[ko]  ,[punct]  than[en]  ##k[en]  >>God[en]<<  .[punct]  건[ko]  ##강[ko]  ##을[ko]  지[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='espacial'
  context : han[en]  llegado[es]  en[es]  tecnología[es]  >>espacial[es]<<  .[punct]  Both[en]  countries[en]  want[en]  to[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='है'
  context : भ[hi]  ##ड़[hi]  ##क[hi]  गई[hi]  >>है[hi]<<  ।[punct]  The[en]  situation[en]  in[en]  Mur[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

### Successful Predictions — Intra-sentential (10 examples)

```
[Chinese-English]  switch_type=intra  switch_token='用'
  context : 经[zh]  济[zh]  的[zh]  作[zh]  >>用[zh]<<  ，[punct]  drive[en]  tech[en]  ##nological[en]  innovation[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##어'
  context : ##할[ko]  수[ko]  있[ko]  ##었[ko]  >>##어[ko]<<  ,[punct]  than[en]  ##k[en]  God[en]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##어'
  context : 한[ko]  번[ko]  느[ko]  ##꼈[ko]  >>##어[ko]<<  ,[punct]  right[en]  ?[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='han'
  context : mostrando[es]  lo[es]  lejos[es]  que[es]  >>han[en]<<  llegado[es]  en[es]  tecnología[es]  espacial[es]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='大'
  context : 得[zh]  压[zh]  力[zh]  好[zh]  >>大[zh]<<  ,[punct]  you[en]  know[en]  ?[punct]  其[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='息'
  context : 饮[zh]  食[zh]  和[zh]  作[zh]  >>息[zh]<<  ,[punct]  seriously[en]  ![punct]  看[zh]  到[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='##ge'
  context : du[fr]  net[fr]  ##to[fr]  ##ya[fr]  >>##ge[fr]<<  ,[punct]  but[en]  if[en]  it[en]  rain[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##عاء'
  context : ص[ar]  ##حة[ar]  ال[ar]  ##أم[ar]  >>##عاء[ar]<<  ،[punct]  right[en]  ؟[punct]  ك[ar]  ##نت[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##د'
  context : ##ذا[ar]  ##ئي[ar]  ال[ar]  ##جي[ar]  >>##د[ar]<<  ،[punct]  don[en]  '[punct]  t[en]  you[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
```

```
[French-English]  switch_type=intra  switch_token='##ble'
  context : ##é[fr]  in[en]  ##cro[en]  ##ya[en]  >>##ble[en]<<  pour[fr]  notre[en]  équipe[en]  .[punct]  Being[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
```

### False Alarms — Inter-sentential (10 examples)

```
[Chinese-English]  switch_type=inter  switch_token='development'
  context : promote[en]  high[en]  -[punct]  quality[en]  >>development[en]<<  。[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Spanish-English]  switch_type=inter  switch_token='involved'
  context : think[en]  about[en]  the[en]  challenges[en]  >>involved[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=inter  switch_token='##s'
  context : sports[en]  and[en]  entertainment[en]  world[en]  >>##s[en]<<  。[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[French-English]  switch_type=inter  switch_token='##ble'
  context : ##ion[fr]  était[en]  pal[en]  ##pa[en]  >>##ble[en]<<  .[punct]  The[en]  way[en]  Key[en]  ##n[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[French-English]  switch_type=inter  switch_token='##where'
  context : is[en]  still[en]  left[en]  every[en]  >>##where[en]<<  .[punct]  J[en]  '[punct]  es[en]  ##p[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[French-English]  switch_type=inter  switch_token='univers'
  context : ##ension[fr]  de[fr]  l[fr]  [UNK][fr]  >>univers[fr]<<  .[punct]  This[fr]  is[en]  exactly[en]  why[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[French-English]  switch_type=inter  switch_token='équipe'
  context : ##ya[en]  ##ble[en]  pour[fr]  notre[en]  >>équipe[en]<<  .[punct]  Being[en]  able[en]  to[en]  contribute[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[French-English]  switch_type=inter  switch_token='sea'
  context : the[en]  bottom[en]  of[en]  the[en]  >>sea[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[French-English]  switch_type=inter  switch_token='##line'
  context : vraiment[fr]  la[fr]  pun[fr]  ##ch[fr]  >>##line[fr]<<  .[punct]  La[fr]  nation[fr]  ,[punct]  c[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Spanish-English]  switch_type=inter  switch_token='##s'
  context : cosas[es]  aún[es]  más[es]  intensa[es]  >>##s[es]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

### False Alarms — Intra-sentential (10 examples)

```
[Chinese-English]  switch_type=intra  switch_token='了'
  context : 去[zh]  年[zh]  提[zh]  高[zh]  >>了[zh]<<  1[zh]  个[zh]  百[zh]  分[zh]  点[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=intra  switch_token='1'
  context : 年[zh]  提[zh]  高[zh]  了[zh]  >>1[zh]<<  个[zh]  百[zh]  分[zh]  点[zh]  ，[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=intra  switch_token='点'
  context : 1[zh]  个[zh]  百[zh]  分[zh]  >>点[zh]<<  ，[punct]  政[zh]  府[zh]  真[zh]  的[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=intra  switch_token='心'
  context : 的[zh]  很[zh]  有[zh]  决[zh]  >>心[zh]<<  要[zh]  推[zh]  动[zh]  经[zh]  济[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=intra  switch_token='资'
  context : 础[zh]  设[zh]  施[zh]  投[zh]  >>资[zh]<<  ，[punct]  经[zh]  济[zh]  可[zh]  能[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=intra  switch_token='情'
  context : 了[zh]  2020[zh]  年[zh]  疫[zh]  >>情[zh]<<  高[zh]  峰[zh]  时[zh]  的[zh]  水[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=intra  switch_token='峰'
  context : 年[zh]  疫[zh]  情[zh]  高[zh]  >>峰[zh]<<  时[zh]  的[zh]  水[zh]  平[zh]  ，[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Chinese-English]  switch_type=intra  switch_token='平'
  context : 峰[zh]  时[zh]  的[zh]  水[zh]  >>平[zh]<<  ，[punct]  这[zh]  说[zh]  明[zh]  中[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Korean-English]  switch_type=intra  switch_token='중요한'
  context : 게[ko]  얼[ko]  ##마[ko]  ##나[ko]  >>중요한[ko]<<  ##지[ko]  다시[ko]  한[ko]  번[ko]  느[ko]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

```
[Spanish-English]  switch_type=intra  switch_token='lunar'
  context : por[es]  establecer[es]  una[es]  base[en]  >>lunar[es]<<  entre[es]  Estados[es]  Unidos[es]  y[es]  China[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
```

### Missed Switches — Inter-sentential (10 examples)

```
[Hindi-English]  switch_type=inter  switch_token='##ला'
  context : जुल[hi]  ##ूस[hi]  न[hi]  ##िका[hi]  >>##ला[hi]<<  ।[punct]  Author[en]  ##ities[en]  are[en]  ur[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##아'
  context : ##장[ko]  ##할[ko]  것[ko]  같[ko]  >>##아[ko]<<  .[punct]  It[en]  must[en]  be[en]  tou[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='ranking'
  context : could[en]  affect[en]  your[en]  national[en]  >>ranking[en]<<  .[punct]  컨[ko]  ##퍼[ko]  ##런[ko]  ##스[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='해'
  context : 느[ko]  ##껴[ko]  ##지[ko]  ##기도[ko]  >>해[ko]<<  .[punct]  Some[en]  conferences[en]  are[en]  clearly[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='year'
  context : clearly[en]  more[en]  competitive[en]  this[en]  >>year[en]<<  .[punct]  이[ko]  ##번[ko]  토[ko]  ##너[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##아'
  context : 영향을[ko]  줄[ko]  것[ko]  같[ko]  >>##아[ko]<<  .[punct]  I[en]  can[en]  '[punct]  t[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='sure'
  context : the[en]  news[en]  ,[punct]  for[en]  >>sure[en]<<  .[punct]  À[fr]  l[fr]  [UNK][fr]  avenir[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##아'
  context : 많이[ko]  올[ko]  것[ko]  같[ko]  >>##아[ko]<<  .[punct]  The[en]  news[en]  said[en]  there[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##야'
  context : ##가지[ko]  않[ko]  ##을[ko]  거[ko]  >>##야[ko]<<  .[punct]  I[en]  think[en]  it[en]  '[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='해'
  context : 조[ko]  ##심[ko]  ##하라[ko]  ##고[ko]  >>해[ko]<<  .[punct]  Flood[en]  ##s[en]  can[en]  happen[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

### Missed Switches — Intra-sentential (10 examples)

```
[Korean-English]  switch_type=intra  switch_token='##지'
  context : ##절[ko]  ##이[ko]  있[ko]  ##었[ko]  >>##지[ko]<<  ,[punct]  you[en]  know[en]  ?[punct]  그[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##어'
  context : ##이[ko]  불[ko]  ##안[ko]  ##했[ko]  >>##어[ko]<<  ,[punct]  hon[en]  ##est[en]  ##ly[en]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='una'
  context : La[es]  competencia[es]  por[es]  establecer[es]  >>una[es]<<  base[en]  lunar[es]  entre[es]  Estados[es]  Unidos[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='base'
  context : competencia[es]  por[es]  establecer[es]  una[es]  >>base[en]<<  lunar[es]  entre[es]  Estados[es]  Unidos[es]  y[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='que'
  context : ,[punct]  mostrando[es]  lo[es]  lejos[es]  >>que[es]<<  han[en]  llegado[es]  en[es]  tecnología[es]  espacial[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='說'
  context : ，[punct]  然[zh]  後[zh]  會[zh]  >>說[zh]<<  ，[punct]  I[en]  think[en]  Tiger[en]  Woods[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='很'
  context : 為[zh]  這[zh]  真[zh]  的[zh]  >>很[zh]<<  sur[en]  ##pris[en]  ##ing[en]  for[en]  both[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='##íos'
  context : ##nta[es]  muchos[es]  desa[es]  ##f[es]  >>##íos[es]<<  ,[punct]  especially[en]  regarding[en]  political[en]  stability[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='##ion'
  context : l[fr]  [UNK][fr]  é[fr]  ##mot[fr]  >>##ion[fr]<<  était[en]  pal[en]  ##pa[en]  ##ble[en]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='活'
  context : 影[zh]  响[zh]  了[zh]  生[zh]  >>活[zh]<<  ,[punct]  right[en]  ?[punct]  有[zh]  时[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
```
