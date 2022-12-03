import wx
class LearnBrailleForBlind(wx.Frame):
	def __init__(self):
		super().__init__(None, title="LearnBrailleForBlind")
		self.Center()
		p = wx.Panel(self)
		wx.StaticText(p, -1, "letter")
		self.t= wx.ComboBox(p, -1,choices=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","؛",".",",","@","=","+","-","*","/","#","ا","ب","ت","ث","ج","ح","خ","د","ذ","ر","ز","س","ش","ص","ض","ط","ظ","ع","غ","ف","ق","ك","ل","م","ن","ه","و","ي","لا","أ","إ","ى","آ","ة","ِ","ٍ","َ","ً","ُ","ٌ","ْ","ّ","ئ","ء","ؤ","ال","على"])

		get = wx.Button(p, -1, "&get letter", pos=(10,235), size=(100,30))
		get.SetDefault()
		get.Bind(wx.EVT_BUTTON, self.onOpen)
		back = wx.Button(p, -1, "&back", pos=(10,235), size=(100,30))
		back.Bind(wx.EVT_BUTTON, self.onback)
		self.Show()
	def onOpen(self, event):
		a=self.t.Value
		if a =="a":
			wx.MessageBox ("1.","")
		elif a =="b":
			wx.MessageBox("1. 2.","")
		elif a =="c":
			wx.MessageBox("1. 4.","")
		elif a =="d":
			wx.MessageBox("1. 4. 5.","")
		elif a =="e":
			wx.MessageBox("1. 5.","")
		elif a =="f":
			wx.MessageBox("1. 2. 4.","")
		elif a =="g":
			wx.MessageBox("1. 2. 4. 5. ","")
		elif a =="h":
			wx.MessageBox("1. 2. 5.","")
		elif a =="i":
			wx.MessageBox("2. 4.","")
		elif a =="j":
			wx.MessageBox("2. 4. 5.","")
		elif a =="k":
			wx.MessageBox("1. 3.","")
		elif a =="l":
			wx.MessageBox("1. 2. 3.","")
		elif a =="m":
			wx.MessageBox("1. 3. 4.","")
		elif a =="n":
			wx.MessageBox("1. 3. 4. 5.","")
		elif a =="o":
			wx.MessageBox("1. 3. 5. ","")
		elif a =="p":
			wx.MessageBox("1. 2. 3. 4.","LearnBrailleForBlind")
		elif a =="q":
			wx.MessageBox("1. 2. 3. 4. 5.","")
		elif a =="r":
			wx.MessageBox("1. 2. 3. 5.","")
		elif a =="s":
			wx.MessageBox("2. 3. 4.","")
		elif a =="t":
			wx.MessageBox("2. 3. 4. 5.","")
		elif a =="u":
			wx.MessageBox("1. 3. 6.","")
		elif a =="v":
			wx.MessageBox("1. 2. 3. 6.","LearnBrailleForBlind")
		elif a =="w":
			wx.MessageBox("2. 4. 5. 6.","LearnBrailleForBlind")
		elif a =="x":
			wx.MessageBox("1. 3. 4. 6.","LearnBrailleForBlind")
		elif a =="y":
			wx.MessageBox("1. 3. 4. 5. 6.","LearnBrailleForBlind")
		elif a =="z":
			wx.MessageBox("1. 3. 5. 6.","LearnBrailleForBlind")
		elif a =="1":
			wx.MessageBox("1.","LearnBrailleForBlind")
		elif a =="2":
			wx.MessageBox("1. 2.","LearnBrailleForBlind")
		elif a =="3":
			wx.MessageBox("1. 4.","LearnBrailleForBlind")
		elif a =="4":
			wx.MessageBox("1. 4. 5.","LearnBrailleForBlind")
		elif a =="5":
			wx.MessageBox("1. 5.","LearnBrailleForBlind")
		elif a =="6":
			wx.MessageBox("1. 2. 4.","LearnBrailleForBlind")
		elif a =="7":
			wx.MessageBox("1. 2. 4. 5.","LearnBrailleForBlind")
		elif a =="8":
			wx.MessageBox("1. 2. 5.","LearnBrailleForBlind")
		elif a =="9":
			wx.MessageBox("2. 4.","LearnBrailleForBlind")
		elif a =="0":
			wx.MessageBox("2. 4. 5.","LearnBrailleForBlind")
		elif a =="@":
			wx.MessageBox("4.","LearnBrailleForBlind")
		elif a =="+":
			wx.MessageBox("2. 6.","LearnBrailleForBlind")
		elif a =="-":
			wx.MessageBox("3. 5.","LearnBrailleForBlind")
		elif a =="*":
			wx.MessageBox("1. 6.","LearnBrailleForBlind")
		elif a =="/":
			wx.MessageBox("3. 4.","LearnBrailleForBlind")
		elif a ==".":
			wx.MessageBox("2. 5. 6.","LearnBrailleForBlind")
		elif a ==",":
			wx.MessageBox("2.","LearnBrailleForBlind")
		elif a =="'":
			wx.MessageBox("3.","LearnBrailleForBlind")
		elif a =="؛":
			wx.MessageBox("5. 6.","LearnBrailleForBlind")
		elif a =="=":
			wx.MessageBox("2. 5. 2. 5.","LearnBrailleForBlind")
		elif a =="#":
			wx.MessageBox("3. 4. 5. 6.","LearnBrailleForBlind")
		elif a =="ا":
			wx.MessageBox("1.","LearnBrailleForBlind")
		elif a =="ب":
			wx.MessageBox("1. 2.","LearnBrailleForBlind")
		elif a =="ت":
			wx.MessageBox("2. 3. 4. 5.","LearnBrailleForBlind")
		elif a =="ث":
			wx.MessageBox("1. 4. 5. 6.","LearnBrailleForBlind")
		elif a =="ج":
			wx.MessageBox("2. 4. 5.","LearnBrailleForBlind")
		elif a =="ح":
			wx.MessageBox("1. 5. 6.","LearnBrailleForBlind")
		elif a =="خ":
			wx.MessageBox("1. 3. 4. 6.","LearnBrailleForBlind")
		elif a =="د":
			wx.MessageBox("1. 4. 5.","LearnBrailleForBlind")
		elif a =="ذ":
			wx.MessageBox("2. 3. 4. 6.","LearnBrailleForBlind")
		elif a =="ر":
			wx.MessageBox("1. 2. 3. 5.","LearnBrailleForBlind")
		elif a =="ز":
			wx.MessageBox("1. 3. 5. 6.","LearnBrailleForBlind")
		elif a =="س":
			wx.MessageBox("2. 3. 4.","LearnBrailleForBlind")
		elif a =="ش":
			wx.MessageBox("1. 4. 6.","LearnBrailleForBlind")
		elif a =="ص":
			wx.MessageBox("1. 2. 3. 4. 6.","LearnBrailleForBlind")
		elif a =="ض":
			wx.MessageBox("1. 2. 4. 6.","LearnBrailleForBlind")
		elif a =="ط":
			wx.MessageBox("2. 3. 4. 5. 6.","LearnBrailleForBlind")
		elif a =="ظ":
			wx.MessageBox("1. 2. 3. 4. 5. 6.","LearnBrailleForBlind")
		elif a =="ع":
			wx.MessageBox("1. 2. 3. 5. 6.","LearnBrailleForBlind")
		elif a =="غ":
			wx.MessageBox("1. 2. 6.","LearnBrailleForBlind")
		elif a =="ف":
			wx.MessageBox("1. 2. 4.","LearnBrailleForBlind")
		elif a =="ق":
			wx.MessageBox("1. 2. 3. 4. 5.","LearnBrailleForBlind")
		elif a =="ك":
			wx.MessageBox("1. 3.","LearnBrailleForBlind")
		elif a =="ل":
			wx.MessageBox("1. 2. 3.","LearnBrailleForBlind")
		elif a =="م":
			wx.MessageBox("1. 3. 4.","LearnBrailleForBlind")
		elif a =="ن":
			wx.MessageBox("1. 3. 4. 5.","LearnBrailleForBlind")
		elif a =="ه":
			wx.MessageBox("1. 2. 5.","LearnBrailleForBlind")
		elif a =="و":
			wx.MessageBox("2. 4. 5. 6.","LearnBrailleForBlind")
		elif a =="ي":
			wx.MessageBox("2. 4.","LearnBrailleForBlind")
		elif a =="لا":
			wx.MessageBox("1. 2. 3. 6.","LearnBrailleForBlind")
		elif a =="أ":
			wx.MessageBox("3. 4.","LearnBrailleForBlind")
		elif a =="إ":
			wx.MessageBox("4. 6.","LearnBrailleForBlind")
		elif a =="ى":
			wx.MessageBox("1. 3. 5.","LearnBrailleForBlind")
		elif a =="آ":
			wx.MessageBox("3. 4. 5.","LearnBrailleForBlind")
		elif a =="ة":
			wx.MessageBox("1. 6.","LearnBrailleForBlind")
		elif a =="ِ":
			wx.MessageBox("1. 5. ","LearnBrailleForBlind")
		elif a =="ٍ":
			wx.MessageBox("3. 5.","LearnBrailleForBlind")
		elif a =="َ":
			wx.MessageBox("2","LearnBrailleForBlind")
		elif a =="ً":
			wx.MessageBox("2. 3.","LearnBrailleForBlind")
		elif a =="ُ":
			wx.MessageBox("1. 3. 6.","LearnBrailleForBlind")
		elif a =="ٌ":
			wx.MessageBox("2. 6.","LearnBrailleForBlind")
		elif a =="ْ":
			wx.MessageBox("2. 5.","LearnBrailleForBlind")
		elif a =="ّ":
			wx.MessageBox("6.","LearnBrailleForBlind")
		elif a =="ئ":
			wx.MessageBox("1. 3. 4. 5. 6.","LearnBrailleForBlind")
		elif a =="ء":
			wx.MessageBox("3.","LearnBrailleForBlind")
		elif a =="ؤ":
			wx.MessageBox("1. 2. 5. 6.","LearnBrailleForBlind")
		elif a =="ال":
			wx.MessageBox("1. 4.","LearnBrailleForBlind")
		elif a =="على":
			wx.MessageBox("1. 3. 5.","LearnBrailleForBlind")
	def onback(self, event):
		self.Close()
