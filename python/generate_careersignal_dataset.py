import numpy as np
import pandas as pd

np.random.seed(42)

N = 5000

branches = [
    "CSE",
    "IT",
    "ECE",
    "EEE",
    "Mechanical",
    "Civil"
]

role_types = [
    "Software Engineer",
    "Data Analyst",
    "Product Analyst",
    "Business Analyst",
    "Consulting",
    "Core Engineering"
]

company_types = [
    "Product",
    "Service",
    "Startup",
    "Consulting",
    "Core"
]

records = []

for student_id in range(1, N + 1):

    # =====================================================
    # ACADEMIC PROFILE
    # =====================================================

    branch = np.random.choice(
        branches,
        p=[0.35, 0.15, 0.15, 0.10, 0.15, 0.10]
    )

    college_tier = np.random.choice(
        [1, 2, 3],
        p=[0.10, 0.30, 0.60]
    )

    cgpa = round(
        np.clip(
            np.random.normal(7.2, 1.0),
            5.0,
            10.0
        ),
        2
    )

    internships = np.random.choice(
        [0, 1, 2, 3],
        p=[0.45, 0.35, 0.15, 0.05]
    )

    projects = np.random.randint(1, 8)

    certifications = np.random.randint(0, 7)

    # =====================================================
    # SKILLS
    # =====================================================

    dsa_score = int(
        np.clip(
            round(np.random.normal(6, 2)),
            1,
            10
        )
    )

    sql_score = int(
        np.clip(
            round(np.random.normal(6, 2)),
            1,
            10
        )
    )

    python_score = int(
        np.clip(
            round(np.random.normal(6, 2)),
            1,
            10
        )
    )

    communication_score = int(
        np.clip(
            round(np.random.normal(6.5, 1.5)),
            1,
            10
        )
    )

    aptitude_score = int(
        np.clip(
            round(np.random.normal(6, 2)),
            1,
            10
        )
    )

    problem_solving_score = int(
        np.clip(
            round(np.random.normal(6, 2)),
            1,
            10
        )
    )

    # =====================================================
    # RESUME SCORE
    # =====================================================

    resume_score = (
        projects * 8
        + internships * 15
        + certifications * 4
        + np.random.normal(0, 8)
    )

    resume_score = round(
        np.clip(
            resume_score,
            0,
            100
        ),
        0
    )

    # =====================================================
    # READINESS SCORE
    # =====================================================

    readiness_score = (
        cgpa * 3
        + internships * 7
        + projects * 2
        + certifications
        + dsa_score * 2.5
        + sql_score * 2
        + python_score * 2
        + communication_score * 3
        + aptitude_score * 2
        + resume_score * 0.15
    )

    readiness_score = round(
        np.clip(
            readiness_score,
            0,
            100
        ),
        1
    )

    # =====================================================
    # APPLICATION FUNNEL
    # =====================================================

    applications_sent = np.random.randint(
        25,
        150
    )

    oa_attempted = np.random.binomial(
        applications_sent,
        np.random.uniform(0.60, 0.85)
    )

    # =====================================================
    # OA CLEARANCE
    # =====================================================

    oa_clear_rate = (
        0.08
        + dsa_score / 35
        + aptitude_score / 45
    )

    oa_clear_rate = min(
        oa_clear_rate,
        0.75
    )

    oa_cleared = np.random.binomial(
        oa_attempted,
        oa_clear_rate
    )

    # =====================================================
    # INTERVIEW CALLS
    # =====================================================

    interview_rate = (
        0.12
        + communication_score / 40
    )

    interview_rate = min(
        interview_rate,
        0.60
    )

    interviews_received = np.random.binomial(
        oa_cleared,
        interview_rate
    )

    # =====================================================
    # INTERVIEW SUCCESS
    # =====================================================

    interview_clear_rate = (
        0.10
        + communication_score / 40
        + problem_solving_score / 50
    )

    interview_clear_rate = min(
        interview_clear_rate,
        0.60
    )

    interviews_cleared = np.random.binomial(
        interviews_received,
        interview_clear_rate
    )

    # =====================================================
    # OFFERS
    # =====================================================

    offer_rate = (
        0.10
        + communication_score / 50
        + internships / 30
    )

    offer_rate = min(
        offer_rate,
        0.50
    )

    offers_received = np.random.binomial(
        interviews_cleared,
        offer_rate
    )

    offers_received = min(
        offers_received,
        4
    )

    # =====================================================
    # PLACEMENT STATUS
    # =====================================================

    placed = 1 if offers_received > 0 else 0

    # =====================================================
    # PACKAGE
    # =====================================================

    if placed:

        base_package = (
            1.5
            + cgpa * 0.25
            + internships * 0.60
            + dsa_score * 0.18
            + communication_score * 0.12
            + np.random.normal(0, 1.2)
        )

        if college_tier == 1:
            base_package *= 1.30

        elif college_tier == 2:
            base_package *= 1.10

        package_lpa = round(
            np.clip(
                base_package,
                3,
                24
            ),
            2
        )

        role_type = np.random.choice(
            role_types
        )

        company_type = np.random.choice(
            company_types,
            p=[
                0.20,
                0.40,
                0.15,
                0.15,
                0.10
            ]
        )

    else:

        package_lpa = 0

        role_type = "Not Placed"

        company_type = "Not Placed"

    records.append([
        student_id,
        branch,
        college_tier,
        cgpa,
        internships,
        projects,
        certifications,
        dsa_score,
        sql_score,
        python_score,
        communication_score,
        aptitude_score,
        problem_solving_score,
        resume_score,
        readiness_score,
        applications_sent,
        oa_attempted,
        oa_cleared,
        interviews_received,
        interviews_cleared,
        offers_received,
        placed,
        package_lpa,
        role_type,
        company_type
    ])

columns = [
    "student_id",
    "branch",
    "college_tier",
    "cgpa",
    "internships",
    "projects",
    "certifications",
    "dsa_score",
    "sql_score",
    "python_score",
    "communication_score",
    "aptitude_score",
    "problem_solving_score",
    "resume_score",
    "readiness_score",
    "applications_sent",
    "oa_attempted",
    "oa_cleared",
    "interviews_received",
    "interviews_cleared",
    "offers_received",
    "placed",
    "package_lpa",
    "role_type",
    "company_type"
]

df = pd.DataFrame(records, columns=columns)

df.to_csv(
    "career_signal_dataset_v1.csv",
    index=False
)

print("\nDataset Shape:", df.shape)

print(
    "\nPlacement Rate:",
    round(df["placed"].mean() * 100, 2),
    "%"
)

placed_students = df[df["placed"] == 1]

print(
    "\nAverage Package:",
    round(
        placed_students["package_lpa"].mean(),
        2
    ),
    "LPA"
)

print("\nOffer Distribution:")

print(
    df["offers_received"]
    .value_counts(normalize=True)
    .sort_index()
    .round(3)
)