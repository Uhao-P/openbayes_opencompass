from mmengine.config import read_base
with read_base():
    #一、通用能力数据集
    #二、考试题目
    from .groups.mmlu import mmlu_summary_groups
    from .groups.cmmlu import cmmlu_summary_groups
    from .groups.ceval import ceval_summary_groups
    from .groups.GaokaoBench import GaokaoBench_summary_groups
    from .groups.agieval import agieval_summary_groups
    #三、语言能力
    from .groups.flores import flores_summary_groups
    #四、知识能力
    from .groups.tydiqa import tydiqa_summary_groups
summarizer = dict(
    dataset_abbrs=[
        #五、理解能力
        '---五、理解能力---',
        'lcsts',
    ],
    summary_groups=sum(
        [v for k, v in locals().items() if k.endswith('_summary_groups')], []),
)
