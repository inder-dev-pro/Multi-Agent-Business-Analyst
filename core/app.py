import streamlit as st
import sys
import os
from pathlib import Path

# Add the project root directory to the Python path
project_root = str(Path(__file__).parent.parent)
sys.path.append(project_root)

# Import dependencies
try:
    from crewai import Crew, Process
    from agents.market_research_agent import MarketResearchAgent
    from agents.idea_viability_agent import IdeaViabilityAgent
    from agents.funding_advisor_agent import FundingAdvisorAgent
    from tasks.research_task import MarketResearchTask
    from tasks.idea_viability_task import IdeaViabilityTask
    from tasks.funding_task import FundingTask
    from dotenv import load_dotenv
except ImportError as e:
    st.error(f"❌ Import Error: {e}")
    st.stop()

# Load environment variables
env_path = os.path.join(project_root, "config", ".env")
if os.path.exists(env_path):
    load_dotenv(env_path)
else:
    st.warning(f"⚠️ .env file not found at {env_path}")

st.set_page_config(page_title="Business Analysis Suite", page_icon="📊", layout="wide")

def run_analysis(business_idea):
    try:
        market_research_agent = MarketResearchAgent(topic=business_idea)
        idea_viability_agent = IdeaViabilityAgent(idea=business_idea)
        funding_advisor_agent = FundingAdvisorAgent(idea=business_idea)

        market_research_task = MarketResearchTask(topic=business_idea)
        idea_viability_task = IdeaViabilityTask(idea=business_idea)
        funding_task = FundingTask(idea=business_idea)

        crew = Crew(
            agents=[market_research_agent, idea_viability_agent, funding_advisor_agent],
            tasks=[market_research_task, idea_viability_task, funding_task],
            verbose=True,
            process=Process.sequential
        )
        results = crew.kickoff()
        # Always wrap results in a dict if tuple/list of length 3
        if isinstance(results, (tuple, list)) and len(results) == 3:
            return {
                'market_research': results[0],
                'idea_viability': results[1],
                'funding_strategy': results[2]
            }
        # If already a dict, return as is
        if isinstance(results, dict):
            return results
        # Otherwise, raise error
        raise ValueError("Analysis did not return expected results.")
    except Exception as e:
        st.error(f"❌ Analysis Error: {e}")
        return None

def main():
    st.title("Business Analysis Suite")
    st.markdown("""
    Enter your business idea below to receive:
    - Market Research
    - Idea Viability Assessment
    - Funding Strategy
    """)

    business_idea = st.text_area("Describe your business idea:", height=120)
    if st.button("Analyze Business Idea"):
        if not business_idea.strip():
            st.error("❌ Please enter a business idea to analyze.")
            return
        with st.spinner("Analyzing your business idea..."):
            results = run_analysis(business_idea)
            if isinstance(results, dict):
                st.subheader("Market Research")
                st.markdown(results['market_research'])
                st.subheader("Idea Viability")
                st.markdown(results['idea_viability'])
                st.subheader("Funding Strategy")
                st.markdown(results['funding_strategy'])
                st.download_button(
                    label="Download Full Report",
                    data=f"""# Business Analysis Report

## Business Idea
{business_idea}

## Market Research
{results['market_research']}

## Idea Viability
{results['idea_viability']}

## Funding Strategy
{results['funding_strategy']}
""",
                    file_name="business_analysis_report.md",
                    mime="text/markdown"
                )
            else:
                st.error("❌ No results to display. Please try again.")

if __name__ == "__main__":
    main()