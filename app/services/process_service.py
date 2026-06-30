import psutil

class ProcessService:

    @staticmethod
    def get_processes():

        processes = []

        for proc in psutil.process_iter(
            ['pid', 'name']
        ):
            try:
                processes.append({
                    "pid": proc.info["pid"],
                    "name": proc.info["name"]
                })
            except:
                pass

        return processes
