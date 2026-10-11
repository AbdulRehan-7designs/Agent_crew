# tasks.py
# PURPOSE: Define tasks for each agent

import datetime
from crewai import Task, Agent


def create_research_task(agent: Agent, topic: str, search_context: str) -> Task:
    """Create a research task for the given topic."""
    return Task(
        description=(
            f"Conduct comprehensive research on the following topic:\n\n"
            f"'{topic}'\n\n"
            f"Use the following recent web search results as your primary source of truth:\n"
            f"--- WEB SEARCH RESULTS ---\n"
            f"{search_context}\n"
            f"--------------------------\n\n"
            f"Your research should cover:\n"
            f"1. Key concepts and definitions\n"
            f"2. Current trends and developments\n"
            f"3. Important facts and statistics\n"
            f"4. Different perspectives and viewpoints\n"
            f"5. Potential implications and future outlook\n\n"
            f"Provide a detailed research brief with organized findings."
        ),
        expected_output=(
            "A comprehensive research brief with clearly organized sections, "
            "key findings, relevant data points, and source references."
        ),
        agent=agent,
    )


def create_analysis_task(agent: Agent, topic: str, context: list[Task] = None) -> Task:
    """Create an analysis task based on research findings."""
    return Task(
        description=(
            f"Analyze the research findings on '{topic}' and extract:\n\n"
            f"1. The most important insights and key takeaways\n"
            f"2. Emerging trends and patterns\n"
            f"3. Strengths, weaknesses, opportunities, and threats\n"
            f"4. Actionable recommendations\n"
            f"5. Data-backed conclusions\n\n"
            f"Focus on what truly matters — cut through the noise."
        ),
        expected_output=(
            "A structured analysis with ranked insights, identified trends, "
            "and clear actionable recommendations. Should be concise but thorough."
        ),
        agent=agent,
        context=context or [],
    )


def create_writing_task(agent: Agent, topic: str, context: list[Task] = None) -> Task:
    """Create a report writing task based on analysis."""
    return Task(
        description=(
            f"Using the research and analysis provided, write a professional "
            f"report on:\n\n"
            f"'{topic}'\n\n"
            f"The report should:\n"
            f"1. Have a compelling executive summary\n"
            f"2. Be well-structured with clear headings and subheadings\n"
            f"3. Present information in an accessible and engaging manner\n"
            f"4. Include relevant examples and data points\n"
            f"5. End with conclusions and key recommendations\n\n"
            f"Target length: 800-1200 words. Use markdown formatting.\n"
            f"IMPORTANT: The current date is {datetime.date.today().strftime('%B %d, %Y')}. Ensure the report uses this as the current date."
        ),
        expected_output=(
            "A polished, publication-ready report in markdown format with "
            "a compelling title, organized sections, data-backed insights, "
            "and a clear conclusion with recommendations."
        ),
        agent=agent,
        context=context or [],
    )
