import wx

print "Iniciando App wx"
app=wx.App()
frame=wx.Frame(None,wx.ID_ANY,"proyector")
frame.SetBackgroundColour("black")
frame.ShowFullScreen(True)
frame.Show(True)
app.MainLoop()
