from mmengine.config import read_base
with read_base():
    from .groups.mmlu import mmlu_summary_groups
    from .groups.cmmlu import cmmlu_summary_groups
    from .groups.ceval import ceval_summary_groups
    from .groups.GaokaoBench import GaokaoBench_summary_groups
    from .groups.agieval import agieval_summary_groups
    from .groups.tydiqa import tydiqa_summary_groups
    from .groups.bbh import bbh_summary_groups

    from .groups.FewCLUE import FewCLUE_summary_groups
    from .groups.CLUE import CLUE_summary_groups
    from .groups.SuperGLUE import SuperGLUE_summary_groups

    from .groups.OpenFinData import OpenFinData_summary_groups
    from .groups.longbench import longbench_summary_groups
    
summarizer = dict(
    dataset_abbrs=[
        #一、通用能力
        '--- 一、通用能力 ---',
        'FewCLUE',
        'SuperGLUE',
        'CLUE',
        '--详细信息👇  --',
        '--FewCLUE--',
        'bustm-dev',
        'bustm-test',
        'chid-dev',
        'chid-test',
        'cluewsc-dev',
        'cluewsc-test',
        'csl_dev',
        'csl_test',
        'eprstmt-dev',
        'eprstmt-test',
        'ocnli_fc-dev',
        'ocnli_fc-test',
        'tnews-dev',
        'tnews-test',
        'FewCLUE',
        '---SuperGLUE---',
        'BoolQ',
        'AX_b',
        'AX_g',
        'CB',
        'COPA',
        'MultiRC',
        'ReCoRD',
        'RTE',
        'WiC',
        'WSC',
        'SuperGLUE',
        '---CLUE---',
        'afqmc-dev',
        'C3',
        'cmnli',
        'CMRC_dev',
        'DRCD_dev',
        'ocnli',
        'CLUE',
        
        '---二、学科能力---',
        ['ceval', 'naive_average'],
        ['cmmlu', 'naive_average'],
        ['ARC-c', 'accuracy'],     
        ['GaokaoBench', 'weighted_average'],
        'agieval',
        '--详细信息👇  --',

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
        #四、知识能力
        '---四、知识能力---',
        'triviaqa',
        'nq',
        'OpenFinData',
        'tydiqa',
        'tydiqa-goldp',
        
        #五、理解能力
        '---五、理解能力---',
        'lcsts',
        #六、推理能力
        '---六、推理能力---',
        'bbh',
        'hellaswag',
        'piqa',
        'siqa',
        #七、长文本
        '---五、长文本---',
        'longbench',
        'longbench_zh',
        'longbench_en',
        '--详细信息👇  --',
        '--------- LongBench Single-Document QA ---------', # category
        'longbench_single-document-qa',
        'LongBench_narrativeqa',
        'LongBench_qasper',
        'LongBench_multifieldqa_en',
        'LongBench_multifieldqa_zh',
        '--------- LongBench Multi-Document QA ---------', # category
        'longbench_multi-document-qa',
        'LongBench_hotpotqa',
        'LongBench_2wikimqa',
        'LongBench_musique',
        'LongBench_dureader',
        '--------- LongBench Summarization ---------', # category
        'longbench_summarization',
        'LongBench_gov_report',
        'LongBench_qmsum',
        'LongBench_multi_news',
        'LongBench_vcsum',
        '--------- LongBench Few-shot Learning ---------', # category
        'longbench_few-shot-learning',
        'LongBench_trec',
        'LongBench_triviaqa',
        'LongBench_samsum',
        'LongBench_lsht',
        '--------- LongBench Synthetic Tasks ---------', # category
        'longbench_synthetic-tasks',
        'LongBench_passage_count',
        'LongBench_passage_retrieval_en',
        'LongBench_passage_retrieval_zh',
        '--------- LongBench Code Completion ---------', # category
        'longbench_code-completion',
        'LongBench_lcc',
        'LongBench_repobench-p',
        '---八、数学能力---',
        'math',
        'gsm8k',
        #九、代码能力
        '---九、代码能力---',
        'openai_humaneval',
        'sanitized_mbpp',
        
    ],    

    summary_groups=sum(
        [v for k, v in locals().items() if k.endswith('_summary_groups')], []),
)
