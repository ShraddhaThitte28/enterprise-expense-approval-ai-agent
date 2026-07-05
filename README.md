# Enterprise Expense Approval AI Agent

## Overview

Enterprise Expense Approval AI Agent is an AI-powered reimbursement approval system developed using Google's Agent Development Kit (ADK) and Gemini.

The agent helps employees submit reimbursement requests and automatically evaluates them using company business rules before making an approval decision.

This project was developed as part of the Kaggle 5-Day AI Agents: Intensive Vibe Coding Course with Google Capstone Project.

---

## Features

- AI Powered Expense Approval
- Google ADK Agent
- Gemini Flash Model
- Expense Category Validation
- Company Expense Policy Checking
- Department Budget Verification
- Fraud Risk Detection
- Human-in-the-loop Conversation
- Automatic Approval & Rejection
- Enterprise Style Decision Report

---

## Technologies Used

- Python
- Google ADK
- Gemini Flash
- Agents CLI
- Google AI Studio API
- VS Code

---

## Project Workflow

Employee submits expense request

↓

AI Agent collects missing information

↓

Expense Category Validation

↓

Company Policy Check

↓

Department Budget Check

↓

Fraud Detection

↓

Final Approval / Rejection

---

## Example

Input

Employee Name : Shraddha

Department : IT

Expense Type : Hotel

Amount : ₹7000

Reason : Office Meeting

Output

APPROVED

Expense Category : Valid

Policy : Passed

Budget : Available

Fraud Risk : Low

---

## Folder Structure

```
ambient-expense-agent
│
├── app
│   ├── agent.py
│   ├── business_tools.py
│   └── app_utils
│
├── tests
│
├── .env
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## Future Enhancements

- Multi-Agent Architecture
- Database Integration
- Employee Login
- Manager Approval Portal
- Finance Dashboard
- Receipt Upload
- Email Notifications
- Analytics Dashboard

---

## Author

Shraddha Thitte

MCA Student

IMCC Pune

Kaggle AI Agents Capstone Project (2026)


## Quick Start

Install `agents-cli` and its skills if not already installed:

```bash
uvx google-agents-cli setup
```

Install required packages:

```bash
agents-cli install
```

Test the agent with a local web server:

```bash
agents-cli playground
```

You can also use features from the [ADK](https://adk.dev/) CLI with `uv run adk`.

## Commands

| Command              | Description                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------- |
| `agents-cli install` | Install dependencies using uv                                                         |
| `agents-cli playground` | Launch local development environment                                                  |
| `agents-cli lint`    | Run code quality checks                                                               |
| `agents-cli eval`    | Evaluate agent behavior (generate, grade, analyze, and more — see `agents-cli eval --help`) |
| `uv run pytest tests/unit tests/integration` | Run unit and integration tests                                                        |

## 🛠️ Project Management

| Command | What It Does |
|---------|--------------|
| `agents-cli scaffold enhance` | Add CI/CD pipelines and Terraform infrastructure |
| `agents-cli infra cicd` | One-command setup of entire CI/CD pipeline + infrastructure |
| `agents-cli scaffold upgrade` | Auto-upgrade to latest version while preserving customizations |

---

