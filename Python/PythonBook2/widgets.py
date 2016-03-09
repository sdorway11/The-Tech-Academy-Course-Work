import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(300,250))
        panel = wx.Panel(self)

##        wx.StaticText(panel, label="Static Box Text", pos=(10,10),\
##                      size=(280,200))
##
##        wx.StaticText(panel, label='Single line', pos=(100,100))

##        simpsons = ['Bart', 'Lisa', 'Maggie', 'Marge', 'Homer']
##        cb = wx.ComboBox(panel, pos=(100, 50), choices= simpsons,\
##                         style= wx.CB_READONLY)

##        wx.RadioButton(panel, label="Male", pos=(100,50), style= wx.RB_GROUP)
##        wx.RadioButton(panel, label="Female", pos=(100, 80))

##        wx.TextCtrl(panel, size=(200, -1), pos=(50, 30))
##        wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(200, 100), pos=(50, 80))        

        sc = wx.SpinCtrl(panel, value='0', pos=(130, 50), size=(70, 25))
        self.ValueText = wx.StaticText(panel, label='', pos=(130, 80))

        # Bind the spin control
        sc.Bind(wx.EVT_SPINCTRL, self.spinControl)

    def spinControl(self, event):
        # Get spin control value
        value = event.GetInt()

        # Update static value
        self.ValueText.SetLabel(str(value))
        
            
app = wx.App()
frame = Frame("wxPython Widgets!")
frame.Show()
app.MainLoop()
