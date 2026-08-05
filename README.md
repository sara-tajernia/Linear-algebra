# Applied Linear Algebra Mini-Projects

Four small Python projects demonstrate applied linear-algebra techniques through interactive programs and accompanying Persian reports.

## Projects

| Directory | What the code does | Input |
| --- | --- | --- |
| [`Equation_device/`](Equation_device/) | Performs row operations on an augmented matrix, identifies pivot and free variables, and prints a parameterized solution. | Matrix dimensions, coefficient rows, and constants entered at the prompt. |
| [`Shadow/`](Shadow/) | Applies a shear-style coordinate transformation to dark pixels and overlays the original color pixels to form a shadow effect. | A user-supplied image path. |
| [`Corona_prediction/`](Corona_prediction/) | Fits linear and quadratic least-squares models to an `Open` series, reserves the final ten rows for comparison, prints prediction errors, and plots the quadratic fit. | A user-supplied CSV containing an `Open` column. |
| [`Blur/`](Blur/) | Uses truncated singular-value decomposition for RGB image reconstruction and for denoising a synthetic `sin(xy)` surface. | An image path for `miniProject4.1.py`; the second script generates its own data. |

Each directory includes the report that explains its mathematical background and examples.

## Requirements

The imports in the scripts require Python together with:

- NumPy
- Matplotlib
- Pandas for the regression project

No dependency versions or environment file are recorded in the repository.

## Running a project

Run the desired script and follow its prompt, for example:

```bash
python3 Equation_device/main.py
python3 Shadow/main.py
python3 Corona_prediction/miniProject3.py
python3 Blur/miniProject4.1.py
python3 Blur/miniProject4.2.py
```

The image and CSV inputs used in the reports are not included. The scripts are interactive and there is no automated test suite, so the numerical or visual results depend on the supplied data.
