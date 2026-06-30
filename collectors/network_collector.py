import psutil

class NetworkCollector:

    @staticmethod
    def collect():

        connections = []

        for conn in psutil.net_connections():

            try:

                connections.append({
                    "status": str(conn.status),
                    "pid": conn.pid
                })

            except Exception:
                pass

        return connections
