#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
released_module.txt 에서 names 리스트에 따른 존재 여부를 검사하고,
names에 포함되지 않은 라인들은 new 로 표시하여 출력하는 스크립트.

사용법:
1. names 리스트를 수정해 검사할 키워드를 추가/삭제하세요.
2. released_module.txt 파일을 스크립트와 같은 폴더에 넣으세요.
3. python released_module_reviewer.py 실행 -> released_module_reviewer_output.txt 생성
"""

import os

# --- 사용자가 편집하는 부분: 검사할 키워드들 ---
names = [
    "hive-ui-languagepack",
    "hive-push-amazon-adm",
    "hive-authv4-google-recaptcha",
    "hive-datastore",
    "hive-authv4-google-inappupdate",
    "hive-authv4-provider-steam",
    "hive-authv4-provider-line",
    "hive-authv4-provider-google-credential-signin",
    "hive-iapv4-market-onestore",
    "hive-promotion",
    "hive-iapv4-market-huawei",
    "hive-hercules",
    "hive-authv4-provider-wechat",
    "hive-iapv4-market-onestore-v4",
    "hive-core",
    "hive-protocol",
    "hive-iapv4-market-amazon",
    "hive-authv4-provider-x",
    "hive-authv4-identity-verification",
    "hive-sdk-bom",
    "hive-analytics-provider-singular",
    "hive-authv4-provider-huawei",
    "hive-authv4-provider-hive-membership",
    "hive-authv4-provider-google-signin",
    "hive-iapv4",
    "hive-authv4-provider-apple-signin",
    "hive-push-google-fcm",
    "hive-analytics-provider-adjust",
    "hive-authv4-provider-weverse",
    "hive-iapv4-market-samsung",
    "hive-authv4-provider-telegram",
    "hive-analytics-consent-mode",
    "hive-iapv4-market-google",
    "hive-analytics-provider-firebase",
    "hive-service-google-base",
    "hive-authv4-provider-facebook",
    "hive-plugin-c2s",
    "hive-promotion-google-inappreview",
    "hive-analytics-provider-appsflyer",
    "hive-authv4-provider-google-playgames",
    "hive-analytics-provider-airbridge",
    "hive-chat",
    "hive-authv4-real-name-verification",
    "hive-authv4-provider-vk",
    "hive-matchmaking",
    "hive-plugin-java",
    "hive-ui",
    "hive-iapv4-base",
    "hive-authv4-provider-qq",
    "hive-iapv4-market-hivestore",
    "hive-authv4-adult-confirm",
    "hive-service",
    "hive-iapv4-repayment",
    "hive-iapv4-market-lebi",
    "hive-authv4-device-management",
    "hive-sdk",
    # 필요하면 더 추가하세요.
]

# -----------------------------------------------------

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_path, "released_module.txt")
    output_path = os.path.join(base_path, "released_module_reviewer_output.txt")

    if not os.path.exists(input_path):
        print(f"[ERROR] released_module.txt 파일이 존재하지 않습니다: {input_path}")
        return

    # 입력 파일의 모든 라인 읽기 (양 끝 공백 제거, 빈 라인 무시)
    with open(input_path, "r", encoding="utf-8") as f:
        raw_lines = f.read().splitlines()
    lines = [ln.strip() for ln in raw_lines if ln.strip() != ""]

    # names 별로 존재 여부 검사
    name_results = []
    for name in names:
        found = any(name in line for line in lines)
        status = "exist" if found else "not exist"
        name_results.append(f"{name} : {status}")

    # names 중 어떤 키워드도 포함하지 않는 라인들 찾기
    unmatched_lines = []
    for line in lines:
        if not any(name in line for name in names):
            unmatched_lines.append(line)

    # 출력 파일 작성 (두 섹션으로 구분)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("=== Names existence ===\n")
        for r in name_results:
            f.write(r + "\n")

        f.write("\n=== New lines (no matching names) ===\n")
        if unmatched_lines:
            # 중복 제거하면서 순서 유지
            seen = set()
            for ln in unmatched_lines:
                if ln not in seen:
                    seen.add(ln)
                    f.write(f"{ln} : new\n")
        else:
            f.write("(no new lines)\n")

    print(f"[INFO] 완료! 결과 파일 생성됨: {output_path}")

if __name__ == "__main__":
    main()