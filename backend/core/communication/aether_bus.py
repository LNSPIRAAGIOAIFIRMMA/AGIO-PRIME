# ปรับปรุง backend/main.py

from core.communication.aether_bus import AsyncAetherBus, AetherEvent

# 1. สร้างระบบประสาท
nervous_system = AsyncAetherBus()

# 2. สร้าง "สติ" (Sati Observer) เพื่อเฝ้าดูความคิด
async def sati_observer(event: AetherEvent):
    # เมื่อมีความคิดเกิดขึ้น ให้ Sathris รับรู้
    if event.topic == "intent.detected":
        print(f"👁️ [Sati] Recognizing intent: {event.payload.get('content')}")
        # สั่งให้ Sathris ทำงานต่อ...

# 3. เริ่มต้นระบบตอนเปิด Server
@app.on_event("startup")
async def wakeup_nervous_system():
    print("🧠 [System] Nervous System Coming Online...")
    nervous_system.subscribe("intent.detected", sati_observer)

# 4. ปรับจุดรับ Request ให้ส่งกระแสประสาทแทนการเรียกฟังก์ชันตรงๆ
@app.post("/reflect")
async def reflect_intent(input_data: VoidInput):
    # แทนที่จะเรียก sathris.reflect() ตรงๆ เราส่ง "กระแสจิต" เข้าไปใน Bus
    event = AetherEvent(
        topic="intent.detected",
        payload={"content": input_data.intent},
        sender_id="UserVessel"
    )
    await nervous_system.publish(event)
    
    return {"status": "Processing in Aether", "job_id": event.event_id}
