import os
import wx
import NBSapi
# os.chdir(os.path.dirname(__file__ + "\Documents"))
tts = NBSapi.NBSapi()
class texttospeechm(wx.Frame): # كلاس الواجهة الرئيسية للبرنامج
	def __init__(self):
		super().__init__(None, title="microsoft Text to speech")
		self.Center()
		self.activeFile = None
		p = wx.Panel(self)
		open = wx.Button(p, -1, "&open text file", pos=(10,235), size=(100,30))
		open.Bind(wx.EVT_BUTTON, self.onOpen)
		wx.StaticText(p, -1, "text ")
		self.ttss = wx.TextCtrl(p, -1, style=wx.TE_MULTILINE + wx.HSCROLL)
		wx.StaticText(p, -1, "Rate")
		self.rate = wx.SpinCtrl(p, -1, min=-100, max=100, initial = 0)
		wx.StaticText(p, -1, "Volume")
		self.volume= wx.SpinCtrl(p, -1, min=1, max=100, initial = 100)
		play = wx.Button(p, -1, "play", pos=(10,235), size=(100,30))
		play.Bind(wx.EVT_BUTTON, self.onplay)
		save = wx.Button(p, -1, "&save")
		save.Bind(wx.EVT_BUTTON, self.onSave)
		back = wx.Button(p, -1, "&back", pos=(10,235), size=(100,30))
		back.Bind(wx.EVT_BUTTON, self.onback)
		menubar = wx.MenuBar()
		file = wx.Menu()
		play1=file.Append(-1, "play 	f5")
		pause=file.Append(-1, "Pause	f6")
		resume=file.Append(-1, "Resume 	f7")
		stop=file.Append(-1, "Stop 	f8")
		menubar.Append(file, "program") 
		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_MENU, self.onplay,play1)
		self.Show()
		self.Bind(wx.EVT_MENU, lambda event:tts.Pause() , pause)
		self.Bind(wx.EVT_MENU, lambda event:tts.Resume() , resume)
		self.Bind(wx.EVT_MENU, lambda event:tts.Stop() , stop)
	def onOpen(self, event):
		openDialog = wx.FileDialog(self, "open")
		result = openDialog.ShowModal()
		if result == wx.ID_CANCEL:
			return

		path = openDialog.Path
		filename = openDialog.Filename
		file = open(path, "r", encoding="utf-8")
		self.ttss.Value = file.read()
		file.close()


	def onplay(self, event):
		tts.SetRate(self.rate.Value)
		tts.SetVolume(self.volume.Value)
		tts.Speak(self.ttss.Value, 1)

	def onSave(self, event):
		txeet=wx.GetTextFromUser("file name")
		tts.SpeakToFile(self.ttss.Value, f"{txeet}.Wav", 0)
	def onback(self, event):
		self.Close()

