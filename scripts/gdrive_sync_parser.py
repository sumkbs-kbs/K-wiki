import os
import shutil
import re

SOURCE_DOCS = r"G:\내 드라이브\4_문서"
SOURCE_BOOKS = r"G:\내 드라이브\도서"
TARGET_DIR = r"c:\Python\wiki\My_Wiki\LLM-Wiki\GoogleDrive"

SKIP_EXTS = {".ai", ".psd", ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ini"}
LINK_EXTS = {".zip", ".7z", ".rar", ".gz", ".tar", ".gdoc", ".gslides", ".gsheet"}
WRAP_EXTS = {".pdf"}

def fix_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', '_', filename).strip()

def process_directory(source_path, target_path_base, folder_name, global_toc, link_only=False):
    print(f"Processing: {source_path}")
    if not os.path.exists(source_path):
        print(f"Directory not found: {source_path}")
        return
        
    target_path = os.path.join(target_path_base, folder_name)
    os.makedirs(target_path, exist_ok=True)
    
    local_toc = [f"# {folder_name} 목차\n"]
    
    for root, dirs, files in os.walk(source_path):
        for file in files:
            ext_full = os.path.splitext(file)[1].lower()
            src_file_path = os.path.join(root, file)
            
            # calculate relative structure to keep subdirectories
            rel_path = os.path.relpath(root, source_path)
            if rel_path == ".":
                dst_root = target_path
            else:
                dst_root = os.path.join(target_path, rel_path)
                os.makedirs(dst_root, exist_ok=True)
            
            dst_file_path = os.path.join(dst_root, file)
            
            if ext_full in SKIP_EXTS:
                continue
                
            elif ext_full in LINK_EXTS or link_only:
                # Add link directly to G:\...
                safe_name = file
                link_addr = "file:///" + src_file_path.replace("\\", "/")
                local_toc.append(f"- 📦 [대용량 파일/구글문서 링크: {safe_name}]({link_addr})")
                
            else:
                # Copy the file
                if not os.path.exists(dst_file_path):
                    try:
                        shutil.copy2(src_file_path, dst_file_path)
                    except Exception as e:
                        print(f"Failed to copy {src_file_path}: {e}")
                        continue
                
                safe_name = fix_filename(file)
                
                # If PDF, create a markdown wrapper
                if ext_full in WRAP_EXTS:
                    base_only = os.path.splitext(file)[0]
                    safe_base = fix_filename(base_only)
                    md_wrapper_path = os.path.join(dst_root, f"{safe_base}.md")
                    
                    if not os.path.exists(md_wrapper_path):
                        with open(md_wrapper_path, 'w', encoding='utf-8') as mf:
                            mf.write(f"---\ntype: gdrive_document\n---\n\n# {base_only}\n\n![[{file}]]\n")
                            
                    local_toc.append(f"- 📄 [[{safe_base}]]")
                else:
                    # other files like .docx, .txt
                    local_toc.append(f"- 📎 [[{file}]]")

    # save local TOC
    local_index = os.path.join(target_path, "_Index.md")
    if len(local_toc) > 1: # has contents
        with open(local_index, 'w', encoding='utf-8') as f:
            f.write("\n".join(local_toc))
        global_toc.append(f"- [[_Index|{folder_name} 폴더 문서 보기]] (경로: `{folder_name}/`)")

if __name__ == "__main__":
    os.makedirs(TARGET_DIR, exist_ok=True)
    global_toc_doc = []
    global_toc_bok = []
    
    print("Migrating 4_문서 folder...")
    process_directory(SOURCE_DOCS, TARGET_DIR, "4_문서", global_toc_doc)
    
    print("Migrating 도서 folder...")
    process_directory(SOURCE_BOOKS, TARGET_DIR, "도서", global_toc_bok, link_only=True)
    
    # Write master index
    master_index_path = os.path.join(TARGET_DIR, "_Index_구글드라이브.md")
    with open(master_index_path, 'w', encoding='utf-8') as f:
        f.write("# 구글 드라이브 (문서 & 도서) 지식창고\n\n")
        
        f.write("## 📝 4_문서\n")
        f.write("\n".join(global_toc_doc) if global_toc_doc else "- 문서가 없습니다.")
        f.write("\n\n")
        
        f.write("## 📚 도서\n")
        f.write("\n".join(global_toc_bok) if global_toc_bok else "- 도서가 없습니다.")
        f.write("\n")

    print("Success! Migration complete.")
