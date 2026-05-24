import os
import shutil
import re

SOURCE_DIR = r"C:\Users\user\Downloads\생존코딩-강의자료(전체통합본)\생존코딩-강의자료(All)"
TARGET_DIR = r"c:\Python\wiki\My_Wiki\LLM-Wiki\생존코딩강의"

ASSETS_PDF_DIR = os.path.join(TARGET_DIR, "Assets", "PDFs")
ASSETS_IMG_DIR = os.path.join(TARGET_DIR, "Assets", "Images")
ASSETS_ARCHIVE_DIR = os.path.join(TARGET_DIR, "Assets", "Archives")
DOCS_DIR = os.path.join(TARGET_DIR, "강의자료_문서")

def setup_directories():
    os.makedirs(ASSETS_PDF_DIR, exist_ok=True)
    os.makedirs(ASSETS_IMG_DIR, exist_ok=True)
    os.makedirs(ASSETS_ARCHIVE_DIR, exist_ok=True)
    os.makedirs(DOCS_DIR, exist_ok=True)

def fix_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', '_', filename).strip()

def process_pdfs():
    print("Processing PDFs...")
    pdf_source = os.path.join(SOURCE_DIR, "PDF강의자료")
    toc_lines = []
    
    if not os.path.exists(pdf_source):
        print(f"Directory not found: {pdf_source}")
        return toc_lines

    for f in os.listdir(pdf_source):
        if f.lower().endswith(".pdf"):
            src_path = os.path.join(pdf_source, f)
            dst_path = os.path.join(ASSETS_PDF_DIR, f)
            if not os.path.exists(dst_path):
                shutil.copy2(src_path, dst_path)
            
            base_name = os.path.splitext(f)[0]
            safe_name = fix_filename(base_name)
            
            md_path = os.path.join(DOCS_DIR, f"{safe_name}.md")
            with open(md_path, 'w', encoding='utf-8') as mf:
                mf.write(f"---\ntype: lecture_pdf\n---\n\n# {base_name}\n\n![[{f}]]\n")
            
            toc_lines.append(f"- [[{safe_name}]]")
    
    return toc_lines

def process_extras():
    print("Processing Extra Materials...")
    extra_source = os.path.join(SOURCE_DIR, "추가자료파일들")
    toc_lines = []
    
    if not os.path.exists(extra_source):
        print(f"Directory not found: {extra_source}")
        return toc_lines

    for d in os.listdir(extra_source):
        d_path = os.path.join(extra_source, d)
        if not os.path.isdir(d_path):
            continue
            
        safe_lecture = fix_filename(d)
        md_content = [f"---\ntype: lecture_material\n---\n\n# {safe_lecture} 강의 추자 자료 및 코드\n\n"]
        
        for f in os.listdir(d_path):
            if f == ".DS_Store": continue
            f_path = os.path.join(d_path, f)
            if not os.path.isfile(f_path): continue
            
            ext = f.lower().split('.')[-1]
            
            if ext in ['pdf']:
                dst_path = os.path.join(ASSETS_PDF_DIR, f)
                if not os.path.exists(dst_path): shutil.copy2(f_path, dst_path)
                md_content.append(f"## {f}\n![[{f}]]\n\n")
                
                # Also create an individual MD for this PDF for consistency
                base_name = os.path.splitext(f)[0]
                safe_name = fix_filename(base_name)
                pdf_md_path = os.path.join(DOCS_DIR, f"{safe_name}.md")
                if not os.path.exists(pdf_md_path):
                    with open(pdf_md_path, 'w', encoding='utf-8') as pmf:
                        pmf.write(f"---\ntype: lecture_pdf\n---\n\n# {base_name}\n\n![[{f}]]\n")

            elif ext in ['jpg', 'png', 'jpeg']:
                dst_path = os.path.join(ASSETS_IMG_DIR, f)
                if not os.path.exists(dst_path): shutil.copy2(f_path, dst_path)
                md_content.append(f"## {f}\n![[{f}]]\n\n")

            elif ext in ['zip', 'rar']:
                dst_path = os.path.join(ASSETS_ARCHIVE_DIR, f)
                if not os.path.exists(dst_path): shutil.copy2(f_path, dst_path)
                md_content.append(f"## {f}\n[[{f}]] (다운로드 링크)\n\n")

            elif ext in ['txt']:
                md_content.append(f"## {f}\n")
                try:
                    with open(f_path, 'r', encoding='utf-8') as txt_f:
                        content = txt_f.read()
                except UnicodeDecodeError:
                    try:
                        with open(f_path, 'r', encoding='cp949') as txt_f:
                            content = txt_f.read()
                    except:
                        content = "Error reading text file."
                
                # If the content looks like a prompt, we can put it in a quote block
                md_content.append(f"> [!tip] 바이브코딩 프롬프트 / 메모\n> \n")
                for line in content.splitlines():
                    md_content.append(f"> {line}\n")
                md_content.append("\n")

            elif ext in ['vue', 'js', 'html', 'css']:
                md_content.append(f"## {f}\n")
                try:
                    with open(f_path, 'r', encoding='utf-8') as txt_f:
                        content = txt_f.read()
                except:
                    content = "// Error reading file."
                md_content.append(f"```{ext}\n{content}\n```\n\n")

        # Write lecture MD
        if len(md_content) > 1: # basically if something was added
            out_file = os.path.join(DOCS_DIR, f"{safe_lecture} 실습자료.md")
            with open(out_file, 'w', encoding='utf-8') as f_out:
                f_out.write("".join(md_content))
            toc_lines.append(f"- [[{safe_lecture} 실습자료]]")

    return toc_lines

if __name__ == "__main__":
    print("Setting up directories...")
    setup_directories()
    
    print("Starting process...")
    pdf_toc = process_pdfs()
    extra_toc = process_extras()
    
    print("Creating Map of Content (_Index_생존코딩.md)...")
    index_path = os.path.join(TARGET_DIR, "_Index_생존코딩.md")
    
    with open(index_path, 'w', encoding='utf-8') as idx:
        idx.write("# 생존코딩 강의 (지도/목차)\n\n")
        
        idx.write("## 📝 실습 및 프롬프트 자료\n")
        idx.write("\n".join(extra_toc))
        idx.write("\n\n")

        idx.write("## 📚 강의 PDF\n")
        idx.write("\n".join(pdf_toc))
        idx.write("\n")
        
    print("Done! Migration complete.")
