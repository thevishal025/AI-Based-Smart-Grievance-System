css_content = """
/* =========================================
   MODERN UI REDESIGN - DARK GLASSMORPHISM
   ========================================= */

:root {
    --primary: #00d2ff;
    --primary-dark: #0088cc;
    --accent: #3a7bd5;
    --bg: #050505;
    --surface: rgba(20, 20, 25, 0.45);
    --surface-alt: rgba(35, 35, 45, 0.4);
    --text: #f0f0f0;
    --muted: #a0a0a0;
    --border: rgba(255, 255, 255, 0.08);
    --danger: #ff4757;
    --warning: #ffa502;
    --success: #2ed573;
    --shadow-sm: 0 4px 20px rgba(0, 0, 0, 0.3);
    --shadow-md: 0 10px 40px rgba(0, 0, 0, 0.5);
    --glow-primary: 0 0 15px rgba(0, 210, 255, 0.5);
    --glow-hover: 0 0 25px rgba(0, 210, 255, 0.8);
}

body {
    background: #050505;
    color: var(--text);
}

/* Background Animated Blobs */
.blob {
    position: fixed;
    border-radius: 50%;
    filter: blur(80px);
    z-index: 0;
    opacity: 0.6;
    animation: float 20s infinite ease-in-out;
}
.blob-1 {
    top: -10%;
    left: -10%;
    width: 50vw;
    height: 50vw;
    background: radial-gradient(circle, rgba(0,210,255,0.15) 0%, rgba(0,0,0,0) 70%);
    animation-delay: 0s;
}
.blob-2 {
    bottom: -20%;
    right: -10%;
    width: 60vw;
    height: 60vw;
    background: radial-gradient(circle, rgba(58,123,213,0.15) 0%, rgba(0,0,0,0) 70%);
    animation-delay: -5s;
}
@keyframes float {
    0% { transform: translate(0, 0) scale(1); }
    33% { transform: translate(5%, 5%) scale(1.1); }
    66% { transform: translate(-5%, 2%) scale(0.9); }
    100% { transform: translate(0, 0) scale(1); }
}

.app-shell {
    z-index: 10;
    background: transparent;
}

/* Glassmorphism */
.app-sidebar,
.topbar,
.kpi-shell,
.filter-shell,
.complaint-card,
.form-shell,
.chatbot-panel,
.toast-item,
.menu-panel,
.modal-content,
.login-card {
    background: var(--surface) !important;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--border) !important;
    box-shadow: var(--shadow-sm) !important;
}

/* Enhancements */
.app-sidebar {
    background: rgba(10, 10, 15, 0.6) !important;
}
.topbar {
    background: rgba(10, 10, 15, 0.6) !important;
}

.kpi-shell, .complaint-card, .form-shell, .filter-shell {
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.kpi-shell:hover, .complaint-card:hover {
    transform: translateY(-5px);
    border-color: rgba(0, 210, 255, 0.4) !important;
    box-shadow: var(--shadow-md), var(--glow-primary) !important;
}

/* Buttons */
.btn-primary, button[type="submit"] {
    background: linear-gradient(135deg, #00d2ff, #3a7bd5) !important;
    color: #fff !important;
    border: none !important;
    box-shadow: var(--glow-primary) !important;
    transition: all 0.3s ease !important;
    font-weight: 600;
    letter-spacing: 0.5px;
}
.btn-primary:hover, button[type="submit"]:hover {
    box-shadow: var(--glow-hover) !important;
    transform: translateY(-2px) scale(1.02);
}
.btn-secondary, .btn-ghost, .btn-outline {
    background: rgba(255,255,255,0.05) !important;
    color: var(--text) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
}
.btn-secondary:hover, .btn-ghost:hover, .btn-outline:hover {
    background: rgba(255,255,255,0.1) !important;
    border-color: rgba(255,255,255,0.3) !important;
    box-shadow: 0 0 10px rgba(255,255,255,0.1) !important;
}

/* Inputs */
input, select, textarea, .search-shell {
    background: rgba(0,0,0,0.4) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: #fff !important;
    transition: all 0.3s ease;
}
input:focus, select:focus, textarea:focus, .search-shell:focus-within {
    border-color: var(--primary) !important;
    box-shadow: 0 0 12px rgba(0, 210, 255, 0.3) !important;
    background: rgba(0,0,0,0.6) !important;
}
input::placeholder, textarea::placeholder {
    color: rgba(255,255,255,0.4) !important;
}

/* Text */
.page-title, h1, h2, h3, h4, .brand-title, .brand-subtitle, .group-title, .kpi-label, .complaint-copy, p, span, label {
    color: var(--text) !important;
}
.kpi-label, .group-title {
    color: var(--muted) !important;
}
.kpi-value {
    color: #fff !important;
    text-shadow: 0 0 10px rgba(255,255,255,0.2);
}

/* Nav Items */
.nav-item.active {
    background: rgba(0, 210, 255, 0.15) !important;
    border-right: 3px solid var(--primary);
}
.nav-item:hover {
    background: rgba(255,255,255,0.08) !important;
}
.active-bar {
    display: none !important;
}

/* Tables */
table th { background: rgba(255,255,255,0.05) !important; color: #fff !important; }
table td { border-bottom-color: rgba(255,255,255,0.05) !important; }
table tr:hover { background: rgba(255,255,255,0.03) !important; }

/* Menus */
.lang-menu summary, .profile-menu summary, .department-select {
    background: rgba(255,255,255,0.05) !important;
    border-color: rgba(255,255,255,0.1) !important;
    color: #fff !important;
}
.menu-panel a { color: var(--text) !important; }
.menu-panel a:hover { background: rgba(0, 210, 255, 0.15) !important; color: var(--primary) !important; }
.menu-panel p { color: var(--muted) !important; }

/* Badges & Pills */
.filter-pill { background: rgba(255,255,255,0.05) !important; color: var(--text) !important; border-color: rgba(255,255,255,0.1) !important; }
.filter-pill.active { background: var(--primary) !important; color: #fff !important; border-color: var(--primary) !important; box-shadow: var(--glow-primary); }
.id-pill { background: rgba(0,0,0,0.5) !important; color: var(--primary) !important; border: 1px solid rgba(0, 210, 255, 0.2); }

/* Chatbot */
.chatbot-fab { background: linear-gradient(135deg, #00d2ff, #3a7bd5) !important; box-shadow: var(--glow-primary) !important; border: none !important; }
.chatbot-panel.open { border-color: rgba(0, 210, 255, 0.4) !important; box-shadow: 0 10px 50px rgba(0,0,0,0.6), var(--glow-primary) !important; }
.chatbot-bubble.bot { background: rgba(255,255,255,0.05) !important; border-color: rgba(255,255,255,0.1) !important; color: #fff !important; }
.chatbot-bubble.user { background: rgba(0, 210, 255, 0.2) !important; border-color: rgba(0, 210, 255, 0.3) !important; color: #fff !important; }
.chatbot-header, .chatbot-input { background: rgba(0,0,0,0.4) !important; border-color: rgba(255,255,255,0.1) !important; }

/* Modals / Overlays */
.toast-item { background: var(--surface) !important; border-left-color: var(--primary) !important; backdrop-filter: blur(20px); color: #fff !important; }

/* File Input Hack for Dark Mode */
.file-trigger {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: #fff !important;
}

/* Authentication Pages Adjustments */
.split-left {
    background: transparent !important; /* To let the blob show through */
}
.split-right {
    background: rgba(10, 10, 15, 0.6) !important;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
}
.auth-panel {
    background: var(--surface) !important;
    backdrop-filter: blur(20px);
    border: 1px solid var(--border) !important;
    box-shadow: var(--shadow-sm) !important;
}
"""
with open('c:/copy/static/style.css', 'a', encoding='utf-8') as f:
    f.write("\n\n" + css_content)
