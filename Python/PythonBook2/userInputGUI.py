import wx, userInputDatabaseGUI

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, \
            title=title, size=(800,700))
        self.Center()

        panel = wx.Panel(self)

        # Create the menu bar
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)

        self.CreateStatusBar()

        # Setup add new character UI
        # Create Static Box
        wx.StaticBox(panel, label='Add a new character', \
                     pos=(20,40), size=(280,190))

        # Text for name, gender, age, and occuptation
        wx.StaticText(panel, label='Name', pos =(30,70))
        wx.StaticText(panel, label='Gender', pos=(30,110))
        wx.StaticText(panel, label='Age', pos=(30,150))
        wx.StaticText(panel, label='Occupation', pos=(30,190))

        # Single line text boxes
        self.sName = wx.TextCtrl(panel, size=(150, -1), pos=(130, 70))
        self.sGen = wx.TextCtrl(panel, size=(150, -1), pos=(130, 110))
        self.sAge = wx.SpinCtrl(panel, size=(150, -1), pos=(130, 150))
        self.sOcc = wx.TextCtrl(panel, size=(150, -1), pos=(130, 190))

        # Save Button
        save = wx.Button(panel, label="Add Character", \
                         pos=(100, 230))
        save.Bind(wx.EVT_BUTTON, self.addCharacter)

        # Setup the Table UI
        # Setup Table as listCtrl
        self.listCtrl = wx.ListCtrl(panel, size =(400,400), pos =(350, 40), \
                               style = wx.LC_REPORT |wx.BORDER_SUNKEN)

        # Add columns to listCtrl
        self.listCtrl.InsertColumn(0, "ID")
        self.listCtrl.InsertColumn(1, "Name")
        self.listCtrl.InsertColumn(2, "Gender")
        self.listCtrl.InsertColumn(3, "Age")
        self.listCtrl.InsertColumn(4, "Occupation")

        # Add Data to list
        self.fillListCtrl()

        # Setup delete button
        deleteBtn = wx.Button(panel, label="Delete", pos=(640,450))

        # Run onSelect function when item is selected
        self.listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect)

        # Bind the delete button to function
        deleteBtn.Bind(wx.EVT_BUTTON, self.onDelete)

        # Setup Update Character UI
        # Create static box
        wx.StaticBox(panel, label='Update a Character', pos =(20,340), \
                     size=(280,190))

        # Text for name, gender, etc
        wx.StaticText(panel, label='Name:', pos=(30,370))
        wx.StaticText(panel, label='Gender:', pos=(30,410))
        wx.StaticText(panel, label='Age:', pos=(30,450))
        wx.StaticText(panel, label='Occupation:', pos=(30,490))

        # Single line text boxes
        self.sNameU = wx.TextCtrl(panel, size=(150,-1), pos=(130,370))
        self.sGenU = wx.TextCtrl(panel, size=(150,-1), pos=(130,410))
        self.sAgeU = wx.SpinCtrl(panel, value='0', pos=(130,450), size=(70,25))
        self.sOccU = wx.TextCtrl(panel, size=(150,-1), pos=(130,490))

        # Save Button
        saveUpdate = wx.Button(panel, label='Update Character', pos=(100,530))
        saveUpdate.Bind(wx.EVT_BUTTON, self.updateCharacter)

        

    # Create updateCharacter function
    def updateCharacter(self, event):
        name = self.sNameU.GetValue()
        gen = self.sGenU.GetValue()
        age = self.sAgeU.GetValue()
        occ = self.sOccU.GetValue()

        # Update the character
        userInputDatabaseGUI.updateCharacter(self.selectedId, name, gen, age, occ)

        # Refresh list control
        self.listCtrl.DeleteAllItems()
        self.fillListCtrl()
        

    # Create onDelete function
    def onDelete(self, event):
        
        # Delete the character
        userInputDatabaseGUI.deleteCharacter(self.selectedId)

        # Update listCtrl
        self.listCtrl.DeleteAllItems()
        self.fillListCtrl()

        

    # Create the onSelect function
    def onSelect(self, event):
        self.selectedId = event.GetText()

        # Get index of selected row
        index = event.GetIndex()

        # Get character info
        charInfo = self.allData[index]

        # Set value of update text boxes
        self.sNameU.SetValue(charInfo[1])
        self.sGenU.SetValue(charInfo[2])
        self.sAgeU.SetValue(charInfo[3])
        self.sOccU.SetValue(charInfo[4])

        print charInfo

        

    # Get Data from the database
    def fillListCtrl(self):
        self.allData = userInputDatabaseGUI.viewAll()

        for row in self.allData:
            # Loop through and append row
            self.listCtrl.Append(row)
        

    def addCharacter(self, event):
        name = self.sName.GetValue()
        gen = self.sGen.GetValue()
        age = self.sAge.GetValue()
        occ = self.sOcc.GetValue()

        # Check to see if variables have value
        if (name == '') or (gen == '') or \
           (age == '') or (occ == ''):

            # Alert user that a variable is missing
            dlg = wx.MessageDialog(None, 'Some character details are missing \
                                    Please enter values in each text box.', \
                                   'Missing Details!', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            return False
            

        # Adding Character to database
        userInputDatabaseGUI.newCharacter(name, gen, age, occ)
        print userInputDatabaseGUI.viewAll()

        print name
        print gen
        print age
        print occ

        # Reset the values
        self.sName.Clear()
        self.sGen.Clear()
        self.sAge.SetValue(0)
        self.sOcc.Clear()

        # Update listCtrl
        self.listCtrl.DeleteAllItems()
        self.fillListCtrl()

    def exitProgram(self, event):
        self.Destroy()
        


app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
