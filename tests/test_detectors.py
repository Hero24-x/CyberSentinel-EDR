import unittest

from agent.detectors.process_detector \
    import ProcessDetector


class TestDetector(unittest.TestCase):

    def test_blacklisted_process(self):

        processes = [
            {
                "name": "keylogger.exe"
            }
        ]

        alerts = (
            ProcessDetector.detect(
                processes
            )
        )

        self.assertEqual(
            len(alerts),
            1
        )


if __name__ == "__main__":
    unittest.main()
