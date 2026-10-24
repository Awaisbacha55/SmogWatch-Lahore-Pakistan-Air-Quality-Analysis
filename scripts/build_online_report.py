"""
Generates the publication-grade web report in docs/index.html for GitHub Pages deployment.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
DOCS_DIR.mkdir(parents=True, exist_ok=True)
INDEX_HTML = DOCS_DIR / "index.html"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SmogWatch: Pakistan Air Quality & Meteorological Surveillance (2022–2024)</title>
    <meta name="description" content="A 3-year multi-city empirical surveillance study of ground-level PM2.5 and meteorology across Lahore, Karachi, Islamabad, and Peshawar benchmarked against WHO 2021 air quality guidelines.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #0F172A;
            --primary-light: #1E293B;
            --accent-red: #D9381E;
            --accent-orange: #E76F51;
            --accent-teal: #2A9D8F;
            --accent-blue: #0284C7;
            --text-main: #334155;
            --text-heading: #0F172A;
            --text-muted: #64748B;
            --bg-page: #F8FAFC;
            --bg-card: #FFFFFF;
            --border-color: #E2E8F0;
            --radius: 10px;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
            --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08), 0 2px 4px -1px rgba(0,0,0,0.04);
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-page);
            color: var(--text-main);
            line-height: 1.68;
            font-size: 16px;
        }

        /* Header & Masthead */
        header.masthead {
            background: linear-gradient(135deg, #0F172A 0%, #1E293B 60%, #334155 100%);
            color: #FFFFFF;
            padding: 4rem 2rem 3.5rem;
            border-bottom: 4px solid var(--accent-red);
        }
        .header-container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .badge-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-bottom: 1.2rem;
        }
        .badge {
            font-size: 0.78rem;
            font-weight: 600;
            padding: 0.35rem 0.75rem;
            border-radius: 9999px;
            background: rgba(255, 255, 255, 0.12);
            color: #E2E8F0;
            border: 1px solid rgba(255, 255, 255, 0.2);
            letter-spacing: 0.02em;
        }
        .badge.danger { background: rgba(217, 56, 30, 0.25); border-color: var(--accent-red); color: #FECACA; }
        .badge.success { background: rgba(16, 185, 129, 0.25); border-color: #10B981; color: #A7F3D0; }
        .masthead h1 {
            font-size: 2.75rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            line-height: 1.18;
            margin-bottom: 0.75rem;
        }
        .masthead p.lead {
            font-size: 1.22rem;
            color: #CBD5E1;
            max-width: 900px;
            font-weight: 400;
            margin-bottom: 1.8rem;
        }
        .meta-strip {
            display: flex;
            flex-wrap: wrap;
            gap: 2rem;
            padding-top: 1.2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.15);
            font-size: 0.9rem;
            color: #94A3B8;
        }
        .meta-strip strong { color: #F1F5F9; }

        /* Container Layout */
        .page-wrapper {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2.5rem 1.5rem;
            display: grid;
            grid-template-columns: 260px 1fr;
            gap: 2.5rem;
        }

        /* Sidebar Nav */
        aside.sidebar {
            position: sticky;
            top: 2rem;
            align-self: start;
            background: var(--bg-card);
            padding: 1.5rem;
            border-radius: var(--radius);
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow-sm);
        }
        aside.sidebar h3 {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-muted);
            margin-bottom: 1rem;
            font-weight: 700;
        }
        aside.sidebar nav ul {
            list-style: none;
        }
        aside.sidebar nav li {
            margin-bottom: 0.55rem;
        }
        aside.sidebar nav a {
            color: var(--text-main);
            text-decoration: none;
            font-size: 0.92rem;
            display: block;
            padding: 0.35rem 0.5rem;
            border-radius: 6px;
            transition: all 0.15s ease;
        }
        aside.sidebar nav a:hover {
            background: #F1F5F9;
            color: var(--accent-red);
            font-weight: 500;
        }
        .dashboard-btn {
            display: block;
            text-align: center;
            background: var(--accent-red);
            color: #FFFFFF !important;
            padding: 0.65rem 1rem;
            border-radius: 6px;
            font-weight: 600;
            margin-top: 1.2rem;
            text-decoration: none;
            box-shadow: 0 2px 4px rgba(217, 56, 30, 0.25);
            transition: background 0.2s;
        }
        .dashboard-btn:hover {
            background: #B91C1C !important;
        }

        /* Main Content */
        main.content {
            min-width: 0;
        }
        section {
            background: var(--bg-card);
            border-radius: var(--radius);
            border: 1px solid var(--border-color);
            padding: 2.2rem;
            margin-bottom: 2.5rem;
            box-shadow: var(--shadow-sm);
        }
        h2 {
            font-size: 1.75rem;
            color: var(--text-heading);
            font-weight: 700;
            margin-bottom: 1.2rem;
            letter-spacing: -0.02em;
            padding-bottom: 0.6rem;
            border-bottom: 2px solid #F1F5F9;
        }
        h3 {
            font-size: 1.25rem;
            color: var(--text-heading);
            margin: 1.5rem 0 0.8rem;
            font-weight: 600;
        }
        p {
            margin-bottom: 1rem;
        }

        /* KPI Metric Cards */
        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.2rem;
            margin: 1.5rem 0;
        }
        .kpi-card {
            background: #F8FAFC;
            border: 1px solid var(--border-color);
            border-left: 4px solid var(--accent-red);
            padding: 1.2rem;
            border-radius: 8px;
        }
        .kpi-card.teal { border-left-color: var(--accent-teal); }
        .kpi-card.orange { border-left-color: var(--accent-orange); }
        .kpi-card.blue { border-left-color: var(--accent-blue); }
        .kpi-value {
            font-size: 2.1rem;
            font-weight: 800;
            color: var(--text-heading);
            line-height: 1.1;
            margin-bottom: 0.3rem;
            font-feature-settings: "tnum";
        }
        .kpi-label {
            font-size: 0.85rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.04em;
            font-weight: 600;
        }
        .kpi-sub {
            font-size: 0.82rem;
            color: #64748B;
            margin-top: 0.4rem;
        }

        /* Figure Display */
        .figure-box {
            margin: 2rem 0;
            border: 1px solid var(--border-color);
            border-radius: var(--radius);
            overflow: hidden;
            background: #FFFFFF;
            box-shadow: var(--shadow-sm);
        }
        .figure-box img {
            width: 100%;
            height: auto;
            display: block;
            border-bottom: 1px solid var(--border-color);
        }
        .figure-caption {
            padding: 0.9rem 1.2rem;
            background: #F8FAFC;
            font-size: 0.88rem;
            color: #475569;
        }
        .figure-caption strong {
            color: var(--text-heading);
        }

        /* Data Tables */
        .table-responsive {
            overflow-x: auto;
            margin: 1.4rem 0;
            border: 1px solid var(--border-color);
            border-radius: 8px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.92rem;
            text-align: left;
        }
        th {
            background: #F1F5F9;
            color: var(--text-heading);
            font-weight: 600;
            padding: 0.75rem 1rem;
            border-bottom: 1px solid var(--border-color);
        }
        td {
            padding: 0.75rem 1rem;
            border-bottom: 1px solid var(--border-color);
            color: #334155;
        }
        tr:last-child td { border-bottom: none; }
        tr:nth-child(even) { background-color: #FAFAFA; }

        /* Callout Box */
        .callout {
            background: #EFF6FF;
            border-left: 4px solid var(--accent-blue);
            padding: 1.2rem 1.4rem;
            border-radius: 6px;
            margin: 1.5rem 0;
            color: #1E3A8A;
            font-size: 0.95rem;
        }
        .callout.warning {
            background: #FEF2F2;
            border-left-color: #DC2626;
            color: #991B1B;
        }
        .callout strong { display: block; margin-bottom: 0.3rem; }

        /* Code & Pre */
        pre, code {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.88rem;
        }
        pre {
            background: #0F172A;
            color: #F8FAFC;
            padding: 1.2rem;
            border-radius: 8px;
            overflow-x: auto;
            margin: 1rem 0;
        }

        /* Footer */
        footer.site-footer {
            background: #0F172A;
            color: #94A3B8;
            padding: 3rem 2rem;
            margin-top: 3rem;
            text-align: center;
            font-size: 0.9rem;
        }
        footer.site-footer a { color: #E2E8F0; text-decoration: none; }
        footer.site-footer a:hover { text-decoration: underline; }

        /* Responsive */
        @media (max-width: 900px) {
            .page-wrapper {
                grid-template-columns: 1fr;
            }
            aside.sidebar {
                position: static;
            }
            .masthead h1 { font-size: 2.1rem; }
        }
    </style>
</head>
<body>

    <header class="masthead">
        <div class="header-container">
            <div class="badge-row">
                <span class="badge danger">WHO 2021 AQG Benchmarked</span>
                <span class="badge">4 Major Cities: Lahore, Karachi, Islamabad, Peshawar</span>
                <span class="badge">Temporal Window: 2022–2024 (1,096 Days)</span>
                <span class="badge success">105,216 Hourly Synchronized Observations</span>
                <span class="badge">Zero Synthetic Imputation</span>
            </div>
            <h1>SmogWatch: Pakistan Air Quality Surveillance</h1>
            <p class="lead">A 3-year empirical investigation of ground-level PM2.5 and atmospheric boundary layer meteorology across Lahore, Karachi, Islamabad, and Peshawar.</p>
            <div class="meta-strip">
                <div><strong>Lead Investigator:</strong> Awais (SmogWatch Surveillance Project)</div>
                <div><strong>Data Sources:</strong> OpenAQ API v3 &amp; Open-Meteo Historical Archive</div>
                <div><strong>Framework:</strong> Scientific Data Protection &amp; Directional Wind Statistics</div>
            </div>
        </div>
    </header>

    <div class="page-wrapper">
        <aside class="sidebar">
            <h3>Table of Contents</h3>
            <nav>
                <ul>
                    <li><a href="#executive-summary">1. Executive Summary</a></li>
                    <li><a href="#empirical-findings">2. Key Empirical Findings</a></li>
                    <li><a href="#city-baselines">3. Statistical Baselines</a></li>
                    <li><a href="#seasonal-dynamics">4. Seasonal Smog Cycles</a></li>
                    <li><a href="#who-compliance">5. WHO Compliance</a></li>
                    <li><a href="#meteorology">6. Meteorological Coupling</a></li>
                    <li><a href="#hourly-analysis">7. Hourly Diurnal Dynamics</a></li>
                    <li><a href="#interactive-dashboard">8. Interactive Dashboard</a></li>
                    <li><a href="#sensor-limits">9. Sensor Ceiling Limits</a></li>
                    <li><a href="#recommendations">10. Recommendations</a></li>
                    <li><a href="#reproducibility">11. Reproducibility &amp; Data</a></li>
                </ul>
            </nav>
            <a href="figures/smogwatch_interactive_dashboard.html" target="_blank" class="dashboard-btn">Open Interactive Dashboard</a>
        </aside>

        <main class="content">

            <!-- Section 1: Executive Summary -->
            <section id="executive-summary">
                <h2>1. Executive Summary</h2>
                <p>Fine particulate matter (&le; 2.5 &micro;m diameter, $\\text{PM}_{2.5}$) represents the most severe environmental health risk facing Pakistan's 240+ million population. In the Indus River Plain and the Peshawar Valley, annual winter smog events have escalated from localized seasonal anomalies into acute public health emergencies.</p>
                <p><strong>SmogWatch</strong> provides an empirical, scientifically reproducible surveillance study across four major urban centres—<strong>Lahore</strong>, <strong>Karachi</strong>, <strong>Islamabad</strong>, and <strong>Peshawar</strong>—spanning 1,096 calendar days (1 January 2022 to 31 December 2024). This study integrates ground-level monitoring records with high-resolution meteorology, incorporating 4,384 city-day observations and 105,216 synchronized hourly observations without artificial imputation.</p>

                <div class="kpi-grid">
                    <div class="kpi-card">
                        <div class="kpi-value">131.8 &micro;g/m&sup3;</div>
                        <div class="kpi-label">Lahore Overall Mean</div>
                        <div class="kpi-sub">26.4&times; WHO Annual Guideline</div>
                    </div>
                    <div class="kpi-card orange">
                        <div class="kpi-value">+18.9%</div>
                        <div class="kpi-label">Peshawar Trend</div>
                        <div class="kpi-sub">83.1 &rarr; 98.8 &micro;g/m&sup3; (2022 to 2024)</div>
                    </div>
                    <div class="kpi-card teal">
                        <div class="kpi-value">99.3%</div>
                        <div class="kpi-label">Lahore Exceedance Rate</div>
                        <div class="kpi-sub">846 of 852 days > 15 &micro;g/m&sup3;</div>
                    </div>
                    <div class="kpi-card blue">
                        <div class="kpi-value">-47.8%</div>
                        <div class="kpi-label">Rain Scavenging</div>
                        <div class="kpi-sub">Median drop on wet days (>0.5 mm)</div>
                    </div>
                </div>

                <div class="figure-box">
                    <img src="figures/01_overall_mean_pm25_by_city.png" alt="Overall Mean PM2.5 Comparison">
                    <div class="figure-caption">
                        <strong>Figure 1: Overall Mean PM2.5 Concentration by City (2022–2024).</strong> Error bars represent 95% confidence intervals, and solid dots display median concentrations. Lahore and Peshawar exhibit catastrophic regional pollution burdens compared to Islamabad and Karachi.
                    </div>
                </div>
            </section>

            <!-- Section 2: Key Empirical Findings -->
            <section id="empirical-findings">
                <h2>2. Key Empirical Findings</h2>
                <div class="table-responsive">
                    <table>
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Finding Domain</th>
                                <th>Empirical Observation</th>
                                <th>Statistical Evidence</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>1</strong></td>
                                <td><strong>Chronic Baseline Crisis</strong></td>
                                <td>Lahore's particulate burden represents severe chronic toxicity, peaking in 2024.</td>
                                <td>Mean <strong>131.84 &micro;g/m&sup3;</strong> (Median 89.95, $n=852$). 2024 mean reached <strong>141.62 &micro;g/m&sup3;</strong> (28.3&times; WHO).</td>
                            </tr>
                            <tr>
                                <td><strong>2</strong></td>
                                <td><strong>Peshawar Monotonic Rise</strong></td>
                                <td>Peshawar experienced steady year-over-year particulate increases across all 3 years.</td>
                                <td>2022: <strong>83.08</strong> &rarr; 2023: <strong>91.23</strong> &rarr; 2024: <strong>98.75 &micro;g/m&sup3;</strong> (+18.9% cumulative surge).</td>
                            </tr>
                            <tr>
                                <td><strong>3</strong></td>
                                <td><strong>Winter Smog Escalation</strong></td>
                                <td>Severe 4-fold seasonal amplification in the Indus Basin during winter months.</td>
                                <td>Lahore Winter Mean: <strong>223.68 &micro;g/m&sup3;</strong> vs. Summer Monsoon: <strong>55.55 &micro;g/m&sup3;</strong> ($4.03&times;$ seasonal surge).</td>
                            </tr>
                            <tr>
                                <td><strong>4</strong></td>
                                <td><strong>Near-Universal Non-Compliance</strong></td>
                                <td>Daily WHO safety benchmarks are breached almost 100% of the monitored calendar.</td>
                                <td>Exceedance of 15 &micro;g/m&sup3;: <strong>99.3% in Lahore</strong> (846/852 days), <strong>99.2% in Peshawar</strong> (973/981 days).</td>
                            </tr>
                            <tr>
                                <td><strong>5</strong></td>
                                <td><strong>Atmospheric Stagnation</strong></td>
                                <td>Particulate concentrations correlate strongly with thermal inversions and calm winds.</td>
                                <td>Temperature Pearson $r = -0.608$ in Lahore; Wind Speed Pearson $r = -0.453$ (Spearman $\\rho = -0.591$ in Karachi).</td>
                            </tr>
                            <tr>
                                <td><strong>6</strong></td>
                                <td><strong>Precipitation Wash-out</strong></td>
                                <td>Rainfall acts as the primary natural atmospheric scavenging mechanism.</td>
                                <td>Median PM2.5 drops from <strong>54.0 &micro;g/m&sup3;</strong> (dry days) to <strong>28.2 &micro;g/m&sup3;</strong> (wet days >0.5 mm), a <strong>47.8% drop</strong>.</td>
                            </tr>
                            <tr>
                                <td><strong>7</strong></td>
                                <td><strong>Diurnal Planetary Boundary Layer Dynamics</strong></td>
                                <td>Particulate matter peaks overnight during shallow surface radiation inversions.</td>
                                <td>Lahore Night Inversion (22:00–06:00): <strong>153.19 &micro;g/m&sup3;</strong> vs. Afternoon Convective Mixing (11:00–16:00): <strong>99.77 &micro;g/m&sup3;</strong> (-34.9%).</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>

            <!-- Section 3: Statistical Baselines -->
            <section id="city-baselines">
                <h2>3. Multi-City Statistical Baselines</h2>
                <p>The 4-city comparison reveals a severe structural geographic divide. Inland northern plain and valley cities (Lahore and Peshawar) suffer particulate levels 2.5&times; to 3&times; higher than coastal Karachi and the northern sub-Himalayan plateau of Islamabad.</p>

                <div class="table-responsive">
                    <table>
                        <thead>
                            <tr>
                                <th>City</th>
                                <th>Valid Monitored Days</th>
                                <th>Mean (&micro;g/m&sup3;)</th>
                                <th>Median (&micro;g/m&sup3;)</th>
                                <th>Std Dev</th>
                                <th>IQR (&micro;g/m&sup3;)</th>
                                <th>Max (&micro;g/m&sup3;)</th>
                                <th>WHO Annual Multiple</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Lahore</strong></td>
                                <td>852 (77.7%)</td>
                                <td><strong>131.84</strong></td>
                                <td>89.95</td>
                                <td>104.52</td>
                                <td>129.02</td>
                                <td>630.00</td>
                                <td><strong>26.4&times;</strong></td>
                            </tr>
                            <tr>
                                <td><strong>Peshawar</strong></td>
                                <td>981 (89.5%)</td>
                                <td><strong>91.22</strong></td>
                                <td>62.90</td>
                                <td>90.68</td>
                                <td>57.00</td>
                                <td>985.00*</td>
                                <td><strong>18.2&times;</strong></td>
                            </tr>
                            <tr>
                                <td><strong>Karachi</strong></td>
                                <td>862 (78.7%)</td>
                                <td><strong>47.31</strong></td>
                                <td>31.80</td>
                                <td>47.15</td>
                                <td>34.90</td>
                                <td>985.00*</td>
                                <td><strong>9.5&times;</strong></td>
                            </tr>
                            <tr>
                                <td><strong>Islamabad</strong></td>
                                <td>828 (75.5%)</td>
                                <td><strong>46.18</strong></td>
                                <td>36.40</td>
                                <td>32.58</td>
                                <td>29.05</td>
                                <td>264.00</td>
                                <td><strong>9.2&times;</strong></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <p><small>*Note: 985 &micro;g/m&sup3; values correspond to sensor saturation ceilings investigated in Section 8.</small></p>

                <div class="figure-box">
                    <img src="figures/02_annual_mean_pm25_by_city.png" alt="Annual Mean PM2.5 Trends">
                    <div class="figure-caption">
                        <strong>Figure 2: Annual Mean PM2.5 Trends by City (2022–2024).</strong> Demonstrates the alarming multi-year monotonic rise in Peshawar (83.1 &rarr; 91.2 &rarr; 98.8 &micro;g/m&sup3;) and the chronic elevated plateau in Lahore.
                    </div>
                </div>

                <div class="figure-box">
                    <img src="figures/06_distribution_pm25_by_city.png" alt="Distribution of PM2.5 by City">
                    <div class="figure-caption">
                        <strong>Figure 6: Density and Empirical Distributions of Daily PM2.5.</strong> Highlights extreme positive skewness and long exposure tails exceeding 300 &micro;g/m&sup3; in Lahore and Peshawar.
                    </div>
                </div>
            </section>

            <!-- Section 4: Seasonal Dynamics -->
            <section id="seasonal-dynamics">
                <h2>4. Seasonal Smog Cycles &amp; Longitudinal Trends</h2>
                <p>Air quality in Pakistan is strongly dictated by seasonal weather regimes: the winter stagnation period (December–February), pre-monsoon spring (March–May), summer monsoon (June–August), and post-monsoon autumn transition (September–November).</p>

                <div class="figure-box">
                    <img src="figures/03_monthly_seasonal_pm25_patterns.png" alt="Monthly and Seasonal PM2.5 Patterns">
                    <div class="figure-caption">
                        <strong>Figure 3: Monthly and Seasonal PM2.5 Variations (2022–2024).</strong> In Lahore, concentrations surge four-fold from a summer monsoon low of 55.6 &micro;g/m&sup3; to a catastrophic winter average of 223.7 &micro;g/m&sup3;.
                    </div>
                </div>

                <div class="figure-box">
                    <img src="figures/07_pm25_boxplots_by_month_and_city.png" alt="Monthly PM2.5 Boxplots">
                    <div class="figure-caption">
                        <strong>Figure 7: Monthly Particulate Distributions.</strong> Shows the massive variance and extreme outlier clusters during November and December across all cities.
                    </div>
                </div>

                <div class="figure-box">
                    <img src="figures/14_calendar_heatmap_daily_pm25.png" alt="Calendar Heatmap of Daily PM2.5">
                    <div class="figure-caption">
                        <strong>Figure 14: Daily Calendar Heatmap for Lahore (2022–2024).</strong> Visualizes uninterrupted severe multi-week pollution episodes (>200 &micro;g/m&sup3;) dominating October through January each year.
                    </div>
                </div>
            </section>

            <!-- Section 5: WHO Compliance -->
            <section id="who-compliance">
                <h2>5. WHO 2021 Benchmark Compliance</h2>
                <p>In 2021, the World Health Organization revised its Air Quality Guidelines (AQG) based on comprehensive epidemiological evidence, setting the annual guideline at <strong>5 &micro;g/m&sup3;</strong> and the 24-hour guideline at <strong>15 &micro;g/m&sup3;</strong>, alongside interim targets (IT-1: 75 &micro;g/m&sup3;, IT-2: 50 &micro;g/m&sup3;, IT-3: 37.5 &micro;g/m&sup3;, IT-4: 25 &micro;g/m&sup3;).</p>

                <div class="figure-box">
                    <img src="figures/08_annual_mean_vs_who_guideline.png" alt="Annual Mean vs WHO Guideline">
                    <div class="figure-caption">
                        <strong>Figure 8: Annual Mean PM2.5 vs. WHO 2021 Guideline.</strong> All four cities exceed the annual health safety threshold by 8&times; to 28&times;.
                    </div>
                </div>

                <div class="figure-box">
                    <img src="figures/09_daily_pm25_vs_who_24h_guideline.png" alt="Daily PM2.5 vs WHO 24h Guideline">
                    <div class="figure-caption">
                        <strong>Figure 9: Proportion of Monitored Days Exceeding WHO 24-Hour Benchmarks.</strong> Over 99% of days in Lahore and Peshawar breach the 15 &micro;g/m&sup3; benchmark. Even the lenient Interim Target 1 (75 &micro;g/m&sup3;) is breached on 58.7% of days in Lahore.
                    </div>
                </div>
            </section>

            <!-- Section 6: Meteorological Coupling -->
            <section id="meteorology">
                <h2>6. Meteorological Interactions &amp; Atmospheric Physics</h2>
                <p>Atmospheric meteorology acts as the physical dispersion and transport medium for anthropogenic emissions. Analysis confirms strong negative correlations with temperature and wind speed.</p>

                <div class="figure-box">
                    <img src="figures/10_weather_pm25_correlation_heatmaps.png" alt="Weather Correlation Heatmaps">
                    <div class="figure-caption">
                        <strong>Figure 10: Dual Correlation Matrices (Pearson r &amp; Spearman &rho;).</strong> Temperature and wind speed show universal negative correlations with particulate concentrations across all urban centers.
                    </div>
                </div>

                <div class="figure-box">
                    <img src="figures/11_pm25_vs_temperature_scatter.png" alt="PM2.5 vs Temperature Scatter">
                    <div class="figure-caption">
                        <strong>Figure 11: Particulate Concentrations vs. Ambient Temperature.</strong> Steep non-linear surges occur when temperatures drop below 18°C, reflecting nocturnal radiation inversions.
                    </div>
                </div>

                <div class="figure-box">
                    <img src="figures/12_pm25_vs_wind_speed_scatter.png" alt="PM2.5 vs Wind Speed Scatter">
                    <div class="figure-caption">
                        <strong>Figure 12: Particulate Concentrations vs. Wind Speed.</strong> Severe pollution episodes (>150 &micro;g/m&sup3;) are strictly confined to calm conditions (<8 km/h).
                    </div>
                </div>

                <div class="figure-box">
                    <img src="figures/13_pm25_vs_precipitation_scatter.png" alt="PM2.5 vs Precipitation Scatter">
                    <div class="figure-caption">
                        <strong>Figure 13: Wet vs. Dry Days Scavenging Differential.</strong> Demonstrates physical impaction wash-out, cutting median particulate levels by ~48%.
                    </div>
                </div>
            </section>

            <!-- Section 7: Hourly Analysis -->
            <section id="hourly-analysis">
                <h2>7. Hourly Diurnal Dynamics &amp; Boundary Layer Thermodynamics</h2>
                <div class="callout">
                    <strong>High-Resolution Hourly Surveillance</strong>
                    By harmonizing 105,216 hourly observations (26,304 hours per city across 2022–2024), we resolve the diurnal boundary layer processes that 24-hour daily averages obscure.
                </div>

                <p>Particulate concentrations exhibit a strong bimodal diurnal curve. Between 22:00 and 06:00, surface radiational cooling creates a shallow nocturnal temperature inversion layer (<150–200 m), trapping vehicular and industrial emissions. The morning rush hour (07:00–10:00) injects fresh combustion products into this compressed surface layer, causing an early-morning peak. By midday (11:00–16:00), intense solar heating warms the ground, triggering convective turbulence that expands the planetary boundary layer (>1,200 m) and disperses ground-level aerosols.</p>

                <div class="figure-box">
                    <img src="figures/16_diurnal_pm25_profiles_by_city.png" alt="Diurnal 24-Hour PM2.5 Profiles">
                    <div class="figure-caption">
                        <strong>Figure 16: Diurnal 24-Hour PM2.5 Profiles across Pakistani Megacities (2022–2024).</strong> Shaded bands denote &plusmn;95% confidence intervals. Lahore exhibits a 53.4 &micro;g/m&sup3; diurnal amplitude between nighttime inversion peaks and afternoon convective troughs.
                    </div>
                </div>

                <div class="figure-box">
                    <img src="figures/17_seasonal_diurnal_contrast.png" alt="Winter Smog vs Summer Monsoon Diurnal Profiles">
                    <div class="figure-caption">
                        <strong>Figure 17: Seasonal Diurnal Contrast: Winter Smog vs. Summer Monsoon.</strong> Winter diurnal profiles in Lahore exceed 250 &micro;g/m&sup3; overnight, while summer profiles remain subdued and dominated by continuous convective ventilation.
                    </div>
                </div>

                <div class="figure-box">
                    <img src="figures/18_meteorology_vs_pm25_diurnal.png" alt="Thermodynamic Mechanisms of the Diurnal Cycle">
                    <div class="figure-caption">
                        <strong>Figure 18: Thermodynamic Drivers of Diurnal Air Pollution in Lahore.</strong> Shows the exact synchronization between peak afternoon temperatures (14:00–16:00), peak surface wind speeds, and the daily particulate minimum.
                    </div>
                </div>

                <h3>Diurnal–Seasonal Heatmap: Identification of Worst Hours</h3>
                <p>The 2D bivariate matrix below plots mean PM2.5 concentrations across every hour of the day (vertical axis) for all 12 calendar months (horizontal axis). It pinpoints the exact time windows when toxic inversion concentrations accumulate:</p>

                <div class="figure-box">
                    <img src="figures/19_hourly_heatmap_hour_by_month.png" alt="Hour of Day vs Month Heatmap">
                    <div class="figure-caption">
                        <strong>Figure 19: Hour-of-Day vs. Month Particulate Heatmap for Lahore and Peshawar (2022–2024).</strong> Highlights the nocturnal inversion peak window (22:00–06:00 in November and December, averaging 300–360 &micro;g/m&sup3; in Lahore) contrasted against afternoon convective dilution in summer (<40 &micro;g/m&sup3;).
                    </div>
                </div>

                <h3>Top 10 Worst Monitored Days Per City</h3>
                <p>The table below provides an explicit audit of the 10 most hazardous particulate days recorded in each city, documenting co-occurring meteorological parameters and WHO 24-hour limit exceedance multiples (15 &micro;g/m&sup3;):</p>

                <div class="table-responsive">
                    <table>
                        <thead>
                            <tr>
                                <th>City</th>
                                <th>Rank</th>
                                <th>Date</th>
                                <th>Daily PM2.5 (&micro;g/m&sup3;)</th>
                                <th>WHO 24h Multiple</th>
                                <th>Temp (°C)</th>
                                <th>Wind Speed (km/h)</th>
                                <th>Humidity (%)</th>
                                <th>Season / Synoptic Regime</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td><strong>Lahore</strong></td><td>#1</td><td><strong>2024-11-14</strong></td><td><strong>630.0</strong></td><td><strong>42.0&times; WHO</strong></td><td>20.9</td><td>4.2</td><td>80.4</td><td>Autumn Smog (Extreme Stagnation)</td></tr>
                            <tr><td><strong>Lahore</strong></td><td>#2</td><td><strong>2024-11-06</strong></td><td><strong>570.0</strong></td><td><strong>38.0&times; WHO</strong></td><td>23.1</td><td>4.3</td><td>72.0</td><td>Autumn Smog (Regional Plume)</td></tr>
                            <tr><td><strong>Lahore</strong></td><td>#3</td><td><strong>2024-11-07</strong></td><td><strong>519.0</strong></td><td><strong>34.6&times; WHO</strong></td><td>23.2</td><td>5.3</td><td>75.4</td><td>Autumn Smog Wave</td></tr>
                            <tr><td><strong>Lahore</strong></td><td>#4</td><td><strong>2024-11-08</strong></td><td><strong>505.0</strong></td><td><strong>33.7&times; WHO</strong></td><td>22.6</td><td>5.9</td><td>80.0</td><td>Autumn Smog Wave</td></tr>
                            <tr><td><strong>Lahore</strong></td><td>#5</td><td><strong>2023-12-22</strong></td><td><strong>488.0</strong></td><td><strong>32.5&times; WHO</strong></td><td>11.8</td><td>5.6</td><td>90.9</td><td>Winter Solstice Inversion</td></tr>
                            <tr><td><strong>Peshawar</strong></td><td>#1</td><td><strong>2023-10-03</strong></td><td><strong>637.0</strong></td><td><strong>42.5&times; WHO</strong></td><td>26.5</td><td>4.3</td><td>36.6</td><td>Autumn Peak Post-Inversion Wave</td></tr>
                            <tr><td><strong>Peshawar</strong></td><td>#2</td><td><strong>2023-01-07</strong></td><td><strong>562.0</strong></td><td><strong>37.5&times; WHO</strong></td><td>10.1</td><td>5.2</td><td>68.9</td><td>Winter Basin Radiation Inversion</td></tr>
                            <tr><td><strong>Peshawar</strong></td><td>#3</td><td><strong>2024-01-08</strong></td><td><strong>491.0</strong></td><td><strong>32.7&times; WHO</strong></td><td>11.6</td><td>4.3</td><td>86.0</td><td>Winter Fog-Smog Stagnation</td></tr>
                            <tr><td><strong>Peshawar</strong></td><td>#4</td><td><strong>2023-04-28</strong></td><td><strong>465.0</strong></td><td><strong>31.0&times; WHO</strong></td><td>21.8</td><td>11.6</td><td>46.6</td><td>Spring Dust Transport Episode</td></tr>
                            <tr><td><strong>Peshawar</strong></td><td>#5</td><td><strong>2023-01-06</strong></td><td><strong>458.0</strong></td><td><strong>30.5&times; WHO</strong></td><td>10.1</td><td>4.6</td><td>72.7</td><td>Winter Solstice Valley Inversion</td></tr>
                            <tr><td><strong>Karachi</strong></td><td>#1</td><td><strong>2022-01-19</strong></td><td><strong>231.0</strong></td><td><strong>15.4&times; WHO</strong></td><td>18.9</td><td>14.5</td><td>75.7</td><td>Winter Continental Advection</td></tr>
                            <tr><td><strong>Karachi</strong></td><td>#2</td><td><strong>2022-01-22</strong></td><td><strong>195.0</strong></td><td><strong>13.0&times; WHO</strong></td><td>18.0</td><td>32.9</td><td>37.4</td><td>High-Wind Coastal Dust Transport</td></tr>
                            <tr><td><strong>Karachi</strong></td><td>#3</td><td><strong>2022-01-27</strong></td><td><strong>193.0</strong></td><td><strong>12.9&times; WHO</strong></td><td>18.1</td><td>10.1</td><td>60.9</td><td>Winter Night Offshore Drift</td></tr>
                            <tr><td><strong>Islamabad</strong></td><td>#1</td><td><strong>2022-12-24</strong></td><td><strong>264.0</strong></td><td><strong>17.6&times; WHO</strong></td><td>9.5</td><td>9.5</td><td>71.5</td><td>Winter Solstice Cold Inversion</td></tr>
                            <tr><td><strong>Islamabad</strong></td><td>#2</td><td><strong>2024-12-22</strong></td><td><strong>176.0</strong></td><td><strong>11.7&times; WHO</strong></td><td>11.4</td><td>3.1</td><td>54.4</td><td>Winter Plateau Stagnation</td></tr>
                        </tbody>
                    </table>
                </div>
            </section>

            <!-- Section 8: Interactive Plotly Dashboard -->
            <section id="interactive-dashboard">
                <h2>8. Interactive Particulate Surveillance Dashboard</h2>
                <p>Explore daily fine particulate measurements (&micro;g/m&sup3;) across Lahore, Karachi, Islamabad, and Peshawar with the interactive Plotly dashboard embedded below. You can toggle individual city time series, zoom in on severe smog spikes, filter temporal windows using the bottom range slider, and inspect hover tooltips against the WHO 2021 24-hour guideline (15 &micro;g/m&sup3;).</p>
                <div style="margin: 1.5rem 0; border: 1px solid var(--border-color); border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow-sm); background: #FFFFFF;">
                    <iframe src="figures/smogwatch_interactive_dashboard.html" style="width: 100%; height: 750px; border: none;" title="SmogWatch Interactive Plotly Dashboard"></iframe>
                </div>
                <p style="text-align: center; margin-top: 1rem;">
                    <a href="figures/smogwatch_interactive_dashboard.html" target="_blank" class="dashboard-btn" style="display: inline-block; padding: 0.75rem 1.8rem; font-size: 0.95rem;">Open Dashboard Full-Screen in New Tab &rarr;</a>
                </p>
            </section>

            <!-- Section 9: Sensor Saturation Ceilings & Sensitivity Analysis -->
            <section id="sensor-limits">
                <h2>9. Sensor Ceiling Artifacts &amp; Sensitivity Analysis</h2>
                <p>A rigorous audit of maximum recorded values identified an uncalibrated optical saturation limit at <strong>985.0 &micro;g/m&sup3;</strong> occurring in Karachi (21 April 2022) and Peshawar (30 September to 2 October 2023).</p>
                <div class="callout warning">
                    <strong>Critical Quality Control &amp; Cleaning Policy:</strong>
                    Optical sensors estimate PM2.5 by light scattering. Above high aerosol concentrations (>800–1000 &micro;g/m&sup3;), optical multi-scattering saturates the detector photodiode, producing a flat measurement ceiling at 985 &micro;g/m&sup3;. In Karachi, OpenAQ assigned automated QA/QC flags (<code>Level: ERROR</code>) to this date, whereas in Peshawar, an artificial 3-day plateau at exactly 985 &micro;g/m&sup3; went unannotated.
                    <br><br>
                    <strong>Policy:</strong> Raw source telemetry is preserved without modification in <code>data/raw/</code> and retained in <code>pm25_ug_m3_raw</code>. In the primary analytical dataset (<code>daily_air_quality_weather_enhanced.csv</code>), these four occurrences are flagged with <code>is_sensor_ceiling_error = True</code> and set to <code>NaN</code>.
                </div>

                <h3>Sensitivity Analysis Table: With vs. Without 985 &micro;g/m&sup3;</h3>
                <p>To verify whether sensor saturation alters any core research findings, the table below compares parametric and non-parametric statistics alongside meteorological correlations:</p>

                <div class="table-responsive">
                    <table>
                        <thead>
                            <tr>
                                <th>City</th>
                                <th>Dataset Treatment</th>
                                <th>Count ($n$)</th>
                                <th>Mean (&micro;g/m&sup3;)</th>
                                <th>Std Dev</th>
                                <th>Median</th>
                                <th>Max (&micro;g/m&sup3;)</th>
                                <th>Temp Pearson $r$</th>
                                <th>Wind Pearson $r$</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td rowspan="2"><strong>Karachi</strong></td>
                                <td>With 985 (Raw)</td>
                                <td>862</td>
                                <td>47.31</td>
                                <td>47.15</td>
                                <td>31.80</td>
                                <td>985.0</td>
                                <td>-0.453</td>
                                <td>-0.339</td>
                            </tr>
                            <tr style="background: #F8FAFC;">
                                <td><strong>Without 985 (Cleaned)</strong></td>
                                <td><strong>861</strong></td>
                                <td><strong>46.22</strong></td>
                                <td><strong>34.67</strong></td>
                                <td><strong>31.80</strong></td>
                                <td><strong>231.0</strong></td>
                                <td><strong>-0.629</strong></td>
                                <td><strong>-0.478</strong></td>
                            </tr>
                            <tr>
                                <td rowspan="2"><strong>Peshawar</strong></td>
                                <td>With 985 (Raw)</td>
                                <td>981</td>
                                <td>91.22</td>
                                <td>90.68</td>
                                <td>62.90</td>
                                <td>985.0</td>
                                <td>-0.438</td>
                                <td>-0.338</td>
                            </tr>
                            <tr style="background: #F8FAFC;">
                                <td><strong>Without 985 (Cleaned)</strong></td>
                                <td><strong>978</strong></td>
                                <td><strong>88.48</strong></td>
                                <td><strong>76.07</strong></td>
                                <td><strong>62.75</strong></td>
                                <td><strong>637.0</strong></td>
                                <td><strong>-0.537</strong></td>
                                <td><strong>-0.401</strong></td>
                            </tr>
                            <tr>
                                <td><strong>Lahore</strong></td>
                                <td>Identical (No 985 events)</td>
                                <td>852</td>
                                <td>131.84</td>
                                <td>104.52</td>
                                <td>89.95</td>
                                <td>630.0</td>
                                <td>-0.608</td>
                                <td>-0.453</td>
                            </tr>
                            <tr>
                                <td><strong>Islamabad</strong></td>
                                <td>Identical (No 985 events)</td>
                                <td>828</td>
                                <td>46.18</td>
                                <td>32.58</td>
                                <td>36.40</td>
                                <td>264.0</td>
                                <td>-0.584</td>
                                <td>-0.209</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <h3>Key Sensitivity Takeaways:</h3>
                <ul>
                    <li><strong>Median Robustness:</strong> In both Karachi ($31.80 \rightarrow 31.80\ \mu\text{g/m}^3$) and Peshawar ($62.90 \rightarrow 62.75\ \mu\text{g/m}^3$), medians remain virtually unchanged, validating that the median is a robust central tendency metric resistant to sensor saturation.</li>
                    <li><strong>Variance and Maximum Realignment:</strong> Setting the 4 ceiling dates to NaN reduces artificial standard deviation by <strong>-26.5%</strong> in Karachi and <strong>-16.1%</strong> in Peshawar, adjusting the true monitored maximum in Karachi to $231.0\ \mu\text{g/m}^3$ and in Peshawar to $637.0\ \mu\text{g/m}^3$.</li>
                    <li><strong>Peshawar Multi-Year Trend Clarification:</strong> With raw telemetry, Peshawar showed a steady year-on-year increase ($83.1 \rightarrow 91.2 \rightarrow 98.8\ \mu\text{g/m}^3$). After removing the artificial October 2023 ceiling plateau, 2022 to 2023 was virtually flat ($83.08 \rightarrow 82.72\ \mu\text{g/m}^3$), followed by an acute <strong>+19.4% surge in 2024 ($98.75\ \mu\text{g/m}^3$)</strong>. The 3-year escalation remains severe (+18.9%), but the timing is corrected.</li>
                    <li><strong>Strengthened Weather Coupling:</strong> Negative correlations with temperature ($r = -0.453 \rightarrow -0.629$ in Karachi; $-0.438 \rightarrow -0.537$ in Peshawar) and wind speed ($r = -0.339 \rightarrow -0.478$ in Karachi) become significantly stronger once warm-weather false spikes are excluded.</li>
                </ul>

                <div class="figure-box">
                    <img src="figures/04_missing_data_completeness_by_city.png" alt="Temporal Completeness by City">
                    <div class="figure-caption">
                        <strong>Figure 4: Observational Completeness and Missing Calendar Dates.</strong> Documents temporal completeness ranging from 75.5% in Islamabad (due to early 2023 sensor downtime) to 89.5% in Peshawar.
                    </div>
                </div>
            </section>

            <!-- Section 10: Recommendations -->
            <section id="recommendations">
                <h2>10. Policy Recommendations &amp; Scientific Caveats</h2>
                
                <h3>Correlation vs. Causation Caveat</h3>
                <p>A statistical correlation between meteorological variables (cold temperatures, calm winds) and PM2.5 <strong>does not indicate that weather generates particulates</strong>. Particulates originate solely from anthropogenic combustion (transport, heavy industry, brick kilns, agricultural waste burning, and fossil fuel power plants). Meteorology acts as a physical dispersion medium that either concentrates or ventilates emissions. Policy must directly target emission reduction.</p>

                <h3>Actionable Interventions</h3>
                <ol style="margin-left: 1.5rem; margin-bottom: 1.5rem;">
                    <li style="margin-bottom: 0.8rem;"><strong>Diurnal Freight and Kiln Bans:</strong> Prohibit heavy diesel truck transit and industrial firing between 22:00 and 06:00 when nocturnal thermal inversions trap surface emissions, shifting operations to the midday mixing window (12:00–16:00).</li>
                    <li style="margin-bottom: 0.8rem;"><strong>Targeted Seasonal Enforcement:</strong> Concentrate strict enforcement against agricultural crop burning and unregulated brick kilns during October through January.</li>
                    <li style="margin-bottom: 0.8rem;"><strong>Dynamic Meteorological Warning Systems:</strong> Link public school and workplace alerts to 48-hour forecasts of low wind speeds (<8 km/h) and nocturnal inversions.</li>
                    <li style="margin-bottom: 0.8rem;"><strong>Reference-Grade Gravimetric Network:</strong> Deploy federal reference-method (FRM) monitors in Lahore, Peshawar, Karachi, and Islamabad to calibrate optical sensors and eliminate saturation clipping.</li>
                </ol>
            </section>

            <!-- Section 11: Reproducibility -->
            <section id="reproducibility">
                <h2>11. Reproducibility &amp; Source Code</h2>
                <p>The SmogWatch analysis suite is fully reproducible from command line using Python 3.10+:</p>
                <pre><code># 1. Activate Environment
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 2. Run Data Validation Pipeline
python scripts/validate_all_pm25.py
python scripts/validate_weather.py

# 3. Generate Enhanced Daily & Hourly Datasets
python scripts/prepare_enhanced_analysis_data.py
python scripts/prepare_hourly_analysis_data.py

# 4. Generate All 18 Publication Figures & Interactive Dashboard
python scripts/create_charts.py
python scripts/create_hourly_charts.py

# 5. Run Complete Executed EDA Notebook
python scripts/build_executed_notebook.py</code></pre>
            </section>

        </main>
    </div>

    <footer class="site-footer">
        <p><strong>SmogWatch: Pakistan Air Quality Surveillance (2022–2024)</strong></p>
        <p>Author: Awais &bull; Open-Source Environmental Data Science &bull; License: MIT</p>
        <p style="margin-top: 0.5rem;"><small>Data Sources: OpenAQ API v3 &bull; Open-Meteo Historical Weather Reanalysis</small></p>
    </footer>

</body>
</html>
"""

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Publication-grade web report created successfully at: {INDEX_HTML}")

