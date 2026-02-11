# 🚀 E-commerce Multi-Channel Marketing Optimization
> **Project Status:** Completed | **Role:** Data Analyst | **Tools:** Power BI, Python, SQL

## 1. Executive Summary
This project analyzes marketing performance across three major platforms: **Facebook Ads, Google Ads, and TikTok Ads**. The objective was to solve the problem of fragmented data and optimize budget allocation to maximize ROAS (Return on Ad Spend).

**Key Outcomes:**
* Identified **20% of the budget** was being wasted on underperforming TikTok campaigns (ROAS < 1).
* Proposed a budget reallocation strategy projected to increase **total revenue by 15%** without increasing ad spend.
* Developed an automated "Early Warning System" dashboard to detect bleeding campaigns in real-time.

---

## 2. The Business Problem
The simulated E-commerce company was running ads across multiple channels but faced three critical challenges:
1.  **"Black Box" Spending:** Difficulty in determining which channel was driving actual net profit versus vanity metrics (clicks/likes).
2.  **Budget Bleeding:** Inefficient campaigns were running for too long due to a lack of real-time reporting.
3.  **Customer Drop-off:** Unclear visibility on where customers were abandoning the conversion funnel.

---

## 3. Data-Driven Insights
Based on the analysis of the 2025 simulated dataset, here are the critical findings:

### 📉 Insight 1: TikTok Ads - The "Impression Trap"
* **Observation:** TikTok generated massive brand awareness (**116M Impressions**) but suffered from an extremely low conversion rate (~0.5%).
* **Result:** The ROAS for TikTok represents a net loss at **0.63**.
* **Conclusion:** For every $100 spent on TikTok, the company loses $37. It is effective for top-of-funnel awareness but detrimental to immediate profitability.

### 💰 Insight 2: Google Ads - The "Cash Cow"
* **Observation:** Despite having a CPC (Cost Per Click) 3x higher than TikTok, Google Ads delivered the highest conversion intent.
* **Result:** Achieved a ROAS of **1.43** (The highest among all platforms).
* **Conclusion:** This is the primary revenue driver and should be the focus of budget scaling.

### 📊 Insight 3: Campaign Segmentation (Quadrant Analysis)
Using a Scatter Plot analysis, campaigns were segmented into four quadrants:
* **"Stars" (High Spend, High ROAS):** Campaigns to scale immediately.
* **"Bleeders" (High Spend, Low ROAS):** Campaigns draining the budget (mostly TikTok & some Facebook broad targeting).

---

## 4. Strategic Recommendations
As a Data Analyst, I propose the following actionable steps based on these insights:

1.  **Stop Loss Protocol:** Immediately pause all "Bleeder" campaigns (specifically TikTok Ads with ROAS < 0.8) to recover ~20% of wasted ad spend.
2.  **Re-allocation Strategy:** Shift 70% of the recovered budget into **Google Ads** to maximize high-intent traffic, and 30% into Facebook Retargeting campaigns.
3.  **Funnel Optimization:** The drop-off rate from *Click* to *Conversion* is high (97%). I recommend reviewing the Landing Page UX and checkout flow to improve the Conversion Rate (CR).

---

## 5. Dashboard Visualization
The interactive Power BI dashboard allows stakeholders to monitor these metrics in real-time.

### Overall Performance View
![Dashboard Overview](images/dashboard_overview.png)
*The dashboard features high-level KPIs and conditional formatting (Red Alerts) for underperforming channels.*

### Campaign Strategy Matrix (Scatter Plot)
![Campaign Matrix](images/scatter_plot.png)
*The Scatter Plot identifies "Cash Cows" vs. "Bleeders" in seconds, enabling quick decision-making.*

---

## 6. Technical Implementation
To deliver this analysis, I employed a full-stack data analysis approach:

* **Data Simulation (Python):** Developed a Python script to generate realistic E-commerce data (incorporating seasonality, funnel logic, and variable CPCs) to ensure **Data Privacy/NDA compliance** (no real client data was used).
* **Data Modeling (Power BI):** Designed a **Star Schema** with a central `Fact_Marketing` table and supporting `Dim_Date` / `Dim_Platform` tables for optimal performance.
* **DAX Measures:**
    * Calculated `ROAS = [Total Revenue] / [Total Spend]`
    * Time-Intelligence: `MoM Growth = ([Revenue] - [Revenue LM]) / [Revenue LM]`
    * Dynamic Conditional Formatting to visualize trends.

---
*Thank you for reviewing this portfolio project. If you are looking for a Data Analyst who focuses on ROI and Business Value, feel free to connect with me via [LinkedIn Link] or [Email].*
