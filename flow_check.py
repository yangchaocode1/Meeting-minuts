"""flow_check: 流程测试演示模块，描述一个任务在 Flow 中的阶段流转。"""

FLOW_STAGES = ("assign", "implement", "verify", "conclude")


def stage_index(stage: str) -> int:
    """返回阶段的 0 基下标；未知阶段抛出 ValueError。"""
    try:
        return FLOW_STAGES.index(stage)
    except ValueError:
        raise ValueError(f"unknown stage: {stage!r}") from None


def next_stage(stage: str) -> str:
    """返回给定阶段的下一阶段；传入最后一个阶段时抛出 ValueError。"""
    idx = stage_index(stage)
    if idx == len(FLOW_STAGES) - 1:
        raise ValueError(f"no stage after {stage!r}")
    return FLOW_STAGES[idx + 1]
