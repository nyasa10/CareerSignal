# CareerSignal – Placement Intelligence & Student Readiness Analytics

## Overview

CareerSignal is a placement analytics and intelligence prototype designed to explore how data can be used to improve student placement outcomes.

The project combines Python, PostgreSQL, SQL, and Power BI to analyze student readiness, recruitment funnel performance, placement outcomes, and skill intelligence. By transforming raw placement data into actionable insights, CareerSignal demonstrates how institutions can leverage analytics to make better placement-related decisions.

---

## Problem Statement

Colleges generate large volumes of placement-related data but often lack visibility into:

* Student placement readiness
* Recruitment funnel performance
* Branch-wise placement outcomes
* Skill gaps impacting employability
* Placement intervention opportunities

Without structured analytics, placement teams struggle to identify bottlenecks, prioritize interventions, and improve placement performance.

CareerSignal explores how a placement intelligence solution can help institutions centralize placement analytics and support data-driven decision-making.

---

## Project Highlights

* Generated a synthetic dataset containing 5,000 student records using Python.
* Designed a relational PostgreSQL database with 4 interconnected tables.
* Developed 20+ analytical SQL queries covering placement performance, recruitment funnel metrics, package analysis, and skill intelligence.
* Built 3 interactive Power BI dashboards for executive reporting and placement analytics.
* Applied product-thinking principles by defining user personas, success metrics, and a future roadmap for a placement intelligence solution.

---

## Target Users

### Placement Officers

**Needs**

* Placement performance tracking
* Recruitment funnel monitoring
* Branch-wise placement analysis
* Placement forecasting

### Career Counselors

**Needs**

* Student readiness assessment
* Skill gap identification
* Intervention planning
* Career guidance support

### Students

**Needs**

* Placement readiness benchmarking
* Skill development insights
* Career preparation visibility

---

## Product Vision

To build a placement intelligence solution that helps institutions proactively improve student employability through analytics-driven interventions and performance tracking.

---

## Success Metrics

### North Star Metric

**Placement Success Rate**

Percentage of students successfully placed.

### Supporting Metrics

* OA Conversion Rate
* Interview Conversion Rate
* Interview → Offer Conversion Rate
* Average Package (LPA)
* Branch-wise Placement Rate
* Offer Distribution

---

## Tech Stack

| Component          | Technology |
| ------------------ | ---------- |
| Dataset Generation | Python     |
| Database           | PostgreSQL |
| Query Layer        | SQL        |
| Visualization      | Power BI   |

---

## Project Architecture

```text
Python
↓
Synthetic Dataset Generation
↓
CSV Files
↓
PostgreSQL Database
↓
SQL Analytics Layer
↓
Power BI Dashboards
↓
Business Insights
```

---

## Dataset Overview

### Project Scale

* 5,000 Students
* 4 Relational Tables
* 20+ Analytical SQL Queries
* 3 Interactive Power BI Dashboards

---

### Students Table

Contains demographic and academic information.

| Column          |
| --------------- |
| student_id      |
| branch          |
| college_tier    |
| cgpa            |
| internships     |
| projects        |
| certifications  |
| resume_score    |
| readiness_score |

---

### Skills Table

Contains technical and employability skill indicators.

| Column                |
| --------------------- |
| skill_id              |
| student_id            |
| dsa_score             |
| python_score          |
| sql_score             |
| communication_score   |
| aptitude_score        |
| problem_solving_score |

---

### Applications Table

Tracks recruitment funnel activity.

| Column              |
| ------------------- |
| app_id              |
| student_id          |
| applications_sent   |
| oa_attempted        |
| oa_cleared          |
| interviews_received |

---

### Placements Table

Tracks placement outcomes.

| Column          |
| --------------- |
| placement_id    |
| student_id      |
| placed          |
| package_lpa     |
| offers_received |

---

## Database Design

The database follows a relational schema centered around **student_id**.

### Relationships

```text
students
    |
    | student_id
    |
-------------------------------------
|                |                 |
skills      applications      placements
```

### Keys

**Primary Key**

* student_id

**Foreign Key Relationships**

* skills.student_id
* applications.student_id
* placements.student_id

---

## SQL Analytics Layer

The project includes 20+ analytical SQL queries covering:

### Placement Analytics

* Overall Placement Rate
* Branch-wise Placement Rate
* Placement Distribution
* Top Performing Branch Analysis

### Package Analytics

* Average Package by Branch
* Package Distribution Analysis
* High-Package Student Analysis

### Recruitment Funnel Analytics

* OA Conversion Rate
* Interview Conversion Rate
* Offer Conversion Rate
* Funnel Drop-Off Analysis

### Skill Intelligence

* Skill Performance Analysis
* Branch Skill Comparison
* Placement Outcome Analysis

### SQL Techniques Used

* JOINs
* CTEs
* Window Functions
* Aggregations
* Ranking Functions
* CASE Statements

---

## Dashboard 1 – Executive Overview

### Purpose

Provides a high-level view of placement performance across the institution.

### KPIs

* Placement Rate
* Average Package
* Total Students
* Students Placed
* Highest Placement Rate Branch

### Visuals

* Placement Rate by Branch
* Average Package by Branch
* Offer Distribution

---

## Dashboard 2 – Placement Funnel Analysis

### Purpose

Analyzes recruitment pipeline performance and identifies funnel bottlenecks.

### KPIs

* Total Applications
* OA Conversion Rate
* Interview Conversion Rate
* Interview → Offer Conversion Rate

### Visuals

* Recruitment Funnel
* Interviews vs Offers by Branch

---

## Dashboard 3 – Skill Intelligence Dashboard

### Purpose

Evaluates student readiness and employability indicators.

### KPIs

* Average Resume Score
* Average Internship Count
* Average DSA Score
* Average Communication Score

### Visuals

* DSA Score vs Placement Rate by Branch
* Branch Skill Matrix
* Placement Rate by College Tier

---

## Key Findings

### Placement Performance

* Overall Placement Rate: **45.74%**
* Total Students Placed: **2,287**
* Average Package: **6.08 LPA**
* CSE achieved the highest placement performance among all branches.

### Recruitment Funnel

* The largest funnel drop occurs between **OA Attempted** and **OA Cleared**.
* OA Conversion Rate: **38.35%**
* Interview Conversion Rate: **28.40%**
* Interview → Offer Conversion Rate: **10.07%**

### Branch Insights

* CSE generated the highest interview volume.
* Placement outcomes vary across academic branches.
* Average package levels differ by branch despite similar placement rates.

### Skill Insights

* Communication scores were consistently higher than technical skill scores.
* DSA performance was analyzed against placement outcomes across branches.
* Skill readiness varies across academic disciplines.

---

## Business Impact

This project demonstrates how placement analytics can:

* Identify placement performance gaps across branches
* Measure end-to-end recruitment funnel efficiency
* Evaluate student readiness indicators
* Support data-driven placement strategy decisions
* Improve visibility into employability outcomes

---

## Product Roadmap

### V1 – Analytics Prototype (Current)

* Placement Analytics Dashboard
* Recruitment Funnel Analysis
* Skill Intelligence Dashboard

### V2 – Readiness Engine

* Student Readiness Scoring
* Placement Risk Segmentation
* Intervention Recommendations

### V3 – Predictive Analytics

* Placement Probability Prediction
* Package Prediction Models
* Placement Forecasting

### V4 – Career Intelligence Platform

* Resume Recommendation Engine
* Skill Gap Analysis
* Personalized Learning Roadmaps

---

## Future Enhancements

* Machine Learning Placement Predictor
* Real-Time Dashboard Integration
* Resume Recommendation System
* Skill Gap Detection Engine
* Placement Forecasting Models

---

## Repository Structure

```text
CareerSignal-Placement-Analytics/
│
├── README.md
│
├── data/
│   ├── students.csv
│   ├── skills.csv
│   ├── applications.csv
│   └── placements.csv
│
├── database/
│   ├── schema.sql
│   ├── data_import.sql
│   ├── analytics_queries.sql
│   └── er_diagram.png
│
├── dashboards/
│   ├── CareerSignal.pbix
│   ├── executive_overview.png
│   ├── placement_funnel.png
│   └── skill_intelligence.png
│
├── python/
│   └── generate_dataset.py
│
└── docs/
    ├── CareerSignal_PRD.pdf
    ├── CareerSignal_Presentation.pdf
    └── Project_Report.pdf
```

---


The project demonstrates data modeling, SQL analytics, dashboard development, KPI design, business intelligence, and product-thinking principles through the lens of placement intelligence.
