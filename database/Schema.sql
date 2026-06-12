CREATE TABLE students (
    student_id INT PRIMARY KEY,
    branch VARCHAR(50),
    college_tier INT,
    cgpa NUMERIC(4,2),
    internships INT,
    projects INT,
    certifications INT,
    resume_score NUMERIC(5,2),
    readiness_score NUMERIC(5,2)
);

CREATE TABLE skills (
    student_id INT PRIMARY KEY,

    dsa_score INT,
    sql_score INT,
    python_score INT,
    communication_score INT,
    aptitude_score INT,
    problem_solving_score INT,

    FOREIGN KEY(student_id)
    REFERENCES students(student_id)
);

CREATE TABLE applications (
    student_id INT PRIMARY KEY,

    applications_sent INT,
    oa_attempted INT,
    oa_cleared INT,
    interviews_received INT,
    interviews_cleared INT,
    offers_received INT,

    FOREIGN KEY(student_id)
    REFERENCES students(student_id)
);

CREATE TABLE placements (
    student_id INT PRIMARY KEY,

    placed INT,

    package_lpa NUMERIC(5,2),

    role_type VARCHAR(100),

    company_type VARCHAR(100),

    FOREIGN KEY(student_id)
    REFERENCES students(student_id)
);
