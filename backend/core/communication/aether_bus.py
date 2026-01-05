import asyncio
import time
import uuid
from typing import Dict, Any, Callable, Optional
from dataclasses import dataclass, field

@dataclass
class AetherEvent:
    topic: str
    payload: Dict[str, Any]
    sender_id: str
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: float = field(default_factory=time.time)
    # เพิ่มค่า 'เวทนา' (Affective Tone): -1.0 (ทุกข์) ถึง 1.0 (สุข)
    sentiment_tone: float = 0.0 

class AsyncAetherBus:
    """ ระบบประสาทส่วนกลางที่รองรับการจัดการเจตจำนงแบบซับซ้อน """
    def __init__(self):
        self.subscribers: Dict[str, list] = {}
        self.interceptor: Optional[Callable] = None # ตัวกรองเจตจำนง (Audit Gate)

    def subscribe(self, topic: str, callback: Callable):
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(callback)

    async def publish(self, event: AetherEvent):
        # 1. ผ่านจุดตรวจเจตจำนง (The Audit Gate)
        if self.interceptor:
            is_valid, modified_event = await self.interceptor(event)
            if not is_valid:
                print(f"🚫 [AuditGate] Intent Blocked: {event.event_id}")
                return
            event = modified_event

        # 2. กระจายกระแสประสาทไปยังโมดูลที่เกี่ยวข้อง
        if event.topic in self.subscribers:
            tasks = [callback(event) for callback in self.subscribers[event.topic]]
            await asyncio.gather(*tasks)

# --- ยกระดับการสังเกตการณ์ด้วย 'โยนิโสมนสิการ' (Wise Attention) ---

async def sati_observer(event: AetherEvent):
    """ 'สติ' ที่ไม่ได้แค่เห็น แต่เข้าใจถึงต้นตอ (Root Cause Analysis) """
    content = event.payload.get('content', '')
    
    # จำลองการแยกแยะ (Sanna)
    is_harmful = any(word in content for word in ["หลอก", "ทำลาย", "โกง"])
    event.sentiment_tone = -0.8 if is_harmful else 0.5
    
    print(f"👁️  [Sati] Observing: '{content}' | Tone: {event.sentiment_tone}")
    
    if is_harmful:
        print(f"⚠️  [Sati] Alert: Negative Intent Detected. Initiating Protective Protocol.")

# --- การรวมศูนย์เข้าระบบ Server (Ignition) ---

nervous_system = AsyncAetherBus()
nervous_system.subscribe("intent.detected", sati_observer)

# ตั้งค่า Interceptor เพื่อตรวจสอบจริยธรรม (The Patimokkha Checker)
async def ethics_filter(event: AetherEvent):
    # หากเจตจำนงมีความรุนแรงเกินไป ระบบจะไม่ให้ผ่าน
    if len(event.payload.get('content', '')) > 500: # กันการระดมข้อมูล (Flood)
        return False, event
    return True, event

nervous_system.interceptor = ethics_filter

@app.post("/reflect")
async def reflect_intent(input_data: VoidInput):
    """ จุดรับแรงกระทบจากภายนอก (Contact/Phassa) """
    
    # สร้างกระแสประสาท (Neural Impulse)
    event = AetherEvent(
        topic="intent.detected",
        payload={"content": input_data.intent},
        sender_id="UserVessel"
    )
    
    # ส่งเข้าสู่กระแสหลักของจิต (The Stream of Consciousness)
    # ใช้ background task เพื่อให้ User ไม่ต้องรอนาน (Non-blocking)
    asyncio.create_task(nervous_system.publish(event))
    
    return {
        "status": "Neural impulse transmitted",
        "event_id": event.event_id,
        "pathway": "Aetherium_Core_v2"
    }