import streamlit as st
from crew import run_crew
from tools import perform_web_search, format_search_results

# ─────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🤖",
    layout="wide"
)

# ─────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #0f1117; }

    .report-box {
        background: #1e1e2e;
        border-left: 4px solid #7c3aed;
        padding: 24px;
        border-radius: 10px;
        color: #e0e0e0;
        line-height: 1.8;
        font-size: 1rem;
    }

    .agent-step {
        background: #12121f;
        border-left: 3px solid #1e88e5;
        padding: 10px 16px;
        border-radius: 6px;
        color: #90caf9;
        margin: 6px 0;
        font-size: 0.9em;
        font-family: monospace;
    }

    .stat-box {
        background: #1e1e2e;
        border: 1px solid #333;
        padding: 16px;
        border-radius: 8px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────
st.markdown("""
    <h1 style='text-align:center'>🤖 AI Research Agent</h1>
    <p style='text-align:center; color:#888'>
        Powered by CrewAI — 3 agents working together to research any topic
    </p>
""", unsafe_allow_html=True)

st.divider()

# ─────────────────────────────────────────
# HOW IT WORKS
# ─────────────────────────────────────────
with st.expander("⚙️ How it works"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        **🔍 Agent 1: Researcher**
        Searches the web and gathers raw information from multiple sources
        """)
    with col2:
        st.markdown("""
        **🧠 Agent 2: Analyst**
        Analyzes findings, spots trends, and rates importance of each insight
        """)
    with col3:
        st.markdown("""
        **✍️ Agent 3: Writer**
        Transforms analysis into a professional structured report
        """)

st.divider()

# ─────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────
if "report" not in st.session_state:
    st.session_state.report = None

if "topic" not in st.session_state:
    st.session_state.topic = ""

# ─────────────────────────────────────────
# INPUT SECTION
# ─────────────────────────────────────────
st.markdown("### 🎯 Enter Research Topic")

# Example topics
examples = [
    "AI trends in healthcare 2026",
    "Quantum computing breakthroughs",
    "Electric vehicle market growth",
    "Generative AI in education",
    "Climate tech innovations",
]

st.markdown("**💡 Try these examples:**")
cols = st.columns(len(examples))
for i, ex in enumerate(examples):
    if cols[i].button(ex, key=f"ex_{i}"):
        st.session_state.topic = ex

# Main input
topic = st.text_input(
    "Topic",
    value=st.session_state.topic,
    placeholder="e.g. Latest breakthroughs in quantum computing...",
    label_visibility="collapsed"
)

# Run button
run_clicked = st.button(
    "🚀 Launch Research Crew",
    use_container_width=True,
    type="primary"
)

# ─────────────────────────────────────────
# RUN CREW
# ─────────────────────────────────────────
if run_clicked:
    if not topic.strip():
        st.warning("⚠️ Please enter a research topic!")
    else:
        st.session_state.topic = topic
        st.session_state.report = None

        # Progress display
        st.divider()
        st.markdown("### ⚡ Agent Progress")

        progress_bar = st.progress(0, text="Initializing crew...")

        col1, col2, col3 = st.columns(3)
        s1 = col1.empty()
        s2 = col2.empty()
        s3 = col3.empty()

        s1.markdown("<div class='agent-step'>🔍 Researcher: Waiting...</div>",
                    unsafe_allow_html=True)
        s2.markdown("<div class='agent-step'>🧠 Analyst: Waiting...</div>",
                    unsafe_allow_html=True)
        s3.markdown("<div class='agent-step'>✍️ Writer: Waiting...</div>",
                    unsafe_allow_html=True)

        # Update progress
        progress_bar.progress(10, text="🔍 Researcher searching the web...")
        s1.markdown("<div class='agent-step'>🔍 Researcher: Working... 🟡</div>",
                    unsafe_allow_html=True)

        try:
            # Run the crew
            with st.spinner("🔍 Searching the web for live data..."):
                raw_results = perform_web_search(topic)
                search_context = format_search_results(raw_results)

            report = run_crew(topic, search_context)

            # Update UI after completion
            progress_bar.progress(100, text="✅ Report complete!")
            s1.markdown("<div class='agent-step'>🔍 Researcher: Done ✅</div>",
                        unsafe_allow_html=True)
            s2.markdown("<div class='agent-step'>🧠 Analyst: Done ✅</div>",
                        unsafe_allow_html=True)
            s3.markdown("<div class='agent-step'>✍️ Writer: Done ✅</div>",
                        unsafe_allow_html=True)

            st.session_state.report = report
            st.rerun()

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("💡 Tip: Check your .env file and API key!")

# ─────────────────────────────────────────
# DISPLAY REPORT
# ─────────────────────────────────────────
if st.session_state.report:
    st.divider()
    st.markdown("### 📄 Research Report")

    # Stats row
    word_count = len(st.session_state.report.split())
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div class='stat-box'>📝 <b>{word_count}</b><br>Words</div>",
                unsafe_allow_html=True)
    c2.markdown(f"<div class='stat-box'>🤖 <b>3</b><br>Agents Used</div>",
                unsafe_allow_html=True)
    c3.markdown(f"<div class='stat-box'>🔍 <b>5+</b><br>Sources Searched</div>",
                unsafe_allow_html=True)

    st.markdown("")

    # Report content
    st.markdown(
        f"<div class='report-box'>{st.session_state.report}</div>",
        unsafe_allow_html=True
    )

    st.divider()

    # Download button
    st.download_button(
        label="⬇️ Download Report",
        data=st.session_state.report,
        file_name=f"research_{topic[:30].replace(' ', '_')}.txt",
        mime="text/plain",
        use_container_width=True
    )
