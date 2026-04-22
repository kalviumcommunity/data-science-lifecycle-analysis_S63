1. Understanding the Lifecycle: Question → Data → Insight

Data science does not begin with code or models—it begins with a clear question. A well-defined question gives direction to the entire analysis. Without a clear question, the work becomes unfocused and may lead to irrelevant or misleading results. For example, instead of asking “What does the data say?”, a better question would be “Which students are at risk of underperforming and why?”

Once the question is defined, the next step is understanding the data. Data acts as evidence, not absolute truth. It is important to know where the data comes from, what each column represents, and whether the data is complete and reliable. Without this understanding, any analysis performed on the data may produce incorrect conclusions.

Insights emerge through exploration, not just by applying tools or algorithms. By analyzing patterns, trends, and relationships in the data, we can generate meaningful insights. These insights help in making informed decisions. Therefore, the lifecycle connects logically: a clear question guides data selection, and proper data understanding leads to reliable insights.

2. Applying the Lifecycle to a Project Context
Project Context: Identifying At-Risk Students in Schools

Question:
Which students are at risk of falling behind academically, and what factors contribute to their performance?

Data Required:
To answer this question, we would need data such as:

Student performance (subject-wise marks)
Attendance records
Assignment scores
Demographic information (age, gender, location)

This data may come from school databases, student management systems, or surveys. Each feature represents a different aspect of student behavior and performance.

Expected Insight:
The goal is to identify patterns such as low attendance leading to poor performance or students struggling across multiple subjects. These insights can help educators take early action, such as providing additional support or personalized interventions.




Reading & Interpreting a Data Science Project Repository
1. A Repository Is a Story, Not Just Files

A data science repository should be understood as a story rather than just a collection of files and folders. Each part of the repository represents a step in solving a problem. Instead of randomly opening files, it is important to first understand the intent of the project.

The first question to ask is: What problem is this project trying to solve? Once the problem is clear, the structure of the repository starts to make sense. For example, notebooks may represent exploration, while scripts may contain reusable logic. This reflects the data science lifecycle from question to data to insight.

Understanding a repository as a story helps in identifying what has already been done, what assumptions were made, and what work is still incomplete.

2. Understanding the Role of the README

The README is the most important file in any repository because it acts as the entry point. It provides context about the project and guides the reader on how to navigate the repository.

A good README should clearly explain:

The problem being solved
The dataset used and its source
The approach taken for analysis
Key findings or insights
Instructions to run or explore the project

While reviewing a repository, it is important to check whether the README is complete. Sometimes, important details like data source or methodology may be missing. Identifying such gaps helps in understanding what is unclear and what needs improvement.

3. Interpreting Folder Structure and File Organization

A typical data science repository is divided into folders based on different stages of the workflow.

Common folders include:

data/ → contains raw or processed datasets
notebooks/ → contains exploratory analysis
src/ or scripts/ → contains reusable code
reports/ or figures/ → contains outputs like graphs

Each folder represents a stage in the data science lifecycle. For example, notebooks are used during exploration, while scripts are used for structured and reusable work.

Understanding this structure helps in navigating the project efficiently and prevents making changes in the wrong place.

4. Reading Notebooks and Code with Purpose

When opening notebooks or scripts, the goal is not to understand every line of code immediately. Instead, the focus should be on understanding the flow of analysis.

Key things to look for:

Where the data is loaded
How the data is cleaned and processed
What kind of analysis is performed
What conclusions are drawn

By scanning the notebook in this way, it becomes easier to follow the reasoning behind the work rather than getting stuck on technical details.

5. Identifying Assumptions, Limitations, and Open Questions

Every data science project is based on certain assumptions. These may not always be clearly written, so it is important to identify them while reading the repository.

Some important questions to ask:

Is the data complete and reliable?
Are there any missing values or biases?
What factors are not considered in the analysis?
Are there unanswered questions or areas for improvement?

This step helps in critically evaluating the project instead of accepting everything at face value.

6. How This Prepares You to Contribute

Understanding how to read a repository prepares you to contribute effectively to real-world projects.

It helps you to:

Avoid breaking existing code or workflows
Build on top of existing work instead of repeating it
Improve documentation where needed
Ask meaningful questions during discussions

This makes your contribution more valuable and aligned with the project goals.

✅ Conclusion

Reading a data science repository is an essential skill that goes beyond just understanding code. It involves interpreting the project’s purpose, structure, and logic. By treating the repository as a story and analyzing it step by step, we can better understand the work, identify gaps, and contribute effectively.



Environment Setup (Milestone 4.5)
Operating System

Windows 10 (or your OS)

Python Installation

Command:

python --version

Output:

Python 3.11.5
Anaconda Installation

Command:

conda --version

Output:

conda 23.x.x
Environment Verification

Command:

python

Output:

>>> print("Hello")
Hello


Environment Verification (Milestone 4.6)
Operating System

Windows 11

Python Verification

Command:

python --version

Output:

Python 3.12.4
Conda Verification

Command:

conda --version

Output:

conda 23.x.x
Environment Activation

Command:

conda activate base

Output:

(base) C:\Users\Dell>
Jupyter Verification

Command:

jupyter notebook

Result:

Jupyter Notebook opened successfully in browser
Created a new notebook
Executed Python code successfully

Example Output:

print("Jupyter Working")
Jupyter Working


Milestone 4.7: Launching Jupyter Notebook and Understanding its Interface

1) Confirm Working Directory

What to do:
Run:
pwd

Then confirm your target project folder:
/c/Users/Dell/OneDrive/Desktop/data-science-lifecycle-analysis_S63

Why it matters:
Jupyter opens in the folder where you start it. Starting in the right folder keeps notebooks organized.

2) Move to the Project Folder

What to do:
If needed, run:
cd /c/Users/Dell/OneDrive/Desktop/data-science-lifecycle-analysis_S63

Why it matters:
This ensures all notebook files are created inside your project, not in random locations.

3) Activate Conda Environment

What to do:
Use:
conda activate base

If activation is not available in your shell, use:
conda run -n base <command>

Why it matters:
The active environment controls Python version and installed packages used by your notebook.

4) Launch Jupyter Notebook

What to do:
Run:
conda run -n base jupyter notebook

Why it matters:
This starts the notebook server and opens the Jupyter Home page in your browser.

5) Understand Jupyter Home Interface

What to do:
On the Home page, identify:
- File/folder list
- Current path (top area)
- New button (top-right)
- Upload button

Why it matters:
Jupyter Home is your notebook file manager. You use it to create, open, and organize work.

6) Navigate Folders Correctly

What to do:
- Click a folder name to go inside
- Use the path/breadcrumb to go back to parent folder

Why it matters:
Correct navigation helps you avoid creating notebooks in the wrong directory.

7) Create and Open a Notebook

What to do:
Click New -> Python 3 (ipykernel) (or the available Python kernel).

Why it matters:
A notebook needs a kernel to execute code. Python kernel means cells run with Python.

8) Run a Simple Python Cell

What to do:
In the first cell, type:
print("Hello, Jupyter!")

Then press Shift + Enter.

Why it matters:
Running a cell means Python executes your code and shows output below the cell.

9) Rename Notebook

What to do:
Click the notebook title (usually Untitled) and rename it to:
milestone_4_7_practice

Why it matters:
Meaningful names make files easier to find and review later.

10) Save Notebook

What to do:
Press Ctrl + S (or File -> Save and Checkpoint).

Why it matters:
Saving stores your latest work to disk and creates a reliable restore point.

11) Close Notebook Safely

What to do:
Inside notebook:
File -> Close and Halt

Back on Home page (if needed):
Select notebook checkbox -> Shutdown

Why it matters:
Closing and halting stops the running kernel and frees memory/CPU resources.

12) Reopen Notebook from Home

What to do:
From Jupyter Home, click:
milestone_4_7_practice.ipynb

Why it matters:
This confirms your notebook was saved in the correct folder and can be resumed anytime.

13) Stop Jupyter Server (When Done)

What to do:
In terminal, press Ctrl + C and confirm with y.

Why it matters:
Stops the local server cleanly and avoids leaving background processes running.

Milestone 4.7 Outcome

You can now:
- Launch Jupyter Notebook from terminal
- Understand the Jupyter Home interface
- Navigate folders correctly
- Create and run notebook cells
- Rename, save, close, and reopen notebooks safely


Milestone 4.8: Understanding Notebook Cells (Code vs Markdown)

Use this as a beginner-friendly practice flow. Follow one step at a time.

Step 1: Open Jupyter and Create a New Notebook

What to do:
- Launch Jupyter Notebook from terminal.
- On Home page, click New -> Python 3 (ipykernel).

Why it matters:
- A notebook is your workspace.
- You need a live notebook before learning cell types.

Checkpoint:
- Confirm you see a new notebook tab (usually named Untitled).

Step 2: Create and Run a Code Cell

What to do:
- Click the first cell (default type is Code).
- Type:
print("This is a code cell")
- Press Shift + Enter.

Why it matters:
- Code cells execute Python logic.
- Only code cells run code and produce program output.

Checkpoint:
- You should see:
This is a code cell

Step 3: Create a Markdown Cell

What to do:
- Insert a new cell below.
- Change cell type from Code to Markdown (from toolbar dropdown).
- Type:
# My First Notebook
This notebook shows the difference between Code and Markdown cells.
- Press Shift + Enter to render.

Why it matters:
- Markdown cells are for writing explanations and structure.
- Markdown is documentation, not executable logic.

Checkpoint:
- Text appears formatted (title + normal sentence), not as raw symbols.

Step 4: Switch Cell Types (Both Directions)

What to do:
- Select a Code cell and change it to Markdown.
- Select a Markdown cell and change it to Code.
- You can use toolbar dropdown or keyboard shortcuts in command mode:
  - M for Markdown
  - Y for Code

Why it matters:
- In real work, you often adjust cell type while organizing analysis.
- Correct type prevents mistakes (for example, trying to execute explanation text).

When to use each:
- Code cell: calculations, Python commands, logic, outputs.
- Markdown cell: title, context, interpretation, next steps.

Step 5: Build a Clean, Structured Mini Notebook

What to do:
Create this 4-cell structure:

1) Markdown title
# Code vs Markdown Practice

2) Markdown explanation
In this notebook, I run simple Python in Code cells and explain results in Markdown cells.

3) Code cell
x = 5
print("Value of x is", x)

4) Markdown explanation of output
The code created a variable x and printed its value.

Why it matters:
- Good notebooks are readable by others and by your future self.
- Core rule:
  - Code = what you do
  - Markdown = why you do it

Checkpoint:
- Run all cells from top to bottom and verify flow is clear.

Step 6: Self-Check (Understanding Test)

What to do:
Answer this in your notebook (Markdown cell):
- What is the difference between Code and Markdown cells?

Why it matters:
- Explaining in your own words proves understanding better than memorizing.

Suggested answer format:
- Code cells execute Python and produce outputs.
- Markdown cells explain ideas, steps, and findings, and do not execute Python logic.

Step 7: 2-Minute Video Preparation Script

What to do:
Use this speaking plan:

1) Intro (15-20 sec)
- "In this demo, I will show Code cells and Markdown cells in Jupyter."

2) Code cell demo (30-40 sec)
- Create Code cell.
- Run print("This is a code cell").
- Say: "Code cells run Python and generate output."

3) Markdown cell demo (30-40 sec)
- Create Markdown cell with a title and one explanation sentence.
- Render with Shift + Enter.
- Say: "Markdown cells are for explanation and notebook structure."

4) Switch cell type demo (20-25 sec)
- Convert Code -> Markdown and Markdown -> Code.
- Say when each type should be used.

5) Clear difference statement (20-25 sec)
- "Code = what I do in Python."
- "Markdown = why I am doing it and what it means."

Why it matters:
- Speaking while demonstrating shows both practical skill and conceptual clarity.

Milestone 4.8 Outcome

You can now:
- Create and run Code cells
- Create and render Markdown cells
- Switch between cell types correctly
- Organize a notebook in a clean, readable structure
- Clearly explain Code vs Markdown in your own words

You are ready for the next milestone.


Milestone 4.9: Running, Restarting, and Interrupting Jupyter Kernels

Use this as a beginner-safe guided practice. Follow step by step.

Step 1: What a Kernel Is

What to do:
- Open a Jupyter notebook.
- Look at the top-right kernel indicator (for example, Python 3).

Why it matters:
- Kernel = engine that runs code.
- It stores variables in memory while your session is active.

Quick understanding line:
- If kernel memory changes, notebook behavior can change.

Step 2: Run Cells in Order

What to do:
Create these three Code cells:

Cell 1:
a = 10

Cell 2:
b = 5

Cell 3:
print("Sum:", a + b)

Run in order: Cell 1 -> Cell 2 -> Cell 3 using Shift + Enter.

Why it matters:
- Running in order builds state correctly.
- Kernel remembers variables from earlier cells.

Now test execution order:
- Restart kernel (Kernel -> Restart).
- Run only Cell 3 first.

Expected observation:
- Error because a and b are not defined yet.

Why this happens:
- Execution order matters because variables must exist before use.

Step 3: Demonstrate Hidden State

What to do:
Create two Code cells:

Cell A:
name = "Data Science"

Cell B:
print("Learning:", name)

Run A then B (works).
Now restart kernel and run only B.

Ask yourself:
- What changed?

Expected result:
- You get a NameError for name.

Why it matters:
- Hidden state means notebook seemed fine only because old variables were stored in memory.
- This can confuse beginners if they do not run from top to bottom.

Step 4: Restart Kernel and Re-run

What to do:
- Go to Kernel -> Restart Kernel (or Restart & Clear Output, if available).
- Then run all cells from top in sequence.

Why it matters:
- Restart clears memory.
- Re-running from top checks reproducibility (anyone can get same result from a clean state).

Best practice:
- Before sharing/submitting notebook, restart and run all cells once.

Step 5: Interrupt a Running Cell

What to do:
Create a safe long-running cell:

import time
while True:
    print("Running...")
    time.sleep(1)

Run it, wait 2-3 seconds, then click Kernel -> Interrupt (or stop button).

Why it matters:
- Interrupt stops the currently running code.
- It does NOT reset all kernel memory.

Important safety note:
- Use this only for practice and interrupt quickly.

Step 6: Restart vs Interrupt (Core Difference)

Interrupt means:
- Stop current running task.
- Keep existing memory/variables (in many cases).

Restart means:
- Stop everything and start a fresh kernel.
- Clear all variables from memory.

When to interrupt:
- Code is stuck, too slow, or infinite loop is running.

When to restart:
- Notebook state is messy, errors are confusing, or you want a clean reproducible run.

Step 7: 2-Minute Video Preparation

Use this speaking flow:

1) Kernel meaning (20-25 sec)
- "Kernel is the engine that runs Python code and stores variables in memory."

2) Running cells (25-30 sec)
- Show simple cells with variables.
- Run in order and explain why order matters.

3) Hidden state (20-25 sec)
- Run dependent cell after restart and show NameError.
- Explain hidden state in simple words.

4) Interrupt demo (20-25 sec)
- Start long loop.
- Interrupt and explain: stop task, memory not fully reset.

5) Restart demo (20-25 sec)
- Restart kernel.
- Explain: clears memory and gives clean start.

6) Clear difference statement (15-20 sec)
- "Interrupt = stop current execution."
- "Restart = reset the whole session."

Milestone 4.9 Outcome

You can now:
- Explain what a kernel is
- Run cells in correct order
- Understand execution-order effects
- Detect hidden state issues
- Use interrupt to stop running code
- Use restart to reset memory and ensure reproducibility

You can control Jupyter kernels confidently now.