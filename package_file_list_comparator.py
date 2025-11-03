import os

# file_a와 file_b에 작성된 '경로+파일명+확장자'를 비교하여 한쪽 파일에만 있는 정보들을 정리
def compare_file_lists(file_a, file_b, report_file):
    with open(file_a, "r", encoding="utf-8") as fa:
        set_a = set(line.strip() for line in fa if line.strip())

    with open(file_b, "r", encoding="utf-8") as fb:
        set_b = set(line.strip() for line in fb if line.strip())

    only_in_a = sorted(set_a - set_b)
    only_in_b = sorted(set_b - set_a)

    with open(report_file, "w", encoding="utf-8") as f:
        f.write("=== A에만 존재하는 파일 ===\n")
        for path in only_in_a:
            f.write(path + "\n")

        f.write("\n=== B에만 존재하는 파일 ===\n")
        for path in only_in_b:
            f.write(path + "\n")

    print(f"✅ 비교 결과가 '{report_file}' 에 저장되었습니다.")


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fileA = os.path.join(current_dir, "package_file_list_reporter_output_A.txt")  # 파일명은 package_file_list_reporter_output_A 로 작성 필요
    fileB = os.path.join(current_dir, "package_file_list_reporter_output_B.txt")  # 파일명은 package_file_list_reporter_output_B 로 작성 필요
    reportFile = os.path.join(current_dir, "package_file_list_comparator_output.txt")
    compare_file_lists(fileA, fileB, reportFile)