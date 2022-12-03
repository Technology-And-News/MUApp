import wx





class Notepad(wx.Frame): # كلاس الواجهة الرئيسية للبرنامج
	def __init__(self):
		super().__init__(None, title="untitled- notepad")
		self.Center()
		self.activeFile = None
		p = wx.Panel(self)
		wx.StaticText(p, -1, "Input/Result")
		self.content = wx.TextCtrl(p, -1, style=wx.TE_MULTILINE + wx.HSCROLL+wx.TE_PROCESS_TAB)
		menubar = wx.MenuBar()
		file = wx.Menu()
		open =file.Append(-1, "open 	ctrl+o")
		save =file.Append(-1, "save 	ctrl+s")
		clos =file.Append(-1, "back 	alt+b")



		menubar.Append(file, "file") 

		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_MENU, self.onOpen,open)
		self.Bind(wx.EVT_MENU, self.onSave,save)
		self.Bind(wx.EVT_MENU, self.onback,clos )



		self.Show()

	def onOpen(self, event):
		openDialog = wx.FileDialog(self, "open")
		result = openDialog.ShowModal()
		if result == wx.ID_CANCEL:
			return

		path = openDialog.Path
		filename = openDialog.Filename
		file = open(path, "r", encoding="utf-8")
		self.content.Value = file.read()
		file.close()
		self.Title = f"{filename} - notepad"
		self.activeFile = path

	def onSave(self, event):
		if not self.activeFile:
			saveDialog = wx.FileDialog(self, "save", style=wx.FD_SAVE)
			saveDialog.Wildcard = "text file(.txt(|*.txt||all file*.*"
			result = saveDialog.ShowModal()
			if result == wx.ID_CANCEL:
				return
			path = saveDialog.Path
			filename = saveDialog.Filename
			self.Title = f"{filename} - notepad"
		else:
			path = self.activeFile
		file = open(path, "w", encoding="utf-8")
		file.write(self.content.Value)
		file.close()
		self.activeFile = path
		self.content.SetModified(False)
		wx.MessageBox(f"saved in {path}","file")
	def onOpen(self, event):
		openDialog = wx.FileDialog(self, "open")
		result = openDialog.ShowModal()
		if result == wx.ID_CANCEL:
			return

		path = openDialog.Path
		filename = openDialog.Filename
		file = open(path, "r", encoding="utf-8")
		self.content.Value = file.read()
		file.close()
		self.Title = f"{filename} - notepad"
		self.activeFile = path
	def onback(self, event):
		self.Close()






