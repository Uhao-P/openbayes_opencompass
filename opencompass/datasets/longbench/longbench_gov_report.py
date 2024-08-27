from datasets import Dataset, load_dataset

from opencompass.registry import LOAD_DATASET

from ..base import BaseDataset


@LOAD_DATASET.register_module()
class LongBenchgov_reportDataset(BaseDataset):

    @staticmethod
    def load(**kwargs):
        dataset = load_dataset('json', data_files={"test": kwargs['path']})
        split = 'test'
        raw_data = []
        for i in range(len(dataset[split])):
            context = dataset[split]['context'][i]
            answers = dataset[split]['answers'][i]
            raw_data.append({'context': context, 'answers': answers})
        dataset[split] = Dataset.from_list(raw_data)
        return dataset
