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


datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])