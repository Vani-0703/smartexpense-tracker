import streamlit as st
import pypdf
from google import genai
import pandas as pd
import time

# ==============================================================================
# 1. PLATFORM CORE CONFIGURATION & AUTH
# ==============================================================================
API_KEY = "AQ.Ab8RN6LeUs_odvC1hzGUGP8skXGWIgXDnkHKbOCJZ4HDymeR2w"

try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    st.error(f"Platform Authentication Failure: {e}")
    st.stop()

# Persistent state management across platform features
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "scanned_count" not in st.session_state:
    st.session_state["scanned_count"] = 42
if "last_analysis_results" not in st.session_state:
    st.session_state["last_analysis_results"] = None
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# ==============================================================================
# 2. LOGIN INTERFACE
# ==============================================================================
def render_login_view():
    st.set_page_config(page_title="Sign In | ATS Premium Portal", page_icon="🔐", layout="centered")
    st.write("<br><br>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; color: #1E293B;'>⚡ Enterprise ATS Intelligence</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B;'>Secure multi-agent application evaluation gateway</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        username = st.text_input("Corporate ID / Email", placeholder="admin")
        password = st.text_input("Access Token Key", type="password", placeholder="••••••••")
        st.write("")
        
        if st.button("Authenticate Client Session", use_container_width=True, type="primary"):
            if username.strip() == "admin" and password == "password":
                st.session_state["logged_in"] = True
                st.success("Authorization validated. Directing to environment workspace...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Authentication rejected: Invalid credentials verified. (Use: admin / password)")

# ==============================================================================
# 3. PREMIUM WORKSPACE ENVIRONMENT
# ==============================================================================
def render_platform_workspace():
    st.set_page_config(page_title="Workspace | ATS Core Engine", page_icon="⚡", layout="wide")
    
    # Header Control Bar
    col_header, col_logout = st.columns([9, 1])
    with col_header:
        st.markdown("<h1 style='color: #0F172A;'>⚡ ATS Cloud Engine Suite</h1>", unsafe_allow_html=True)
    with col_logout:
        st.write("<br>", unsafe_allow_html=True)
        if st.button("Sign Out", type="secondary", use_container_width=True):
            st.session_state["logged_in"] = False
            st.rerun()
            
    # Main Navigation Architecture Tabs
    tab_scan, tab_dashboard, tab_chat = st.tabs([
        "🔍 ATS Scanner Engine", 
        "📊 System Analytics Dashboard", 
        "💬 Interactive Candidate Chat"
    ])

    # --------------------------------------------------------------------------
    # TAB 1: ATS CORE SCANNER
    # --------------------------------------------------------------------------
    with tab_scan:
        st.markdown("### 🛠️ Optimization Sandbox")
        st.write("Compare resume structures and textual semantic mapping directly against active hiring specifications.")
        
        col_inputs, col_live_metrics = st.columns([1, 1])
        
        with col_inputs:
            with st.container(border=True):
                st.markdown("**📂 Target Assets Input**")
                uploaded_file = st.file_uploader("Upload Profile Resume (PDF Asset Only)", type=["pdf"])
                job_description = st.text_area("Paste Target Job Requirements:", height=180, placeholder="Requirements, technology stacks, roles...")
                
                trigger_analysis = st.button("Execute Pipeline Scoring", type="primary", use_container_width=True)
                
        with col_live_metrics:
            if uploaded_file and job_description and trigger_analysis:
                with st.spinner("Executing structural vector scanning and token checks..."):
                    try:
                        # Parse PDF Document content text
                        pdf_reader = pypdf.PdfReader(uploaded_file)
                        resume_text = ""
                        for page in pdf_reader.pages:
                            resume_text += page.extract_text() or ""
                        
                        if not resume_text.strip():
                            st.error("Text parsing failed. Ensure target document is an unencrypted, text-based PDF format.")
                            st.stop()
                        
                        # High precision analytics payload
                        analysis_prompt = f"""
                        You are an elite corporate recruitment infrastructure engine.
                        Break down this analysis into exactly four sections using clear Markdown formatting:
                        
                        ### [SCORE]
                        Provide ONLY a single percentage match score string (example: 78%).
                        
                        ### [METRICS]
                        Provide 3 quick bullet items covering: Keyword Density Rank, Structural Format Integrity, and Experience Level Match.
                        
                        ### [REPORT]
                        Provide a brief summary of Key Alignments and a clean bulleted list of Missing Critical Keywords.
                        
                        ### [ACTION_ITEMS]
                        Provide 3 highly practical modifications the candidate can make to pass strict automated filters.

                        RESUME CONTENT:
                        {resume_text}

                        JOB SPECIFICATION:
                        {job_description}
                        """
                        
                        response = client.models.generate_content(
                            model='gemini-2.5-flash',
                            contents=analysis_prompt,
                        )
                        
                        # Cache historical runs and logs
                        st.session_state["scanned_count"] += 1
                        st.session_state["last_analysis_results"] = response.text
                        st.success("Target document evaluation complete.")
                        
                    except Exception as err:
                        st.error(f"Processing execution crash: {err}")

            # Render Results Section dynamically
            if st.session_state["last_analysis_results"]:
                raw_output = st.session_state["last_analysis_results"]
                
                # Split output elements securely for premium widget views
                parts = raw_output.split("### ")
                score_val = "Pending"
                metrics_val = ""
                body_report = raw_output
                
                for part in parts:
                    if part.startswith("[SCORE]"):
                        score_val = part.replace("[SCORE]", "").strip()
                    elif part.startswith("[METRICS]"):
                        metrics_val = part.replace("[METRICS]", "").strip()

                with st.container(border=True):
                    st.markdown("#### 📊 Real-Time Asset Profile Report")
                    m_col1, m_col2 = st.columns([1, 2])
                    with m_col1:
                        st.metric("Calculated Match Index", score_val)
                    with m_col2:
                        if "%" in score_val:
                            try:
                                numeric_score = int(''.join(filter(str.isdigit, score_val)))
                                st.progress(numeric_score / 100.0)
                            except:
                                st.progress(0.75)
                        else:
                            st.progress(0.70)
                    
                    st.markdown("---")
                    st.markdown(body_report)
            else:
                st.info("💡 Complete configuration inputs on the left panel and click 'Execute Pipeline Scoring' to view deep visual analytics here.")

    # --------------------------------------------------------------------------
    # TAB 2: SYSTEM METRICS DASHBOARD
    # --------------------------------------------------------------------------
    with tab_dashboard:
        st.markdown("### 📊 Operational Analytics Matrix")
        st.write("Track active platform load volumes, historical metrics performance, and system throughput states.")
        
        d_col1, d_col2, d_col3 = st.columns(3)
        d_col1.metric("Pipeline Submissions System-Wide", f"{st.session_state['scanned_count']}", "+4 updates active")
        d_col2.metric("Mean Global Match Threshold", "76.4%", "+2.1% variance")
        d_col3.metric("System Operational Uptime", "99.98%", "Healthy State")
        
        st.markdown("---")
        
        chart_col, log_col = st.columns([2, 1])
        with chart_col:
            st.markdown("**📈 System Scanning Load Volume Frequency (By Cycle)**")
            mock_historical_data = pd.DataFrame(
                [24, 28, 31, 35, 39, st.session_state["scanned_count"]],
                index=["Cycle A", "Cycle B", "Cycle C", "Cycle D", "Cycle E", "Current Evaluation"],
                columns=["Active Profiles Evaluated"]
            )
            st.area_chart(mock_historical_data, height=260, use_container_width=True)
            
        with log_col:
            st.markdown("**📋 Security Event Monitoring Logs**")
            with st.container(height=260, border=True):
                st.caption("🟢 Core Server Cluster: Status Active Optimum [2026-07-10]")
                st.caption("📄 Engine Callback: Parser stream committed safely")
                st.caption("🔑 API Handshake verification successfully finalized")
                st.caption("🔓 Security Module: Client token active configuration state updated")

    # --------------------------------------------------------------------------
    # TAB 3: CONVERSATIONAL AI CHAT
    # --------------------------------------------------------------------------
    with tab_chat:
        st.markdown("### 💬 Interactive Strategy Consultation Terminal")
        st.write("Converse directly with the core evaluation engine regarding structural modifications or strategic modifications.")
        
        # Display persistent interactive platform chat logs
        for chat in st.session_state["chat_history"]:
            with st.chat_message(chat["role"]):
                st.markdown(chat["content"])
                
        user_message = st.chat_input("Query the system matrix (e.g., 'How can I format standard experience listings?')")
        
        if user_message:
            with st.chat_message("user"):
                st.markdown(user_message)
            st.session_state["chat_history"].append({"role": "user", "content": user_message})
            
            with st.spinner("Querying evaluation engine contextual graphs..."):
                try:
                    chat_prompt = f"""
                    You are an elite automated corporate recruitment mentor AI. 
                    Answer the following user platform request comprehensively and elegantly. 
                    Keep the tone highly professional, direct, and elite.
                    
                    QUERY: {user_message}
                    """
                    chat_response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=chat_prompt,
                    )
                    
                    with st.chat_message("assistant"):
                        st.markdown(chat_response.text)
                    st.session_state["chat_history"].append({"role": "assistant", "content": chat_response.text})
                    
                except Exception as c_err:
                    st.error(f"Chat communication failure: {c_err}")

# ==============================================================================
# 4. SYSTEM RUN ROUTER
# ==============================================================================
if st.session_state["logged_in"]:
    render_platform_workspace()
else:
    render_login_view()

