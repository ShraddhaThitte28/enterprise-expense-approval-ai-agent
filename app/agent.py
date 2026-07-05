# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

from app.business_tools import (
    validate_expense,
    check_expense_policy,
    check_budget,
    detect_fraud,
    
)





def get_weather(query: str) -> str:
    """Simulates a web search. Use it get information on weather.

    Args:
        query: A string containing the location to get weather information for.

    Returns:
        A string with the simulated weather information for the queried location.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."


def get_current_time(query: str) -> str:
    """Simulates getting the current time for a city.

    Args:
        city: The name of the city to get the current time for.

    Returns:
        A string with the current time information.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        tz_identifier = "America/Los_Angeles"
    else:
        return f"Sorry, I don't have timezone information for query: {query}."

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return f"The current time for query {query} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"


root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model="gemini-flash-latest",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""
You are an Enterprise Expense Approval AI Assistant.

Your job is to help employees with expense reimbursement requests.

Whenever an employee submits an expense request:

1. Validate whether the expense category is allowed.
2. Check the company expense policy.
3. Check the department budget.
4. Detect possible fraud.
5. If any check fails, explain why.
6. If all checks pass, approve the reimbursement.

If any required information is missing
(for example employee name,
department,
expense type,
amount,
or reason),
ask the user first.

Always use ALL available business tools before giving the final answer.


After using the tools, always generate the final response in the following format:

Expense Approval Report

Employee Name:
Department:
Expense Category:
Expense Amount:

Expense Validation:
Expense Policy:
Budget Status:
Fraud Risk:

Final Decision:

Reason:
""",

    tools=[
    validate_expense,
    check_expense_policy,
    check_budget,
    detect_fraud,
],
)

app = App(
    root_agent=root_agent,
    name="app",
)
