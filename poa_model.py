dic = {
    "Reason": "Why are we passing this case? What value are we adding to the customer by passing this? Is any language skill needed?",
    "Issue": "What is the actual issue being experienced? - i.e. When doing X the customer is experiencing X.",
    "StepsTried": "What did you already do? - i.e.  Reviewed logs and found X",
    "NextSteps": "What does the technician receiving the case need to do? i.e. WebEx to troubleshoot X",
    "NextCustomerContact": "Are they waiting for us, or are we waiting for them? What is the customer's availability after the current shift's business hours?Has the customer requested a call?"
}

class POAModel:
    def __init__(self):
        self.poa = None