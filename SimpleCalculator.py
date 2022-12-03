import wx
class SimpleCalculator(wx.Frame):
	def __init__(self):
		super().__init__(None, title="simple calculator")
		self.Center()
		p = wx.Panel(self)
		wx.StaticText(p, -1, "number1")
		self.number1= wx.TextCtrl(p, -1)
		wx.StaticText(p, -1, "value")
		self.value= wx.ComboBox(p, -1,choices=["+","-","*","/","<",">","<=",">=","no="])
		self.value.Selection = 0
		wx.StaticText(p, -1, "number2")
		self.number2= wx.TextCtrl(p, -1)
		r= wx.Button(p, -1, "&get result")
		r.Bind(wx.EVT_BUTTON, self.onr)
		wx.StaticText(p, -1, "result")
		self.re= wx.TextCtrl(p, -1,style=wx.TE_MULTILINE+wx.HSCROLL+wx.TE_READONLY)
		exit = wx.Button(p,-1,"&back")
		self.Bind(wx.EVT_BUTTON,self.onExit,exit)
		self.Show()
	def onr(self, event):
		self.re.Value=""
		num1=float(self.number1.Value)
		num2=float(self.number2.Value)
		if self.value.Value=="+":
			plus=num1+num2
			self.re.Value=f"{plus}"
		elif self.value.Value=="-":
			m1=num1-num2
			self.re.Value=f"{m1}"
		elif self.value.Value=="*":
			s1=num1*num2
			self.re.Value=f"{s1}"
		elif self.value.Value=="/":
			l1=num1/num2
			self.re.Value=f"{l1}"
		elif self.value.Value=="<":
			d1=num1<num2
			self.re.Value=f"{d1}"
		elif self.value.Value==">":
			g1=num1>num2
			self.re.Value=f"{g1}"
		elif self.value.Value=="<=":
			se1=num1<=num2
			self.re.Value=f"{se1}"
		elif self.value.Value==">=":
			ge1=num1>=num2
			self.re.Value=f"{ge1}"
		elif self.value.Value=="no=":
			no1=num1!=num2
			self.re.Value=f"{no1}"


	def onExit(self, event):
		self.Close()
