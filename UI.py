import tkinter as tk


WIDTH = 600
HEIGHT = 800
loading = True

chat_text = []

root = tk.Tk()
root.title("Twitch Chat Bot")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='dota.png')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='#99bbff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

main_label = tk.Label(frame, font=40, text='Twitch Chat Bot')
main_label.place(relwidth=0.5, relheight=1)


button = tk.Button(frame, text='Join Chat!', font=40, command=lambda: "")
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#99bbff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=40)
label.place(relwidth=1, relheight=1)

entry = tk.Entry(lower_frame, font= 40)
entry.place(relwidth=1, relheight=0.1, rely=0.9)

send_button = tk.Button(entry, text='Send', font= 40)
send_button.place(relwidth=0.2,relheight=1, relx=0.8)


root.mainloop()