import os
import json
import re
import html

TAKEOUT_DIR = r"C:\Users\user\Downloads\takeout-20260415T072005Z-3-001\Takeout"
WIKI_EXPORT_DIR = r"c:\Python\wiki\My_Wiki\LLM-Wiki\Takeout_Import"

def clean_html(raw_html):
    # remove head, style, script
    text = re.sub(r'<(script|style|head).*?>.*?</\1>', '', raw_html, flags=re.IGNORECASE | re.DOTALL)
    # replace <br> with newline
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    # replace <p> tags with double newline
    text = re.sub(r'</p\s*>', '\n\n', text, flags=re.IGNORECASE)
    # remove remaining tags
    text = re.sub(r'<[^>]+>', '', text)
    # unescape html entities
    text = html.unescape(text)
    # remove excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def fix_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', '_', filename).strip()

def process_gemini():
    gemini_dir = os.path.join(TAKEOUT_DIR, "Gemini")
    gems_file = os.path.join(gemini_dir, "gemini_gems_data.html")
    
    out_dir = os.path.join(WIKI_EXPORT_DIR, "Prompts", "Gems")
    os.makedirs(out_dir, exist_ok=True)
    
    if os.path.exists(gems_file):
        with open(gems_file, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        # Match <div><b>이름:</b>(.*?)<br><b>안내:</b>(.*?)<br><br></div>
        pattern = r'<div>\s*<b>이름:</b>\s*(.*?)\s*(?:<br>|\n)\s*<b>안내:\s*</b>(.*?)\s*(?:<br><br></div>|</div>)'
        matches = re.findall(pattern, content, flags=re.IGNORECASE|re.DOTALL)
        
        # If the above strict regex fails, let's use a simpler one
        if not matches:
             pattern2 = r'<b>이름:</b>(.*?)<br>.*?<b>안내:</b>(.*?)</div>'
             matches = re.findall(pattern2, content, flags=re.IGNORECASE|re.DOTALL)
             
        for name, instructions in matches:
            name = clean_html(name).strip()
            instructions = clean_html(instructions).strip()
            
            safe_name = fix_filename(name)
            md_content = f"---\ntype: gemini_gem\ntitle: \"{safe_name}\"\n---\n\n# {name}\n\n## Instructions\n\n{instructions}\n"
            
            out_file = os.path.join(out_dir, f"{safe_name}.md")
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(md_content)
        print(f"Processed {len(matches)} Gemini Gems.")
    else:
        print("Gemini Gems data not found.")

def parse_notebooklm():
    nl_dir = os.path.join(TAKEOUT_DIR, "NotebookLM")
    if not os.path.exists(nl_dir):
        print("NotebookLM directory not found.")
        return
        
    for nb_name in os.listdir(nl_dir):
        nb_path = os.path.join(nl_dir, nb_name)
        if not os.path.isdir(nb_path):
            continue
            
        print(f"Processing Notebook: {nb_name}")
        safe_nb_name = fix_filename(nb_name)
        
        out_nb_dir = os.path.join(WIKI_EXPORT_DIR, safe_nb_name)
        out_sources_dir = os.path.join(out_nb_dir, "Sources")
        os.makedirs(out_sources_dir, exist_ok=True)
        
        sources_path = os.path.join(nb_path, "Sources")
        if not os.path.exists(sources_path):
            continue
            
        html_files = [f for f in os.listdir(sources_path) if f.lower().endswith(".html")]
        json_files = [f for f in os.listdir(sources_path) if f.lower().endswith(".json")]
        
        count = 0
        toc_lines = [f"# {safe_nb_name} Map of Content\n", "\n## Sources\n"]
        
        for h_file in html_files:
            h_base = os.path.splitext(h_file)[0]
            
            meta_json = None
            for jf in json_files:
                j_base = os.path.splitext(jf)[0]
                j_base_cleaned = j_base.replace(" metadata", "").strip()
                if h_base.startswith(j_base_cleaned[:15]) or j_base_cleaned.startswith(h_base[:15]):
                    meta_json = os.path.join(sources_path, jf)
                    break
                    
            frontmatter = {"type": "notebook_source", "notebook": safe_nb_name}
            title = h_base
            
            if meta_json and os.path.exists(meta_json):
                try:
                    with open(meta_json, 'r', encoding='utf-8', errors='replace') as jf:
                        jdata = json.load(jf)
                        if "title" in jdata:
                            title = jdata["title"]
                        if "metadata" in jdata:
                            md = jdata["metadata"]
                            if "originalSourceContentType" in md:
                                frontmatter["source_type"] = md["originalSourceContentType"]
                            if "sourceAddedTimestamp" in md:
                                frontmatter["added"] = md["sourceAddedTimestamp"]
                            if "youtubeMetadata" in md:
                                frontmatter["youtube_id"] = md["youtubeMetadata"].get("videoId", "")
                                frontmatter["youtube_channel"] = md["youtubeMetadata"].get("channelName", "")
                except Exception as e:
                    print(f"  Error reading JSON {meta_json}: {e}")
            
            # Clean title
            frontmatter["title"] = title.replace('"', '')
            
            h_path = os.path.join(sources_path, h_file)
            with open(h_path, 'r', encoding='utf-8', errors='replace') as f:
                h_content = f.read()
            text_content = clean_html(h_content)
            
            # Yaml formatting
            yaml_lines = ["---"]
            for k, v in frontmatter.items():
                v_str = str(v).replace('"', '')
                yaml_lines.append(f'{k}: "{v_str}"')
            yaml_lines.append("---")
            yaml_str = "\n".join(yaml_lines)
            
            # Output Markdown
            safe_title = fix_filename(title)
            if len(safe_title) > 80: safe_title = safe_title[:80]
            
            md_content = f"{yaml_str}\n\n# {title}\n\n{text_content}\n"
            
            out_file = os.path.join(out_sources_dir, f"{safe_title}.md")
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(md_content)
                
            toc_lines.append(f"- [[{safe_title}]]")
            count += 1
            
        chat_history_path = os.path.join(nb_path, "Chat History")
        out_chats_dir = os.path.join(out_nb_dir, "Chats")
        
        chat_count = 0
        if os.path.exists(chat_history_path):
            os.makedirs(out_chats_dir, exist_ok=True)
            chat_files = [f for f in os.listdir(chat_history_path) if f.lower().endswith(".html")]
            if chat_files:
                toc_lines.append("\n## Chat History\n")
            for c_file in chat_files:
                c_base = os.path.splitext(c_file)[0]
                c_path = os.path.join(chat_history_path, c_file)
                with open(c_path, 'r', encoding='utf-8', errors='replace') as f:
                    c_content = f.read()
                
                text_content = clean_html(c_content)
                text_content = re.sub(r'USER:', '\n**User:**\n', text_content)
                text_content = re.sub(r'MODEL:', '\n**NotebookLM:**\n', text_content)
                
                frontmatter = {"type": "notebook_chat", "notebook": safe_nb_name, "title": c_base.replace('"', '')}
                yaml_lines = ["---"]
                for k, v in frontmatter.items():
                    yaml_lines.append(f'{k}: "{str(v)}"')
                yaml_lines.append("---")
                yaml_str = "\n".join(yaml_lines)
                
                safe_title = fix_filename(c_base)
                if len(safe_title) > 80: safe_title = safe_title[:80]
                
                md_content = f"{yaml_str}\n\n# {c_base}\n\n{text_content}\n"
                
                out_file = os.path.join(out_chats_dir, f"{safe_title}.md")
                with open(out_file, 'w', encoding='utf-8') as f:
                    f.write(md_content)
                    
                toc_lines.append(f"- [[{safe_title}]]")
                chat_count += 1
                
        index_file = os.path.join(out_nb_dir, "_Index.md")
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(toc_lines))
        print(f"  Saved {count} sources and {chat_count} chats.")

if __name__ == "__main__":
    print(f"Starting parsing from {TAKEOUT_DIR}")
    os.makedirs(WIKI_EXPORT_DIR, exist_ok=True)
    process_gemini()
    parse_notebooklm()
    print(f"Finished parsing. Content written to {WIKI_EXPORT_DIR}")
