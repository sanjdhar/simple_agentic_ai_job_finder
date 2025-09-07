# Simple Agentic AI Job Finder

An AI-powered job search system designed for professionals in any field. Uses specialized agents and multiple search strategies to find the best positions matching your skills, experience, and preferences.

## 🚀 Features

### Multiple Search Types

- **Standard Search**: Comprehensive job search with detailed analysis
- **Salary Focused**: Target jobs within specific salary ranges
- **Company Targeted**: Search at specific companies you want to work for
- **Entry Level**: Find entry-level positions and internships
- **Quick Search**: Fast results with minimal filtering
- **Full Search**: Complete search with outreach message generation

### Specialized AI Agents

- **JobSearchAgent**: Expert job researcher with advanced search strategies
- **CompanyTargetedAgent**: Specialist in researching specific companies
- **EntryLevelAgent**: Career advisor for new professionals
- **AnalysisAgent**: Strategic career guidance and market analysis (uses file reading tools to analyze previous results)
- **MessageWriterAgent**: Creates LinkedIn messages and cold emails (uses file reading tools to access job data)

### Advanced Search Tools

- **job_search**: Generic job search with skill matching and filtering
- **salary_job_search**: Filter jobs by salary range
- **company_specific_search**: Target specific companies
- **entry_level_search**: Find junior and entry-level positions
- **quick_search**: Fast search with minimal filtering
- **docs_tool**: Read and analyze previous job search results from output directory
- **file_tool**: Access specific result files for detailed analysis

## 📋 Prerequisites

1. **Python 3.8+**
2. **API Keys**:
   - SerpAPI key for job search (get from [serpapi.com](https://serpapi.com))
   - Google Gemini API key for AI agents (get from [Google AI Studio](https://makersuite.google.com/app/apikey))

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd generic-job-search
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:

   ```env
   SERPER_API_KEY=your_serpapi_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   GEMINI_MODEL=gemini-1.5-flash
   ```

4. **Create output directory**:
   ```bash
   mkdir -p job-posts
   ```

## 🎯 Usage

### Interactive Mode (Recommended)

Run the interactive search tool:

```bash
python run_search.py
```

This will present a menu where you can choose from different search types.

### Direct Execution

Run specific search types directly:

```bash
python main.py
```

Edit the `search_type` variable in `main.py` to choose:

- `"standard"` - Basic search with analysis
- `"salary_focused"` - Salary-based search
- `"company_targeted"` - Company-specific search
- `"entry_level"` - Entry-level positions
- `"quick"` - Fast search
- `"full"` - Complete search with messaging

## ⚙️ Configuration

### Customize Your Search

Edit `config.py` to customize your job search preferences:

```python
JOB_CONFIG = {
    "title": "Oracle Database Engineer",
    "alternative_titles": ["Oracle DBA", "Database Administrator"],
    "years": "1-3",
    "level": "beginner/intermediate",
    "required_skills": ["Oracle", "SQL", "PL/SQL"],
    "preferred_skills": ["Performance Tuning", "Oracle RAC"],
    "location_preference": "remote",
    "salary_expectation": "$70,000 - $110,000",
    "target_companies": "Oracle, Microsoft, Amazon, Google, IBM"
}
```

### Search Type Details

| Search Type      | Best For                      | Output Files                                  |
| ---------------- | ----------------------------- | --------------------------------------------- |
| Standard         | General job searching         | `job-results-2.json`, `new-job-analysis-2.md` |
| Salary Focused   | Salary is primary concern     | `salary-focused-results.md`                   |
| Company Targeted | Preferred companies           | `company-targeted-results.md`                 |
| Entry Level      | New graduates/career changers | `entry-level-results.md`                      |
| Quick            | Urgent job searching          | `quick-search-results.md`                     |
| Full             | Comprehensive with networking | All files + `new-job-post-2.md`               |

## 📁 Output Files

Results are saved in the `./job-posts/` directory:

- **JSON files**: Structured job data for further processing
- **Markdown files**: Human-readable analysis and recommendations
- **Analysis files**: Career guidance and market insights
- **Message files**: LinkedIn messages and cold emails

### Multi-Agent Workflow

The system uses a collaborative approach where agents build upon each other's work:

1. **JobSearchAgent** writes initial job search results to files
2. **AnalysisAgent** reads these results using `docs_tool` and `file_tool` to provide comprehensive analysis
3. **MessageWriterAgent** accesses the job data to create personalized outreach messages

This workflow ensures that each agent has access to the complete context of previous searches and analyses, enabling more intelligent and comprehensive results.

## 🔧 Troubleshooting

### Common Issues

1. **API Key Errors**:

   - Verify your `.env` file has correct API keys
   - Check API key permissions and quotas

2. **Rate Limiting**:

   - The tool automatically retries with delays
   - Consider upgrading your SerpAPI plan for higher limits

3. **No Results Found**:

   - Try broader search terms
   - Check if your location preference is too restrictive
   - Verify your required skills aren't too specific

4. **Import Errors**:

   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility

5. **File Access Issues**:
   - Ensure the `./job-posts/` directory exists and is writable
   - Check file permissions if agents can't read previous results
   - Verify that search results are being written to the output directory

### Debug Mode

Enable verbose logging by setting `verbose=True` in crew configurations.

### Understanding Agent Collaboration

The system uses file-based communication between agents:

- If **AnalysisAgent** reports "No previous results found", ensure JobSearchAgent completed successfully
- If **MessageWriterAgent** can't create personalized messages, check that job search results exist in `./job-posts/`
- The `docs_tool` and `file_tool` are essential for agent collaboration - don't remove them

## 🔄 How the Multi-Agent System Works

### Agent Collaboration Flow

1. **Search Phase**: JobSearchAgent performs job searches and saves results to `./job-posts/`
2. **Analysis Phase**: AnalysisAgent reads the search results using file tools and provides strategic insights
3. **Outreach Phase**: MessageWriterAgent accesses job data to create personalized LinkedIn messages and emails

### File-Based Communication

- **docs_tool**: Reads all markdown files from the job-posts directory for comprehensive analysis
- **file_tool**: Accesses specific files when agents need detailed information
- **Output Files**: Serve as the communication medium between agents

This architecture ensures each agent builds upon previous work, creating a comprehensive job search experience.

## 🎯 Search Strategies

### For Different Experience Levels

**Entry Level (0-2 years)**:

```bash
# Use entry_level search type
python run_search.py
# Choose option 4
```

**Mid-Level (3-7 years)**:

```bash
# Use standard or salary_focused search
# Adjust years and level in config.py
```

**Senior Level (8+ years)**:

```bash
# Use company_targeted search
# Focus on specific companies and senior roles
```

### For Different Goals

**Salary Optimization**:

- Use `salary_focused` search
- Set specific min/max salary ranges
- Focus on high-paying markets

**Company Targeting**:

- Use `company_targeted` search
- Research specific companies first
- Customize target_companies list

**Quick Job Change**:

- Use `quick` search for immediate results
- Follow up with `full` search for top picks

## 📊 Understanding Results

### Job Analysis Includes:

- **Role Matching**: How well jobs match your skills
- **Salary Analysis**: Compensation insights and trends
- **Skill Gaps**: Areas for professional development
- **Market Trends**: Oracle job market insights
- **Career Progression**: Growth opportunities

### Outreach Messages Include:

- **LinkedIn Messages**: Personalized recruiter outreach
- **Cold Emails**: Direct company contact templates
- **Application Tips**: How to stand out for each role

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add new search tools or agents
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:

1. Check the troubleshooting section
2. Review the configuration options
3. Open an issue on GitHub

## 🔮 Future Enhancements

- [ ] Integration with job boards (Indeed, LinkedIn Jobs)
- [ ] Resume matching and optimization
- [ ] Interview preparation based on job requirements
- [ ] Salary negotiation guidance
- [ ] Application tracking system
- [ ] Company culture analysis
- [ ] Skills assessment and certification recommendations

---

**Happy Job Hunting! 🎯**
