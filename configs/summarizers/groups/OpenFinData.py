OpenFinData_summary_groups = []

_OpenFinData = ['data_inspection', 'emotion_identification', 'entity_disambiguation', 'entity_recognition', 'financial_facts', 'financial_terminology', 'intent_understanding', 'metric_calculation', 'value_extraction']
_OpenFinData = ['OpenFinData-' + s for s in _OpenFinData]
OpenFinData_summary_groups.append({'name': 'OpenFinData', 'subsets': _OpenFinData})
