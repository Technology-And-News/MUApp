import winsound
import wx
import random
class RandomSelection(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,parent=None,title="random selection",name="random selection")
		self.Centre()
		panel = wx.Panel(self)
		self.names=[]
		self.namesBox = wx.ListBox(panel, -1,choices=self.names)
		add = wx.Button(panel,-1,"&add...",pos=(335,30),size=(35,35))
		s = wx.Button(panel,-1,"choo&se name")
		exit = wx.Button(panel,-1,"&back")
		add.Bind(wx.EVT_BUTTON,self.onAdd)
		add.SetDefault()
		self.Bind(wx.EVT_BUTTON,self.onChoose,s)
		self.Bind(wx.EVT_BUTTON,self.onExit,exit)
		self.contextSetup()
		self.Show()
	def onAdd(self,event):
		name = wx.GetTextFromUser("inter name", "RandomSelection")
		add1= wx.MessageDialog(self, "Is the answer true or false?", "answer case", style=wx.YES_NO+wx.YES_DEFAULT+wx.ICON_WARNING+wx.ICON_QUESTION)
		add1.SetYesNoLabels("&true answer ", "&false answer ")
		if add1.ShowModal() == wx.ID_YES:
			self.names.append(name)
			self.namesBox.Append(f"{name} answer case: true")
		else:
			self.namesBox.Append(f"{name} answer case: false")

	def onChoose(self,event):
		choice = random.choice(self.names)
		wx.MessageBox("the winner is "+choice,self.GetTitle(),parent=self)
		winsound.PlaySound('sounds/applause4.wav', 1)

	def onExit(self, event):
		self.Close()



	def onremove(self,event):
		index2 = self.namesBox.GetSelection()
		index1 = self.namesBox.GetStringSelection()
		self.namesBox.Delete(index2)
		self.names.remove(index1)



	def contextSetup(self):
		context = wx.Menu()
		removes = context.Append(-1, "&delete")
		self.Bind(wx.EVT_MENU, self.onremove,removes)
		self.namesBox.Bind(wx.EVT_CONTEXT_MENU, lambda event: self.PopupMenu(context))



