summarizer = dict(
    dataset_abbrs = [
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
    ],
    summary_groups=sum([v for k, v in locals().items() if k.endswith('_summary_groups')], []),
)
