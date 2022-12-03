import os
import wx
from gtts import gTTS
# os.chdir(os.path.dirname(__file__ + "\Documents"))

class texttospeech(wx.Frame): # كلاس الواجهة الرئيسية للبرنامج
	def __init__(self):
		super().__init__(None, title="google Text to speech")
		self.Center()
		self.activeFile = None
		p = wx.Panel(self)
		open = wx.Button(p, -1, "&open text file", pos=(10,235), size=(100,30))
		open.Bind(wx.EVT_BUTTON, self.onOpen)
		wx.StaticText(p, -1, "text ")
		self.ttss = wx.TextCtrl(p, -1, style=wx.TE_MULTILINE + wx.HSCROLL)
		wx.StaticText(p, -1, "file name")
		self.filename= wx.TextCtrl(p, -1)
		wx.StaticText(p, -1, "Language code Example Arabic:ar English:en French:fr")
		self.language= wx.TextCtrl(p, -1)
		self.language.Value="en"
		save = wx.Button(p, -1, "&save")
		save.Bind(wx.EVT_BUTTON, self.onSave)
		back = wx.Button(p, -1, "&back", pos=(10,235), size=(100,30))
		back.Bind(wx.EVT_BUTTON, self.onback)
		self.Show()
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


	def onSave(self, event):
		tts = gTTS(self.ttss.Value, lang=self.language.Value)
		tts.save(self.filename.Value + '.mp3')


	def onback(self, event):
		self.Close()

