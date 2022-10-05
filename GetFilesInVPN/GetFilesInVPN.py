import shutil, os

try:
    fileNumbers = ["701",
"696","697","702","699","698","694","689","700","690","695","691","692","693","679","680","681",
"682","683","684","685","686","687","688","781","787","778","777","788","786","779","785","789",
"776","782","775","765","766","767","768","769","770","771","772","773","774","912","918","911",
"910","907","913","914","919","908","917","915","909","916","906","892","893","894","895","896",
"897","898","899","900","901","902","903","904","905","1108","1109","1110","1111","1112","1113","1114",
"1115","1116","1117","1229","1230","1231","1232","1233","1234","1235","1236","1237","1238","1239","1240","1241",
"1242","1218","1219","1221","1222","1223","1224","1225","1226","1227","1228","1410","1411","1412","1413","1414",
"1415","1416","1417","1418","1419","1420","1421","1422","1423","1398","1399","1400","1401","1402","1403","1404",
"1405","1406","1407","1408","1409","1570","1571","1572","1573","1574","1575","1576","1577","1578","1579","1580",
"1581","1583","1556","1557","1558","1559","1560","1561",
"1562","1563","1564","1565","1566","1567","1568","1569",
"1769","1770","1771","1772","1773","1774","1775","1776",
"1777","1778","1780","1781","1782","1783","1784","1785",
"1786","1787","1789","1790","1791","1792","1795","1797",
"1798","1799","1964","1965","1966","1967","1968","1969",
"1970","1971","1972","1973","1974","1975","1976","1978",
"1980","1981","1982","1983","1984","1985","2103","2104",
"2105","2106","2107","2108","2109","2110","2111","2112",
"2115","2116","2117","2128",
"2131","2132","2118","2119","2120",
"2121","2122","2123","2124",
"2125","2126",
"2127","2345",
"2346","2347",
"2348","2349",
"2350","2351",
"2352","2353",
"2354","2355",
"2356","2357",
"2358","2359",
"2360","2335",
"2336","2337",
"2338","2339",
"2340","2341",
"2342","2343",
"2344","2482",
"2483","2484",
"2485","2486",
"2487","2488",
"2489","2490",
"2491","2492",
"2493","2494",
"2495","2496",
"2497","2498",
"2499","2500",
"2501","2502",
"2503","2504",
"2505","2506",
"2507","2508",
"2509","2665",
"2666","2667",
"2668","2669",
"2670","2671",
"2672","2673",
"2674","2675",
"2676","2695",
"2696","2699",
"2700","2701",
"2702",
"2703",
"2704",
"2705",
"2706",
"2645",
"2646",
"2647",
"2648",
"2649",
"2650",
"2651",
"2652",
"2653",
"2654",
"2655",
"2656",
"2657",
"2658",
"2659",
"2660",
"2792",
"2796",
"2797",
"2798",
"2799",
"2800",
"2801",
"2802",
"2803",
"2804",
"2805",
"2806",
"2807",
"2808",
"2809",
"2810",
"2811",
"2812",
"2813",
"3007",
"3008",
"3011",
"3012",
"3013",
"3014",
"3017",
"3018",
"2987",
"2988",
"2989",
"2991",
"2992",
"2993",
"2994",
"2995",
"2996",
"2997",
"2998",
"2999",
"3000",
"3001",
"3002",
"3194",
"3195",
"3198",
"3199",
"3200",
"3201",
"3204",
"3205",
"3206",
"3207",
"3208",
"3209",
"3210",
"3211",
"3212",
"3213",
"3214",
"3215",
"3216",
"3217",
"3302",
"3303",
"3306",
"3308",
"3310",
"3311",
"3314",
"3315",
"3316",
"3317",
"3318",
"3319",
"3320",
"3322",
"3323",
"3324",
"3325",
"3326",
"3327",
"3451",
"3452",
"3455",
"3456",
"3457",
"3458",
"3461",
"3462",
"3463",
"3464",
"3465",
"3466",
"3467",
"3468",
"3469",
"3470",
"3471",
"3472",
"3473",
"3474",
"3592",
"3593",
"3596",
"3597",
"3598",
"3599",
"3602",
"3603",
"3604",
"3605",
"3606",
"3607",
"3608",
"3609",
"3610",
"3611",
"3612",
"3613",
"3614",
"3615",
"3616",
"3617",
"3738",
"3739",
"3740",
"3741",
"3742",
"3743",
"3744",
"3745",
"3746",
"3747",
"3748",
"3749",
"3750",
"3751",
"3752",
"3753",
"3754",
"3755",
"3756",
"3757",
"3758",
"3759",
"3760",
"3761",
"3762",
"3763",
"3764",
"3765",
"3766",
"3767",
"3866",
"3867",
"3868",
"3869",
"3870",
"3871",
"3872",
"3873",
"3874",
"3875",
"3876",
"3877",
"3878",
"3879",
"3880",
"3881",
"3882",
"3883",
"3884",
"3885",
"3886",
"3887",
"3888",
"3889",
"3890",
"3891",
"3892",
"3893",
"3894",
"3895",
"4057",
"4058",
"4059",
"4060",
"4061",
"4062",
"4063",
"4064",
"4065",
"4066",
"4067",
"4068",
"4069",
"4070",
"4071",
"4072",
"4073",
"4074",
"4075",
"4076",
"4077",
"4078",
"4079",
"4080",
"4081",
"4082",
"4083",
"4084",
"4085",
"4086",
"4230",
"4231",
"4232",
"4233",
"4234",
"4235",
"4236",
"4237",
"4238",
"4239",
"4240",
"4241",
"4242",
"4243",
"4244",
"4245",
"4332",
"4333",
"4334",
"4335",
"4336",
"4337",
"4338",
"4339",
"4340",
"4341",
"4342",
"4343",
"4344",
"4345",
"4346",
"4347",
"4348",
"4349",
"4605",
"4606",
"4607",
"4608",
"4609",
"4610",
"4611",
"4612",
"4613",
"4615",
"4616",
"4623",
"4624",
"4627",
"4628",
"4629",
"4630",
"4632",
"4633",
"4634",
"4617",
"4618",
"4635",
"4636",
"4637",
"4638",
"4639",
"4640",
"4727",
"4728",
"4731",
"4732",
"4733",
"4734",
"4737",
"4738",
"4931",
"4932",
"4935",
"4936",
"4937",
"4938",
"4941",
"4942",
"5095",
"5096",
"5099",
"5100",
"5101",
"5102",
"5106",
"5239",
"5243",
"5244",
"5245",
"5246",
"5249",
"5250",
"5266",
"5353",
"5354",
"5355",
"5356",
"5357",
"5358",
"5359",
"5360",
"5361",
"5362",
"5363",
"5364",
"5365",
"5366",
"5507",
"5508",
"5509",
"5510",
"5511",
"5512",
"5513",
"5514",
"5515",
"5516",
"5517",
"5518",
"5627",
"5628",
"5629",
"5630",
"5631",
"5632",
"5633",
"5634",
"5635",
"5636",
"5637",
"5720",
"5721",
"5722",
"5723",
"5724",
"5725",
"5726",
"5727",
"5728",
"5729",
"5730",
"5731",
"5801",
"5802",
"5803",
"5804",
"5805",
"5806",
"5807",
"5808",
"5809",
"5810",
"5811",
"5914",
"5915",
"5916",
"5917",
"5918",
"5919",
"5920",
"5921",
"5922",
"5923",
"5924",
"5925",
"6056",
"6057",
"6058",
"6059",
"6060",
"6061",
"6062",
"6063",
"6064",
"6065",
"6066",
"6067",
"6068",
"6069",
"6070",
"6071",
"6072",
"6073",
"6074",
"6075",
"6076",
"6077",
"6197",
"6198",
"6199",
"6200",
"6201",
"6202",
"6203",
"6204",
"6205",
"6206",
"6207",
"6208",
"6209",
"6210",
"6286",
"6287",
"6288",
"6289",
"6290",
"6291",
"6292",
"6293",
"6294",
"6295",
"6296",
"6297",
"6298",
"6299",
"6300",
"6301",
"6302",
"6303",
"6304",
"6305",
"6306",
"6307",
"6308",
"6309",
"6310",
"6311",
"6312",
"6313",
"6314",
"6315",
"6472",
"6473",
"6474",
"6475",
"6476",
"6477",
"6478",
"6479",
"6480",
"6481",
"6482",
"6483",
"6484",
"6485",
"6486",
"6487",
"6488",
"6489",
"6490",
"6491",
"6492",
"6493",
"6494",
"6495",
"6496",
"6497",
"6498",
"6499",
"6500",
"6501",
"6776",
"6777",
"6778",
"6779",
"6780",
"6781",
"6785",
"6786",
"6787",
"6788",
"6789",
"6790",
"6791",
"6792",
"6805",
"6806",
"6807",
"6809",
"6810",
"6811",
"6812",
"6813",
"6814",
"6815",
"6816",
"6817",
"6818",
"6819",
"6793",
"6794",
"6795",
"6797",
"6798",
"6799",
"6800",
"6801",
"6802",
"6803",
"6804",
"6820",
"6821",
"6822",
"6823",
"6824",
"6825",
"6826",
"6827",
"6828",
"6829",
"6830",
"6985",
"6986",
"6987",
"6988",
"6989",
"6990",
"6991",
"6992",
"6993",
"6994",
"6995",
"6996",
"6997",
"6998",
"6999",
"7000",
"7001",
"7002",
"7003",
"7004",
"7005",
"7006",
"7007",
"7008",
"7009",
"7010",
"7248",
"7249",
"7250",
"7251",
"7252",
"7253",
"7254",
"7255",
"7256",
"7257",
"7258",
"7259",
"7260",
"7263",
"7264",
"7265",
"7266",
"7267",
"7268",
"7269",
"7270",
"7271",
"7272",
"7273",
"7324",
"7325",
"7326",
"7327",
"7328",
"7329",
"7330",
"7331",
"7332",
"7333",
"7334",
"7335",
"7336",
"7337",
"7338",
"7339",
"7340",
"7341",
"7342",
"7343",
"7344",
"7345",
]
    for fileNumber in fileNumbers:
        source = "\\10.7.8.4\dpc\NF liberadas por TAX"
        destination = "C:\Users\mmga\Desktop\Arquivos - Jurong"
        for filename in os.listdir(source):
            if "Vix" in filename and fileNumber in filename:
                shutil.move(source, destination)
except :
    pass