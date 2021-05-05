from sys import argv
from base64 import b64encode
from json import dumps
ENCODING='utf-8' # 指定编码形式

# 获得文件名参数
IMAGE_NAME='C:/Users/86177/Desktop/exam/test/d7_10_120_150.jpg'
JSON_NAME='C:/Users/86177/Desktop/exam/test/d7_1.json'



# 以二进制读取图片，获得原始字节码，注意'rb'
with open(IMAGE_NAME,'rb')as jpg_file:
    byte_content=jpg_file.read()

base64_bytes=b64encode(byte_content) # 把原始字节码编码成base64字节码
base64_string=base64_bytes.decode(ENCODING) # 将base64字节码解码成utf-8格式的字符串

# 用字典形式保存数据
raw_data={}
raw_data["version"]="4.5.6"
raw_data['flags']={}

raw_data["shapes"]=[
    {
      "label": "mid",
      "points": [
        [
          755.5555555555555,
          23.209876543209877
        ],
        [
          759.0123456790124,
          224.93827160493828
        ],
        [
          799.7530864197531,
          224.44444444444446
        ],
        [
          796.0493827160494,
          22.469135802469136
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "low",
      "points": [
        [
          807.9012345679013,
          24.938271604938272
        ],
        [
          812.8395061728395,
          223.95061728395063
        ],
        [
          853.3333333333334,
          223.95061728395063
        ],
        [
          849.6296296296297,
          23.209876543209877
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "low",
      "points": [
        [
          701.2345679012346,
          23.703703703703706
        ],
        [
          704.6913580246913,
          223.20987654320987
        ],
        [
          744.9382716049383,
          222.46913580246914
        ],
        [
          741.9753086419753,
          23.703703703703706
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          156.3186813186813,
          31.59340659340659
        ],
        [
          154.67032967032966,
          234.06593406593404
        ],
        [
          196.97802197802199,
          234.34065934065933
        ],
        [
          196.7032967032967,
          32.69230769230769
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          209.34065934065933,
          29.395604395604394
        ],
        [
          209.06593406593407,
          231.5934065934066
        ],
        [
          251.37362637362637,
          230.4945054945055
        ],
        [
          252.1978021978022,
          30.21978021978022
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "low",
      "points": [
        [
          263.46153846153845,
          29.12087912087912
        ],
        [
          262.08791208791206,
          229.94505494505495
        ],
        [
          304.94505494505495,
          229.39560439560438
        ],
        [
          304.94505494505495,
          29.395604395604394
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "high",
      "points": [
        [
          318.68131868131866,
          26.923076923076923
        ],
        [
          318.95604395604397,
          229.67032967032966
        ],
        [
          361.53846153846155,
          230.2197802197802
        ],
        [
          360.7142857142857,
          26.923076923076923
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "high",
      "points": [
        [
          375.0,
          28.021978021978022
        ],
        [
          373.90109890109886,
          223.9010989010989
        ],
        [
          416.4835164835165,
          222.25274725274724
        ],
        [
          415.9340659340659,
          28.57142857142857
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          427.4725274725275,
          26.373626373626372
        ],
        [
          429.3956043956044,
          228.02197802197801
        ],
        [
          472.8021978021978,
          227.74725274725273
        ],
        [
          473.90109890109886,
          25.549450549450547
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          485.16483516483515,
          25.274725274725274
        ],
        [
          485.7142857142857,
          226.37362637362637
        ],
        [
          526.9230769230769,
          226.37362637362637
        ],
        [
          527.4725274725274,
          24.45054945054945
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          539.2857142857142,
          25.274725274725274
        ],
        [
          542.032967032967,
          224.45054945054943
        ],
        [
          583.5164835164835,
          225.82417582417582
        ],
        [
          581.8681318681319,
          25.549450549450547
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "low",
      "points": [
        [
          593.1318681318681,
          25.0
        ],
        [
          594.2307692307692,
          225.54945054945054
        ],
        [
          637.0879120879121,
          226.09890109890108
        ],
        [
          635.1648351648352,
          24.45054945054945
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          648.0769230769231,
          23.35164835164835
        ],
        [
          650.8241758241758,
          225.27472527472526
        ],
        [
          691.7582417582418,
          223.07692307692307
        ],
        [
          690.3846153846154,
          24.45054945054945
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          154.35356200527704,
          250.65963060686016
        ],
        [
          150.3957783641161,
          430.60686015831135
        ],
        [
          190.23746701846966,
          429.5514511873351
        ],
        [
          195.51451187335093,
          250.13192612137203
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "low",
      "points": [
        [
          208.17941952506595,
          247.49340369393138
        ],
        [
          205.54089709762533,
          429.5514511873351
        ],
        [
          246.70184696569922,
          428.23218997361477
        ],
        [
          249.6042216358839,
          246.96569920844328
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "low",
      "points": [
        [
          259.6306068601583,
          247.49340369393138
        ],
        [
          258.8390501319261,
          427.70448548812664
        ],
        [
          303.6939313984169,
          426.12137203166225
        ],
        [
          305.5408970976253,
          246.70184696569922
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          318.4696569920844,
          243.7994722955145
        ],
        [
          315.5672823218997,
          422.9551451187335
        ],
        [
          357.5197889182058,
          424.0105540897098
        ],
        [
          360.68601583113457,
          244.85488126649076
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "low",
      "points": [
        [
          372.55936675461743,
          245.3825857519789
        ],
        [
          370.4485488126649,
          425.065963060686
        ],
        [
          413.1926121372032,
          424.0105540897098
        ],
        [
          417.41424802110816,
          245.64643799472296
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          429.5612009237875,
          243.18706697459584
        ],
        [
          427.2517321016166,
          422.40184757505773
        ],
        [
          469.5150115473441,
          423.55658198614316
        ],
        [
          471.3625866050808,
          241.8013856812933
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "high",
      "points": [
        [
          483.9473684210526,
          242.36842105263156
        ],
        [
          483.4210526315789,
          422.89473684210526
        ],
        [
          525.7894736842105,
          423.4210526315789
        ],
        [
          527.1052631578947,
          240.52631578947367
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "low",
      "points": [
        [
          541.0423452768729,
          241.69381107491856
        ],
        [
          538.7622149837133,
          419.21824104234526
        ],
        [
          579.8045602605863,
          419.21824104234526
        ],
        [
          582.4104234527687,
          241.04234527687294
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          594.7882736156351,
          240.39087947882734
        ],
        [
          592.1824104234527,
          416.28664495114003
        ],
        [
          636.4820846905537,
          416.61237785016283
        ],
        [
          636.8078175895765,
          240.06514657980455
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          649.5114006514657,
          239.41368078175893
        ],
        [
          649.5114006514657,
          421.17263843648203
        ],
        [
          691.2052117263843,
          420.84690553745924
        ],
        [
          691.5309446254071,
          239.73941368078172
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          702.6058631921824,
          237.78501628664492
        ],
        [
          701.628664495114,
          421.8241042345276
        ],
        [
          744.9511400651465,
          420.52117263843644
        ],
        [
          745.9283387622149,
          238.76221498371333
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          758.957654723127,
          238.11074918566774
        ],
        [
          757.6547231270357,
          415.63517915309444
        ],
        [
          799.0228013029315,
          415.96091205211724
        ],
        [
          800.6514657980455,
          238.11074918566774
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "high",
      "points": [
        [
          814.9837133550487,
          238.43648208469054
        ],
        [
          813.6807817589576,
          414.657980456026
        ],
        [
          852.442996742671,
          414.98371335504885
        ],
        [
          853.7459283387622,
          237.78501628664492
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "low",
      "points": [
        [
          151.1056511056511,
          445.70024570024566
        ],
        [
          148.64864864864865,
          626.2899262899263
        ],
        [
          190.9090909090909,
          625.7985257985257
        ],
        [
          191.64619164619162,
          445.20884520884516
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "high",
      "points": [
        [
          204.66830466830464,
          444.96314496314494
        ],
        [
          201.22850122850122,
          625.061425061425
        ],
        [
          245.45454545454544,
          625.5528255528255
        ],
        [
          248.15724815724815,
          445.70024570024566
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          258.7223587223587,
          445.94594594594594
        ],
        [
          257.4938574938575,
          624.078624078624
        ],
        [
          303.68550368550365,
          624.078624078624
        ],
        [
          303.4398034398034,
          445.45454545454544
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          315.2334152334152,
          442.26044226044223
        ],
        [
          314.7420147420147,
          623.3415233415233
        ],
        [
          357.4938574938575,
          623.8329238329238
        ],
        [
          358.47665847665843,
          441.76904176904173
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          370.02457002457,
          440.29484029484024
        ],
        [
          369.04176904176904,
          621.6216216216216
        ],
        [
          412.5307125307125,
          622.3587223587223
        ],
        [
          413.022113022113,
          439.3120393120393
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          427.027027027027,
          439.3120393120393
        ],
        [
          424.3243243243243,
          622.8501228501228
        ],
        [
          467.07616707616705,
          622.3587223587223
        ],
        [
          470.02457002457,
          439.5577395577395
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "low",
      "points": [
        [
          482.06388206388203,
          439.066339066339
        ],
        [
          479.60687960687955,
          622.6044226044226
        ],
        [
          524.8157248157248,
          621.8673218673218
        ],
        [
          525.7985257985258,
          438.3292383292383
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          537.3464373464373,
          438.3292383292383
        ],
        [
          536.1179361179361,
          619.4103194103194
        ],
        [
          578.8697788697789,
          620.1474201474201
        ],
        [
          580.09828009828,
          437.5921375921376
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          592.3832923832923,
          436.3636363636363
        ],
        [
          592.1375921375922,
          616.9533169533169
        ],
        [
          634.1523341523341,
          618.6732186732187
        ],
        [
          635.3808353808354,
          437.8378378378378
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "high",
      "points": [
        [
          648.6486486486486,
          440.29484029484024
        ],
        [
          646.6830466830467,
          617.9361179361179
        ],
        [
          689.4348894348894,
          616.9533169533169
        ],
        [
          690.1719901719902,
          439.8034398034398
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "mid",
      "points": [
        [
          702.9484029484029,
          435.8722358722358
        ],
        [
          701.7199017199017,
          618.1818181818181
        ],
        [
          744.9631449631449,
          616.7076167076167
        ],
        [
          745.4545454545454,
          434.6437346437346
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "low",
      "points": [
        [
          757.2481572481572,
          434.8894348894349
        ],
        [
          756.7567567567567,
          616.2162162162161
        ],
        [
          798.5257985257985,
          616.7076167076167
        ],
        [
          797.051597051597,
          435.6265356265356
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    },
    {
      "label": "low",
      "points": [
        [
          812.2850122850123,
          434.8894348894349
        ],
        [
          811.3022113022113,
          616.2162162162161
        ],
        [
          853.0712530712531,
          616.4619164619164
        ],
        [
          852.3341523341522,
          434.6437346437346
        ]
      ],

      "shape_type": "polygon",
      "flags": {}
    }
  ]

raw_data["imagePath"]="d7_10_120_150.jpg"
raw_data["imageData"]=base64_string
raw_data["imageHeight"]=1057
raw_data["imageWidth"]=960

json_data=dumps(raw_data,indent=2) #将字典变成json格式，缩进为2个空格

# 将 json格式的数据保存到文件中
with open(JSON_NAME,'w') as json_file:
    json_file.write(json_data)
