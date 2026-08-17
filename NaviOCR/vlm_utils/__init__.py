import importlib



__lazy_attrs__ = {
    "NaviOCRClient": (".NaviOCR_client", "NaviOCRClient"),
    "NaviOCRSamplingParams": (".NaviOCR_client", "NaviOCRSamplingParams"),
    "NaviOCRLogitsProcessor": (".vlm_client.vllm_v1_no_repeat_ngram", "VllmV1NoRepeatNGramLogitsProcessor"),
}


def __getattr__(name: str):
    if name in __lazy_attrs__:
        module_name, attr_name = __lazy_attrs__[name]
        module = importlib.import_module(module_name, __name__)
        return getattr(module, attr_name)
    raise AttributeError(f"Module '{__name__}' has no attribute '{name}'")


