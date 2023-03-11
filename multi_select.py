import pcbnew
import os
import sys
import wx


class MultiSelect(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Multi Select"
        self.category = ""
        self.description = ""
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "pelle.png")

    def init(self):
        self.add_action("Multi Select", self.Run)

    def Run(self):
        self.window = wx.GetActiveWindow()        
        self.window.Bind(wx.EVT_CHAR_HOOK, self.onKey)
        

    def onKey(self, event):
        keycode = event.GetKeyCode()
        if chr(event.GetUnicodeKey()) == "S":
            board = pcbnew.GetBoard()

            board_items = [track for track in board.GetTracks()]
            footprints = [fp for fp in board.GetFootprints()]
            for fp in footprints:
                board_items += [pad for pad in fp.Pads()]

            selected_items = [item for item in board_items if item.IsSelected()]
            if len(selected_items) == 0:
                info = wx.MessageDialog(None, "Nothing selected.", "Error", wx.OK | wx.ICON_INFORMATION)
                info.ShowModal()
                return

            selected_item = selected_items[0]

            bbox = selected_item.GetBoundingBox()
            #items_in_layer = [item for item in board_items if item.]
            layer = selected_item.GetLayerSet().ExtractLayer()
            layer_items = [item for item in board_items if item.GetLayerSet().ExtractLayer() == layer]
            sys.stderr.write(f"Layer: {selected_item.GetLayerSet().ExtractLayer()}\n")
            count = 0
            for item in layer_items:
                if bbox.Intersects(item.GetBoundingBox()):
                    item.SetSelected()
                    count += 1
                    sys.stderr.write(f"{item.GetClass()} {item.GetLayerSet().ExtractLayer()}\n")
            
            sys.stderr.write(f"{count}\n")
            pcbnew.Refresh()    


MultiSelect().register()
