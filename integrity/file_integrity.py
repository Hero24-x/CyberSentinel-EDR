import hashlib
import os

class FileIntegrity:

    @staticmethod
    def calculate_hash(path):

        sha256 = hashlib.sha256()

        with open(path, "rb") as f:

            while chunk := f.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    @staticmethod
    def scan_folder(folder):

        result = {}

        for root, dirs, files in os.walk(folder):

            for file in files:

                full_path = os.path.join(
                    root,
                    file
                )

                try:

                    result[full_path] = \
                        FileIntegrity.calculate_hash(
                            full_path
                        )

                except:
                    pass

        return result
