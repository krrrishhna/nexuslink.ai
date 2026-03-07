"""
NexusLink AI — Job Matching & Career Tools
"""


def register_jobs_tools(mcp):

    @mcp.tool()
    def match_job_keywords(job_description: str, resume_skills: str) -> str:
        """
        Compare a job description against your skills to find keyword gaps.
        
        Args:
            job_description: Full text of the job posting
            resume_skills: Comma-separated list of your current skills
        """
        my_skills = set(s.strip().lower() for s in resume_skills.split(","))
        jd_words = set(job_description.lower().split())

        # Common tech/business keywords to look for
        keyword_categories = {
            "technical": ["python", "java", "sql", "aws", "docker", "kubernetes", "react", 
                         "node", "api", "cicd", "agile", "scrum", "jira", "git", "cloud",
                         "machine learning", "data", "analytics", "ios", "android"],
            "soft_skills": ["leadership", "communication", "collaboration", "strategic",
                           "stakeholder", "cross-functional", "mentoring", "presenting"],
            "pm_specific": ["roadmap", "backlog", "sprint", "user stories", "okr", "kpi",
                           "product strategy", "a/b testing", "market research", "prioritization"],
        }

        matches = []
        gaps = []

        for category, keywords in keyword_categories.items():
            for kw in keywords:
                if kw in jd_words or kw in " ".join(jd_words):
                    if kw in my_skills:
                        matches.append(f"✅ {kw}")
                    else:
                        gaps.append(f"❌ {kw} (consider adding)")

        result = "🎯 Keyword Match Report\n\n"
        result += f"Matched Skills ({len(matches)}):\n" + "\n".join(matches) + "\n\n"
        result += f"Missing Keywords ({len(gaps)}):\n" + "\n".join(gaps)
        return result

    @mcp.tool()
    def generate_cover_letter_outline(company: str, role: str, why_interested: str) -> str:
        """
        Generate a structured cover letter outline for a specific role.
        
        Args:
            company: Target company name
            role: Job title you're applying for
            why_interested: Brief reason you're interested in this role
        """
        outline = f"""Cover Letter Outline — {role} at {company}

OPENING (2-3 sentences):
- Lead with a specific detail about {company} that excites you
- State the role and how you discovered it
- One-line value proposition

BODY PARAGRAPH 1 — Relevant Experience:
- Most relevant project or role that maps to this position
- Quantify impact where possible (%, $, users, etc.)

BODY PARAGRAPH 2 — Why {company}:
- {why_interested}
- Connect your values/goals to the company's mission
- Show you've done research

BODY PARAGRAPH 3 — Unique Value:
- What you bring that other candidates likely don't
- Bridge any experience gaps with transferable skills

CLOSING (2-3 sentences):
- Reiterate enthusiasm
- Clear call to action
- Professional sign-off
"""
        return outline
