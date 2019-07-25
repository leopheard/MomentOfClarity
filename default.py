# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/LeeCamp2
#------------------------------------------------------------
# Based on code from youtube addon
#------------------------------------------------------------
import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.momentofclarity'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID = "LeeCamp2"

# Entry point
def run():
    plugintools.log("momentofclarity.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("momentofclarity.main_list "+repr(params))
#note below - some YTs are /user/xxx and some /channel/xxx
    plugintools.add_item( 
        #action="", 
        title="Moment Of Clarity",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID+"/",
        thumbnail=icon,
        folder=True )

run()
