# Data Science Lifecycle Analysis (S63)

This repository contains beginner-friendly milestone work for setting up and using Jupyter Notebook in a clean, reusable data science project structure.

## Objective

Build practical confidence in:
- launching Jupyter Notebook
- using Code and Markdown cells
- controlling kernels (run, interrupt, restart)
- writing clear notebook documentation
- organizing project folders for collaboration

## Project Structure

```text
data-science-lifecycle-analysis_S63/
├── data/
│   └── .gitkeep
├── notebooks/
│   ├── M4_7_jupyter_interface.ipynb
│   ├── M4_8_code_vs_markdown.ipynb
│   ├── M4_9_kernel_control.ipynb
│   ├── M4_10_markdown_basics.ipynb
│   └── M4_11_project_structure.ipynb
├── outputs/
│   └── .gitkeep
├── src/
│   └── .gitkeep
└── README.md
```

## Environment

- OS: Windows
- Python: managed through Anaconda
- Environment: `base`
- Tool: Jupyter Notebook

## How to Run

From repository root:

```bash
conda run -n base jupyter notebook
```

Then open notebooks from the `notebooks/` folder.

## Milestones Implemented

### Milestone 4.7 - Launching Jupyter & Interface Basics
- Notebook: `notebooks/M4_7_jupyter_interface.ipynb`
- Covers:
  - launch from terminal
  - home interface elements
  - create/open/save/close notebook
  - run first Python cell

### Milestone 4.8 - Code Cells vs Markdown Cells
- Notebook: `notebooks/M4_8_code_vs_markdown.ipynb`
- Covers:
  - creating/running Code cells
  - creating/rendering Markdown cells
  - switching cell types
  - structure rule: Code = what, Markdown = why

### Milestone 4.9 - Running, Restarting, Interrupting Kernels
- Notebook: `notebooks/M4_9_kernel_control.ipynb`
- Covers:
  - kernel concept and memory
  - execution order effects
  - hidden state
  - restart vs interrupt usage

### Milestone 4.10 - Markdown: Headings, Lists, Code Blocks
- Notebook: `notebooks/M4_10_markdown_basics.ipynb`
- Covers:
  - headings and subheadings
  - ordered/unordered lists
  - inline code and fenced code blocks
  - combining Markdown and Code for readability

### Milestone 4.11 - Data Science Folder Structure
- Notebook: `notebooks/M4_11_project_structure.ipynb`
- Covers:
  - root folder and standard subfolders
  - separation of data, code, notebooks, and outputs
  - structure for reuse and collaboration

## Verification Checklist

- [ ] Jupyter launches from terminal
- [ ] All milestone notebooks open successfully
- [ ] Cells run in expected order
- [ ] Markdown renders correctly
- [ ] Project folders are clean and logically separated

## Key Learning Outcomes

- I can create and manage Jupyter notebooks confidently.
- I understand when to use Code cells and Markdown cells.
- I can control kernels (run, interrupt, restart) safely.
- I can organize a clean, collaboration-ready data science project.
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


Milestone 4.10: Writing Markdown for Headings, Lists, and Code Blocks in Jupyter Notebooks

Use this as a guided beginner practice. Follow one step at a time.

Step 1: Setup

What to do:
- Open Jupyter Notebook.
- Create a new notebook from New -> Python 3 (ipykernel).

Why it matters:
- You need a notebook open before practicing Markdown formatting.

Checkpoint:
- Confirm your notebook tab is open.

Step 2: Markdown Introduction

What to do:
- Insert a new cell.
- Change cell type to Markdown from the toolbar.
- Write a simple title:
# Markdown Practice Notebook
- Press Shift + Enter to render.

Why it matters:
- Markdown is for explanation and structure.
- Code cells are for execution.

Core idea:
- Markdown explains your work.
- Code performs your work.

Step 3: Headings Practice

What to do:
In a Markdown cell, write:
# Main Heading
## Subheading 1
## Subheading 2
### Smaller Subheading

Then press Shift + Enter.

Why it matters:
- Headings organize notebook sections.
- Better structure makes your notebook easier to read and review.

Step 4: Lists Practice

What to do:
Create one Markdown cell with unordered list:
- Clean data
- Analyze data
- Present findings

Create another Markdown cell with ordered list:
1. Write the question
2. Run the code
3. Explain the result

Why it matters:
- Lists make important points easy to scan quickly.
- Ordered lists are useful for step-by-step workflows.

Step 5: Inline Code

What to do:
Write this sentence in a Markdown cell:
Use `x` to store a value and call `print()` to display it.

Then render the cell.

Why it matters:
- Inline code highlights technical words, variable names, and functions inside explanations.
- It improves clarity without switching to a full code block.

Step 6: Code Blocks in Markdown

What to do:
Write this in a Markdown cell:
```python
x = 5
print(x)
```
Then press Shift + Enter.

Why it matters:
- Code blocks show code examples for explanation.
- Markdown code blocks do not execute; they are for documentation only.

Step 7: Combine Markdown + Code Cells

What to do:
Create this 4-cell notebook flow:

1) Markdown title
# Simple Notebook Structure

2) Markdown explanation
This notebook demonstrates how Markdown and Code cells work together.

3) Code cell
num = 10
print("Number is", num)

4) Markdown explanation of output
The code created a variable and printed its value.

Why it matters:
- Clean notebooks combine explanation and execution in logical order.
- Rule to remember:
  - Markdown = why
  - Code = what

Step 8: Reflection

What to do:
Answer these in a Markdown cell:
- Why should we not write everything only in code comments?
- Why is Markdown important in notebooks?

Why it matters:
- Reflection builds understanding, not memorization.
- Good notebook communication helps teammates and future-you.

Suggested short points:
- Code comments are limited and stay inside code blocks.
- Markdown gives full context, section structure, and readable explanations.

Step 9: 2-Minute Video Preparation

Use this speaking flow:

1) Intro (15-20 sec)
- "This demo shows Markdown basics in Jupyter notebooks."

2) Markdown cell creation (20-25 sec)
- Create a Markdown cell and render it.

3) Headings and lists (25-30 sec)
- Show one heading and both list types.
- Explain readability benefit.

4) Inline code and code block (25-30 sec)
- Show `print()` as inline code.
- Show fenced code block and explain it is not executed in Markdown.

5) Switch Markdown <-> Code and explain purpose (20-25 sec)
- Markdown for explanation.
- Code for execution.

6) Close with importance (15-20 sec)
- "Documentation matters because it makes analysis understandable and reproducible."

Milestone 4.10 Outcome

You can now:
- Write headings in Markdown
- Create ordered and unordered lists
- Use inline code and Markdown code blocks
- Structure a notebook with Markdown and Code cells
- Explain clearly when to use Markdown vs Code

You are ready for the next milestone.


Milestone 4.11: Creating a Project Folder Structure for Data Science Work

Use this as a beginner-friendly guided practice. Follow one step at a time.

Step 1: Concept Understanding

What to do:
- Ask yourself: "Have I created project folders before?"
- Write a one-line answer in your notes.

Why it matters:
- Project structure prevents confusion.
- It keeps work organized, reusable, and easier to maintain.

Simple idea:
- Good structure saves time later.

Step 2: Create Root Folder

What to do:
- Create one main project folder.
- Example name:
student-performance-analysis

Why it matters:
- This root folder is the main container for everything in your project.
- It keeps all related files in one place.

Step 3: Create Standard Subfolders

What to do:
Inside the root folder, create these subfolders one by one:
- data/
- notebooks/
- src/ (or scripts/)
- outputs/

Why it matters:
- data/ -> raw and processed datasets
- notebooks/ -> Jupyter notebooks for analysis
- src/ or scripts/ -> reusable Python logic
- outputs/ -> charts, reports, final artifacts

Key rule:
- Separate data, code, and results.

Step 4: Structure Understanding Check

What to do:
Answer these quickly:
- Where should raw files go?
- Where should notebook files go?
- Where should reusable Python files go?
- Where should plots/reports go?

Why it matters:
- Correct placement avoids messy projects.
- Important principles:
  - Never mix data and code in random folders
  - Never overwrite raw data directly

Correct mapping:
- Raw data -> data/
- Notebooks -> notebooks/
- Reusable code -> src/ or scripts/
- Results -> outputs/

Step 5: Best Practices for Folder Design

What to do:
Apply these naming habits:
- Use lowercase folder names
- Use clear names
- Avoid deep nested folders unless necessary

Why it matters:
- Improves readability and navigation.
- Makes your project easier for others to understand.

Good examples:
- data/
- notebooks/
- src/
- outputs/

Step 6: Collaboration Thinking

What to do:
Ask:
- "If a teammate opens this project, can they understand it in 30 seconds?"

Why it matters:
- A good structure should be self-explanatory.
- Collaboration becomes smoother when folder purpose is obvious.

Step 7: Visualize the Hierarchy

What to do:
Write your structure in tree form:

project/
  data/
  notebooks/
  src/
  outputs/

Why it matters:
- Seeing hierarchy clearly helps avoid misplacing files.
- Tree view builds strong project organization habits.

Step 8: 2-Minute Video Preparation

Use this simple speaking flow:

1) Root folder intro (20-25 sec)
- "This is my main project folder, which contains all project work."

2) Subfolder walkthrough (45-55 sec)
- data/: data files
- notebooks/: analysis notebooks
- src/: reusable code
- outputs/: results and reports

3) Why separation matters (25-30 sec)
- "Separating data, code, and results keeps projects clean and reduces confusion."

4) Collaboration angle (20-25 sec)
- "A teammate can quickly understand and continue this project."

5) Closing line (10-15 sec)
- "Good structure is the foundation of reliable data science work."

Why this helps:
- You explain your understanding in simple words, not memorized definitions.

Milestone 4.11 Outcome

You can now:
- Explain why folder structure matters
- Create a clean project root folder
- Organize standard data science subfolders
- Separate data, code, and outputs correctly
- Prepare projects for collaboration and reuse

You can now create clean project structures confidently.


Milestone 4.12: Organizing Raw Data, Processed Data, and Output Artifacts

Use this guided flow to build correct data organization habits.

Step 1: Concept Understanding

What to do:
- Ask yourself: "Do I know the difference between raw and processed data?"

Why it matters:
- Clear definitions prevent mistakes later.

Simple explanation:
- Raw data = original untouched data (must not be modified)
- Processed data = cleaned or transformed version
- Outputs = results such as plots, reports, or model artifacts

Example:
- Raw: original attendance file
- Processed: cleaned attendance file with standardized column names
- Output: final chart/report created from processed data

Step 2: Create Data Folder Structure

What to do:
Use this structure inside your project:

project/
  data/
    raw/
    processed/
  outputs/

Why it matters:
- `raw/` protects source-of-truth data
- `processed/` stores transformation results
- `outputs/` keeps final artifacts separate from data

Step 3: Raw Data Rules

What to do:
Ask yourself: "Should raw data ever be edited?"

Why it matters:
- Raw data should always be read-only.
- Keeping it unchanged lets you re-run workflows from a trusted source.

Rule:
- Never modify files directly inside `data/raw/`.

Step 4: Processed Data Understanding

What to do:
- When data is cleaned, standardized, or transformed, save it into `data/processed/`.
- Use clear names such as `cleaned_data`.

Why it matters:
- Processed data captures your preparation stage.
- Clear naming improves traceability and teamwork.

Step 5: Output Artifacts

What to do:
- Store plots, reports, and model results inside `outputs/`.

Why it matters:
- Outputs are results, not input data.
- Separation keeps project stages clean and auditable.

Step 6: Prevent Data Contamination

What to do:
Ask: "What happens if raw data is overwritten?"

Why it matters:
- You lose the original source.
- Reproducibility breaks because nobody can reproduce from the same starting point.

Correct flow:
- `raw -> processed -> outputs`

Step 7: Structure Visualization

What to do:
Represent your structure clearly:

project/
  data/
    raw/
    processed/
  outputs/

Why it matters:
- Visual hierarchy reduces confusion and file misplacement.

Step 8: Best Practices

What to do:
- Use clear names
- Never mix folders by purpose
- Keep workflow one-directional

Why it matters:
- Projects stay understandable and maintainable.
- Collaboration becomes easier.

Step 9: 2-Minute Video Preparation

Use this speaking flow:

1) Raw data folder (25-30 sec)
- What it contains and why it must stay unchanged.

2) Processed data folder (25-30 sec)
- What transformations mean and why cleaned data is stored separately.

3) Output folder (25-30 sec)
- What artifacts belong here and why they should not mix with data.

4) Importance of separation (25-30 sec)
- Explain contamination risk and reproducibility impact.

5) Closing (10-15 sec)
- "I follow raw -> processed -> outputs to keep projects reliable."

Milestone 4.12 Outcome

You can now:
- Distinguish raw, processed, and output stages clearly
- Organize folders to prevent contamination
- Maintain one-directional reproducible workflow
- Manage project artifacts in a professional, collaboration-ready way

You can now manage data organization properly and confidently.