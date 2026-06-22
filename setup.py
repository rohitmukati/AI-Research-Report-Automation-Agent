import os
import sys

# PROJECT_NAME = "ai_research_agent"

STRUCTURE = {
    # ─── ROOT FILES ────────────────────────────────────────────
    ".env.example": "",
    ".gitignore": "",
    "requirements.txt": "",
    "docker-compose.yml": "",
    "README.md": "",

    # ─── BACKEND ───────────────────────────────────────────────
    "backend/__init__.py": "",
    "backend/main.py": "",
    "backend/config.py": "",
    "backend/dependencies.py": "",

    # Auth
    "backend/auth/__init__.py": "",
    "backend/auth/router.py": "",
    "backend/auth/service.py": "",
    "backend/auth/schemas.py": "",
    "backend/auth/utils.py": "",
    "backend/auth/jwt_handler.py": "",
    "backend/auth/email_service.py": "",

    # Research routes
    "backend/research/__init__.py": "",
    "backend/research/router.py": "",
    "backend/research/service.py": "",
    "backend/research/schemas.py": "",
    "backend/research/websocket_manager.py": "",

    # Memory routes
    "backend/memory/__init__.py": "",
    "backend/memory/router.py": "",
    "backend/memory/service.py": "",
    "backend/memory/schemas.py": "",

    # Database
    "backend/db/__init__.py": "",
    "backend/db/client.py": "",
    "backend/db/models.py": "",
    "backend/db/migrations/001_initial.sql": "",
    "backend/db/migrations/002_memory_embeddings.sql": "",
    "backend/db/migrations/003_agent_logs.sql": "",

    # ─── LANGGRAPH AGENTS ──────────────────────────────────────
    "backend/agents/__init__.py": "",

    # Graph definition
    "backend/agents/graph/__init__.py": "",
    "backend/agents/graph/builder.py": "",
    "backend/agents/graph/state.py": "",
    "backend/agents/graph/edges.py": "",
    "backend/agents/graph/nodes.py": "",

    # Individual agents
    "backend/agents/orchestrator/__init__.py": "",
    "backend/agents/orchestrator/agent.py": "",
    "backend/agents/orchestrator/prompts.py": "",

    "backend/agents/planner/__init__.py": "",
    "backend/agents/planner/agent.py": "",
    "backend/agents/planner/prompts.py": "",

    "backend/agents/search/__init__.py": "",
    "backend/agents/search/agent.py": "",
    "backend/agents/search/tools.py": "",
    "backend/agents/search/prompts.py": "",

    "backend/agents/analysis/__init__.py": "",
    "backend/agents/analysis/agent.py": "",
    "backend/agents/analysis/prompts.py": "",

    "backend/agents/writer/__init__.py": "",
    "backend/agents/writer/agent.py": "",
    "backend/agents/writer/prompts.py": "",
    "backend/agents/writer/formatters.py": "",

    "backend/agents/reviewer/__init__.py": "",
    "backend/agents/reviewer/agent.py": "",
    "backend/agents/reviewer/prompts.py": "",
    "backend/agents/reviewer/scorer.py": "",

    # Memory managers
    "backend/agents/memory/__init__.py": "",
    "backend/agents/memory/short_term.py": "",
    "backend/agents/memory/long_term.py": "",
    "backend/agents/memory/retriever.py": "",
    "backend/agents/memory/embeddings.py": "",

    # Shared tools
    "backend/agents/tools/__init__.py": "",
    "backend/agents/tools/tavily_search.py": "",
    "backend/agents/tools/pdf_generator.py": "",
    "backend/agents/tools/summarizer.py": "",

    # ─── FRONTEND ──────────────────────────────────────────────
    "frontend/app.py": "",
    "frontend/config.py": "",
    "frontend/api_client.py": "",

    "frontend/pages/__init__.py": "",
    "frontend/pages/login.py": "",
    "frontend/pages/signup.py": "",
    "frontend/pages/forgot_password.py": "",
    "frontend/pages/reset_password.py": "",
    "frontend/pages/dashboard.py": "",
    "frontend/pages/new_research.py": "",
    "frontend/pages/history.py": "",
    "frontend/pages/report_viewer.py": "",
    "frontend/pages/profile.py": "",

    "frontend/components/__init__.py": "",
    "frontend/components/agent_progress.py": "",
    "frontend/components/report_card.py": "",
    "frontend/components/sidebar.py": "",
    "frontend/components/auth_guard.py": "",
    "frontend/components/memory_panel.py": "",

    "frontend/utils/__init__.py": "",
    "frontend/utils/session_state.py": "",
    "frontend/utils/formatters.py": "",
    "frontend/utils/websocket_client.py": "",

    "frontend/assets/style.css": "",

    # ─── TESTS ─────────────────────────────────────────────────
    "tests/__init__.py": "",
    "tests/test_auth.py": "",
    "tests/test_agents.py": "",
    "tests/test_memory.py": "",
    "tests/test_research.py": "",
    "tests/conftest.py": "",

    # ─── SCRIPTS ───────────────────────────────────────────────
    "scripts/seed_db.py": "",
    "scripts/test_agents.py": "",
    "scripts/generate_migration.py": "",
}


def create_structure(base_path: str):
    created_files = 0
    created_dirs = 0

    for rel_path in STRUCTURE.keys():
        full_path = os.path.join(base_path, rel_path)
        dir_path = os.path.dirname(full_path)

        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
            created_dirs += 1

        if not os.path.exists(full_path):
            with open(full_path, "w") as f:
                f.write("")
            created_files += 1

    return created_dirs, created_files


def print_tree(base_path: str):
    print(f"\n📁 {os.path.basename(base_path)}/")
    for root, dirs, files in os.walk(base_path):
        dirs[:] = sorted([d for d in dirs if d not in ["__pycache__", ".git"]])
        level = root.replace(base_path, "").count(os.sep)
        indent = "    " * level
        folder = os.path.basename(root)
        if level > 0:
            print(f"{indent}📂 {folder}/")
        for f in sorted(files):
            print(f"{'    ' * (level + 1)}📄 {f}")


def main():
    print("=" * 55)
    print("  AI Research & Report Automation System — Setup")
    print("=" * 55)

    base = os.getcwd()   # Current folder hi project root hoga

    print(f"\n🚀 Creating project at: {base}\n")
    dirs, files = create_structure(base)

    print_tree(base)

    print("\n" + "=" * 55)
    print(f"  ✅ Done!  {dirs} folders  |  {files} files created")
    print("=" * 55)
    print("""
📌 Next Steps:
─────────────────────────────────────────────────────
1. Create virtual env:  python -m venv venv
2. Activate:            venv\\Scripts\\activate
3. Copy env file:       .env.example -> .env
4. Fill .env with your Supabase, OpenAI, Tavily keys
5. Install deps:        pip install -r requirements.txt
─────────────────────────────────────────────────────
Backend:   cd backend && uvicorn main:app --reload
Frontend:  cd frontend && streamlit run app.py
─────────────────────────────────────────────────────
""")


if __name__ == "__main__":
    main()