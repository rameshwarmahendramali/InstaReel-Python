import tkinter as tk
from tkinter import messagebox
from instaloader import Instaloader, Post, Profile

def download_video_from_link(video_link, target_filename):
    L = Instaloader()
    try:
        post = Post.from_shortcode(L.context, video_link.split("/")[-2])
        if post.is_video:
            L.download_post(post, target=target_filename)
            return True
        else:
            messagebox.showinfo("Not a Video", "The provided link is not for a video.")
    except Exception as e:
        messagebox.showerror("Error", f"Error downloading video: {str(e)}")
    return False

def download_button_clicked():
    video_link = entry.get()
    target_filename = entry_filename.get()
    if video_link and target_filename:
        if download_video_from_link(video_link, target_filename):
            messagebox.showinfo("Success", "Download completed!")
    else:
        messagebox.showerror("Error", "Enter both video link and target filename.")

# Create the main window
root = tk.Tk()
root.title("Instagram Downloader")

# Set window size and position
window_width = 500
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f'{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}')

# Set window background color
root.config(bg='#f0f0f0')

# Create and pack widgets
label_link = tk.Label(root, text="Enter Instagram Video Link:", bg='#f0f0f0')
label_link.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

label_filename = tk.Label(root, text="Enter Target Filename (with extension):", bg='#f0f0f0')
label_filename.pack(pady=10)

entry_filename = tk.Entry(root, width=30)
entry_filename.pack(pady=10)

download_button = tk.Button(root, text="Download Video", command=download_button_clicked, bg='#0088cc', fg='#ffffff')
download_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
