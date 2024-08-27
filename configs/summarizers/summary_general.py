from mmengine.config import read_base
with read_base():

    from .groups.mmlu import mmlu_summary_groups
    from .groups.cmmlu import cmmlu_summary_groups
    from .groups.ceval import ceval_summary_groups
    from .groups.GaokaoBench import GaokaoBench_summary_groups
    from .groups.agieval import agieval_summary_groups
    from .groups.tydiqa import tydiqa_summary_groups
    from .groups.general import FewCLUE_summary_groups,SuperGLUE_summary_groups,CLUE_summary_groups
summarizer = dict(
    dataset_abbrs=[
        #一、通用能力
        '--- 一、通用能力 ---',
        'FewCLUE',
        'SuperGlUE',
        'CLUE',
        
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
        'SuperGlUE',
        '---CLUE---',
        'afqmc-dev',
        'C3',
        'cmnli',
        'CMRC_dev',
        'DRCD_dev',
        'ocnli',
        'CLUE',
        
    ],
    summary_groups=sum(
        [v for k, v in locals().items() if k.endswith('_summary_groups')], []),
)
