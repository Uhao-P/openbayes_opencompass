from mmengine.config import read_base
 
with read_base():
    #六、推理能力（全英）
    #BBH（英文文本理解、推理、逻辑推理、数学推理和常识推理）
    from ..datasets.bbh.bbh_gen_2879b0 import bbh_datasets
    #HellaSwag (英文常识性自然语言推理)
    from ..datasets.hellaswag.hellaswag_gen_6faab5 import hellaswag_datasets
    #siqa（英文社会常识）
    from ..datasets.piqa.piqa_gen_1194eb import piqa_datasets
    #piqa（英文物理常识）；
    from ..datasets.siqa.siqa_gen_e78df3 import siqa_datasets
 
 
datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])