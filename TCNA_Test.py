import pcbnew
import wx
import os


class TwoClickNetAssign(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "TCNA_TEST"
        self.category = ""
        self.description = ""
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "pelle.png")

    def init(self):
        self.add_action("TwoClickNetAssign", self.Run)
        self.Net = ""


    def Run(self):
        self.window = wx.GetActiveWindow()        
        #app =  wx.GetApp()
        #wx.MessageDialog(None, "Test", str(app), wx.OK | wx.ICON_INFORMATION).ShowModal()

        self.window.Bind(wx.EVT_CHAR_HOOK, self.onKey) 


    def onKey(self, event):
 
        keycode = event.GetKeyCode()
        if keycode  == wx.WXK_ESCAPE:
            self.window.Unbind(wx.EVT_CHAR_HOOK)


        # Press 'c' for storing net information
        elif chr(event.GetUnicodeKey()) == "C":
            itemCount = 0
            board = pcbnew.GetBoard()

            selection = [track for track in board.GetTracks() if track.IsSelected()]
            if len(selection) == 0:
                footprints = [fp for fp in board.GetFootprints()]
                for fp in footprints:
                    selected_pads = [pad for pad in fp.Pads() if pad.IsSelected()]
                    selection += selected_pads
            
            if len(selection) == 0:
                info = wx.MessageDialog(None, "Nothing selected.", "Error", wx.OK | wx.ICON_INFORMATION)
                info.ShowModal()

            item = selection[0]
            self.Net = item.GetNetname() 

        
        # Press 'v' to do stuff
        elif chr(event.GetUnicodeKey()) == "V":
            board = pcbnew.GetBoard()

            selection = [track for track in board.GetTracks() if track.IsSelected()]
            footprints = [fp for fp in board.GetFootprints()]
            for fp in footprints:
                selection += [pad for pad in fp.Pads() if pad.IsSelected()]

            for target in selection:
                target.SetNet(board.FindNet(self.Net))

            pcbnew.Refresh()

        #event.Skip()           

TwoClickNetAssign().register()
