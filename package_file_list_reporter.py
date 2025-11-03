import os

# base_path 경로 이하이 모든 파일에 대해서 '경로+파일명+확장자' 형태로 output_file에 저장
def save_all_files(base_path, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk(base_path):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_path)  # 상대경로로 저장
                f.write(rel_path + "\n")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_dir, "package_file_list_reporter_output.txt")     # package_file_list_output.txt로 저장
    save_all_files(current_dir, output_path)
    print(f"✅ 파일 목록이 '{output_path}' 에 저장되었습니다.")