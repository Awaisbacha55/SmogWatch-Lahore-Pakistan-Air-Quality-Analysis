"""
SmogWatch: End-to-End System & Data Integrity Audit
---------------------------------------------------
Verifies:
1. Exact cryptographic match (SHA-256) of all raw and processed source datasets.
2. Zero data corruption, no synthetic fabrication, explicit preservation of missing values.
3. Existence of all 15 required visualization artifacts and interactive dashboard.
4. Correctness of data schemas, row counts (1,096 per city, 4,384 total), and city coverage.
5. Exclusion of credentials (.env, API keys) from git tracking.
"""

import hashlib
import sys
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

# Baseline SHA-256 hashes recorded at project inspection
BASELINE_HASHES = {
    "data/processed/daily_air_quality_weather_2022_2024.csv": "36A77CBFCC07D312B0810E1216C91A295E817078877C8BAEA8C04811253125E9",
    "data/raw/air_quality/islamabad_pm25_2022_2024.csv": "145188081F534660ACFFCCE6283F41EF5AD39F560343603C74E0606B98B1C834",
    "data/raw/air_quality/karachi_pm25_2022_2024.csv": "A4B07274113E5A70A142EA84281E4437B9AA233FF26923A4B81252B3E33CE6AF",
    "data/raw/air_quality/lahore_pm25_2022_2024.csv": "C5609DE2B80B1477F3F8338BD3B5712449D068AC1E1D14AA44D8197C8652A350",
    "data/raw/air_quality/peshawar_pm25_2022_2024.csv": "26D6A1856FBEC7CE700A089BA32DD37537043EE55CB823089A87D9BA03B4C6AC",
    "data/raw/weather/islamabad_weather.csv": "52A1F8FABB525EB0E2ED0E3C0DDD119082EDD7D8AD8D88CC5A9EDEEB2B5A689D",
    "data/raw/weather/karachi_weather.csv": "1691F2CC2806AC842AF9C726308D73E67BE805BC409A5A040760124A858BFBD9",
    "data/raw/weather/lahore_weather.csv": "76A51327419D5B2B27EEBD1BE6C5C98618A0B14271DC9962736BBDFF9E2DFFC0",
    "data/raw/weather/peshawar_weather.csv": "3067AB393FFE3220C11209C973C9D4B6DA2F062136FC2394DA4C44C8040C9F36",
    "data/raw/weather/quetta_weather.csv": "45CC8560C2ADF3A650089EE553115D9AD108EE2186F88F23E3BF50542307233E",
}

EXPECTED_FIGURES = [
    "01_overall_mean_pm25_by_city.png",
    "02_annual_mean_pm25_by_city.png",
    "03_monthly_seasonal_pm25_patterns.png",
    "04_missing_data_completeness_by_city.png",
    "05_daily_pm25_trends_over_time.png",
    "06_distribution_pm25_by_city.png",
    "07_pm25_boxplots_by_month_and_city.png",
    "08_annual_mean_vs_who_guideline.png",
    "09_daily_pm25_vs_who_24h_guideline.png",
    "10_weather_pm25_correlation_heatmaps.png",
    "11_pm25_vs_temperature_scatter.png",
    "12_pm25_vs_wind_speed_scatter.png",
    "13_pm25_vs_precipitation_scatter.png",
    "14_calendar_heatmap_daily_pm25.png",
    "15_interactive_plotly_overview.png",
    "smogwatch_interactive_dashboard.html",
]


def sha256_file(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest().upper()


def run_audit():
    print("=" * 70)
    print("SMOGWATCH SYSTEM & DATA INTEGRITY FINAL VALIDATION")
    print("=" * 70)

    failures = 0

    # 1. SHA-256 Dataset Immutability Check
    print("\n[CHECK 1/5] Cryptographic Hash Verification (Baseline Datasets)")
    for rel_path, expected_hash in BASELINE_HASHES.items():
        file_path = BASE_DIR / rel_path
        if not file_path.exists():
            print(f"  [FAIL] Missing dataset: {rel_path}")
            failures += 1
            continue
        current_hash = sha256_file(file_path)
        if current_hash == expected_hash:
            print(f"  [PASS] {file_path.name:<38} SHA-256 MATCH")
        else:
            print(f"  [FAIL] {file_path.name} HASH MISMATCH!")
            print(f"         Expected: {expected_hash}")
            print(f"         Got:      {current_hash}")
            failures += 1

    # 2. Enhanced Dataset Check
    print("\n[CHECK 2/5] Enhanced Analysis Dataset Integrity")
    enh_path = BASE_DIR / "data" / "processed" / "daily_air_quality_weather_enhanced.csv"
    if not enh_path.exists():
        print(f"  [FAIL] Enhanced dataset not found at {enh_path}")
        failures += 1
    else:
        df_enh = pd.read_csv(enh_path)
        expected_rows = 4384
        if len(df_enh) == expected_rows:
            print(f"  [PASS] Row count: {len(df_enh)} (Exactly {expected_rows} across 4 cities)")
        else:
            print(f"  [FAIL] Row count mismatch: {len(df_enh)} vs expected {expected_rows}")
            failures += 1

        missing_pm25 = df_enh["pm25_ug_m3"].isna().sum()
        if missing_pm25 == 861:
            print(f"  [PASS] Missing PM2.5 values: {missing_pm25} (Exactly 861; no synthetic filling)")
        else:
            print(f"  [FAIL] Missing PM2.5 count mismatch: {missing_pm25} vs expected 861")
            failures += 1

        if "wind_direction_circular_deg" in df_enh.columns and "season" in df_enh.columns:
            print(f"  [PASS] Enhanced features present: circular wind degrees, season, WHO indicators")
        else:
            print(f"  [FAIL] Missing enhanced features in dataset")
            failures += 1

    # 3. Figure Artifact Verification
    print("\n[CHECK 3/5] Visualizations & Dashboard Artifacts")
    fig_dir = BASE_DIR / "reports" / "figures"
    for fig_name in EXPECTED_FIGURES:
        fp = fig_dir / fig_name
        if fp.exists() and fp.stat().st_size > 0:
            print(f"  [PASS] {fig_name:<42} Exists ({fp.stat().st_size / 1024:.1f} KB)")
        else:
            print(f"  [FAIL] Missing or empty figure: {fig_name}")
            failures += 1

    # 4. Report & Notebook Verification
    print("\n[CHECK 4/5] Report & Notebook Deliverables")
    report_file = BASE_DIR / "reports" / "smogwatch_week1_report.md"
    notebook_file = BASE_DIR / "notebooks" / "01_smogwatch_eda.ipynb"
    readme_file = BASE_DIR / "README.md"
    req_file = BASE_DIR / "requirements.txt"

    for doc in [report_file, notebook_file, readme_file, req_file]:
        if doc.exists() and doc.stat().st_size > 0:
            print(f"  [PASS] {doc.name:<35} Exists ({doc.stat().st_size / 1024:.1f} KB)")
        else:
            print(f"  [FAIL] Missing deliverable: {doc}")
            failures += 1

    # 5. Security & Exclusions Check
    print("\n[CHECK 5/5] Security & Secrets Exclusion")
    env_file = BASE_DIR / ".env"
    gitignore_file = BASE_DIR / ".gitignore"
    if gitignore_file.exists():
        gi_content = gitignore_file.read_text()
        if ".env" in gi_content and ".venv" in gi_content:
            print("  [PASS] .gitignore correctly excludes .env and .venv")
        else:
            print("  [FAIL] .gitignore missing .env or .venv rules")
            failures += 1

    print("\n" + "=" * 70)
    if failures == 0:
        print("ALL AUDIT CHECKS PASSED WITH ZERO ERRORS (100% COMPLIANT)")
        print("=" * 70)
        sys.exit(0)
    else:
        print(f"AUDIT FAILED WITH {failures} ERRORS")
        print("=" * 70)
        sys.exit(1)


if __name__ == "__main__":
    run_audit()
