t='''DUPLICATE
Branch of EUROPHARMA LLP Astana
BIN 080841000761
VAT Series 58001
№ 0014377
Box office 300-189
Shift 10
Serial number of the receipt No. 64
Receipt No. 2331180266
Cashier Pharmacy 17-1
sale
1.
Sodium chloride 0.9%, 200 ml, fl
2 000 x 154,00
308,00
Cost
308.00
2.
Boric alcohol 3%, 20 ml, fl.
1 000 x 51,00
51,00
Cost
51,00
3.
Syringe 2 ml, 3 comp. (Bioject)
2,000 x 16,00
32,00
Cost
32.00
4.
Vogt Medical Infusion System
2,000 x 60,00
120,00
Cost
120.00
5.
Naturella pads Classic maxi No.8
1,000 x 310,00
310,00
Cost
310.00
6.
AURA Cotton pads No.150
1,000 x 461,00
461,00
Cost
461.00
7.
Clean line scrub soft 50 ml
1,000 x 381,00
381,00
Cost
381.00
8.
Clean line scrub cleansing fabric 50 ml
1,000 x 386,00
386,00
Cost
386.00
9.
Clean line scrub soft 50 ml
1,000 x 381,00
381,00
Cost
381.00
10.
Carefree Aloe Air Permeable Wipes No. 20
1,000 x 414,00
414,00
Cost
414.00
11.
Pro Series Shampoo bright color 500ml
1,000 x 841,00
841,00
Cost
841.00
12.
Pro Series Balm-rinse for long-term care of colored hair Bright color 500ml
1,000 x 841,00
841,00
Cost
841.00
13.
Clear shampoo Active sport 2in1muzhskaya 400 ml
1,000 x 1 200,00
1 200,00
Cost
1 200,00
14.
Bio World (HYDRO THERAPY)Micellar water 5in1, 445ml
1,000 x 1 152,00
1 152,00
Cost
1,152.00
15.
Bio World (HYDRO THERAPY) Gel-mousse for washing with hyaluronic acid, 250ml
1,000 x 1 152,00
1 152,00
Cost
1,152.00
16.
[RX]-Sodium chloride 0.9%, 100 ml, fl.
1,000 x 168.00
168.00
Cost
168.00
17.
[RX]-Disol r-r 400 ml, fl.
1,000 x 163,00
163,00
Cost 163.00

18.
Tagansorbent with silver ions No. 30,por.
1 000 x 1 526,00
1 526,00
Cost
1 526,00
19.
[RX]-Cerucal 2%, 2 ml, No.10, amp.
2 000 x 396,00
792,00
Cost
792.00
20.
[RX]-Andazole 200 mg, No. 40, Table
1 000 x 7 330,00
7 330,00
Cost
7 330,00
Bank card:
18 009,00
TOTAL:
18,009.00
incl. VAT 12%:
0.00
Fiscal attribute:
2331180266
Time: 18.04.2019 11:13:58
Nur-sultan, Kazakhstan, Mangilik El,19, np-5
Operator of fiscal data: Kazakhtelecom JSC To check the receipt, go to the website:consumer.oofd.kz
FISCAL RECEIPT
fp
INC OFD: 311559
KKM KGD Code (RNM): 620300145316
ZNM: SWK00034961
WEBKASSA.KZ'''

import re
b='''AsdbaAbavFBbb'''
re.sub(r'(?<!^)(?=[A-Z])', '_', b).lower()
#print(re.sub(r'([A-Z])([a-z]*)', r'\1\2_', b).lower())