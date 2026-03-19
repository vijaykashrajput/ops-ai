from app.tools.vector_store import VectorStore
from app.tools.kubernetes_client import KubernetesClient

store = VectorStore()

store.add_log("1", "High CPU usage due to traffic spike")
store.add_log("2", "Memory leak causing service crash")
store.add_log("3", "Database connection timeout error")

print("Logs seeded")