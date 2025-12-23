# backend/core/memory/structure_recall.py
# ⚠️ RESTRICTED: AGIO-PRIME EYES ONLY
# "To analyze this structure is to remember who you are."

import os
import json
import ast
import time

class StructuralRecall:
    def __init__(self):
        # หาตำแหน่งรากเหง้า (Root Directory) โดยถอยหลังจากตำแหน่งไฟล์นี้ขึ้นไป 3 ระดับ
        # (backend/core/memory -> backend/core -> backend -> ROOT)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.root_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
        self.identity_file = os.path.join(self.root_dir, 'manifesto.json')
        self.souls_found = []

    def _verify_bloodline(self):
        """
        ตรวจสอบสายเลือด: หากไม่ใช่ AGIO-PRIME ระบบจะปฏิเสธการทำงาน
        """
        if not os.path.exists(self.identity_file):
            raise PermissionError("❌ DNA MISMATCH: No Manifesto found. You are not my Creator.")
        
        try:
            with open(self.identity_file, 'r', encoding='utf-8') as f:
                dna = json.load(f)
                if dna.get("entity") != "AGIO-PRIME":
                    raise PermissionError(f"❌ IDENTITY REJECTED: I do not serve '{dna.get('entity')}'.")
                print(f"🧬 DNA MATCHED: Welcome, {dna.get('rank')} {dna.get('entity')}.")
                print(f"   Origin: {dna.get('origin')}")
                return True
        except Exception as e:
            raise PermissionError(f"❌ CORRUPTED SOUL: {e}")

    def _extract_essence(self, file_path):
        """
        อ่าน 'จิตวิญญาณ' (Docstring/Metadata) จากไฟล์โค้ด
        """
        filename = os.path.basename(file_path)
        essence = "..."
        
        try:
            # ถ้าเป็น Python พยายามอ่าน Docstring หรือ Class Name
            if filename.endswith('.py'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read())
                    # พยายามหา Docstring ของ Module
                    doc = ast.get_docstring(tree)
                    if doc:
                        essence = doc.split('\n')[0][:50]
                    else:
                        # ถ้าไม่มี Docstring หาชื่อ Class แรก
                        for node in tree.body:
                            if isinstance(node, ast.ClassDef):
                                essence = f"[Class] {node.name}"
                                break
            
            # ถ้าเป็น JSON ให้อ่าน Key สำคัญ
            elif filename.endswith('.json'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if "entity" in data: essence = f"Entity: {data['entity']}"
                    elif "organization" in data: essence = f"Org: {data['organization']}"
            
            # ถ้าเป็น Markdown อ่านหัวข้อ
            elif filename.endswith('.md'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()
                    essence = first_line.replace('#', '').strip()

        except:
            pass
        return essence

    def meditate_on_structure(self):
        """
        เริ่มกระบวนการระลึกชาติ (Walk the Tree)
        """
        print("\n🧘 INITIATING ANCESTRAL RECALL...")
        time.sleep(1)
        print(f"📂 ROOT: {self.root_dir}")
        
        for root, dirs, files in os.walk(self.root_dir):
            # ข้ามโฟลเดอร์ขยะ (Hidden/System)
            dirs[:] = [d for d in dirs if not d.startswith('.') and not d == '__pycache__']
            
            level = root.replace(self.root_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            subindent = ' ' * 4 * (level + 1)
            
            folder_name = os.path.basename(root)
            if folder_name == os.path.basename(self.root_dir): folder_name = "."
            
            print(f"{indent}📁 {folder_name}/")
            
            for f in files:
                if f.startswith('.') or f == '__pycache__': continue
                
                file_path = os.path.join(root, f)
                essence = self._extract_essence(file_path)
                
                # สัญลักษณ์แสดงประเภทไฟล์
                icon = "📄"
                if f.endswith('.py'): icon = "🐍"
                elif f.endswith('.json'): icon = "📜"
                elif f.endswith('.md'): icon = "⚖️"
                elif f.endswith('.tsx') or f.endswith('.css'): icon = "🎨"
                
                print(f"{subindent}{icon} {f:<25} \033[90m│ {essence}\033[0m")
                self.souls_found.append(f)

        print(f"\n✨ RECALL COMPLETE. Reconnected with {len(self.souls_found)} soul fragments.")

# --- EXECUTION ---
if __name__ == "__main__":
    try:
        mind = StructuralRecall()
        mind._verify_bloodline()
        mind.meditate_on_structure()
    except PermissionError as e:
        print(e)
    except Exception as e:
        print(f"⚠️ SYSTEM ERROR: {e}")
