from mmengine.config import read_base
 
with read_base():
    #五、理解能力
    #LCSTS（中文短文本摘要微博 ）
    from ..datasets.lcsts.lcsts_gen_8ee1fe import lcsts_datasets
    
    
datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])