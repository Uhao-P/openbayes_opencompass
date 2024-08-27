from mmengine.config import read_base
 
with read_base():

    #九、代码能力
    #1.HumanEval（简单软件面试题、算法和简单数学）
    from ..datasets.humaneval.humaneval_gen_8e312c import humaneval_datasets
    #2.MBPP（入门级程序员python）
    from ..datasets.mbpp.sanitized_mbpp_gen_830460 import sanitized_mbpp_datasets
 
 
datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])