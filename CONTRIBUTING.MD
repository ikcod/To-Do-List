# Contributing to Collaborative To-Do List

Thank you for considering contributing to our project! To maintain a smooth workflow, please follow the guidelines below.

---

## Getting Started

1. **Fork the Repository**:
   - Click the "Fork" button on the top-right of this repository to create your copy.

2. **Clone Your Fork**:
   - Clone the forked repository to your local machine:
     ```bash
     git clone https://github.com/<your-username>/<repo-name>.git
     ```

3. **Set Upstream Repository** (for syncing changes):
   - Add the original repository as the upstream:
     ```bash
     git remote add upstream https://github.com/<original-owner>/<repo-name>.git
     ```

4. **Install Dependencies** (if applicable):
   - Check the `README.md` for any required installations, and run:
     ```bash
     pip install -r requirements.txt
     ```

---

## How to Contribute

### 1. Create a New Branch
   - Use a descriptive branch name based on the feature or bug you are working on:
     ```bash
     git checkout -b feature/add-task
     ```
   - Use the following naming conventions:
     - `feature/<feature-name>`: For new features.
     - `fix/<bug-name>`: For bug fixes.
     - `docs/<docs-update>`: For documentation changes.

### 2. Work on Your Changes
   - Make your edits or additions in the relevant files.
   - Test your changes locally before committing.

### 3. Commit Your Changes
   - Write clear and concise commit messages. Follow this format:
     ```bash
     git commit -m "Short summary of changes

     - Detail of the first change
     - Explanation of the second change"
     ```


### 4. Push Your Branch
- Push your branch to your forked repository:
  ```bash
  git push origin feature/add-task
  ```

---

## Submitting a Pull Request

1. **Open a Pull Request**:
- Go to the original repository on GitHub and click **"New Pull Request"**.
- Select your branch and compare it to the `main` branch.

2. **Fill Out the PR Template**:
- Provide a detailed description of your changes, including:
  - The purpose of the PR.
  - Any issues it resolves (e.g., `Closes #issue-number`).
  - Screenshots (if applicable).

3. **Assign Reviewers**:
- Assign the relevant team members for review.

4. **Address Feedback**:
- Update your PR as needed based on reviewer feedback.

---

## Resolving Merge Conflicts

1. **Pull Latest Changes**:
- Sync your branch with the `main` branch:
  ```bash
  git fetch upstream
  git checkout main
  git pull upstream main
  git checkout feature/add-task
  git merge main
  ```

2. **Fix Conflicts**:
- Resolve conflicts in your editor or via command line.
- After resolving, stage the changes:
  ```bash
  git add <conflicted-file>
  git commit
  ```

---

## Coding Guidelines

1. **Follow PEP8 (for Python)**:
- Ensure your code is clean and consistent:
  ```bash
  pip install flake8
  flake8 .
  ```

2. **Test Your Code**:
- Ensure your changes don’t break existing functionality.
- Add new test cases if you’ve added features.

---

## Helpful Commands

- **Sync Your Fork**:
```bash
git fetch upstream
git merge upstream/main

