from mmengine.config import read_base
from opencompass.partitioners import SizePartitioner, NaivePartitioner
from opencompass.runners import LocalRunner
from opencompass.tasks import OpenICLInferTask, OpenICLEvalTask

with read_base():
    from .dataset_collections.dataset_language import datasets
    from .models.carbon.carbon import models
    from .summarizers.summary_language import summarizer
work_dir = 'outputs/result/result_language'

#设置推理和评分时的并行数，在进行推理或者评分时会按照模型-小数据集(ceval中的)进行任务绑定，
infer = dict(
    partitioner=dict(type=SizePartitioner, max_task_size=5000),
    runner=dict(
        type=LocalRunner,
        max_num_workers=16,
        task=dict(type=OpenICLInferTask)),
)
#
eval = dict(
    partitioner=dict(type=NaivePartitioner),
    runner=dict(
        type=LocalRunner,
        task=dict(type=OpenICLEvalTask),
        max_num_workers=8,
    )
)
   
    
    