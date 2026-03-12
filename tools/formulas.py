from langchain.tools import tool

@tool
def voltage_divider(vin: float, r1: float, r2: float) -> float:
    """
    Calculate the output voltage of a voltage divider.
    
    Vout = Vin * (R2 / (R1 + R2))
    """
    
    vout = vin * (r2 / (r1 + r2))
    return vout