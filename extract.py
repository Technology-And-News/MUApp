import wx
import urlfinder
import xFind
class extract(wx.Frame):
	def __init__(self):
		super().__init__(None, title="extract")
		self.Centre()
		panel = wx.Panel(self)
		self.re= wx.TextCtrl(panel , -1,style=wx.TE_MULTILINE+wx.HSCROLL)
		gitre = wx.Button(panel,-1,"&get result",pos=(335,30),size=(35,35))
		gitre.Bind(wx.EVT_BUTTON,self.onAdd)
		gitre.SetDefault()
		wx.StaticText(panel , -1, "links")
		self.links = wx.ListBox(panel, -1,)
		wx.StaticText(panel , -1, "Text in quotation marks")
		self.text = wx.ListBox(panel, -1,)
		clos = wx.Button(panel , -1, "&back")
		clos.Bind(wx.EVT_BUTTON, self.onback)
		self.Show()
	def onAdd(self,event):
		self.links.Set(urlfinder.find_urls(self.re.Value))
		self.text.Set(xFind.xFind(self.re.Value, '"', '"'))
	def onback(self, event):
		self.Close()



