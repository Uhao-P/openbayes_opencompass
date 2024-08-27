from mmengine.config import read_base
 
with read_base():
    #四、知识能力
    #1.OpenFinData（中文金融领域知识，以实际场景为主）
    from ..datasets.OpenFinData.OpenFinData_gen_46dedb import OpenFinData_datasets
    #2.TriviaqQA（英文阅读理解，冷知识）
    from ..datasets.triviaqa.triviaqa_gen_2121ce import triviaqa_datasets
    #3.NQ（英文更难的阅读理解，维基百科文章）
    from ..datasets.nq.nq_gen_3dcea1 import nq_datasets
    #4.TyDiQA（多语言问答，但是没有中文）
    from ..datasets.tydiqa.tydiqa_gen_978d2a import tydiqa_datasets
datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])