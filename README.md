# Week 7 Homework: Grade Book

A command line program that tracks quiz scores for two students using a `Gradebook` class, and lets you enter scores and view each student's grades and average through a simple text menu.

## File

- **Christine_Griffith_Week_7_Homework_Assignment.py** - the full program, prompts for two student names, then loops through a menu to enter quiz scores or display current grades.

## What it does

1. Asks for Student 1's and Student 2's names, creating a `Gradebook` object for each.
2. Shows a running count of how many students are in the gradebook.
3. Presents a menu:
   - `0` - Exit
   - `1` - Enter a quiz score for Student 1
   - `2` - Enter a quiz score for Student 2
   - `3` - Display current grades and average for both students
4. Keeps looping until you choose `0`.

Each student can have multiple quiz scores entered over time, and option `3` shows the full list of scores plus the calculated average for each.

## What was wrong with the original and what I fixed

The original had a few issues that kept it from running correctly:

- **`quizScore` was called without parentheses.** `Gradebook.quizScore` just referenced the method itself, it never actually ran. Fixed to call it properly on each student's own gradebook object, passing the score in: `gradebook_1.quizScore(q_score_1)`.
- **`quizScore` appended the wrong data.** It ignored the `score` parameter entirely and instead appended two undefined globals (`q_score_1` and `q_score_2`) to `self.grades` every time, regardless of which student it was for. Fixed so it appends the score that was actually passed in.
- **Both student objects were anonymous.** The original called `Gradebook(student_1)` and `Gradebook(student_2)` without keeping a reference to either object, so there was no way to add scores to a specific student afterward. Fixed by storing them as `gradebook_1` and `gradebook_2`.
- **`full_student_1` and `full_student_2` were broken and unused.** They referenced undefined class attributes (`Gradebook.s1_score`) and used `{student_1}` as if building a set rather than assigning a value. Since nothing in the program called them and averages are handled by `currentAverage()` instead, they were removed.
- **No average was ever calculated.** `currentAverage()` just printed a label with no actual number. Fixed to calculate and return the mean of a student's `grades` list, and to handle the case of no scores yet without crashing.
- **Option `3` only showed the most recent score.** It printed the bare variables `q_score_1` and `q_score_2`, which only ever held the last score entered and would crash with a `NameError` if you picked option 3 before entering any scores. Fixed to print each student's full list of grades and their average instead.
- **Leftover unused code.** An empty `quiz_scores = []` list at the top was never used anywhere and was removed.

## Requirements

- Python 3

## Usage

Run it from the command line:

```
python3 Christine_Griffith_Week_7_Homework_Assignment.py
```

Follow the prompts to enter both student names, then use the menu to add quiz scores and view results.
