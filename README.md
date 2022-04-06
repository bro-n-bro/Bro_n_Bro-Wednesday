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
