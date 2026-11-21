# PyBookKeeper – Restructured source

This folder contains a cleaned, single-folder Python version of the application
recovered from `script.exe`.  The original executable was built with Python 3.9
and PyQt5, using `.ui` files produced with Qt Designer.

## Layout

```
.
├── main.py                      # Application entry point
├── requirements.txt             # Runtime dependencies
└── Common/
    ├── __init__.py
    ├── backend.py               # Database access layer (sqlite3)
    ├── transaction.py           # Plain data classes for bills/items
    ├── createdocx.py            # Word/PDF report generation
    ├── opening_dialog.py        # Daily opening rates dialog
    ├── cash_credit_dialog.py    # End-of-day cash reconciliation dialog
    ├── making_dialog.py         # Making-charge calculator dialog
    ├── urd_dialog.py            # URD / scrap exchange dialog (hand-coded UI)
    ├── frontend_window.py       # Main window (partially recovered)
    ├── Frontend.ui              # Qt Designer UI files (kept as-is)
    ├── Opening.ui
    └── CCCalc.ui
```

## What has been recovered

| Module | Status |
|--------|--------|
| `main.py`, `Common/__init__.py` | Complete |
| `Common/transaction.py` | Fully reconstructed from decompiled output |
| `Common/backend.py` | Fully reconstructed (DB layer including the functions truncated by pycdc) |
| `Common/opening_dialog.py` | Complete, signal wiring corrected |
| `Common/cash_credit_dialog.py` | Complete, reconstructed from bytecode |
| `Common/making_dialog.py` | Complete, signal wiring corrected |
| `Common/urd_dialog.py` | Hand-coded UI plus `connect_dialog` reconstructed from bytecode |
| `Common/createdocx.py` | Report generation reconstructed; `gen_sum()` still needs its layout recovered |
| `Common/frontend_window.py` | `__init__` and a few short handlers are present; many event handlers are stubs because the decompiler output was truncated |

## Running

1. Create a Python 3.9 virtual environment (matching the original executable).
2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Launch the application:
   ```bash
   python main.py
   ```

## Notes

* `database.db` is created at runtime by `Common/backend.py` and stores all
  transaction data.
* `docx2pdf` requires Microsoft Word on Windows to convert `.docx` files to
  PDF.
* The `.ui` files were copied verbatim from the original `Common/` folder and
  are not modified.
* Several methods in `frontend_window.py` are intentionally left as
  well-documented stubs (`NotImplementedError`).  Their exact bodies were lost
  by the C++ decompiler; the bytecode for those methods is still available in
  `../decompiled_std/Frontendlogic_xdis.txt` if you want to recover them.
