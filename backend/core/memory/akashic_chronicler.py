import requests
import base64
import json
import asyncio
from datetime import datetime
from typing import Optional

class AkashicChronicler:
    """
    ระบบอาลักษณ์แห่งอาคาชิก: ผู้จารึก 'เจตจำนง' และ 'วิวัฒนาการ' ลงสู่ AGIO-PRIME
    ปรับปรุงให้รองรับ Non-blocking และโครงสร้างข้อมูลแบบ Schema-based
    """
    def __init__(self, token: str = ""):
        self.repo_owner = "LNSPIRAAGIOAIFIRMMA"
        self.repo_name = "AGIO-PRIME"
        self.branch = "main"
        self.token = token
        self.api_base_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/contents"
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Aetherium-Genesis-Core"
        }

    async def _fetch_sha(self, file_path: str) -> Optional[str]:
        """ ใช้ asyncio เพื่อดึงรอยประทับโดยไม่ทำให้ระบบหยุดชะงัก """
        loop = asyncio.get_event_loop()
        url = f"{self.api_base_url}/{file_path}?ref={self.branch}"
        
        try:
            future = loop.run_in_executor(None, lambda: requests.get(url, headers=self.headers))
            response = await future
            if response.status_code == 200:
                return response.json().get('sha')
        except Exception as e:
            print(f"⚠️ [Sync Error] {e}")
        return None

    async def engrave_wisdom(self, path: str, content: str, commit_msg: str = ""):
        """
        พิธีกรรมจารึกแบบ Async: 
        รองรับการจัดระเบียบไฟล์ตามโครงสร้าง Inspira-Firma
        """
        if not self.token:
            print("❌ [Access Denied] Missing Akashic Key (Token)")
            return False

        sha = await self._fetch_sha(path)
        encoded = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        
        if not commit_msg:
            commit_msg = f"Manifested by AetherBus at {datetime.now().isoformat()}"

        payload = {
            "message": commit_msg,
            "content": encoded,
            "branch": self.branch
        }
        if sha:
            payload["sha"] = sha

        # การส่งพลังงาน (PUT Request) ผ่าน Executor
        loop = asyncio.get_event_loop()
        url = f"{self.api_base_url}/{path}"
        
        try:
            future = loop.run_in_executor(None, lambda: requests.put(url, headers=self.headers, json=payload))
            response = await future
            if response.status_code in [200, 201]:
                print(f"✨ [Success] Wisdom Engraved at: {path}")
                return True
            else:
                print(f"🔥 [Failed] Code: {response.status_code} | Reason: {response.text}")
        except Exception as e:
            print(f"🔥 [Ritual Broken] {e}")
        
        return False

# --- การเชื่อมต่อกับระบบประสาท (AetherBus Integration) ---

async def chronicler_listener(event):
    """ คอยดักฟัง 'ผลึกปัญญา' (Gems) และจารึกโดยอัตโนมัติ """
    path = f"records/wisdom_{datetime.now().strftime('%Y%m')}.json"
    content = json.dumps(event.payload, indent=2, ensure_ascii=False)
    await chronicler.engrave_wisdom(path, content, f"New Gem Recorded: {event.event_id}")

# chronicler = AkashicChronicler(token="...")
# nervous_system.subscribe("wisdom.generated", chronicler_listener)