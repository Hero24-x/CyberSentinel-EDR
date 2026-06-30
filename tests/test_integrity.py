import unittest

from agent.integrity.file_integrity \
    import FileIntegrity


class TestIntegrity(unittest.TestCase):

    def test_hash_generation(self):

        hash_value = \
            FileIntegrity.calculate_hash(
                __file__
            )

        self.assertTrue(
            len(hash_value) > 0
        )


if __name__ == "__main__":
    unittest.main()
