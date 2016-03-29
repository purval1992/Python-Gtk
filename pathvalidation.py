import gi
import os
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Path validation")
	
	self.set_size_request(300,500)
	grid = Gtk.Grid()
	self.add(grid)

	label1 = Gtk.Label("Ener Path name:")
	self.entry1 = Gtk.Entry()
	
	label2 = Gtk.Label("remove directory :")
	self.entry2 = Gtk.Entry()


	button1 = Gtk.Button(label="mkdir")
	button1.connect("clicked",self.on_mkdir_clicked)
	
	
	button2 = Gtk.Button(label="rmdir")
	button2.connect("clicked",self.on_rmdir_clicked)

	grid.add(label1)
	grid.attach_next_to(self.entry1,label1,Gtk.PositionType.RIGHT,1,1)
	grid.attach_next_to(label2,label1,Gtk.PositionType.BOTTOM,1,1)

	
	grid.attach_next_to(self.entry2,label2,Gtk.PositionType.RIGHT,1,1)
	grid.attach_next_to(button1,label2,Gtk.PositionType.BOTTOM,1,1)
	grid.attach_next_to(button2,button1,Gtk.PositionType.RIGHT,1,1)

	self.entry3 = Gtk.Entry()
	grid.attach_next_to(self.entry3,button1,Gtk.PositionType.BOTTOM,1,1)

	button3 = Gtk.Button(label= "commands")
	grid.attach_next_to(button3,self.entry3,Gtk.PositionType.BOTTOM,1,1)	
	button3.connect("clicked",self.on_command_clicked)

	scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        scrolledwindow.add(self.textview)

	grid.attach_next_to(scrolledwindow,button3,Gtk.PositionType.BOTTOM,4,4)

	currency_combo = Gtk.ComboBoxText()


    def on_command_clicked(self,widget):
	
	filepath = self.entry3.get_text()
	print filepath
	if os.path.isabs(filepath):
            print("valid path")
       # else:
        #    print("invalid path")


#open file which you are serching in to entry widget
	    f = open(filepath, 'r')
            fr = f.read()
            f.close()            
	    self.textbuffer.set_text(fr)
	
	else:
	    dialog1 = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,Gtk.ButtonsType.CANCEL, "ERROR")
            dialog1.format_secondary_text("Invalid Path..Try Again!!!")
            dialog1.run()
            dialog1.destroy()


    def on_mkdir_clicked(self,widget):
        path1=self.entry1.get_text()
	if os.path.isabs(path1):
	    print("valid path")
	else:
	    print("invalid path")
	

	if not os.path.exists(path1):   
	    os.mkdir(path1)
	    print path1
	else:
	    dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,Gtk.ButtonsType.CANCEL, "ERROR")
            dialog.format_secondary_text("File Already Exist,Or Invalid Path Name")
            dialog.run()
            dialog.destroy()
#	    print("Directory exist")
	
	


    def on_rmdir_clicked(self,widget):
	remove = self.entry2.get_text()
	print remove

	if os.path.exists(remove):
            os.rmdir(remove)
        else:
            dialog1 = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,Gtk.ButtonsType.CANCEL, "ERROR")
            dialog1.format_secondary_text("File Not Exist..Try Again!!!")
            dialog1.run()
            dialog1.destroy()


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

