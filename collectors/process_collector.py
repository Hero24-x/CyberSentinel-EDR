import psutil

class ProcessCollector:

    @staticmethod
    def collect():

        processes = []

        for proc in psutil.process_iter(
            ['pid', 'name', 'username']
        ):
            try:

                processes.append({
                    "pid": proc.info["pid"],
                    "name": proc.info["name"],
                    "user": proc.info["username"]
                })

            except Exception:
                continue

        return processes
