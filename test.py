import tkinter as tk
from tkinter import scrolledtext

def add_entry():
    # 入力されたテキストを取得
    entered_text = entry.get()
    # 入力フィールドをクリア
    entry.delete(0, tk.END)

    # 入力が空でない場合
    if entered_text:
        # 各出力テキストボックスにテキスト追加
        for output in [output_text1, output_text2, output_text3]:
            output.configure(state=tk.NORMAL)
            output.insert(tk.END, entered_text + "\n")
            output.configure(state=tk.DISABLED)
            output.see(tk.END)  # テキストエリアの最後にスクロール

# メインウィンドウの作成
root = tk.Tk()
root.title("Tkinter 入力と 3つの出力")
root.geometry("800x400")

# 入力フィールド
entry = tk.Entry(root)
entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

# 送信ボタン
submit_button = tk.Button(root, text="送信", command=add_entry)
submit_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# 上部の出力フィールド1
output_text1 = scrolledtext.ScrolledText(root, state='disabled')
output_text1.grid(row=0, column=1, rowspan=2, padx=5, pady=5, sticky="nsew")

# 上部の出力フィールド2
output_text2 = scrolledtext.ScrolledText(root, state='disabled')
output_text2.grid(row=0, column=2, rowspan=2, padx=5, pady=5, sticky="nsew")

# 下部の出力フィールド3
output_text3 = scrolledtext.ScrolledText(root, height=10, state='disabled')
output_text3.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

# ウィジェットを適切にスケールするためのグリッド設定
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=0)  # 入力フィールドとボタンの列は固定幅
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# GUIのメインループを開始
root.mainloop()