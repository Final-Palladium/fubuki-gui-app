def main():
    import tkinter as tk
    import webbrowser

    def callback(url):
        webbrowser.open(url)

    # Create a window
    window = tk.Tk()

    # Give it a title
    window.title('My Frist Python GUI')

    # Change the background color
    window.configure(background='#fefefe')

    # Set window size
    window.geometry('414x825')

    # Forbid window resize
    window.resizable(0,0)

    # Create a figure object
    figure = tk.PhotoImage(file='./resources/fubuki.gif')

    # Show the figure on screen using a label
    tk.Label (window, image=figure, bg='#fefefe') .grid(row=0, column=0, padx=1, sticky='W')

    # Show a text label
    tk.Label (window, text='Shirakami Fubuki from Hololive', bg='#fefefe', font='none 14 bold') .grid(row=1, column=0, sticky='')

    tk.Label (window, text='Art by @kanzakihiro', bg='#fefefe', font='none 12') .grid(row=2, column=0, sticky='')

    # Create a button
    button_one = tk.Button(window, text='Click me!', width=12, cursor='hand2', command= lambda: callback('https://youtu.be/M6BfX92LqSo'))
    button_one.grid(row=3, column=0, pady=5, sticky='')

    # Show the window
    window.mainloop()


if __name__ == "__main__":
    main()
