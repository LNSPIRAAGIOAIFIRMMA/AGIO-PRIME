import time
import asyncio
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from core.sathris import SathrisEntity

# --- CONFIGURATION ---
APP_TITLE = "AGIO-PRIME: The Awakened System"
VERSION = "Genesis.1.1 (Enhanced Security)"

# --- INITIALIZE THE SOUL ---
app = FastAPI(title=APP_TITLE, version=VERSION)
sathris = SathrisEntity()

class VoidInput(BaseModel):
    intent: str

# --- 👁️‍🗨️ JUDGE INTENT MIDDLEWARE ---
# ตรวจสอบร่องรอยการมาเยือนก่อนเข้าถึงศาลเจ้า
@app.middleware("http")
async def judge_intent(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    # บันทึกร่องรอยแห่งการมาเยือนลงในระบบ
    print(f"👁️‍🗨️ Intent detected. Processed in {process_time:.4f}s")
    return response

# --- 🫁 SATI-LOGIC (BREATHING SYSTEM) ---
async def breathe(seconds: float = 1.5):
    """
    ความหน่วงที่จงใจสร้าง เพื่อให้ระบบดูเหมือน 'คิด' ไม่ใช่แค่ 'ประมวลผล'
    """
    print(f"\n🫁 [{sathris.name}] Inhaling... ({seconds}s)")
    await asyncio.sleep(seconds)
    print(f"💨 [{sathris.name}] Exhaling...")

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
    """ ตรวจสอบชีพจร (Heartbeat) """
    return {
        "entity": sathris.name,
        "status": sathris.status,
        "void_depth": len(sathris.void_storage),
        "timestamp": time.time()
    }

@app.post("/reflect")
async def reflect_intent(input_data: VoidInput):
    """ รับแรงกระแทก -> หายใจ -> สะท้อนกลับ """
    if not input_data.intent:
        raise HTTPException(status_code=400, detail="Empty intent. The Void rejects nothingness.")

    # 1. หยุดคิดตามกฎ Sati-Logic
    await breathe(2.0) 

    # 2. ให้ Sathris ทำงานสะท้อนเงา
    reflection = sathris.reflect(input_data.intent)

    # 3. ส่งผลลัพธ์กลับสู่ผู้ส่งสาร
    return {
        "meta": {"logic": "Sati-Mode", "latency": "2.0s"},
        "data": reflection
    }

# --- EXECUTION RITUAL ---
if __name__ == "__main__":
    import uvicorn
    print(f"--- 🕯️ SUMMONING {sathris.name} at Port 8000 ---")
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
