import webbrowser
import wx
class HelpAndSettings(wx.Frame): # كلاس الواجهة الرئيسية للبرنامج
	def __init__(self):
		super().__init__(None, title="HelpAndSettings")
		self.Center()
		p = wx.Panel(self)
		wx.StaticText(p, -1, "help")
		self.re= wx.TextCtrl(p, -1,style=wx.TE_MULTILINE+wx.HSCROLL+wx.TE_READONLY)
		self.re.Value="""MU app
Multi Usage Application (MU App)
• Name: "MU App".
• Version: 1.0.
• Release date: December 2, 2022, 8:00 PM (UTC) Coordinated Universal Time.
• Program Developers: Mohamed Amr and Anas Mohammed.
• Description: A versatile portable program with a very simple graphical interface free of complications.
You will find a lot of tools in this program, and we will explain them now.
Tools
Notepad
A simple notepad tool that allows you to create, open and save text files.
Go to the File menu by pressing the Alt key to find the save and open options, or you can use the following keyboard shortcuts.
• CTRL+O: Open a new file.
• CTRL+S: Save the file.
• ALT+B or ALT+F4: Return to the MU App window.
Search Multiple Sites
A tool that allows you to search in multiple and various sites, including:
search engines
• Google
• bing
• yahoo
• ecosia
• DuckDuckGo
And also search in Arabic, English and French Wikipedia.
You can search on other sites such as YouTube and Amazon, and you can type or paste a link to open it in the browser.
Another feature of Search Multiple Sites: Share text on
With this feature you can share any text you write in some sites, just type the text and press ALT+S, then choose the site you want to share the text on.
Text to Speech
A simple text-to-speech tool, when you open it will prompt you to choose a text-to-speech service.
The supported services are Google and Microsoft, press the Tab key and choose what you want.
• Note: Microsoft Text-to-Speech only supports English (US) with David's voice.
When choosing Google you will find the following items.
• Open Text File: To fetch text from TXT files.
• Text: to enter text manually.
• Filename: To Enter the filename to be saved.
• Language code: To enter the language code, e.g: Arabic: ar, English: en, French: fr.
• Save: to save the file in MP3 format.
◦ It will be saved next to the program's executable file, regardless of its path.
• Press ALT+B/ALT+F4 to return to the MU App window.
When choosing Microsoft you will find the following items.
• Open Text File: To fetch text from TXT files.
• Text: to enter text manually.
• Rate: To Specify/type the speech rate for the file to be saved, from 100 to -100, (the default is 0).
• Volume: To Specify/type the volume of the file to be saved, from 1 to 100 (the default is 100).
• Keyboard shortcuts: Press F5 to preview the audio, F6 to pause the preview, F7 to resume the preview.
• Save: to save the file (in WAV format).
◦ It will be saved next to the program's executable file, regardless of its path.
• Press ALT+B/ALT+F4 to return to the MU App window.
Random Selection
A simple electronic lottery, when you open it you will find the following items.
• names list.
• Add... To add a new name to the names list, you can press the Enter key from anywhere to quickly open it.
• choose name: to choose a random name from the added names list.
Notes.
• To delete a name from the names list, select the name you want to delete, then press the Applications key and press Delete.
• When you add a name to the names list, you will see a dialogue, you can choose whether this answer is correct or not.
◦ You can press T for the true answer, or F for the false answer.
• Press ALT+B/ALT+F4 to return to the MU App window.
simplecalculator
A simple calculator, when you open it you will find the following items.
• number 1: To type the first number
• Value: To Specify/type the value, e.g: plus, minus, or equals.
• number 2: To type the second number.
• Get Result: To get the result.
◦ The result will be displayed in the result edit box.
• Press ALT+B/ALT+F4 to return to the MU App window.
Learn Braille For Blind
A tool to learnning Braille for Blind, when you open it you will find the following items.
• Letter: To select/type the letter whose dots is required for Braille.
• get letter: to get dots for the letter.
• Press ALT+B/ALT+F4 to return to the MU App window.
Create HTML
A tool to write HTML codes easily. When you open it, you will find the following items.
• HTML: This is an edit box into which the results of the currently opened file are written/displayed.
◦ By pressing the Application key on the edit box, you can insert a link, paragraph, or title.
• Open: to open and modify HTML files.
• Save: to save the file.
• Close the opened file: To close the currently opened HTML file, when you click Save, it will be saved as a new file.
• Press ALT+B/ALT+F4 to return to the MU App window.
Create Markdown
A tool to write Markdown codes easily. When you open it you will find the following items.
• Markdown: This is an edit box into which the results of the currently opened file are written/displayed.
◦ By pressing the Application key on the edit box, you can insert a link, paragraph, or heading.
• Open: to open and modify Markdown files.
• Save: to save the file.
• Close the opened file: To close the Markdown file that is currently open, and when you click Save, it will be saved as a new file.
• Press ALT+B/ALT+F4 to return to the MU App window.
extract links or "text"
A tool to extract links or text between quotation marks. When you open it you will find the following items.
• Edit box to paste/type text between quotation marks or that contains links.
• Get Result: To get the result.
◦ You can press the Tab key to see the result.
• Press ALT+B/ALT+F4 to return to the MU App window.
is over. We hope you will get the most out of the program.
Sincere regards and appreciation
Technology and News Team."""
		mesteranas= wx.Button(p, -1, "mester&anas")
		self.Bind(wx.EVT_BUTTON,self.onAnas,mesteranas)
		mohammedtechnology= wx.Button(p, -1, "&MohammedTechnology")
		self.Bind(wx.EVT_BUTTON,self.onMohammed,mohammedtechnology)
		technologyandnews= wx.Button(p, -1, "&technology and news")
		self.Bind(wx.EVT_BUTTON,self.onTan,technologyandnews)
		clos = wx.Button(p , -1, "&back")
		clos.Bind(wx.EVT_BUTTON, self.onback)
		self.Show()
	def onAnas(self, event):
		Anas= wx.Menu()
		telegram= Anas.Append(-1, "telegram")
		twitter= Anas.Append(-1, "twitter")
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/mesteranasm"), telegram)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://twitter.com/mesteranasm"), twitter)
		self.PopupMenu(Anas)
	def onMohammed(self, event):
		Mohammed= wx.Menu()
		telegram1= Mohammed.Append(-1, "telegram")
		twitter1= Mohammed.Append(-1, "twitter")
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/mohamedtechnology"), telegram1)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://twitter.com/mohamedtechnolo"), twitter1)
		self.PopupMenu(Mohammed)
	def onTan(self, event):
		Tan= wx.Menu()
		telegram2= Tan.Append(-1, "telegram")
		youtube= Tan.Append(-1, "youtube")
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/technologyandnewsanasmohammed"), telegram2)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://youtube.com/@technologyandnews"), youtube)
		self.PopupMenu(Tan)

	def onback(self, event):
		self.Close()













