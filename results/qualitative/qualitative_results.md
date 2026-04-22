# Qualitative Analysis Results

## Global: Inter-sentential vs Intra-sentential

| Model | Type | F1 | Prec | Rec | DurAcc | #Switches |
|---|---|---|---|---|---|---|
| xlmr | inter | 0.7404 | 0.7385 | 0.7423 | 0.8100 | 12035 |
| xlmr | intra | 0.4889 | 0.5270 | 0.4560 | 0.5346 | 21661 |
| mbert | inter | 0.6988 | 0.7361 | 0.6650 | 0.8495 | 12081 |
| mbert | intra | 0.4789 | 0.4871 | 0.4710 | 0.5577 | 21189 |

## Per Language Pair: Inter-sentential vs Intra-sentential

| Pair | Model | Type | F1 | Prec | Rec | DurAcc | #Switches |
|---|---|---|---|---|---|---|---|
| Arabic-English | xlmr | inter | 0.7831 | 0.8268 | 0.7438 | 0.8775 | 2073 |
| Arabic-English | xlmr | intra | 0.5226 | 0.5487 | 0.4988 | 0.5602 | 2608 |
| Arabic-English | mbert | inter | 0.7531 | 0.8198 | 0.6963 | 0.9254 | 2078 |
| Arabic-English | mbert | intra | 0.4995 | 0.5160 | 0.4841 | 0.5355 | 2603 |
| Chinese-English | xlmr | inter | 0.8174 | 0.8356 | 0.8001 | 0.8607 | 3036 |
| Chinese-English | xlmr | intra | 0.5388 | 0.5487 | 0.5292 | 0.5540 | 3184 |
| Chinese-English | mbert | inter | 0.7695 | 0.8187 | 0.7260 | 0.9281 | 3047 |
| Chinese-English | mbert | intra | 0.5374 | 0.5453 | 0.5296 | 0.6133 | 3408 |
| French-English | xlmr | inter | 0.4230 | 0.3306 | 0.5869 | 0.6868 | 1041 |
| French-English | xlmr | intra | 0.1188 | 0.1244 | 0.1136 | 0.3341 | 4516 |
| French-English | mbert | inter | 0.4220 | 0.3362 | 0.5667 | 0.7419 | 1050 |
| French-English | mbert | intra | 0.1277 | 0.1109 | 0.1504 | 0.3821 | 3756 |
| Hindi-English | xlmr | inter | 0.7824 | 0.8095 | 0.7571 | 0.7624 | 1128 |
| Hindi-English | xlmr | intra | 0.6317 | 0.7320 | 0.5556 | 0.6015 | 2743 |
| Hindi-English | mbert | inter | 0.7470 | 0.8245 | 0.6828 | 0.8044 | 1135 |
| Hindi-English | mbert | intra | 0.6380 | 0.6850 | 0.5969 | 0.5777 | 2754 |
| Korean-English | xlmr | inter | 0.7749 | 0.8222 | 0.7328 | 0.8827 | 2676 |
| Korean-English | xlmr | intra | 0.6113 | 0.6957 | 0.5452 | 0.5586 | 2458 |
| Korean-English | mbert | inter | 0.6878 | 0.8277 | 0.5883 | 0.9067 | 2679 |
| Korean-English | mbert | intra | 0.4918 | 0.5984 | 0.4175 | 0.5730 | 2527 |
| Spanish-English | xlmr | inter | 0.7462 | 0.7544 | 0.7381 | 0.6627 | 2081 |
| Spanish-English | xlmr | intra | 0.6208 | 0.6796 | 0.5714 | 0.6214 | 6152 |
| Spanish-English | mbert | inter | 0.7282 | 0.7796 | 0.6831 | 0.6649 | 2092 |
| Spanish-English | mbert | intra | 0.6284 | 0.6667 | 0.5944 | 0.6284 | 6141 |

## Qualitative Examples — XLMR

### Successful Predictions — Inter-sentential (48 examples)

```
[Korean-English]  switch_type=inter  switch_token='▁know'
  context : 다고[ko]  ▁생각해[ko]  ,[punct]  ▁you[en]  >>▁know[en]<<  ?[punct]  ▁이런[ko]  ▁일이[ko]  ▁언론[ko]  계[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁know'
  context : ▁agir[fr]  ▁rapidement[fr]  ,[punct]  ▁you[fr]  >>▁know[fr]<<  ?[punct]  ▁On[en]  ▁va[fr]  ▁sûr[fr]  ement[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='cular'
  context : ▁to[en]  ▁be[en]  ▁[punct]  specta[en]  >>cular[en]<<  ![punct]  ▁그럼[ko]  ▁오늘[ko]  ▁밤[ko]  에[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁them'
  context : ▁place[en]  ▁was[en]  ▁unexpected[en]  ▁for[en]  >>▁them[en]<<  .[punct]  ▁Après[fr]  ▁quelques[fr]  ▁seconde[fr]  s[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁it'
  context : ▁really[en]  ▁looking[en]  ▁forward[en]  ▁to[en]  >>▁it[en]<<  .[punct]  ▁나는[ko]  ▁그[ko]  ▁영화[ko]  가[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='ly'
  context : ▁بيانات[ar]  ي[ar]  ,[punct]  ▁honest[en]  >>ly[en]<<  ![punct]  ▁أحب[ar]  ▁أ[ar]  تابع[ar]  ▁أخبار[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='ology'
  context : y[en]  ▁in[en]  ▁pale[en]  ont[en]  >>ology[en]<<  .[punct]  ▁كنت[ar]  ▁دائما[ar]  ً[punct]  ▁م[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁much'
  context : ▁things[en]  ▁have[en]  ▁changed[en]  ▁so[en]  >>▁much[en]<<  .[punct]  ▁Di[es]  jo[es]  ▁que[es]  ▁tras[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='이다'
  context : ▁[punct]  점이[ko]  ▁인상[ko]  적[ko]  >>이다[ko]<<  .[punct]  ▁She[en]  ▁appreciate[en]  s[en]  ▁when[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁right'
  context : 진[ko]  ▁것[ko]  ▁같아요[ko]  ,[punct]  >>▁right[en]<<  ?[punct]  ▁개인[ko]  화[ko]  ▁옵션[ko]  이[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁hit'
  context : ▁it[en]  ▁was[en]  ▁a[en]  ▁huge[en]  >>▁hit[en]<<  ![punct]  ▁La[fr]  ▁fête[fr]  ▁était[en]  ▁super[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁हैं'
  context : ,[punct]  ▁क्या[hi]  ▁वो[hi]  ▁पर्याप्त[hi]  >>▁हैं[hi]<<  ?[punct]  ▁Sometimes[en]  ,[punct]  ▁I[en]  ▁feel[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='▁know'
  context : 政策[zh]  变化[zh]  ，[punct]  you[en]  >>▁know[en]<<  ?[punct]  ▁[punct]  债券[zh]  净[zh]  融资[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁है'
  context : ▁का[hi]  ▁माहौल[hi]  ▁बहुत[hi]  ▁गरम[hi]  >>▁है[hi]<<  ।[punct]  ▁The[en]  ▁youth[en]  ▁are[en]  ▁e[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁know'
  context : ▁más[es]  ▁atención[es]  ,[punct]  ▁you[en]  >>▁know[en]<<  ?[punct]  ▁Ella[es]  ▁empezar[es]  á[es]  ▁una[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='입니다'
  context : ▁데[ko]  ▁꼭[ko]  ▁필요한[ko]  ▁도구[ko]  >>입니다[ko]<<  .[punct]  ▁It[en]  ▁helps[en]  ▁us[en]  ▁solve[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='ائي'
  context : ائل[ar]  تي[ar]  ▁وأ[ar]  صدق[ar]  >>ائي[ar]<<  .[punct]  ▁We[en]  ▁need[en]  ▁to[en]  ▁stay[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='有趣'
  context : 的[zh]  番茄[zh]  ，[punct]  真的很[zh]  >>有趣[zh]<<  ！[punct]  ▁Did[en]  ▁you[en]  ▁know[en]  ▁that[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='▁family'
  context : ▁on[en]  ▁TV[en]  ▁with[en]  ▁my[en]  >>▁family[en]<<  .[punct]  ▁[punct]  中美[zh]  关系[zh]  的[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='里程碑'
  context : 视为[zh]  两国[zh]  关系[zh]  的[zh]  >>里程碑[zh]<<  。[punct]  ▁It[en]  '[punct]  s[en]  ▁a[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='▁forward'
  context : ▁push[en]  ed[en]  ▁the[en]  ▁industry[en]  >>▁forward[en]<<  .[punct]  ▁[punct]  很多[zh]  公司[zh]  因为[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='ly'
  context : ▁mental[en]  ly[en]  ▁and[en]  ▁physical[en]  >>ly[en]<<  .[punct]  ▁أنا[ar]  ▁و[ar]  صاحب[ar]  ي[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁amis'
  context : ▁la[fr]  ▁télévision[fr]  ▁avec[fr]  ▁mes[fr]  >>▁amis[fr]<<  .[punct]  ▁We[en]  ▁used[en]  ▁to[en]  ▁get[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁gaming'
  context : ▁tiene[es]  ▁mejor[es]  ▁rendimiento[es]  ▁for[en]  >>▁gaming[en]<<  ?[punct]  ▁La[es]  ▁tecnología[es]  ▁avanza[es]  ▁muy[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁था'
  context : ▁के[hi]  ▁बारे[hi]  ▁में[hi]  ▁सुना[hi]  >>▁था[hi]<<  ।[punct]  ▁He[en]  ▁was[en]  ▁quite[en]  ▁surprised[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁know'
  context : '[punct]  achat[en]  ,[punct]  ▁you[en]  >>▁know[en]<<  ?[punct]  ▁Le[fr]  ▁gouvernement[fr]  ▁avait[fr]  ▁en[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁right'
  context : ▁बहुत[hi]  ▁खास[hi]  ▁होगी[hi]  ,[punct]  >>▁right[en]<<  ?[punct]  ▁मैंने[hi]  ▁सुना[hi]  ▁है[hi]  ▁कि[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁know'
  context : صنع[ar]  ▁شيء[ar]  ،[punct]  ▁you[en]  >>▁know[en]<<  ؟[punct]  ▁هذا[ar]  ▁الشخص[ar]  ▁مسؤول[ar]  ▁عن[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='ين'
  context : لات[ar]  ▁بين[ar]  ▁الم[ar]  شجع[ar]  >>ين[ar]<<  .[punct]  ▁Fans[en]  ▁are[en]  ▁e[en]  ager[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁है'
  context : ▁sound[en]  ▁quality[en]  ▁काफी[hi]  ▁impressive[en]  >>▁है[hi]<<  ।[punct]  ▁They[en]  ▁want[en]  ▁to[en]  ▁try[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁monde'
  context : ▁plus[fr]  ▁sain[fr]  s[fr]  ▁du[fr]  >>▁monde[fr]<<  .[punct]  ▁After[en]  ▁reading[en]  ▁the[en]  ▁article[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁situation'
  context : ▁cop[en]  e[en]  ▁with[en]  ▁the[en]  >>▁situation[en]<<  .[punct]  ▁Las[es]  ▁relaciones[es]  ▁comerciales[es]  ▁entre[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁right'
  context : ▁un[es]  ▁juego[es]  ▁terrible[es]  ,[punct]  >>▁right[en]<<  ?[punct]  ▁Nunca[es]  ▁lograr[es]  on[es]  ▁una[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='하다'
  context : ▁남[ko]  을[ko]  지[ko]  ▁궁금[ko]  >>하다[ko]<<  .[punct]  ▁Her[en]  ▁[punct]  lega[en]  cy[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁changed'
  context : ,[punct]  ▁things[en]  ▁have[en]  ▁totally[en]  >>▁changed[en]<<  .[punct]  ▁أنا[ar]  ▁م[ar]  هتم[ar]  ة[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='▁values'
  context : ▁reflect[en]  s[en]  ▁her[en]  ▁true[en]  >>▁values[en]<<  。[punct]  ▁她[zh]  为[zh]  家庭[zh]  付出[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁जाएगी'
  context : ▁कीमत[hi]  ▁फिर[hi]  ▁से[hi]  ▁बढ़[hi]  >>▁जाएगी[hi]<<  ।[punct]  ▁That[en]  ’[punct]  s[en]  ▁a[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁muchos'
  context : ▁Unidos[es]  ▁sorprend[es]  ieron[es]  ▁a[en]  >>▁muchos[es]<<  .[punct]  ▁It[en]  ▁felt[en]  ▁like[en]  ▁a[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='▁consequences'
  context : ▁to[en]  ▁disa[en]  stro[en]  us[en]  >>▁consequences[en]<<  。[punct]  特朗普[zh]  强调[zh]  ，[punct]  他[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁है'
  context : ब[hi]  ग[hi]  ▁बहुत[hi]  ▁खतरनाक[hi]  >>▁है[hi]<<  ।[punct]  ▁People[en]  ▁really[en]  ▁need[en]  ▁to[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='▁forward'
  context : s[en]  ▁will[en]  ▁drive[en]  ▁us[en]  >>▁forward[en]<<  .[punct]  ▁中国[zh]  式[zh]  现代化[zh]  的[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁mucho'
  context : ▁y[es]  ▁me[en]  ▁impresion[es]  aron[es]  >>▁mucho[es]<<  .[punct]  ▁This[en]  ▁year[en]  ,[punct]  ▁I[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁colon'
  context : ▁con[es]  ▁el[es]  ▁cáncer[es]  ▁de[es]  >>▁colon[es]<<  .[punct]  ▁He[en]  ▁encourage[en]  d[en]  ▁everyone[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁थी'
  context : ▁जांच[hi]  ▁शुरू[hi]  ▁कर[hi]  ▁दी[hi]  >>▁थी[hi]<<  ।[punct]  ▁Many[en]  ▁people[en]  ▁question[en]  ed[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁field'
  context : ▁impressed[en]  ▁everyone[en]  ▁on[en]  ▁the[en]  >>▁field[en]<<  .[punct]  ▁في[ar]  ▁النهاية[ar]  ،[punct]  ▁الفريق[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='euses'
  context : ▁bac[fr]  téri[fr]  es[fr]  ▁danger[fr]  >>euses[fr]<<  .[punct]  ▁The[en]  ▁study[en]  ▁showed[en]  ▁how[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁families'
  context : ▁will[en]  ▁definitely[en]  ▁impact[en]  ▁many[en]  >>▁families[en]<<  .[punct]  ▁직원들[ko]  의[ko]  ▁불안[ko]  감이[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='over'
  context : ▁that[en]  ▁kind[en]  ▁of[en]  ▁make[en]  >>over[en]<<  .[punct]  ▁De[fr]  main[fr]  ,[punct]  ▁il[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

### Successful Predictions — Intra-sentential (48 examples)

```
[Korean-English]  switch_type=intra  switch_token='▁않아'
  context : 은[ko]  ▁[punct]  흔[ko]  치[ko]  >>▁않아[ko]<<  ,[punct]  ▁trust[en]  ▁me[en]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁de'
  context : ▁ver[en]  ▁la[es]  ▁nueva[es]  ▁película[es]  >>▁de[es]<<  ▁Disney[en]  ,[punct]  ▁pero[es]  ▁honest[en]  ly[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁Russia'
  context : ,[punct]  ▁इसी[hi]  ▁वजह[hi]  ▁से[hi]  >>▁Russia[en]<<  ▁को[hi]  ▁काफी[hi]  ▁नुकसान[hi]  ▁हुआ[hi]  ▁है[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='▁있어요'
  context : ▁운동[ko]  을[ko]  ▁꾸준히[ko]  ▁하고[ko]  >>▁있어요[ko]<<  ,[punct]  ▁right[en]  ?[punct]  ▁식[ko]  단[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁की'
  context : ▁में[hi]  ▁इन[hi]  ▁CM[en]  Es[en]  >>▁की[hi]<<  ▁predict[en]  ion[en]  ▁और[hi]  ▁monitoring[en]  ▁को[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='فرة'
  context : ▁في[ar]  ▁قيمة[ar]  ▁العملات[ar]  ▁المش[ar]  >>فرة[ar]<<  ▁،[punct]  ▁especially[en]  ▁meme[en]  ▁coin[en]  s[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='▁سلسلة'
  context : ▁Netflix[en]  ▁قررت[ar]  ▁تخت[ar]  م[ar]  >>▁سلسلة[ar]<<  ▁The[en]  ▁Sand[en]  man[en]  ▁في[ar]  ▁الموسم[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='지'
  context : ▁이야기를[ko]  ▁자주[ko]  ▁들[ko]  었[ko]  >>지[ko]<<  ,[punct]  ▁you[en]  ▁know[en]  ?[punct]  ▁그[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁universo'
  context : ▁fascinant[es]  es[es]  ▁sobre[es]  ▁el[es]  >>▁universo[es]<<  ,[punct]  ▁right[en]  ?[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='▁و'
  context : ▁بين[ar]  ▁Lucky[en]  C[en]  hap[en]  >>▁و[ar]<<  ▁Josh[en]  ▁Sch[en]  wart[en]  z[en]  ،[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='ंगा'
  context : ▁सरकारी[hi]  ▁वेबसाइट[hi]  ▁पर[hi]  ▁जाऊ[hi]  >>ंगा[hi]<<  ▁to[en]  ▁check[en]  ▁more[en]  ▁details[en]  ▁about[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='帮助'
  context : 业[zh]  发展[zh]  一定[zh]  有[zh]  >>帮助[zh]<<  ,[punct]  ▁for[en]  ▁sure[en]  .[punct]  ▁[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁mais'
  context : ▁certains[fr]  ▁panne[fr]  aux[fr]  ,[punct]  >>▁mais[fr]<<  ▁the[en]  ▁final[en]  ▁decision[en]  ▁be[en]  long[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='s'
  context : ▁comes[en]  ▁to[en]  ▁national[en]  ▁interest[en]  >>s[en]<<  ."[punct]  ▁Elle[fr]  ▁a[en]  ▁expliqué[fr]  ▁à[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='不错'
  context : 巴[zh]  切[zh]  最近[zh]  状态[zh]  >>不错[zh]<<  ,[punct]  ▁don[en]  '[punct]  t[en]  ▁you[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='▁community'
  context : 사[ko]  했는데[ko]  ,[punct]  ▁international[en]  >>▁community[en]<<  는[ko]  ▁정말[ko]  로[ko]  ▁상황[ko]  을[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='▁skills'
  context : ▁[punct]  효율[ko]  적인[ko]  ▁communication[en]  >>▁skills[en]<<  로[ko]  ▁팀[ko]  을[ko]  ▁이[ko]  끌[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='▁المرضى'
  context : ▁ب[ar]  جد[ar]  ▁ل[ar]  مساعدة[ar]  >>▁المرضى[ar]<<  ،[punct]  ▁really[en]  ![punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁maintenant'
  context : r[fr]  ▁avec[fr]  ▁United[fr]  ▁Airlines[fr]  >>▁maintenant[fr]<<  ,[punct]  ▁it[en]  '[punct]  s[en]  ▁just[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁fun'
  context : ▁to[en]  ▁be[en]  ▁so[en]  ▁much[en]  >>▁fun[en]<<  ▁de[fr]  ▁découvrir[fr]  ▁comment[fr]  ▁cela[fr]  ▁peut[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁a'
  context : ▁Ma[es]  ña[es]  na[es]  ▁voy[es]  >>▁a[en]<<  ▁revisar[es]  ▁los[es]  ▁sectores[es]  ▁clave[es]  ▁del[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='이다'
  context : 을[ko]  ▁잡[ko]  을[ko]  ▁생각[ko]  >>이다[ko]<<  ,[punct]  ▁just[en]  ▁to[en]  ▁make[en]  ▁sure[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='大'
  context : 资金[zh]  运用[zh]  规模[zh]  越来越[zh]  >>大[zh]<<  ，[punct]  invest[en]  ment[en]  ▁yi[en]  eld[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁pero'
  context : ▁[punct]  innova[es]  r[es]  ,[punct]  >>▁pero[es]<<  ▁sometimes[en]  ▁the[en]  ▁tac[en]  tics[en]  ▁they[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁discover'
  context : ▁ge[en]  ological[en]  ▁features[en]  ▁को[hi]  >>▁discover[en]<<  ▁करेगा[hi]  ,[punct]  ▁you[en]  ▁know[en]  ?[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁हैं'
  context : ें[punct]  ▁अभी[hi]  ▁भी[hi]  ▁बाकी[hi]  >>▁हैं[hi]<<  ,[punct]  ▁finger[en]  s[en]  ▁cross[en]  ed[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁a'
  context : est[fr]  ▁vrai[fr]  .[punct]  ▁Elle[fr]  >>▁a[en]<<  ▁toujours[fr]  ▁été[fr]  ▁une[fr]  ▁figure[fr]  ▁importante[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁होगी'
  context : ▁इंडिया[hi]  ▁जीत[hi]  ने[hi]  ▁वाली[hi]  >>▁होगी[hi]<<  ,[punct]  ▁trust[en]  ▁me[en]  ,[punct]  ▁मैं[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='1'
  context : ▁C[en]  /20[en]  24[en]  ▁S[en]  >>1[en]<<  ،[punct]  ▁و[ar]  سمع[ar]  ت[ar]  ▁إنه[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='提升'
  context : 存储[zh]  容量[zh]  会有[zh]  很大[zh]  >>提升[zh]<<  ，[punct]  amaz[en]  ing[en]  ![punct]  ▁中国[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁sector'
  context : ▁तय[hi]  ▁है[hi]  ,[punct]  ▁technology[en]  >>▁sector[en]<<  ▁में[hi]  ▁ये[hi]  ▁बहुत[hi]  ▁ही[hi]  ▁exciting[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='▁materials'
  context : ▁need[en]  ▁to[en]  ▁adapt[en]  ▁teaching[en]  >>▁materials[en]<<  ，[punct]  以[zh]  确保[zh]  学生[zh]  能够[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='ه'
  context : ▁ي[ar]  تابع[ar]  ون[ar]  ▁أخبار[ar]  >>ه[ar]<<  ،[punct]  ▁right[en]  ?[punct]  ▁أ[ar]  كيد[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁a'
  context : ▁dedica[es]  ndo[es]  ▁tantos[es]  ▁recursos[es]  >>▁a[en]<<  ▁causas[es]  ▁sociales[es]  ,[punct]  ▁especially[en]  ▁when[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='精彩'
  context : 明天[zh]  的比赛[zh]  会[zh]  很[zh]  >>精彩[zh]<<  ,[punct]  ▁you[en]  ▁know[en]  ?[punct]  ▁[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='ché'
  context : ▁produits[fr]  ▁du[fr]  ▁super[fr]  mar[fr]  >>ché[fr]<<  ,[punct]  ▁and[en]  ▁next[en]  ▁time[en]  ,[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='거야'
  context : ▁[punct]  챙[ko]  길[ko]  ▁[punct]  >>거야[ko]<<  ,[punct]  ▁right[en]  ?[punct]  ▁[punct]  규칙[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='錯過'
  context : ，[punct]  一定[zh]  唔[zh]  會[zh]  >>錯過[zh]<<  ，[punct]  for[en]  ▁sure[en]  ！[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='니까'
  context : ▁치[ko]  열[ko]  해[ko]  지[ko]  >>니까[ko]<<  ,[punct]  ▁brand[en]  s[en]  ▁really[en]  ▁need[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='ة'
  context : اة[ar]  ▁الهو[ar]  كي[ar]  ▁الليل[ar]  >>ة[ar]<<  ،[punct]  ▁you[en]  ▁know[en]  ?[punct]  ▁ال[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁protéger'
  context : ▁Cette[en]  ▁mesure[en]  ▁vise[en]  ▁à[fr]  >>▁protéger[en]<<  ▁la[fr]  ▁santé[fr]  ▁publique[fr]  ▁et[fr]  ▁à[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁technology'
  context : ▁important[en]  .[punct]  ▁आज[hi]  कल[hi]  >>▁technology[en]<<  ▁इतनी[hi]  ▁तेजी[hi]  ▁से[hi]  ▁बढ़[hi]  ▁रही[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁poco'
  context : ▁a[en]  ▁cambiar[es]  ▁poco[es]  ▁a[en]  >>▁poco[es]<<  ,[punct]  ▁anyway[en]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁résultats'
  context : ▁vraiment[fr]  ▁[punct]  améliorer[fr]  ▁les[fr]  >>▁résultats[fr]<<  ,[punct]  ▁but[en]  ▁only[en]  ▁if[en]  ▁everyone[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='多'
  context : 满满[zh]  ，[punct]  任务[zh]  超级[zh]  >>多[zh]<<  ，[punct]  wo[en]  w[en]  ![punct]  ▁新[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='لة'
  context : تطور[ar]  ات[ar]  ▁مذ[ar]  ه[ar]  >>لة[ar]<<  ,[punct]  ▁you[en]  ▁know[en]  ?[punct]  ▁سي[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁han'
  context : ▁mostrando[es]  ▁lo[es]  ▁lejos[es]  ▁que[es]  >>▁han[en]<<  ▁llegado[es]  ▁en[es]  ▁tecnología[es]  ▁espacial[es]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='s'
  context : ▁a[en]  ▁los[es]  ▁Pan[en]  ther[en]  >>s[en]<<  ,[punct]  ▁pero[es]  ▁decir[es]  ▁que[es]  ▁en[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

### False Alarms — Inter-sentential (48 examples)

```
[Hindi-English]  switch_type=inter  switch_token='▁right'
  context : s[en]  ▁quite[en]  ▁impressive[en]  ,[punct]  >>▁right[en]<<  ?[punct]  ▁Mujh[en]  e[en]  ▁lagt[en]  a[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁सके'
  context : ▁that[en]  ▁लोग[hi]  ▁सुरक्षित[hi]  ▁रह[hi]  >>▁सके[hi]<<  ं[punct]  ।[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁movies'
  context : ▁like[en]  d[en]  ▁the[en]  ▁original[en]  >>▁movies[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='ly'
  context : cél[fr]  ération[fr]  ,[punct]  ▁honest[fr]  >>ly[fr]<<  .[punct]  ▁La[fr]  ▁tension[fr]  ▁entre[fr]  ▁les[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='UU'
  context : as[es]  ▁de[es]  ▁EE[en]  .[punct]  >>UU[en]<<  .[punct]  ▁The[en]  ▁European[en]  ▁Commission[en]  ▁has[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁agree'
  context : ▁don[fr]  ’[punct]  t[en]  ▁you[en]  >>▁agree[en]<<  ?[punct]  ▁J[en]  ’[punct]  en[en]  ▁ai[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁this'
  context : ed[en]  ▁account[en]  s[en]  ▁like[en]  >>▁this[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁end'
  context : ▁went[en]  ▁well[en]  ▁in[en]  ▁the[en]  >>▁end[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁measure'
  context : '[punct]  s[en]  ▁a[en]  ▁security[en]  >>▁measure[en]<<  ।[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁pasado'
  context : ▁al[es]  ▁show[en]  ▁el[es]  ▁sábado[es]  >>▁pasado[es]<<  .[punct]  ▁Dana[es]  ▁Car[en]  vey[en]  ▁really[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁India'
  context : ▁electric[en]  ▁vehicle[en]  ▁market[en]  ▁in[en]  >>▁India[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁change'
  context : ▁respond[en]  s[en]  ▁to[en]  ▁climate[en]  >>▁change[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='cient'
  context : 会[zh]  更[zh]  e[en]  ffi[en]  >>cient[en]<<  。[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='s'
  context : ers[fr]  ▁rester[fr]  ont[fr]  ▁populaire[fr]  >>s[fr]<<  .[punct]  ▁However[fr]  ,[punct]  ▁some[fr]  ▁consumer[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁technologies'
  context : ▁adopt[fr]  er[fr]  ▁les[fr]  ▁nouvelles[fr]  >>▁technologies[fr]<<  .[punct]  ▁Sometimes[fr]  ,[punct]  ▁change[fr]  ▁can[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='ifying'
  context : ▁فعلا[ar]  ً[punct]  ▁كانت[ar]  ▁electr[en]  >>ifying[en]<<  ![punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁him'
  context : ▁for[en]  ▁senior[en]  s[en]  ▁like[en]  >>▁him[en]<<  ![punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='ed'
  context : ▁she[en]  ▁felt[en]  ▁truly[en]  ▁bless[en]  >>ed[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='希望'
  context : 时代[zh]  ，[punct]  真的很[zh]  有[zh]  >>希望[zh]<<  ！[punct]  ▁不过[zh]  ，[punct]  我也[zh]  想知道[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁it'
  context : ,[punct]  ▁isn[en]  '[punct]  t[en]  >>▁it[en]<<  ?[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁right'
  context : ▁진짜[ko]  ▁재미있[ko]  어[ko]  ,[punct]  >>▁right[en]<<  ?[punct]  ▁WP[en]  ▁Engine[en]  이[ko]  ▁Automat[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁him'
  context : ▁gre[en]  w[en]  ▁up[en]  ▁with[en]  >>▁him[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='冲突'
  context : 警方[zh]  在[zh]  首都[zh]  发生了[zh]  >>冲突[zh]<<  。[punct]  这种情况[zh]  让人[zh]  担心[zh]  未来的[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁days'
  context : ▁is[en]  ▁very[en]  ▁relevant[en]  ▁these[en]  >>▁days[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='어'
  context : ▁[punct]  짜[ko]  릿[ko]  했[ko]  >>어[ko]<<  ![punct]  ▁나[ko]  도[ko]  ▁놀[ko]  랐[ko]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁seriously'
  context : ▁reco[es]  r[es]  tes[es]  ,[punct]  >>▁seriously[en]<<  ?[punct]  ▁Me[en]  ▁preocupa[es]  ▁el[es]  ▁futuro[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁movie'
  context : ▁in[en]  ▁a[en]  ▁science[en]  ▁fiction[en]  >>▁movie[en]<<  ![punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁performance'
  context : bility[en]  ▁without[en]  ▁sacrifici[en]  ng[en]  >>▁performance[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁think'
  context : ▁don[en]  '[punct]  t[en]  ▁you[en]  >>▁think[en]<<  ?[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='s'
  context : ing[en]  ▁Think[en]  ing[en]  ▁Machine[en]  >>s[en]<<  .[punct]  ▁Lili[en]  an[en]  ▁We[en]  ng[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='day'
  context : ▁PC[en]  ▁with[en]  ▁it[en]  ▁some[en]  >>day[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁right'
  context : ▁souvenir[fr]  ▁du[fr]  ▁passé[fr]  ,[punct]  >>▁right[fr]<<  ?[punct]  ▁Franc[fr]  he[en]  ment[en]  ,[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='s'
  context : 人[zh]  ▁understand[en]  ▁their[en]  ▁struggle[en]  >>s[en]<<  。[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='ly'
  context : ▁último[es]  ▁juego[es]  ,[punct]  ▁honest[en]  >>ly[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='▁lives'
  context : ▁about[en]  ▁people[en]  ’[punct]  s[en]  >>▁lives[en]<<  。[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁needs'
  context : ▁tool[en]  ▁fit[en]  s[en]  ▁her[en]  >>▁needs[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁know'
  context : ren[fr]  eur[fr]  ,[punct]  ▁you[fr]  >>▁know[fr]<<  ?[punct]  ▁Je[fr]  ▁vais[fr]  ▁attendre[fr]  ▁de[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁série'
  context : ▁[punct]  énergie[fr]  ▁à[fr]  ▁la[fr]  >>▁série[fr]<<  .[punct]  ▁Il[fr]  ▁a[en]  ▁sur[fr]  pris[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁له'
  context : ▁كما[ar]  ▁هو[ar]  ▁م[ar]  خطط[ar]  >>▁له[ar]<<  .[punct]  ▁كانت[ar]  ▁ال[ar]  وس[ar]  اط[ar]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='s'
  context : ▁li[fr]  sses[fr]  ▁et[fr]  ▁uniforme[fr]  >>s[fr]<<  .[punct]  ▁S[fr]  cient[fr]  ists[fr]  ▁will[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁know'
  context : ▁같[ko]  아[ko]  .[punct]  ▁You[en]  >>▁know[en]<<  ?[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='어'
  context : ▁행복[ko]  해[ko]  ▁보[ko]  였[ko]  >>어[ko]<<  .[punct]  ▁진짜[ko]  ▁family[en]  가[ko]  ▁완성[ko]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁cine'
  context : ▁experiencia[es]  ▁increíble[es]  ▁en[es]  ▁el[es]  >>▁cine[en]<<  .[punct]  ▁Maybe[en]  ▁I[en]  '[punct]  ll[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁economía'
  context : ▁un[es]  ▁desafío[es]  ▁para[es]  ▁su[es]  >>▁economía[es]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='的生活'
  context : 这[zh]  可能会[zh]  影响[zh]  我们[zh]  >>的生活[zh]<<  。[punct]  ▁[punct]  我希望[zh]  未来的[zh]  贸易[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='s'
  context : -[punct]  China[es]  ▁trade[en]  ▁tension[en]  >>s[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁है'
  context : ▁कुछ[hi]  ▁पता[hi]  ▁चल[hi]  ता[hi]  >>▁है[hi]<<  ।[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁world'
  context : ▁especially[en]  ▁in[en]  ▁the[en]  ▁business[en]  >>▁world[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

### False Alarms — Intra-sentential (48 examples)

```
[Chinese-English]  switch_type=intra  switch_token='▁before'
  context : 情况[zh]  会[zh]  ▁worse[en]  ▁than[en]  >>▁before[en]<<  ,[punct]  ▁seriously[en]  ![punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='▁مختلفة'
  context : ▁الجديدة[ar]  ▁وكل[ar]  ها[ar]  ▁كانت[ar]  >>▁مختلفة[ar]<<  ▁عن[ar]  ▁السن[ar]  ين[ar]  ▁اللي[ar]  ▁قبل[ar]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁de'
  context : ▁sobre[es]  ▁el[es]  ▁bro[es]  te[es]  >>▁de[es]<<  ▁sara[es]  mp[es]  ión[es]  ▁en[es]  ▁el[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁है'
  context : ▁health[en]  ▁पर[hi]  ▁असर[hi]  ▁पड़ा[hi]  >>▁है[hi]<<  ▁क्योंकि[hi]  ▁वह[hi]  ▁पूरे[hi]  ▁दिन[hi]  ▁खड़ा[hi]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='▁powerful'
  context : hi[en]  zin[en]  是[zh]  super[en]  >>▁powerful[en]<<  ▁antioxidant[en]  ，[punct]  你[zh]  了解[zh]  吗[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='经济增长'
  context : 能[zh]  实现[zh]  5%[en]  的[zh]  >>经济增长[zh]<<  ，[punct]  还有很多[zh]  变[zh]  数[zh]  ，[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁questions'
  context : ▁réponse[fr]  s[fr]  ▁à[fr]  ▁leurs[fr]  >>▁questions[fr]<<  ,[punct]  ▁right[fr]  ?[punct]  ▁Les[fr]  ▁autorités[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁Gaza'
  context : ▁ataques[es]  ▁aéreo[es]  s[es]  ▁en[es]  >>▁Gaza[es]<<  ▁son[es]  ▁alarm[es]  antes[es]  ,[punct]  ▁especially[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='消息'
  context : 觉得[zh]  这是[zh]  利[zh]  空[zh]  >>消息[zh]<<  ，[punct]  但[zh]  from[en]  ▁another[en]  ▁perspective[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='▁movie'
  context : ▁intui[en]  tion[en]  ▁about[en]  ▁the[en]  >>▁movie[en]<<  ▁before[en]  ▁it[en]  ▁even[en]  ▁came[en]  ▁out[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='ريا'
  context : يدة[ar]  ▁للب[ar]  كت[ar]  ي[ar]  >>ريا[ar]<<  ▁الن[ar]  افع[ar]  ة[ar]  ،[punct]  ▁right[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁à'
  context : ▁[punct]  écoute[fr]  s[fr]  ▁montre[fr]  >>▁à[fr]<<  ▁quel[fr]  ▁point[fr]  ▁le[fr]  ▁pouvoir[fr]  ▁peut[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='▁예정'
  context : 에[ko]  ▁대해[ko]  ▁이야기[ko]  할[ko]  >>▁예정[ko]<<  이[ko]  야[ko]  ,[punct]  ▁because[en]  ▁sharing[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁conclusion'
  context : ▁before[en]  ▁jump[en]  ing[en]  ▁to[en]  >>▁conclusion[en]<<  s[en]  ,[punct]  ▁you[en]  ▁know[en]  ?[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁performance'
  context : ▁was[en]  ▁talking[en]  ▁about[en]  ▁his[en]  >>▁performance[en]<<  ▁on[en]  ▁social[en]  ▁media[en]  .[punct]  ▁शा[hi]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁vais'
  context : ▁Je[fr]  >>▁vais[fr]<<  ▁lire[fr]  ▁l[fr]  '[punct]  article[fr]  ▁sur[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁Meta'
  context : .[punct]  ▁La[es]  ▁competencia[es]  ▁entre[es]  >>▁Meta[es]<<  ▁y[es]  ▁Open[es]  AI[es]  ▁se[es]  ▁va[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='▁المباراة'
  context : ▁[punct]  أداء[ar]  ▁الفريق[ar]  ▁في[ar]  >>▁المباراة[ar]<<  ▁الأخيرة[ar]  ▁وكيف[ar]  ▁كان[ar]  ▁الجميع[ar]  ▁ي[ar]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='خر'
  context : عيد[ar]  ▁الوطني[ar]  ▁ب[ar]  ف[ar]  >>خر[ar]<<  ▁كبير[ar]  ،[punct]  ▁yeah[en]  ![punct]  ▁الوطن[ar]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁है'
  context : यर[hi]  ▁को[hi]  ▁अवार्ड[hi]  ▁देता[hi]  >>▁है[hi]<<  ,[punct]  ▁और[hi]  ▁इस[hi]  ▁साल[hi]  ▁भी[hi]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='عروض'
  context : ▁ال[ar]  إثارة[ar]  ▁في[ar]  ▁ال[ar]  >>عروض[ar]<<  ▁الجديدة[ar]  ،[punct]  ▁well[en]  ![punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁de'
  context : ▁parece[es]  ▁que[es]  ▁la[es]  ▁temporada[es]  >>▁de[es]<<  ▁premios[es]  ▁this[en]  ▁year[en]  ▁está[es]  ▁un[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁कि'
  context : ▁वो[hi]  ▁कह[hi]  ती[hi]  ▁थी[hi]  >>▁कि[hi]<<  ▁स्मार्टफोन[hi]  ▁खरीद[hi]  ना[hi]  ▁अब[hi]  ▁स[hi]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='逊'
  context : 传统[zh]  股[zh]  表现[zh]  稍[zh]  >>逊[zh]<<  色[zh]  。[punct]  We[en]  '[punct]  ll[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='▁중요하다'
  context : 을[ko]  ▁조절[ko]  하는[ko]  ▁게[ko]  >>▁중요하다[ko]<<  고[ko]  ▁생각해[ko]  요[ko]  ,[punct]  ▁don[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁impressive'
  context : ▁this[fr]  ▁victor[fr]  y[fr]  ▁was[en]  >>▁impressive[fr]<<  ▁pour[fr]  ▁son[fr]  ▁[punct]  âge[fr]  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='ux'
  context : ▁et[fr]  ▁d[en]  '[punct]  anima[en]  >>ux[en]<<  ▁danger[en]  eux[en]  ,[punct]  ▁ce[fr]  ▁qui[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='tion'
  context : ▁[punct]  exprimer[fr]  ▁son[fr]  ▁indigna[fr]  >>tion[fr]<<  ,[punct]  ▁right[fr]  ?[punct]  ▁Je[fr]  ▁vais[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='▁새로운'
  context : ?[punct]  ▁그래서[ko]  ▁우리[ko]  도[ko]  >>▁새로운[ko]<<  ▁기술[ko]  을[ko]  ▁잘[ko]  ▁배[ko]  워[ko]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='ies'
  context : ▁think[en]  ?[punct]  ▁ऐसी[hi]  ▁discover[en]  >>ies[en]<<  ▁young[en]  ▁mind[en]  s[en]  ▁को[hi]  ▁space[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁display'
  context : watch[en]  ▁का[hi]  ▁design[en]  ▁और[hi]  >>▁display[en]<<  ▁details[en]  ▁brand[en]  ▁की[hi]  ▁official[en]  ▁वेबसाइट[hi]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='겠다'
  context : ▁이[ko]  길[ko]  ▁수도[ko]  ▁있[ko]  >>겠다[ko]<<  고[ko]  ▁느[ko]  꼈[ko]  어[ko]  ,[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁gobierno'
  context : ▁revue[es]  lo[es]  ▁en[es]  ▁el[es]  >>▁gobierno[es]<<  ▁última[es]  mente[es]  ,[punct]  ▁you[en]  ▁know[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁pérdida'
  context : .[punct]  ▁seguramente[es]  ▁siente[es]  ▁esta[es]  >>▁pérdida[es]<<  ▁profunda[es]  mente[es]  .[punct]  ▁He[en]  ▁was[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='▁this'
  context : ▁can[en]  '[punct]  t[en]  ▁believe[en]  >>▁this[en]<<  ▁happened[en]  ▁again[en]  .[punct]  ▁모델[ko]  링[ko]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁45'
  context : ▁की[hi]  ▁है[hi]  ,[punct]  ▁जिसमें[hi]  >>▁45[hi]<<  ▁नाम[hi]  ▁शामिल[hi]  ▁हैं[hi]  ।[punct]  ▁This[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='▁plot'
  context : i[en]  led[en]  ▁the[en]  ▁entire[en]  >>▁plot[en]<<  ▁for[en]  ▁fans[en]  .[punct]  ▁ل[ar]  حسن[ar]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁it'
  context : '[punct]  s[en]  ▁more[en]  ▁to[en]  >>▁it[en]<<  ▁than[en]  ▁meet[en]  s[en]  ▁the[en]  ▁eye[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁à'
  context : ▁7[fr]  ▁Pro[fr]  ▁va[fr]  ▁continuer[fr]  >>▁à[fr]<<  ▁impression[fr]  ner[fr]  ,[punct]  ▁you[fr]  ▁know[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='说道'
  context : 最新的[zh]  科技[zh]  趋势[zh]  时[zh]  >>说道[zh]<<  ：[punct]  "[punct]  近年来[zh]  ，[punct]  人工智能[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='12'
  context : 하는데[ko]  ▁혹시[ko]  ▁vitamin[en]  ▁B[en]  >>12[en]<<  ▁de[en]  fici[en]  en[en]  cy[en]  일[ko]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁années'
  context : ▁il[fr]  ▁y[fr]  ▁a[en]  ▁quelques[fr]  >>▁années[fr]<<  ▁et[fr]  ▁elle[fr]  ▁était[en]  ▁vraiment[en]  ▁impression[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='▁fact'
  context : 我们[zh]  ，[punct]  一个[zh]  有趣的[zh]  >>▁fact[en]<<  ▁about[en]  ▁the[en]  ▁human[en]  ▁body[en]  是[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='م'
  context : متابعة[ar]  ▁هؤلاء[ar]  ▁الن[ar]  جو[ar]  >>م[ar]<<  ▁ال[ar]  جدد[ar]  .[punct]  ▁Everyone[en]  ▁is[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='▁중요하다'
  context : ▁요즘[ko]  ▁건강[ko]  이[ko]  ▁정말[ko]  >>▁중요하다[ko]<<  고[ko]  ▁느[ko]  꼈[ko]  어요[ko]  ,[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁médicos'
  context : ▁Colorado[es]  ▁preocupa[es]  ▁a[en]  ▁muchos[es]  >>▁médicos[es]<<  ▁porque[es]  ▁la[es]  ▁vacuna[es]  ción[es]  ▁es[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='دعاء'
  context : ▁من[ar]  ▁[punct]  صحة[ar]  ▁الا[ar]  >>دعاء[ar]<<  ات[ar]  ،[punct]  ▁and[en]  ▁authorities[en]  ▁will[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='惠'
  context : 价格[zh]  还是[zh]  很[zh]  实[zh]  >>惠[zh]<<  的[zh]  ，[punct]  ▁oh[en]  ▁my[en]  ▁go[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

### Missed Switches — Inter-sentential (48 examples)

```
[Hindi-English]  switch_type=inter  switch_token='▁hit'
  context : ▁crew[en]  ▁after[en]  ▁such[en]  ▁a[en]  >>▁hit[en]<<  ?[punct]  ▁यह[hi]  ▁फिल्म[hi]  ▁देखकर[hi]  ▁लोगों[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁sure'
  context : ▁أ[ar]  قوى[ar]  ،[punct]  ▁for[en]  >>▁sure[en]<<  .[punct]  ▁الاهتمام[ar]  ▁بال[ar]  صحة[ar]  ▁النفسية[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='ntes'
  context : s[es]  ▁mantener[es]  se[es]  ▁vigila[es]  >>ntes[es]<<  .[punct]  ▁Trump[en]  ▁gives[en]  ▁Putin[en]  ▁the[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='▁research'
  context : ▁stay[en]  ▁ahead[en]  ▁in[en]  ▁my[en]  >>▁research[en]<<  .[punct]  ▁[punct]  他们[zh]  居然[zh]  能[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='enses'
  context : ▁families[en]  ▁manage[en]  ▁their[en]  ▁exp[en]  >>enses[en]<<  .[punct]  ▁En[fr]  ▁janvier[fr]  ,[punct]  ▁plusieurs[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁Cher'
  context : ▁déroule[fr]  ▁actuellement[fr]  ▁dans[fr]  ▁le[fr]  >>▁Cher[fr]<<  .[punct]  ▁They[en]  ▁are[en]  ▁hosting[en]  ▁a[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁exam'
  context : ▁confident[en]  ▁during[en]  ▁the[en]  ▁actual[en]  >>▁exam[en]<<  .[punct]  ▁तुम्हें[hi]  ▁क्या[hi]  ▁लगता[hi]  ▁है[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁people'
  context : ▁are[en]  ▁deliver[en]  ed[en]  ▁to[en]  >>▁people[en]<<  .[punct]  ▁많은[ko]  ▁사람들이[ko]  ▁이[ko]  ▁계획[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='te'
  context : ▁solution[en]  ▁to[en]  ▁tire[en]  ▁was[en]  >>te[en]<<  .[punct]  ▁Des[es]  ar[es]  roll[es]  aron[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁end'
  context : ▁leading[en]  ▁just[en]  ▁before[en]  ▁the[en]  >>▁end[en]<<  .[punct]  ▁Les[fr]  ▁supporter[fr]  s[fr]  ▁sont[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁here'
  context : PR[en]  1[en]  ▁release[en]  ▁is[en]  >>▁here[en]<<  ![punct]  ▁[punct]  لاحظ[ar]  ▁أ[ar]  صدق[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁हैं'
  context : ▁में[hi]  ▁high[en]  ▁performance[en]  ▁चाहते[hi]  >>▁हैं[hi]<<  ।[punct]  ▁In[en]  ▁his[en]  ▁opinion[en]  ,[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='▁so'
  context : '[punct]  t[en]  ▁you[en]  ▁think[en]  >>▁so[en]<<  ?[punct]  ▁[punct]  有时候[zh]  科学[zh]  真的很[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='어'
  context : 촉[ko]  했다고[ko]  ▁들[ko]  었[ko]  >>어[ko]<<  .[punct]  ▁He[en]  ▁might[en]  ▁be[en]  ▁a[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='的比赛'
  context : 20[en]  男[zh]  足[zh]  接下来[zh]  >>的比赛[zh]<<  。[punct]  ▁I[en]  ▁will[en]  ▁definitely[en]  ▁watch[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁दिया'
  context : ▁के[hi]  ▁खिलाफ[hi]  ▁कमाल[hi]  ▁कर[hi]  >>▁दिया[hi]<<  ।[punct]  ▁He[en]  ▁took[en]  ▁back[en]  -[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='s'
  context : ed[en]  ▁to[en]  ▁Alzheimer[en]  '[punct]  >>s[en]<<  .[punct]  ▁سأ[ar]  تحدث[ar]  ▁مع[ar]  ▁ع[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁easier'
  context : ▁make[en]  ▁sharing[en]  ▁VR[en]  ▁experiences[en]  >>▁easier[en]<<  .[punct]  ▁سيكون[ar]  ▁بإ[ar]  مكان[ar]  ▁المستخدم[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='素质'
  context : 等待[zh]  真的很[zh]  考验[zh]  心理[zh]  >>素质[zh]<<  。[punct]  pro[en]  long[en]  ed[en]  ▁[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='打'
  context : 的[zh]  资格[zh]  赛[zh]  开[zh]  >>打[zh]<<  。[punct]  ▁It[en]  ▁was[en]  ▁exciting[en]  ▁to[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁cancer'
  context : ▁his[en]  ▁fight[en]  ▁against[en]  ▁bone[en]  >>▁cancer[en]<<  .[punct]  ▁अब[hi]  ▁सोशल[hi]  ▁मीडिया[hi]  ▁पर[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='ibles'
  context : ▁de[es]  pred[es]  adores[es]  ▁tem[es]  >>ibles[es]<<  .[punct]  ▁But[en]  ▁who[en]  ▁knew[en]  ▁they[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁Hollywood'
  context : ▁twist[en]  ▁dig[es]  no[es]  ▁de[es]  >>▁Hollywood[en]<<  .[punct]  ▁Nunca[es]  ▁imagin[es]  é[es]  ▁que[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='well'
  context : ,[punct]  ▁showing[fr]  ▁the[en]  ▁fare[en]  >>well[en]<<  .[punct]  ▁Le[fr]  ▁destin[fr]  ▁de[fr]  ▁ces[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁amazing'
  context : ▁is[en]  ▁going[en]  ▁to[en]  ▁be[en]  >>▁amazing[en]<<  ![punct]  ▁이번[ko]  ▁영화[ko]  는[ko]  ▁현실[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='ة'
  context : بر[ar]  ▁عن[ar]  ▁مشاعر[ar]  ▁عميق[ar]  >>ة[ar]<<  .[punct]  ▁S[en]  no[en]  op[en]  ▁Dog[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='했어요'
  context : 가[ko]  ▁나[ko]  한테[ko]  ▁말[ko]  >>했어요[ko]<<  .[punct]  ▁Have[en]  ▁you[en]  ▁heard[en]  ▁about[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁unexpected'
  context : ▁sur[en]  .[punct]  ▁It[en]  ▁was[en]  >>▁unexpected[en]<<  ![punct]  ▁La[es]  ▁tormenta[es]  ▁casi[es]  ▁golpe[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁है'
  context : ▁पूरे[hi]  ▁दिन[hi]  ▁खड़ा[hi]  ▁रहता[hi]  >>▁है[hi]<<  ।[punct]  ▁Doctor[en]  s[en]  ▁ने[hi]  ▁recommend[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁disease'
  context : ▁Hunt[en]  ington[en]  ’[punct]  s[en]  >>▁disease[en]<<  .[punct]  ▁हम[hi]  ▁future[en]  ▁में[hi]  ▁stimula[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='▁land'
  context : ▁how[en]  ▁space[en]  craft[en]  s[en]  >>▁land[en]<<  .[punct]  ▁[punct]  साइ[hi]  ंस[hi]  ▁में[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁hospital'
  context : ▁en[es]  ▁Gaza[es]  ▁con[es]  ▁el[es]  >>▁hospital[es]<<  .[punct]  ▁The[en]  ▁images[en]  ▁and[en]  ▁stories[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁découverte'
  context : ▁scientifique[en]  ▁a[en]  ▁publié[en]  ▁sa[fr]  >>▁découverte[fr]<<  .[punct]  ▁It[en]  '[punct]  s[en]  ▁quite[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=inter  switch_token='cing'
  context : '[punct]  re[en]  ▁experi[en]  en[en]  >>cing[en]<<  .[punct]  ▁Les[fr]  ▁conséquence[fr]  s[fr]  ▁du[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='例外'
  context : book[en]  LM[en]  ▁[punct]  是個[zh]  >>例外[zh]<<  。[punct]  ▁I[en]  ▁remember[en]  ▁the[en]  ▁first[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁top'
  context : ▁make[en]  ▁it[en]  ▁to[en]  ▁the[en]  >>▁top[en]<<  ?[punct]  ▁Las[es]  ▁clasifica[es]  ciones[es]  ▁de[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='▁walk'
  context : s[en]  ▁go[en]  ▁for[en]  ▁a[en]  >>▁walk[en]<<  ![punct]  ▁한국[ko]  ▁음식[ko]  ▁정말[ko]  ▁맛있[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='▁electric'
  context : ▁in[en]  ▁the[en]  ▁room[en]  ▁was[en]  >>▁electric[en]<<  .[punct]  ▁Elle[fr]  ▁a[en]  ▁dit[en]  ▁que[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='어'
  context : 했다는[ko]  ▁소식[ko]  ▁들[ko]  었[ko]  >>어[ko]<<  ?[punct]  ▁I[en]  ▁honest[en]  ly[en]  ▁didn[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='▁peligro'
  context : zar[es]  ,[punct]  ▁no[es]  ▁habría[es]  >>▁peligro[es]<<  .[punct]  ▁But[en]  ▁it[en]  ▁turn[en]  s[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='back'
  context : ▁perspective[en]  ▁on[en]  ▁the[en]  ▁quarter[en]  >>back[en]<<  .[punct]  ▁قال[ar]  ▁أحد[ar]  ▁الم[ar]  شجع[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁funding'
  context : ▁policies[en]  ▁affect[en]  ▁public[en]  ▁health[en]  >>▁funding[en]<<  .[punct]  ▁سأ[ar]  حرص[ar]  ▁على[ar]  ▁الت[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='▁prices'
  context : ▁gadget[en]  s[en]  ▁at[en]  ▁lower[en]  >>▁prices[en]<<  .[punct]  ▁الكثير[ar]  ▁من[ar]  ▁الناس[ar]  ▁ي[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='어'
  context : ▁집[ko]  회를[ko]  ▁열[ko]  었[ko]  >>어[ko]<<  .[punct]  ▁The[en]  ▁messages[en]  ▁at[en]  ▁each[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='어'
  context : ,[punct]  ▁정말[ko]  ▁기대[ko]  됐[ko]  >>어[ko]<<  .[punct]  ▁Especial[en]  ly[en]  ▁since[en]  ▁the[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='PT'
  context : AI[fr]  ▁et[fr]  ▁Chat[fr]  G[fr]  >>PT[fr]<<  .[punct]  ▁It[en]  ▁really[en]  ▁made[en]  ▁me[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='▁it'
  context : t[en]  ▁wait[en]  ▁to[en]  ▁see[en]  >>▁it[en]<<  ![punct]  ▁[punct]  电影[zh]  名[zh]  册[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='▁6'
  context : ▁was[en]  ▁open[en]  ▁until[en]  ▁April[en]  >>▁6[en]<<  ,[punct]  ▁2025[punct]  .[punct]  ▁[punct]  这些[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

### Missed Switches — Intra-sentential (48 examples)

```
[Chinese-English]  switch_type=intra  switch_token='场比赛'
  context : 期待[zh]  下[zh]  一个[zh]  主[zh]  >>场比赛[zh]<<  ，[punct]  let[en]  '[punct]  s[en]  ▁see[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='饮食'
  context : 孕[zh]  期[zh]  开始[zh]  注意[zh]  >>饮食[zh]<<  ，[punct]  to[en]  ▁ensure[en]  ▁long[en]  -[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁de'
  context : ▁La[es]  ▁salud[es]  ▁pública[es]  ▁depende[es]  >>▁de[es]<<  ▁our[en]  ▁collective[en]  ▁efforts[en]  ▁y[es]  ▁la[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='نتظر'
  context : ▁GTA[en]  ▁6[en]  ▁وس[ar]  أ[ar]  >>نتظر[ar]<<  ▁Trailer[en]  ▁2[en]  ▁بكل[ar]  ▁صبر[ar]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='▁Quest'
  context : ▁سي[ar]  ضيف[ar]  ▁Meta[en]  >>▁Quest[en]<<  ▁مي[ar]  زة[ar]  ▁share[en]  ▁الجديدة[ar]  ▁قريب[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='呼吁'
  context : 中[zh]  好多[zh]  声音[zh]  都在[zh]  >>呼吁[zh]<<  ▁peace[en]  。[punct]  ▁[punct]  我们在[zh]  曼[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁Indiana'
  context : ▁como[es]  ▁una[es]  ▁película[es]  ▁de[es]  >>▁Indiana[en]<<  ▁Jones[es]  .[punct]  ▁La[es]  ▁historia[es]  ▁de[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='更重要的是'
  context : ▁optimiza[en]  tion[en]  .[punct]  ▁[punct]  >>更重要的是[zh]<<  ，[punct]  E[en]  VOL[en]  VE[en]  pro[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁imagine'
  context : s[fr]  .[punct]  ▁Can[fr]  ▁you[fr]  >>▁imagine[fr]<<  ▁how[en]  ▁much[en]  ▁we[en]  ▁still[en]  ▁have[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='부터'
  context : .[punct]  ▁나는[ko]  ▁예[ko]  전[ko]  >>부터[ko]<<  ▁The[en]  ▁View[en]  ▁패[ko]  널[ko]  들의[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='에는'
  context : ▁내년[ko]  >>에는[ko]<<  ▁E[en]  LIZA[en]  ▁[punct]  챗[ko]  봇[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[French-English]  switch_type=intra  switch_token='il'
  context : k[en]  ▁parce[en]  ▁qu[en]  '[punct]  >>il[fr]<<  ▁a[en]  ▁une[fr]  ▁vi[fr]  be[en]  ▁différent[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='▁عن'
  context : فض[ar]  اء[ar]  ▁وال[ar]  بحث[ar]  >>▁عن[ar]<<  ▁sign[en]  s[en]  ▁of[en]  ▁life[en]  ▁beyond[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁moins'
  context : gier[fr]  ▁les[fr]  ▁produits[fr]  ▁avec[fr]  >>▁moins[fr]<<  ▁d[en]  '[punct]  ad[en]  dit[en]  ifs[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='ing'
  context : ▁It[en]  ▁became[en]  ▁a[en]  ▁trend[en]  >>ing[en]<<  ▁meme[es]  ▁online[en]  ▁almost[en]  ▁immediately[en]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁सुन'
  context : ▁जब[hi]  ▁मैंने[hi]  ▁ये[hi]  ▁खबर[hi]  >>▁सुन[hi]<<  ी[punct]  ,[punct]  ▁I[en]  ▁felt[en]  ▁really[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='▁فقدان'
  context : ،[punct]  ▁وم[ar]  شكل[ar]  ة[ar]  >>▁فقدان[ar]<<  ▁CBS[en]  ▁تجعل[ar]  ▁الأمور[ar]  ▁أكثر[ar]  ▁تو[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='▁때'
  context : 을[ko]  ▁처음[ko]  ▁접[ko]  했을[ko]  >>▁때[ko]<<  ,[punct]  ▁shock[en]  ed[en]  ▁by[en]  ▁how[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='▁기술'
  context : .[punct]  ▁이[ko]  ▁제품[ko]  은[ko]  >>▁기술[ko]<<  ▁innovation[en]  의[ko]  ▁좋은[ko]  ▁예[ko]  라고[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='ko'
  context : ▁की[hi]  ▁तस्वीर[hi]  ▁देखकर[hi]  ▁sab[en]  >>ko[en]<<  ▁लगा[hi]  ▁कि[hi]  ▁ब्रह्मा[hi]  ंड[hi]  ▁कितना[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁premium'
  context : ers[en]  ▁को[hi]  ▁up[en]  front[en]  >>▁premium[en]<<  ▁देना[hi]  ▁होगा[hi]  ,[punct]  ▁तो[hi]  ▁शायद[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='ارة'
  context : ا[ar]  ▁معينة[ar]  ▁من[ar]  ▁الحج[ar]  >>ارة[ar]<<  ،[punct]  ▁showing[en]  ▁a[en]  ▁preference[en]  ▁that[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='ra'
  context : ▁de[es]  ▁que[es]  ▁la[es]  ▁producto[es]  >>ra[es]<<  ▁sea[en]  ▁nueva[es]  ▁y[es]  ▁esté[es]  ▁lider[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁the'
  context : ▁wait[en]  ▁and[en]  ▁see[en]  ▁what[en]  >>▁the[en]<<  ▁final[es]  ▁policy[en]  ▁will[en]  ▁be[en]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁our'
  context : .[punct]  ▁That[en]  ▁would[en]  ▁expose[en]  >>▁our[en]<<  ▁planet[es]  ▁to[en]  ▁much[en]  ▁higher[en]  ▁levels[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='▁El'
  context : es[en]  ▁more[en]  ▁research[en]  .[punct]  >>▁El[es]<<  ▁doctor[en]  ▁comenta[es]  ▁que[es]  ▁la[es]  ▁ciencia[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='▁بس'
  context : ▁بعض[ar]  ▁الم[ar]  شاهد[ar]  ،[punct]  >>▁بس[ar]<<  ▁honest[en]  ly[en]  ▁كنت[ar]  ▁فا[ar]  هم[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='▁이런'
  context : 종[ko]  ▁동[ko]  료[ko]  들과[ko]  >>▁이런[ko]<<  ▁tech[en]  ▁de[en]  als[en]  에[ko]  ▁대해[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='as'
  context : és[en]  ▁aux[fr]  ▁a[en]  lé[en]  >>as[en]<<  ▁du[fr]  ▁secteur[en]  ▁a[en]  érie[en]  n[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='에서'
  context : 도[ko]  ▁자신의[ko]  ▁보[ko]  트[ko]  >>에서[ko]<<  ▁Hur[en]  rica[en]  ne[en]  ▁Mil[en]  ton[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='顿'
  context : 了[zh]  南[zh]  安[zh]  普[zh]  >>顿[zh]<<  ，[punct]  send[en]  ▁them[en]  ▁to[en]  ▁rele[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁analyser'
  context : ▁Elle[fr]  >>▁analyser[fr]<<  a[en]  ▁les[fr]  ▁potential[fr]  ités[fr]  ▁d[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='▁보면'
  context : ▁요즘[ko]  ▁[punct]  엔터테인먼트[ko]  ▁프로그램[ko]  >>▁보면[ko]<<  ,[punct]  ▁military[en]  ▁fashion[en]  이[ko]  ▁진짜[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁से'
  context : ▁बिल्कुल[hi]  ,[punct]  ▁इसी[hi]  ▁वजह[hi]  >>▁से[hi]<<  ▁Russia[en]  ▁को[hi]  ▁काफी[hi]  ▁नुकसान[hi]  ▁हुआ[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁की'
  context : ▁age[en]  .[punct]  ▁हि[hi]  ना[hi]  >>▁की[hi]<<  ▁positiv[en]  ity[en]  ▁और[hi]  ▁courage[en]  ▁बहुत[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='REM'
  context : ▁sleep[en]  ,[punct]  ▁especially[en]  ▁[punct]  >>REM[es]<<  ▁and[en]  ▁deep[en]  ▁sleep[en]  ,[punct]  ▁impact[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='هم'
  context : ▁أن[ar]  ▁الفيلم[ar]  ▁أعط[ar]  ا[ar]  >>هم[ar]<<  ▁hope[en]  ▁للم[ar]  ستقبل[ar]  ،[punct]  ▁وهذا[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁forme'
  context : ▁était[en]  ▁toujours[en]  ▁en[fr]  ▁pleine[fr]  >>▁forme[fr]<<  ,[punct]  ▁I[en]  ▁was[en]  ▁feeling[en]  ▁terrible[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁बहुत'
  context : मन[hi]  ▁गि[hi]  ल[hi]  ▁ने[hi]  >>▁बहुत[hi]<<  ▁hard[en]  ▁work[en]  ▁किया[hi]  ▁था[hi]  ▁और[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='上'
  context : 。[punct]  ▁[punct]  我会[zh]  带[zh]  >>上[zh]<<  my[en]  ▁running[en]  ▁gear[en]  和[zh]  nutri[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='ات'
  context : ▁حول[ar]  ▁فوائد[ar]  ▁المخ[ar]  لل[ar]  >>ات[ar]<<  ،[punct]  ▁you[en]  ▁know[en]  ؟[punct]  ▁الدراسة[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁défi'
  context : ▁avec[fr]  ▁ce[fr]  ▁genre[fr]  ▁de[fr]  >>▁défi[fr]<<  ,[punct]  ▁because[en]  ▁risk[en]  ing[en]  ▁your[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁उसके'
  context : ▁face[en]  ▁critic[en]  ism[en]  ▁because[en]  >>▁उसके[hi]<<  ▁posts[en]  ▁पहले[hi]  ▁से[hi]  ▁ही[hi]  ▁Indian[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='病'
  context : ▁我[zh]  以前[zh]  从来没有[zh]  肾[zh]  >>病[zh]<<  ,[punct]  ▁but[en]  ▁last[en]  ▁week[en]  ▁I[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='▁crucial'
  context : ▁and[en]  ▁it[en]  '[punct]  s[en]  >>▁crucial[en]<<  ▁de[fr]  ▁respecter[fr]  ▁les[fr]  ▁victime[fr]  s[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='高'
  context : 查[zh]  出血[zh]  脂[zh]  偏[zh]  >>高[zh]<<  ，[punct]  the[en]  ▁doctor[en]  ▁advise[en]  d[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='에'
  context : ast[en]  가[ko]  ▁항상[ko]  ▁게임[ko]  >>에[ko]<<  ▁unexpected[en]  ▁twist[en]  s[en]  를[ko]  ▁넣어[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='▁बहुत'
  context : ▁ये[hi]  ▁मिस[hi]  ाइल[hi]  ें[punct]  >>▁बहुत[hi]<<  ▁powerful[en]  ▁हैं[hi]  ।[punct]  ▁They[en]  ▁have[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

## Qualitative Examples — MBERT

### Successful Predictions — Inter-sentential (48 examples)

```
[Chinese-English]  switch_type=inter  switch_token='##tive'
  context : is[en]  so[en]  ima[en]  ##gina[en]  >>##tive[en]<<  .[punct]  我[zh]  觉[zh]  得[zh]  这[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='है'
  context : ##न[hi]  ##ुक[hi]  ##रण[hi]  किया[hi]  >>है[hi]<<  ।[punct]  The[en]  simulation[en]  explore[en]  ##s[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='ci'
  context : ##r[fr]  cette[fr]  fois[fr]  -[punct]  >>ci[fr]<<  ?[punct]  I[en]  need[en]  to[en]  check[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='towns'
  context : ,[punct]  especially[en]  in[en]  small[en]  >>towns[en]<<  .[punct]  अ[hi]  ##गर[hi]  authorities[en]  ने[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='right'
  context : ##खन[hi]  ##ा[punct]  चाहिए[hi]  ,[punct]  >>right[en]<<  ?[punct]  म[hi]  ##च[hi]  ##्छ[hi]  ##रों[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='electric'
  context : stadium[en]  was[en]  absolute[en]  ##ly[en]  >>electric[en]<<  ![punct]  Les[fr]  joueurs[fr]  de[fr]  Van[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='##ness'
  context : o[en]  ##h[en]  my[en]  good[en]  >>##ness[en]<<  ![punct]  美[zh]  国[zh]  和[zh]  乌[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='جديدة'
  context : ##يج[ar]  ##رب[ar]  ح[ar]  ##اجات[ar]  >>جديدة[ar]<<  .[punct]  It[en]  [UNK][en]  s[en]  interesting[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##요'
  context : 조[ko]  ##용[ko]  ##하[ko]  ##네[ko]  >>##요[ko]<<  .[punct]  Even[en]  though[en]  mort[en]  ##gage[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='right'
  context : 생[ko]  ##각[ko]  ##해[ko]  ,[punct]  >>right[en]<<  ?[punct]  과[ko]  ##학[ko]  ##이[ko]  이[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='end'
  context : amis[fr]  ce[fr]  week[fr]  -[punct]  >>end[fr]<<  .[punct]  I[en]  mean[fr]  ,[punct]  Claude[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='dur'
  context : subir[fr]  ##ont[fr]  un[fr]  coup[fr]  >>dur[fr]<<  .[punct]  "[punct]  It[en]  made[en]  her[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='right'
  context : encore[fr]  une[fr]  fois[fr]  ,[punct]  >>right[fr]<<  ?[punct]  On[en]  se[fr]  demande[fr]  comment[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='##dor'
  context : proteger[es]  al[es]  con[es]  ##sumi[es]  >>##dor[es]<<  .[punct]  Maybe[en]  strict[en]  ##er[en]  inspection[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='##ing'
  context : results[en]  were[en]  sur[en]  ##pris[en]  >>##ing[en]<<  .[punct]  سب[ar]  ##ق[ar]  و[ar]  ##شاه[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='right'
  context : a[en]  muchas[es]  naciones[es]  ,[punct]  >>right[en]<<  ?[punct]  Vo[es]  ##y[es]  a[en]  discu[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='know'
  context : ##렸[ko]  ##어[ko]  ,[punct]  you[en]  >>know[en]<<  ?[punct]  두[ko]  팀[ko]  ##이[ko]  오[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='market'
  context : models[en]  for[en]  the[en]  current[en]  >>market[en]<<  .[punct]  요[ko]  ##즘[ko]  비[ko]  ##즈[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='know'
  context : ##ित[hi]  हैं[hi]  ,[punct]  you[en]  >>know[en]<<  ?[punct]  अ[hi]  ##गर[hi]  स[hi]  ##ु[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='忧'
  context : 人[zh]  感[zh]  到[zh]  担[zh]  >>忧[zh]<<  。[punct]  As[en]  a[en]  doctor[en]  ,[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='seriously'
  context : ##ोक[hi]  दिया[hi]  है[hi]  ,[punct]  >>seriously[en]<<  ![punct]  कुछ[hi]  students[en]  तो[hi]  बहुत[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='##s'
  context : aprender[es]  sobre[es]  nuevos[es]  descubrimiento[es]  >>##s[es]<<  .[punct]  Science[en]  is[en]  the[en]  poetry[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='है'
  context : ##ree[en]  2[en]  दे[hi]  ##खी[hi]  >>है[hi]<<  ?[punct]  It[en]  '[punct]  s[en]  really[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='it'
  context : ,[punct]  isn[fr]  '[punct]  t[en]  >>it[en]<<  ?[punct]  La[fr]  re[fr]  ##cons[fr]  ##titut[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='##س'
  context : ##فكر[ar]  ##ة[ar]  ك[ar]  ##وي[ar]  >>##س[ar]<<  .[punct]  It[en]  felt[en]  like[en]  I[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='##s'
  context : la[es]  tecnología[es]  de[es]  videojuego[es]  >>##s[es]<<  .[punct]  He[en]  immediately[en]  realized[en]  how[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='##ly'
  context : العالم[ar]  ،[punct]  hon[en]  ##est[en]  >>##ly[en]<<  .[punct]  سوف[ar]  أ[ar]  ##طل[ar]  ##ع[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='sure'
  context : ##عا[ar]  ##ئد[ar]  ,[punct]  for[en]  >>sure[en]<<  .[punct]  سوف[ar]  أ[ar]  ##تاب[ar]  ##ع[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='internacional'
  context : con[es]  la[es]  comunidad[es]  científica[es]  >>internacional[es]<<  .[punct]  This[en]  could[en]  lead[en]  to[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='right'
  context : cada[es]  rin[es]  ##cón[es]  ,[punct]  >>right[en]<<  ?[punct]  Se[es]  resp[es]  ##etar[es]  ##án[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##었다'
  context : 조[ko]  ##화를[ko]  이[ko]  ##루[ko]  >>##었다[ko]<<  .[punct]  Jeff[en]  Gold[en]  ##blu[en]  ##m[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='##سوق'
  context : م[ar]  ##باشر[ar]  على[ar]  ال[ar]  >>##سوق[ar]<<  .[punct]  It[en]  was[en]  interesting[en]  to[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='##गी'
  context : ट[hi]  ##ेस्ट[hi]  खेल[hi]  ##े[punct]  >>##गी[hi]<<  ।[punct]  The[en]  weather[en]  for[en]  ##eca[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='动'
  context : 的[zh]  战[zh]  争[zh]  行[zh]  >>动[zh]<<  。[punct]  This[en]  has[en]  caused[en]  a[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='##ed'
  context : the[en]  market[en]  re[en]  ##act[en]  >>##ed[en]<<  .[punct]  من[ar]  زمان[ar]  وأن[ar]  ##ا[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='empresa'
  context : la[es]  situación[es]  de[es]  la[es]  >>empresa[es]<<  .[punct]  The[en]  board[en]  ,[punct]  however[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='it'
  context : countries[en]  talk[en]  ##ed[en]  about[en]  >>it[en]<<  .[punct]  Muchos[es]  c[es]  ##re[es]  ##ían[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='team'
  context : missed[en]  by[en]  the[en]  whole[en]  >>team[en]<<  .[punct]  她[zh]  还[zh]  提[zh]  到[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##니다'
  context : ##응[ko]  ##하는[ko]  편[ko]  ##입[ko]  >>##니다[ko]<<  .[punct]  You[en]  never[en]  know[en]  where[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='region'
  context : big[en]  impact[en]  on[en]  the[en]  >>region[en]<<  。[punct]  作[zh]  为[zh]  一[zh]  个[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='know'
  context : 보[ko]  ##냈다[ko]  ,[punct]  you[en]  >>know[en]<<  ?[punct]  비[ko]  ##가[ko]  와[ko]  ##서[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='习'
  context : 个[zh]  性[zh]  化[zh]  学[zh]  >>习[zh]<<  。[punct]  But[en]  we[en]  still[en]  need[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='##يقية'
  context : ##من[ar]  ##اف[ar]  ##سة[ar]  الحق[ar]  >>##يقية[ar]<<  .[punct]  The[en]  atmosphere[en]  in[en]  Miami[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='##s'
  context : ##s[fr]  fr[fr]  ##é[fr]  ##quent[fr]  >>##s[fr]<<  .[punct]  But[en]  is[en]  it[en]  safe[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##했다'
  context : ##하다[ko]  ##고[ko]  생[ko]  ##각[ko]  >>##했다[ko]<<  .[punct]  All[en]  you[en]  need[en]  is[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='pays'
  context : pour[fr]  le[fr]  progrès[fr]  du[fr]  >>pays[fr]<<  .[punct]  But[en]  sometimes[en]  ,[punct]  disa[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='here'
  context : is[en]  for[en]  foreign[en]  businesses[en]  >>here[en]<<  .[punct]  讨[zh]  论[zh]  结[zh]  束[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='##where'
  context : making[en]  head[en]  ##lines[en]  every[en]  >>##where[en]<<  .[punct]  फ[hi]  ##़[punct]  ##ुट[hi]  ##ब[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

### Successful Predictions — Intra-sentential (48 examples)

```
[Chinese-English]  switch_type=intra  switch_token='##X'
  context : 斯[zh]  克[zh]  和[zh]  Space[en]  >>##X[en]<<  因[zh]  为[zh]  违[zh]  反[zh]  联[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='思'
  context : 退[zh]  让[zh]  的[zh]  意[zh]  >>思[zh]<<  ,[punct]  right[en]  ?[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='sometimes'
  context : dure[fr]  ##ment[fr]  ,[punct]  mais[fr]  >>sometimes[fr]<<  they[en]  need[en]  a[en]  break[en]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='a'
  context : los[es]  49[es]  ##ers[en]  va[es]  >>a[en]<<  jugar[es]  muy[es]  bien[es]  el[es]  próximo[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='##ment'
  context : व[hi]  ##ो[punct]  ex[en]  ##cite[en]  >>##ment[en]<<  अलग[hi]  ही[hi]  level[en]  का[hi]  होगा[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='उनकी'
  context : ##न[hi]  ##ना[hi]  है[hi]  कि[hi]  >>उनकी[hi]<<  business[en]  background[en]  उन्हें[hi]  अलग[hi]  बना[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='202'
  context : 在[zh]  >>202[zh]<<  ##4[en]  世[zh]  界[zh]  计[zh]  算[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='sector'
  context : यह[hi]  sustainable[en]  practice[en]  health[en]  >>sector[en]<<  में[hi]  भी[hi]  positive[en]  ब[hi]  ##दल[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##k'
  context : ##와[ko]  Elo[en]  ##n[en]  Mus[en]  >>##k[en]<<  같은[ko]  유[ko]  ##명[ko]  인[ko]  ##사의[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##지만'
  context : 추[ko]  ##측[ko]  ##을[ko]  했[ko]  >>##지만[ko]<<  ,[punct]  hon[en]  ##est[en]  ##ly[en]  ,[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='a'
  context : actores[es]  de[es]  voz[es]  frente[es]  >>a[en]<<  la[es]  intel[es]  ##igencia[es]  artificial[es]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='##t'
  context : ##ंत[hi]  doctor[en]  से[hi]  consul[en]  >>##t[en]<<  कर[hi]  ##ें[punct]  ।[punct]  Early[en]  diagnosis[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='[UNK]'
  context : 将[zh]  宣[zh]  布[zh]  的[zh]  >>[UNK][en]<<  对[zh]  等[zh]  关[zh]  税[zh]  [UNK][en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='待'
  context : 有[zh]  什[zh]  么[zh]  期[zh]  >>待[zh]<<  ，[punct]  especially[en]  after[en]  watching[en]  the[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##phone'
  context : 내[ko]  ##년에[ko]  새로운[ko]  smart[en]  >>##phone[en]<<  ##을[ko]  사[ko]  ##려[ko]  ##고[ko]  해[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[French-English]  switch_type=intra  switch_token='A'
  context : que[fr]  le[fr]  Livre[fr]  ##t[fr]  >>A[en]<<  va[fr]  évolue[fr]  ##r[fr]  ,[punct]  especially[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='الصغيرة'
  context : ال[ar]  ##ت[ar]  ##فا[ar]  ##صيل[ar]  >>الصغيرة[ar]<<  ،[punct]  believe[en]  me[en]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='हैं'
  context : ##se[en]  ब[hi]  ##ढ़[hi]  गए[hi]  >>हैं[hi]<<  after[en]  the[en]  announcement[en]  ?[punct]  Yes[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='TV'
  context : ##D[en]  -[punct]  OL[en]  ##ED[en]  >>TV[en]<<  ##에[ko]  대한[ko]  관[ko]  ##심[ko]  ##이[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='##bot'
  context : a[en]  usar[es]  su[es]  chat[en]  >>##bot[en]<<  favor[es]  ##ito[es]  para[es]  hacer[es]  la[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='A'
  context : who[en]  really[en]  knows[en]  ?[punct]  >>A[en]<<  veces[es]  sien[es]  ##to[es]  que[es]  la[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='##á'
  context : ,[punct]  y[es]  probablemente[es]  dir[es]  >>##á[es]<<  ,[punct]  "[punct]  Let[en]  me[en]  say[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='##tes'
  context : distintas[es]  sobre[es]  los[es]  magna[en]  >>##tes[en]<<  te[es]  ##c[es]  ##nol[es]  ##ógicos[es]  ,[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='a'
  context : Ce[fr]  que[fr]  Donald[fr]  Trump[fr]  >>a[en]<<  annoncé[fr]  sur[fr]  l[fr]  [UNK][fr]  arrêt[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='있어'
  context : 많은[ko]  논[ko]  ##의[ko]  ##가[ko]  >>있어[ko]<<  ,[punct]  you[en]  know[en]  ?[punct]  새로운[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='show'
  context : ##너[ko]  ##먼[ko]  ##트[ko]  selection[en]  >>show[en]<<  ##를[ko]  볼[ko]  것이다[ko]  .[punct]  그녀의[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='events'
  context : ##래[ko]  ##에[ko]  trauma[en]  ##tic[en]  >>events[en]<<  ##를[ko]  어[ko]  ##떻[ko]  ##게[ko]  기[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='##ude'
  context : '[punct]  in[en]  ##qui[en]  ##ét[en]  >>##ude[en]<<  en[fr]  Chine[en]  .[punct]  At[en]  that[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##ات'
  context : با[ar]  ##لم[ar]  ##وا[ar]  ##صف[ar]  >>##ات[ar]<<  ،[punct]  really[en]  a[en]  good[en]  deal[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='##mm'
  context : ##est[en]  ##ly[en]  ,[punct]  43[punct]  >>##mm[en]<<  也[zh]  有[zh]  自[zh]  己[zh]  的[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='alcohol'
  context : ##ción[es]  de[es]  dejar[es]  el[es]  >>alcohol[en]<<  en[es]  cierta[es]  edad[es]  para[es]  proteger[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='##U'
  context : .[punct]  टीम[hi]  में[hi]  AN[en]  >>##U[en]<<  के[hi]  researchers[en]  भी[hi]  शामिल[hi]  हैं[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##سرعة'
  context : العالم[ar]  بيت[ar]  ##غير[ar]  ب[ar]  >>##سرعة[ar]<<  ،[punct]  you[en]  know[en]  ?[punct]  أن[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='##y'
  context : ##ini[es]  ##tiva[es]  ##mente[es]  vo[es]  >>##y[es]<<  a[en]  estar[es]  más[es]  at[es]  ##enta[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='और'
  context : से[hi]  ,[punct]  उसने[hi]  treatment[en]  >>और[hi]<<  care[en]  को[hi]  sus[en]  ##tain[en]  किया[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='##ence'
  context : résultats[fr]  avec[fr]  im[fr]  ##pati[fr]  >>##ence[fr]<<  ,[punct]  of[en]  course[fr]  ![punct]  Tout[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##4'
  context : Flight[en]  Sim[en]  ##ulator[en]  202[en]  >>##4[en]<<  ال[ar]  ##شهر[ar]  الماضي[ar]  ،[punct]  وكانت[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##라'
  context : ##할[ko]  ##지[ko]  ##도[ko]  몰[ko]  >>##라[ko]<<  ,[punct]  sounds[en]  fun[en]  ![punct]  그녀는[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='من'
  context : ##لم[ar]  ##وس[ar]  ##م[ar]  الجديد[ar]  >>من[ar]<<  C[en]  ##rue[en]  ##l[en]  Int[en]  ##ention[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='Rahman'
  context : A[en]  .[punct]  R[en]  .[punct]  >>Rahman[en]<<  ح[ar]  ##سي[ar]  ##ت[ar]  ال[ar]  ##مو[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='supporters'
  context : the[en]  end[en]  .[punct]  Les[fr]  >>supporters[en]<<  sont[fr]  dé[fr]  ##çu[en]  ##s[en]  ,[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='months'
  context : in[en]  the[en]  next[en]  few[en]  >>months[en]<<  ，[punct]  因[zh]  为[zh]  反[zh]  对[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='[UNK]'
  context : 继[zh]  续[zh]  强[zh]  调[zh]  >>[UNK][en]<<  枫[zh]  桥[zh]  经[zh]  验[zh]  [UNK][en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='bike'
  context : की[hi]  ##मत[hi]  में[hi]  ये[hi]  >>bike[en]<<  सब[hi]  ##को[hi]  attract[en]  कर[hi]  ##े[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='dit'
  context : et[fr]  je[fr]  me[en]  suis[en]  >>dit[en]<<  que[fr]  c[fr]  [UNK][fr]  est[fr]  vraiment[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='و'
  context : بين[ar]  Xbox[en]  Game[en]  Studios[en]  >>و[ar]<<  ##O[en]  ##bs[en]  ##idia[en]  ##n[en]  Entertainment[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='##ble'
  context : ##iance[fr]  in[en]  ##cro[en]  ##ya[en]  >>##ble[en]<<  et[fr]  é[fr]  ##cout[fr]  ##er[fr]  les[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##اً'
  context : ##ا[ar]  الجديدة[ar]  ق[ar]  ##ريب[ar]  >>##اً[ar]<<  ,[punct]  right[en]  ?[punct]  سي[ar]  ##لاح[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=1 (predicted switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

### False Alarms — Inter-sentential (48 examples)

```
[Spanish-English]  switch_type=inter  switch_token='ciudad'
  context : identidad[es]  cultural[es]  de[es]  la[es]  >>ciudad[es]<<  .[punct]  La[es]  comunidad[es]  internacional[es]  debe[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='prevention'
  context : ##s[en]  for[en]  chronic[en]  disease[en]  >>prevention[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##cy'
  context : a[en]  tool[en]  for[en]  diploma[en]  >>##cy[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='##गी'
  context : eng[en]  ##aging[en]  रही[hi]  हो[hi]  >>##गी[hi]<<  ।[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='##tions'
  context : such[en]  shock[en]  ##ing[en]  revela[en]  >>##tions[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='meeting'
  context : some[en]  progress[en]  after[en]  the[en]  >>meeting[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='well'
  context : 예[ko]  ##정이[ko]  ##야[ko]  ,[punct]  >>well[en]<<  ?[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='involved'
  context : think[en]  about[en]  the[en]  challenges[en]  >>involved[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='investors'
  context : great[en]  opportunity[en]  for[en]  new[en]  >>investors[en]<<  .[punct]  Blue[en]  Cloud[en]  Soft[en]  ##ech[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

```
[French-English]  switch_type=inter  switch_token='##ry'
  context : felt[en]  un[en]  ##nec[en]  ##essa[en]  >>##ry[en]<<  .[punct]  Selon[en]  lui[en]  ,[punct]  la[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='development'
  context : care[en]  ##s[en]  about[en]  talent[en]  >>development[en]<<  。[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='him'
  context : who[en]  grew[en]  up[en]  with[en]  >>him[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='impressive'
  context : ##rib[en]  ##ers[en]  is[en]  still[en]  >>impressive[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='competition'
  context : despite[en]  the[en]  fie[en]  ##rce[en]  >>competition[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='know'
  context : ##ा[punct]  है[hi]  ,[punct]  you[en]  >>know[en]<<  ?[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='course'
  context : ##pati[fr]  ##ence[fr]  ,[punct]  of[en]  >>course[fr]<<  ![punct]  Tout[fr]  le[fr]  monde[fr]  va[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='exploration'
  context : politics[en]  might[en]  affect[en]  space[en]  >>exploration[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='teams'
  context : and[en]  integration[en]  of[en]  the[en]  >>teams[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='right'
  context : de[es]  las[es]  noticias[es]  ,[punct]  >>right[en]<<  ?[punct]  Me[en]  sor[es]  ##prende[es]  cómo[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='##way'
  context : mes[fr]  amis[fr]  ,[punct]  any[fr]  >>##way[fr]<<  .[punct]  Je[fr]  suis[fr]  s[fr]  ##ûr[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='##nce'
  context : ##pter[fr]  en[fr]  per[fr]  ##mane[fr]  >>##nce[fr]<<  .[punct]  Technology[fr]  is[en]  becoming[en]  a[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='है'
  context : ये[hi]  information[en]  बहुत[hi]  important[en]  >>है[hi]<<  ।[punct]  अ[hi]  ##गल[hi]  ##ी[punct]  बार[hi]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='fate'
  context : solar[en]  sector[en]  face[en]  this[en]  >>fate[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='too'
  context : your[en]  body[en]  needs[en]  balance[en]  >>too[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='##s'
  context : integrated[en]  into[en]  daily[en]  routine[en]  >>##s[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='know'
  context : ##ndió[es]  mucho[es]  ,[punct]  you[en]  >>know[en]<<  ?[punct]  Me[en]  pregunta[es]  ##ba[es]  cómo[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='special'
  context : which[en]  made[en]  my[en]  day[en]  >>special[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='jour'
  context : les[fr]  gens[fr]  vivent[fr]  chaque[fr]  >>jour[fr]<<  .[punct]  Access[fr]  to[en]  these[en]  new[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='system'
  context : ##aw[en]  ##s[en]  in[en]  the[en]  >>system[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='होगा'
  context : के[hi]  लिए[hi]  बहुत[hi]  useful[en]  >>होगा[hi]<<  ।[punct]  लेकिन[hi]  iPhone[en]  की[hi]  EMI[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='dernier'
  context : ##vée[fr]  l[fr]  '[punct]  an[en]  >>dernier[en]<<  .[punct]  This[en]  increase[en]  is[en]  really[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='right'
  context : última[es]  actual[es]  ##ización[es]  ,[punct]  >>right[en]<<  ?[punct]  A[en]  veces[es]  la[es]  tecnología[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='threat'
  context : my[en]  garden[en]  from[en]  this[en]  >>threat[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='[UNK]'
  context : ##온[ko]  게임[ko]  진[ko]  ##짜[ko]  >>[UNK][en]<<  .[punct]  Have[en]  you[en]  tried[en]  the[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='right'
  context : ##할[ko]  거[ko]  ##야[ko]  ,[punct]  >>right[en]<<  ?[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='##ups'
  context : some[en]  ex[en]  ##citing[en]  match[en]  >>##ups[en]<<  ?[punct]  Derek[en]  Brown[en]  ha[en]  proporciona[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='know'
  context : spot[en]  ##light[en]  ,[punct]  you[en]  >>know[en]<<  ?[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='morning'
  context : ##res[en]  ##hing[en]  in[en]  the[en]  >>morning[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='situation'
  context : what[en]  a[en]  tou[en]  ##gh[en]  >>situation[en]<<  ![punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='healthy'
  context : ref[en]  ##res[en]  ##hing[en]  and[en]  >>healthy[en]<<  ![punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='methods'
  context : s[en]  choice[en]  of[en]  execution[en]  >>methods[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='consequences'
  context : and[en]  uni[en]  ##nten[en]  ##ded[en]  >>consequences[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='去'
  context : 被[zh]  移[zh]  植[zh]  过[zh]  >>去[zh]<<  ？[punct]  大[zh]  家[zh]  都[zh]  在[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='proyecto'
  context : ##uc[es]  ##rado[es]  en[es]  el[es]  >>proyecto[es]<<  .[punct]  Es[es]  ##o[es]  le[en]  da[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='platforms'
  context : too[en]  dependent[en]  on[en]  these[en]  >>platforms[en]<<  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='##गा'
  context : controversy[en]  create[en]  कर[hi]  ##े[punct]  >>##गा[hi]<<  ।[punct]  अब[hi]  उनके[hi]  family[en]  members[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##요'
  context : ##말[ko]  궁[ko]  ##금[ko]  ##해[ko]  >>##요[ko]<<  .[punct]  그녀의[ko]  이야기[ko]  ##를[ko]  들[ko]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='athletes'
  context : ##ing[en]  stories[en]  behind[en]  the[en]  >>athletes[en]<<  。[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

### False Alarms — Intra-sentential (48 examples)

```
[Hindi-English]  switch_type=intra  switch_token='दिया'
  context : ##ना[hi]  ब[hi]  ##ंद[hi]  कर[hi]  >>दिया[hi]<<  था[hi]  ,[punct]  right[en]  ?[punct]  विशेष[hi]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='مختلفة'
  context : ##ها[ar]  مع[ar]  ##تقد[ar]  ##ات[ar]  >>مختلفة[ar]<<  حول[ar]  ال[ar]  ##لق[ar]  ##اح[ar]  ##ات[ar]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='[UNK]'
  context : C[fr]  >>[UNK][fr]<<  est[fr]  in[en]  ##cro[en]  ##ya[en]  ##ble[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##ات'
  context : ##ى[ar]  و[ar]  ##الم[ar]  ##علوم[ar]  >>##ات[ar]<<  ال[ar]  ##حساس[ar]  ##ة[ar]  .[punct]  Samsung[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='J'
  context : ,[punct]  you[fr]  know[fr]  ?[punct]  >>J[fr]<<  '[punct]  es[fr]  ##p[fr]  ##ère[fr]  que[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='well'
  context : ##له[ar]  ,[punct]  everything[en]  went[en]  >>well[en]<<  in[en]  the[en]  end[en]  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='theory'
  context : -[punct]  Lange[en]  ##vin[en]  quantum[en]  >>theory[en]<<  framework[en]  ![punct]  他[zh]  骑[zh]  着[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='##ovi'
  context : noticia[es]  sobre[es]  App[en]  ##L[en]  >>##ovi[en]<<  ##n[en]  fue[es]  realmente[es]  im[es]  ##presi[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='का'
  context : ##ा[punct]  है[hi]  कि[hi]  Apple[en]  >>का[hi]<<  इस[hi]  बार[hi]  का[hi]  launch[en]  बहुत[hi]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='worldwide'
  context : 200[en]  ,[punct]  000[punct]  devices[en]  >>worldwide[en]<<  ,[punct]  which[en]  makes[en]  detection[en]  and[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='test'
  context : about[en]  the[en]  simple[en]  blood[en]  >>test[en]<<  for[en]  heart[en]  attacks[en]  .[punct]  그녀의[ko]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##다'
  context : 사[ko]  ##고[ko]  ##가[ko]  났[ko]  >>##다[ko]<<  ##더[ko]  ##라[ko]  .[punct]  병[ko]  ##원에[ko]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='Lamar'
  context : nuevo[es]  LP[en]  de[es]  Kendrick[en]  >>Lamar[es]<<  en[es]  casa[es]  .[punct]  So[en]  catch[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='以'
  context : 的[zh]  企[zh]  业[zh]  可[zh]  >>以[zh]<<  交[zh]  流[zh]  经[zh]  验[zh]  ，[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='##re'
  context : a[en]  romantic[en]  ge[en]  ##stu[en]  >>##re[en]<<  ,[punct]  but[en]  also[en]  a[en]  reflect[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='Media'
  context : you[en]  know[en]  ?[punct]  People[en]  >>Media[en]<<  Factory[en]  हम[hi]  ##ेश[hi]  ##ा[punct]  interesting[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='suis'
  context : ##ions[fr]  ,[punct]  je[fr]  me[en]  >>suis[en]<<  rap[en]  ##pel[en]  ##é[en]  toutes[en]  ces[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='择'
  context : 不[zh]  错[zh]  的[zh]  选[zh]  >>择[zh]<<  ，[punct]  不[zh]  过[zh]  风[zh]  险[zh]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='signature'
  context : ##eur[fr]  était[en]  un[fr]  feature[en]  >>signature[en]<<  ,[punct]  giving[en]  them[en]  a[en]  sense[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='à'
  context : la[fr]  visite[fr]  du[fr]  président[fr]  >>à[fr]<<  Djibouti[fr]  pour[fr]  le[fr]  dî[fr]  ##ner[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##어'
  context : 못[ko]  ##한다[ko]  ##고[ko]  했[ko]  >>##어[ko]<<  ,[punct]  그리고[ko]  hon[en]  ##est[en]  ##ly[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='ai'
  context : J[fr]  '[punct]  >>ai[fr]<<  lu[fr]  cet[fr]  article[fr]  sur[fr]  le[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='election'
  context : ##ues[en]  during[en]  a[en]  papal[en]  >>election[en]<<  and[en]  attracted[en]  many[en]  award[en]  nominations[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##يبة'
  context : ال[ar]  ##نتيجة[ar]  م[ar]  ##خ[ar]  >>##يبة[ar]<<  ل[ar]  ##ل[ar]  ##آ[ar]  ##مال[ar]  حق[ar]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='extra'
  context : it[en]  was[en]  worth[en]  the[en]  >>extra[en]<<  money[en]  .[punct]  Il[fr]  a[en]  re[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='cooperation'
  context : 将[zh]  会[zh]  inspire[en]  global[en]  >>cooperation[en]<<  in[en]  the[en]  coming[en]  years[en]  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='best'
  context : उन[hi]  लोगों[hi]  के[hi]  लिए[hi]  >>best[en]<<  option[en]  हैं[hi]  जो[hi]  कम[hi]  budget[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='crucial'
  context : ##trition[en]  .[punct]  Il[fr]  est[fr]  >>crucial[fr]<<  de[fr]  rester[fr]  actif[fr]  ,[punct]  you[fr]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='mechanics'
  context : gameplay[en]  and[en]  innovative[en]  VR[en]  >>mechanics[en]<<  that[en]  truly[en]  s[en]  ##care[en]  ##d[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='Tina'
  context : >>Tina[en]<<  ne[en]  bat[en]  ##aya[en]  ki[en]  ja[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='##iva'
  context : ##mós[es]  ##fera[es]  in[es]  ##mers[es]  >>##iva[es]<<  y[es]  terror[es]  ##ífic[es]  ##a[es]  .[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##متاز'
  context : من[ar]  ##ظم[ar]  بشكل[ar]  م[ar]  >>##متاز[ar]<<  مع[ar]  م[ar]  ##شارك[ar]  ##ات[ar]  كثيرة[ar]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='وقت'
  context : ##س[ar]  أكثر[ar]  من[ar]  أي[ar]  >>وقت[ar]<<  م[ar]  ##ضى[ar]  ,[punct]  for[en]  sure[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='conté'
  context : amiga[es]  ##s[es]  ,[punct]  les[es]  >>conté[es]<<  sobre[es]  el[es]  incidente[es]  y[es]  todas[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='##bilidad'
  context : ##es[es]  sobre[es]  la[es]  culpa[es]  >>##bilidad[es]<<  de[es]  los[es]  hermanos[es]  .[punct]  It[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##니'
  context : 얘[ko]  ##기[ko]  ##했[ko]  ##으[ko]  >>##니[ko]<<  ##까[ko]  ,[punct]  I[en]  think[en]  people[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='Anand'
  context : यह[hi]  फिल्म[hi]  >>Anand[en]<<  ##hi[en]  के[hi]  लिए[hi]  बहुत[hi]  खा[hi]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='situación'
  context : man[es]  ##ej[es]  ##ó[es]  la[es]  >>situación[es]<<  con[es]  mucha[es]  clase[es]  .[punct]  We[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='them'
  context : can[en]  '[punct]  t[en]  let[en]  >>them[en]<<  down[en]  .[punct]  회[ko]  ##의[ko]  ##가[ko]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='time'
  context : prices[en]  for[en]  the[en]  first[en]  >>time[en]<<  in[en]  a[en]  decade[en]  ,[punct]  it[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='##n'
  context : decisiones[es]  judicial[es]  ##es[es]  afecta[es]  >>##n[es]<<  la[es]  confianza[es]  en[es]  el[es]  sistema[es]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='Alexis'
  context : ##가[ko]  ##인[ko]  Bryan[en]  ##과[ko]  >>Alexis[en]<<  Roberts[en]  ##의[ko]  script[en]  ##로[ko]  만[ko]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=1 (medium (3-6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='long'
  context : [UNK][en]  t[en]  last[en]  very[en]  >>long[en]<<  ,[punct]  which[en]  was[en]  disa[en]  ##ppo[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='يوم'
  context : ##كار[ar]  ##ات[ar]  تظهر[ar]  كل[ar]  >>يوم[ar]<<  ت[ar]  ##قر[ar]  ##يبا[ar]  ##ً[punct]  ,[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##견'
  context : 양[ko]  ##에서[ko]  ##도[ko]  발[ko]  >>##견[ko]<<  ##됐[ko]  ##다[ko]  ##던[ko]  ##데[ko]  ,[punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='nation'
  context : ##es[en]  people[en]  across[en]  the[en]  >>nation[en]<<  ,[punct]  show[en]  ##cas[en]  ##ing[en]  a[en]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='लगा'
  context : ##कर[hi]  बहुत[hi]  अ[hi]  ##च्छा[hi]  >>लगा[hi]<<  कि[hi]  Messi[en]  के[hi]  ब[hi]  ##ेट[hi]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='doubt'
  context : ##य[hi]  है[hi]  ,[punct]  no[en]  >>doubt[en]<<  about[en]  it[en]  ![punct]
  ysw_true=0 (no switch)
  ysw_pred=1 (predicted switch)
  ydur_true=-1 (n/a)
  ydur_pred=2 (long (>6 tok))
```

### Missed Switches — Inter-sentential (48 examples)

```
[Arabic-English]  switch_type=inter  switch_token='##يدة'
  context : ##روف[ar]  ج[ar]  ##فاف[ar]  شد[ar]  >>##يدة[ar]<<  .[punct]  Water[en]  management[en]  policies[en]  have[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='everyone'
  context : ##est[en]  ##ly[en]  hard[en]  for[en]  >>everyone[en]<<  .[punct]  现[zh]  在[zh]  黄[zh]  牛[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='Texas'
  context : energy[en]  companies[en]  are[en]  in[en]  >>Texas[en]<<  .[punct]  ي[ar]  ##قال[ar]  إن[ar]  ك[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='दी'
  context : ##त[hi]  की[hi]  स[hi]  ##जा[hi]  >>दी[hi]<<  ।[punct]  It[en]  '[punct]  s[en]  shock[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='##t'
  context : becoming[en]  more[en]  res[en]  ##ilien[en]  >>##t[en]<<  .[punct]  她[zh]  们[zh]  也[zh]  注[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##되었다'
  context : 편[ko]  ##지는[ko]  무[ko]  ##시[ko]  >>##되었다[ko]<<  .[punct]  It[en]  seems[en]  that[en]  br[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##돼'
  context : 경기[ko]  ##가[ko]  기[ko]  ##대[ko]  >>##돼[ko]<<  ![punct]  Pen[en]  ##ta[en]  ##의[ko]  스[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='hit'
  context : crew[en]  after[en]  such[en]  a[en]  >>hit[en]<<  ?[punct]  यह[hi]  फिल्म[hi]  दे[hi]  ##ख[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='partido'
  context : ##nar[es]  duro[es]  para[es]  el[es]  >>partido[es]<<  .[punct]  I[en]  hope[en]  my[en]  team[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='home'
  context : people[en]  play[en]  games[en]  at[en]  >>home[en]<<  .[punct]  의[ko]  ##사로[ko]  ##서[ko]  그녀는[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='있어'
  context : ##오[ko]  ##기를[ko]  바[ko]  ##라고[ko]  >>있어[ko]<<  .[punct]  If[en]  the[en]  deal[en]  goes[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='generations'
  context : be[en]  ##acon[en]  for[en]  future[en]  >>generations[en]<<  .[punct]  Son[fr]  h[fr]  ##éritage[fr]  inspire[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='奖'
  context : 贝[zh]  尔[zh]  化[zh]  学[zh]  >>奖[zh]<<  。[punct]  It[en]  '[punct]  s[en]  in[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='me'
  context : interesting[en]  for[en]  fans[en]  like[en]  >>me[en]<<  .[punct]  예[ko]  ##전에[ko]  ##는[ko]  이런[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='industry'
  context : ,[punct]  no[en]  matter[en]  the[en]  >>industry[en]<<  .[punct]  这[zh]  次[zh]  事[zh]  故[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='public'
  context : de[fr]  la[fr]  confiance[fr]  du[fr]  >>public[fr]<<  .[punct]  The[en]  phrase[fr]  "[punct]  encourage[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='किया'
  context : ख[hi]  ##त[hi]  ##्म[hi]  नहीं[hi]  >>किया[hi]<<  ।[punct]  Why[en]  do[en]  you[en]  think[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='élection'
  context : résultats[fr]  de[fr]  l[fr]  '[punct]  >>élection[fr]<<  .[punct]  I[en]  won[en]  ##der[en]  how[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='tier'
  context : value[en]  is[en]  top[en]  -[punct]  >>tier[en]<<  。[punct]  他[zh]  認[zh]  為[zh]  這[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='兴'
  context : 乎[zh]  民[zh]  族[zh]  复[zh]  >>兴[zh]<<  。[punct]  He[en]  used[en]  to[en]  say[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='का'
  context : है[hi]  advantage[en]  ले[hi]  ##ने[hi]  >>का[hi]<<  ।[punct]  The[en]  team[en]  should[en]  stay[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='design'
  context : have[en]  a[en]  brand[en]  new[en]  >>design[en]<<  .[punct]  Según[es]  los[es]  documentos[es]  internos[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='fiction'
  context : things[en]  were[en]  just[en]  science[en]  >>fiction[en]<<  ![punct]  Je[fr]  me[en]  sou[en]  ##vien[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##게'
  context : ##지[ko]  말[ko]  ##해[ko]  ##줄[ko]  >>##게[ko]<<  .[punct]  The[en]  news[en]  said[en]  someone[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##길'
  context : ##해[ko]  ##질[ko]  수[ko]  있[ko]  >>##길[ko]<<  .[punct]  He[en]  '[punct]  s[en]  been[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='especialista'
  context : consulta[es]  ##r[es]  a[en]  un[es]  >>especialista[es]<<  .[punct]  The[en]  doctor[en]  explained[en]  that[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='progress'
  context : be[en]  our[en]  key[en]  to[en]  >>progress[en]<<  .[punct]  في[ar]  ال[ar]  ##مس[ar]  ##ت[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='see'
  context : ,[punct]  we[en]  '[punct]  ll[en]  >>see[en]<<  ![punct]  Je[fr]  vai[fr]  ##s[fr]  lire[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='everything'
  context : Z[en]  ##Pa[en]  ##ss[en]  for[en]  >>everything[en]<<  ![punct]  ب[ar]  ##س[ar]  بر[ar]  ##ض[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='Ukraine'
  context : alliance[en]  between[en]  France[en]  and[en]  >>Ukraine[en]<<  .[punct]  我[zh]  作[zh]  为[zh]  一[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='intense'
  context : this[en]  time[en]  felt[en]  more[en]  >>intense[en]<<  .[punct]  شعر[ar]  ##ت[ar]  أن[ar]  قرار[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='together'
  context : can[en]  feel[en]  everyone[en]  coming[en]  >>together[en]<<  .[punct]  म[hi]  ##ैं[punct]  ##ने[hi]  भी[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='##vous'
  context : get[en]  a[en]  bit[en]  ner[en]  >>##vous[en]<<  .[punct]  Después[es]  del[es]  mit[en]  ##in[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='healthy'
  context : role[en]  in[en]  stay[en]  ##ing[en]  >>healthy[en]<<  .[punct]  Les[fr]  médecin[fr]  ##s[fr]  s[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='choice'
  context : before[en]  making[en]  a[en]  final[en]  >>choice[en]<<  .[punct]  في[ar]  ال[ar]  ##نهاية[ar]  ،[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=inter  switch_token='##tion'
  context : even[en]  more[en]  he[en]  ##sita[en]  >>##tion[en]<<  .[punct]  虽[zh]  然[zh]  AI[en]  和[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='well'
  context : check[en]  ##ups[en]  and[en]  eat[en]  >>well[en]<<  .[punct]  Ella[es]  dis[es]  ##fr[es]  ##uta[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='2025'
  context : ##ing[en]  on[en]  20[en]  January[en]  >>2025[en]<<  .[punct]  इस[hi]  कंपनी[hi]  का[hi]  share[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='##ble'
  context : which[en]  is[en]  ad[es]  ##mira[es]  >>##ble[es]<<  .[punct]  A[en]  veces[es]  ,[punct]  losing[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=inter  switch_token='pas'
  context : '[punct]  est[fr]  -[punct]  ce[fr]  >>pas[en]<<  ?[punct]  Sa[fr]  passion[fr]  pour[fr]  le[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='strategy'
  context : reste[en]  ##d[en]  showed[en]  good[en]  >>strategy[en]<<  .[punct]  र[hi]  ##ाज[hi]  ##को[hi]  ##ट[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='support'
  context : needs[en]  clear[en]  information[en]  and[en]  >>support[en]<<  .[punct]  Muchos[es]  padres[es]  estar[es]  ##án[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=inter  switch_token='##ra'
  context : tenía[es]  una[es]  personalidad[es]  inspirado[es]  >>##ra[es]<<  .[punct]  His[en]  contributions[en]  to[en]  social[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='##هم'
  context : ##ة[ar]  على[ar]  رو[ar]  ##اتب[ar]  >>##هم[ar]<<  .[punct]  Many[en]  believe[en]  it[en]  '[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=inter  switch_token='real'
  context : ،[punct]  ولكن[ar]  الأمر[ar]  أصبح[ar]  >>real[en]<<  .[punct]  في[ar]  الجامعة[ar]  ،[punct]  درس[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=inter  switch_token='science'
  context : this[en]  res[en]  ##ha[en]  ##pe[en]  >>science[en]<<  .[punct]  हम[hi]  ##ेश[hi]  ##ा[punct]  ल[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[French-English]  switch_type=inter  switch_token='##ble'
  context : ,[punct]  un[en]  ##beli[en]  ##eva[en]  >>##ble[en]<<  ![punct]  Même[fr]  à[fr]  son[fr]  âge[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=inter  switch_token='##어'
  context : ##이브[ko]  ##로[ko]  보고[ko]  싶[ko]  >>##어[ko]<<  .[punct]  I[en]  think[en]  watching[en]  it[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

### Missed Switches — Intra-sentential (48 examples)

```
[Hindi-English]  switch_type=intra  switch_token='ही'
  context : हम[hi]  ##ेश[hi]  ##ा[punct]  से[hi]  >>ही[hi]<<  top[en]  -[punct]  not[en]  ##ch[en]  रही[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##에'
  context : 그는[ko]  다음[ko]  달[ko]  >>##에[ko]<<  Real[en]  ID[en]  ##를[ko]  받[ko]  ##으[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='et'
  context : ##ge[en]  d[en]  '[punct]  insectes[en]  >>et[fr]<<  d[en]  '[punct]  animaux[en]  danger[en]  ##eux[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='लिए'
  context : इसे[hi]  दे[hi]  ##खने[hi]  के[hi]  >>लिए[hi]<<  tele[en]  ##scope[en]  ##s[en]  का[hi]  इस्तेमाल[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##즘'
  context : 요[ko]  >>##즘[ko]<<  PS[en]  ##5[en]  Pro[en]  가[ko]  ##격[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='किया'
  context : ##PR[en]  tool[en]  ##kit[en]  develop[en]  >>किया[hi]<<  genetic[en]  disorders[en]  के[hi]  treatment[en]  के[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='change'
  context : break[fr]  ##through[fr]  could[fr]  really[fr]  >>change[fr]<<  the[en]  game[en]  for[en]  nuclear[en]  energy[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##ly'
  context : ##어[ko]  .[punct]  Hon[en]  ##est[en]  >>##ly[en]<<  ,[punct]  그[ko]  기[ko]  ##술[ko]  ##이[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##에'
  context : 그[ko]  ##녀[ko]  ##가[ko]  다음[ko]  >>##에[ko]<<  [UNK][en]  할[ko]  ##지[ko]  궁[ko]  ##금[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='contra'
  context : el[es]  partido[es]  de[es]  Georgia[en]  >>contra[es]<<  Texas[en]  ?[punct]  That[en]  over[en]  ##tur[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='##é'
  context : un[fr]  avis[en]  tra[en]  ##nch[en]  >>##é[en]<<  sur[fr]  l[fr]  '[punct]  OL[fr]  ,[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##ت'
  context : ##rs[en]  و[ar]  ##اج[ar]  ##ه[ar]  >>##ت[ar]<<  bankruptcy[en]  problems[en]  .[punct]  اند[ar]  ##ه[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='##lé'
  context : '[punct]  en[en]  ai[en]  par[en]  >>##lé[en]<<  avec[fr]  mes[fr]  amis[fr]  après[fr]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='strategy'
  context : It[en]  '[punct]  s[en]  about[en]  >>strategy[en]<<  y[es]  el[es]  esfuerzo[es]  del[es]  equipo[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='赛'
  context : 选[zh]  赛[zh]  的[zh]  比[zh]  >>赛[zh]<<  ，[punct]  F[en]  ##P[en]  ##X[en]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='屏'
  context : 悟[zh]  空[zh]  》[punct]  刷[zh]  >>屏[zh]<<  ，[punct]  every[en]  ##where[en]  I[en]  looked[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='때'
  context : 처음[ko]  접[ko]  ##했[ko]  ##을[ko]  >>때[ko]<<  ,[punct]  shock[en]  ##ed[en]  by[en]  how[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='مرة'
  context : ,[punct]  seriously[en]  ![punct]  كل[ar]  >>مرة[ar]<<  Kevin[en]  Owens[en]  كان[ar]  ي[ar]  ##طل[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='sector'
  context : Americans[en]  and[en]  public[es]  -[punct]  >>sector[es]<<  workers[en]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##ري'
  context : ##ا[ar]  س[ar]  ##أ[ar]  ##شت[ar]  >>##ري[ar]<<  Air[en]  ##P[en]  ##ods[en]  Pro[en]  2[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='住'
  context : 强[zh]  调[zh]  要[zh]  抓[zh]  >>住[zh]<<  AI[en]  带[zh]  来[zh]  的[zh]  机[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='décision'
  context : att[en]  ##ente[en]  .[punct]  Cette[en]  >>décision[en]<<  va[fr]  s[fr]  ##ûr[fr]  ##ement[fr]  fac[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='realized'
  context : una[es]  vez[es]  ,[punct]  she[en]  >>realized[en]<<  que[es]  ne[es]  ##cesi[es]  ##taba[es]  leer[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='में'
  context : disease[en]  .[punct]  हम[hi]  future[en]  >>में[hi]<<  st[en]  ##imu[en]  ##late[en]  कर[hi]  ##ें[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='كثير'
  context : ،[punct]  و[ar]  ##نا[ar]  ##س[ar]  >>كثير[ar]<<  ex[en]  ##cited[en]  ي[ar]  ##ش[ar]  ##وف[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='especially'
  context : ala[es]  ##rman[es]  ##tes[es]  ,[punct]  >>especially[en]<<  porque[es]  la[es]  situación[es]  ha[en]  sido[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='Shadow'
  context : ##AC[en]  ##MS[en]  और[hi]  Storm[en]  >>Shadow[en]<<  म[hi]  ##िस[hi]  ##ा[punct]  ##इल[hi]  ##ें[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='A'
  context : .[punct]  F[en]  [UNK][en]  king[en]  >>A[en]<<  ,[punct]  정[ko]  ##말[ko]  대[ko]  ##단[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##에'
  context : ##대[ko]  ##돼[ko]  .[punct]  처음[ko]  >>##에[ko]<<  Mag[en]  ##S[en]  ##af[en]  ##e[en]  나[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Korean-English]  switch_type=intra  switch_token='##어'
  context : ##도[ko]  있다고[ko]  들[ko]  ##었[ko]  >>##어[ko]<<  ,[punct]  right[en]  ?[punct]  맞[ko]  ##아[ko]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[French-English]  switch_type=intra  switch_token='[UNK]'
  context : ,[punct]  well[en]  ,[punct]  c[en]  >>[UNK][en]<<  est[fr]  la[fr]  vie[fr]  à[fr]  mon[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='Y'
  context : >>Y[en]<<  染[zh]  色[zh]  体[zh]  正[zh]  在[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='Je'
  context : pot[fr]  ##enti[fr]  ##el[fr]  .[punct]  >>Je[fr]<<  me[en]  sou[en]  ##vien[en]  ##s[en]  avoir[fr]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='पर'
  context : ##ंग[hi]  ##ल[hi]  ग[hi]  ##्रह[hi]  >>पर[hi]<<  life[en]  possible[en]  है[hi]  ,[punct]  right[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##ly'
  context : ##رب[ar]  ي[ar]  ##ختار[ar]  wise[en]  >>##ly[en]<<  في[ar]  ال[ar]  ##در[ar]  ##افت[ar]  .[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='展'
  context : 国[zh]  家[zh]  的[zh]  发[zh]  >>展[zh]<<  ，[punct]  right[en]  ?[punct]  国[zh]  家[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##ي'
  context : في[ar]  مع[ar]  ##رض[ar]  جو[ar]  >>##ي[ar]<<  ،[punct]  but[en]  the[en]  local[en]  critics[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='##ات'
  context : ##د[ar]  ##ًا[ar]  ب[ar]  ##تطور[ar]  >>##ات[ar]<<  Apple[en]  Intelligence[en]  ،[punct]  you[en]  know[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=1 (medium (3-6 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='many'
  context : ##ly[en]  ,[punct]  losing[en]  so[en]  >>many[en]<<  stores[es]  could[en]  impact[en]  access[en]  to[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[French-English]  switch_type=intra  switch_token='So'
  context : ne[fr]  voulait[fr]  sortir[fr]  .[punct]  >>So[fr]<<  ,[punct]  we[en]  just[en]  made[en]  hot[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='的'
  context : ##a[en]  是[zh]  球[zh]  队[zh]  >>的[zh]<<  future[en]  key[en]  player[en]  。[punct]  库[zh]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='本'
  context : 款[zh]  新[zh]  遊[zh]  戲[zh]  >>本[zh]<<  ，[punct]  because[en]  the[en]  price[en]  -[punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=2 (long (>6 tok))
  ydur_pred=2 (long (>6 tok))
```

```
[Chinese-English]  switch_type=intra  switch_token='很'
  context : 真[zh]  的[zh]  觉[zh]  得[zh]  >>很[zh]<<  surprise[en]  ##d[en]  ![punct]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='lance'
  context : Cuando[es]  >>lance[en]<<  su[es]  próxima[es]  misión[es]  ,[punct]  everyone[en]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='बहुत'
  context : होता[hi]  तो[hi]  पृथ्वी[hi]  पर[hi]  >>बहुत[hi]<<  [UNK][en]  ब[hi]  ##दल[hi]  ##ाव[hi]  आ[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Hindi-English]  switch_type=intra  switch_token='की'
  context : ये[hi]  जा[hi]  ##न[hi]  ##ने[hi]  >>की[hi]<<  cu[en]  ##rios[en]  ##ity[en]  रही[hi]  कि[hi]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Spanish-English]  switch_type=intra  switch_token='y'
  context : ##gan[es]  la[es]  cal[es]  ##ma[es]  >>y[es]<<  rev[en]  ##isen[en]  las[es]  actual[es]  ##iza[es]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=0 (short (≤2 tok))
  ydur_pred=0 (short (≤2 tok))
```

```
[Arabic-English]  switch_type=intra  switch_token='في'
  context : لو[ar]  است[ar]  ##ث[ar]  ##مرت[ar]  >>في[ar]<<  N[en]  ##vid[en]  ##ia[en]  ،[punct]  م[ar]
  ysw_true=1 (switch occurs after this token)
  ysw_pred=0 (predicted no switch)
  ydur_true=1 (medium (3-6 tok))
  ydur_pred=0 (short (≤2 tok))
```
