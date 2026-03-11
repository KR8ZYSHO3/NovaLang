"""
NovaLang GUI (v0.1.1) – simple Tkinter IDE for editing and running .nova programs.
Cross-platform: Windows, macOS, Linux (requires tk; on some Linux distros: python3-tk).
"""

import re
import sys
from pathlib import Path

# Ensure project root is on path for interpreter import
sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, simpledialog
    from tkinter.scrolledtext import ScrolledText
except ImportError:
    print("Tkinter is required for the GUI. Install it (e.g. on Linux: python3-tk).", file=sys.stderr)
    sys.exit(1)

from interpreter import interpret


# Plain ASCII default (no smart quotes)
DEFAULT_CODE = "set x 42\nprint x"
WINDOW_SIZE = (1000, 700)
OUTPUT_FONT = ("Consolas", 10)
EDITOR_FONT = ("Consolas", 10)
KEYWORDS = [
    "set", "add", "sub", "mul", "div", "mod",
    "print", "input", "if", "while",
    "array_set", "array_get",
]


class NovaGUI:
    """Simple IDE: editor (left), output (right), toolbar, status bar."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NovaLang IDE (v0.1.1)")
        self.root.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")
        self.current_file = None

        self._build_toolbar()
        self._build_panes()
        self._build_status_bar()

        self.output_pane.config(state=tk.DISABLED)  # read-only
        self._dark_mode = False
        self.editor.focus_set()

    def _build_toolbar(self):
        toolbar = tk.Frame(self.root, relief=tk.RAISED, bd=1)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=2, pady=2)
        tk.Button(toolbar, text="Run", command=self._run, width=6).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="Clear", command=self._clear, width=6).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="New", command=self._new, width=6).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="Open", command=self._open, width=6).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="Save", command=self._save, width=6).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="Examples", command=self._load_example, width=8).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text="Dark", command=self._toggle_dark, width=5).pack(side=tk.LEFT, padx=2, pady=2)

    def _build_panes(self):
        paned = tk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)

        # Left: line numbers + editor (wider by default)
        left = tk.Frame(paned)
        tk.Label(left, text="Code (.nova)", anchor=tk.W).pack(fill=tk.X)
        editor_row = tk.Frame(left)
        editor_row.pack(fill=tk.BOTH, expand=True)
        self.line_numbers = tk.Text(
            editor_row, width=4, padx=2, takefocus=0, border=0,
            background="#e8e8e8", state=tk.DISABLED, font=EDITOR_FONT,
        )
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        self.editor = ScrolledText(editor_row, wrap=tk.WORD, font=EDITOR_FONT, width=58)
        self.editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.editor.insert(tk.END, DEFAULT_CODE)
        self.editor.tag_configure("keyword", foreground="#0000cc")
        self.editor.bind("<KeyRelease>", self._on_editor_change)
        self.editor.bind("<MouseWheel>", self._on_editor_scroll)
        self.editor.bind("<Button-4>", self._on_editor_scroll)
        self.editor.bind("<Button-5>", self._on_editor_scroll)
        paned.add(left, minsize=400)

        # Right: output (narrower)
        right = tk.Frame(paned)
        tk.Label(right, text="Console / Print results", anchor=tk.W).pack(fill=tk.X)
        self.output_pane = ScrolledText(right, wrap=tk.WORD, font=OUTPUT_FONT, width=38, state=tk.NORMAL)
        self.output_pane.pack(fill=tk.BOTH, expand=True)
        paned.add(right, minsize=300)

        self._update_line_numbers()
        self._highlight()

    def _build_status_bar(self):
        self.status = tk.Label(self.root, text="Ready", anchor=tk.W, relief=tk.SUNKEN)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def _on_editor_change(self, event=None):
        self._update_line_numbers()
        self._highlight()

    def _on_editor_scroll(self, event=None):
        self._update_line_numbers()
        # Sync line numbers scroll with editor
        self.line_numbers.yview_moveto(self.editor.yview()[0])

    def _update_line_numbers(self):
        self.line_numbers.config(state=tk.NORMAL)
        self.line_numbers.delete("1.0", tk.END)
        content = self.editor.get("1.0", tk.END)
        line_count = max(1, content.count("\n") + (1 if not content.endswith("\n") else 0))
        self.line_numbers.insert(tk.END, "\n".join(str(i) for i in range(1, line_count + 1)))
        self.line_numbers.config(state=tk.DISABLED)
        self.line_numbers.yview_moveto(self.editor.yview()[0])

    def _highlight(self):
        content = self.editor.get("1.0", tk.END)
        self.editor.tag_remove("keyword", "1.0", tk.END)
        pattern = r"\b(" + "|".join(re.escape(k) for k in sorted(KEYWORDS, key=len, reverse=True)) + r")\b"
        offset = 0
        lines = content.split("\n")
        for i, line in enumerate(lines):
            for m in re.finditer(pattern, line):
                start_idx = f"{i + 1}.{m.start()}"
                end_idx = f"{i + 1}.{m.end()}"
                self.editor.tag_add("keyword", start_idx, end_idx)
            offset += len(line) + 1

    def _run(self):
        program = self.editor.get("1.0", tk.END)
        self._write_output("")  # clear output
        self.status.config(text="Running...")
        self.root.update_idletasks()

        def input_fn():
            value = simpledialog.askstring("NovaLang Input", "Enter an integer (or leave empty for 0):", parent=self.root)
            return value.strip() if value else "0"

        try:
            result = interpret(program, input_fn=input_fn)
            if result:
                self._write_output(result)
            self.status.config(text="Run finished successfully.")
        except ValueError as e:
            msg = str(e)
            if "division by zero" in msg.lower():
                self._write_output("Error: division by zero (div with 0).")
            elif "modulo by zero" in msg.lower():
                self._write_output("Error: modulo by zero (mod with 0).")
            else:
                self._write_output(f"Error: {e}")
            self.status.config(text="Run finished with errors.")
        except Exception as e:
            self._write_output(f"Error: {e}")
            self.status.config(text="Run finished with errors.")

    def _write_output(self, text: str) -> None:
        self.output_pane.config(state=tk.NORMAL)
        self.output_pane.delete("1.0", tk.END)
        self.output_pane.insert(tk.END, text)
        self.output_pane.config(state=tk.DISABLED)

    def _clear(self):
        self.editor.delete("1.0", tk.END)
        self._write_output("")
        self._update_line_numbers()
        self.status.config(text="Cleared.")
        self.current_file = None

    def _new(self):
        self.editor.delete("1.0", tk.END)
        self.editor.insert(tk.END, DEFAULT_CODE)
        self._write_output("")
        self._update_line_numbers()
        self._highlight()
        self.status.config(text="New file.")
        self.current_file = None

    def _open(self):
        path = filedialog.askopenfilename(
            defaultextension=".nova",
            filetypes=[("NovaLang files", "*.nova"), ("All files", "*.*")],
        )
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.editor.delete("1.0", tk.END)
            self.editor.insert(tk.END, content)
            self._update_line_numbers()
            self._highlight()
            self.current_file = path
            self.status.config(text=f"Opened: {path}")
        except Exception as e:
            messagebox.showerror("Open failed", str(e))

    def _load_example(self):
        examples_dir = Path(__file__).resolve().parent / "examples"
        if not examples_dir.is_dir():
            messagebox.showinfo("Examples", "No examples folder found.")
            return
        path = filedialog.askopenfilename(
            initialdir=str(examples_dir),
            defaultextension=".nova",
            filetypes=[("NovaLang files", "*.nova"), ("All files", "*.*")],
        )
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.editor.delete("1.0", tk.END)
            self.editor.insert(tk.END, content)
            self._update_line_numbers()
            self._highlight()
            self.current_file = None
            self.status.config(text=f"Loaded example: {Path(path).name}")
        except Exception as e:
            messagebox.showerror("Load example failed", str(e))

    def _toggle_dark(self):
        self._dark_mode = not self._dark_mode
        if self._dark_mode:
            bg, fg = "#1e1e1e", "#d4d4d4"
            num_bg = "#2d2d2d"
            self.editor.config(bg=bg, fg=fg, insertbackground=fg)
            self.editor.tag_configure("keyword", foreground="#569cd6")
            self.line_numbers.config(background=num_bg, foreground=fg)
            self.output_pane.config(bg=bg, fg=fg, insertbackground=fg)
        else:
            bg, fg = "white", "black"
            num_bg = "#e8e8e8"
            self.editor.config(bg=bg, fg=fg, insertbackground=fg)
            self.editor.tag_configure("keyword", foreground="#0000cc")
            self.line_numbers.config(background=num_bg, foreground=fg)
            self.output_pane.config(bg=bg, fg=fg, insertbackground=fg)
        self.status.config(text="Dark mode on." if self._dark_mode else "Dark mode off.")

    def _save(self):
        path = self.current_file or filedialog.asksaveasfilename(
            defaultextension=".nova",
            filetypes=[("NovaLang files", "*.nova"), ("All files", "*.*")],
        )
        if not path:
            return
        try:
            content = self.editor.get("1.0", tk.END)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            self.current_file = path
            self.status.config(text=f"Saved: {path}")
        except Exception as e:
            messagebox.showerror("Save failed", str(e))

    def run(self):
        self.root.mainloop()


def main():
    app = NovaGUI()
    app.run()


if __name__ == "__main__":
    main()
