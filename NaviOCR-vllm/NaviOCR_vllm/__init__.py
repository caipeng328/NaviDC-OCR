"""vLLM plugin registration for NaviOCR."""

from __future__ import annotations


def register() -> None:
    from vllm import ModelRegistry

    model_ref = "NaviOCR_vllm.qwen2_5_vl:Qwen2_5_VLForConditionalGeneration"

    # Keep the original architecture name so existing NaviOCR config.json files
    # can run without changing their architectures field.
    ModelRegistry.register_model("Qwen2_5_VLForConditionalGeneration", model_ref)

    # Also expose an explicit NaviOCR name for future model configs.
    ModelRegistry.register_model("NaviOCRForConditionalGeneration", model_ref)
