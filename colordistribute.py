import matplotlib, numpy

# Wudio
# 20210913
# 用于计算给定数据在固定长度的区间内，所有元素求和结果最大的区间所在位置与最大值
# 此处用于计算图像中像素的色相分布，寻找图像内的颜色特征

# data
ORG1 = [
    3222, 2181, 1467, 1299, 1124, 1040, 1015, 879, 887, 829, 840, 746, 849,
    773, 755, 861, 804, 794, 845, 803, 888, 910, 887, 876, 930, 874, 830, 874,
    911, 776, 901, 831, 907, 879, 915, 850, 930, 849, 972, 864, 935, 817, 874,
    834, 890, 953, 903, 855, 926, 896, 859, 924, 889, 940, 927, 932, 928, 1009,
    941, 731, 906, 650, 593, 615, 635, 521, 529, 536, 517, 524, 427, 323, 483,
    331, 341, 345, 279, 289, 282, 266, 258, 219, 293, 274, 171, 219, 232, 219,
    192, 157, 181, 195, 183, 177, 161, 147, 179, 156, 136, 147, 147, 129, 137,
    131, 106, 114, 128, 113, 130, 127, 105, 98, 141, 92, 111, 96, 105, 89, 94,
    76, 292, 96, 104, 82, 103, 88, 73, 83, 77, 83, 71, 88, 101, 85, 74, 76, 94,
    76, 85, 95, 76, 82, 84, 74, 84, 81, 73, 78, 98, 89, 116, 98, 109, 99, 101,
    103, 98, 89, 106, 105, 65, 98, 66, 69, 59, 62, 43, 47, 54, 45, 62, 34, 43,
    44, 50, 52, 52, 41, 55, 31, 15, 6, 5, 8, 5, 3, 3, 0, 0, 0, 2, 0, 1, 0, 0,
    0, 2, 0, 0, 0, 0, 1, 2, 0, 0, 1, 2, 2, 0, 0, 6, 0, 6, 0, 2, 2, 1, 5, 0, 2,
    5, 1, 2, 0, 1, 3, 0, 0, 5, 1, 4, 1, 3, 3, 3, 1, 2, 0, 0, 0, 39, 0, 0, 2, 1,
    2, 0, 3, 5, 1, 5, 0, 5, 2, 0, 4, 5, 1, 0, 0, 9, 0, 1, 2, 4, 5, 0, 0, 0, 0,
    3, 1, 2, 1, 2, 0, 2, 0, 1, 0, 3, 0, 6, 0, 0, 2, 0, 0, 1, 0, 3, 2, 2, 0, 2,
    2, 1, 2, 0, 0, 5, 0, 0, 1, 1, 1, 1, 0, 0, 0, 4, 0, 3, 2, 0, 0, 2, 1, 2, 0,
    2, 0, 1, 0, 1, 1, 2, 5, 0, 0, 8, 0, 2, 1, 0, 0, 1, 0, 2, 0, 13, 2, 2, 0, 0,
    9, 0, 0, 3, 0, 0, 2, 0, 4, 4, 0, 0, 13, 76, 406
]

ORG2 = [
    4, 3, 5, 11, 6, 10, 5, 11, 11, 8, 7, 13, 7, 14, 21, 24, 19, 18, 15, 21, 22,
    24, 32, 15, 28, 29, 29, 29, 36, 36, 32, 49, 43, 40, 51, 49, 59, 67, 50, 64,
    98, 91, 92, 108, 111, 120, 96, 107, 122, 101, 124, 147, 140, 152, 166, 185,
    178, 193, 196, 168, 256, 219, 281, 257, 311, 254, 262, 255, 311, 346, 254,
    231, 361, 265, 254, 268, 269, 270, 245, 281, 295, 258, 311, 265, 260, 285,
    279, 305, 269, 217, 266, 240, 270, 260, 220, 227, 270, 269, 262, 248, 283,
    244, 247, 213, 252, 224, 218, 243, 257, 206, 221, 214, 277, 162, 246, 231,
    185, 191, 178, 173, 281, 230, 240, 188, 220, 255, 266, 274, 224, 254, 252,
    348, 337, 274, 294, 338, 402, 355, 393, 385, 377, 424, 373, 385, 440, 438,
    452, 405, 581, 413, 492, 472, 584, 514, 483, 641, 552, 578, 676, 702, 548,
    917, 792, 875, 742, 942, 975, 901, 1078, 918, 1208, 972, 1091, 1152, 1146,
    1091, 1190, 1147, 1328, 1158, 1774, 1334, 1284, 1174, 1206, 1070, 962, 866,
    952, 873, 775, 690, 643, 626, 559, 543, 441, 481, 409, 360, 424, 438, 411,
    359, 366, 353, 310, 271, 248, 144, 144, 140, 126, 100, 106, 102, 91, 74,
    75, 60, 48, 54, 51, 44, 31, 31, 19, 20, 14, 9, 8, 8, 4, 5, 0, 5, 3, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

ORG3 = [
    1, 0, 0, 2, 0, 0, 0, 3, 1, 1, 5, 4, 10, 7, 7, 3, 3, 5, 6, 4, 13, 9, 11, 10,
    17, 9, 13, 17, 13, 17, 16, 15, 19, 16, 21, 25, 29, 31, 33, 24, 36, 42, 48,
    30, 66, 57, 57, 63, 77, 49, 82, 82, 92, 135, 162, 183, 241, 275, 282, 276,
    321, 283, 244, 297, 328, 276, 303, 290, 299, 345, 278, 245, 361, 326, 272,
    349, 259, 327, 280, 298, 310, 319, 365, 316, 339, 335, 335, 267, 308, 282,
    286, 351, 320, 303, 303, 308, 372, 346, 313, 335, 386, 343, 350, 283, 347,
    317, 342, 311, 382, 319, 306, 292, 371, 249, 358, 315, 267, 263, 292, 293,
    404, 336, 310, 302, 377, 378, 387, 353, 382, 337, 425, 515, 531, 492, 430,
    494, 540, 473, 539, 526, 593, 619, 519, 535, 667, 672, 624, 640, 828, 610,
    772, 721, 959, 806, 729, 1063, 776, 883, 936, 941, 716, 1100, 1016, 1144,
    923, 1134, 1163, 1063, 1328, 1113, 1455, 1110, 1198, 1226, 1201, 1144,
    1224, 1175, 1197, 1004, 1602, 1093, 923, 803, 744, 598, 585, 459, 505, 401,
    389, 328, 324, 264, 222, 224, 191, 163, 133, 140, 122, 130, 94, 109, 64,
    66, 63, 47, 34, 39, 47, 30, 24, 16, 26, 19, 18, 18, 12, 11, 13, 7, 8, 3, 8,
    7, 4, 3, 4, 3, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

ORG4 = [
    35, 0, 2, 1, 1, 10, 12, 9, 20, 11, 16, 15, 21, 20, 15, 16, 19, 24, 25, 25,
    28, 20, 20, 29, 21, 15, 23, 21, 36, 20, 26, 25, 23, 20, 28, 28, 25, 27, 30,
    37, 32, 45, 36, 34, 34, 40, 49, 36, 56, 43, 49, 62, 64, 57, 68, 72, 63, 75,
    66, 60, 85, 51, 57, 59, 66, 69, 62, 54, 68, 83, 55, 48, 66, 51, 48, 65, 51,
    52, 52, 46, 64, 56, 40, 48, 37, 33, 38, 36, 43, 37, 29, 41, 42, 33, 35, 39,
    45, 34, 26, 34, 30, 33, 36, 32, 30, 22, 35, 35, 32, 33, 43, 35, 21, 32, 33,
    27, 26, 26, 26, 24, 94, 35, 32, 29, 33, 47, 39, 41, 28, 26, 36, 31, 48, 41,
    44, 53, 46, 36, 47, 53, 40, 49, 46, 43, 49, 53, 61, 54, 68, 44, 71, 62, 72,
    63, 68, 73, 77, 88, 79, 87, 74, 114, 89, 111, 104, 104, 131, 116, 152, 123,
    152, 141, 162, 176, 161, 182, 177, 177, 195, 166, 337, 266, 291, 280, 262,
    287, 309, 282, 280, 296, 307, 314, 320, 302, 267, 329, 303, 340, 294, 345,
    358, 332, 386, 362, 361, 377, 381, 387, 387, 384, 468, 460, 493, 445, 483,
    498, 580, 512, 536, 588, 593, 575, 693, 629, 642, 700, 693, 757, 797, 761,
    763, 920, 954, 994, 1023, 1175, 1448, 2160, 4036, 8632, 21957, 3152, 1008,
    379, 146, 57, 28, 13, 7, 6, 8, 1, 2, 3, 1, 0, 3, 2, 1, 0, 0, 0, 0, 2, 3, 4,
    4, 0, 1, 0, 0, 2, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0,
    0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
    1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

# 区间大小
size = 100

# 可滑动距离
dis = len(ORG1) - size

print(len(ORG1))

# 存储每个区间的和
sumlist = []

for tt in range(0, dis):  # 所有需求和情况循环
    sum = 0
    for t in range(tt, tt + size):  # 单一区间求和循环
        data = ORG4[t]
        sum += data
        # print(t)
    # print(sum)
    sumlist.append(sum)

print(sumlist)
print(len(sumlist))

print('max = %s' % max(sumlist))
print('pos = %s' % (sumlist.index(max(sumlist))+1))