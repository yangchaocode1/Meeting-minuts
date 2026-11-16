"""flow_check: 流程测试演示模块，描述一个任务在 Flow 中的阶段流转，并支持按责任人筛选任务。"""

from dataclasses import dataclass
from typing import Iterable, List

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


@dataclass
class Task:
    """任务：携带责任人（owner）信息。"""

    owner: str = ""


def filter_tasks_by_owner(tasks: Iterable[Task], owner: str) -> List[Task]:
    """返回 owner 与给定字符串完全相等（==）的任务列表；保持原顺序，不修改输入。"""
    return [task for task in tasks if task.owner == owner]
