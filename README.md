# Bro_n_Bro IBC Lottery aka Bro Wednesday

## TL;DR

**Bro_n_Bro** IBC lottery is a number of events aimed to distribute IBC tokens between delegators **Bro_n_Bro** Validator. IBC lottery is taking action on every Wednesday starting Feb 16th. Distribution planning is a systematic approach of 12 rounds divided into 4 tours (3 rounds per tour) with 10 winners per round. The winners of each round will be defined by random picking python script and will be blacklisted till the next tour, in this way giving other participants a chance to win. To raise your winning chances delegate your assets to **Bro_n_Bro** Validator from one Keplr account to different chains - the more you delegate, the higher chances to win! There is a list of rewards distribution for each round. No need to claim the reward, transactions will be proceeded automatically. No registration, KYC or any other actions required. The IBC lottery is created with a purpose of cosmos network growth.

## Provisions

The main goal is to distribute a part of **bro-n-bro** validator's week commission income between winners every week. Not all `bro-n-bro` delegators are participating in that lottery. To avoid some kind of rush attacks was decided to cut addresses by median value divided to 1.618. The minimal amount for participation will be available on the game monitors.

#### The Game schema

The Game schema is divided into 4 tours by 3 rounds each. This way is 12 rounds or 12 weeks will have happened.

The rules for tours are similar:

0. Define the reward
1. Define the winners
2. Distribute rewards
3. Kick winners from distribution on the current tour.  

The black list of tour winners will have upgraded in each new tour started.

The schema:

| Tour | Round | Date | Percents of the week income |
| :---:| :---:| :---:| :---:|
|1|1|2022-03-30|5|
|1|2|2022-04-06|5|
|1|3|2022-04-13|5|
|2|1|2022-04-20|10|
|2|2|2022-04-27|10|
|2|3|2022-05-04|10|
|3|1|2022-05-11|15|
|3|2|2022-05-18|15|
|3|3|2022-05-25|15|
|4|1|2022-06-01|20|
|4|2|2022-06-08|30|
|4|3|2022-06-15|50|

#### The reward definition

The prize pool will have semi-automatically updated on the Game monitors. The final definition will be available one day before distribution, right after transferring the prize pool to the distribution address. The set of participants will have fixed at the moment of lottery starts. The prize pool will be consist of all tokens of **Bro_n_Bro** validated networks. The distribution will be in the **Osmosis** network.

#### The minimum delegation amount definition

The minimum delegation amount for each network is defined to avoid an attack on the lottery. This is a dynamic value that is calculated every 15 minutes with all other values.  The calculations are easy for understanding: the median of all delegations in each network is calculated and then divided by 1.618 (golden ratio). The calculated value is the minimum amount of delegation for participation. 

For instance. Let's define a network with token denom `token`. In that network, the bro_n_bro validator has 9 delegators with delegations in table below:

| Delegator | Delegation | Denom |
| :---| ---:| :---|
|networkaddress1|100|token|
|networkaddress2|98|token|
|networkaddress3|50|token|
|networkaddress4|45|token|
|***networkaddress5***|***45***|***token***|
|networkaddress6|45|token|
|networkaddress7|29|token|
|networkaddress8| 1|token|
|networkaddress9| 1|token|

The median (bolded address) is 45 tokens. This way the minimum amount of delegations for the network is `45 / 1.618 = 27.812`.

That means all delegators with delegations less than the calculated amount are excluded from the lottery. But, as said before, this value is dynamic, so each participant should follow this value if he wants to win a prize.

#### The winners definition

All **Bro_n_Bro** delegators in all **Bro_n_Bro** validated networks are participating. The algorithm of defining winners is very easy:

1. For each network distribute the winning points for each address. 3 points to addresses for the top ten delegators by their delegated amount of tokens (descending sorting). 2 points for delegators from 11 to 20 and 1 point for the rest delegators.

2. Convert all participated addresses to `osmo` address prefix and sum their points.

3. Multiplicate points of each address by the number of supported networks.

4. Create a list with addresses. Put each address N-times to the list, where N is a number of address points.

5. Randomly get the winner and kick his address from the list. Repeat while the number of winners will be 10.

6. The first address is the 1st place, the tenth is the 10th.

7. Distribute the rewards.

8. Put the winners' addresses into the black list till the end of the tour.

#### The rewards distribution

The reward distribution shares list is:

```python
[0.34141715125513766, 0.17070857630498384, 0.1138057175366559, 0.08535428815249192, 0.06828343052199354, 0.05690285876832795, 0.0487738789442811, 0.04267714407624596, 0.0379352391788853, 0.03414171526099677]
```

That means the first place address will get ~34% of the prize pool then the tenth - ~3.4%.

For instance, the prize pool in the round is 150 OSMO, 1000000000 BOOT, and 15 JUNO.

The distribution table will be:

| Address | Share | OSMO | BOOT | JUNO |
| :---:| :---:| :---:| :---:| :---:|
|osmoaddress1|0.34141715125513766|51,212572|341417151|5,121257|
|osmoaddress2|0.17070857630498384|25,606286|170708576|2,560628|
|osmoaddress3|0.1138057175366559|17,070857|113805717|1,707085|
|osmoaddress4|0.08535428815249192|12,803143|85354288|1,280314|
|osmoaddress5|0.06828343052199354|10,242514|68283430|1,024251|
|osmoaddress6|0.05690285876832795|8,535428|56902858|0,853542|
|osmoaddress7|0.0487738789442811|7,316081|48773878|0,731608|
|osmoaddress8|0.04267714407624596|6,401571|42677144|0,640157|
|osmoaddress9|0.0379352391788853|5,690285|37935239|0,569028|
|osmoaddress10|0.03414171526099677|5,121257|34141715|0,512125|
|total|1.0|149,999994|999999996|14,999995|

Then, all winner addresses go to the blacklist till the next tour.

#### The blacklist

To give a chance for all delegators the blacklist mechanics are provided. Besides adding the tour winners to the black list till the end of the tour all foundation addresses will be in permanently.

## Conclusion

The IBC lottery is a great chance to win some set of tokens without any additional actions, KYC, or whatever from the participants. It should help advanced cosmonauts and newcomers understand how IBC works and involve them in ecosystem networks life.

## Winners. Tour 4 Round 3

| address                                     |     ungm |    ujuno |   utick |     ustars |   ugraviton |       boot |    uosmo |
|:--------------------------------------------|---------:|---------:|--------:|-----------:|------------:|-----------:|---------:|
| osmo1uncwfa0p5sq2uaf8xazd9ndrrrhk8rhztxkchc | 51340605 | 28305190 |  716977 | 1079209247 |   114294788 | 1124705333 | 52149252 |
| osmo1679yrs8dmska7wcsawgy2m25kwucm3z0uxyaa3 | 25670303 | 14152595 |  358488 |  539604625 |    57147394 |  562352669 | 26074626 |
| osmo1fvfh8py05qqs5x3vz258gv68c3afh3y7uj5xml | 17113535 |  9435063 |  238992 |  359736417 |    38098262 |  374901779 | 17383084 |
| osmo1ws5my28ys2d3mmajn2c2r72qnyfqxa3leyf4qz | 12835151 |  7076297 |  179244 |  269802312 |    28573697 |  281176334 | 13037313 |
| osmo1hjm560zedyflcgc5w03m5w7cekc7hfx2f8d866 | 10268121 |  5661038 |  143395 |  215841850 |    22858957 |  224941067 | 10429850 |
| osmo1atqpalkryh98ll5uqsgl6rge83730lac4def2h |  8556767 |  4717531 |  119496 |  179868208 |    19049131 |  187450889 |  8691542 |
| osmo1jlu5u2sj0afddmcj7lxfy0ng466s8l2qx69fae |  7334372 |  4043598 |  102425 |  154172750 |    16327826 |  160672191 |  7449893 |
| osmo18ly3q3wdnpc98xf9gsuk2yhftnqnztv5ygj3d0 |  6417575 |  3538148 |   89622 |  134901156 |    14286848 |  140588167 |  6518656 |
| osmo1jextv724kkue3pt3me2zyyun9jaj75m39drtn5 |  5704511 |  3145021 |   79664 |  119912139 |    12699420 |  124967259 |  5794361 |
| osmo1hc0ltysu4n0x0hz59sk9zpwk55y4wrmwmg7q7p |  5134060 |  2830519 |   71697 |  107920925 |    11429478 |  112470533 |  5214925 |

## Winners. Tour 4 Round 2

| address                                     |     ungm |    ujuno |   utick |    ustars |   ugraviton |      boot |    uosmo |
|:--------------------------------------------|---------:|---------:|--------:|----------:|------------:|----------:|---------:|
| osmo140ua06006u0gew8yst4s24df4enfa46c28s9fn | 29600869 | 16388024 |  419944 | 630938896 |    65893511 | 938214333 | 31444521 |
| osmo1hlknvugejd4t5tjvurhdrjhsq94cyq0tt4vu69 | 14800434 |  8194012 |  209972 | 315469449 |    32946755 | 469107168 | 15722260 |
| osmo1zlzuq5tuzqmusahytz8mklud34l3n65vk7cyz7 |  9866956 |  5462675 |  139981 | 210312966 |    21964503 | 312738112 | 10481507 |
| osmo15ec9vpecxpqxgj79gp3tqwhllmgkne5wklldnc |  7400217 |  4097006 |  104986 | 157734724 |    16473377 | 234553584 |  7861130 |
| osmo1d5lu67hu3lhqtw6zyv7uy4gkfpdtfnzxx5act4 |  5920173 |  3277605 |   83988 | 126187779 |    13178702 | 187642867 |  6288904 |
| osmo15j3l0t4de2f39re2mz7eeh2jtzgq7k9sy84xwa |  4933478 |  2731337 |   69990 | 105156483 |    10982251 | 156369056 |  5240753 |
| osmo1cy7a7emfy2xuqkkz8sm346vm8euln0vc703gz7 |  4228695 |  2341146 |   59992 |  90134128 |     9413358 | 134030619 |  4492074 |
| osmo19plrfwtuggr9a3uywduwj9t0gnxdddqa697fhm |  3700108 |  2048503 |   52493 |  78867362 |     8236688 | 117276792 |  3930565 |
| osmo1v3l565wnxf4c95lj3393zap74f59hnr4nwckfd |  3288985 |  1820891 |   46660 |  70104322 |     7321501 | 104246037 |  3493835 |
| osmo1x8958xm5el05p4thmg3vajv883z2w434c3jcd0 |  2960086 |  1638802 |   41994 |  63093889 |     6589351 |  93821433 |  3144452 |

## Winners. Tour 4 Round 1

| address                                     |     ungm |    ujuno |   utick |    ustars |   ugraviton |      boot |    uosmo |
|:--------------------------------------------|---------:|---------:|--------:|----------:|------------:|----------:|---------:|
| osmo1mn23nz7zt4af8ds835yefrphrzaryks32l2snl | 17990636 | 10211788 |  265624 | 395968102 |    40466128 | 650087130 | 21779683 |
| osmo13x35tul2awvffdq8p5w4075qm68d9n2nvh05xj |  8995318 |  5105894 |  132812 | 197984052 |    20233064 | 325043566 | 10889841 |
| osmo1jgcvdrupnhp7qzuqft2w20zun95cnrglah86y4 |  5996878 |  3403929 |   88541 | 131989368 |    13488709 | 216695711 |  7259894 |
| osmo1yy7mamcpe9rr9886gh8xwrvnzv7y0hdx6tawhg |  4497659 |  2552947 |   66406 |  98992026 |    10116532 | 162521783 |  5444920 |
| osmo1zpk4af56a965n7vech2u23kfekcqhugjms78ev |  3598127 |  2042357 |   53124 |  79193620 |     8093225 | 130017426 |  4355936 |
| osmo1ymprf45c44rp9k0g2r84w2tjhsq7kalvw0ytf7 |  2998439 |  1701964 |   44270 |  65994684 |     6744354 | 108347855 |  3629947 |
| osmo16macu2qtc0jmqc7txvf0wkz84cycsx72v4svwd |  2570090 |  1458826 |   37946 |  56566872 |     5780875 |  92869590 |  3111383 |
| osmo17a0xkhvnavt3fx5rfkrq89gkt0genewqw5vzn0 |  2248829 |  1276473 |   33203 |  49496013 |     5058266 |  81260891 |  2722460 |
| osmo1zv3tckq563cnfhxpsm5qgdfcve0sk3lzsv4rlz |  1998959 |  1134643 |   29513 |  43996456 |     4496236 |  72231903 |  2419964 |
| osmo15ta7hrv2ejyucmfjf4707xx5fy8w0vxx5076ec |  1799063 |  1021178 |   26562 |  39596810 |     4046612 |  65008713 |  2177968 |

## Winners. Tour 3 Round 3

| address                                     |     ungm |    ujuno |   utick |    ustars |   ugraviton |      boot |    uosmo |
|:--------------------------------------------|---------:|---------:|--------:|----------:|------------:|----------:|---------:|
| osmo1e2qur2pmzn5jtderg3p7hwck53ert72tv9uk2p | 17000528 | 10099121 |  240700 | 911481370 |    37671458 | 603937566 | 14587902 |
| osmo1tz9jzsnuxrdp55f6wnf83ettjlkt8xd3uf6ar5 |  8500264 |  5049560 |  120350 | 455740687 |    18835729 | 301968784 |  7293951 |
| osmo1gg7z4cvgghdl30nhjhp388jvfp68rxlm8fs2pu |  5666842 |  3366373 |   80233 | 303827124 |    12557152 | 201312522 |  4862634 |
| osmo1z4sn4t3qkqt5lukv3pwxgrqdzjt23lwy0frs6a |  4250132 |  2524780 |   60175 | 227870343 |     9417864 | 150984392 |  3646975 |
| osmo134h2clsm8jeq7ku9v0ecplr8t8pnjrtcquvqny |  3400105 |  2019824 |   48140 | 182296274 |     7534291 | 120787513 |  2917580 |
| osmo17f9wn6hmcfph56kczul88ejcmx0gjmce2xjek2 |  2833421 |  1683186 |   40116 | 151913562 |     6278576 | 100656261 |  2431317 |
| osmo1x24e6ust4dsdtewuh4vcxrqddgjfahz33uukmv |  2428646 |  1442731 |   34385 | 130211624 |     5381636 |  86276795 |  2083986 |
| osmo1s8ftvy9crkta5yxr3vh98qkkn23u644akdqsae |  2125066 |  1262390 |   30087 | 113935171 |     4708932 |  75492196 |  1823487 |
| osmo1gmsvfd4jczze0dhu49ajng3h7q9kmcntgnhhgm |  1888947 |  1122124 |   26744 | 101275708 |     4185717 |  67104174 |  1620878 |
| osmo13sv4qp32xwqathqssdtr228eg92jz3qr8kh5fg |  1700052 |  1009912 |   24070 |  91148137 |     3767145 |  60393756 |  1458790 |

## Winners. Tour 3 Round 2

| address                                     |     ungm |   ujuno |   utick |    ustars |   ugraviton |      boot |    uosmo |
|:--------------------------------------------|---------:|--------:|--------:|----------:|------------:|----------:|---------:|
| osmo1vvsv5k6md3m5w02n7kk9w4w9ng9wtd4348eqch | 13609742 | 8475682 |  199730 | 298620513 |    31302150 | 475003977 | 14783364 |
| osmo1679yrs8dmska7wcsawgy2m25kwucm3z0uxyaa3 |  6804871 | 4237841 |   99865 | 149310257 |    15651075 | 237501989 |  7391682 |
| osmo14g346rvtyw7aac8qq5p9488ls8pqdk5ujs0ej0 |  4536580 | 2825227 |   66576 |  99540171 |    10434050 | 158334659 |  4927788 |
| osmo1yy7mamcpe9rr9886gh8xwrvnzv7y0hdx6tawhg |  3402435 | 2118920 |   49932 |  74655128 |     7825537 | 118750994 |  3695841 |
| osmo1ykyvwkzydq7u05q0yjzue7v7xva3wydq6pg5uh |  2721948 | 1695136 |   39946 |  59724102 |     6260430 |  95000795 |  2956672 |
| osmo1r90gx96qu6xd8unlpya4m7ghwc004gpwpl5snk |  2268290 | 1412613 |   33288 |  49770085 |     5217025 |  79167329 |  2463894 |
| osmo1w9w8y9fjq9hxjdcmcnyn8ua0u7ghfpaqva0hma |  1944248 | 1210811 |   28532 |  42660073 |     4471735 |  67857711 |  2111909 |
| osmo1g00rzta7g52q94jjau5nz05vw708j0t6nvdht7 |  1701217 | 1059460 |   24966 |  37327564 |     3912768 |  59375497 |  1847920 |
| osmo18n3vlcthxv5s2s4zgjdrjr5a6lw9e7tm09jk8t |  1512193 |  941742 |   22192 |  33180057 |     3478016 |  52778219 |  1642596 |
| osmo15m0ecmh7mplgqjlwmdxqyd56482zd47lkmc3uk |  1360974 |  847568 |   19973 |  29862051 |     3130215 |  47500397 |  1478336 |

## Winners. Tour 3 Round 1

| address                                     |     ungm |    ujuno |   utick |    ustars |   ugraviton |      boot |    uosmo |
|:--------------------------------------------|---------:|---------:|--------:|----------:|------------:|----------:|---------:|
| osmo18tq9gk04sfrdmms4e2kd5wa4lh5r62k2gvj7t0 | 14682646 | 10106803 |  189488 | 317927653 |    32499498 | 497046895 | 13482224 |
| osmo13dpy00jest96g7h5vdgvg9zpxq6xnclhll9du2 |  7341323 |  5053401 |   94744 | 158963827 |    16249749 | 248523448 |  6741112 |
| osmo1h50x8jphk6q0ksc5djlfrd7sujs6jdcghscn3g |  4894215 |  3368934 |   63162 | 105975884 |    10833166 | 165682299 |  4494074 |
| osmo1m8a5uw2a9cfuea32psudjqkk4yln9qsw54p0ne |  3670661 |  2526700 |   47372 |  79481913 |     8124874 | 124261724 |  3370556 |
| osmo1uwenqayqm823g33nxnzguhtytq8erc48686ulv |  2936529 |  2021360 |   37897 |  63585530 |     6499899 |  99409379 |  2696444 |
| osmo1qeua96a0v2mudxa9cv7mw4fqrw8yddrltwxvyy |  2447107 |  1684467 |   31581 |  52987942 |     5416583 |  82841149 |  2247037 |
| osmo15mw3j22qd9dmnh7vgqcrn2teugkpjtfxyjtfl7 |  2097520 |  1443829 |   27069 |  45418236 |     4642785 |  71006699 |  1926032 |
| osmo1959r3zp37k9yuz8kjtc4feayyfkkxpcv7eul8m |  1835330 |  1263350 |   23686 |  39740956 |     4062437 |  62130862 |  1685278 |
| osmo18nw5pjlrq3s2ungfmg45lqmygfcdymwhfvus79 |  1631405 |  1122978 |   21054 |  35325294 |     3611055 |  55227433 |  1498024 |
| osmo1926sjp9jpwluh6nct72hs0g0af40qy5ntt2jev |  1468264 |  1010680 |   18948 |  31792765 |     3249949 |  49704689 |  1348222 |

## Winners. Tour 2 Round 3

| address                                     |    ungm |   ujuno |   utick |    ustars |   ugraviton |      boot |   uosmo |
|:--------------------------------------------|--------:|--------:|--------:|----------:|------------:|----------:|--------:|
| osmo1vxurf7gcsrn6unggcez7agvdnjyvpxq7e8rmxs | 9973821 | 9645035 |  121546 | 191268718 |    22448520 | 321555481 | 7905857 |
| osmo15mw3j22qd9dmnh7vgqcrn2teugkpjtfxyjtfl7 | 4986910 | 4822517 |   60773 |  95634359 |    11224260 | 160777741 | 3952928 |
| osmo1w9e4nk4qqchvvm8s7y8v84xw07fe3mx67d5zd2 | 3324607 | 3215011 |   40515 |  63756239 |     7482840 | 107185160 | 2635285 |
| osmo1g3p420t58q0fsxjhws6tfur5ylsummmaug4qe7 | 2493455 | 2411258 |   30386 |  47817179 |     5612130 |  80388870 | 1976464 |
| osmo1paq5h6cp2fcwv2969xs6vr6ljtyaj3fv8kfkcs | 1994764 | 1929007 |   24309 |  38253743 |     4489704 |  64311096 | 1581171 |
| osmo1ky8473adh7mgzsw6cwnzqmhvj96vqe80rxxak8 | 1662303 | 1607505 |   20257 |  31878119 |     3741420 |  53592580 | 1317642 |
| osmo14ghs6hs8xkl9racufmqnvmg4l0n7unhpckqdae | 1424831 | 1377862 |   17363 |  27324102 |     3206931 |  45936497 | 1129408 |
| osmo1edugrjmqdlf94nqtp83knhsz2c32wv0uz0eylq | 1246727 | 1205629 |   15193 |  23908589 |     2806065 |  40194435 |  988232 |
| osmo16phjecw25muxjyxgft4jxmwntvx24xhcmh3lhc | 1108202 | 1071670 |   13505 |  21252079 |     2494280 |  35728386 |  878428 |
| osmo1ssyzemwsazljwejglwyt7e5t8v3nzmrdlvus0p |  997382 |  964503 |   12154 |  19126871 |     2244852 |  32155548 |  790585 |

## Winners. Tour 2 Round 2

| address                                     |    ungm |   ujuno |   utick |    ustars |   ugraviton |      boot |   uosmo |
|:--------------------------------------------|--------:|--------:|--------:|----------:|------------:|----------:|--------:|
| osmo167mlc0ya0hzp86s0h735cnjlf6re0nxj67wucp | 9975527 | 7778851 |  113693 | 175544067 |    22655761 | 304586796 | 7905857 |
| osmo1vtlq7spnshlmpu6ev0cdemcqpf6t673m53lu5v | 4987763 | 3889425 |   56846 |  87772034 |    11327880 | 152293398 | 3952928 |
| osmo1s2a7rckcky6jmhncxwy0xtwf2ymg87puaj4z2h | 3325175 | 2592950 |   37897 |  58514689 |     7551920 | 101528932 | 2635285 |
| osmo1mdcmajvfgs0cx08enmj4zv6kp2vge8jcvvvd43 | 2493881 | 1944712 |   28423 |  43886017 |     5663940 |  76146699 | 1976464 |
| osmo1azl8d4w3vmxe4pv80xw2fwyphzr23kqzp2k796 | 1995105 | 1555770 |   22738 |  35108813 |     4531152 |  60917359 | 1581171 |
| osmo1xxhn7zrdjgmr8lvkxn3mvgaul7zv083rqus5kp | 1662587 | 1296475 |   18948 |  29257344 |     3775960 |  50764466 | 1317642 |
| osmo1t8c83d9t44t829pzjq9uxc9aq5kzf64xkqjdhv | 1425075 | 1111264 |   16241 |  25077724 |     3236537 |  43512399 | 1129408 |
| osmo1sxk4st7m2v6tg27h7fhsjutwspmjdlfmdv4mkl | 1246940 |  972356 |   14211 |  21943008 |     2831970 |  38073349 |  988232 |
| osmo13nzzsqenw5r98x7lpwxy2f5l5mq2gncgetfwpl | 1108391 |  864316 |   12632 |  19504896 |     2517306 |  33842977 |  878428 |
| osmo1tzk22rvpcplurat85v6yzsluzm6ajl0n7p3yf2 |  997552 |  777885 |   11369 |  17554406 |     2265576 |  30458679 |  790585 |

## Winners. Tour 2 Round 1

| address                                     |     ungm |   ujuno |   utick |    ustars |   ugraviton |      boot |   uosmo |
|:--------------------------------------------|---------:|--------:|--------:|----------:|------------:|----------:|--------:|
| osmo10x2t27pthskehz5tefe3tsghla55470h3mp8wp | 10129848 | 7845767 |  114718 | 179564255 |    27162808 | 298801114 | 7677107 |
| osmo1zv35taypuhgeqxmv38hucfcshf8uyfwcy4vhgm |  5064924 | 3922883 |   57359 |  89782128 |    13581404 | 149400558 | 3838553 |
| osmo1sah5fvjft7e60ufwahkv3m73r2uwm6qj4d3sc5 |  3376616 | 2615255 |   38239 |  59854752 |     9054269 |  99600372 | 2559035 |
| osmo1jmvdlyau9h52arp6s6836k7m8u6xkuf7u0xuh2 |  2532462 | 1961441 |   28679 |  44891064 |     6790702 |  74700279 | 1919276 |
| osmo1ffve0zx389ffl80ae9t8jmghcjuzdlqrl368pc |  2025969 | 1569153 |   22943 |  35912851 |     5432561 |  59760223 | 1535421 |
| osmo1plxajyqwe97ghd4em2xgd39wzvr27aelnn2yfj |  1688308 | 1307627 |   19119 |  29927376 |     4527134 |  49800186 | 1279517 |
| osmo1sug63zszkvas04lwhfckmqkkrs4u4lcsjy9m2g |  1447121 | 1120823 |   16388 |  25652036 |     3880401 |  42685873 | 1096729 |
| osmo1unq30l8r6cu5typqf8s3t99ux5zw9sa9me94tt |  1266231 |  980720 |   14339 |  22445532 |     3395351 |  37350139 |  959638 |
| osmo1z63r2yzl5gztm03zewl3l3mrlh65gcjsakezdn |  1125538 |  871751 |   12746 |  19951584 |     3018089 |  33200124 |  853011 |
| osmo1js2p0vzlwh4r0wruz8hy29m73vn3jejpw33e2g |  1012984 |  784576 |   11471 |  17956425 |     2716280 |  29880111 |  767710 |

## Winners. Tour 1 Round 3

| address                                     |    ungm |   ujuno |   utick |   ustars |   ugraviton |      boot |   uosmo |
|:--------------------------------------------|--------:|--------:|--------:|---------:|------------:|----------:|--------:|
| osmo10py9qrj0rrf052fs38qd74rlnpjduhg598u2sl | 4899337 | 2267012 |   55311 | 87086981 |    15006993 | 144939980 | 3827288 |
| osmo1s2a7rckcky6jmhncxwy0xtwf2ymg87puaj4z2h | 2449668 | 1133506 |   27655 | 43543490 |     7503496 |  72469990 | 1913644 |
| osmo1jvw3n50rznxa2c4yfnd4pvmmcdymwpa4yer794 | 1633112 |  755670 |   18437 | 29028993 |     5002331 |  48313326 | 1275762 |
| osmo1yhppklazvehhap0je5lerlpuwzq9jhzvc9ru7w | 1224834 |  566753 |   13827 | 21771745 |     3751748 |  36234995 |  956822 |
| osmo1dlyccvmvcewd2mahhs5n69n3ves4ldtlym4l90 |  979867 |  453402 |   11062 | 17417396 |     3001398 |  28987996 |  765457 |
| osmo1vcs68xf2tnqes5tg0khr0vyevm40ff6zn0dqs6 |  816556 |  377835 |    9218 | 14514496 |     2501165 |  24156663 |  637881 |
| osmo1eze56tv3cuv0ys3fppmjjzhhgyux3djv979d96 |  699905 |  323858 |    7901 | 12440997 |     2143856 |  20705711 |  546755 |
| osmo19esp908j9he2em56tqympuz3c2zeffp3sdw9qg |  612417 |  283376 |    6913 | 10885872 |     1875874 |  18117497 |  478411 |
| osmo1atevshfyd6sdmydj4wk508gh99nrk46kfk0wpa |  544370 |  251890 |    6145 |  9676331 |     1667443 |  16104442 |  425254 |
| osmo15cxzysdx8aavudyr8phtreq2uw6k5j3gfl7ljp |  489933 |  226701 |    5531 |  8708698 |     1500699 |  14493998 |  382728 |

## Winners. Tour 1 Round 2

| address                                     |    ungm |   ujuno |   utick |   ustars |   ugraviton |      boot |   uosmo |
|:--------------------------------------------|--------:|--------:|--------:|---------:|------------:|----------:|--------:|
| osmo1vghct4lm8hp5ntxtm0l0g5evz2vxqp7m28fmfh | 4757650 | 3755589 |   52579 | 83322686 |    14926418 | 141088988 | 3762076 |
| osmo1a6kfadt24cgm9fy8z564jrglc27vtfz978j8ym | 2378825 | 1877794 |   26289 | 41661343 |     7463209 |  70544494 | 1881038 |
| osmo1pyrpuy567yu9tze5xrwttacfq9r76xlk7x7yf6 | 1585883 | 1251863 |   17526 | 27774229 |     4975472 |  47029662 | 1254025 |
| osmo1h4w509ewf0wh6m3d9fqyak9z45m9lrqsy5r63n | 1189412 |  938897 |   13144 | 20830671 |     3731604 |  35272247 |  940519 |
| osmo1ez0jlywwr8ysfmkp9tmse4q4v32w3m3awq7xc5 |  951530 |  751117 |   10515 | 16664537 |     2985283 |  28217797 |  752415 |
| osmo1lvwg06eawdltptpt8jt3wwuy7x0a4dl9nh3uqf |  792941 |  625931 |    8763 | 13887114 |     2487736 |  23514831 |  627012 |
| osmo1ykf3dvdumzarls3ugl76jqu3d6xcg295lymhtq |  679664 |  536512 |    7511 | 11903241 |     2132345 |  20155569 |  537439 |
| osmo1ankp34c85s4340jteh8y8hryl4qz76nw3w08z3 |  594706 |  469448 |    6572 | 10415335 |     1865802 |  17636123 |  470259 |
| osmo10vtw8cc7gfu662ckajmgldwf3es37fqlxvcaat |  528627 |  417287 |    5842 |  9258076 |     1658490 |  15676554 |  418008 |
| osmo1fvfh8py05qqs5x3vz258gv68c3afh3y7uj5xml |  475765 |  375558 |    5257 |  8332268 |     1492641 |  14108898 |  376207 |

## Winners. Tour 1 Round 1

| address                                     |    ungm |   ujuno |   utick |    ustars |   ugraviton |      boot |   uosmo |
|:--------------------------------------------|--------:|--------:|--------:|----------:|------------:|----------:|--------:|
| osmo1ks2z0xl2dczwlavfyk24v36xhl9jx3xgqwh507 | 4818590 | 3672112 |   51212 | 158999845 |    14785069 | 132274793 | 3725373 |
| osmo10lp0ehzrmf3gq2vjumk4vw452u44tjhy7ts2nq | 2409295 | 1836056 |   25606 |  79499922 |     7392534 |  66137397 | 1862686 |
| osmo1xppn98w0gg6wl0q2g2nasmkqlf2elwpkh96gzk | 1606196 | 1224037 |   17070 |  52999948 |     4928356 |  44091598 | 1241791 |
| osmo1ryacht55dn8nu0qajngptmfve76lmc7cuz6fvs | 1204647 |  918028 |   12803 |  39749961 |     3696267 |  33068698 |  931343 |
| osmo1dsrt9h4wjqwuv9wc02jn05qmr60thap8l9gqms |  963718 |  734422 |   10242 |  31799969 |     2957013 |  26454958 |  745074 |
| osmo1k7dah7ptpu4r7mfu5f2q6uedxsjqc2xtg24zsu |  803098 |  612018 |    8535 |  26499974 |     2464178 |  22045799 |  620895 |
| osmo1m2wjpcc9lvspndvuwnk3d9zml9s76v7vd679qz |  688370 |  524587 |    7316 |  22714263 |     2112152 |  18896399 |  532196 |
| osmo1pmaltcu0x97x8j5klc8xluaapkzcvztcczt4nm |  602323 |  459014 |    6401 |  19874980 |     1848133 |  16534349 |  465671 |
| osmo1a40llxlvkr7fxlff77k7q6nwrl7ec8a0yfqxwm |  535398 |  408012 |    5690 |  17666649 |     1642785 |  14697199 |  413930 |
| osmo1yfq24dsvn45g8tt8xhd9tlshr4638y5s2x5quc |  481859 |  367211 |    5121 |  15899984 |     1478506 |  13227479 |  372537 |
