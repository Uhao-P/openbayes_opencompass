from opencompass.models import CarbonAI
from mmengine.config import Config, DictAction

api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
    reserved_roles=[dict(role='SYSTEM', api_role='SYSTEM')],
)

models = [
    dict(
        #当前测试模型的名称:用于结果展示
        abbr='Meta-Llama-3-8B-Instruct',
        type=CarbonAI,
        #修改1,对外API之前测试会有部分请求失败
        #❌0.0.0.0:8080  ✅localhost 或127.0.0.1      
        openai_api_base='http://localhost:8080/v1/chat/completions', # 服务地址
        
        #path:在之前采用tiktoken库(更快)计算len(tokens),只能用gpt-3.5固定参数,已改为了直接使用tokenier,删掉了api中关于gpt-3.5的代码,见:opencompass/opencompass/models/openai_api.py

        
        path='/input0/', # 请求服务时的 model name
        #2
        rpm_verbose=False, # 是否打印请求速率
        meta_template=api_meta_template, # 服务请求模板
        query_per_second=0.5, # 服务请求速率
        batch_size=256, # 批处理大小
        retry=10, # 重试次数
        #3
        max_out_len=8192, # 最大输出长度
        temperature=0.2, # 生成温度
        max_model_len=32768,#上下文长度
        repetition_penalty=1.2
    )
]