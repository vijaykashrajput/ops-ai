from .base_agent import BaseAgent
from app.tools.kubernetes_client import KubernetesClient

class FixAgent(BaseAgent):

    async def run(self, data):
        k8s = KubernetesClient()

        analysis = data.get("analysis", {})
        confidence = data.get("confidence", 0)

        if confidence < 0.8:
            return "Low confidence — manual intervention required"

        root_cause = str(analysis).lower()

        if "cpu" in root_cause:
            k8s.scale_pods()
            return "Scaled pods due to high CPU"

        if "memory" in root_cause:
            k8s.restart_service()
            return "Restarted service due to memory issue"

        return "No automated fix available"