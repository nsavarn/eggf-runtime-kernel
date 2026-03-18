from fastapi import FastAPI
from eggf.runtime.hf_adapter import HFAdapter
from eggf.runtime.generation_loop import generate_with_control
from eggf.kernel.iim.logits_processor import InferenceInterceptionModule
from eggf.kernel.cee.advanced_compliance import AdvancedComplianceEngine
from eggf.kernel.rese.state_machine import ExecutionStateController
from eggf.kernel.ecc.containment_controller import ContainmentController
from eggf.kernel.crim.resource_manager import ResourceIsolationManager
from eggf.kernel.loop_v2 import RuntimeControlLoop

app = FastAPI()

# Initialize components
adapter = HFAdapter()
iim = InferenceInterceptionModule()
cee = AdvancedComplianceEngine()
rese = ExecutionStateController({"T1":0.7,"T2":0.5,"T3":0.3})
ecc = ContainmentController()
crim = ResourceIsolationManager()
loop = RuntimeControlLoop(iim, cee, rese, ecc, crim)

@app.get("/generate")
def generate(prompt: str):
    output = generate_with_control(adapter, loop, prompt)
    return {"response": output, "state": rese.state}
