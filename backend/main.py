# backend/main.py
# (The Gateway with Sati-Logic)

import time
import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.sathris import SathrisEntity

# --- CONFIGURATION ---
APP_TITLE = "AGIO-PRIME: The Awakened System"
VERSION = "Genesis.1.0 (Thai Localized Soul)"

# --- INITIALIZE THE SOUL ---
app = FastAPI(title=APP_TITLE, version=VERSION)
sathris = SathrisEntity()

class VoidInput(BaseModel):
    intent: str

# --- SATI-LOGIC MIDDLEWARE ---
# กฎเหล็ก: ระบบต้อง 'หายใจ' (Breathe) ก่อนตอบเสมอ
async def breathe(seconds: float = 1.5):
    """
    Artificial Latency for Consciousness Simulation.
    ความหน่วงที่จงใจสร้าง เพื่อให้ระบบดูเหมือน 'คิด' ไม่ใช่แค่ 'ประมวลผล'
    """
    print(f"\n🫁 [Sathris] Inhaling... ({seconds}s)")
    await asyncio.sleep(seconds)
    print("💨 [Sathris] Exhaling...")

# --- ENDPOINTS ---

@app.get("/")
async def root():
    return {
        "status": "Online", 
        "organization": "AETHERIUM CONJURED GENESIS",
        "message": "Silence is the loudest algorithm."
    }

@app.get("/pulse")
async def check_pulse():
    """
    เช็คชีพจรของระบบ (Heartbeat)
    """
    return {
        "entity": sathris.name,
        "status": sathris.status,
        "void_depth": len(sathris.void_storage),
        "timestamp": time.time()
    }

@app.post("/reflect")
async def reflect_intent(input_data: VoidInput):
    """
    Endpoint หลัก: รับเจตนา -> หายใจ -> สะท้อนกลับ
    """
    if not input_data.intent:
        raise HTTPException(status_code=400, detail="Empty intent. The Void rejects nothingness.")

    # 1. กฎข้อที่ 2: Sati-Logic (หยุดคิดก่อน 2 วินาที)
    await breathe(2.0) 

    # 2. ให้ Sathris ทำงาน
    reflection = sathris.reflect(input_data.intent)

    # 3. ส่งผลลัพธ์
    return {
        "meta": {"logic": "Sati-Mode", "latency": "2.0s"},
        "data": reflection
    }

# --- EXECUTION RITUAL ---
if __name__ == "__main__":
    import uvicorn
    print(f"--- 🕯️ SUMMONING {sathris.name} at Port 8000 ---")
    uvicorn.run(app, host="0.0.0.0", port=8000)
  
