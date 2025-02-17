import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageTk

class GraphDigitizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Digitizer Wizard")
        
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()
        
        self.image_path = None
        self.image = None
        self.tk_image = None
        
        self.zoom_factor = 1.0
        self.points = []
        self.origin = None
        self.x_axis = None
        self.y_axis = None
        self.x_max = None
        self.y_max = None
        
        self.start_wizard()
        
    def start_wizard(self):
        messagebox.showinfo("Step 1", "Select the graph image file")
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        if not self.image_path:
            return
        
        self.image = Image.open(self.image_path)
        self.display_image()
        
        messagebox.showinfo("Step 2", "Click on the origin (0,0)")
        self.canvas.bind("<Button-1>", self.get_origin)
        
    def get_origin(self, event):
        self.origin = (event.x, event.y)
        self.canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2, fill='green')
        
        messagebox.showinfo("Step 3", "Click on the extreme point of the X-axis")
        self.canvas.bind("<Button-1>", self.get_x_axis)
    
    def get_x_axis(self, event):
        self.x_axis = (event.x, event.y)
        self.x_max = float(simpledialog.askstring("X-axis", "Enter maximum value for X-axis:"))
        self.canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2, fill='blue')
        
        messagebox.showinfo("Step 4", "Click on the extreme point of the Y-axis")
        self.canvas.bind("<Button-1>", self.get_y_axis)
    
    def get_y_axis(self, event):
        self.y_axis = (event.x, event.y)
        self.y_max = float(simpledialog.askstring("Y-axis", "Enter maximum value for Y-axis:"))
        self.canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2, fill='yellow')
        
        messagebox.showinfo("Step 5", "Click on points along the curves to record their coordinates.")
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<MouseWheel>", self.on_zoom)
        
    def display_image(self):
        self.canvas.delete("all")  # Clear the canvas
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        image_ratio = self.image.width / self.image.height
        canvas_ratio = canvas_width / canvas_height
        
        if image_ratio > canvas_ratio:
            self.zoom_factor = canvas_width / self.image.width
        else:
            self.zoom_factor = canvas_height / self.image.height
        
        resized_image = self.image.resize((int(self.image.width * self.zoom_factor), int(self.image.height * self.zoom_factor)))
        self.tk_image = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(canvas_width // 2, canvas_height // 2, image=self.tk_image)
    
    def scale_point(self, x, y):
        x_scaled = self.x_max * (x - self.origin[0]) / (self.x_axis[0] - self.origin[0])
        y_scaled = self.y_max * (self.origin[1] - y) / (self.origin[1] - self.y_axis[1])
        return x_scaled, y_scaled
    
    def on_click(self, event):
        x, y = event.x, event.y
        x_scaled, y_scaled = self.scale_point(x, y)
        self.points.append((x_scaled, y_scaled))
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill='red')
        
    def on_zoom(self, event):
        self.zoom_factor *= 1.1 if event.delta > 0 else 0.9
        self.display_image()
        
    def save_points(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not save_path:
            return
        
        with open(save_path, 'w') as file:
            file.write("x_scaled,y_scaled\n")
            for point in self.points:
                file.write(f"{point[0]},{point[1]}\n")
        
        messagebox.showinfo("Saved", f"Points saved to {save_path}")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = GraphDigitizerApp(root)
    save_button = tk.Button(root, text="Save Points", command=app.save_points)
    save_button.pack()
    root.mainloop()
