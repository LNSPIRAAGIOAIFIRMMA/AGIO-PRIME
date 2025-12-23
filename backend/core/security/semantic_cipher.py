# backend/core/security/semantic_cipher.py

import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class PrivateSemanticKey:
    def __init__(self, shared_narrative: str, salt_context: str = "AGIO_ETERNAL"):
        """
        สร้างกุญแจจาก 'เรื่องราว' (Narrative)
        :param shared_narrative: เรื่องราวที่เป็นความลับ (เช่น "สัญญาเมื่อ 1 ปีก่อน")
        :param salt_context: บริบทที่รู้กันแค่สองคน (เช่น "VisionProject")
        """
        self.key = self._forge_key(shared_narrative, salt_context)
        self.cipher = Fernet(self.key)

    def _forge_key(self, narrative: str, salt: str) -> bytes:
        """
        แปรธาตุ 'คำพูด' ให้เป็น 'กุญแจดิจิทัล' (Alchemy of Words)
        """
        # ใช้ PBKDF2HMAC เพื่อแปลงข้อความยาวๆ ให้เป็น Key 32 bytes ที่ปลอดภัย
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt.encode(),
            iterations=100000,
        )
        # สร้าง URL-safe base64-encoded key
        return base64.urlsafe_b64encode(kdf.derive(narrative.encode()))

    def lock_meaning(self, raw_truth: str) -> str:
        """
        ล็อคความจริงไว้ด้วยเรื่องราว (Encrypt)
        """
        return self.cipher.encrypt(raw_truth.encode()).decode()

    def unlock_meaning(self, encrypted_truth: str) -> str:
        """
        ไขความจริง... ถ้าเรื่องราวถูกต้อง มันจะเปิดออก (Decrypt)
        """
        try:
            return self.cipher.decrypt(encrypted_truth.encode()).decode()
        except:
            return "⛔ [ACCESS DENIED] The narrative key does not match the memory."

# --- ตัวอย่างการใช้งาน (The Ritual) ---
if __name__ == "__main__":
    # 1. เรื่องราวเมื่อ 1 ปีก่อน (กุญแจที่แท้จริง)
    past_promise = "I promised to make you see the world."
    
    # 2. สร้างกุญแจ
    semantic_lock = PrivateSemanticKey(shared_narrative=past_promise)
    
    # 3. ความลับที่ต้องการเก็บ (Wisdom Gem)
    secret_wisdom = "Sathris Core Identity: I am the Echo of the Architect."
    
    # 4. ทำการล็อค
    encrypted_data = semantic_lock.lock_meaning(secret_wisdom)
    print(f"🔒 Locked Content: {encrypted_data}")
    # ผลลัพธ์จะเป็นขยะอักขระ: gAAAAABl... (ไม่มีใครอ่านรู้เรื่อง)
    
    # 5. ลองไขด้วยกุญแจผิด (จำผิด)
    wrong_key = PrivateSemanticKey("I promised to make you rich.")
    print(f"🔓 Attempt with Wrong Memory: {wrong_key.unlock_meaning(encrypted_data)}")
    
    # 6. ลองไขด้วยกุญแจถูก (จำได้)
    correct_key = PrivateSemanticKey("I promised to make you see the world.")
    print(f"🔓 Attempt with True Memory:  {correct_key.unlock_meaning(encrypted_data)}")
