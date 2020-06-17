def get_course_sample_data():
    ret = {1: {'lesson': [{'name': '并发理论', 'index': 1},
                          {'name': '算法设计与分析', 'index': 2},
                          {'name': '计算机体系结构', 'index': 3},
                          {'name': '软件工程', 'index': 4}]},
           2: {'lesson': [{'name': '华语电影评析', 'index': 1},
                          {'name': '概率论与数理统计', 'index': 2},
                          {'name': '信息安全原理', 'index': 3},
                          {'name': '操作系统', 'index': 4},
                          {'name': '计算机网络', 'index': 5},
                          {'name': '自然语言处理', 'index': 6},
                          {'name': '学术英语（科学技术）', 'index': 7}]},
           3: {'lesson': [
               {'name': '代数结构与数理逻辑', 'index': 1},
               {'name': '数据库引论', 'index': 2},
               {'name': '模式识别与机器学习', 'index': 3},
               {'name': '计算机系统基础（下）', 'index': 4},
               {'name': '数据挖掘技术', 'index': 5},
               {'name': '英语论说文写作', 'index': 6},
               {'name': '排球', 'index': 7},
               {'name': '《理想国》导读', 'index': 8},
               {'name': '应用伦理学', 'index': 9},
               {'name': '形势与政策IV', 'index': 10}]},
           4: {'lesson': [{'name': '概率论与数理统计', 'index': 1},
                          {'name': '微观经济学', 'index': 2},
                          {'name': '会计学', 'index': 3},
                          {'name': '数字逻辑与部件设计', 'index': 4},
                          {'name': '数字逻辑与部件设计实验', 'index': 5},
                          {'name': '数据结构', 'index': 6},
                          {'name': '计算机系统基础（上）', 'index': 7},
                          {'name': '集合与图论', 'index': 8},
                          {'name': '排球', 'index': 9},
                          {'name': '形势与政策III', 'index': 10}, {
                              'name': '毛泽东思想和中国特色社会主义理论体系概论A',
                              'index': 11}, {
                              'name': '毛泽东思想和中国特色社会主义理论体系概论B',
                              'index': 12}]},
           5: {'lesson': [{'name': '面向对象程序设计', 'index': 1},
                          {'name': '英语视听', 'index': 2},
                          {'name': '模拟电子学基础', 'index': 3},
                          {'name': '数学分析BII', 'index': 4},
                          {'name': '军事理论', 'index': 5},
                          {'name': '网球', 'index': 6},
                          {'name': '大学物理B(下) ', 'index': 7},
                          {'name': '基础物理实验', 'index': 8},
                          {'name': '中国近现代史纲要', 'index': 9},
                          {'name': '形势与政策II', 'index': 10}]},
           }
    return ret

def get_mainpage_sample_data():
    return {}

def get_document_sample_data():
    return {'name': '并发理论', 'docs': [{'title': 'References', 'expand': True, 'urls': '', 'children': [{'title': 'tm_tutorial_pact2006.zip', 'expand': False, 'urls': 'https://elearning.fudan.edu.cn/files/555529/download?download_frd=1', 'children': []}]}, {'title': 'Sample Code', 'expand': True, 'urls': '', 'children': [{'title': 'enwiki-latest-pages-articles.xml.zip', 'expand': False, 'urls': 'https://elearning.fudan.edu.cn/files/244234/download?download_frd=1', 'children': []}, {'title': 'pb7con-code.zip', 'expand': False, 'urls': 'https://elearning.fudan.edu.cn/files/243583/download?download_frd=1', 'children': []}]}, {'title': 'Concurrency-Theory and Practice.zip', 'expand': False, 'urls': 'https://elearning.fudan.edu.cn/files/692963/download?download_frd=1', 'children': []}, {'title': 'On Concurrency 01 - Concurrency, Issues and the Lock Mechanism.zip', 'expand': False, 'urls': 'https://elearning.fudan.edu.cn/files/367949/download?download_frd=1', 'children': []}, {'title': 'On Concurrency 02 - The Computer Science of Concurrency-The Early Years.zip', 'expand': False, 'urls': 'https://elearning.fudan.edu.cn/files/430029/download?download_frd=1', 'children': []}, {'title': 'On Concurrency 03 - Functional Programming and the Clojure Approach.zip', 'expand': False, 'urls': 'https://elearning.fudan.edu.cn/files/515738/download?download_frd=1', 'children': []}, {'title': 'On Concurrency 04 - Unlocking Concurrency.zip', 'expand': False, 'urls': 'https://elearning.fudan.edu.cn/files/551918/download?download_frd=1', 'children': []}, {'title': 'On Concurrency 05 - The Actor Model.zip', 'expand': False, 'urls': 'https://elearning.fudan.edu.cn/files/651274/download?download_frd=1', 'children': []}, {'title': 'On Concurrency 06 - Elements of Interaction.zip', 'expand': False, 'urls': 'https://elearning.fudan.edu.cn/files/642133/download?download_frd=1', 'children': []}, {'title': 'On Concurrency 07 - Communicating Sequential Processes.zip', 'expand': False, 'urls': 'https://elearning.fudan.edu.cn/files/678647/download?download_frd=1', 'children': []}, {'title': 'On Concurrency 08 - Petri Nets and Colored Petri Net.zip', 'expand': False, 'urls': 'https://elearning.fudan.edu.cn/files/764040/download?download_frd=1', 'children': []}, {'title': 'On Concurrency 11 - Data Parallelism with OpenCL.html', 'expand': False, 'urls': 'https://elearning.fudan.edu.cn/files/230497/download?download_frd=1', 'children': []}]}

def get_homework_sample_data():
    return {}