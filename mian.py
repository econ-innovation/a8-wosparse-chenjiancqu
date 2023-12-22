import pandas as pd

# 文件路径
file_path = '/Users/chenjian/github/a8-wosparse-chenjiancqu/qje2014_2023.txt'

# 使用Pandas读取文件
try:
    data = pd.read_csv(file_path, sep='\t', encoding='utf-8')
    print(data.head())  # 打印前几行数据以确认读取正确
except FileNotFoundError:
    print("文件不存在")
    

# 第一张表：论文的基本信息
papers_info = data[['UT', 'PY', 'SO', 'SN', 'DI', 'IS', 'VL']].drop_duplicates()

# 第二张表：论文的摘要信息
abstracts = data[['UT', 'AB']].drop_duplicates()

# 第三张表：论文的题目
titles = data[['UT', 'TI']].drop_duplicates()

# 第四张表：论文的作者
authors = data[['UT', 'AU', 'AF']].drop_duplicates()

# 第五张表：论文的作者与单位
authors_affiliations = data[['UT', 'AU', 'AF', 'C1']].drop_duplicates()

# 第六张表：论文的参考文献信息
references = data[['UT', 'CR']].drop_duplicates()

# 根据需要可以将这些 DataFrame 导出为文件或进行进一步处理

# 第一张表：论文的基本信息
papers_info.to_csv('papers_info.csv', index=False)

# 第二张表：论文的摘要信息
abstracts.to_csv('abstracts.csv', index=False)

# 第三张表：论文的题目
titles.to_csv('titles.csv', index=False)

# 第四张表：论文的作者
authors.to_csv('authors.csv', index=False)

# 第五张表：论文的作者与单位
authors_affiliations.to_csv('authors_affiliations.csv', index=False)

# 第六张表：论文的参考文献信息
references.to_csv('references.csv', index=False)
