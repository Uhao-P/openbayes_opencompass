from mmengine.config import read_base
 
with read_base():

    
    #八、数学能力
    #1.GSM8K（英语小学数学）
    from ..datasets.gsm8k.gsm8k_gen_1d7fe4 import gsm8k_datasets
    #2.MATH（英文数据竞赛）
    from ..datasets.math.math_gen_265cce import math_datasets
    
datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])