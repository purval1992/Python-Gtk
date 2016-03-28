import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

	self.set_size_request(300,200)

	grid = Gtk.Grid()
	self.add(grid)

	label1 = Gtk.Label("only characters")
	self.entry1 = Gtk.Entry()

	self.entry1.set_max_length(8)
#	self.entry1.connect('changed',self.filter_numbers)
#	entry1.set_invisible_char(a)

	grid.add(label1)
	grid.attach_next_to(self.entry1,label1,Gtk.PositionType.RIGHT,1,1)
	
	label2 = Gtk.Label("only numbers")
	self.entry2 = Gtk.Entry()
	

	label3 = Gtk.Label("Enter Email address")
	self.entry3 = Gtk.Entry()

	grid.attach_next_to(label2,label1,Gtk.PositionType.BOTTOM,1,1)
	grid.attach_next_to(self.entry2,label2,Gtk.PositionType.RIGHT,1,1)	

	button1 = Gtk.Button(label="OK",stock=Gtk.STOCK_OK)
	button1.connect("clicked",self.on_button_clicked)

	button2 = Gtk.Button(label="Cancel",stock=Gtk.STOCK_CANCEL)
#	button2.connect("clicked",self.on_button_clicked)
   
	grid.attach_next_to(label3,label2,Gtk.PositionType.BOTTOM,1,1)
        grid.attach_next_to(self.entry3,label3,Gtk.PositionType.RIGHT,1,1)


	label4 = Gtk.Label("Enter IP address :")
	self.entry4 = Gtk.Entry()

	grid.attach_next_to(label4,label3,Gtk.PositionType.BOTTOM,1,1)
	grid.attach_next_to(self.entry4,label4,Gtk.PositionType.RIGHT,1,1)

 	grid.attach_next_to(button1,label4,Gtk.PositionType.BOTTOM,1,1)
        grid.attach_next_to(button2,button1,Gtk.PositionType.BOTTOM,1,1)

#validation of character entry
 
    def on_button_clicked(self, widget):
	text = self.entry2.get_text()
	if (text.isdigit() == False):
	
	    dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            	Gtk.ButtonsType.OK, "Message box")
            dialog.format_secondary_text("Enter only numbers")
            response = dialog.run() 
	    if response == Gtk.ResponseType.OK:
	        print("Try again")
	    else:
		print("ok")	
	    dialog.destroy()
	elif (text == "-") :
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, "Message box")
            dialog.format_secondary_text("Enter proper value")
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                print("Try again")
            else:
                print("ok")
            dialog.destroy()
	
#validation of Number entry
	
	text2 = self.entry1.get_text()
	
	if (text2.isalpha() == False):

            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, "Message box")
            dialog.format_secondary_text("Enter Only characters without space and numbers")
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                print("Try again")
            else:
                print("ok")
            dialog.destroy()
        else:

            print("correct value")

#validation of Email Id
	text3 = self.entry3.get_text()
	print text3
	suffix = ".com"
	if (text3.endswith(suffix) == False):
	    print("incorrect email address")
	    dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                Gtk.ButtonsType.OK, "Message box")
            dialog.format_secondary_text("Wrong mail ID format.it must be (eg.xxx@gmail.com)")
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                print("Try again")
            else:
                print("ok")
            dialog.destroy()

	else:
	    print("correct")


#ip validation
	p = self.entry4.get_text()
    #def ip_checkv4(p):
        parts=p.split(".")
        if len(parts)<4 or len(parts)>4:
	    print("Invalid IP address")
#            return "invalid IP length should be 4 not greater or less than 4"
        else:
            while len(parts)== 4:
                a=int(parts[0])
                b=int(parts[1])
                c=int(parts[2])
                d=int(parts[3])
                if a<= 0 or a == 127 :
		    print("invalid id")
                    #return "invalid IP address"
                elif d == 0:
	   	    print("host id  should not be 0 or less than zero ")
		    return
   #                 return "host id  should not be 0 or less than zero "
                elif a>=255:
		    print("should not be 255 or greater than 255 or less than 0 A")
		    return
  #                  return "should not be 255 or greater than 255 or less than 0 A"
                elif b>=255 or b<0:
  		    print("should not be 255 or greater than 255 or less than 0 B")
       #               return "should not be 255 or greater than 255 or less than 0 B"
                elif c>=255 or c<0:
		    print("should not be 255 or greater than 255 or less than 0 C")
 #                   return "should not be 255 or greater than 255 or less than 0 C"
                elif d>=255 or c<0:
		    print("should not be 255 or greater than 255 or less than 0 D")
  #                  return "should not be 255 or greater than 255 or less than 0 D"
                else:
		    print("Valid Ip addess"), p
                   # return "Valid IP address ", ip

	#p=raw_input("Enter IP address")
	#print ip_checkv4(p)
	print p

#end of validation

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
