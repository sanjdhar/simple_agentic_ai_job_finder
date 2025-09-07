from crewai import Task
from agents import JobSearchAgent, AnalysisAgent, MessageWriterAgent, CompanyTargetedAgent, EntryLevelAgent

JobSearch = Task(
    description="""Search for 5-10 recent {title} job postings for candidates with {years} years experience.
    
    Use the job_search tool with these parameters:
    - Primary title: {title}
    - Alternative titles to try: {alternative_titles}
    - Required skills: {required_skills}
    - Experience level: {years} years
    - Location: {location_preference}
    
    If the primary title doesn't yield enough results, try the alternative titles.
    Focus on positions that match the salary expectation: {salary_expectation}
    
    Return comprehensive job information including company name, full job description, salary, direct application link, required skills, and experience requirements.""",
    expected_output="A JSON list with job title, company, location, full description, salary, application link, required skills, and experience level for each position.",
    agent=JobSearchAgent,
    output_file="./job-posts/job-results-2.json"
)

Analysis = Task(
    description="""Analyze the job data to provide targeted recommendations for a {level} {title} candidate.
    
    Focus on:
    - Best matching roles based on required skills: {required_skills}
    - Opportunities to develop preferred skills: {preferred_skills}
    - Salary alignment with expectation: {salary_expectation}
    - Career progression opportunities aligned with goals: {career_goals}
    - Skills gaps and development recommendations
    - Market trends for {title} professionals
    
    Consider the candidate's {years} years of experience and {level} skill level.""",
    expected_output="A comprehensive 4-paragraph analysis covering: 1) Best matching roles and why, 2) Required vs preferred skills analysis, 3) Salary and career progression insights, 4) Skill development recommendations and market trends.",
    agent=AnalysisAgent,
    output_file="./job-posts/new-job-analysis-2.md"
)

MessageWriting = Task(
    description="Write LinkedIn messages and cold emails for 3-5 top job entries. Include job title, company, location, tools/stack, and application link in a formatted daily digest.",
    expected_output="A job digest with 2–3 job entries, each containing a recruiter message and cold email.",
    agent=MessageWriterAgent,
    output_file="./job-posts/new-job-post-2.md"
)

SalaryFocusedSearch = Task(
    description="""Search for {title} positions within specific salary ranges.
    
    Use the salary_job_search tool with these parameters:
    - Title: {title}
    - Required skills: {required_skills}
    - Minimum salary: {min_salary}
    - Maximum salary: {max_salary}
    - Location: {location_preference}
    
    Focus on positions that clearly state salary information and filter for relevant roles.
    Prioritize remote opportunities and positions with comprehensive benefits packages.""",
    expected_output="A formatted list of {title} jobs with salary information, including company details, job requirements, and application links.",
    agent=JobSearchAgent,
    output_file="./job-posts/salary-focused-results.md"
)

CompanyTargetedSearch = Task(
    description="""Search for {title} positions at specific target companies.
    
    Use the company_specific_search tool with these parameters:
    - Company names: {target_companies}
    - Job title: {title}
    - Location: {location_preference}
    
    Research each company's needs, team structure, and hiring patterns for {title} roles.
    Provide insights on company culture and growth opportunities.""",
    expected_output="A detailed report of {title} opportunities at target companies, including company analysis and role recommendations.",
    agent=CompanyTargetedAgent,
    output_file="./job-posts/company-targeted-results.md"
)

EntryLevelSearch = Task(
    description="""Search for entry-level {title} positions and career development opportunities.
    
    Use the entry_level_search tool with these parameters:
    - Job title: {title}
    - Required skills: {required_skills}
    - Location: {location_preference}
    - Include internships: {include_internships}
    
    Focus on positions suitable for new graduates, career changers, or professionals with 0-2 years experience.
    Identify roles that offer training, mentorship, and clear career progression paths.""",
    expected_output="A comprehensive guide to entry-level {title} opportunities, including skill requirements, career paths, and development recommendations.",
    agent=EntryLevelAgent,
    output_file="./job-posts/entry-level-results.md"
)

QuickSearch = Task(
    description="""Perform a quick {title} job search for immediate opportunities.
    
    Use the quick_search tool with these parameters:
    - Keywords: {search_keywords}
    - Location: {location_preference}
    
    Provide a rapid overview of current market opportunities with minimal filtering.
    Focus on speed and breadth of results rather than detailed analysis.""",
    expected_output="A quick summary of current {title} job opportunities with basic details and application links.",
    agent=JobSearchAgent,
    output_file="./job-posts/quick-search-results.md"
)