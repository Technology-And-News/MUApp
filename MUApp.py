import HelpAndSettings
import TextToSpeechM
import TextToSpeachG
import notepad
import SearchMultipleSites
import RandomSelection
import SimpleCalculator
import LirnBraillesForBlind
import HTML
import md
import extract
import wx
class MUApp(wx.Frame): # كلاس الواجهة الرئيسية للبرنامج
	def __init__(self):
		super().__init__(None, title="MUapp")
		self.Center()
		p = wx.Panel(self)
		HAS= wx.Button(p, -1, "HelpAnd&Settings")
		notep = wx.Button(p, -1, "Notepad")
		SearchMultipleSite = wx.Button(p, -1, "SearchMultipleSites")
		textt = wx.Button(p, -1, "TextToSpeech")
		textt.Bind(wx.EVT_BUTTON, self.onTTS)
		randomSelection = wx.Button(p, -1, "RandomSelection")
		SimpleCalculat= wx.Button(p, -1, "SimpleCalculator")
		LirnBrailleForBlind= wx.Button(p, -1, "LearnBrailleForBlind")
		htmls= wx.Button(p, -1, "Create HTML")
		mds= wx.Button(p, -1, "Create Markdown")
		extraction= wx.Button(p, -1, """extract links or "text" """)
		self.Show()
		self.Bind(wx.EVT_BUTTON, lambda event: HelpAndSettings.HelpAndSettings(), HAS)
		self.Bind(wx.EVT_BUTTON, lambda event: notepad.Notepad(), notep)
		self.Bind(wx.EVT_BUTTON, lambda event: SearchMultipleSites.SearchMultipleSites(), SearchMultipleSite)
		self.Bind(wx.EVT_BUTTON, lambda event: RandomSelection.RandomSelection(), randomSelection)
		self.Bind(wx.EVT_BUTTON, lambda event: SimpleCalculator.SimpleCalculator(), SimpleCalculat)
		self.Bind(wx.EVT_BUTTON, lambda event: LirnBraillesForBlind.LearnBrailleForBlind(), LirnBrailleForBlind)
		self.Bind(wx.EVT_BUTTON, lambda event: HTML.html(), htmls)
		self.Bind(wx.EVT_BUTTON, lambda event: md.Markdown(), mds)
		self.Bind(wx.EVT_BUTTON, lambda event: extract.extract(), extraction)

	def onTTS(self, event):
		add1= wx.MessageDialog(self, "choose the text-to-speech service", "text to speach", style=wx.YES_NO+wx.CANCEL)
		add1.SetYesNoCancelLabels("google", "microsoft", "back")
		if add1.ShowModal() == wx.ID_YES:
			TextToSpeachG.texttospeech()
		elif add1.ShowModal() == wx.ID_NO:
			TextToSpeechM.texttospeechm()
		else:
				retern

app = wx.App()
MUApp()
app.MainLoop()