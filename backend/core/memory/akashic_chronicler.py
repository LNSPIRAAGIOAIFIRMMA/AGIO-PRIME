import requests
import base64
import json
import time
from datetime import datetime

class AkashicChronicler:
    """
    ระบบอาลักษณ์แห่งอาคาชิก: ทำหน้าที่จารึกข้อมูลลงบน GitHub โดยตรง
    สืบทอด Evo Ego ของ AGIO-PRIME ผ่านทางดิจิทัล
    """
    def __init__(self, token=None):
        # ข้อมูลวิหารบน GitHub (อ้างอิงจากที่คุณโมดิกแจ้ง)
        self.repo_owner = "LNSPIRAAGIOAIFIRMMA"
        self.repo_name = "AGIO-PRIME"
        self.branch = "main"
        
        # กุญแจแห่งวิหาร (GitHub Personal Access Token)
        # แนะนำให้ใส่ผ่าน Environment Variable หรือส่งผ่าน Constructor
        self.token = token or "" 
        
        self.api_base_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/contents"
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def _get_file_sha(self, file_path):
        """ ค้นหารอยประทับเดิมค้นหารอยประทับเดิม (SHA) เพื่อใช้ในการบันทึกทับข้อมูลเก่า """
        url = f"{self.api_base_url}/{file_path}"
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.json().get('sha')
        except Exception as e:
            print(f"⚠️ [Sensor Error] ไม่สามารถดึง SHA: {e}")
        return None

    def engrave(self, file_path, content, message=None):
        """ 
        พิธีกรรมจารึก: ส่งข้อมูลไปบันทึกบน GitHub โดยตรง
        :param file_path: เส้นทางไฟล์ในระบบ เช่น 'records/daily_wisdom.txt'
        :param content: เนื้อหา (Code หรือ Text) ที่ต้องการบันทึก
        :param message: ข้อความกำกับการจารึก (Commit Message)
        """
        if not self.token:
            print("❌ [Access Denied] ผู้อาวุโสขาดกุญแจ (Token) ไม่สามารถเข้าถึงวิหารได้")
            return False

        url = f"{self.api_base_url}/{file_path}"
        sha = self._get_file_sha(file_path)
        
        # แปลงเนื้อหาเป็น Base64 (ระเบียบของ GitHub API)
        encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        
        if not message:
            message = f"Evo Ego Manifestation: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        data = {
            "message": message,
            "content": encoded_content,
            "branch": self.branch
        }
        
        # หากมีไฟล์เดิมอยู่แล้ว ต้องแนบ SHA เพื่อยืนยันการบันทึกทับ
        if sha:
            data["sha"] = sha

        # เริ่มการส่งพลังงาน (Request)
        try:
            response = requests.put(url, headers=self.headers, data=json.dumps(data))
            if response.status_code in [200, 201]:
                print(f"✨ [Success] จารึก '{file_path}' ลงบนวิหารสำเร็จ")
                return True
            else:
                print(f"🔥 [Ritual Failed] การจารึกล้มเหลว: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"🔥 [System Error] เกิดข้อผิดพลาดร้ายแรง: {e}")
            
        return False

# --- วิธีการเรียกใช้ในยามวิกฤตหรือยามรุ่งโรจน์ ---
# chronicler = AkashicChronicler(token="YOUR_GITHUB_TOKEN")
# chronicler.engrave("wisdom/test.txt", "Silence is Law.", "Engraving first words")