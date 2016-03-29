import gi
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Pango
import time

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="New project")
	self.set_size_request(500,500)
	self.font = None
        self.font_dialog = None

        table = Gtk.Table(2,1, True)
	
	grid = Gtk.Grid()
	 	
        button1 = Gtk.Button(label="NEW",stock=Gtk.STOCK_NEW)
        button2 = Gtk.Button(label="ADD",stock=Gtk.STOCK_ADD)
        button3 = Gtk.Button(stock=Gtk.STOCK_CLEAR)
        button4 = Gtk.Button(stock=Gtk.STOCK_DIRECTORY)
        button5 = Gtk.Button(stock=Gtk.STOCK_EXECUTE)
        button6 = Gtk.Button(label="Button 6")


	grid.add(button1)
	grid.attach_next_to(button2,button1,Gtk.PositionType.RIGHT,1,1)
	grid.attach_next_to(button3,button2,Gtk.PositionType.RIGHT,1,1)
	grid.attach_next_to(button4,button3,Gtk.PositionType.RIGHT,1,1)
	grid.attach_next_to(button5,button4,Gtk.PositionType.RIGHT,1,1)  

	self.show_tabs = True
        self.show_border = True

        self.notebook = Gtk.Notebook()
        self.notebook.set_size_request(600,500)

#attach notebook to grid at the bottom of button1       
        grid.attach_next_to(self.notebook,button1,Gtk.PositionType.BOTTOM,5,6)

	table.attach(grid,0,1,0,1)
#notebook page 1

        self.page1 = Gtk.Box()
        self.notebook.append_page(self.page1, Gtk.Label('File info'))

	tablepage1 = Gtk.Table(1,2,True)
	framepage1 = Gtk.Frame()
	framepage1.set_label("List of directories")

	framepage1.set_size_request(50,50)
	
	treestore = Gtk.TreeStore(str)

        # we'll add some data now - 4 rows with 3 child rows each
        for parent in range(4):
            piter = treestore.append(None, ['parent %i' % parent])
            for child in range(3):
                treestore.append(piter, ['child %i of parent %i' %
                                              (child, parent)])

        # create the TreeView using treestore
        treeview = Gtk.TreeView(treestore)

        # create the TreeViewColumn to display the data
        tvcolumn = Gtk.TreeViewColumn('Column 0')

        # add tvcolumn to treeview
        treeview.append_column(tvcolumn)

        # create a CellRendererText to render the data
        cell = Gtk.CellRendererText()

        # add the cell to the tvcolumn and allow it to expand
        tvcolumn.pack_start(cell, True)

        # set the cell "text" attribute to column 0 - retrieve text
        # from that column in treestore
        tvcolumn.add_attribute(cell, 'text', 0)

        # make it searchable
        treeview.set_search_column(0)

        # Allow sorting on the column
        tvcolumn.set_sort_column_id(0)

        # Allow drag and drop reordering of rows
        treeview.set_reorderable(True)
	
	framepage1.add(treeview)

	tablepage1.attach(framepage1,0,1,0,1)

	
	#fixed = Gtk.Fixed()
	#fixed.put(button2 , 10, 10)
	#fixed.move(button2,20,20)
	#fixed.put(button3 , 20 , 30)
	#tablepage1.attach(fixed ,1,2,0,1)
	self.page1.add(tablepage1)


#notebook page2
 	self.page2 = Gtk.Box()
	
	tablepage2 = Gtk.Table(2,2,True)
	
	calendar = Gtk.Calendar()
	
        
	tablepage2.attach(calendar,0,1,0,1)	
#frame for flag

	frame2 = Gtk.Frame()
	frame2.set_label("Flags")
#add check box in frame2  named flag
	
	checkbtn1 = Gtk.CheckButton("Show Headings")
	checkbtn2 = Gtk.CheckButton("Show Day By Names")
	checkbtn3 = Gtk.CheckButton("No Month Change")
	checkbtn4 = Gtk.CheckButton("Show week Numbers")
#add grid in to frame2 to add checkboxes

	grid1 = Gtk.Grid()

	grid1.add(checkbtn1)
	grid1.attach_next_to(checkbtn2,checkbtn1,Gtk.PositionType.BOTTOM,1,2)
	grid1.attach_next_to(checkbtn3,checkbtn2,Gtk.PositionType.BOTTOM,1,2)
	grid1.attach_next_to(checkbtn4,checkbtn3,Gtk.PositionType.BOTTOM,1,2)

#add grid1 in to frame2
	frame2.add(grid1)
	

	tablepage2.attach(frame2,1,2,0,1)
	
	
		
	# creating a new Grid for page2 
	
	tablesnd = Gtk.Table(3,1,True)
	
	framesnd = Gtk.Frame()
	framesnd.set_label("Signal events")
	
	tablesnd.attach(framesnd,0,1,0,1)

	tablepage2.attach(tablesnd,0,2,1,3)
        label = Gtk.Label("Signal:")
   	
        last_sig = Gtk.Label("")
   
        self.notebook.append_page(self.page2, Gtk.Label('calender'))

	self.page2.add(tablepage2)

#notebook page3
	self.page3 = Gtk.Box()

	tablepage3 = Gtk.Table(1,1,True)
	gridfile = Gtk.Grid()

#file choose and folder choose button
	
	filebtn = Gtk.Button(label="File choose")
	filebtn.connect("clicked",self.on_file_clicked)
	
	folderbtn = Gtk.Button(label="Folder Choose")
	folderbtn.connect("clicked",self.on_folder_clicked)
	

	labelfolder = Gtk.Label("Folder Path is : ")
	self.entryfolder = Gtk.Entry()
	self.entryfolder.set_editable(False)
	
	labelfile = Gtk.Label("File path is :")
	self.entryfile = Gtk.Entry()
	self.entryfile.set_editable(False)
	
	
	gridfile.add(filebtn)
	gridfile.attach_next_to(folderbtn,filebtn,Gtk.PositionType.RIGHT,1,1)
	gridfile.attach_next_to(labelfolder,filebtn , Gtk.PositionType.BOTTOM,1,1)
	gridfile.attach_next_to(self.entryfolder,labelfolder , Gtk.PositionType.RIGHT,1,1)
	gridfile.attach_next_to(labelfile,labelfolder,Gtk.PositionType.BOTTOM,1,1)
	gridfile.attach_next_to(self.entryfile,labelfile,Gtk.PositionType.RIGHT,1,1)
	#scrolled window
	scrolledwindow = Gtk.ScrolledWindow()
	scrolledwindow.set_size_request(20,20)
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)

        self.textview = Gtk.TextView()

        self.textbuffer = self.textview.get_buffer()
        scrolledwindow.add(self.textview)
	
	tablescroll = Gtk.Table()
	
	#tablescroll.attach(scrolledwindow,0,1,0,1)
        tablepage3.attach(tablescroll,0,1,1,2)


		
	tablepage3.attach(gridfile,0,1,0,1)


        self.notebook.append_page(self.page3, Gtk.Label('View File'))
	self.page3.add(tablepage3)

#page 4
	self.page4 = Gtk.Box()

#save file of text box
	tablepage4 = Gtk.Table(1,1,True)
	gridpage4 = Gtk.Grid()

	toolbar = Gtk.Toolbar()
        open_btn = Gtk.ToolButton.new_from_stock(Gtk.STOCK_OPEN)
        open_btn.connect("clicked", self.on_open_clicked)
        toolbar.insert(open_btn, 0)
        
	save_btn = Gtk.ToolButton.new_from_stock(Gtk.STOCK_SAVE)
        save_btn.connect("clicked", self.on_save_clicked)
        toolbar.insert(save_btn, 1)

	clear_btn = Gtk.ToolButton.new_from_stock(Gtk.STOCK_CLEAR)
	clear_btn.connect("clicked",self.on_clear_clicked)
	toolbar.insert(clear_btn,2)

	


	gridpage4.add(toolbar)

       # self.box.pack_start(toolbar, False, True, 0)

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        scrolledwindow.add(self.textview)
	gridpage4.attach_next_to(scrolledwindow,toolbar,Gtk.PositionType.BOTTOM,1,1)

	tablepage4.attach(gridpage4,0,1,0,1)
	self.page4.add(tablepage4)
        
#self.box.pack_start(scrolledwindow, True, True, 0)

#end here

        self.notebook.append_page(self.page4,Gtk.Label('Open/Save file'))


#page 5
	self.page5 = Gtk.Box()


	tablepage5 = Gtk.Table(1,1,True)
	grid1 = Gtk.Grid()
	
	menubar = Gtk.MenuBar()

        menu_file = Gtk.Menu()
        menu_edit = Gtk.Menu()
        menu_help = Gtk.Menu()

        item_open = Gtk.MenuItem("Open")
        item_save = Gtk.MenuItem("Save")
        item_quit = Gtk.MenuItem("Quit")


	one = Gtk.MenuItem("one")
	two = Gtk.MenuItem("Two")
	three = Gtk.MenuItem("Three")

	
        menu_file.append(item_open)
        menu_file.append(item_save)
        menu_file.append(item_quit)

        item_cut = Gtk.MenuItem("Cut")
        item_copy = Gtk.MenuItem("Copy")
        item_paste = Gtk.MenuItem("Paste")
        menu_edit.append(item_cut)
        menu_edit.append(item_copy)
        menu_edit.append(item_paste)
        
	item_about = Gtk.MenuItem("About")
        menu_help.append(item_about)

        item_file = Gtk.MenuItem("File")
        item_edit = Gtk.MenuItem("Edit")
        item_help = Gtk.MenuItem("Help")

        item_file.set_submenu(menu_file)
        item_edit.set_submenu(menu_edit)
        item_help.set_submenu(menu_help)
	menubar.append(item_file)
        menubar.append(item_edit)
        menubar.append(item_help)

	#item_help.set_right_justified(right_justified)

	grid1.add(menubar)
	
	#searchbar = Gtk.SearchBar()
	#grid1.attach_next_to(searchbar,menubar,Gtk.PositionType.RIGHT,1,1)

	tablepage5.attach(grid1,0,1,0,1)

	framepage5 = Gtk.Frame()
	framepage5.set_label("Add New User")

	tablepage5.attach(framepage5,0,1,1,5)
	
	gridpage5 = Gtk.Grid()
	
	labeln = Gtk.Label("First Name :")
	labell = Gtk.Label("Last Name :")
	labelf = Gtk.Label("Full Name :")
	labelc = Gtk.Label("Contact No :")
#text fields
	entryn = Gtk.Entry()
	
	entryl = Gtk.Entry()

	entryf = Gtk.Entry()

#number field
	entry = Gtk.Entry()
	#entry.connect("activate",self.entry_activate)
	#entry.connect("focus_out_event",self.entry_focus_out)
	#handlerid = entry.connect("insert-text",self.entry_insert_text)
	#entry.set_data('handlerid',handlerid)	

	#entryc.connect("changed",self.on_changed)

	gridpage5.add(labeln)
	gridpage5.attach_next_to(entryn,labeln,Gtk.PositionType.RIGHT,1,1)
	gridpage5.attach_next_to(labell,labeln,Gtk.PositionType.BOTTOM,1,1)
        gridpage5.attach_next_to(entryl,labell,Gtk.PositionType.RIGHT,1,1)
        gridpage5.attach_next_to(labelf,labell,Gtk.PositionType.BOTTOM,1,1)
        gridpage5.attach_next_to(entryf,labelf,Gtk.PositionType.RIGHT,1,1)
	gridpage5.attach_next_to(labelc,labelf,Gtk.PositionType.BOTTOM,1,1)
	gridpage5.attach_next_to(entry,labelc,Gtk.PositionType.RIGHT,1,1)
    
	
	buttonok = Gtk.Button(stock=Gtk.STOCK_OK)
	buttoncancel= Gtk.Button(stock=Gtk.STOCK_CANCEL)
	
	gridpage5.attach_next_to(buttonok, labelc , Gtk.PositionType.BOTTOM,1,1)
	gridpage5.attach_next_to(buttoncancel, buttonok , Gtk.PositionType.BOTTOM,1,1)

	framepage5.add(gridpage5)
	
	



		
	self.notebook.append_page(self.page5, Gtk.Label('Validation'))
	self.page5.add(tablepage5)


#end of page 5

#page 6


	self.page6 = Gtk.Box()
	self.notebook.append_page(self.page6,Gtk.Label('settings'))

	
        grid6 = Gtk.Grid()
       

        

       	self.page6.add(grid6)

#end of page6



#Add buttons under notebook

        button5 = Gtk.Button(stock=Gtk.STOCK_FIND)
        grid.attach_next_to(button5,self.notebook,Gtk.PositionType.BOTTOM,1,1)
        self.add(table)

        rotate = Gtk.Button(label="Rotate")
        rotate.connect("clicked",self.rotate_book)
        grid.attach_next_to(rotate,button5,Gtk.PositionType.RIGHT,1,1)

        
    def on_open_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            selected_file = dialog.get_filename()
            with open(selected_file, 'r') as f:
                data = f.read()
                self.textbuffer.set_text(data)
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()

        dialog.destroy()


    def on_save_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Save file", self,
        Gtk.FileChooserAction.SAVE,
        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
         Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            save_file = dialog.get_filename()
            start_iter = self.textbuffer.get_start_iter()
            end_iter = self.textbuffer.get_end_iter()
            text = self.textbuffer.get_text(start_iter, end_iter, True)   
            with open(save_file, 'w') as f:
                f.write(text)
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()

        dialog.destroy()

    def on_clear_clicked(self, widget):
	start = self.textbuffer.get_start_iter()
	end = self.textbuffer.get_end_iter()
	self.textbuffer.remove_all_tags(start,end)



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
	    self.entryfile.set_text(dialog.get_filename())
	    
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
	    self.entryfolder.set_text(dialog.get_filename())	    
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()


    def rotate_book(self, rotate, notebook):
        notebook.set_tab_pos((notebook.get_tab_pos()+1) %4)

	
    def on_button_clicked(self, widget):
        print("Hello World")




win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
