from src.semantic import Analysis

if __name__ == '__main__':
    text = '上海的天气怎么样'

    slu = Analysis(text)

    data = slu.analysis()  # 解析
    print(data)  # 总的结果

    print('--------------------------')

    print(slu.cws)  # 分词

    print(slu.pos)  # 词性标注

    print(slu.ner)  # 命名实体识别

    print(slu.domain)  # 领域分类

    print(slu.intent)  # 意图识别

    print(slu.slot)  # 槽填充

# 解析结果{
#     "input": "厦门明天会不会下雨",
#     "semantics": [
#         {
#             "score": "0.8",
#             "domain": "天气",
#             "intent": "雨",
#             "slot": [
#                 [
#                     "城市",
#                     "厦门"
#                 ],
#                 [
#                     "日期",
#                     "明天"
#                 ]
#             ]
#         }
#     ],
#     "词法分析": {
#         "词性标注": [
#             "地名",
#             "时间词",
#             "动词",
#             "动词",
#             "动词"
#         ],
#         "实体识别": [
#             "B-地名",
#             "O",
#             "O",
#             "O",
#             "O"
#         ],
#         "中文分词": [
#             "厦门",
#             "明天",
#             "会",
#             "不会",
#             "下雨"
#         ]
#     }
# }
#