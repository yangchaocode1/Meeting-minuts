import unittest

from flow_check import FLOW_STAGES, Task, filter_tasks_by_owner, next_stage, stage_index


class FlowCheckTests(unittest.TestCase):
    def test_stage_order(self):
        self.assertEqual(FLOW_STAGES, ("assign", "implement", "verify", "conclude"))

    def test_stage_index(self):
        for expected, stage in enumerate(FLOW_STAGES):
            self.assertEqual(stage_index(stage), expected)

    def test_unknown_stage_raises(self):
        with self.assertRaises(ValueError):
            stage_index("deploy")

    def test_next_stage(self):
        self.assertEqual(next_stage("assign"), "implement")
        self.assertEqual(next_stage("implement"), "verify")
        self.assertEqual(next_stage("verify"), "conclude")

    def test_next_stage_after_last_raises(self):
        with self.assertRaises(ValueError):
            next_stage("conclude")


class FilterTasksByOwnerTests(unittest.TestCase):
    def test_task_owner_field(self):
        self.assertEqual(Task(owner="张三").owner, "张三")

    def test_task_owner_default(self):
        self.assertEqual(Task().owner, "")

    def test_filter_exact_match_keeps_order(self):
        lisi = Task(owner="李四")
        zhangsan_a = Task(owner="张三")
        wangwu = Task(owner="王五")
        zhangsan_b = Task(owner="张三")
        result = filter_tasks_by_owner([lisi, zhangsan_a, wangwu, zhangsan_b], "张三")
        self.assertEqual(len(result), 2)
        self.assertIs(result[0], zhangsan_a)
        self.assertIs(result[1], zhangsan_b)

    def test_filter_no_match_returns_empty(self):
        tasks = [Task(owner="张三"), Task(owner="李四")]
        result = filter_tasks_by_owner(tasks, "王五不存在")
        self.assertEqual(result, [])

    def test_filter_empty_input_returns_empty(self):
        result = filter_tasks_by_owner([], "张三")
        self.assertEqual(result, [])

    def test_filter_excludes_unassigned(self):
        zhangsan_task = Task(owner="张三")
        tasks = [zhangsan_task, Task()]
        result = filter_tasks_by_owner(tasks, "张三")
        self.assertEqual(result, [zhangsan_task])
        for task in result:
            self.assertIsNot(task, tasks[1])

    def test_filter_similar_owner_not_matched(self):
        zhangsan = Task(owner="张三")
        zhangsanfeng = Task(owner="张三丰")
        result = filter_tasks_by_owner([zhangsan, zhangsanfeng], "张三")
        self.assertEqual(result, [zhangsan])
        self.assertNotIn(zhangsanfeng, result)

    def test_filter_does_not_mutate_input(self):
        tasks = [Task(owner="张三"), Task(owner="李四")]
        snapshot = list(tasks)
        result = filter_tasks_by_owner(tasks, "张三")
        self.assertEqual(tasks, snapshot)
        self.assertIsNot(result, tasks)


if __name__ == "__main__":
    unittest.main()
