# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

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
VIDEOS = {'Studio Ghibli': [{'name': 'Spireted Away',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/6/79597.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=803a48f8a7eea9f6&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n76&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1481956587637995&mt=1487859294&ip=149.56.134.248&ipbits=0&expire=1487873828&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=53CE3B9E2B15CB71FDBD8067CB8246326E868BC2.5C4177453838296FD9E77489A70B8067747FDDC2&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
                      {'name': 'My Neighbor Totoro',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/4/75923.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=fc55004bf8ab9c2e&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-vgqs7nlz&ms=nxu&mv=m&pl=25&mime=video/mp4&lmt=1482047943509616&mt=1487860468&ip=149.56.134.248&ipbits=0&expire=1487874955&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=2D3A30A09203708AC16020F7FDB803A8FAF8E099.6A199FE7F3B8E43578B654E9B38BDE3E5E5B2175&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
                      {'name': 'Princess Mononoke',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/7/75919.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=01eaf7be23390634&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7e&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1481957668002614&mt=1487864575&ip=149.56.134.248&ipbits=0&expire=1487879163&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=B515DCC39244E094B6E8443E9A1037ABF71159AE.949C457F99CAF42350BBBDAE3A6F1648ACB089FD&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					  {'name': 'Howls Moving Castle',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/5/75810.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=adabb8050c118ed1&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7d&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1481956677672171&mt=1487860833&ip=149.56.134.248&ipbits=0&expire=1487875307&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=3756E2ADF5AE7B756F41F1920FC60DDD28A23FEC.21EB37382F611A377827421D8C6D547CDC425040&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					  {'name': 'Kikis Delivery Service',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/10/75916.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=de46ca6b82953625&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7e&ms=nxu&mv=m&pl=25&mime=video/mp4&lmt=1481952312993738&mt=1487863587&ip=149.56.134.248&ipbits=0&expire=1487878081&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=AA325D3F30FCDE81B085506613A56C266C279459.01A1FBA8DBBDCA3E98B23A29045E3F41DA9AC641&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					  {'name': 'Grave of the Fireflies',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/7/75808.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=afbd068dceb7db9d&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n76&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1469339277460890&mt=1487860431&ip=149.56.134.248&ipbits=0&expire=1487874996&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=6FC4C8645DAA196E7F69978F4D481CFF20C69EF0.B801C54EB2E655A101CC41F12C53CAD60D152861&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					  {'name': 'Castle in the Sky',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/5/37799.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=408c5c4ffe182fe1&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7z&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1481958833514958&mt=1487865852&ip=149.56.134.248&ipbits=0&expire=1487880328&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=86AC835E1549A2FD73B5FEDDAB9162C44F655B4B.B466319AA0B5FE1084D4057FBB6DCFDFE9B44B3F&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'Ponyo',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/7/8970.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=1282fcd8eea58aa4&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7s&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1481960676948022&mt=1487864384&ip=149.56.134.248&ipbits=0&expire=1487878896&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=9DB5AE0BE165865B26317C2F3995E7A830352E27.832601FC749293D4D932280D154D45068497E9B7&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'Porco Rosso',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/6/2878.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=4d9c9a4db193183f&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n76&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1469984213457672&mt=1487867788&ip=149.56.134.248&ipbits=0&expire=1487882369&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=74C71418DA8417AB7623672B4F16A51BE4C9251E.507B98B4701FB6A9C922C1A19D965D63A069BCBD&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'The Secret World of Arrietty',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/9/75905.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=c41a161d2deb02ca&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7s&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1481958933782067&mt=1487861319&ip=149.56.134.248&ipbits=0&expire=1487875961&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=163AD66D780C7C270A153B2585B07B8C70771B5C.5AF73E5DF2401AC7883D1A3C4DF0E28A736759CC&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'The Wind Rises',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/8/52353.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=783ecd2d30b3555c&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n76&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1482777862206004&mt=1487862287&ip=149.56.134.248&ipbits=0&expire=1487877141&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=5F1582CD0CD025E97296C67B86B21C76BB10FBEE.3F5C732FA556613865D161DFE55A0510C6CCB5DE&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'Whisper of the Heart',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/8/75921.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=97262d5f113a459b&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7z&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1481946814633258&mt=1487864201&ip=149.56.134.248&ipbits=0&expire=1487878727&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=3098BB38FBEF9DB35CF24A9FE7622462DBD17430.091D9ECC5C7875EF39272C28CCF410D8976C56A8&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'Only Yesterday',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/9/75922.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=457c329ef82017db&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7s&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1481960071151233&mt=1487867161&ip=149.56.134.248&ipbits=0&expire=1487881727&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=A06AADDAD6ACA7E0A1CE76A67F7EF6D522E31D49.AA751D51BF7A73833E08B80F69B55969F2A17AE6&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'The Cat Returns',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/1/597.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=c18ea98dc2f2275d&itag=59&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7l&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1481944674005013&mt=1487863837&ip=149.56.134.248&ipbits=0&expire=1487878365&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=126294CA1BFC59B63F06F5A5426D053E55995BA8.7847EF1AD1D21300E2C2A7CF3019667FC5CA42B9&key=ck2&app=explorer&fmt_list=59/854x480/9/0/115&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'Kokuriko-zaka Kara',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/8/32547.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=c0846a58f1655887&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-vgqsrnel&ms=nxu&mv=m&pl=25&mime=video/mp4&lmt=1481945969647376&mt=1487863109&ip=149.56.134.248&ipbits=0&expire=1487877671&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=8475CAEAB67379633BB8B5087FADB1E77CABA841.886762FFCF9D00B9AC9BB2C0E06DA6FDF069A4FF&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'Tales From Earthsea',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/5/73443.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=127c830d44ad5654&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7z&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1481958540258247&mt=1487861319&ip=149.56.134.248&ipbits=0&expire=1487875947&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=441B4AED62E7D2D072D311BAEAA592AA71E639FA.25A57F54A991171CA111F446855A6FF7ED0C0B4D&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'Pom Poko',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/11/75925.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=7dec12f1aef40e58&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7e&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1481957858849866&mt=1487868214&ip=149.56.134.248&ipbits=0&expire=1487882925&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=9D6651A5CE03AC82AA2BEA1C1B19D9AE11A9CA32.B70223AED27B4A9D0F820A614B62E17639E86BE0&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'The Tale of the Princess Kaguya',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/5/65925.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=b94870e45bc5c807&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7z&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1470818584116499&mt=1487867587&ip=149.56.134.248&ipbits=0&expire=1487882123&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=22B97DB633E21994469A07D0DC81E31953E82486.653A75EE554F20CA192045ACC2D149928799BAF4&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'When Marnie Was There',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/7/64293.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=419423914b4e4afa&itag=37&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qlsnz6&ms=nxu&mv=m&pl=25&mime=video/mp4&lmt=1481950327937805&mt=1487862152&ip=149.56.134.248&ipbits=0&expire=1487876659&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=56AB61EB6EE8422B94123324ED49DCC9DB44BEC3.2EA5E302AD67A452CBEC8DA92425BB7606FF7342&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'My Neighbors the Yamadas',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/7/75926.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=f1d66d7c3faf708a&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n76&ms=nxu&mv=m&pl=25&mime=video/mp4&lmt=1468897682886424&mt=1487862687&ip=149.56.134.248&ipbits=0&expire=1487877174&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=332AE9BA123D0CC6B01361A70F02F0AC7F29C417.B119153963B703D6CC82A328F5CFC1CC2FBE4FF7&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'I Can Hear the Sea',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/5/52359.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=43a7e487c2b378a7&itag=59&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7z&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1481945052690670&mt=1487867161&ip=149.56.134.248&ipbits=0&expire=1487881637&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=82EE10898F47120937676F035EBF13A2D511F74E.8D7D4F792F97F331E3D0EB4E82731B33D69C42CB&key=ck2&app=explorer&fmt_list=59/854x480/9/0/115&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'Taneyamagahara no yoru',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/8/3739.jpg',
                       'video': 'http://2.bp.blogspot.com/vv6anUw0U43jB5i5haJ8MiXIkW1zQ02XpQvcvgNQopVvxTG6FeZjkf2uAmiltswrMiAwuxtOj4mnoQJCBAhpmW268brzrl8=m22',
                       'genre': 'Studio Ghibli'},
					   {'name': 'On Your Mark',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/10/81234.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=c2a02fabbd3e5583&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7d&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1481941075017447&mt=1487868707&ip=149.56.134.248&ipbits=0&expire=1487883327&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=46EB8E956BC2964A39AE3F39F0550F21CBFB980E.98B309C8E309355E8AFBD4F743D1A9AFC2EB31EE&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'Ghost in the Shell 2: Innocence',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/10/75628.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=3236f746254e6b15&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-vgqs7nlr&ms=nxu&mv=m&pl=25&mime=video/mp4&lmt=1481957798505581&mt=1487862447&ip=149.56.134.248&ipbits=0&expire=1487876982&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=24DCA6B2FFB392B3A7DBB321D171BEBBEFEC7344.7400545B9FE098245221127F1F5372D56315DA87&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'Panda Kopanda',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/6/32957.jpg',
                       'video': 'https://redirector.googlevideo.com/videoplayback?id=2b111fda71cf1f4f&itag=22&source=webdrive&requiressl=yes&ttl=transient&mm=30&mn=sn-p5qs7n7e&ms=nxu&mv=u&pl=25&mime=video/mp4&lmt=1486463326973808&mt=1487864575&ip=149.56.134.248&ipbits=0&expire=1487879169&sparams=ip,ipbits,expire,id,itag,source,requiressl,ttl,mm,mn,ms,mv,pl,mime,lmt&signature=9917FBE17A035E361A0FAB009C94C4FA584CA621.ADA87A7AAB9724E2DC6CE20092275F2E2F4E74D7&key=ck2&app=explorer&kparams=MzEuMjAxLjE5Ni4xMDA=&upx=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU2LjAuMjkyNC44NyBTYWZhcmkvNTM3LjM2&tr=2',
                       'genre': 'Studio Ghibli'},
					   {'name': 'Iblard Jikan',
                       'thumb': 'https://myanimelist.cdn-dena.com/images/anime/2/18420.jpg',
                       'video': 'http://2.bp.blogspot.com/yhYF8Oqt-Rc7i0NuPSE42A3_NSze29wz89m4g8RGujLjeaR5cqCbylvAq8QVN8jF9tJPi6cwVTAC_hXh-8CZzVzm5YV-Nro78Q=m22',
                       'genre': 'Studio Ghibli'}
                      ],
            'Cars': [{'name': 'Postal Truck',
                      'thumb': 'http://www.vidsplay.com/vids/us_postal.jpg',
                      'video': 'http://www.vidsplay.com/vids/us_postal.mp4',
                      'genre': 'Cars'},
                     {'name': 'Traffic',
                      'thumb': 'http://www.vidsplay.com/vids/traffic1.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic1.avi',
                      'genre': 'Cars'},
                     {'name': 'Traffic Arrows',
                      'thumb': 'http://www.vidsplay.com/vids/traffic_arrows.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic_arrows.mp4',
                      'genre': 'Cars'}
                     ],
            'Food': [{'name': 'Chicken',
                      'thumb': 'http://www.vidsplay.com/vids/chicken.jpg',
                      'video': 'http://www.vidsplay.com/vids/bbqchicken.mp4',
                      'genre': 'Food'},
                     {'name': 'Hamburger',
                      'thumb': 'http://www.vidsplay.com/vids/hamburger.jpg',
                      'video': 'http://www.vidsplay.com/vids/hamburger.mp4',
                      'genre': 'Food'},
                     {'name': 'Pizza',
                      'thumb': 'http://www.vidsplay.com/vids/pizza.jpg',
                      'video': 'http://www.vidsplay.com/vids/pizza.mp4',
                      'genre': 'Food'}
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
