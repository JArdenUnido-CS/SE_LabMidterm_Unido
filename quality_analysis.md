# Software Quality Analysis

## 1. Functional Suitability
Functional suitability refers to how well the software provides functions that meet stated requirements.
The calculator module implements accurate addition and division operations, including validation and
error handling for invalid inputs and division by zero. Automated tests verify correct behavior across
normal, negative, and edge cases, ensuring correctness.

## 2. Reliability
Reliability refers to the system’s ability to perform consistently under defined conditions.
Error handling prevents crashes caused by invalid inputs, while unit tests ensure stable behavior
when changes are introduced. Continuous Integration (CI) using GitHub Actions automatically runs tests
on every push, preventing faulty code from being merged.

## CI/CD Contribution to Quality
The CI/CD pipeline improves reliability by detecting errors early. Every code change is tested
automatically, ensuring that regressions are caught immediately and the application remains stable
over time.
