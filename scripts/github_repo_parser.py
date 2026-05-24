import os
import sys
import shutil
import subprocess
import glob

# 설정
TARGET_BASE_DIR = r"c:\Python\wiki\My_Wiki\LLM-Wiki\GithubRepos"
TEMP_DIR = r"c:\Python\wiki\scripts\temp_repo"

# 무시할 디렉토리 및 확장자
SKIP_DIRS = {".git", "node_modules", "dist", "build", ".venv", "venv", "__pycache__", ".idea", ".vscode", "coverage"}
SKIP_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".mp4", ".mov", ".zip", ".tar", ".gz", ".pdf", ".exe", ".dll", ".so", ".dylib", ".woff", ".ttf", ".eot"}

def is_text_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            f.read(1024)
        return True
    except UnicodeDecodeError:
        return False
    except Exception:
        return False

def get_language_from_ext(ext):
    ext_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.jsx': 'jsx',
        '.tsx': 'tsx',
        '.json': 'json',
        '.html': 'html',
        '.css': 'css',
        '.sh': 'bash',
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.md': 'markdown',
        '.xml': 'xml',
        '.java': 'java',
        '.c': 'c',
        '.cpp': 'cpp',
        '.h': 'c',
        '.hpp': 'cpp',
        '.go': 'go',
        '.rs': 'rust',
        '.rb': 'ruby',
        '.php': 'php',
        '.sql': 'sql'
    }
    return ext_map.get(ext.lower(), '')

def parse_repo(repo_url):
    # 1. 레포지토리 이름 추출
    repo_name = repo_url.rstrip('/').split('/')[-1]
    if repo_name.endswith('.git'):
        repo_name = repo_name[:-4]

    target_repo_dir = os.path.join(TARGET_BASE_DIR, repo_name)
    os.makedirs(target_repo_dir, exist_ok=True)

    print(f"Cloning {repo_url} into temp catalog...")
    
    # 기존 temp 폴더 안전 삭제
    if os.path.exists(TEMP_DIR):
        try:
            shutil.rmtree(TEMP_DIR, ignore_errors=True)
        except Exception as e:
            print(f"Warning: could not force remote temp_dir: {e}")

    try:
        subprocess.run(["git", "clone", "--depth", "1", repo_url, TEMP_DIR], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository: {e}")
        return

    print(f"Processing and converting files into Markdown structures...")
    
    local_toc = [f"# 📦 Github Repository: {repo_name}\n", f"URL: [{repo_url}]({repo_url})\n"]
    
    for root, dirs, files in os.walk(TEMP_DIR):
        # 무시 디렉토리 제외
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in SKIP_EXTS:
                continue

            src_file_path = os.path.join(root, file)
            
            # 텍스트 파일이 아닌 경우 (바이너리 등) 건너뛰기
            if not is_text_file(src_file_path):
                continue
                
            rel_path = os.path.relpath(src_file_path, TEMP_DIR)
            rel_dir = os.path.dirname(rel_path)
            
            dst_root = os.path.join(target_repo_dir, rel_dir)
            os.makedirs(dst_root, exist_ok=True)
            
            # 마크다운 포장명으로 파일 생성
            # 기존 마크다운 파일은 내용이 중복 마크다운 블록이 될수 있지만 카파시식 구조화를 위해 일관성 유지
            dst_file_path = os.path.join(dst_root, f"{file}.md")
            
            try:
                with open(src_file_path, 'r', encoding='utf-8') as sf:
                    content = sf.read()
                    
                language = get_language_from_ext(ext)
                
                with open(dst_file_path, 'w', encoding='utf-8') as df:
                    df.write(f"---\n")
                    df.write(f"type: github_repo\n")
                    df.write(f"repo: {repo_name}\n")
                    df.write(f"file: {rel_path.replace(chr(92), '/')}\n")
                    df.write(f"---\n\n")
                    df.write(f"# {rel_path.replace(chr(92), '/')}\n\n")
                    
                    df.write(f"```{language}\n")
                    df.write(content)
                    if not content.endswith('\n'):
                        df.write("\n")
                    df.write(f"```\n")
                    
                local_toc.append(f"- 📄 [[{file}.md|{rel_path.replace(chr(92), '/')}]]")
            except Exception as e:
                print(f"Failed to process {src_file_path}: {e}")

    # Master index 파일 생성
    index_path = os.path.join(target_repo_dir, "_Index.md")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(local_toc))

    # 임시 폴더 삭제
    print("Cleaning up temporary files...")
    shutil.rmtree(TEMP_DIR, ignore_errors=True)
    
    print(f"Success! Repository {repo_name} has been structurally indexed into {target_repo_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python github_repo_parser.py <github_repo_url>")
        sys.exit(1)
        
    repo_url = sys.argv[1]
    parse_repo(repo_url)
