# CareerSignal – Placement Intelligence & Student Readiness Analytics

## Overview

CareerSignal is a placement intelligence platform designed to help placement cells, career counselors, and academic institutions monitor student readiness, identify recruitment funnel bottlenecks, and improve placement outcomes through data-driven decision-making.

The project combines Python, PostgreSQL, SQL, and Power BI to transform raw placement data into actionable insights across student performance, recruitment efficiency, and employability indicators.

---

## Problem Statement

Colleges generate large volumes of placement-related data but often lack visibility into:

* Student placement readiness
* Recruitment funnel performance
* Branch-wise placement outcomes
* Skill gaps impacting employability
* Placement intervention opportunities

Without structured analytics, placement teams struggle to identify at-risk students and optimize placement strategies.

CareerSignal addresses this challenge by providing a centralized analytics platform for placement intelligence.

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

To build a placement intelligence platform that enables institutions to proactively improve student employability through analytics-driven interventions and performance tracking.

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
* Student Readiness Score
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

### Total Records

* 5,000 Students
* 4 Relational Tables
* 20+ Analytical SQL Queries
* 3 Interactive Power BI Dashboards

---

### Students Table

Contains student demographic and academic information.

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

Contains employability and technical skill indicators.

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

* Primary Key: student_id
* Foreign Key Relationships:

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
* Top Performing Branches

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
* Placement Correlation Analysis

### SQL Techniques Used

* JOINs
* CTEs
* Window Functions
* Aggregations
* Ranking Functions
* CASE Statements
* Correlation Analysis

---

## Dashboard 1 – Executive Overview

### Purpose

Provides a high-level view of placement performance.

### KPIs

* Placement Rate
* Average Package
* Total Students
* Students Placed
* Top Performing Branch

### Visuals

* Placement Rate by Branch
* Average Package by Branch
* Offer Distribution

---

## Dashboard 2 – Placement Funnel Analysis

### Purpose

Analyzes recruitment pipeline performance.

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

* DSA Score vs Placement Rate
* Branch Skill Matrix
* Placement Rate by College Tier

---

## Key Findings

### Placement Performance

* Overall Placement Rate: **45.74%**
* Total Students Placed: **2,287**
* Average Package: **6.08 LPA**

### Recruitment Funnel

* Largest funnel drop occurs between **OA Attempted** and **OA Cleared**
* OA Conversion Rate: **38.35%**
* Interview Conversion Rate: **28.40%**
* Interview → Offer Conversion Rate: **10.07%**

### Branch Insights

* CSE achieved the highest placement performance
* CSE generated the highest interview volume
* Significant variation exists across branches

### Skill Insights

* Communication scores consistently outperform technical skills
* DSA performance shows a measurable relationship with placement outcomes
* Skill readiness varies across branches

---

## Business Impact

* Identified placement performance gaps across branches
* Measured end-to-end recruitment funnel efficiency
* Evaluated skill-readiness indicators
* Enabled data-driven placement strategy decisions
* Built an interactive placement intelligence solution

---

## Product Roadmap

### V1 – Analytics Platform

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



CareerSignal was developed as an end-to-end Product Analytics & Business Intelligence project combining Python, PostgreSQL, SQL, and Power BI to demonstrate data engineering, analytics, dashboarding, and product thinking capabilities.
