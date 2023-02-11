import customtkinter
import modules.finiding_path as m_path
import PIL

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.APP_WIDTH = 400
        self.APP_HEIGHT = 350
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()

        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.SCREEN_WIDTH // 2 - self.APP_WIDTH // 2}+{self.SCREEN_HEIGHT // 2 - self.APP_HEIGHT // 2}")
        self.resizable(False, False)
        self.IMAGE = customtkinter.CTkImage(
            dark_image = PIL.Image.open(m_path.search("img/1.png")), 
            size = (self.APP_WIDTH, self.APP_HEIGHT)
        )
        self.IMAGE_LABEL = customtkinter.CTkLabel(master = self, text = "", image = self.IMAGE)
        self.IMAGE_LABEL.grid(row = 10, column = 10)
