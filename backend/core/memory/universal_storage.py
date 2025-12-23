# backend/core/memory/universal_storage.py

import json
import os

class UniversalWisdomStorage:
    def __init__(self, api_key="STORAGE_ACCESS_KEY"):
        self.local_db = "akashic_records.json"
        self.api_key = api_key

    def commit_transaction(self, wisdom_gem):
        """
        บันทึกผลึกปัญญาลงสู่ถาวรวัตถุ (Persistent Storage)
        รองรับทั้ง Local File และ Cloud API (จำลอง)
        """
        print(f"💾 [Storage] Committing Wisdom Gem: {wisdom_gem['rule_id']}...")
        
        # 1. โหลดข้อมูลเก่า (Ancestral Recall)
        history = self._load_local()
        
        # 2. ผนวกความรู้ใหม่ (Integration)
        history.append(wisdom_gem)
        
        # 3. บันทึกกลับลงไป (Etching)
        self._save_local(history)
        
        # 4. (ถ้ามี) ส่งไปยัง Storage Access API เพื่อข้ามโดเมน
        # self._sync_to_cloud(wisdom_gem)
        
        print(f"   ✅ Wisdom Preserved. Total Records: {len(history)}")

    def _load_local(self):
        if not os.path.exists(self.local_db):
            return []
        try:
            with open(self.local_db, 'r') as f:
                return json.load(f)
        except:
            return []

    def _save_local(self, data):
        with open(self.local_db, 'w') as f:
            json.dump(data, f, indent=4)

# --- การเชื่อมต่อเข้ากับ The Enforcer ---
# ในคลาส TheEnforcer ของท่าน ให้เพิ่มบรรทัดนี้:
# self.storage = UniversalWisdomStorage()
# และในเมธอด commit_ritual:
# self.storage.commit_transaction(gem)
