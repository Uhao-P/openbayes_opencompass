from mmengine.config import read_base
 
with read_base():  
    #二、考试题目
    #1.ceval多选，中学、高中、大学和专业，从人文学科到科学和工程学科
    from ..datasets.ceval.ceval_gen_5f30c7 import ceval_datasets
    #2.CMMLU（选择题、需要计算和推理的自然科学，需要知识的人文科学和社会科学,以及需要生活常识的中国驾驶规则等）
    from ..datasets.cmmlu.cmmlu_gen_c13365 import cmmlu_datasets
    #3.AGIEval（选择题和完形填空、高标准的入学和资格考试，比如普通大学入学考试中国高考和美国SAT、法学院入学考试、数学竞赛、律师资格考试和国家公务员考试）
    from ..datasets.agieval.agieval_gen_617738 import agieval_datasets
    #4.ARC-c（选择题为主，从三年级到九年级的科学考试）
    from ..datasets.ARC_c.ARC_c_gen_1e0de5 import ARC_c_datasets
    #5.GAOKAO-Bench（高考题，2010-2023年高考题）
    from ..datasets.GaokaoBench.GaokaoBench_gen_5cfe9e import GaokaoBench_datasets
datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])