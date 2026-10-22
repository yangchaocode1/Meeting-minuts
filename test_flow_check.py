import unittest

from flow_check import FLOW_STAGES, next_stage, stage_index


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


if __name__ == "__main__":
    unittest.main()
