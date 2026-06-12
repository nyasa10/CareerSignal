import pandas as pd

df = pd.read_csv("career_signal_dataset_v1.csv")

students_df = df[
[
'student_id',
'branch',
'college_tier',
'cgpa',
'internships',
'projects',
'certifications',
'resume_score',
'readiness_score'
]
]

skills_df = df[
[
'student_id',
'dsa_score',
'sql_score',
'python_score',
'communication_score',
'aptitude_score',
'problem_solving_score'
]
]

applications_df = df[
[
'student_id',
'applications_sent',
'oa_attempted',
'oa_cleared',
'interviews_received',
'interviews_cleared',
'offers_received'
]
]

placements_df = df[
[
'student_id',
'placed',
'package_lpa',
'role_type',
'company_type'
]
]

students_df.to_csv("students.csv", index=False)
skills_df.to_csv("skills.csv", index=False)
applications_df.to_csv("applications.csv", index=False)
placements_df.to_csv("placements.csv", index=False)

print("Done")