# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
#e((hPzLvrLftNJmkTh%s

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'Animoe': [{'name': 'preview',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/4/64447.jpg',
                       'video': 'http://2.bp.blogspot.com/0uCoi5JSupOqZ_AFtp-Ng4ufXpyOXGbVjMxSbZzJRkLtrPiFyp6EXVc_yFh5Tlq9s1rjW7_SqsjXEmD83Q8aquf3rYw-Vw8=m22',
                       'genre': 'gay'},
					 {'name': 'episode 1',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/4/64447.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=9702c6470437f931&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-ab5l6nzl&ms=nxu&mv=m&pl=48&mime=video/mp4&lmt=1481944189535930&mt=1487954848&ip=2604:a880:800:a1::796:9001&ipbits=0&expire=1487969365&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=03A8CBDC4CCEA989A13FC9EC2195B68D2A1B4CC7.3D25CBBA54FE26725D6995ED81BFCD8A78157B5C&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'gay'},
					 {'name': 'episode 2',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/4/64447.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=64282dd317e8fb6c&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-ab5l6nly&ms=nxu&mv=m&pl=48&mime=video/mp4&lmt=1468808553815108&mt=1487954848&ip=2604:a880:800:a1::796:9001&ipbits=0&expire=1487969341&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=473690D06795AC45E90FFC85AC7EFF28100326AC.998B9B4BBC01BACB6FDF6D2E6C7D1872E4967585&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'gay'},
					 {'name': 'episode 3',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/4/64447.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=50be0eaa0584556e&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-ab5l6n6l&ms=nxu&mv=m&pl=48&mime=video/mp4&lmt=1481948681042063&mt=1487954247&ip=2604:a880:800:a1::796:9001&ipbits=0&expire=1487968714&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=9C65EBE082B87612FC0881436FB69A524AE112C9.18B115E6C99644F842E01D760476F39BF6C3300F&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'gay'},
					 {'name': 'episode 4',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/4/64447.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=671f35930fa6f043&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-ab5l6n67&ms=nxu&mv=m&pl=48&mime=video/mp4&lmt=1468807695695507&mt=1487954614&ip=2604:a880:800:a1::796:9001&ipbits=0&expire=1487969120&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=8D47C4BB7AAB2F084BBDBA0E9CE4A2FED3FFCC98.07737DB3081F2602DABD31E297B25D1AAABC3BFB&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'gay'},
					 {'name': 'episode 5',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/4/64447.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=bf7679f55142f597&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-ab5l6n6s&ms=nxu&mv=m&pl=48&mime=video/mp4&lmt=1468800798897011&mt=1487954553&ip=2604:a880:800:a1::796:9001&ipbits=0&expire=1487969057&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=6A4EAE93098718527EA615E58423A463B925AC4A.092501B83313335B3CF950704EC8920E74216D70&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'gay'}
					   ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: list
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': category, 'genre': category})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        list_item.setInfo('video', {'title': video['name'], 'genre': video['genre']})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/vids/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
