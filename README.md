# openai-gen-co-and-qp
Generate Course Outcomes and Question Papers with AI

## About the Application
- To generate course outcomes you may input the entire syllabus or course handout, and the application will generate course outcomes.
- To generate course/module specific questions, input the details regarding the textbook and the chapter being studied and the application will generate questions that test the conceptual grasp of students.
- OpenAI API key is hidden and comes from environment variables
- The API is protected using bearer token authorization
- Modular API structure for easy development and maintainability
- Uses FastAPI and asynchronicity, thus making it faster than traditional Flask based APIs

# Input Examples

1. Generate Course Outcomes

```sh
POST
Authorization: Bearer <token>
```
  
```json
{
    "course_name": "Database Management Systems",
    "syllabus": {
        "Course_Title": "Advanced Database Management Systems",
        "Course_Overview": "This course provides an in-depth exploration of advanced concepts and techniques in Database Management Systems (DBMS) for students pursuing a Master's degree in Computer Science. Through lectures, hands-on exercises, and projects, students will gain comprehensive knowledge and practical skills required to design, implement, and optimize complex database systems.",
        "Prerequisites": [
            "Undergraduate-level course in Database Management Systems or equivalent knowledge",
            "Proficiency in SQL",
            "Understanding of basic data structures and algorithms",
            "Familiarity with relational database concepts"
        ],
        "Course_Objectives": [
            "Understand advanced database models and architectures.",
            "Explore advanced query optimization techniques.",
            "Learn about distributed and parallel databases.",
            "Gain knowledge of data warehousing and data mining concepts.",
            "Develop skills in database security and privacy.",
            "Explore emerging trends and technologies in database management."
        ],
        "Course_Structure": {
            "Module_1": {
                "Title": "Advanced Database Models",
                "Topics": [
                    "Relational Model Extensions",
                    "Object-Oriented and Object-Relational Databases",
                    "XML and Semi-Structured Data Models",
                    "NoSQL Databases",
                    "Graph Databases"
                ]
            },
            "Module_2": {
                "Title": "Advanced Query Optimization",
                "Topics": [
                    "Query Processing and Optimization Techniques",
                    "Cost Models and Estimation",
                    "Query Execution Plans",
                    "Indexing and Access Methods",
                    "Parallel Query Processing"
                ]
            },
            "Module_3": {
                "Title": "Distributed and Parallel Databases",
                "Topics": [
                    "Distributed Database Architectures",
                    "Replication and Fragmentation",
                    "Data Partitioning and Distribution",
                    "Concurrency Control in Distributed Databases",
                    "Parallel Database Processing Techniques"
                ]
            },
            "Module_4": {
                "Title": "Data Warehousing and Data Mining",
                "Topics": [
                    "Data Warehouse Architecture",
                    "Dimensional Modeling",
                    "Extract, Transform, Load (ETL) Processes",
                    "Data Mining Techniques",
                    "Association Rule Mining, Clustering, Classification"
                ]
            },
            "Module_5": {
                "Title": "Database Security and Privacy",
                "Topics": [
                    "Access Control and Authorization",
                    "Encryption and Cryptography",
                    "Auditing and Logging",
                    "Data Anonymization Techniques",
                    "GDPR and Regulatory Compliance"
                ]
            },
            "Module_6": {
                "Title": "Emerging Trends in Database Management",
                "Topics": [
                    "Big Data Technologies",
                    "Cloud Databases",
                    "Blockchain and Distributed Ledger Technologies",
                    "In-Memory Databases",
                    "IoT Data Management"
                ]
            }
        },
        "Assessment": [
            "Assignments and Programming Projects",
            "Midterm Examination",
            "Final Project: Design and Implementation of an Advanced Database System",
            "Class Participation and Discussion"
        ],
        "Textbook": [
            "Database System Concepts by Abraham Silberschatz, Henry F. Korth, and S. Sudarshan",
            "Database Management Systems by Raghu Ramakrishnan and Johannes Gehrke",
            "Additional research papers and online resources"
        ],
        "Software_Tools": [
            "MySQL, PostgreSQL, or Oracle for relational database management",
            "MongoDB or Cassandra for NoSQL databases",
            "Apache Hadoop or Spark for distributed processing",
            "Data mining tools such as Weka or R"
        ],
        "Grading_Policy": {
            "Assignments_and_Projects": "40%",
            "Midterm_Examination": "20%",
            "Final_Project": "30%",
            "Class_Participation": "10%"
        },
        "Note": "This syllabus is subject to change at the discretion of the instructor to accommodate emerging technologies and industry trends. Students are expected to actively engage in discussions, complete assignments on time, and demonstrate a thorough understanding of the course materials."
    }
}
```


2. Generate Question Paper

```sh
POST
Authorization: Bearer <token>
```


```json
{
    "course_name": "Engineering Thermodynamics",
    "textbook_name": "A Textbook of Engineering Thermodynamics",
    "textbook_authors": "R.K. Rajput",
    "isbn": "9788170084372, 8170084377",
    "topic": "Chapter 6",
    "difficulty": "difficult",
    "number_of_questions": "10"
}
```
