# -*- coding: utf-8 -*-
"""
released_module.txt 에서 이름 존재 여부를 확인하는 스크립트
사용법:
1. 아래 names 리스트를 직접 수정하여 검사할 이름들을 적으세요.
2. 동일 경로에 released_module.txt 파일을 둡니다.
3. python released_module_reviewer.py 실행 시
   -> released_module_reviewer.txt 가 생성됩니다.
"""

# 📝 사용자가 직접 편집하는 부분
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
    # 여기에 원하는 이름들을 추가하세요.
]

# -----------------------------------------------------
import os

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_path, "released_module.txt")
    output_path = os.path.join(base_path, "released_module_reviewer_output.txt")

    if not os.path.exists(input_path):
        print(f"[ERROR] released_module.txt 파일이 존재하지 않습니다: {input_path}")
        return

    # component_summary.txt 내용 읽기
    with open(input_path, "r", encoding="utf-8") as f:
        summary_lines = f.read().splitlines()

    # 보고서 생성
    results = []
    for name in names:
        found = any(name in line for line in summary_lines)
        status = "exist" if found else "not exist"
        results.append(f"{name} : {status}")

    # 결과 파일 쓰기
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(results))

    print(f"[INFO] 완료! 결과 파일 생성됨: {output_path}")

if __name__ == "__main__":
    main()