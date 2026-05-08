"""A simple calculator with a dark, modern UI built using Tkinter."""

import tkinter as tk


# --- Theme ----------------------------------------------------------------
BG = "#1e1e2e"          # window background
DISPLAY_BG = "#181825"  # display background
TEXT = "#cdd6f4"        # light text
DIGIT_BG = "#313244"    # digit/decimal buttons
OP_BG = "#f5a97f"       # +  -  *  /
OP_FG = "#1e1e2e"
EQ_BG = "#a6e3a1"       # =
CLEAR_BG = "#f38ba8"    # C
FONT_DISPLAY = ("SF Mono", 32, "bold")
FONT_BUTTON = ("SF Pro Display", 18, "bold")


# Layout: (label, row, col, colspan, color, fg)
BUTTONS = [
    ("C", 1, 0, 2, CLEAR_BG, BG),
    ("/", 1, 2, 1, OP_BG, OP_FG),
    ("*", 1, 3, 1, OP_BG, OP_FG),

    ("7", 2, 0, 1, DIGIT_BG, TEXT),
    ("8", 2, 1, 1, DIGIT_BG, TEXT),
    ("9", 2, 2, 1, DIGIT_BG, TEXT),
    ("-", 2, 3, 1, OP_BG, OP_FG),

    ("4", 3, 0, 1, DIGIT_BG, TEXT),
    ("5", 3, 1, 1, DIGIT_BG, TEXT),
    ("6", 3, 2, 1, DIGIT_BG, TEXT),
    ("+", 3, 3, 1, OP_BG, OP_FG),

    ("1", 4, 0, 1, DIGIT_BG, TEXT),
    ("2", 4, 1, 1, DIGIT_BG, TEXT),
    ("3", 4, 2, 1, DIGIT_BG, TEXT),
    ("=", 4, 3, 1, EQ_BG, BG),

    ("0", 5, 0, 2, DIGIT_BG, TEXT),
    (".", 5, 2, 1, DIGIT_BG, TEXT),
]


class Calculator:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("340x460")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.expression = tk.StringVar(value="0")

        self._build_display()
        self._build_buttons()

    def _build_display(self) -> None:
        display = tk.Label(
            self.root,
            textvariable=self.expression,
            anchor="e",
            bg=DISPLAY_BG,
            fg=TEXT,
            font=FONT_DISPLAY,
            padx=20,
            pady=30,
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

    def _build_buttons(self) -> None:
        # Make grid cells stretch evenly
        for c in range(4):
            self.root.grid_columnconfigure(c, weight=1, uniform="col")
        for r in range(1, 6):
            self.root.grid_rowconfigure(r, weight=1)

        for label, row, col, colspan, bg, fg in BUTTONS:
            btn = tk.Button(
                self.root,
                text=label,
                bg=bg,
                fg=fg,
                font=FONT_BUTTON,
                bd=0,
                activebackground=bg,
                activeforeground=fg,
                cursor="hand2",
                command=lambda v=label: self.on_button_click(v),
            )
            btn.grid(
                row=row, column=col, columnspan=colspan,
                sticky="nsew", padx=5, pady=5,
            )

    # --- Calculator logic -------------------------------------------------
    def on_button_click(self, value: str) -> None:
        """Handle a button press.

        TODO (you implement this): decide what to do for each kind of input.

        The display value lives in `self.expression` — read with
        `self.expression.get()` and update with `self.expression.set(...)`.

        You need to handle four cases:
          1. value == "C"   -> reset the display to "0"
          2. value == "="   -> evaluate the current expression and show the result
                               (hint: Python's built-in `eval` works for "1+2*3";
                                wrap it in try/except to handle bad input)
          3. value is a digit / "." / operator -> append it to the display
                               (remember: if the display is currently "0",
                                replace it instead of appending, e.g. "07")
        """
        raise NotImplementedError("Implement on_button_click in calculator.py")


def main() -> None:
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
