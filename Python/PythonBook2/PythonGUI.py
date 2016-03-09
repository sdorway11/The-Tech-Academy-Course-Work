import wx

class Frame(wx.Frame):
    # Added title parameter
    def __init__(self, title):
        # Title = title variable
        wx.Frame.__init__(self, None,\
        title="Python GUI", size=(300,200))
        self.Center()

        # Creating a button
        panel = wx.Panel(self)
        button = wx.Button(panel, label = "Exit",\
                           size=(100,40),pos=(100,30))

        # Bind the button to the function self.exit
        button.Bind(wx.EVT_BUTTON, self.exit)

        # Create Menu Bar
        menuBar = wx.MenuBar()
        #Create the menus
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        
        # Add fileMenu and editMenu to menuBar
        menuBar.Append(fileMenu, "File")
        menuBar.Append(editMenu, "Edit")
        
        # Add items to fileMenu
        fileMenu.Append(wx.NewId(), "New File", "Create a new file")
        fileMenu.Append(wx.NewId(), "Open", "Open a file")
        exitItem = fileMenu.Append(wx.NewId(), "Exit", "Exit the Program")

        # Bind exit item to exit function
        self.Bind(wx.EVT_MENU, self.exit, exitItem)

        self.SetMenuBar(menuBar)

        self.CreateStatusBar()

    # Add Exit Function
    def exit(self, event):
        self.Destroy()

    

app = wx.App()

# Pass the frame title
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
