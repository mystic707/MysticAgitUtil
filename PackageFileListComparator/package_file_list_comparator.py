#!/usr/bin/env python3
import os
import sys

# ---------------------------
# 기본 하드코딩된 경로 (파라미터 없을 때 사용)
# ---------------------------
DEFAULT_PATH_A = "/Users/jschoi/UnityTestProjects/2022_3_67_Hive26_0_0_packagetest/Assets"
DEFAULT_PATH_B = "/Users/jschoi/PlatformClientGit/HIVE-SDK-Manager/Assets"


def get_all_paths(root_path):
    """
    root_path 아래 모든 파일 & 빈 폴더를 수집해서 리스트 반환.
    - 파일:  "dir/file.ext"
    - 폴더:  "dir/"   (폴더가 비었을 때만)
    """
    collected = []

    for current_root, dirs, files in os.walk(root_path):
        # 상대 경로 계산
        rel_root = os.path.relpath(current_root, root_path).replace(os.sep, '/')

        # 최상위 디렉토리(".")는 생략
        if rel_root == ".":
            rel_root = ""

        # 1) 빈 폴더 체크
        if len(files) == 0 and len(dirs) == 0:
            # 빈 폴더만 기록
            folder_path = rel_root + "/" if rel_root else ""
            if folder_path:
                collected.append(folder_path)

        # 2) 파일 처리
        for f in files:
            file_path = os.path.join(rel_root, f).replace(os.sep, '/')
            collected.append(file_path)

    return sorted(collected)


def write_list_to_file(file_path, items):
    with open(file_path, "w", encoding="utf-8") as f:
        for item in items:
            f.write(item + "\n")


def main():
    # ---------------------------
    # 1. 파라미터 처리
    # ---------------------------
    if len(sys.argv) >= 3:
        path_a = sys.argv[1]
        path_b = sys.argv[2]
        print(f"[INFO] 파라미터 입력 감지 → A={path_a}, B={path_b}")
    else:
        path_a = DEFAULT_PATH_A
        path_b = DEFAULT_PATH_B
        print("[INFO] 파라미터 없음 → 하드코딩된 기본 경로 사용")
        print(f"A={path_a}")
        print(f"B={path_b}")

    # ---------------------------
    # 2. 파일+빈폴더 리스트 수집
    # ---------------------------
    list_a = get_all_paths(path_a)
    list_b = get_all_paths(path_b)

    write_list_to_file("package_file_list_output_path_A.txt", list_a)
    write_list_to_file("package_file_list_output_path_B.txt", list_b)

    print("[INFO] A/B 리스트 파일 생성 완료")

    # ---------------------------
    # 3. 비교 결과 작성
    # ---------------------------
    set_a = set(list_a)
    set_b = set(list_b)

    only_in_a = sorted(set_a - set_b)
    only_in_b = sorted(set_b - set_a)

    result_path = "package_file_list_output_result.txt"

    with open(result_path, "w", encoding="utf-8") as f:
        f.write("===== A 경로에만 있는 파일/폴더 리스트 =====\n")
        f.write("> A : " + path_a + "\n")
        if only_in_a:
            for item in only_in_a:
                f.write(item + "\n")
        else:
            f.write("(없음)\n")

        f.write("\n===== B 경로에만 있는 파일/폴더 리스트 =====\n")
        f.write("> B : " + path_b + "\n")
        if only_in_b:
            for item in only_in_b:
                f.write(item + "\n")
        else:
            f.write("(없음)\n")

    print(f"[INFO] 비교 결과가 '{result_path}' 로 생성되었습니다.")


if __name__ == "__main__":
    main()