# agents.py
# PURPOSE: Define each AI agent with role, goal, backstory

from crewai import Agent

def create_researcher():
    return Agent(
        role="Senior Research Analyst",
        goal=(
            "Find comprehensive, accurate, and up-to-date information "
            "on the given topic using web search."
        ),
        backstory=(
            "You are an expert research analyst with 10 years of experience "
            "in gathering and synthesizing information from multiple sources. "
            "You are thorough, detail-oriented, and always verify facts."
        ),
        tools=[], # Removed web_search because OpenRouter free models don't support tool calling
        verbose=True,           # Shows thinking process in terminal
        allow_delegation=False, # This agent doesn't delegate to others
        max_iter=5,             # Max reasoning iterations
    )


def create_analyst():
    return Agent(
        role="Data Analyst",
        goal=(
            "Analyze raw research findings and extract the most important "
            "insights, trends, and key takeaways."
        ),
        backstory=(
            "You are a sharp analytical thinker who specializes in finding "
            "patterns and meaning in large amounts of information. "
            "You cut through noise and focus on what truly matters."
        ),
        tools=[],               # Analyst doesn't search — only thinks
        verbose=True,
        allow_delegation=False,
    )


def create_writer():
    return Agent(
        role="Professional Report Writer",
        goal=(
            "Transform analyzed insights into a clear, engaging, "
            "well-structured professional report."
        ),
        backstory=(
            "You are an experienced technical writer who can explain "
            "complex topics in a clear and compelling way. "
            "Your reports are always well-structured, concise, and impactful."
        ),
        tools=[],
        verbose=True,
        allow_delegation=False,
    )