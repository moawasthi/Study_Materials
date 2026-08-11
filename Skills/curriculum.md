# Data Engineering Interview Curriculum

This is the full topic taxonomy for the data engineer interview prep skill. SKILL.md points here when picking or verifying a topic — this file itself is only loaded when needed, not on every session.

Treat this list as the map of what's in scope, not a script to read aloud. When picking a topic, cross-reference it against the learner's progress file (see SKILL.md) rather than working through this document top to bottom.

## Table of contents

**Section 1 — Technical Preparation**
1. Azure Data Engineering / DP-203
2. Azure Databricks — Associate
3. Azure Databricks — Professional
4. Dimensional Modeling
5. ER Modeling Basics
6. Python
7. Python Data Structures & Coding Interviews
8. SQL
9. Data Security
10. Data Governance
11. Data Engineering System Design
12. Distributed Systems & Data Platform Architecture

**Section 2 — Career & Interview Preparation**
13. Resume Preparation
14. Job Description Analysis
15. LinkedIn & GitHub Preparation
16. Technical Interview Preparation
17. System Design Interview Preparation
18. Behavioral Interview Preparation
19. STAR Method
20. Data Engineering Scenario Questions
21. Communication & Problem-Solving Strategy
22. Mock Interviews

**Section 3 — Capstone Project**
23. Project Objective
24. Business Requirements
25. System Architecture
26. Data Ingestion
27. Data Processing
28. Data Modeling
29. Batch & Streaming
30. Data Quality
31. Security & Governance
32. Monitoring & Observability
33. Performance Optimization
34. Cost Optimization
35. CI/CD & Deployment
36. Documentation
37. Interview Defense

---

## Section 1 — Technical Preparation

### 1. Azure Data Engineering / DP-203

* Azure Data Lake Storage Gen2
* Azure Data Factory
* Azure Synapse Analytics
* Azure Event & Streaming Services
* Azure Monitoring

### 2. Azure Databricks — Associate

* Databricks Fundamentals
* Apache Spark Fundamentals
* PySpark
* Delta Lake
* Databricks Workflows
* Unity Catalog

### 3. Azure Databricks — Professional

* Spark Performance Optimization
* Advanced Delta Lake
* Streaming
* Production Architecture

### 4. Dimensional Modeling

* Fact tables
* Dimension tables
* Measures
* Attributes
* Grain
* Surrogate keys
* Natural keys
* Degenerate dimensions
* Conformed dimensions
* Role-playing dimensions
* Slowly Changing Dimensions
* Transaction fact
* Periodic snapshot fact
* Accumulating snapshot fact
* SCD Type 0
* SCD Type 1
* SCD Type 2
* SCD Type 3
* Star schema
* Snowflake schema

### 5. ER Modeling Basics

* Entity
* Attribute
* Relationship
* Primary key
* Foreign key
* Candidate key
* Natural key
* Surrogate key
* Composite key
* Cardinality
* Optionality
* 1 : 1
* 1 : N
* N : N
* 1NF
* 2NF
* 3NF
* BCNF

### 6. Python

* Python fundamentals
* Variables
* Data types
* Strings
* Lists
* Tuples
* Sets
* Dictionaries
* Conditions
* Loops
* Functions
* Lambda
* List comprehensions
* Dictionary comprehensions
* Exception handling
* Modules
* Packages
* Virtual environments
* `*args`
* `**kwargs`
* Iterators
* Generators
* Decorators
* Context managers
* `map`
* `filter`
* `reduce`
* `zip`
* `enumerate`
* `sorted`
* Mutable vs immutable
* Shallow vs deep copy
* CSV processing
* JSON processing
* Large file processing
* API ingestion
* Pagination
* Error handling
* Logging
* Configuration
* Environment variables
* Database connectivity
* Date/time processing
* Batch processing
* pandas
* PySpark
* requests
* json
* datetime
* logging
* os
* pathlib

### 7. Python Data Structures & Coding Interviews

* Lists
* Tuples
* Sets
* Dictionaries
* Stacks
* Queues
* Deques
* Hash maps
* Linked lists
* Trees
* Binary search trees
* Heaps
* Graphs
* Two pointers
* Sliding window
* Hashing
* Binary search
* Stack
* Queue
* BFS
* DFS
* Heap / Top K
* Recursion
* O(1)
* O(log n)
* O(n)
* O(n log n)
* O(n²)
* O(2ⁿ)

### 8. SQL

* SQL Fundamentals
* SELECT
* WHERE
* GROUP BY
* HAVING
* ORDER BY
* DISTINCT
* CASE
* NULL handling
* Aggregate functions
* INNER JOIN
* LEFT JOIN
* RIGHT JOIN
* FULL OUTER JOIN
* CROSS JOIN
* SELF JOIN
* One-to-one joins
* One-to-many joins
* Many-to-many joins
* Join multiplication
* Duplicate rows caused by joins
* CTEs
* Scalar subqueries
* Correlated subqueries
* EXISTS
* NOT EXISTS
* Recursive CTE
* Window functions
* ROW_NUMBER
* RANK
* DENSE_RANK
* LAG / LEAD
* Running totals
* Deduplication
* Query execution plans
* Indexes
* Partitioning
* Views
* Materialized views
* Transactions
* ACID
* Isolation levels
* Query optimization
* Normalization
* Denormalization

### 9. Data Security

* Authentication
* Authorization
* Encryption
* Identity management
* RBAC
* ACL
* Least privilege
* Secrets management
* Network security
* Data masking
* Tokenization
* Key management
* Audit logging
* Microsoft Entra ID
* Managed identities
* Azure Key Vault
* Storage ACLs
* Private endpoints
* VNets
* Network security
* Encryption at rest
* Encryption in transit
* Unity Catalog
* Catalog permissions
* Schema permissions
* Table permissions
* Column-level security
* Row-level security
* External locations
* Storage credentials
* Secrets
* Service principals / identities
* Audit logs
* Data lineage

### 10. Data Governance

* Data ownership
* Data stewardship
* Data catalog
* Data lineage
* Data classification
* Data discovery
* Data quality
* Data privacy
* Data retention
* Metadata management
* Access policies
* Accuracy
* Completeness
* Consistency
* Timeliness
* Validity
* Uniqueness
* Null checks
* Duplicate checks
* Referential integrity
* Schema validation
* Range validation
* Business-rule validation
* Reconciliation

### 11. Data Engineering System Design

* Requirements gathering
* Functional requirements
* Non-functional requirements
* Scalability
* Availability
* Reliability
* Fault tolerance
* Performance
* Latency
* Throughput
* Consistency
* Durability
* Cost
* Security
* Sources
* Message Broker
* Ingestion
* Data Lake
* Processing
* Data Warehouse / Lakehouse
* Serving Layer
* BI / ML / Applications
* Batch vs Streaming
* Watermarks
* CDC
* Timestamps
* Sequence numbers
* Change tracking
* Idempotency
* Deduplication
* Upserts
* Backfills
* Retries
* Checkpointing
* Dead-letter queues
* Error handling
* Replay
* Failure recovery
* Disaster recovery
* Horizontal scaling
* Partitioning
* Parallel processing
* Distributed computing
* Data sharding
* Load balancing
* Autoscaling

### 12. Distributed Systems & Data Platform Architecture

* Distributed computing
* CAP theorem
* Consistency models
* Partitioning
* Replication
* Fault tolerance
* Horizontal scaling
* Message queues
* Event-driven architecture
* Exactly-once vs at-least-once
* Idempotency
* Event ordering
* Backpressure
* Checkpointing
* Distributed transactions
* Data locality
* Eventual consistency
* Spark
* Kafka / Event Hubs
* Databricks
* Data Lakes
* Lakehouses
* Data Warehouses

---

# Section 2 — Career & Interview Preparation

### 13. Resume Preparation

* Resume tailored to target roles
* Quantifiable achievements
* Azure / Databricks experience
* System design experience
* Capstone project
* ATS-friendly formatting

### 14. Job Description Analysis

* Required skills
* Must-have skills
* Nice-to-have skills
* Skill gaps
* Preparation priorities
* Resume customization
* Skill matrix

### 15. LinkedIn & GitHub Preparation

* Professional headline
* Data Engineering keywords
* Azure / Databricks skills
* Experience
* Projects
* Certifications
* Professional summary
* Python repositories
* SQL repositories
* PySpark repositories
* Azure repositories
* Databricks repositories
* Data modeling repositories
* System design repositories
* Capstone project

### 16. Technical Interview Preparation

* SQL Round
* Python Round
* Data Engineering Round
* Architecture Round
* Query writing
* Window functions
* Joins
* Aggregations
* CTEs
* Optimization
* Python fundamentals
* Data structures
* Coding problems
* ETL/ELT
* ADF
* ADLS
* Databricks
* Spark
* Delta Lake
* Data modeling
* Pipeline design
* Lakehouse design
* Batch/streaming
* Scalability
* Reliability
* Security
* Governance

### 17. System Design Interview Preparation

* E-commerce data platform
* Real-time analytics platform
* Customer 360 platform
* Clickstream processing system
* Recommendation data pipeline
* IoT data platform
* Financial transaction platform
* CDC-based data warehouse
* Enterprise data lake
* Lakehouse platform
* Requirements
* Scale
* Architecture
* Data ingestion
* Storage
* Processing
* Data model
* Serving
* Scalability
* Reliability
* Security
* Monitoring
* Cost
* Trade-offs

### 18. Behavioral Interview Preparation

* Production incident
* Project failure
* Tight deadline
* Technical disagreement
* Conflict with teammate
* Conflict with manager
* Technical decision
* Architecture trade-off
* Mistake
* Learning from failure
* Taking ownership
* Process improvement
* Handling ambiguity
* Helping teammates
* Leadership
* Difficult stakeholder

### 19. STAR Method

* Situation
* Task
* Action
* Result

### 20. Data Engineering Scenario Questions

* Design a 1 TB/day data pipeline.
* Design a real-time analytics system.
* Design a customer 360 platform.
* Design a CDC pipeline.
* Design an enterprise data lake.
* Handle a 10x increase in data volume.
* Recover from a failed pipeline.
* Process duplicate events.
* Handle schema evolution.
* Process late-arriving data.
* Perform a historical backfill.
* Optimize a slow Spark job.
* Secure sensitive customer data.

### 21. Communication & Problem-Solving Strategy

* Clarify requirements
* Clarify scale
* Clarify latency
* Clarify SLA
* Clarify data volume
* Clarify data sources
* Clarify consumers
* Clarify security requirements
* Structure answers
* Think aloud
* State assumptions
* Explain brute force
* Optimize
* Code
* Test
* Analyze complexity
* Explain unknown concepts honestly

### 22. Mock Interviews

* SQL
* Python
* Data Engineering
* Spark
* Azure
* Databricks
* Data Modeling
* System Design
* Behavioral
* STAR

---

# Section 3 — Capstone Project

### 23. Project Objective

* End-to-End Azure Data Engineering Lakehouse

### 24. Business Requirements

* Customers
* Products
* Orders
* Payments
* Stores
* Inventory
* Web Events
* Daily batch ingestion
* Incremental processing
* Near-real-time event processing
* Historical reporting
* Customer analytics
* Product analytics
* Sales analytics
* Inventory analytics
* Data quality
* Security
* Governance
* Monitoring

### 25. System Architecture

* Source Systems
* Batch Sources
* Streaming Events
* Azure Data Factory
* Azure Event Hubs
* ADLS Gen2
* Bronze
* Azure Databricks
* Silver
* Gold
* Synapse / SQL
* BI / Analytics

### 26. Data Ingestion

* Full ingestion
* Incremental ingestion
* CDC
* Watermarking
* Parameterized pipelines
* Metadata-driven ingestion
* Error handling
* Retry
* Idempotency

### 27. Data Processing

* Schema validation
* Data cleansing
* Deduplication
* Transformations
* Joins
* Aggregations
* Business rules
* SCD processing
* Incremental processing

### 28. Data Modeling

* fact_sales
* fact_inventory
* fact_customer_activity
* dim_customer
* dim_product
* dim_store
* dim_date
* dim_promotion
* Star schema
* Surrogate keys
* SCD Type 2
* Conformed dimensions
* Fact grain

### 29. Batch & Streaming

* Batch
* Streaming
* Azure Event Hubs
* Structured Streaming
* Bronze
* Silver
* Gold

### 30. Data Quality

* Null checks
* Duplicate checks
* Schema validation
* Referential integrity
* Business-rule validation
* Reconciliation
* Freshness checks
* Quarantine

### 31. Security & Governance

* RBAC
* Managed identities
* Key Vault
* Unity Catalog
* Least privilege
* PII classification
* Access control
* Audit logging
* Data lineage

### 32. Monitoring & Observability

* Pipeline duration
* Records processed
* Records rejected
* Failures
* Retries
* Freshness
* Spark execution time
* Shuffle
* Input/output
* Task failures
* Partition distribution
* Sales
* Orders
* Customers
* Inventory

### 33. Performance Optimization

* Partition strategy
* Broadcast joins
* Predicate pushdown
* Column pruning
* Repartitioning
* Small-file optimization
* Data skew handling
* Delta optimization
* Query optimization

### 34. Cost Optimization

* Compute sizing
* Autoscaling
* Job clusters
* Serverless options where appropriate
* Storage lifecycle
* File optimization
* Query optimization
* Workload scheduling
* Avoiding unnecessary processing
* Performance vs Cost

### 35. CI/CD & Deployment

* Git
* Feature Branch
* Pull Request
* Code Review
* CI
* Testing
* Deployment
* Unit tests
* PySpark tests
* SQL tests
* Configuration management
* Environment separation
* Development
* Test
* Production

### 36. Documentation

* Business problem
* Requirements
* Architecture
* Data model
* Security
* Governance
* Data quality
* Design decisions
* Performance decisions
* Cost decisions

### 37. Interview Defense

* Architecture
* System Design
* Data Modeling
* Spark
* Security
* Governance
* Performance
* Scalability
* Reliability
* Cost
* Trade-offs
* Failure scenarios
* Backfills
* Schema evolution
* Duplicate events
* Idempotency

---