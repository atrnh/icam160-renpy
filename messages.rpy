init python:
    import renpy.store as store
    
    reply_screen = False
    draft_screen = False

    class Mail(store.object):
        def __init__(self, subject, sender, body, reply_label=False, delay=False, view=True, read=False):
            self.subject = subject
            self.sender = sender
            self.body = body
            self.reply_label = reply_label
            self.delay = delay
            self.view = view
            self.read = read
            if delay:
                self.queued()
            else:            
                self.deliver()  
                
        def delete(self):
            self.view = False
            renpy.restart_interaction()
            
        def deliver(self):
            if self in mail_queue:
                mail_queue.remove(self)
            mail.insert(0, self)
            
        def mark_read(self):
            self.read = True 
            renpy.restart_interaction()         
            
        def queued(self):
            mail_queue.append(self)           
            
        def reply(self):
            global reply_screen
            reply_screen = True
            renpy.call_in_new_context(self.reply_label, current_message=self)                
            reply_screen = False            
            
        def restore(self):
            self.view = True  
            renpy.restart_interaction()            

    class Contact(store.object):
        def __init__(self, name, draft_label):
            self.name = name
            self.draft_label = draft_label  
            self.add_contact()
            
        def add_contact(self):
            contacts.append(self)

        def draft(self):
            global draft_screen
            draft_screen = True
            renpy.call_in_new_context(self.draft_label, contact=self)            
            draft_screen = False
            
        def delete(self):
            contacts.remove(self)

    def add_message(subject, sender, body, reply_label=False, delay=False):
        message = Mail(subject, sender, body, reply_label, delay)
        
    def check(subject):
        for item in mail:
            if item.subject == subject:
                if item.read:
                    return True
                else:
                    return False
                    
    def deliver_all(): 
        mail.extend(mail_queue)
        mail_queue = list()          
        
    def deliver_next():
        if mail_queue:
            mail_queue[0].deliver()

    def mark_all_read():
        unread_messages = [x for x in mail if not x.read]
        for x in unread_messages:
            x.mark_read()                

    def message_count():
        visible_messages = [x for x in mail if x.view]
        return len(visible_messages)
        
    def new_message_count():
        unread_messages = [ x for x in mail if not x.read]
        return len(unread_messages)
            
    def restore_all():
        deleted_messages = [x for x in mail if not x.view]
        for x in deleted_messages:
            x.restore()
        renpy.restart_interaction()

# screen mailbox_overlay:
#     hbox:
#         xalign 1.0 yalign 0.0
#         if new_message_count() > 0:
#             textbutton "Mailbox (%d New)" % (new_message_count()) action Show("mailbox")
#         else:
#             textbutton "Mailbox" action Show("mailbox")

# screen mailbox:
#     tag menu
#     modal True
#     default current_message = None
#     $ available_drafts = [i for i in contacts if i.draft_label]    
#     frame:
#         style_group "mailbox"
#         vbox:
#             label "Inbox"
#             if new_message_count() > 0:
#                 text ("Messages: %d (%d unread)") % (message_count(), new_message_count())
#             else:
#                 text ("Messages: %d") % message_count()
#             side "c r":
#                 area (0,0,800,93)
#                 viewport id "message_list":
#                     draggable True mousewheel True
#                     vbox:
#                         for i in mail:
#                             if i.view:
#                                 if not i.read:
#                                     textbutton ("*NEW* " + i.sender + " - " + i.subject) action [SetScreenVariable("current_message",i), i.mark_read] xfill True
#                                 else:
#                                     textbutton (i.sender + " - " + i.subject) action SetScreenVariable("current_message",i) xfill True
#                 vbar value YScrollValue("message_list")
#             hbox:
#                 null height 20
#             side "c r":
#                 area (0,0,800,380)
#                 viewport id "view_message":
#                     draggable True mousewheel True
#                     vbox:
#                         if current_message:
#                             text ("From: " + current_message.sender)
#                             text ("Subject: " + current_message.subject)
#                             text current_message.body
#                 vbar value YScrollValue("view_message")
#             use mailbox_commands

# screen mailbox_commands:
#     hbox:
#         if available_drafts:
#             textbutton "Draft New" action Show("contacts")
#         else:
#             textbutton "Draft New" action None
#         if current_message and current_message.reply_label:
#             textbutton "Reply" action current_message.reply
#         else:
#             textbutton "Reply" action None
#         if current_message:
#             textbutton "Delete" action [current_message.delete, SetScreenVariable("current_message", None)]
#         else:
#             textbutton "Delete" action None
#         if new_message_count() > 0:
#             textbutton "Mark All Read" action mark_all_read
#         else:
#             textbutton "Mark All Read" action None
#         textbutton "Restore All" action restore_all
#         textbutton "Exit" action Hide("mailbox")
        
screen contacts:
    modal True
    frame:
        style_group "mailbox"
        xsize 200
        vbox:
            label "Contacts"
            for name in contacts:
                if name.draft_label:
                    textbutton name.name action [name.draft, Hide("contacts")]
                else:
                    textbutton name.name action None
            textbutton "Close" action Hide("contacts")

# init -2 python:
#     style.mailbox = Style(style.default)
#     style.mailbox_vbox.xalign = 0.5
#     style.mailbox_vbox.xfill = True
#     style.mailbox_hbox.xalign = 0.5
#     style.mailbox_label_text.size = 30
#     style.mailbox_label_text.xalign = 0.5
#     style.mailbox_label.xfill = True
#     style.mailbox_frame.xalign = 0.5
#     style.mailbox_frame.yalign = 0.5
    
# updated choice screen    
# screen choice:

#     if reply_screen or draft_screen:
#         # this is the menu for message replies and drafts
#         frame:
#             style_group "mailbox"

#             vbox:
#                 label "Draft"
#                 if reply_screen:
#                     text ("To: " + current_message.sender)                
#                     text ("Subject: Re: " + current_message.subject)
#                 else:
#                     text ("To: " + contact.name)
#                     text ("Subject: " + message_title)
#                 null  height 30

#                 for caption, action, chosen in items:

#                     if action:
#                         button:
#                             action action
#                             style "menu_choice_button" xalign 0.5

#                             text caption text_align 0.5

#                     else:
#                         text caption style "menu_caption"
                        
#     else:
#         # this is the default choice menu
#         window:
#             style "menu_window"
#             xalign 0.5
#             yalign 0.5

#             vbox:
#                 style "menu"
#                 spacing 2

#                 for caption, action, chosen in items:

#                     if action:

#                         button:
#                             action action
#                             style "menu_choice_button"

#                             text caption style "menu_choice"

#                     else:
#                         text caption style "menu_caption"    
