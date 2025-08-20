# Contributing to Pulse

<!--toc:start-->
- [Contributing to Pulse](#contributing-to-habitmaster)
  - [How to Contribute](#how-to-contribute)
  - [Code Style](#code-style)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
<!--toc:end-->

We welcome contributions to Pulse! By contributing, you're helping to make this project better for everyone.

## How to Contribute

1.  **Fork the repository**:
    Click the "Fork" button at the top right of this page to create your own copy of the repository.

2.  **Clone your forked repository**:
    ```bash
    git clone https://github.com/Triangulation5/Pulse.git
    cd Pulse
    ```

3.  **Create a new branch**:
    Always create a new branch for your changes. Use a descriptive name.
    ```bash
    git checkout -b feature/your-feature-name
    # or
    git checkout -b bugfix/your-bug-fix
    ```

4.  **Make your changes**:
    Implement your feature or bug fix. Ensure your code adheres to the existing style and conventions.

5.  **Test your changes**:
    If you're adding new features, please write tests for them. If you're fixing a bug, ensure your fix includes a test that reproduces the bug and then passes with your fix.

6.  **Commit your changes**:
    Write clear and concise commit messages.
    ```bash
    git add .
    git commit -m "feat: Add new feature X" # or "fix: Resolve bug Y"
    ```

7.  **Push to your fork**:
    ```bash
    git push origin feature/your-feature-name
    ```

8.  **Create a Pull Request (PR)**:
    Go to the original Pulse repository on GitHub and create a new Pull Request from your forked repository and branch. Provide a clear description of your changes.

## Code Style

-   Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
-   Use clear and descriptive variable and function names.
-   Add comments where necessary to explain complex logic.

## Reporting Bugs

If you find a bug, please open an issue on the GitHub issue tracker. Provide as much detail as possible, including:

-   A clear and concise description of the bug.
-   Steps to reproduce the behavior.
-   Expected behavior.
-   Screenshots or error messages (if applicable).
-   Your operating system and Python version.

## Suggesting Enhancements

We welcome suggestions for new features or improvements. Please open an issue on the GitHub issue tracker and describe your idea in detail.

Thank you for contributing to Pulse!
