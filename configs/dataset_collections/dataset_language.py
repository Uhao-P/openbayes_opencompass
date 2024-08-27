from mmengine.config import read_base
 
with read_base():

        #三、语言能力
    #1.Flores101（英语和小语种之间互相翻译）
    from ..datasets.flores.flores_gen_806ede import flores_datasets
#     #2.其他包含在CLUE中

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])