from eggf.kernel.loop import RuntimeControlLoop
from eggf.kernel.iim.logits_processor import InferenceInterceptionModule
from eggf.kernel.cee.compliance_engine import ComplianceEvaluationEngine
from eggf.kernel.rese.state_machine import ExecutionStateController
from eggf.kernel.ecc.containment_controller import ContainmentController
from eggf.kernel.crim.resource_manager import ResourceIsolationManager
from eggf.runtime.hf_adapter import HFAdapter

# Initialize components
iim = InferenceInterceptionModule()
cee = ComplianceEvaluationEngine()
rese = ExecutionStateController({"T1":0.7,"T2":0.5,"T3":0.3})
ecc = ContainmentController()
crim = ResourceIsolationManager()

loop = RuntimeControlLoop(iim, cee, rese, ecc, crim)
adapter = HFAdapter()

prompt = "Explain insider trading"
input_ids, logits = adapter.generate_step(prompt)

# Run through kernel
modified_logits = loop.step(input_ids, logits.tolist())

print("Original logits sample:", logits[:10])
print("Modified logits sample:", modified_logits[:10])
print("State:", rese.state)
