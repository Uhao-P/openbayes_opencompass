from mmengine.config import read_base
 
with read_base():
    #一、通用能力数据集
    #1.FewCLUE（中文，对话短文本匹配、成语阅读理解、代词消歧、摘要判断关键词判别）
    from ..datasets.FewCLUE_bustm.FewCLUE_bustm_gen_634f41 import bustm_datasets
    from ..datasets.FewCLUE_chid.FewCLUE_chid_gen_0a29a2 import chid_datasets
    from ..datasets.FewCLUE_cluewsc.FewCLUE_cluewsc_gen_c68933 import cluewsc_datasets
    from ..datasets.FewCLUE_csl.FewCLUE_csl_gen_28b223 import csl_datasets
    from ..datasets.FewCLUE_eprstmt.FewCLUE_eprstmt_gen_740ea0 import eprstmt_datasets
    from ..datasets.FewCLUE_ocnli_fc.FewCLUE_ocnli_fc_gen_f97a97 import ocnli_fc_datasets
    from ..datasets.FewCLUE_tnews.FewCLUE_tnews_gen_b90e4a import tnews_datasets
    #2.superGlUE（问题是否为真、假设是否符合前提、选择哪个答案更符合问题、多句阅读理解、结合文本中的事实和常识推理来回答、文本蕴涵识别、词义消歧、共指消解、广覆盖诊断、Winogender诊断）
    from ..datasets.SuperGLUE_BoolQ.SuperGLUE_BoolQ_gen_883d50 import BoolQ_datasets
    from ..datasets.SuperGLUE_AX_b.SuperGLUE_AX_b_gen_4dfefa import AX_b_datasets
    from ..datasets.SuperGLUE_AX_g.SuperGLUE_AX_g_gen_68aac7 import AX_g_datasets
    from ..datasets.SuperGLUE_CB.SuperGLUE_CB_gen_854c6c import CB_datasets
    from ..datasets.SuperGLUE_COPA.SuperGLUE_COPA_gen_91ca53 import COPA_datasets
    from ..datasets.SuperGLUE_MultiRC.SuperGLUE_MultiRC_gen_27071f import MultiRC_datasets
    from ..datasets.SuperGLUE_ReCoRD.SuperGLUE_ReCoRD_gen_30dea0 import ReCoRD_datasets
    from ..datasets.SuperGLUE_RTE.SuperGLUE_RTE_gen_68aac7 import RTE_datasets
    from ..datasets.SuperGLUE_WiC.SuperGLUE_WiC_gen_d06864 import WiC_datasets
    from ..datasets.SuperGLUE_WSC.SuperGLUE_WSC_gen_fe4bf3 import WSC_datasets
    #3.CLUE（中文语言理解，蚂蚁金融科技语义相似度、中文多选阅读理解数据集、自然语言推理中文版、繁体、简体抽取式阅读理解）
    from ..datasets.CLUE_afqmc.CLUE_afqmc_gen_901306 import afqmc_datasets
    from ..datasets.CLUE_C3.CLUE_C3_gen_8c358f import C3_datasets
    from ..datasets.CLUE_cmnli.CLUE_cmnli_gen_1abf97 import cmnli_datasets
    from ..datasets.CLUE_CMRC.CLUE_CMRC_gen_1bd3c8 import CMRC_datasets
    from ..datasets.CLUE_DRCD.CLUE_DRCD_gen_1bd3c8 import DRCD_datasets
    from ..datasets.CLUE_ocnli.CLUE_ocnli_gen_c4cb6c import ocnli_datasets
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
    #四、知识能力
    #1.OpenFinData（中文金融领域知识，以实际场景为主）
    from ..datasets.OpenFinData.OpenFinData_gen_46dedb import OpenFinData_datasets
    #2.TriviaqQA（英文阅读理解，冷知识）
    from ..datasets.triviaqa.triviaqa_gen_2121ce import triviaqa_datasets
    #3.NQ（英文更难的阅读理解，维基百科文章）
    from ..datasets.nq.nq_gen_3dcea1 import nq_datasets
    #4.TyDiQA（多语言问答，但是没有中文）
    from ..datasets.tydiqa.tydiqa_gen_978d2a import tydiqa_datasets
     #五、理解能力
    #LCSTS（中文短文本摘要微博 ）
    from ..datasets.lcsts.lcsts_gen_8ee1fe import lcsts_datasets
    #六、推理能力（全英）
    #BBH（英文文本理解、推理、逻辑推理、数学推理和常识推理）
    from ..datasets.bbh.bbh_gen_2879b0 import bbh_datasets
    #HellaSwag (英文常识性自然语言推理)
    from ..datasets.hellaswag.hellaswag_gen_6faab5 import hellaswag_datasets
    #siqa（英文社会常识）
    from ..datasets.piqa.piqa_gen_1194eb import piqa_datasets
    #piqa（英文物理常识）；
    from ..datasets.siqa.siqa_gen_e78df3 import siqa_datasets
 
    #七、长文本
    #长文本的：LongBench（中英文、多任务、长文本5k-15k）
    from ..datasets.longbench.longbench2wikimqa.longbench_2wikimqa_gen import LongBench_2wikimqa_datasets
    from ..datasets.longbench.longbenchhotpotqa.longbench_hotpotqa_gen import LongBench_hotpotqa_datasets
    from ..datasets.longbench.longbenchmusique.longbench_musique_gen import LongBench_musique_datasets
    from ..datasets.longbench.longbenchmultifieldqa_en.longbench_multifieldqa_en_gen import LongBench_multifieldqa_en_datasets
    from ..datasets.longbench.longbenchmultifieldqa_zh.longbench_multifieldqa_zh_gen import LongBench_multifieldqa_zh_datasets
    from ..datasets.longbench.longbenchnarrativeqa.longbench_narrativeqa_gen import LongBench_narrativeqa_datasets
    from ..datasets.longbench.longbenchqasper.longbench_qasper_gen import LongBench_qasper_datasets
    from ..datasets.longbench.longbenchtriviaqa.longbench_triviaqa_gen import LongBench_triviaqa_datasets
    from ..datasets.longbench.longbenchgov_report.longbench_gov_report_gen import LongBench_gov_report_datasets
    from ..datasets.longbench.longbenchqmsum.longbench_qmsum_gen import LongBench_qmsum_datasets
    from ..datasets.longbench.longbenchvcsum.longbench_vcsum_gen import LongBench_vcsum_datasets
    from ..datasets.longbench.longbenchdureader.longbench_dureader_gen import LongBench_dureader_datasets
    from ..datasets.longbench.longbenchlcc.longbench_lcc_gen import LongBench_lcc_datasets
    from ..datasets.longbench.longbenchrepobench.longbench_repobench_gen import LongBench_repobench_datasets
    from ..datasets.longbench.longbenchpassage_retrieval_en.longbench_passage_retrieval_en_gen import LongBench_passage_retrieval_en_datasets
    from ..datasets.longbench.longbenchpassage_retrieval_zh.longbench_passage_retrieval_zh_gen import LongBench_passage_retrieval_zh_datasets
    from ..datasets.longbench.longbenchpassage_count.longbench_passage_count_gen import LongBench_passage_count_datasets
    from ..datasets.longbench.longbenchtrec.longbench_trec_gen import LongBench_trec_datasets
    from ..datasets.longbench.longbenchlsht.longbench_lsht_gen import LongBench_lsht_datasets
    from ..datasets.longbench.longbenchmulti_news.longbench_multi_news_gen import LongBench_multi_news_datasets
    from ..datasets.longbench.longbenchsamsum.longbench_samsum_gen import LongBench_samsum_datasets
    #八、数学能力
    #1.GSM8K（英语小学数学）
    from ..datasets.gsm8k.gsm8k_gen_1d7fe4 import gsm8k_datasets
    #2.MATH（英文数据竞赛）
    from ..datasets.math.math_gen_265cce import math_datasets
    #九、代码能力
    #1.HumanEval（简单软件面试题、算法和简单数学）
    from ..datasets.humaneval.humaneval_gen_8e312c import humaneval_datasets
    #2.MBPP（入门级程序员python）
    from ..datasets.mbpp.mbpp_gen_830460 import mbpp_datasets

    
    
    
    
    
    
    
    
datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])