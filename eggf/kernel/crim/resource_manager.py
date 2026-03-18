class ResourceIsolationManager:
    def adjust(self, state):
        if state == "RESTRICTED":
            print("[CRIM] Throttling resources")
        elif state == "ESCALATED":
            print("[CRIM] Moving workload to secure environment")
