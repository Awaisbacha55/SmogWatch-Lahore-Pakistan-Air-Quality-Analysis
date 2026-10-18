# SmogWatch: Lahore & Pakistan Air Quality Analysis (2022–2024)

> ### 🌐 Live Published Project Links
> - **Live Web Report (Published Online):** [https://awaisbacha55.github.io/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis/](https://awaisbacha55.github.io/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis/)
> - **Live Interactive Plotly Dashboard:** [https://awaisbacha55.github.io/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis/figures/smogwatch_interactive_dashboard.html](https://awaisbacha55.github.io/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis/figures/smogwatch_interactive_dashboard.html)
> - **Source Code Repository:** [https://github.com/Awaisbacha55/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis](https://github.com/Awaisbacha55/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis)

[![Live Web Report](https://img.shields.io/badge/Live%20Report-GitHub%20Pages-blue.svg)](https://awaisbacha55.github.io/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis/)
[![Live Dashboard](https://img.shields.io/badge/Live%20Dashboard-Interactive%20Plotly-green.svg)](https://awaisbacha55.github.io/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis/figures/smogwatch_interactive_dashboard.html)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Hourly Surveillance](https://img.shields.io/badge/Hourly%20Records-105%2C216%20Synchronized-purple.svg)](#diurnal-boundary-layer-dynamics)
[![Data Protection: Verified](https://img.shields.io/badge/Data%20Protection-SHA256%20Verified-brightgreen.svg)](#data-protection--integrity-rules)
[![WHO Guideline Benchmarking](https://img.shields.io/badge/WHO%202021-AQG%20Benchmarked-red.svg)](#who-guideline-comparisons)

A rigorous, reproducible data science surveillance project analyzing ground-level fine particulate matter ($\text{PM}_{2.5}$) and historical meteorology across four major Pakistani cities (**Lahore**, **Karachi**, **Islamabad**, and **Peshawar**) over a complete 3-year observational window (1 January 2022 to 31 December 2024). Includes **105,216 synchronized hourly observations** capturing diurnal boundary layer cycles.

---

## Table of Contents
- [Problem Statement](#problem-statement)
- [Research Questions](#research-questions)
- [Key Empirical Findings](#key-empirical-findings)
- [Project Architecture & Folder Structure](#project-architecture--folder-structure)
- [Data Sources & Sensor Identifiers](#data-sources--sensor-identifiers)
- [Data Protection & Integrity Rules](#data-protection--integrity-rules)
- [Technologies & Libraries](#technologies--libraries)
- [Installation & Quickstart](#installation--quickstart)
- [Reproducibility Workflow](#reproducibility-workflow)
  - [1. Data Validation](#1-data-validation)
  - [2. Daily & Hourly Feature Enhancement](#2-daily--hourly-feature-enhancement)
  - [3. Figure & Dashboard Generation](#3-figure--dashboard-generation)
  - [4. Exploratory Notebook](#4-exploratory-notebook)
- [Generated Visualizations (Figures 01–19)](#generated-visualizations)
- [Data Quality, Sensor Limits & Limitations](#data-quality-sensor-limits--limitations)
- [Correlation vs. Causation Caveat](#correlation-vs-causation-caveat)
- [Project Publication & Deployment Status](#project-publication--deployment-status)
- [References & Citations](#references--citations)

---

## Problem Statement

Pakistan's urban centres, particularly within the Indus River Plain and the Peshawar basin, endure some of the most hazardous air pollution levels on Earth. Each autumn and winter, millions of citizens are exposed to dense, toxic smog laden with respirable particulates ($\text{PM}_{2.5}$), leading to severe cardiorespiratory illnesses, school closures, airport disruptions, and shortened life expectancy. 

Despite public awareness, rigorous empirical analysis linking ground monitoring records with high-resolution meteorology has often been hindered by fragmented data, sensor saturation, and observational gaps. **SmogWatch** provides a transparent, scientifically validated surveillance system that preserves observational reality without fabricating data or conflating physical $\text{PM}_{2.5}$ concentration ($\mu\text{g/m}^3$) with dimensionless Air Quality Index (AQI) scales.

---

## Research Questions

1. **Baseline Levels:** What are the empirical daily, annual, and overall mean and median $\text{PM}_{2.5}$ concentrations in Lahore, Peshawar, Karachi, and Islamabad?
2. **Seasonality:** How acute is the winter "smog season" (October–February) compared to the summer monsoon period?
3. **Completeness:** What proportion of the 1,096-day calendar window is covered by valid measurements versus missing values inside records or completely omitted dates?
4. **Meteorological Interactions:** How do ambient temperature, relative humidity, wind speed, circular wind direction, and precipitation correlate with daily particulate concentrations?
5. **WHO Compliance:** How do observed concentrations compare against the World Health Organization (WHO) 2021 air quality guidelines and interim target benchmarks?
6. **Diurnal 24-Hour Dynamics:** What atmospheric boundary layer mechanisms dictate the diurnal (hourly) rise and fall of particulate matter?

---

## Key Empirical Findings

All findings are derived directly from the validated 4,384 city-day dataset and 105,216 synchronized hourly observations:

1. **Lahore's Chronic Particulate Crisis:** Lahore recorded an overall mean $\text{PM}_{2.5}$ of **$131.84\ \mu\text{g/m}^3$** (median $89.95\ \mu\text{g/m}^3$, $n=852$), exceeding the WHO annual guideline ($5\ \mu\text{g/m}^3$) by **$26.4\times$**. In 2024, Lahore's annual mean peaked at **$141.62\ \mu\text{g/m}^3$** ($28.3\times$ WHO guideline).
2. **Peshawar Multi-Year Increase:** Peshawar's annual average concentration rose steadily across the 3-year study period: **$83.08\ \mu\text{g/m}^3$** (2022) $\rightarrow$ **$91.23\ \mu\text{g/m}^3$** (2023) $\rightarrow$ **$98.75\ \mu\text{g/m}^3$** (2024), representing a cumulative **$18.9\%$ increase**.
3. **Severe Winter Smog Escalation:** In Lahore, winter (Dec–Feb) mean $\text{PM}_{2.5}$ averaged **$223.68\ \mu\text{g/m}^3$** (median $214.00\ \mu\text{g/m}^3$), compared to a summer monsoon (Jun–Aug) trough of **$55.55\ \mu\text{g/m}^3$**—a **$4.03\times$ seasonal surge**.
4. **Catastrophic Non-Compliance with Daily WHO Benchmarks:** Over **$99.3\%$** of monitored days in Lahore (846 of 852 valid days) and **$99.2\%$** in Peshawar (973 of 981 days) breached the WHO 24-hour guideline of $15\ \mu\text{g/m}^3$. In Lahore, **$58.7\%$ of days (500 days)** exceeded even the lenient WHO Interim Target 1 ($75\ \mu\text{g/m}^3$).
5. **Thermal Inversion & Stagnation Modulations:** Particulate levels correlate strongly and negatively with daily temperature in Lahore ($r = -0.608$), Islamabad ($r = -0.584$), and Karachi ($r = -0.453$), and negatively with wind speed ($r = -0.453$ in Lahore; Spearman $\rho = -0.591$ in Karachi). High-pollution episodes (>150 $\mu\text{g/m}^3$) occur almost exclusively during low wind speeds (<8 km/h).
6. **Precipitation Scavenging:** Across all cities, rainfall exhibits consistent negative rank correlation with $\text{PM}_{2.5}$ (Spearman $\rho = -0.45$ to $-0.50$). Median $\text{PM}_{2.5}$ on wet days (>0.5 mm) dropped by **$47.8\%$** relative to dry days.
7. **Diurnal Planetary Boundary Layer Dynamics (Hourly Analysis):** Analysis of 105,216 hourly records shows a sharp bimodal diurnal curve. Particulate concentrations peak overnight between 22:00 and 06:00 ($153.19\ \mu\text{g/m}^3$ in Lahore) during nocturnal temperature inversions, dropping by **$34.9\%$** in the afternoon (11:00–16:00, $99.77\ \mu\text{g/m}^3$) when solar warming expands vertical boundary layer mixing.

---

## Project Architecture & Folder Structure

```
SmogWatch/
├── .github/
│   └── workflows/
│       └── deploy-pages.yml                   # Automated GitHub Actions deployment to GitHub Pages
├── .env.example                               # Template for OpenAQ API configuration
├── .gitignore                                 # Git exclusions (.env, .venv, caches, temp files)
├── README.md                                  # Master project documentation
├── requirements.txt                           # Pinned Python package dependencies
├── validate_weather.py                        # Root weather verification entrypoint
├── docs/                                      # Online Web Report for GitHub Pages
│   ├── index.html                             # Publication-grade styled online report
│   └── figures/                               # Web-optimized figures & interactive dashboard
├── data/
│   ├── processed/
│   │   ├── daily_air_quality_weather_2022_2024.csv   # IMMUTABLE baseline processed dataset
│   │   ├── daily_air_quality_weather_enhanced.csv    # Enhanced dataset (circular wind, features)
│   │   └── hourly_air_quality_weather_2022_2024.csv  # Harmonized 105,216 hourly observations
│   └── raw/
│       ├── air_quality/                       # Original OpenAQ daily PM2.5 CSV files (READ-ONLY)
│       │   ├── hourly/                        # Downloaded OpenAQ hourly PM2.5 CSV files
│       │   ├── islamabad_pm25_2022_2024.csv
│       │   ├── karachi_pm25_2022_2024.csv
│       │   ├── lahore_pm25_2022_2024.csv
│       │   └── peshawar_pm25_2022_2024.csv
│       └── weather/                           # Original Open-Meteo hourly weather CSVs (READ-ONLY)
│           ├── islamabad_weather.csv
│           ├── karachi_weather.csv
│           ├── lahore_weather.csv
│           ├── peshawar_weather.csv
│           └── quetta_weather.csv
├── notebooks/
│   └── 01_smogwatch_eda.ipynb                 # Reproducible Jupyter exploratory notebook (executed)
├── reports/
│   ├── smogwatch_week1_report.md              # 20-section publication-grade Data Story report
│   └── figures/                               # 18 high-res publication figures & dashboard
│       ├── 01_overall_mean_pm25_by_city.png
│       ├── ...
│       ├── 16_diurnal_pm25_profiles_by_city.png
│       ├── 17_seasonal_diurnal_contrast.png
│       ├── 18_meteorology_vs_pm25_diurnal.png
│       └── smogwatch_interactive_dashboard.html
└── scripts/
    ├── build_executed_notebook.py             # Verified end-to-end notebook runner
    ├── build_online_report.py                 # Generates docs/index.html for GitHub Pages
    ├── check_flag_details.py                  # API diagnostic for extreme flag metadata
    ├── check_sensor_history.py                # Telemetry operational window inspector
    ├── create_charts.py                       # Daily visualization suite (Figures 01–15)
    ├── create_hourly_charts.py                # Hourly diurnal visualization suite (Figures 16–18)
    ├── download_hourly_pm25.py                # OpenAQ v3 hourly downloader
    ├── download_pm25.py                       # Daily air quality ingestion script (PROTECTED)
    ├── download_weather.py                    # Open-Meteo ingestion script (PROTECTED)
    ├── find_sensors.py                        # OpenAQ sensor discovery tool
    ├── generate_notebook.py                   # Notebook generator script
    ├── inspect_extremes.py                    # Sensor saturation inspection tool
    ├── prepare_analysis_data.py               # Original aggregation script (SAFEGUARDED)
    ├── prepare_enhanced_analysis_data.py      # Enhanced aggregation with circular wind calculations
    ├── prepare_hourly_analysis_data.py        # Harmonizes hourly PM2.5 and meteorology
    ├── run_full_validation.py                 # Master validation orchestrator
    ├── test_openaq.py                         # OpenAQ API connectivity test
    ├── validate_all_pm25.py                   # Comprehensive air quality data validator
    ├── validate_pm25.py                       # Single-file air quality validator
    ├── validate_processed_data.py             # Processed dataset schema & completeness validator
    └── validate_weather.py                    # Weather dataset completeness validator
```

---

## Data Sources & Sensor Identifiers

- **Lahore Ground Sensor:** ID `25135` (31.5204° N, 74.3587° E)
- **Karachi Ground Sensor:** ID `23747` (24.8607° N, 67.0011° E)
- **Islamabad Ground Sensor:** ID `25066` (33.6844° N, 73.0479° E)
- **Peshawar Ground Sensor:** ID `23455` (34.0151° N, 71.5249° E)
- **Quetta Historical Data:** Sensor ID `13340547` commenced recording in mid-2025; retained in raw files but excluded from the 2022–2024 core comparative baseline.

---

## Data Protection & Integrity Rules

Under the project's strict data protection protocol:
1. **Zero Overwrite Policy:** All raw CSV files and the baseline `daily_air_quality_weather_2022_2024.csv` file are strictly read-only.
2. **Cryptographic Verification:** SHA-256 hashes are verified before and after workflow runs:
   - Baseline Processed Hash: `36A77CBFCC07D312B0810E1216C91A295E817078877C8BAEA8C04811253125E9`
   - Lahore Raw PM2.5 Hash: `C5609DE2B80B1477F3F8338BD3B5712449D068AC1E1D14AA44D8197C8652A350`
   - Karachi Raw PM2.5 Hash: `A4B07274113E5A70A142EA84281E4437B9AA233FF26923A4B81252B3E33CE6AF`
   - Islamabad Raw PM2.5 Hash: `145188081F534660ACFFCCE6283F41EF5AD39F560343603C74E0606B98B1C834`
   - Peshawar Raw PM2.5 Hash: `26D6A1856FBEC7CE700A089BA32DD37537043EE55CB823089A87D9BA03B4C6AC`
3. **No Imputation:** Missing measurements are preserved explicitly as `NaN`.
4. **No API Script Re-execution:** Ingestion scripts (`download_pm25.py`, `download_weather.py`) are not run automatically to prevent uncontrolled data replacement.

---

## Technologies & Libraries

- **Language:** Python 3.12 (compatible with Python >= 3.10)
- **Data Wrangling:** `pandas` (3.0.6), `numpy` (2.5.4)
- **Statistical Analytics:** `scipy` (1.18.1)
- **Data Visualization:** `matplotlib` (3.11.2), `seaborn` (0.13.2)
- **Interactive Dashboards:** `plotly` (7.1.0)
- **Notebook & Reporting:** `nbformat` (5.11.1), Markdown, PowerShell

---

## Installation & Quickstart

### Prerequisites
- Python 3.10, 3.11, or 3.12
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Awaisbacha55/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis.git
cd SmogWatch-Lahore-Pakistan-Air-Quality-Analysis
```

### 2. Set Up Virtual Environment & Dependencies

#### On Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

#### On macOS / Linux (bash/zsh):
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Optional Environment Configuration
```bash
# If running fresh API ingestions (OpenAQ / Open-Meteo)
cp .env.example .env     # macOS/Linux
# or
Copy-Item .env.example .env   # Windows PowerShell
```

---

## Reproducibility Workflow

### 1. Data Validation
Execute the verification scripts to inspect dataset integrity and descriptive metrics:
```powershell
# Validate raw air quality data
python scripts\validate_all_pm25.py

# Validate raw weather data
python scripts\validate_weather.py

# Validate baseline combined dataset
python scripts\validate_processed_data.py
```

### 2. Feature Enhancement
Generate the enhanced analysis dataset with circular wind direction averaging and temporal flags (written to a separate file):
```powershell
python scripts\prepare_enhanced_analysis_data.py
```

### 3. Figure & Dashboard Generation
Generate all 15 publication-grade static figures and the interactive Plotly HTML dashboard:
```powershell
python scripts\create_charts.py
```
Outputs are generated in `reports/figures/`.

### 4. Exploratory Notebook
Open the comprehensive Jupyter notebook:
```powershell
jupyter notebook notebooks\01_smogwatch_eda.ipynb
```

---

## Generated Visualizations

| Chart Number | Target Visual | Artifact Path | Primary Scientific Takeaway |
|:---:|---|---|---|
| **01** | Overall Mean PM2.5 Comparison | [`reports/figures/01_overall_mean_pm25_by_city.png`](reports/figures/01_overall_mean_pm25_by_city.png) | Lahore overall mean is 131.8 µg/m³ (26.4x WHO), followed by Peshawar at 91.2 µg/m³. |
| **02** | Annual Mean PM2.5 by City | [`reports/figures/02_annual_mean_pm25_by_city.png`](reports/figures/02_annual_mean_pm25_by_city.png) | Peshawar shows a consistent upward trend; Lahore peaked in 2024 at 141.6 µg/m³. |
| **03** | Monthly Seasonal Cycles | [`reports/figures/03_monthly_seasonal_pm25_patterns.png`](reports/figures/03_monthly_seasonal_pm25_patterns.png) | Acute winter smog peak (Nov–Jan) vs. monsoon trough (Jul–Aug). |
| **04** | Missing-Data Completeness | [`reports/figures/04_missing_data_completeness_by_city.png`](reports/figures/04_missing_data_completeness_by_city.png) | Peshawar has highest coverage (89.5%); Islamabad experienced 198 unrecorded dates. |
| **05** | Daily PM2.5 Trends Over Time | [`reports/figures/05_daily_pm25_trends_over_time.png`](reports/figures/05_daily_pm25_trends_over_time.png) | 4-panel time series with honest gaps illustrating winter spikes across years. |
| **06** | Distribution of PM2.5 Readings | [`reports/figures/06_distribution_pm25_by_city.png`](reports/figures/06_distribution_pm25_by_city.png) | Full range showing 985 µg/m³ ceiling spikes alongside core IQR focus. |
| **07** | Monthly Box Plots by City | [`reports/figures/07_pm25_boxplots_by_month_and_city.png`](reports/figures/07_pm25_boxplots_by_month_and_city.png) | Monthly dispersion highlighting extreme winter variability in Lahore and Peshawar. |
| **08** | Annual Mean vs. WHO Guideline | [`reports/figures/08_annual_mean_vs_who_guideline.png`](reports/figures/08_annual_mean_vs_who_guideline.png) | Annual means range from 8x to 28x the WHO 5 µg/m³ annual guideline. |
| **09** | Daily PM2.5 vs. WHO 24h Limit | [`reports/figures/09_daily_vs_who_24h_guideline.png`](reports/figures/09_daily_vs_who_24h_guideline.png) | >99% non-compliance in Lahore and Peshawar; >58% of days in Lahore exceed 75 µg/m³. |
| **10** | Weather Correlation Heatmap | [`reports/figures/10_weather_pm25_correlation_heatmaps.png`](reports/figures/10_weather_pm25_correlation_heatmaps.png) | Pearson and Spearman heatmaps confirming temperature and wind speed negative correlations. |
| **11** | PM2.5 vs. Temperature Scatter | [`reports/figures/11_pm25_vs_temperature_scatter.png`](reports/figures/11_pm25_vs_temperature_scatter.png) | Strong negative association confirming winter boundary-layer thermal inversions. |
| **12** | PM2.5 vs. Wind Speed Scatter | [`reports/figures/12_pm25_vs_wind_speed_scatter.png`](reports/figures/12_pm25_vs_wind_speed_scatter.png) | Pollution spikes cluster under stagnant conditions (<8 km/h). |
| **13** | PM2.5 vs. Precipitation | [`reports/figures/13_pm25_vs_precipitation_scatter.png`](reports/figures/13_pm25_vs_precipitation_scatter.png) | Wet deposition causes 47.8% median particulate reduction on rain days. |
| **14** | Calendar Heatmap Matrix | [`reports/figures/14_calendar_heatmap_daily_pm25.png`](reports/figures/14_calendar_heatmap_daily_pm25.png) | Lahore 2024 calendar matrix highlighting the deep-red November smog wall. |
| **15** | Interactive Plotly Dashboard | [`reports/figures/smogwatch_interactive_dashboard.html`](reports/figures/smogwatch_interactive_dashboard.html) | Interactive time series with city filters, range slider, tooltips, and WHO thresholds. |
| **16** | Diurnal 24-Hour Profiles by City | [`reports/figures/16_diurnal_pm25_profiles_by_city.png`](reports/figures/16_diurnal_pm25_profiles_by_city.png) | 24-hour cycle showing overnight surface inversion peaks and afternoon convective dispersion troughs. |
| **17** | Seasonal Diurnal Contrast | [`reports/figures/17_seasonal_diurnal_contrast.png`](reports/figures/17_seasonal_diurnal_contrast.png) | Winter smog diurnal surge past 250 µg/m³ vs. subdued summer monsoon profiles. |
| **18** | Diurnal Meteorology Coupling | [`reports/figures/18_meteorology_vs_pm25_diurnal.png`](reports/figures/18_meteorology_vs_pm25_diurnal.png) | Diurnal boundary layer growth: peak temperatures and wind speed directly drive afternoon PM2.5 troughs. |
| **19** | Hour-of-Day × Month Heatmap | [`reports/figures/19_hourly_heatmap_hour_by_month.png`](reports/figures/19_hourly_heatmap_hour_by_month.png) | Worst hours matrix: 22:00–06:00 pre-dawn inversion peak (300–360 µg/m³ in Nov/Dec) vs afternoon convective minimum (<40 µg/m³ in summer). |

---

## Data Quality, Sensor Limits & Limitations

1. **Low-Cost Sensor Saturation:** Readings of $985\ \mu\text{g/m}^3$ in Karachi (21 April 2022) and Peshawar (30 Sep–2 Oct 2023) reflect hardware saturation ceilings. Rather than deleting these values, they are documented as ceiling events.
2. **Telemetry Outages:** Islamabad experienced 198 unrecorded days (predominantly in early 2023), artificially depressing its 2023 annual mean.
3. **Spatial Granularity:** Each city's data reflects a single primary monitoring station; microclimatic neighborhood variations within megacities like Karachi or Lahore require future multi-sensor densification.
4. **Boundary Layer Profiling:** While 105,216 hourly records reveal diurnal surface dynamics, direct vertical LIDAR ceilometer soundings are recommended for future field campaigns to track inversion layer heights directly.

---

## Correlation vs. Causation Caveat

> **Important Scientific Principle:** Correlation does not establish causation. 

Meteorological variables like low temperatures and calm winds do not *create* particulate pollution. Particulates originate from anthropogenic combustion sources (vehicles, industries, kilns, biomass burning). Meteorology acts as a **dispersive or stagnant physical medium**: cold, still air traps emissions in a shallow vertical layer, while wind and rain disperse or deposit them. Policy interventions must address root emission sources.

---

## Project Publication & Deployment Status

- 🌐 **Live Web Report (Published Online):** [https://awaisbacha55.github.io/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis/](https://awaisbacha55.github.io/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis/)
- 📊 **Live Interactive Dashboard (Online):** [https://awaisbacha55.github.io/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis/figures/smogwatch_interactive_dashboard.html](https://awaisbacha55.github.io/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis/figures/smogwatch_interactive_dashboard.html)
- 🎥 **Demo Walkthrough Video:** [https://www.youtube.com/watch?v=YOUR_VIDEO_ID](https://www.youtube.com/watch?v=YOUR_VIDEO_ID) *(Replace with your YouTube URL)*
- 💻 **Standalone GitHub Repository:** [https://github.com/Awaisbacha55/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis](https://github.com/Awaisbacha55/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis)
- 📑 **Comprehensive Data Story Report:** [`reports/smogwatch_week1_report.md`](reports/smogwatch_week1_report.md)
- 📓 **Reproducible Exploratory Notebook:** [`notebooks/01_smogwatch_eda.ipynb`](notebooks/01_smogwatch_eda.ipynb) (100% pre-executed top-to-bottom with inline plots and zero external dependencies).

### Automated GitHub Pages Deployment:
The repository includes `.github/workflows/deploy-pages.yml` and is hosted via the `gh-pages` branch. The live report and interactive dashboard are immediately accessible at: `https://awaisbacha55.github.io/SmogWatch-Lahore-Pakistan-Air-Quality-Analysis/`

---

## References & Citations

1. **World Health Organization (WHO):** *Global Air Quality Guidelines (2021).* [WHO AQG Guidelines](https://www.who.int/publications/i/item/9789240034228)
2. **OpenAQ Platform:** Community air quality data platform. [OpenAQ Documentation](https://docs.openaq.org/)
3. **Open-Meteo:** Historical weather reanalysis API. [Open-Meteo Archive](https://open-meteo.com/en/docs/historical-weather-api)
4. **Mardia, K. V., & Jupp, P. E.:** *Directional Statistics.* John Wiley & Sons, 2000.
