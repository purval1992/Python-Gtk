import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango, Gdk

software_list = [("Firefox", 2002,  "C++"),
                 ("Eclipse", 2004, "Java" ),
                 ("Pitivi", 2004, "Python"),
                 ("Netbeans", 1996, "Java"),
                 ("Chrome", 2008, "C++"),
                 ("Filezilla", 2001, "C++"),
                 ("Bazaar", 2005, "Python"),
                 ("Git", 2005, "C"),
                 ("Linux Kernel", 1991, "C"),
                 ("GCC", 1987, "C"),
                 ("Frostwire", 2004, "Java")]



class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Welcome to Enjay")
        self.set_border_width(4)
	

        self.show_tabs = True
        self.show_border = True
	
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
	self.notebook.set_size_request(600,500)
		
	self.page1 = Gtk.Box()
        #self.page1.set_border_width(30)

		

	self.notebook.append_page(self.page1, Gtk.Label('Editor'))
	

# page one multiline text box


	
	toolbar = Gtk.Toolbar()
        
        button_bold = Gtk.ToolButton()
        button_bold.set_icon_name("format-text-bold-symbolic")
        toolbar.insert(button_bold, 0)

        button_italic = Gtk.ToolButton()
        button_italic.set_icon_name("format-text-italic-symbolic")
        toolbar.insert(button_italic, 1)

        button_underline = Gtk.ToolButton()
        button_underline.set_icon_name("format-text-underline-symbolic")
        toolbar.insert(button_underline, 2)

  #      button_bold.connect("clicked", self.on_button_clicked, self.tag_bold)
  #      button_italic.connect("clicked", self.on_button_clicked,self.tag_italic)
  #      button_underline.connect("clicked", self.on_button_clicked,self.tag_underline)

        toolbar.insert(Gtk.SeparatorToolItem(), 3)
	
	radio_justifyleft = Gtk.RadioToolButton()
        radio_justifyleft.set_icon_name("format-justify-left-symbolic")
        toolbar.insert(radio_justifyleft, 4)

        radio_justifycenter = Gtk.RadioToolButton.new_from_widget(radio_justifyleft)
        radio_justifycenter.set_icon_name("format-justify-center-symbolic")
        toolbar.insert(radio_justifycenter, 5)

        radio_justifyright = Gtk.RadioToolButton.new_from_widget(radio_justifyleft)
        radio_justifyright.set_icon_name("format-justify-right-symbolic")
        toolbar.insert(radio_justifyright, 6)

        radio_justifyfill = Gtk.RadioToolButton.new_from_widget(radio_justifyleft)
        radio_justifyfill.set_icon_name("format-justify-fill-symbolic")
        toolbar.insert(radio_justifyfill, 7)

        radio_justifyleft.connect("toggled", self.on_justify_toggled,
            Gtk.Justification.LEFT)
        radio_justifycenter.connect("toggled", self.on_justify_toggled,
            Gtk.Justification.CENTER)
        radio_justifyright.connect("toggled", self.on_justify_toggled,
            Gtk.Justification.RIGHT)
        radio_justifyfill.connect("toggled", self.on_justify_toggled,
            Gtk.Justification.FILL)




	scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)

        self.textview = Gtk.TextView()
	
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text("This is some text inside of a Gtk.TextView. "
            + "Select text and click one of the buttons 'bold', 'italic', "
            + "or 'underline' to modify the text accordingly.")
        scrolledwindow.add(self.textview)
	
	
	table1= Gtk.Table(10,10,True)

	table1.attach(toolbar, 0, 10, 0, 1)
	table1.attach(scrolledwindow, 0, 10, 1, 8)
	
	#self.page1.add(Gtk.Button(label="ok"))
	#self.page1.add(Gtk.Button(label="Cancel"))


#bottom buttons

 	check_editable = Gtk.CheckButton("Editable")
        check_editable.set_active(True)
        check_editable.connect("toggled", self.on_editable_toggled)
        table1.attach(check_editable,0,2,8,9)

        check_cursor = Gtk.CheckButton("Cursor Visible")
        check_cursor.set_active(True)
        check_editable.connect("toggled", self.on_cursor_toggled)
        table1.attach(check_cursor,2,4,8,9)


	
	#wrapnone = Gtk.RadioButton.new_with_label_from_widget(None,
         #   "No Wrapping")
        #table1.attach(wrapone,4,5,8,10)
	
        #wrapchar = Gtk.RadioButton.new_with_label_from_widget(
        #    radio_wrapnone, "Character Wrapping")
        #table1.attach(wrapchar,5,6,8,10)

        #wrapword = Gtk.RadioButton.new_with_label_from_widget(
        #    radio_wrapnone, "Word Wrapping")
        #table1.attach(wrapword,6,7,8,10)

        #radio_wrapnone.connect("toggled", self.on_wrap_toggled,
         #   Gtk.WrapMode.NONE)
        #radio_wrapchar.connect("toggled", self.on_wrap_toggled,
         #   Gtk.WrapMode.CHAR)
        #radio_wrapword.connect("toggled", self.on_wrap_toggled,
        #    Gtk.WrapMode.WORD

        
	self.page1.add(table1)

#end

#page 2 add calender

	
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
  	self.notebook.append_page(self.page2, Gtk.Label('Calendar'))
	
	tablepage2 = Gtk.Table(10,10,True)

        calender = Gtk.Calendar()

        label = Gtk.Label("Display calendar")
        tablepage2.attach(label, 0, 5, 0, 1)
        tablepage2.attach(calender, 0, 4, 1, 4)
	

	frame = Gtk.Frame()
	frame.set_label("Signal Events Frame")
	
	tablefr = Gtk.Table(5,5,True)
	
	check1 = Gtk.CheckButton("Show heading")
	check2 = Gtk.CheckButton("Show Day Names")
	check3 = Gtk.CheckButton("Show Week numbers")
	check4 = Gtk.CheckButton("Show Calender")
	
	tablefr.attach(check1, 0, 1, 0, 1)
	tablefr.attach(check2, 0, 1, 1, 2)
	tablefr.attach(check3, 0, 1, 2, 3)

        #frame.add(tablefr)	
	#frame.add(check1)
	
	#tablepage2.attach(frame, 0, 5, 1, 4 )
	frame.add(tablefr)

	bottomframe = Gtk.Frame()
	bottomframe.set_label("other information")
	
	tablebottom = Gtk.Table()
	
	label8 = Gtk.Label("This program is free software;\n"
				+" you can redistribute it and/or \n"
				+" modify it under the terms of the GNU General Public\n ")
	label9 = Gtk.Label("gfjgdjs ff df djfb sfeurshkwer werki ehrkiher")
	label10 = Gtk.Label("sjdfsks ksdf hffkr ff kkhf shl hfkhkfh kdf df kghkdh yyh hf  frehf sf")
	label11 = Gtk.Label("uhd fdfks dfiur eff u ufs  jfjf kdfk kdflsof rforu ofds fdsfj sdhkr ishkfh")
	
	tablebottom.attach(label8,0,1,0,1)
	tablebottom.attach(label9,0,1,1,2)
	tablebottom.attach(label10, 0, 1, 2, 3)
	tablebottom.attach(label11, 0, 1, 3, 4)
	
	bottomframe.add(tablebottom)
	

	tablepage2.attach(bottomframe,0,8,5,9)

	self.page2.add(tablepage2)
	
#page 3

	self.page3 = Gtk.Box()
	#self.page3.set_border_width(20)	
	self.notebook.append_page(self.page3, Gtk.Label('File choose'))

	tablepage3 = Gtk.Table(10,10,True)

	

#start page4 here 

	self.page4 = Gtk.Box()
        self.page4.set_border_width(20)
        self.notebook.append_page(self.page4, Gtk.Label('New Page'))

	table = Gtk.Table(3,3, True)

	
	uname = Gtk.Label("User name")
	fname = Gtk.Label("First Name")
	lname = Gtk.Label("last name")
	
	uentry = Gtk.Entry()
	fentry = Gtk.Entry()
	lentry = Gtk.Entry()	

	table.attach(uname, 0, 1, 0, 1)
	table.attach(fname, 0, 1, 1, 2)
	table.attach(lname, 0 ,1, 1, 3)
	
	table.attach(uentry, 1, 2, 0, 1)
	table.attach(fentry, 1, 2, 1, 2)
	table.attach(lentry, 1, 2, 1, 3)
	
	#table.attach(buttontest, 0, 1, 0, 2 )
	#table.attach(buttontest2, 0, 2, 1, 3)
	
	self.page4.add(table)	

#    def new_tab(self):

	#self.set_default_size(200, 200)

        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["Fedora", "http://fedoraproject.org/"])
        self.liststore.append(["Slackware", "http://www.slackware.com/"])
        self.liststore.append(["Sidux", "http://sidux.com/"])

        treeview = Gtk.TreeView(model=self.liststore)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
        treeview.append_column(column_text)

        renderer_editabletext = Gtk.CellRendererText()
        renderer_editabletext.set_property("editable", True)

        column_editabletext = Gtk.TreeViewColumn("Editable Text",
            renderer_editabletext, text=1)
        treeview.append_column(column_editabletext)

        renderer_editabletext.connect("edited", self.text_edited)

 #add treeview in to tablepage3
	tablepage3.attach(treeview, 0, 9, 1, 6)
	

#file choose
	framechoose = Gtk.Frame()
	framechoose.set_label("Choose file from here")
		
	button1 = Gtk.Button("Choose File")
        button1.connect("clicked", self.on_file_clicked)
	button1.set_size_request(2, 2)
	button1.set_border_width(2)
#attach button to table page3
	
	tablepage3.attach(button1,0,2,6,7)
        

        button2 = Gtk.Button("Choose Folder")
        button2.connect("clicked", self.on_folder_clicked)
	button2.set_size_request(2,2)
	button2.set_border_width(2)

#attach button to tablepage3	
	tablepage3.attach(button2,2,4,6,7)
#add tablepage3 in to notebook page 3

	self.page3.add(tablepage3)

	#buttonx= Gtk.Button(label="hellooo")
	#grid = Gtk.Grid()
	#grid.attach(framechoose,0,9,7,8)
	#grid.attach_next_to(buttonx, framechoose, Gtk.PositionType.RIGHT,1,1)


#page 4

	self.page4 = Gtk.Box()
       # self.page4.set_border_width(20)        
        self.notebook.append_page(self.page4, Gtk.Label('settings'))
		
	table4 = Gtk.Table(5, 5, True)

	frame = Gtk.Frame()
        frame.set_label("Basic Options")
	
	tablechild = Gtk.Table(4,4,True)
	#grid = Gtk.Grid()
		
	label5 = Gtk.Label("Project category")
	label6 = Gtk.Label("Project file")
	label7 = Gtk.Label("Project category")

	entry5 = Gtk.Entry()
	entry6 = Gtk.Entry()
	entry7 = Gtk.Entry()

	

	tablechild.attach(label5,0,1,0,1)
	tablechild.attach(entry5,1,4,0,1)

	tablechild.attach(label6,0,1,1,2)
	tablechild.attach(entry6,1,4,1,2)

	tablechild.attach(label7,0,1,2,3)
	tablechild.attach(entry7,1,4,2,3)	
	
	table4.attach(frame, 0, 5, 0, 1)
	
	frame.add(tablechild)
#	table4.add(frame)

	frameside = Gtk.Frame()
	frameside.set_label("the other buttons")
	frameside.set_border_width(6)

	tableside = Gtk.Table()
	
	labelside = Gtk.Label("choose from Combobox")

	tableside.attach(labelside, 0,1,0,1)


#combo

	name_store = Gtk.ListStore(int, str)
        name_store.append([1, "Billy Bob"])
        name_store.append([11, "Billy Bob Junior"])
        name_store.append([12, "Sue Bob"])
        name_store.append([2, "Joey Jojo"])
        name_store.append([3, "Rob McRoberts"])
        name_store.append([31, "Xavier McRoberts"])

        name_combo = Gtk.ComboBox.new_with_model_and_entry(name_store)
#        name_combo.connect("changed", self.on_name_combo_changed)
        name_combo.set_entry_text_column(1)
  	tableside.attach(name_combo, 0,1,1,2)


#end combo



#end

#page 5

	self.page5 = Gtk.Box()
        self.page5.set_border_width(5)
        self.notebook.append_page(self.page5, Gtk.Label('Clipboard'))
	
	table5 = Gtk.Table(8,8,True)

	tablegrid = Gtk.Table(2, 2 ,True)

	framegrid = Gtk.Frame()
	framegrid.set_label("Grid")

	grid = Gtk.Grid()
	
	buttona = Gtk.Button("buttona")
	buttonb = Gtk.Button("buttonb")
	buttonc = Gtk.Button("buttonc")
	
	labela = Gtk.Label("labela")
	labelb = Gtk.Label("labelb")
	labelc = Gtk.Label("labelc")


	scrolledwin = Gtk.ScrolledWindow()
        grid.add(scrolledwin)
        
	textview = Gtk.TextView()
        grid.attach(textview,1,0,2,5)

	
	#grid.attach(buttona,2,3,4,5)
#	grid.attach_next_to(labelb,buttona,Gtk.PositionType.RIGHT,1)
#	framegrid.add(grid)
	tablegrid.attach(grid,0,1,0,1)
	self.page4.add(tablegrid)


#menu

	#menutable(1,6,True)
	#hbox=Gtk.Box(spacing=2)
#File menu

	accel_group = Gtk.AccelGroup()


	mb = Gtk.MenuBar()
 	filemenu = Gtk.Menu()
	filem = Gtk.MenuItem("File")
	
	filee = Gtk.MenuItem("Edit")
	filev = Gtk.MenuItem("Tabs")

  	filem.set_submenu(filemenu)
	new = Gtk.MenuItem("New")
	new.connect("activate",self.on_menu_clicked)
	
	open = Gtk.MenuItem("Open")
	#new.connect("activate",self.on_menu_clicked)
	
	save = Gtk.MenuItem("Save")
	#new.connect("activate",self.on_menu_clicked)

   	exit = Gtk.MenuItem("Exit")
   	exit.connect("activate", Gtk.main_quit)
	
	filemenu.append(new)
	filemenu.append(open)
	filemenu.append(save)
   	filemenu.append(exit)
  	mb.append(filem)


#Edit menu
	filemenu2 = Gtk.Menu()
	filee.set_submenu(filemenu2)
	copy = Gtk.MenuItem("Copy")
	paste = Gtk.MenuItem("Paste")
	filemenu2.append(copy)
	filemenu2.append(paste)	
	mb.append(filee)

#view menu
	filemenu3 = Gtk.Menu()
	filev.set_submenu(filemenu3)
	name = Gtk.MenuItem("Name Tab")
	prev = Gtk.MenuItem("Previous Tab")
	next = Gtk.MenuItem("Next Tab")
	ml = Gtk.MenuItem("Move to left")
	rotate = Gtk.MenuItem("Rotate")
	rotate.connect("activate",self.rotate_book,self.notebook)

	filemenu3.append(name)
	filemenu3.append(prev)
	filemenu3.append(next)
	filemenu3.append(ml)
	filemenu3.append(rotate)

	mb.append(filev)
	

	#hbox.pack_start(mb,True,True,0)
	#table5.attach(mb,0,1,0,1)
	
	#self.page5.add(table5)
	
	

#end menu

#clipbord area
	frameclip = Gtk.Frame()
	frameclip.set_label("Clipbord")
	table5.attach(frameclip,0,4,1,4)
	
 	tableclip = Gtk.Table(3, 2)

        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.entry = Gtk.Entry()
        self.image = Gtk.Image.new_from_icon_name("process-stop", Gtk.IconSize.MENU)
	
        button_copy_text = Gtk.Button("Copy Text")
        button_paste_text = Gtk.Button("Paste Text")
        button_copy_image = Gtk.Button("Copy Image")
        button_paste_image = Gtk.Button("Paste Image")

        tableclip.attach(self.entry, 0, 1, 0, 1)
        tableclip.attach(self.image, 0, 1, 1, 2)
        tableclip.attach(button_copy_text, 1, 2, 0, 1)
        tableclip.attach(button_paste_text, 2, 3, 0, 1)
        tableclip.attach(button_copy_image, 1, 2, 1, 2)
        tableclip.attach(button_paste_image, 2, 3, 1, 2)

        button_copy_text.connect("clicked", self.copy_text)
        button_paste_text.connect("clicked", self.paste_text)
        button_copy_image.connect("clicked", self.copy_image)
        button_paste_image.connect("clicked", self.paste_image)
	frameclip.add(tableclip)

  	


#end of cilpbord
	button = Gtk.Button("tab position")
        button.connect("clicked", self.rotate_book, self.notebook)
        #table.attach(button, 3,4,1,2)
        #button.show()

#        table5.attach(button, 7,8,7,8)
        self.page5.add(table5)
#end of page5

	
#start of page 6
 	self.page6 = Gtk.Box()
        self.page6.set_border_width(5)
        self.notebook.append_page(self.page6, Gtk.Label('new tab'))

	contact_table = Gtk.Table(5,5,True)
	
	framecontact= Gtk.Frame()
	framecontact.set_label("Add Contact")
	
			
	cid = Gtk.Label("Contact ID :")
	cid.set_justify(Gtk.Justification.LEFT)

	full = Gtk.Label("Full name:")
	first = Gtk.Label("First Name :")
	title = Gtk.Label("Title : ")
	middle = Gtk.Label("Middle Name :")
	last = Gtk.Label("Last Name :")
	
	cidentry = Gtk.Entry()
	fullentry = Gtk.Entry()
	firstentry = Gtk.Entry()
	titleentry = Gtk.Entry()
	midentry = Gtk.Entry()
	lastentry = Gtk.Entry()

	addbtn = Gtk.Button(stock=Gtk.STOCK_ADD)
	addbtn.connect("clicked",self.on_warn_clicked)
		
	deletebtn = Gtk.Button(label="Delete", stock=Gtk.STOCK_DELETE)
	
	firstbtn = Gtk.Button(label="First", stock=Gtk.STOCK_GOTO_FIRST)
	firstbtn.connect("clicked",self.on_error_clicked)

	backbtn = Gtk.Button(label="Back", stock=Gtk.STOCK_MEDIA_PREVIOUS)
	
	lastbtn = Gtk.Button(label="Last", stock=Gtk.STOCK_GOTO_LAST)
	lastbtn.connect("clicked",self.on_error_clicked)
	

	forwardbtn = Gtk.Button(label="forward",stock=Gtk.STOCK_MEDIA_FORWARD)
	#forwardbtn.set_use_stock(Gtk.STOCK_GOTO_FORWARD)
	
	childtbl = Gtk.Table(1,2,True)
	
	childtbl.attach(cid,0,1,0,1)
	childtbl.attach(cidentry,1,2,0,1)

	childtbl.attach(full,2,3,0,1)
	childtbl.attach(fullentry,3,4,0,1)
	
	framecontact.add(childtbl)
	
	contact_table.attach(framecontact,0,5,1,2)

	frameother = Gtk.Frame()
	frameother.set_label("Other Information")

	tableother = Gtk.Table(4,4,True)

	frameother.add(tableother)
	
	tableother.attach(first,0,1,0,1)
	tableother.attach(firstentry,1,2,0,1)
	tableother.attach(middle,0,1,1,2)
	tableother.attach(midentry,1,2,1,2)
	tableother.attach(last,0,1,2,3)
	tableother.attach(lastentry,1,2,2,3)
	
	tableother.attach(addbtn,0,1,3,4)
	tableother.attach(deletebtn,1,2,3,4)
	tableother.attach(firstbtn,2,3,1,2)
	tableother.attach(backbtn,3,4,1,2)
	tableother.attach(forwardbtn,2,3,2,3)
	tableother.attach(lastbtn,3,4,2,3)

	

	contact_table.attach(frameother,0,5,2,5)
	contact_table.attach(mb,0,1,0,1)	
	self.page6.add(contact_table)

#end of page 6

    def on_error_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,Gtk.ButtonsType.CANCEL, " ERROR ")
        dialog.format_secondary_text(
            "No Data Feached")
        dialog.run()
        print("ERROR dialog closed")
        dialog.destroy()

    def on_warn_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
            Gtk.ButtonsType.OK_CANCEL, "WARNING")
        dialog.format_secondary_text(
            "Enter Proper Data")
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("WARN dialog closed by clicking OK button")
        elif response == Gtk.ResponseType.CANCEL:
            print("WARN dialog closed by clicking CANCEL button")

        dialog.destroy()

    def on_menu_clicked(self,filemenu):
	print("you clicked on new")
	

    def rotate_book(self, button, notebook):
        notebook.set_tab_pos((notebook.get_tab_pos()+1) %4)



    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def on_folder_clicked(self, widget):

        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()


    def text_edited(self, widget, path, text):
        self.liststore[path][1] = text

    def on_justify_toggled(self, widget, justification):
        self.textview.set_justification(justification)

    def on_button_clicked(self, widget, tag):
        bounds = self.textbuffer.get_selection_bounds()
        if len(bounds) != 0:
            start, end = bounds
            self.textbuffer.apply_tag(tag, start, end)



    def on_editable_toggled(self, widget):
        self.textview.set_editable(widget.get_active())

    def on_cursor_toggled(self, widget):
        self.textview.set_cursor_visible(widget.get_active())

    def on_wrap_toggled(self, widget, mode):
        self.textview.set_wrap_mode(mode)


    def copy_text(self, widget):
        self.clipboard.set_text(self.entry.get_text(), -1)

    def paste_text(self, widget):
        text = self.clipboard.wait_for_text()
        if text != None:
            self.entry.set_text(text)
        else:
            print("No text on the clipboard.")

    def copy_image(self, widget):
        if self.image.get_storage_type() == Gtk.ImageType.PIXBUF:
            self.clipboard.set_image(self.image.get_pixbuf())
        else:
            print("No image has been pasted yet.")

    def paste_image(self, widget):
        image = self.clipboard.wait_for_image()
        if image != None:
            self.image.set_from_pixbuf(image)

#close

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
