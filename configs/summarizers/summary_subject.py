from mmengine.config import read_base
with read_base():
    #二、考试题目
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
        '---二、学科能力---',
        ['ceval', 'naive_average'],
        ['cmmlu', 'naive_average'],
        ['ARC-c', 'accuracy'],     
        ['GaokaoBench', 'weighted_average'],
        'agieval',


        '--详细评分--',

        'mmlu',
        'mmlu-stem',
        'mmlu-social-science',
        'mmlu-humanities',
        'mmlu-other',

        'cmmlu',
        'cmmlu-stem',
        'cmmlu-social-science',
        'cmmlu-humanities',
        'cmmlu-other',
        'cmmlu-china-specific',

        'ceval',
        'ceval-stem',
        'ceval-social-science',
        'ceval-humanities',
        'ceval-other',
        'ceval-hard',
        
        'agieval',
        'agieval-chinese',
        'agieval-english',
        'agieval-gaokao',
        
    ],
    summary_groups=sum(
        [v for k, v in locals().items() if k.endswith('_summary_groups')], []),
)
