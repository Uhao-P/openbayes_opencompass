import json
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from typing import Dict, List, Optional, Union
 
import jieba
import requests
 
from opencompass.registry import MODELS
from opencompass.utils.prompt import PromptList
 
from .base_api import BaseAPIModel
 
PromptType = Union[PromptList, str]
 
 
@MODELS.register_module()
class CarbonAI(BaseAPIModel):
    is_api: bool = True
    #采样参数
    def __init__(self,
                 path: str,
                 max_model_len: int = 32768,
                 query_per_second: int = 1,
                 rpm_verbose: bool = False,
                 retry: int = 10,
                 key: Union[str, List[str]] = 'ENV',
                 org: Optional[Union[str, List[str]]] = None,
                 meta_template: Optional[Dict] = None,
                 openai_api_base: str = 'None',
                 mode: str = 'none',
                 temperature: Optional[float] = None,
                 #新增
                 max_out_len: int = 8192,
                 repetition_penalty: float = 1.2,
                
                ):
 
        super().__init__(path=path,
                         # max_seq_len=max_seq_len,
                         meta_template=meta_template,
                         query_per_second=query_per_second,
                         rpm_verbose=rpm_verbose,
                         retry=retry,
                        )
        import tiktoken
        self.tiktoken = tiktoken
        self.temperature = temperature
        
        assert mode in ['none', 'front', 'mid', 'rear']
        self.mode = mode
 
        if isinstance(key, str):
            self.keys = [os.getenv('OPENAI_API_KEY') if key == 'ENV' else key]
        else:
            self.keys = key
 
        # record invalid keys and skip them when requesting API
        # - keys have insufficient_quota
        self.invalid_keys = set()
 
        self.key_ctr = 0
        if isinstance(org, str):
            self.orgs = [org]
        else:
            self.orgs = org
        self.org_ctr = 0
        self.url = openai_api_base
        self.path = path
        
        self.max_out_len = max_out_len
        self.max_model_len = max_model_len
        self.repetition_penalty=repetition_penalty
 
 
    def generate(self,
                 inputs: List[PromptType],
                 max_out_len: int = 512,
                 temperature: float = 0.7,
                 **kwargs) -> List[str]:
        """Generate results given a list of inputs.
 
        Args:
            inputs (List[PromptType]): A list of strings or PromptDicts.
                The PromptDict should be organized in OpenCompass'
                API format.
            max_out_len (int): The maximum length of the output.
            temperature (float): What sampling temperature to use,
                between 0 and 2. Higher values like 0.8 will make the output
                more random, while lower values like 0.2 will make it more
                focused and deterministic. Defaults to 0.7.
 
        Returns:
            List[str]: A list of generated strings.
        """
        if self.temperature is not None:
            temperature = self.temperature
 
        with ThreadPoolExecutor() as executor:
            results = list(
                executor.map(self._generate, inputs,
                             [max_out_len] * len(inputs),
                             [temperature] * len(inputs)))
        return results
 
    def _generate(self, input: PromptType, max_out_len: int,
                  temperature: float) -> str:
        """Generate results given a list of inputs.
 
        Args:
            inputs (PromptType): A string or PromptDict.
                The PromptDict should be organized in OpenCompass'
                API format.
            max_out_len (int): The maximum length of the output.
            temperature (float): What sampling temperature to use,
                between 0 and 2. Higher values like 0.8 will make the output
                more random, while lower values like 0.2 will make it more
                focused and deterministic.
 
        Returns:
            str: The generated string.
        """
        assert isinstance(input, (str, PromptList))
        
        if self.temperature is not None:
            temperature = self.temperature
        if self.repetition_penalty is not None:
            repetition_penalty = self.repetition_penalty
  
        #message处理
        if isinstance(input, str):
            messages = [{'role': 'user', 'content': input}]
        else:
            messages = []
            for item in input:
                msg = {'content': item['prompt']}
                if item['role'] == 'HUMAN':
                    msg['role'] = 'user'
                elif item['role'] == 'BOT':
                    msg['role'] = 'assistant'
                elif item['role'] == 'SYSTEM':
                    msg['role'] = 'system'
                messages.append(msg)
 
        #看context是否传入
        context_window = self.max_model_len
        #最大输出
        # Hold out 100 tokens due to potential errors in tiktoken calculation
        max_out_len = min(
            max_out_len,
            context_window - self.get_token_len(str(input)) - 100)
        if max_out_len <= 0:
            return ''
 
        
        #推理,设置重试次数
        max_num_retries = 0
        print(self.repetition_penalty)
        while max_num_retries < self.retry:
            self.wait()
            with Lock():
                if len(self.invalid_keys) == len(self.keys):
                    raise RuntimeError('All keys have insufficient quota.')
                # find the next valid key
                while True:
                    self.key_ctr += 1
                    if self.key_ctr == len(self.keys):
                        self.key_ctr = 0
                    if self.keys[self.key_ctr] not in self.invalid_keys:
                        break
                key = self.keys[self.key_ctr]
            header = {'Authorization': f'Bearer YOUR_API_KEY'}
            if self.orgs:
                with Lock():
                    self.org_ctr += 1
                    if self.org_ctr == len(self.orgs):
                        self.org_ctr = 0
                header['OpenAI-Organization'] = self.orgs[self.org_ctr]
 
            try:
                print('*'*10,temperature)
                data = dict(
                    model=self.path,
                    messages=messages,
                    max_tokens=max_out_len,
                    #调整采样参数
                    repetition_penalty = repetition_penalty,
                    temperature = temperature
 
 
                    
                )
                raw_response = requests.post(self.url,
                                             headers=header,
                                             data=json.dumps(data))
            except requests.ConnectionError:
                self.logger.error('Got connection error, retrying...')
                continue
            try:
                response = raw_response.json()
            except requests.JSONDecodeError:
                self.logger.error('JsonDecode error, got',
                                  str(raw_response.content))
                continue
            try:
                return response['choices'][0]['message']['content'].strip()
            except KeyError:
                if 'error' in response:
                    if response['error']['code'] == 'rate_limit_exceeded':
                        time.sleep(1)
                        continue
                    elif response['error']['code'] == 'insufficient_quota':
                        self.invalid_keys.add(key)
                        self.logger.warn(f'insufficient_quota key: {key}')
                        continue
 
                    self.logger.error('Find error message in response: ',
                                      str(response['error']))
            max_num_retries += 1
 
        raise RuntimeError('Calling OpenAI failed after retrying for '
                           f'{max_num_retries} times. Check the logs for '
                           'details.')
 
    def get_token_len(self, prompt: str) -> int:
        """Get lengths of the tokenized string. Only English and Chinese
        characters are counted for now. Users are encouraged to override this
        method if more accurate length is needed.
 
        Args:
            prompt (str): Input string.
 
        Returns:
            int: Length of the input tokens
        """
        '''
        #原方法:
        enc = self.tiktoken.get_encoding("gpt-3.5-turbo")
        tokenized_length = len(enc.encode(prompt))  
        '''
        #方法二:采用自带的tokenier计算长度(更慢),英文llama与上述方法采用相同的词向量,中文不同
        from transformers import AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained(self.path)
        return len(tokenizer.encode(prompt))
 
    def bin_trim(self, prompt: str, num_token: int) -> str:
        """Get a suffix of prompt which is no longer than num_token tokens.
 
        Args:
            prompt (str): Input string.
            num_token (int): The upper bound of token numbers.
 
        Returns:
            str: The trimmed prompt.
        """
        token_len = self.get_token_len(prompt)
        if token_len <= num_token:
            return prompt
        pattern = re.compile(r'[\u4e00-\u9fa5]')
        if pattern.search(prompt):
            words = list(jieba.cut(prompt, cut_all=False))
            sep = ''
        else:
            words = prompt.split(' ')
            sep = ' '
 
        l, r = 1, len(words)
        while l + 2 < r:
            mid = (l + r) // 2
            if self.mode == 'front':
                cur_prompt = sep.join(words[-mid:])
            elif self.mode == 'mid':
                cur_prompt = sep.join(words[:mid]) + sep.join(words[-mid:])
            elif self.mode == 'rear':
                cur_prompt = sep.join(words[:mid])
 
            if self.get_token_len(cur_prompt) <= num_token:
                l = mid  # noqa: E741
            else:
                r = mid
 
        if self.mode == 'front':
            prompt = sep.join(words[-l:])
        elif self.mode == 'mid':
            prompt = sep.join(words[:l]) + sep.join(words[-l:])
        elif self.mode == 'rear':
            prompt = sep.join(words[:l])
        return prompt